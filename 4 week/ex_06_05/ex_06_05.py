str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
# print(ipos)
piece = str[ipos + 2:]
# print(piece)
# print(piece + 42.0)   // 오류 발생
value = float(piece)
print(value)
# print(value + 42.0)