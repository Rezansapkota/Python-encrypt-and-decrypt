'''
--------------------------
Group Name:DAN/EXT 14
1st Member:Rejan Sapkota(Student ID: s400142)
2nd Member:Saroj Dhakal(Student ID: s399846)
3rd Member:Raman Lamichhane(Student ID: s401547)
4th Member:Suraj Kandel(Student ID: s395871 )
--------------------------
'''
# Assignment 2 - Question 1

# shift character
def shift_char(c, shift, base):
    return chr((ord(c) - ord(base) + shift) % 26 + ord(base))


# encrypt text using the given assignment conditions
def encrypt_text(text, s1, s2):
    result = ""
# using if else conditions to check the encrypthon condition given in assignment rules
    for c in text:
        if 'a' <= c <= 'm':
            result += shift_char(c, s1 * s2, 'a')
        elif 'n' <= c <= 'z':
            result += shift_char(c, -(s1 + s2), 'a')
        elif 'A' <= c <= 'M':
            result += shift_char(c, -s1, 'A')
        elif 'N' <= c <= 'Z':
            result += shift_char(c, s2 ** 2, 'A')
        else:
            result += c

    return result


# decrypt text according to the conditions provided in assignment (try all possibilities)
def decrypt_text(text, s1, s2):
    result = ""

    for c in text:
        found = False

        # check lowercase
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if 'a' <= ch <= 'm':
                temp = shift_char(ch, s1 * s2, 'a')
            else:
                temp = shift_char(ch, -(s1 + s2), 'a')

            if temp == c:
                result += ch
                found = True
                break

        if found:
            continue

        # check uppercase
        for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if 'A' <= ch <= 'M':
                temp = shift_char(ch, -s1, 'A')
            else:
                temp = shift_char(ch, s2 ** 2, 'A')

            if temp == c:
                result += ch
                found = True
                break

        if found:
            continue

        # keep symbols
        result += c

    return result


# verify files
def verify(f1, f2):
    with open(f1, "r") as a, open(f2, "r") as b:
        if a.read() == b.read():
            print("Decryption successful")
        else:
            print("Decryption failed")


# Error handeling 'prints: enter number only, if user try to enter any other things like alphabet in the shift value'
def main():
    # input
    while True:
        try:
            s1 = int(input("Enter shift1: "))
            s2 = int(input("Enter shift2: "))
            break
        except ValueError:
            print("Enter numbers only")

    # read file 'raw_text.txt'
    try:
        with open("raw_text.txt", "r") as f:
            text = f.read()
    except FileNotFoundError:
        print("File not found")
        return

    # encrypt
    enc = encrypt_text(text, s1, s2)
    with open("encrypted_text.txt", "w") as f:
        f.write(enc)

    # decrypt
    dec = decrypt_text(enc, s1, s2)
    with open("decrypted_text.txt", "w") as f:
        f.write(dec)

    # verify
    verify("raw_text.txt", "decrypted_text.txt")


main()

'''
*** Some shift combination create overlapping mappings, so decryption may not recover the original text.***
 '''