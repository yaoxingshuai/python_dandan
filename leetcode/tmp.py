words = ["gin", "zen", "gig", "msg"]
D = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
     "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

for word in words:
    output = ''
    for c in word:
        output += D[ord(c) - ord('a')]
    print(output)

cc = 'a'
dd = dict()

for morse_code in D:
    dd[cc] = morse_code
    cc = chr(ord(cc) + 1)
print(dd)

for word in words:
    output = ''
    for c in word:
        output += dd[c]
    print(output)

print('----------------------------')

for word in words:
    output = ''.join(D[ord(c)-ord('a')] for c in word)
    print(output)
