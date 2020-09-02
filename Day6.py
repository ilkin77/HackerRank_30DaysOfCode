s = int(input())
One = ""
Two = ""
for x in range(s):
    S= input()
    for k in range(len(S)):
        if k % 2 == 0:
            One += S[k]
        else:
            Two += S[k]
    print(One,Two)
    One=""
    Two = ""