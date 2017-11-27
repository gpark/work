# Complete the function below.
def  decrypt(encrypted_message):
    key = "8251220"
    messageEnd = len(encrypted_message) - 1
    keyEnd = len(key) - 1
    mi = messageEnd
    ki = keyEnd
    adj = ''
    while (mi > - 1):
        if (encrypted_message[mi].isalpha()):
            adj = DecrementCharacter(encrypted_message[mi], key[ki]) + adj
            ki = ki - 1
            if (ki < 0):
                ki = keyEnd
        else:
            adj = encrypted_message[mi] + adj
        mi = mi - 1
    return adj

def DecrementCharacter(character, amount):
    upper = character.isupper()
    a = ord('a')
    value = ord(character.lower()) - int(amount)
    if (value < a):
        value = value + 26
    if (upper):
        return chr(value).upper()
    return chr(value)

message = 'Otjfvknou kskgnl, K mbxg iurtsvcnb ksgq hoz atv. Vje xcxtyqrl vt ujg smewfv vrmcxvtg rwqr ju vhm ytsf elwepuqyez. -Atvt hrqgse, Cnikg'
print(decrypt(message)) # Greetings friend, I have important info for you. The password to the secret treasure room is the word clocktower. -Your friend, Alice
#the first message is printed wrong and I don't know why
message2 = 'Bjj rwkcs dwpyp fwz ovors wxjs vje tcez fqg'
print(decrypt(message2)) # The quick brown fox jumps over the lazy dog
#the second one is printed right
