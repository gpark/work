•	Hacking Time 
Twitter Interview Online Test 

Alice and Bob are avid Twitter users and tweet to each other every day. One day, Alice decides to send Bob a secret message by encrypting it and tweeting it publicly to Bob. They had anticipated a scenario like this, and exchanged a shared secret key some time in the past. Unfortunately, Alice isn’t very familiar with encryption algorithms, so she decides to make her own. Her encryption algorithm works as follows: 
1. Choose a key entirely composed of digits 0 - 9, for example: 12345. 
2. Iterate each letter of the plaintext message and rotate the letter forward a number of times equal to the corresponding digit in the key. If the rotation of the letter passes Z, start back at A. 
3. If the message is longer than the key, loop back to the first digit of the key again, as many times as needed. 
4. If a non-alphabetical character is encountered, leave it as it is and don’t move to the next digit in the key. 
5. Characters should maintain their upper or lowercase orientation after rotation. 

Here is an example message and its encrypted output using Alice’s algorithm: 
Original message: Hi, this is an example 
Example Key: 4071321 
Encrypted message: Li, ailu jw facntll 

Where H was rotated forward 4 letters to L, i rotated 0 to i, t rotated forward 7 letters to a, etc. 

Satisfied with the security of her algorithm, Alice tweets the following ciphertext to Bob: 
Otjfvknou kskgnl, K mbxg iurtsvcnb ksgq hoz atv. Vje xcxtyqrl vt ujg smewfv vrmcxvtg rwqr ju vhm ytsf elwepuqyez. -Atvt hrqgse, Cnikg 

Uh oh! Unfortunately for Alice and Bob, you are “Eve”, the world’s greatest hacker. You’ve been intercepting Alice’s messages for some time now, and know she always ends her messages with the signature “-Your friend, Alice”. You job is now as follows: 

Determine the key Alice is using. 
Using this key, write a function to decrypt any future communications from Alice. This method should take the encrypted string as an input and return the original unencrypted string.
