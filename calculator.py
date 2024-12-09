import math

memory = "empty!"
memory2 = "empty!"
memory3 = "empty!"
memory4 = "empty!"
number1 = 0
number2 = 0
while True:
    operator = input(
        "What operation do you want? Type A for addition, S for Subtraction, M for multiplication, and D for division. Type E for exponents, R for Roots, F for factorials, Mod for Modular stuff, Log for Log, Sin/Cos/tan do what you expect them to do (in radians). Press Q to quit and CMD for more commands. "
    )
    operatorC = operator.upper()
    if operatorC == "Q":
        break
    if operatorC == "MI":
        print(
            "Memory:",
            str(memory).replace("j", "i"),
            memory2,
            memory3,
            memory4,
            ". To add memory, type ME. To use memory in calculations, for me1 its M1, and so on. To reset memory, type MRA to reset all and MR(memory slot) to erase any memory slot, like MR1. ",
        )
        continue
    if operatorC == "CMD":
        print(
            "MI gives memory info, ME1 gives memory edit to slot 1 ME2 to slot 2 and so on until slot 4. C for conversions, Arcsin for arcsin, Sinh for hyperbolic sin. These go on because Arccos exists and Cosh too. Alg for Algebra (in the format ax ± b = c). "
        )
        continue
    if operatorC == "ME1":
        memorySTR = str(memory)
        print(f"M1 is currently {memory}")
        memory = input("What do you want to set memory slot 1 to? ")
        memory = memory.replace("i", "j")
        memory = complex(memory)
        continue
    if operatorC == "ME2":
        memory2STR = str(memory2)
        memory2 = input("What do you want to set memory slot 1 to? ")
        print(f"M2 is currently {memory2}")
        memory2 = memory2.replace("i", "j")
        memory2 = complex(memory2)
        continue
    if operatorC == "ME3":
        memory3STR = str(memory3)
        memory3 = input("What do you want to set memory slot 1 to? ")
        print(f"M3 is currently {memory3}")
        memory3 = memory3.replace("i", "j")
        memory3 = complex(memory3)
        continue
    if operatorC == "ME4":
        memory4 = input("What do you want to set memory slot 1 to? ")
        print(f"M4 is currently {memory4}")
        memory4 = memory4.replace("i", "j")
        memory4 = complex(memory4)
        continue
    if operatorC == "MRA":
        memory = "empty!"
        memory2 = "empty!"
        memory3 = "empty!"
        memory4 = "empty!"
        print("Wiped all memory slots!")
        continue
    if operatorC == "MR1":
        memory = "empty!"
        print("Wiped M1! ")
        continue
    if operatorC == "MR2":
        memory2 = "empty!"
        print("Wiped M2! ")
        continue
    if operatorC == "MR3":
        memory3 = "empty!"
        print("Wiped M3! ")
        continue
    if operatorC == "MR4":
        memory4 = "empty!"
        print("Wiped M4! ")
        continue
    if operatorC == "C":
        converter = input(
            "Type ktm for km to miles, and mtk for reverse. cti for cm to inch and itc for.. obvious. ytm for yards to meter, and mty exists. UTE converts USD to EUR, ETU reverse of that, UTB (usd to gbp) and BTU. FTC converts farenheit to celsius, CTK for celsius to kelvin, and so on. DTO is decimal to octal, DTB is decimal to binary, DTH for hexadecimal. KTP is kilogram -> pound, PTK is opposite. "
        )
        converterC = converter.upper()
        if converterC == "KTM":
            number1 = float(input("How many kilometers? "))
            print("Your answer is:", (number1 * 0.621371))
        if converterC == "MTK":
            number1 = float(input("How many miles? "))
            print("Your answer is:", (number1 * 1.6093))
        if converterC == "CTI":
            number1 = float(input("How many centimeters? "))
            print("Your answer is:", (number1 * 0.393701))
            continue
        if converterC == "ITC":
            number1 = float(input("How many inches? "))
            print("Your answer is:", (number1 * 2.54))
            continue
        if converterC == "YTM":
            number1 = float(input("How many yards? "))
            print("Your answer is:", number1 * 0.9144)
            continue
        if converterC == "MTY":
            number1 = float(input("How many meters? "))
            print("Your answer is:", number1 * 1.09361)
            continue
        if converterC == "UTE":
            number1 = float(input("How many dollars? "))
            print("Your USD in EUR is:", number1 * 0.95)
            continue
        if converterC == "ETU":
            number1 = float(input("How many euros? "))
            print("Your EUR in USD is:", number1 * 1.05)
            continue
        if converterC == "UTB":
            number1 = float(input("How many dollars? "))
            print("Your USD in GBP is:", number1 * 0.79)
            continue
        if converterC == "BTU":
            number1 = float(input("How many pounds? "))
            print("Your GBP in USD is:", number1 * 1.27)
            continue
        if converterC == "FTC":
            number1 = float(input("How many Fahrenheit? "))
            print("Your Fahrenheit in Celsius is:", ((number1 - 32) * (5 / 9)))
        if converterC == "CTF":
            number1 = float(input("How many Celsius? "))
            print("Your Celsius in Fahrenheit is:", ((number1) * (9 / 5)) + 32)
        if converterC == "CTK":
            number1 = float(input("How many Celsius?"))
            print("Your Celsius in Kelvin is:", (number1 + 273.15))
        if converterC == "KTC":
            number1 = float(input("How many Kelvin? "))
            print("Your Kelvin in Celsius is:", (number1 - 273.15))
        if converterC == "FTK":
            number1 = float(input("How many Fahrenheit? "))
            print("Your Fahrenheit in Kelvin is:", ((number1 - 32) * (5 / 9)) + 32)
        if converterC == "KTF":
            number1 = float(input("How many Kelvin? "))
            print("Your Kelvin in Fahrenheit is:", ((number1 - 273.15) * (9 / 5)) + 32)
        if converterC == "DTB":
            number1 = int(input("How much? "))
            print("Your answer is:", (bin(number1)[2:]))
        if converterC == "DTH":
            number1 = int(input("How much? "))
            print("Your answer is:", (hex(number1)[2:]))
        if converterC == "DTO":
            number1 = int(input("How much? "))
            print("Your answer is:", (oct(number1)[2:]))
        if converterC == "KTP":
            number1 = float(input("How many Kilograms? "))
            print("You Kilograms in Pounds is:", (number1 * 2.20462))
        if converterC == "PTK":
            number1 = float(input("How many Pounds? "))
            print("Your Pounds in Kilograms is:", (number1 * 0.453592))
        if converterC not in [
            "KTM",
            "MTK",
            "CTI",
            "ITC",
            "MTY",
            "YTM",
            "UTE",
            "ETU",
            "UTB",
            "BTU",
            "FTC",
            "CTF",
            "CTK",
            "KTC",
            "KTF",
            "FTK",
            "DTB" "DTH" "DTO" "KTP" "PTK",
        ]:
            print("Error: Trying to convert error to error? 500000 years in math jail ")

    def albr_slvr(ques):
        side_1, side_2 = ques.split("=")
        part_1 = side_1.split("x")

        if part_1[0].strip() == "" or part_1[0].strip() == "+":
            a = 1
        elif part_1[0].strip() == "-":
            a = -1
        else:
            a = int(part_1[0].strip())

        if len(part_1) > 1:
            b = int(part_1[1].strip())
        else:
            b = 0

        part_2 = side_2.strip()
        c = int(part_2)

        if a == 0:
            return "Error: Brain Damage, The rise and fall of 0"

        x = (c - b) / a

        return x

    if operatorC == "ALG":
        algebra = input("What equation? (Format: ax ± b = c) ")
        print("x =", albr_slvr(algebra))
    if operatorC == "A":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memoryANS = str(memory + number2).replace("j", "i")
            if "+0i" in memoryANS or "-0i" in memoryANS:
                memoryANS = memoryANS.replace("+0i", "")
                memoryANS = memoryANS.replace("-0i", "")
            print("Your answer is:", memoryANS)
            continue
        if memorydeciderC == "M2":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memory2ANS = str(memory2 + number2).replace("j", "i")
            if "+0i" in memory2ANS or "-0i" in memory2ANS:
                memory2ANS = memory2ANS.replace("+0i", "")
                memory2ANS = memory2ANS.replace("-0i", "")
            print("Your answer is:", memory2ANS)
            continue
        if memorydeciderC == "M3":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memory3ANS = str(memory3 + number2).replace("j", "i")
            if "+0i" in memory3ANS or "-0i" in memory3ANS:
                memory3ANS = memory3ANS.replace("+0i", "")
                memory3ANS = memory3ANS.replace("-0i", "")
            print("Your answer is:", memory3ANS)
            continue
        if memorydeciderC == "M4":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memory4ANS = str(memory4 + number2).replace("j", "i")
            if "+0i" in memoryANS or "-0i" in memory4ANS:
                memory4ANS = memory4ANS.replace("+0i", "")
                memory4ANS = memory4ANS.replace("-0i", "")
            print("Your answer is:", memory4ANS)
            continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = input("Starting Number? ")
            number1 = complex(number1)
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            numberANS = str(number1 + number2).replace("j", "i")
            if "+0i" in numberANS or "-0i" in numberANS:
                numberANS = numberANS.replace("+0i", "")
                numberANS = numberANS.replace("-0i", "")
            print("Your answer is:", numberANS)
            continue
    elif operatorC == "S":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memoryANS = str(memory - number2).replace("j", "i")
            if "+0i" in memoryANS or "-0i" in memoryANS:
                memoryANS = memoryANS.replace("+0i", "")
                memoryANS = memoryANS.replace("-0i", "")
            print("Your answer is:", memoryANS)
            continue
        if memorydeciderC == "M2":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memory2ANS = str(memory2 - number2).replace("j", "i")
            if "+0i" in memory2ANS or "-0i" in memory2ANS:
                memory2ANS = memory2ANS.replace("+0i", "")
                memory2ANS = memory2ANS.replace("-0i", "")
            print("Your answer is:", memory2ANS)
            continue
        if memorydeciderC == "M3":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memory3ANS = str(memory3 - number2).replace("j", "i")
            if "+0i" in memory3ANS or "-0i" in memory3ANS:
                memory3ANS = memory3ANS.replace("+0i", "")
                memory3ANS = memory3ANS.replace("-0i", "")
            print("Your answer is:", memory3ANS)
            continue
        if memorydeciderC == "M4":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memory4ANS = str(memory4 - number2).replace("j", "i")
            if "+0i" in memory4ANS or "-0i" in memory4ANS:
                memory4ANS = memory4ANS.replace("+0i", "")
                memory4ANS = memory4ANS.replace("-0i", "")
            print("Your answer is:", memory4ANS)
            continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = input("Starting Number? ")
            number1 = complex(number1)
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            numberANS = str(number1 - number2).replace("j", "i")
            if "+0i" in numberANS or "-0i" in numberANS:
                numberANS = numberANS.replace("+0i", "")
                numberANS = numberANS.replace("-0i", "")
            print("Your answer is:", numberANS)
            continue
    elif operatorC == "M":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memoryANS = str(memory * number2).replace("j", "i")
            if "+0i" in memoryANS or "-0i" in memoryANS:
                memoryANS = memoryANS.replace("+0i", "")
                memoryANS = memoryANS.replace("-0i", "")
            print("Your answer is:", memoryANS)
            continue
        if memorydeciderC == "M2":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memory2ANS = str(memory2 * number2).replace("j", "i")
            if "+0i" in memory2ANS or "-0i" in memory2ANS:
                memory2ANS = memory2ANS.replace("+0i", "")
                memory2ANS = memory2ANS.replace("-0i", "")
            print("Your answer is:", memory2ANS)
            continue
        if memorydeciderC == "M3":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memory3ANS = str(memory3 * number2).replace("j", "i")
            if "+0i" in memory3ANS or "-0i" in memory3ANS:
                memory3ANS = memory3ANS.replace("+0i", "")
                memory3ANS = memory3ANS.replace("-0i", "")
            print("Your answer is:", memory3ANS)
            continue
        if memorydeciderC == "M4":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memory4ANS = str(memory4 * number2).replace("j", "i")
            if "+0i" in memory4ANS or "-0i" in memoryANS:
                memory4ANS = memory4ANS.replace("+0i", "")
                memory4ANS = memory4ANS.replace("-0i", "")
            print("Your answer is:", memory4ANS)
            continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = input("Number to be multiplied? ")
            number1 = complex(number1)
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            numberANS = str(number1 - number2).replace("j", "i")
            if "+0i" in numberANS or "-0i" in numberANS:
                numberANS = numberANS.replace("+0i", "")
                numberANS = numberANS.replace("-0i", "")
            print("Your answer is:", numberANS)
            continue
    elif operatorC == "D":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memoryANS = str(memory / number2).replace("j", "i")
            if "+0i" in memoryANS or "-0i" in memoryANS:
                memoryANS = memoryANS.replace("+0i", "")
                memoryANS = memoryANS.replace("-0i", "")
            print("Your answer is:", memoryANS)
            continue
            if number2 == 0:
                print("Dividing by 0 can get you 60 years in math jail.")
                continue
        if memorydeciderC == "M2":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memory2ANS = str(memory2 / number2).replace("j", "i")
            if "+0i" in memory2ANS or "-0i" in memoryANS:
                memory2ANS = memory2ANS.replace("+0i", "")
                memory2ANS = memory2ANS.replace("-0i", "")
            print("Your answer is:", memory2ANS)
            continue
            if number2 == 0:
                print("Dividing by 0 can get you 60 years in math jail.")
                continue
            else:
                print("Your answer is:", memory2 / number2)
                continue
        if memorydeciderC == "M3":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memory3ANS = str(memory3**number2).replace("j", "i")
            if "+0i" in memory3ANS or "-0i" in memory3ANS:
                memory3ANS = memory3ANS.replace("+0i", "")
                memoryANS = memory3ANS.replace("-0i", "")
            print("Your answer is:", memory3ANS)
            continue
            if number2 == 0:
                print("Dividing by 0 can get you 60 years in math jail.")
                continue
            else:
                print("Your answer is:", memory3 / number2)
                continue
        if memorydeciderC == "M4":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memory4ANS = str(memory4**number2).replace("j", "i")
            if "+0i" in memory4ANS or "-0i" in memory4ANS:
                memory4ANS = memory4ANS.replace("+0i", "")
                memory4ANS = memory4ANS.replace("-0i", "")
            print("Your answer is:", memory4ANS)
            continue
            if number2 == 0:
                print("Dividing by 0 can get you 60 years in math jail.")
                continue
            else:
                print("Your answer is:", memory4 / number2)
                continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = input("Number to be divided? ")
            number1 = complex(number1)
            number2 = input("Divisor? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            numberANS = str(number1 / number2).replace("j", "i")
            if "+0i" in numberANS or "-0i" in numberANS:
                numberANS = numberANS.replace("+0i", "")
                numberANS = numberANS.replace("-0i", "")
            print("Your answer is:", numberANS)
            continue
            if number2 == 0:
                print("Dividing by 0 can get you 60 years in math jail. ")
            else:
                print("Your answer is:", number1 / number2)
                continue
    elif operatorC == "E":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memoryANS = str(memory**number2).replace("j", "i")
            if "+0i" in memoryANS or "-0i" in memoryANS:
                memoryANS = memoryANS.replace("+0i", "")
                memoryANS = memoryANS.replace("-0i", "")
            print("Your answer is:", memoryANS)
            continue
        if memorydeciderC == "M2":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memory2ANS = str(memory2**number2).replace("j", "i")
            if "+0i" in memory2ANS or "-0i" in memory2ANS:
                memory2ANS = memory2ANS.replace("+0i", "")
                memory2ANS = memory2ANS.replace("-0i", "")
            print("Your answer is:", memory2ANS)
            continue
        if memorydeciderC == "M3":
            number2 = input("Second Number? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            memory3ANS = str(memory3**number2).replace("j", "i")
            if "+0i" in memory3ANS or "-0i" in memory3ANS:
                memory3ANS = memory3ANS.replace("+0i", "")
                memory3ANS = memory3ANS.replace("-0i", "")
            print("Your answer is:", memoryANS)
            continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = input("What number? ")
            number1 = complex(number1)
            number2 = input("What exponent? ")
            number2 = str(number2).replace("i", "j")
            number2 = complex(number2)
            numberANS = str(number1**number2).replace("j", "i")
            if "+0i" in numberANS or "-0i" in numberANS:
                numberANS = numberANS.replace("+0i", "")
                numberANS = numberANS.replace("-0i", "")
            print("Your answer is:", numberANS)
            continue
        if number1 == 0 and number2 == 0:
            print("Error: 0^0 may land you 90 years in Math Jail")
    elif operatorC == "R":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            number2 = input("Second Number? ")
            print("Your answer is:", memory ** (1 / number2))
            continue
        if memorydeciderC == "M2":
            number2 = input("Second Number? ")
            print("Your answer is:", memory2 ** (1 / number2))
            continue
        if memorydeciderC == "M3":
            number2 = input("Second Number? ")
            print("Your answer is:", memory3 ** (1 / number2))
            continue
        if memorydeciderC == "M4":
            number2 = input("Second Number?")
            print("Your answer is:", memory4 ** (1 / number2))
            continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = float(input("What number? "))
            number2 = float(
                input("What level of rooting? (2 for squaring, 3 for cubing etc...)")
            )
            print("Your answer is:", number1 ** (1 / number2))
            continue
        if number2 < 2:
            print(
                "Error: Rooting in such a way can get 8 generations of your family in Math Jail"
            )
        elif number1 < 0:
            print(
                "Error: Such roots cannot exist and you might get 500 families in Math Jail"
            )
    elif operatorC == "F":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            memoryInt = int(memory)
            print("Your answer is:", math.factorial(memoryInt))
            continue
        if memorydeciderC == "M2":
            memory2Int = int(memory2)
            print("Your answer is:", math.factorial(memory2Int))
            continue
        if memorydeciderC == "M3":
            memory3Int = int(memory3)
            print("Your answer is:", math.factorial(memory3Int))
            continue
        if memorydeciderC == "M4":
            memory4Int = int(memory4)
            print("Your answer is:", math.factorial(memory4Int))
            continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = int(input("What number? "))
            print("Your answer is:", math.factorial(number1))
            continue
    elif operatorC == "MOD":
        if number2 == 0:
            print("Error: Divided by 0, United by Math Jail")
        else:
            number3 = number1 % number2
            print("Your answer is", number3)
    elif operatorC == "SIN":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.sin(math.radians(memory))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.sin(memory))
                continue
        if memorydeciderC == "M2":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.sin(math.radians(memory2))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.sin(memory2))
                continue
        if memorydeciderC == "M3":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.sin(math.radians(memory3))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.sin(memory3))
                continue
        if memorydeciderC == "M4":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.sin(math.radians(memory4))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.sin(memory4))
                continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = float(input("What number? "))
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.sin(math.radians(number1))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.sin(number1))
                continue
        if memorydeciderC not in ["M1", "M2", "M3", "M4", "S"] or decidertrigC not in [
            "DEG",
            "RAD",
        ]:
            print("Invalid Choice = Invalid Brain")

    elif operatorC == "COS":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.cos(math.radians(memory))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.cos(memory))
                continue
        if memorydeciderC == "M2":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.cos(math.radians(memory2))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.cos(memory2))
                continue
        if memorydeciderC == "M3":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.cos(math.radians(memory3))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.cos(memory3))
                continue
        if memorydeciderC == "M4":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.cos(math.radians(memory4))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.cos(memory4))
                continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = float(input("What number? "))
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.cos(math.radians(number1))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.cos(number1))
                continue
        if memorydeciderC not in ["M1", "M2", "M3", "M4", "S"] or decidertrigC not in [
            "DEG",
            "RAD",
        ]:
            print("Invalid Choice = Invalid Brain")

    elif operatorC == "TAN":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.tan(math.radians(memory))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.tan(memory))
                continue
        if memorydeciderC == "M2":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.tan(math.radians(memory2))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.tan(memory2))
                continue
        if memorydeciderC == "M3":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.tan(math.radians(memory3))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.tan(memory3))
                continue
        if memorydeciderC == "M4":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.tan(math.radians(memory4))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.tan(memory4))
                continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = float(input("What number? "))
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.tan(math.radians(number1))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.tan(number1))
                continue
        if memorydeciderC not in ["M1", "M2", "M3", "M4", "S"] or decidertrigC not in [
            "DEG",
            "RAD",
        ]:
            print("Invalid Choice = Invalid Brain")

    elif operatorC == "LOG":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            number2 = input("What base? Type e for natural log. ")
            if number2.upper() == "E":
                print("Your answer is:", math.log(memory))
                continue
            else:
                float2 = float(number2)
                print("Your answer is:", math.log(memory, float2))
                continue
        if memorydeciderC == "M2":
            number2 = input("What base? Type e for natural log. ")
            if number2.upper() == "E":
                print("Your answer is:", math.log(memory2))
                continue
            else:
                float2 = float(number2)
                print("Your answer is:", math.log(memory2, float2))
                continue
        if memorydeciderC == "M3":
            number2 = input("What base? Type e for natural log. ")
            if number2.upper() == "E":
                print("Your answer is:", math.log(memory3))
                continue
            else:
                float2 = float(number2)
                print("Your answer is:", math.log(memory3, float2))
                continue
        if memorydeciderC == "M4":
            number2 = input("What base? Type e for natural log. ")
            if number2.upper() == "E":
                print("Your answer is:", math.log(memory4))
                continue
            else:
                float2 = float(number2)
                print("Your answer is:", math.log(memory4, float2))
                continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = float(input("What number? "))
            number2 = input("What base? Type e for natural log. ")
            if number2.upper() == "E":
                print("Your answer is:", math.log(number1))
                continue
            else:
                float2 = float(number2)
                print("Your answer is:", math.log(number1, float2))
                continue
        else:
            print("Inavlid Choice = Invalid Brain")
    elif operatorC == "ARCSIN":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.asin(math.radians(memory))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.asin(memory))
                continue
        if memorydeciderC == "M2":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.asin(math.radians(memory2))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.asin(memory2))
                continue
        if memorydeciderC == "M3":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.asin(math.radians(memory3))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.asin(memory3))
                continue
        if memorydeciderC == "M4":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.asin(math.radians(memory4))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.asin(memory4))
                continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = float(input("What number? "))
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.asin(math.radians(number1))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.asin(number1))
                continue
        if memorydeciderC not in ["M1", "M2", "M3", "M4", "S"] or decidertrigC not in [
            "DEG",
            "RAD",
        ]:
            print("Invalid Choice = Invalid Brain")

    elif operatorC == "ARCCOS":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.acos(math.radians(memory))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.acos(memory))
                continue
        if memorydeciderC == "M2":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.acos(math.radians(memory2))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.acos(memory2))
                continue
        if memorydeciderC == "M3":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.acos(math.radians(memory3))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.acos(memory3))
                continue
        if memorydeciderC == "M4":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.acos(math.radians(memory4))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.acos(memory4))
                continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = float(input("What number? "))
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.acos(math.radians(number1))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.acos(number1))
                continue
        if memorydeciderC not in ["M1", "M2", "M3", "M4", "S"] or decidertrigC not in [
            "DEG",
            "RAD",
        ]:
            print("Invalid Choice = Invalid Brain")

    elif operatorC == "ARCTAN":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.atan(math.radians(memory))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.atan(memory))
                continue
        if memorydeciderC == "M2":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.atan(math.radians(memory2))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.atan(memory2))
                continue
        if memorydeciderC == "M3":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.atan(math.radians(memory3))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.atan(memory3))
                continue
        if memorydeciderC == "M4":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.atan(math.radians(memory4))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.atan(memory4))
                continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = float(input("What number? "))
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.atan(math.radians(number1))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.atan(number1))
                continue
        if memorydeciderC not in ["M1", "M2", "M3", "M4", "S"] or decidertrigC not in [
            "DEG",
            "RAD",
        ]:
            print("Invalid Choice = Invalid Brain")
    elif operatorC == "SINH":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.sinh(math.radians(memory))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.sinh(memory))
                continue
        if memorydeciderC == "M2":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.sinh(math.radians(memory2))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.sinh(memory2))
                continue
        if memorydeciderC == "M3":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.sinh(math.radians(memory3))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.sinh(memory3))
                continue
        if memorydeciderC == "M4":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.sinh(math.radians(memory4))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.sinh(memory4))
                continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = float(input("What number? "))
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.sinh(math.radians(number1))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.sinh(number1))
                continue
        if memorydeciderC not in ["M1", "M2", "M3", "M4", "S"] or decidertrigC not in [
            "DEG",
            "RAD",
        ]:
            print("Invalid Choice = Invalid Brain")
    elif operatorC == "COSH":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.cosh(math.radians(memory))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.cosh(memory))
                continue
        if memorydeciderC == "M2":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.cosh(math.radians(memory2))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.cosh(memory2))
                continue
        if memorydeciderC == "M3":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.cosh(math.radians(memory3))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.cosh(memory3))
                continue
        if memorydeciderC == "M4":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.cosh(math.radians(memory4))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.cosh(memory4))
                continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = float(input("What number? "))
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.cosh(math.radians(number1))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.cosh(number1))
                continue
        if memorydeciderC not in ["M1", "M2", "M3", "M4", "S"] or decidertrigC not in [
            "DEG",
            "RAD",
        ]:
            print("Invalid Choice = Invalid Brain")
    elif operatorC == "COSH":
        memorydecider = input(
            "Choose from M1, M2, M3, and M4. Choose S to skip this step "
        )
        memorydeciderC = memorydecider.upper()
        if memorydeciderC == "M1":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.cosh(math.radians(memory))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.cosh(memory))
                continue
        if memorydeciderC == "M2":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.cosh(math.radians(memory2))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.cosh(memory2))
                continue
        if memorydeciderC == "M3":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.cosh(math.radians(memory3))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.cosh(memory3))
                continue
        if memorydeciderC == "M4":
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.cosh(math.radians(memory4))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.cosh(memory4))
                continue
        if memorydeciderC == "S" or memorydeciderC == "s":
            number1 = float(input("What number? "))
            decidertrig = input("(Deg)rees or (Rad)ians? ")
            decidertrigC = decidertrig.upper()
            if decidertrigC == "DEG":
                memoryDEG = math.tanh(math.radians(number1))
                print("Your answer is:", memoryDEG)
                continue
            elif decidertrigC == "RAD":
                print("Your answer is:", math.tanh(number1))
                continue
        if memorydeciderC not in ["M1", "M2", "M3", "M4", "S"] or decidertrigC not in [
            "DEG",
            "RAD",
        ]:
            print("Invalid Choice = Invalid Brain")
    if (
        operatorC
        in [
            "KTM",
            "MTK",
            "CTI",
            "ITC",
            "MTY",
            "YTM",
            "UTE",
            "ETU",
            "UTB",
            "BTU",
            "FTC",
            "CTF",
            "CTK",
            "KTC",
            "KTF",
            "FTK",
            "DTB" "DTH" "DTO" "KTP" "PTK",
        ]
        or operatorC
        in [
            "A",
            "S",
            "M",
            "D",
            "MOD",
            "F",
            "SIN",
            "COS",
            "TAN",
            "ARCSIN",
            "ARCCOS",
            "ARCTAN",
            "SINH",
            "COSH",
            "TANH",
            "LOG",
            "R",
            "E",
            "ALG",
        ]
        or operatorC
        in ["C", "ME1", "ME2", "ME3", "ME4", "MI", "MRA", "MR1", "MR2", "MR3", "MR4"]
    ):
        continue
    else:
        print("Invalid: The rise and fall of Atuyeyi Operation")
