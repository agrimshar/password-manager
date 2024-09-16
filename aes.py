# Encryption and decryption functions for AES

from lookup import *

'''
Encryption consists of applying a key, substiuting bytes, shifting rows, mixing columns.
1. Apply the key
2. Substitute bytes
3. Shift rows
4. Mix columns
'''

# Substitute bytes
def subBytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = SBOX[state[i][j]]
    return state

# Inverse substitute bytes
def invSubBytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = INVSBOX[state[i][j]]
    return state

# Shift rows 
def shiftRows(state):
    for i in range(4):
        state[i] = state[i][i:] + state[i][:i]
    return state

# Inverse shift rows
def invShiftRows(state):
    for i in range(4):
        state[i] = state[i][-i:] + state[i][:-i]
    return state

# Mix columns
def mixColumns(state):
    for i in range(4):
        a = state[i][0]
        b = state[i][1]
        c = state[i][2]
        d = state[i][3]

        state[i][0] = mulBy2[a] ^ mulBy3[b] ^ c ^ d
        state[i][1] = a ^ mulBy2[b] ^ mulBy3[c] ^ d
        state[i][2] = a ^ b ^ mulBy2[c] ^ mulBy3[d]
        state[i][3] = mulBy3[a] ^ b ^ c ^ mulBy2[d]
    return state

# Inverse mix columns
def invMixColumns(state):
    for i in range(4):
        a = state[i][0]
        b = state[i][1]
        c = state[i][2]
        d = state[i][3]

        state[i][0] = mulBy14[a] ^ mulBy11[b] ^ mulBy13[c] ^ mulBy9[d]
        state[i][1] = mulBy9[a] ^ mulBy14[b] ^ mulBy11[c] ^ mulBy13[d]
        state[i][2] = mulBy13[a] ^ mulBy9[b] ^ mulBy14[c] ^ mulBy11[d]
        state[i][3] = mulBy11[a] ^ mulBy13[b] ^ mulBy9[c] ^ mulBy14[d]
    return state

# Add round key
def addRoundKey(state, key):
    for i in range(4):
        for j in range(4):
            state[i][j] ^= key[i][j]
    return state

# Key expansion
def keyExpansion(key: list, rounds: int):
    expandedKey = key
    for i in range(4, 4*(rounds+1)):
        temp = expandedKey[i-1]
        if i % 4 == 0:
            temp = [SBOX[j] for j in temp]
            temp = [temp[1], temp[2], temp[3], temp[0]]
            temp[0] ^= RCON[i//4]
        expandedKey.append([expandedKey[i-4][j] ^ temp[j] for j in range(4)])
    return expandedKey

# Encryption
def encrypt(state, expandedKey: list, rounds: int):
    addRoundKey(state, expandedKey[:4])
    for i in range(1, rounds):
        subBytes(state)
        shiftRows(state)
        mixColumns(state)
        addRoundKey(state, expandedKey[i*4:(i+1)*4])
    subBytes(state)
    shiftRows(state)
    addRoundKey(state, expandedKey[rounds*4:])
    return state

'''
Decryption consists of inverse mixing the columns, inverse shifting the rows, inversie substituting bytes, and applying the key
1. Inverse mix columns
2. Inverse shift rows
3. Inverse substitute bytes
4. Apply the key
'''

# Decryption
def decrypt(state, expandedKey: list, rounds: int):
    addRoundKey(state, expandedKey[rounds*4:])
    for i in range(rounds-1, 0, -1):
        invShiftRows(state)
        invSubBytes(state)
        addRoundKey(state, expandedKey[i*4:(i+1)*4])
        invMixColumns(state)
    invShiftRows(state)
    invSubBytes(state)
    addRoundKey(state, expandedKey[:4])
    return state