def upperCase(text):
    return text.upper()


def lenStr(text):
    for c in text:
        print(c)    
    # return x
lenStr('hello world')

def findChar(text, char):
    for x in range(0, len(text)):
        if text[x] == char:
            # print(f"{text[x]} == {char}", text[x] == char)
            # print(f"x={x}")
            return x

print(findChar(text='hello world', char='w'))