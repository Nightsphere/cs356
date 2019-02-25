from subprocess import Popen, PIPE, STDOUT
import sys
import re

def encrypt_with_bc(e, n, key_1, key_2):
    
    # Using the ord function, we go through both keys and assign each letter with
    # an ascii value
    key_1_ascii = [ord(c) for c in key_1]
    key_2_ascii = [ord(c) for c in key_2]

    mod = '%'
    to_the = '^'

    # We're making a list for each line that we're printing to the file later
    m_ascii_key_1 = []
    m_ascii_space = []
    m_ascii_key_2 = []

    # Now it's time to go through the key lists and use each ascii number as 'm'
    # We're using the function c = m^e%n, where c is the ciphertext of the ascii value
    for m in key_1_ascii:
        p = Popen(['bc'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        encode_e_n  = "{} {} {} {} {}\n".format(m, to_the, e, mod, n).encode('utf-8')
        stdout_data = p.communicate(input=encode_e_n)[0]
        m_ascii_key_1.append(stdout_data.decode('utf-8')[:-1])
        print('.', end = '', flush = True)

    m = ' '
    space = ord(m)
    p = Popen(['bc'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    encode_e_n  = "{} {} {} {} {}\n".format(space, to_the, e, mod, n).encode('utf-8')
    stdout_data = p.communicate(input=encode_e_n)[0]
    m_ascii_space.append(stdout_data.decode('utf-8')[:-1])
    print('.', end = '', flush = True)

    for m in key_2_ascii:
        p = Popen(['bc'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        encode_e_n  = "{} {} {} {} {}\n".format(m, to_the, e, mod, n).encode('utf-8')
        stdout_data = p.communicate(input=encode_e_n)[0]
        m_ascii_key_2.append(stdout_data.decode('utf-8')[:-1])
        print('.', end = '', flush = True)

    print()
    return m_ascii_key_1, m_ascii_space, m_ascii_key_2

def read_keys(key_file):
    rfile = open(key_file, "r")
    keys = rfile.read()
    keys = re.split('\W+', keys)
    rfile.close()
    return keys[0], keys[1]

# For some reason, write a key on one line, a space on the next one, and the second
# key on the third line
def write_wrapped_keys(wrapped_keys):
    with open("wrappedKeys", "w") as wfile:
        index_counter = 0
        for ascii in range(10):
            wfile.write("%s " % wrapped_keys[index_counter])
            index_counter = index_counter + 1
        wfile.write('\n')
        wfile.write("%s " % wrapped_keys[index_counter])
        index_counter = index_counter + 1
        wfile.write('\n')
        for ascii in range(10):
            wfile.write("%s " % wrapped_keys[index_counter])
            index_counter = index_counter + 1
        wfile.write('\n')

# Where it all starts. We're wrapping the transposition keys using RSA asymmetric
# encryption to better protect them
def main():
    
    # Let the user know that encryption has begun
    print("\n>>> Encrypting keys..")

    # Open the public key file and read them into variables
    public_key_1, public_key_2 = read_keys("publicKey")

    # Open the regular key file and read them into two more variables
    key_1, key_2 = read_keys("keys.txt")

    # Convert the public keys into numbers so we can math them
    e = int(public_key_1)
    n = int(public_key_2)
    
    # Call our encrypt function for each key
    encrypted_key_1, encrypted_space, encrypted_key_2 = encrypt_with_bc(e, n, key_1, key_2)

    # Combine the lists
    fully_encrypted_keys = encrypted_key_1 + encrypted_space + encrypted_key_2

    # Now write the keys to the wrappedKeys file
    write_wrapped_keys(fully_encrypted_keys)

    print(">>> Encryption of keys successful!\n")

if __name__ == '__main__':
    main()
