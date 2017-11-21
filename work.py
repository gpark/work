# Complete the function below.

def  decrypt(encrypted_message):
     key = FindKey(encrypted_message,'-Your friend, Alice')
     return DecryptMessage(encrypted_message, key)

# get the delta between the two characters
def CharacterDelta(actualChar, forwardedChar):
    lca = actualChar.lower()
    lcb = forwardedChar.lower()
    delta = ord(lcb)-ord(lca)
    if (delta < 0):
        delta = delta + 26
    return delta

# finds the key substring in the decrypted section of the known text
# because the known text may have a repeated key in it
def FindSubKey(key):
    end = len(key) - 1
    keySize = int((len(key)/2))

    while (keySize > 3):
        if (IsSubKey(key, keySize)):
            return key[-keySize:]

    return 'Unknown'

# walks backwards to determine if a substring of keysize exists in key
def IsSubKey(key, keySize):
    end = len(key) - 1
    endPtr = end
    ptr = len(key) - 1 - keySize

    while (endPtr > keySize and key[endPtr] == key[ptr]):
        ptr = ptr - 1
        endPtr = endPtr - 1

    return endPtr == keySize and key[endPtr] == key[ptr]


# knownText goes from the right of the encryptedText backward
def FindKey(encryptedText, knownText):
    encryptEnd = len(encryptedText) - 1
    knownEnd = len(knownText) - 1

    kwni = knownEnd
    enci = encryptEnd

    key = ''
    while (kwni > -1):
        if (knownText[kwni].isalpha()):
            key = str(CharacterDelta(knownText[kwni], encryptedText[enci])) + key

        kwni = kwni - 1
        enci = enci - 1

    # now check if the key has is a substring
    return FindSubKey(key)

# increments a character by an amount and wraps back to the beginning as needed
def DecrementCharacter(character, amount):
    upper = character.isupper()

    a = ord('a')
    value = ord(character.lower()) - int(amount)
    if (value < a):
        value = value + 26

    if (upper):
        return chr(value).upper()

    return chr(value)

# once a key is found, decrypt the message using the key
def DecryptMessage(message, key):
    messageEnd = len(message) - 1
    keyEnd = len(key) - 1

    mi = messageEnd
    ki = keyEnd

    adj = ''
    while (mi > - 1):
        if (message[mi].isalpha()):
            adj = DecrementCharacter(message[mi], key[ki]) + adj
            ki = ki - 1
            if (ki < 0):
                ki = keyEnd
        else:
            adj = message[mi] + adj
        mi = mi - 1
    return adj

message = 'Otjfvknou kskgnl, K mbxg iurtsvcnb ksgq hoz atv. Vje xcxtyqrl vt ujg smewfv vrmcxvtg rwqr ju vhm ytsf elwepuqyez. -Atvt hrqgse, Cnikg'
print(decrypt(message))
message2 = 'Bjj rwkcs dwpyp fwz ovors wxjs vje tcez fqg'
print(decrypt(message2))
