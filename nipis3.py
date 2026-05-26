def cek_kurung(ekspresi):
    stack = []

    pasangan = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for karakter in ekspresi:

        if karakter in "([{":
            stack.append(karakter)

        elif karakter in ")]}":

            if len(stack) == 0:
                return False

            atas = stack.pop()

            if atas != pasangan[karakter]:
                return False

    return len(stack) == 0


ekspresi = input("Masukkan ekspresi: ")

if cek_kurung(ekspresi):
    print("Valid")
else:
    print("Tidak Valid")