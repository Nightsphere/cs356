from subprocess import Popen, PIPE, STDOUT
import sys
import re

def encrypt_with_bc(e, n, key_1, key_2):
    
    key_1_ascii = [ord(c) for c in key_1]
    key_2_ascii = [ord(c) for c in key_2]

    mod = '%'
    to_the = '^'

    m_ascii_key_1 = []
    m_ascii_key_2 = []

    

    # Now it's time to go through the key lists and use each ascii number as 'm'
    for m in key_1_ascii:
        p = Popen(['bc'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        encode_e_n  = "{} {} {} {} {}\n".format(m, to_the, e, mod, n).encode('utf-8')
        stdout_data = p.communicate(input=encode_e_n)[0]
        m_ascii_key_1.append(stdout_data.decode('utf-8')[:-1])

    for m in key_2_ascii:
        p = Popen(['bc'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        encode_e_n  = "{} {} {} {} {}\n".format(m, to_the, e, mod, n).encode('utf-8')
        stdout_data = p.communicate(input=encode_e_n)[0]
        m_ascii_key_2.append(stdout_data.decode('utf-8')[:-1])

    return m_ascii_key_1, m_ascii_key_2

def read_keys(key_file):
    rfile = open(key_file, "r")
    keys = rfile.read()
    keys = re.split('\W+', keys)
    return keys[0], keys[1]

def main():
    
    # Open the public key file and read them into variables
    public_key_1, public_key_2 = read_keys("publicKey")

    # Open the regular key file and read them into two more variables
    key_1, key_2 = read_keys("keys.txt")

    # Convert the public keys into numbers so we can math them
    e = int(public_key_1)
    n = int(public_key_2)
    
    # Call our encrypt function for each key
    encrypted_key_1, encrypted_key_2 = encrypt_with_bc(e, n, key_1, key_2)

    # Now we can write 

if __name__ == '__main__':
    main()
