from aes import subBytes, invSubBytes, shiftRows, invShiftRows

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