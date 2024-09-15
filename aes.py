# Encryption and decryption functions for AES

from lookup import SBOX, INVSBOX

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


# Encryption
def encrypt(state, expandedKey: list, rounds: int):
    return 0

'''
Decryption consists of inverse mixing the columns, inverse shifting the rows, inversie substituting bytes, and applying the key
1. Inverse mix columns
2. Inverse shift rows
3. Inverse substitute bytes
4. Apply the key
'''

# Decryption
def decrypt(state, expandedKey: list, rounds: int):
    return 0