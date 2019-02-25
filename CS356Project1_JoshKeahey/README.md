# Project 1: Study of Cryptographic Techniques

This security program was created by Josh Keahey and does the following:

 - Two programs that implement the transposition cipher.

    1. The first program will be used to encrypt plaintext into ciphertext
        * This encrypts the plaintext by using the double transposition
        method using two keys given by the user

    2. The second program will convert the ciphertext back into plaintext
        * This decrypts by doing the double transposition method backwards

    3. The third program uses RSA assymetric encryption
        * This will 'wrap' the two keys provided by the user earlier so that
        when they are sent to the receiver, they are protected on the way

    4. The fourth program will decrypt the encrypted keys
        * This will use the private key of the recepient to decrypt the wrapped
        keys by unwrapping them and printing them to a 

### Running the program

 - To run this program, you will type a total of 4 commands

 - Before this is done however, the AlicePlainText.txt file needs to be filled
    with the sentence that needs to be encrypted! Using your favorite editor, type
    in the sentence and save it

 - A quick note, I'm assuming this program will be run on the computer science machines
    in the CSB, so the python command I will give below will be catered towards that by 
    using `python3`. If used on a computer where python 3 is the default compiler 
    (interpreter?), like the one I used to create this program, just using `python` 
	will work fine.

    1. Type in the command
            `python3 transposition-encr.py`
        and follow the prompts for assigning the two keys and supplying the 
        AlicePlainText.txt file for starting the double transposition cipher

    2. After that, type the command
            `python3 asymmetrickey_encr.py`
        to wrap the keys you gave with the RSA encryption. This will take about
        10 seconds to complete

    3. Now that the keys are wrapped, type in the command
            `python3 asymmetrickey_decr.py`
        so that the recipient of the wrapped keys can decrypt them. Fairly large
        prime numbers were chosen, so this will take about 1 minute and 5 seconds

    4. Lastly, type in the command
            `python3 transposition-decr.py`
        so we can take the newly decrypted keys and use them to determine what the
        original message sent is by looking at BobPlainText.txt

And that's it! Alice and Bob can now send each other messages while feeling somewhat
confident that their messages (and the keys used to encrypt and decrypt those messages)
are safe from others who would do them harm in whatever country Bob is in
