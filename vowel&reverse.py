name=raw_input("")
vowels= ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U')

for i in name:

    if i in vowels:

        name = name.replace(i, '')

print name[::-1]
