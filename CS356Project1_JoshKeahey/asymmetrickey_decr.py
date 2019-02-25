# This import is for calling bc using this python script
from subprocess import Popen, PIPE, STDOUT
# This import of re is for using regex to cut out white space when reading keys
import re

def decrypt_with_bc(d, n, wrapped_keys):

    mod = '%'
    to_the = '^'
    decrypted_keys = []

    # Now it's time to go through the wrapped key list and convert the numbers
    # back to ascii using the private key, d. We're using the function m = c^d%n,
    # where m is the plaintext letter of the keys
    for c in wrapped_keys:
        p = Popen(['bc'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        encode_e_n  = "{} {} {} {} {}\n".format(c, to_the, d, mod, n).encode('utf-8')
        stdout_data = p.communicate(input=encode_e_n)[0]
        decrypted_keys.append(stdout_data.decode('utf-8')[:-1])
        print('\u2630', end = '', flush = True)

    # Convert the ascii number back to letters using the chr function and return it
    decrypted_keys = [chr(int(c)) for c in decrypted_keys]
    print()
    
    return decrypted_keys

# This function will read in the file, and if it's private key, read d into the first
# variable and n into the second. If it's our wrapped keys, read the entire file in
def read_keys(key_file):
    
    rfile = open(key_file, "r")

    if key_file == "privateKey":
        keys = rfile.read()
        keys = re.split('\W+', keys)
        return keys[0], keys[1]
    else:
        return rfile.read().split()

# Write each letter to the file. These are the decrypted two keys needed
def write_unwrapped_keys(decrypted_keys):
    with open("unwrappedKeys", "w") as wfile:
        for letter in decrypted_keys:
            wfile.write("%s" % letter)

# This is where it all begins. Take the private keys along with the wrapped keys and
# ciphertext that was sent using the above functions
def main():

    # Let the user know the long and arduous process of decrypting has begun
    print("\n>>> Decrypting keys..")

    # Open the private key file and read them into variables
    private_key_1, private_key_2 = read_keys("privateKey")

    # Open the wrapped key file and read them into two more variables
    wrapped_keys = read_keys("wrappedKeys")

    # Convert the private keys into numbers so we can math them
    d = int(private_key_1)
    n = int(private_key_2)

    # Call our decrypt function for both keys in a list
    decrypted_keys = decrypt_with_bc(d, n, wrapped_keys)

    # Now write the original plaintext to the unwrappedKeys file
    write_unwrapped_keys(decrypted_keys)

    print(">>> Decryption of keys successful!\n")


if __name__ == '__main__':
    main()

