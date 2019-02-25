# This python script will take the encrypted message written to the AlicePlainText.txt file
# and decrypt it, writing the original message into another file

import numpy as np

# This function is what's called when we want to create a 2D matrix with either the
# plaintext of the matrix used to populate it
def create_matrix(sentence):

    # It's easier to make a variable for how many number of rows we'll need for
    # our sentence. The number of columns will always be 10
    number_of_rows = round(len(sentence)/10)

    # Make a dummy matrix with 0's that will be the size of the full matrix
    sentence_matrix = [[0 for col in range(10)] for row in range(number_of_rows)]

    return sentence_matrix

# Wnen we have our dummy sentence matrix filled with 0's, and our message, we
# can now populate the matrix with said message
def fill_matrix(sentence_matrix, message, key):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    key_word = [c for c in key]
    key_list = [0] * 10
    letter_2_number = 1

    for letter in alphabet:
        if letter in key_word:
            key_list[key_word.index(letter)] = letter_2_number
            letter_2_number = letter_2_number + 1

    letter_counter = 0
    index_counter = 1

    for col in range(10):
        for row in range(len(sentence_matrix)):
            sentence_matrix[row][key_list.index(index_counter)] = message[letter_counter]
            letter_counter = letter_counter + 1
        index_counter = index_counter + 1

    return ''.join(str(letter) for col in sentence_matrix for letter in col)

# Read the file that contains Alice's ciphertext
def read_message():
    rfile = open("AliceCipherText.txt", "r")
    message = rfile.read()
    rfile.close()
    return message

# Read in our two keys that was previously used to encrypt the incoming message
def read_keys():
    rfile = open("unwrappedKeys", "r")
    keys = rfile.read()
    keys = keys.split()
    rfile.close()
    return keys[0], keys[1]

# Where it all happens
def main():

    # Open Bob's plain text file so we can write to it when we are finished
    plaintext_file = open("BobPlainText.txt","w")

    # Read the 2 keys in and assign them accordingly
    key_1, key_2 = read_keys()

    # Read in the encrypted message
    encrypted_message = read_message()

    # Create our dummy 2D list with all 0's for now. Pass in our message so we can use
    # it to determine how many rows our matrix will have
    sentence_matrix = create_matrix(encrypted_message)

    # Populate the matrix with the encrypted message going left to right, top to bottom
    # and return the string of the first decrypted sentence using the second key first
    first_decryption = fill_matrix(sentence_matrix, encrypted_message, key_2)

    # Now enter the first decrypted sentence as a parameter to get the original message
    # But first, recreate the sentence matrix as a dummy matrix that contains all zeros again
    plaintext = fill_matrix(sentence_matrix, first_decryption, key_1)

    # Write the plaintext to Bob's file
    plaintext_file.write(plaintext)

    print("\n>>> Message received!\n")

if __name__ == '__main__':
    main()
