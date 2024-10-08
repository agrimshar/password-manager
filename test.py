from aes import subBytes, invSubBytes, shiftRows, invShiftRows, mixColumns, invMixColumns, encrypt, decrypt

# Test subBytes and invSubBytes
# def testSubBytes():
#     state = [
#         [0x32, 0x88, 0x31, 0xe0],
#         [0x43, 0x5a, 0x31, 0x37],
#         [0xf6, 0x30, 0x98, 0x07],
#         [0xa8, 0x8d, 0xa2, 0x34]
#     ]
#     print("Original state:")
#     for row in state:
#         print(row)
#     print("\nSubstituted state:")
#     subBytes(state)
#     for row in state:
#         print(row)
#     print("\nInverse substituted state:")
#     invSubBytes(state)
#     for row in state:
#         print(row)

# testSubBytes()

# Test shiftRows and invShiftRows
# def testShiftRows():
#     state = [
#         [0x32, 0x88, 0x31, 0xe0],
#         [0x43, 0x5a, 0x31, 0x37],
#         [0xf6, 0x30, 0x98, 0x07],
#         [0xa8, 0x8d, 0xa2, 0x34]
#     ]
#     print("Original state:")
#     for row in state:
#         print(row)
#     print("\nShifted state:")
#     shiftRows(state)
#     for row in state:
#         print(row)
#     print("\nInverse shifted state:")
#     invShiftRows(state)
#     for row in state:
#         print(row)

# testShiftRows()

# Test mixColumns and invMixColumns
# def testMixColumns():
#     state = [
#         [0x32, 0x88, 0x31, 0xe0],
#         [0x43, 0x5a, 0x31, 0x37],
#         [0xf6, 0x30, 0x98, 0x07],
#         [0xa8, 0x8d, 0xa2, 0x34]
#     ]
#     print("Original state:")
#     for row in state:
#         print(row)
#     print("\nMixed state:")
#     mixColumns(state)
#     for row in state:
#         print(row)
#     print("\nInverse mixed state:")
#     invMixColumns(state)
#     for row in state:
#         print(row)

# testMixColumns()

# Test encrypt and decrypt
def testEncryptDecrypt():
    key = [
        [0x2b, 0x28, 0xab, 0x09],
        [0x7e, 0xae, 0xf7, 0xcf],
        [0x15, 0xd2, 0x15, 0x4f],
        [0x16, 0xa6, 0x88, 0x3c]
    ]
    state = [
        [0x32, 0x88, 0x31, 0xe0],
        [0x43, 0x5a, 0x31, 0x37],
        [0xf6, 0x30, 0x98, 0x07],
        [0xa8, 0x8d, 0xa2, 0x34]
    ]
    print("Original state:")
    for row in state:
        print(row)
    print("\nEncrypted state:")
    encrypt(state, key, 10)
    for row in state:
        print(row)
    print("\nDecrypted state:")
    decrypt(state, key, 10)
    for row in state:
        print(row)

testEncryptDecrypt()