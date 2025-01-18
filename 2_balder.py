length = int (input("Hur lång är du? (ange längd i cm): "))
if length < 130:
    print("Tyvärr... Du får inte åka!")
elif length >= 130:
    print("Grattis! Du får åka!")
else:
    print("Nu blev nånting fel!")
