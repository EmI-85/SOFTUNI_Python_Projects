string1 = input()
string2 = input()
new_string = ""

for i in range(1, len(string1) + 1):
    new_string = string2[:i] + string1[i:]
    if string1[i - 1] != string2[i - 1]:
        print(new_string)


