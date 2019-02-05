# This import was for using an ordered dictionary for removing duplicates from strings
# in the validate_key function
from collections import OrderedDict

# This function is what's called when we want to create a 2D matrix with either the
# plaintext or the ciphertext of the first matrix used to populate it
def create_matrix(sentence):

    # A sentence counter needs to be made so we can keep track of where we are in
    # the sentence we want to put into our list of lists
    sen_counter = 0 

    # It's easier to make a variable for how many number of rows we'll need for 
    # our sentence. The number of columns will always be 10
    number_of_rows = round(len(sentence)/10)

    # Make a dummy matrix with 0's that will be the size of the full matrix
    sentence_matrix = [[0 for col in range(10)] for row in range(number_of_rows)]

    for row in range(number_of_rows):
        for col in range(10):
            if sen_counter <= len(sentence) - 1:
                sentence_matrix[row][col] = sentence[sen_counter]
                sen_counter = sen_counter + 1 
            else:
                sentence_matrix[row][col] = 'x' 
            
    return sentence_matrix

# The actual encrypting of the plaintext. We read in the keys from the keys file, assign
# them to lists, and use those along with the sentence_matrix to write the ciphertext
def encrypt_message(sentence_matrix):
    
    # A string containing all 26 letters so we can assign each letter a number
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    key_file = open("keys.txt", "r")
    keys = key_file.read()

    # After we read the two strings into a variable, split on the space in the file and
    # assign the keys accordingly
    keys = keys.split()
    key_1 = keys[0]
    key_1 = [c for c in key_1]

    key_1_list = [0] * 10
    letter_2_number = 1
    for letter in alphabet:
        if letter in key_1:
            key_1_list[key_1.index(letter)] = letter_2_number
            letter_2_number = letter_2_number + 1

    print(key_1_list)

    # TODO: ENCRYPT KEY 2 AFTER KEY 1!
    key_2 = keys[1]
    key_2 = [c for c in key_2]

def retrieve_plaintext():

    print("\n>>> Both keys have been validated. Please provide the name of the one")
    print(">>> sentence text file you would like encrypted")
    file_to_encrypt = input(">>> File name: ")

    myfile = open(file_to_encrypt, "r")
    contents = myfile.read()

    # This beautiful line reads all but the '\n' character into the sentence variable
    # and then replaces all whitespace with nothing, so we can populate our 2D list
    sentence = "".join(contents[:len(contents) - 1].split())

    # This is the finished 2D matrix with the sentence we want to encrypt residing in it
    sentence_matrix = create_matrix(sentence)

    encrypt_message(sentence_matrix)
    

# This function takes a key string and determines if the given key is usable
def validate_key(key):

    # Check to see if the key contains characters that aren't letters.
    if key.isalpha():
        pass
    else:
        return 1

    # Convert the key given to all lower case
    new_key = key.lower()

    # This next line takes the new lower case version of the string given and
    # deletes duplicate letters by joining them with '', printing only one of each
    new_key = "".join(OrderedDict.fromkeys(new_key))

    # Now check to see if the string is less than 10 characters
    if len(new_key) > 9:
        pass
    else:
        return 2

    # If everything else looks good, return the new and improved key
    return new_key[0:10]
    
    
# This function takes in the keys typed by the user and writes them to a file
def get_keys():

    # This key variable lets us know which key is currently being generated
    key = 1

    print("\n>>> Please enter two 10 character keys")
    print(">>> No special characters, and no duplicate letters can be used in one key")

    # This while loop makes sure that we only at most make two successful keys
    while key <= 2:

        # This makes sure we keep pestering the user forever until they provide us
        # with keys that will work for the encryption
        while True:
            
            key_1 = input("\n>>> Key %d: " % key)

            validated_key = validate_key(key_1)

            if validated_key == 1:
                print(">>> The key you've entered contains a character that is not a")
                print(">>> letter in the alphabet. Please enter a legal key")
            elif validated_key == 2:
                print(">>> The key you've entered is less than 10 characters, possibly")
                print(">>> due to the deletion of duplicate letters and special characters")
                print(">>> Please enter a legal key")
            else:
                print(">>> Key %d approved as \"%s\"" % (key, validated_key))

                # Write the key to the keys.txt file
                if key == 1:
                    key_file = open("keys.txt", "w")
                    key_file.write(validated_key + " ")
                else:
                    key_file = open("keys.txt", "a")
                    key_file.write(validated_key)

                # Make sure to add one to key so we ask for the second key
                key = key + 1

                # Don't forget to close the file!
                key_file.close()

                # Break out of the always true while loop, since the key has been validated
                # and we can now move onto the next key
                break


# This is the main function and calls the get_keys function for receiving the keys
def main():
    get_keys()
    retrieve_plaintext()

if __name__ == '__main__':
    main()
