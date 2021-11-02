sparek = float(input("skriv inn saldo på sparekonto: "))

endring = input("vil du sette inn eller ta ut: ")
if endring in ("sette inn"):
    innskud = float(input("Hvor mye vil du sette inn "))
    sparek = sparek + innskud
else:
    uttak = float(input("hvor mye vil du ta ut: "))
    sparek = sparek - uttak
print("ny saldo er %d kr" %sparek)