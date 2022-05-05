  1. # Public Key Cipher
  2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
  3.
  4. import sys, math
  5.
  6. # The public and private keys for this program are created by
  7. # the makePublicPrivateKeys.py program.
  8. # This program must be run in the same folder as the key files.
  9.
 10. SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345
       67890 !?.'
 11.
 12. def main():
 13.     # Runs a test that encrypts a message to a file or decrypts a message
 14.     # from a file.
 15.     filename = 'encrypted_file.txt' # The file to write to/read from.
 16.     mode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.
 17.
 18.     if mode == 'encrypt':
 19.         message = 'Journalists belong in the gutter because that is where
               the ruling classes throw their guilty secrets. Gerald Priestland.
               The Founding Fathers gave the free press the protection it must
               have to bare the secrets of government and inform the people.
               Hugo Black.'
 20.         pubKeyFilename = 'al_sweigart_pubkey.txt'
 21.         print('Encrypting and writing to %s...' % (filename))
 22.         encryptedText = encryptAndWriteToFile(filename, pubKeyFilename,
               message)
 23.
 24.         print('Encrypted text:')
 25.         print(encryptedText)
 26.
 27.     elif mode == 'decrypt':
 28.         privKeyFilename = 'al_sweigart_privkey.txt'
 29.         print('Reading from %s and decrypting...' % (filename))
 30.         decryptedText = readFromFileAndDecrypt(filename, privKeyFilename)
 31.
 32.         print('Decrypted text:')
 33.         print(decryptedText)8
 34.
 35.
 36. def getBlocksFromText(message, blockSize):
 37.     # Converts a string message to a list of block integers.
 38.     for character in message:
 39.         if character not in SYMBOLS:
 40.             print('ERROR: The symbol set does not have the character %s' %
                   (character))
 41.             sys.exit()
 42.     blockInts = []
 43.     for blockStart in range(0, len(message), blockSize):
 44.         # Calculate the block integer for this block of text:
 45.         blockInt = 0
 46.         for i in range(blockStart, min(blockStart + blockSize,
               len(message))):
 47.             blockInt += (SYMBOLS.index(message[i])) * (len(SYMBOLS) **
                   (i % blockSize))
 48.         blockInts.append(blockInt)
 49.     return blockInts
 50.
 51.
 52. def getTextFromBlocks(blockInts, messageLength, blockSize):
 53.     # Converts a list of block integers to the original message string.
 54.     # The original message length is needed to properly convert the last
 55.     # block integer.
 56.     message = []
 57.     for blockInt in blockInts:
 58.         blockMessage = []
 59.         for i in range(blockSize - 1, -1, -1):
 60.             if len(message) + i < messageLength:
 61.                 # Decode the message string for the 128 (or whatever
 62.                 # blockSize is set to) characters from this block integer:
 63.                 charIndex = blockInt // (len(SYMBOLS) ** i)
 64.                 blockInt = blockInt % (len(SYMBOLS) ** i)
 65.                 blockMessage.insert(0, SYMBOLS[charIndex])
 66.         message.extend(blockMessage)
 67.     return ''.join(message)
 68.
 69.
 70. def encryptMessage(message, key, blockSize):
 71.     # Converts the message string into a list of block integers, and then
 72.     # encrypts each block integer. Pass the PUBLIC key to encrypt.
 73.     encryptedBlocks = []
 74.     n, e = key
 75.
 76.     for block in getBlocksFromText(message, blockSize):
 77.         # ciphertext = plaintext ^ e mod n
 78.         encryptedBlocks.append(pow(block, e, n))
 79.     return encryptedBlocks
 80.
 81.
 82. def decryptMessage(encryptedBlocks, messageLength, key, blockSize):
 83.     # Decrypts a list of encrypted block ints into the original message
 84.     # string. The original message length is required to properly decrypt
 85.     # the last block. Be sure to pass the PRIVATE key to decrypt.
 86.     decryptedBlocks = []
 87.     n, d = key
 88.     for block in encryptedBlocks:
 89.         # plaintext = ciphertext ^ d mod n
 90.         decryptedBlocks.append(pow(block, d, n))
 91.     return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)
 92.
 93.
 94. def readKeyFile(keyFilename):
 95.     # Given the filename of a file that contains a public or private key,
 96.     # return the key as a (n,e) or (n,d) tuple value.
 97.     fo = open(keyFilename)
 98.     content = fo.read()
 99.     fo.close()
100.     keySize, n, EorD = content.split(',')
101.     return (int(keySize), int(n), int(EorD))
102.
103.
104. def encryptAndWriteToFile(messageFilename, keyFilename, message,
       blockSize=None):
105.     # Using a key from a key file, encrypt the message and save it to a
106.     # file. Returns the encrypted message string.
107.     keySize, n, e = readKeyFile(keyFilename)
108.     if blockSize == None:
109.         # If blockSize isn't given, set it to the largest size allowed by
               the key size and symbol set size.
110.         blockSize = int(math.log(2 ** keySize, len(SYMBOLS)))
111.     # Check that key size is large enough for the block size:
112.     if not (math.log(2 ** keySize, len(SYMBOLS)) >= blockSize):
113.         sys.exit('ERROR: Block size is too large for the key and symbol
               set size. Did you specify the correct key file and encrypted
               file?')
114.     # Encrypt the message:
115.     encryptedBlocks = encryptMessage(message, (n, e), blockSize)
116.
117.     # Convert the large int values to one string value:
118.     for i in range(len(encryptedBlocks)):
119.         encryptedBlocks[i] = str(encryptedBlocks[i])
120.     encryptedContent = ','.join(encryptedBlocks)
121.
122.     # Write out the encrypted string to the output file:
123.     encryptedContent = '%s_%s_%s' % (len(message), blockSize,
           encryptedContent)
124.     fo = open(messageFilename, 'w')
125.     fo.write(encryptedContent)
126.     fo.close()
127.     # Also return the encrypted string:
128.     return encryptedContent
129.
130.
131. def readFromFileAndDecrypt(messageFilename, keyFilename):
132.     # Using a key from a key file, read an encrypted message from a file
133.     # and then decrypt it. Returns the decrypted message string.
134.     keySize, n, d = readKeyFile(keyFilename)
135.
136.
137.     # Read in the message length and the encrypted message from the file:
138.     fo = open(messageFilename)
139.     content = fo.read()
140.     messageLength, blockSize, encryptedMessage = content.split('_')
141.     messageLength = int(messageLength)
142.     blockSize = int(blockSize)
143.
144.     # Check that key size is large enough for the block size:
145.     if not (math.log(2 ** keySize, len(SYMBOLS)) >= blockSize):
146.         sys.exit('ERROR: Block size is too large for the key and symbol
               set size. Did you specify the correct key file and encrypted
               file?')
147.
148.     # Convert the encrypted message into large int values:
149.     encryptedBlocks = []
150.     for block in encryptedMessage.split(','):
151.         encryptedBlocks.append(int(block))
152.
153.     # Decrypt the large int values:
154.     return decryptMessage(encryptedBlocks, messageLength, (n, d),
           blockSize)
155.
156.
157. # If publicKeyCipher.py is run (instead of imported as a module), call
158. # the main() function.
159. if __name__ == '__main__':
160.     main()