# Symmetric Encryption

Symmetric encryption ensures that all communication between two parties are kept confidential, if and only if, the two parties are the only ones with access to a shared private key. Symmetric encryption means that the encryption and decryption process of a communication channel established between two parties is accomplished utilizing one shared key.

### The Cryptography Triad
To ensure the communication between two parties is secure, the cryptography
being applied should consists of the following properties:
1. **Confidentiality**
    - Confidentiality ensures that the information being transferred between
      two communicating parties is kept secure. In symmetric encryption terms,
      this means only the two parties communicating should have access to the 
      shared key.
2. **Integrity**
    - Integrity checking ensures that the information being transferred between two
      communicating parties has not been tampered with. Just because the data
      between two parties is confidential does not mean an adversary
      cannot malicously manipulate the data.
3. **Authentication**
    - Authentication relates to verifying the identity of both communicating
      parties. It deals with answering the question, how do I know that the
      person I am communicating with is actaully the person I should be 
      communicating with.

### Block & Stream Ciphers
There are two subtypes of symmetric encryption algorithms: block ciphers and stream ciphers.
- Block ciphers work on chunks of data at any single point during the encrypting process. This means that passing large input data into a block cipher would mean that the data is broken down into block size chunks of data an encrypted as such until enough rounds of encryption have occured to have encrypted of the original data. **NOTE**: if you have a block cipher that encrypts 16 bytes of data per chunk, you must have plain text that is at least 16 bytes in length in order for the block cipher to perform a round of encryption. AES is an example of a symmetric encryption block cipher and it's one of the most secure encryption algorithms used today. AES is used in common protocols and services, including TLS, IPSec, file encryption. 
- Stream ciphers, unlike blocks ciphers, operate on a single byte of data throughout the entire encryption process. AES is awesome because it also can act of a stream cipher as well! RC4 was once a popular stream cipher but has been replaced with stream cipher offered by AES.

### The Advanced Encryption Standard
AES has a block size of 16-bytes and has several modes of operation:
1. Electronic Code Book (ECB)
    - **NOTE**: ECB should not used because it has major flaws. Every keyed input passed to the ECB cipher returns the same output. ECB does possess the *avalanche* property which says that a single change in the plaintext will result in nearly 50% change in the ciphertext. The problem with the avalanche propery becomes restricted by boundaries of each plaintext block. So, a change to the beginning of the plaintext will only impact the entropy of the first block size (of course this depends on the block size and how much of the beginning of the plaintext was altared).
2. Cipher Block Chaining (CBC)
    - CBC encrypts sequential block sizes by XORing the subsequent block's input with the ciphertext generated by the previous block. This means that the avalanche property in CBC is not limited to any given block, as in ECB, so no matter what block is altered, all subsequent blocks will also be altered. This dependence shared between every block is what really seperates the effectiveness of CBC from ECB. Because the encryption of all blocks rely on the ciphertext produced by the previous block, an initialization vector is XORed with the first block, and then all following blocks are XORed with the ciphertext of the previous block.
3. Counter mode (CTR)
    - CTR differs from ECB and CBC because it doesn't actually use AES for encryption or decrypting data. CTR works like a one-time pad (OTP) algorithm; it uses the XOR operator to disguise the contents of the original plaintext. The difference between a OTP and AES CTR is the key size used during the encryption and decryption process. A OTP must use a key the size of the plaintext in order for it to work while CTR uses AES and a counter to generate a key stream of variable length, the smallest possible key being 128 bits (16 bytes). CTR is a stream cipher, but can behave like a block cipher and easier to understand when analyzed as a block cipher. Because AES CTR is a stream cipher, no padding is needed. One disadvantage of stream ciphers though is that adversaries will have less trouble modifying the contents of ciphertext to their desires. This is because modifying any byte within the ciphertext generated by a stream cipher only corrupts that particular byte whereas any single byte modified in the ciphertext will cause the resulting ciphertext to be erroneously decrypted. AES CTR is recommended for more circumstances than AES CBC and **AES ECB SHOULD NEVER BE USED**! 
 
### An Effective Cipher
An effective cipher must produce different ciphertext for every time the same plaintext is passed into the cipher. This means that if "**x**" encrypts to "**ajfcdkcaadghtea313jfa**" the first time, "x" should not equal "ajfcdkcaadghtea313jfa" if "x" appears a second time in the plaintext. This is a major issue with ECB because every input that is the same will generate the same output each time. This means that if a particular value appears multiple times within the plaintext, you same ciphertext will appear repeatedly throughout the final ciphertext, minimizing the amount of effort needed to invert the ciphertext. This leads us to the second aspect of an effective cipher: no discernable patterns should exist between encrypted blocks. The more patterns evident within the ciphertext, the more likely the ciphertext will be vulnerable to *frequency analysis* and other cryptanalysis techniques.


### How Initialization Vectors Help Ensure Diverse Ciphertext
An initializtion vector (IV) is a third input, in addition to the key and the plaintext that is added to the cipher to ensure that the same plaintext will not result in the same ciphertext after encryption. The IV does not garantee confidentiality but does garantee that inputs are unique and non-repeatable no matter how similar the input is.

### XOR Truth Table
|x|y|output|
|---|---|---|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|

- when x = 0, output = y
- when x = 1, output = inverse(y)

(A ⊕ B) ⊕ B = A

### Padding
The *cryptography* module provides two mechanisms for padding plaintext, whose length does not meet the desired block size: **PKCS7** and **ANSI x.923**
- **PKCS7** appends *n* bytes to the block with each byte being the number of bytes need to fufil the block size. For example:
    - if the block size = 20; And the plaintext length is 16; PKCS7 will add 4 bytes -> "\x04\x04\x04\x04"
- **ANSI x.923** appends *n* bytes to the block with each byte, excluding the last, being 0. The value of the last block is the number of padding bytes needed.
    - if the block size is 20; And the plaintext length is 16; ANSI x.923 will add 4 bytes -> "\x00\x00\x00\x04"
    
### ECB vs CBC Image Encryption
- ECB Resulting Image

![ecb_image](images/ecb_image.png)

- CBC Resulting Image

![cbc_image](images/cbc_image.png)

### Key/IV Management
Reusing key's or IV's is certainly insecure. Every cryptographical cipher that requires a key, has it's own insecurities when reusing the same key or IV. Reusing key's can help adversaries decipher generated ciphertext because when using the same key, recognizable patterns will occur between plaintexts that contain similiar pieces of data. For example, encrypting an two different HTML pages with AES CBC with the same key will lead to patterns because of the similarities that HTML pages normally share such as HTML tags. With ciphers like AES CTR mode, reusing keys can be especially dangerous because the encryption is accomplished with the XOR operation. If an attacker has obtained plaintext messages that were also encrypted, they could easily recover the key by XORing the plaintext with the ciphertext because XOR is it's own inverse.

### Bypassing the Integrity of Ciphertext
AES-CTR is the most secure implementation of AES compared to AES-ECB and AES-CBC. AES-CTR garantees confidentiality is key's and IV's are not reused. But like all cryptographic ciphers, there is always a weakness to the implementation of any cryptographic algoritms. AES-CTR's weakness arises from being a stream cipher in conjunction with relying on XOR encryption. Because AES-CTR is a stream cipher, any change to a single byte of ciphertext will only result in the corruption of the corresponding plaintext. This differs from AES-CBC where a single modification at any point during the encryption process will result in the corruption of all subsequent blocks of data. If an adversary is tapped into a communication channel between two parties, they can easily recover keystream material by intercepting the ciphertexts and XORing it with known message content. By extracting the key, adversaries have the opportunity to encrypt a malicious message and insert into the section of the ciphertext where the original plaintexts is known. Of course, they are others technique that are used in combination with AES-CTR to provide the integrity that it is uncapable of providing.

### Key Randomness
Generating secure keys is dependent on true randomness. The built-in `random` module provided by Python is a pseudo-random number generator. The values generated by the `random` module are appear to random to the user but it actually generates a random number based on a particular seed value. The `random` module should not be used for secure implementatons of cryptography. Python 3.6 and above now comes with a new module called `secrets`. It provides a much more reliant random number generation algorithm. The `os.urandom` can also be trusted to provide strong randomness for cryptography keys.
