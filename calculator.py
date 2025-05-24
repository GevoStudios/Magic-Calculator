import math
import os
import hashlib
import sqlite3
import random
import datetime
import cmath

memory = "empty!"
memory2 = "empty!"
memory3 = "empty!"
memory4 = "empty!"
number1 = 0
number2 = 0

savecycle = []

equationcycle = []

settings_path = "C:/Users/Public/settings.txt"

if not os.path.exists(settings_path):
    with open(settings_path, "w") as f:
        f.write("histLength=3\n")
        f.write("angleUnit=NOD\n")


def setLoad():
    historylimit = 3
    angleUnit = "NOD"
    path = "C:/Users/Public/settings.txt"

    if os.path.exists(path):
        with open(path, "r") as f:
            for line in f:
                if line.startswith("histLength="):
                    try:
                        val = int(line.strip().split("=")[1])
                        historylimit = max(3, min(100, val))
                    except:
                        historylimit = 3
                elif line.startswith("angleUnit="):
                    val = line.strip().split("=")[1].upper()
                    if val in ["DEG", "RAD", "NOD"]:
                        angleUnit = val
                    else:
                        angleUnit = "NOD"
    return historylimit, angleUnit


def setSave(historylimit, angleUnit):
    with open(settings_path, "w") as f:
        f.write(f"histLength={historylimit}\n")
        f.write(f"angleUnit={angleUnit}\n")


def degs(x):
    return x * (cmath.pi / 180)


loggedin = False
accountin = None

salt = os.urandom(16)

datawire = sqlite3.connect("MagicCalculator31415926.db")
cursor = datawire.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS accountsList(accounts TEXT UNIQUE, password TEXT, salt BLOB, description TEXT, equation TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT)"
)

debug = input("Enable debug mode? Y/N (enabling debug mode requires a password) ")
debugC = debug.upper()
if debugC == "Y":
    directory = input("What directory is the txt in? ")
    passwordfile = os.path.join(directory, "apass.txt")
    keyfile = os.path.join(directory, "kpass.txt")
    if os.path.exists(directory):
        paword = input("What's the password? ")
        usword = input("What's the username? ")
        with open(passwordfile, "r") as pf:
            pfi = pf.read().strip()
        with open(keyfile, "r") as kf:
            kfi = kf.read().strip()
        ipfi = hashlib.sha512((paword).encode("utf-8")).hexdigest().strip()
        ikfi = hashlib.sha512((usword).encode("utf-8")).hexdigest().strip()
        ipfi = str(ipfi).strip()
        pfi = str(pfi).strip()
        ikfi = str(ikfi).strip()
        kfi = str(kfi).strip()
        if ipfi == pfi and ikfi == kfi:
            print("Debug mode enabled!")
        else:
            print("Debug mode disabled: Wrong password entered.")
            debugC = "N"
    else:
        print("Debug mode disabled: Nonexistent Directory")
        debugC = "N"
elif debugC == "N":
    print("Debug mode disabled. Procceding to calculator.")
else:
    print("Not an option")
if debugC == "Y":
    print("DEBUG: debugC = Y")
    print("DEBUG: Action = None")
texter = random.randint(1, 4)
if texter == 1:
    splash = "New Accounts and Settings!"
if texter == 2:
    splash = "Calculate the next update :)"
if texter == 3:
    splash = "again, the outdated money converter"
if texter == 4:
    splash = ""
print("Welcome to Magic Calculator v4.0! The Online Update!")
print(splash)
while True:
    historylimit, angleUnit = setLoad()

    try:
        operator = input(
            "What operation do you want? [CMD FOR MORE COMMANDS, CMD1 FOR EVEN MORE COMMANDS, SET FOR SETTINGS] (type ACC for account) Type A for addition, S for Subtraction, M for multiplication, and D for division. Type E for exponents, R for Roots, F for factorials, Mod for Modular stuff, Log for Log, Sin/Cos/tan do what you expect them to do. Press Q to quit. "
        )
        operatorC = operator.upper()
        if operatorC == "Q":
            if debugC == "Y":
                print("DEBUG: operatorC = Q")
                print("DEBUG: Action = break")
            break
        if operatorC == "SET":
            settingsdecider = input("Edit historylimit or angle unit? (H/A) ")
            settingsdeciderC = settingsdecider.upper()
            if settingsdeciderC == "H":
                historylimit = int(
                    input(
                        f"What do you want the history limit to be? (3-100) (default is 3, currently {historylimit}) "
                    )
                )
                if historylimit < 3 or historylimit > 100:
                    print("(Error Code 17) GO OVER LIMIT = NEGATIVE BRAIN IQ")
                    historylimit = 3
                    continue
                setSave(historylimit)
                continue
            elif settingsdeciderC == "A":
                unitInput = (
                    input(
                        f"Set angle unit to DEG, RAD, or NOD? (currently {angleUnit}) "
                    )
                    .strip()
                    .upper()
                )

                if unitInput not in ["DEG", "RAD", "NOD"]:
                    print("(Error Code 18) GET IN-SET!  ")
                    continue

                angleUnit = unitInput
                setSave(historylimit, angleUnit)
                continue
        if operatorC == "MI":
            if debugC == "Y":
                print("DEBUG: operatorC = MI")
                print("DEBUG: Action = print()")
            memory = str(memory).replace("j", "i")
            if "+0i" in memory or "-0i" in memory or "0i" in memory:
                memory = memory.replace("+0i", "")
                memory = memory.replace("-0i", "")
                memory = memory.replace("0i", "")
            memory2 = str(memory2).replace("j", "i")
            if "+0i" in memory2 or "-0i" in memory2 or "0i" in memory2:
                memory2 = memory2.replace("+0i", "")
                memory2 = memory2.replace("-0i", "")
                memory2 = memory2.replace("0i", "")
            memory3 = str(memory3).replace("j", "i")
            if "+0i" in memory3 or "-0i" in memory3 or "0i" in memory3:
                memory3 = memory3.replace("+0i", "")
                memory3 = memory3.replace("-0i", "")
                memory3 = memory3.replace("0i", "")
            memory4 = str(memory4).replace("j", "i")
            if "+0i" in memory4 or "-0i" in memory4 or "0i" in memory4:
                memory4 = memory4.replace("+0i", "")
                memory4 = memory4.replace("-0i", "")
                memory4 = memory4.replace("0i", "")
            print(
                "Memory:",
                memory,
                memory2,
                memory3,
                memory4,
                ". To add memory, type ME. To use memory in calculations, for me1 its M1, and so on. To reset memory, type MRA to reset all and MR(memory slot) to erase any memory slot, like MR1. ",
            )
            continue
        if operatorC == "CMD":
            if debugC == "Y":
                print("DEBUG: operatorC = CMD")
                print("DEBUG: Action = print()")
            print(
                "MI gives memory info, ME1 gives memory edit to slot 1 ME2 to slot 2 and so on until slot 4. C for conversions, Arcsin for arcsin, Sinh for hyperbolic sine, Arcsinh for Hyperbolic Arcsin. These go on because Arccos exists and Arccosh and Cosh too. Alg for Algebra (in the format ax ± b = c). QALG for Quadratic Algebra (in the format ax^2 ± b ± c = 0). "
            )
        if operatorC == "CMD1":
            print(
                "HIST is history, RAND is random number, EXP is Export, CLEAR to clear history"
            )
            continue
        if operatorC == "ME1":
            if debugC == "Y":
                print("DEBUG: operatorC = ME1")
                print("DEBUG: Action = var = str()")
            memorySTR = str(memory)
            print(f"M1 is currently {memory}")
            memory = input("What do you want to set memory slot 1 to? ")
            memory = str(memory).replace("j", "i")
            if "+0i" in memory or "-0i" in memory or "0i" in memory:
                memory = memory.replace("+0i", "")
                memory = memory.replace("-0i", "")
                memory = memory.replace("0i", "")
            memory = memory.replace("i", "j")
            memory = complex(memory)
            if debugC == "Y":
                print(f"DEBUG: memory = {memory}")
                print("DEBUG: Action = None")
            continue
        if operatorC == "ME2":
            if debugC == "Y":
                print("DEBUG: operatorC = ME2")
                print("DEBUG: Action = var = str()")
            memory2STR = str(memory2)
            print(f"M2 is currently {memory2}")
            memory2 = input("What do you want to set memory slot 2 to? ")
            memory2 = str(memory2).replace("j", "i")
            if "+0i" in memory2 or "-0i" in memory2 or "0i" in memory2:
                memory2 = memory2.replace("+0i", "")
                memory2 = memory2.replace("-0i", "")
                memory2 = memory2.replace("0i", "")
            memory2 = memory2.replace("i", "j")
            memory2 = complex(memory2)
            if debugC == "Y":
                print(f"DEBUG: memory2 = {memory2}")
                print("DEBUG: Action = None")
            continue
        if operatorC == "ME3":
            if debugC == "Y":
                print("DEBUG: operatorC = ME3")
                print("DEBUG: Action = var = str()")
            memory3STR = str(memory3)
            print(f"M3 is currently {memory3}")
            memory3 = input("What do you want to set memory slot 3 to? ")
            memory3 = str(memory3).replace("j", "i")
            if "+0i" in memory3 or "-0i" in memory3 or "0i" in memory3:
                memory3 = memory3.replace("+0i", "")
                memory3 = memory3.replace("-0i", "")
                memory3 = memory3.replace("0i", "")
            memory3 = memory3.replace("i", "j")
            memory3 = complex(memory3)
            if debugC == "Y":
                print(f"DEBUG: memory3 = {memory3}")
                print("DEBUG: Action = None")
            continue
        if operatorC == "ME4":
            if debugC == "Y":
                print("DEBUG: operatorC = ME4")
                print("DEBUG: Action = var = str()")
            print(f"M4 is currently {memory4}")
            memory4 = input("What do you want to set memory slot 4 to? ")
            memory4 = str(memory4).replace("j", "i")
            if "+0i" in memory4 or "-0i" in memory4 or "0i" in memory4:
                memory4 = memory4.replace("+0i", "")
                memory4 = memory4.replace("-0i", "")
                memory4 = memory4.replace("0i", "")
            memory4 = memory4.replace("i", "j")
            memory4 = complex(memory4)
            if debugC == "Y":
                print(f"DEBUG: memory4 = {memory4}")
                print("DEBUG: Action = None")
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
                "Type ktm for km to miles, and mtk for reverse. cti for cm to inch and itc for.. obvious. ytm for yards to meter, and mty exists. UTE converts USD to EUR, ETU reverse of that, UTB (usd to gbp) and BTU. FTC converts farenheit to celsius, CTK for celsius to kelvin, and so on. DTO is decimal to octal, DTB is decimal to binary, DTH for hexadecimal. KTP is kilogram -> pound, PTK is opposite. FTM is Feet to Meters. "
            )
            converterC = converter.upper()
            if converterC == "KTM":
                number1 = float(input("How many kilometers? "))
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = number1
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"Convert {number1} kilometers to miles."
                print("Your answer is:", (number1 * 0.621371))
            if converterC == "MTK":
                number1 = float(input("How many miles? "))
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = number1
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"Convert {number1} miles to kilometers."
                print("Your answer is:", (number1 * 1.6093))
            if converterC == "CTI":
                number1 = float(input("How many centimeters? "))
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = number1
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"Convert {number1} centimeters to inches."
                print("Your answer is:", (number1 * 0.393701))
                continue
            if converterC == "ITC":
                number1 = float(input("How many inches? "))
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = number1
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"Convert {number1} inches to centimeters."
                print("Your answer is:", (number1 * 2.54))
                continue
            if converterC == "YTM":
                number1 = float(input("How many yards? "))
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = number1
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"Convert {number1} yards to meters."
                print("Your answer is:", number1 * 0.9144)
                continue
            if converterC == "MTY":
                number1 = float(input("How many meters? "))
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = number1
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"Convert {number1} meters to yards."
                print("Your answer is:", number1 * 1.09361)
                continue
            if converterC == "UTE":
                number1 = float(input("How many dollars? "))
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = number1
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"Convert {number1} USD to EUR."
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
                print("Your GBP in USD is:", number1 * 1.26)
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
                print(
                    "Your Kelvin in Fahrenheit is:", ((number1 - 273.15) * (9 / 5) + 32)
                )
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
            if converterC == "FTM":
                number1 = float(input("How many feet? "))
                print("Your Feet in Meters is:", (number1 * 0.3048))
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
                "DTB",
                "DTH",
                "DTO",
                "KTP",
                "PTK",
                "FTM",
            ]:
                print(
                    "Error: Trying to convert error to error? 500000 years in math jail "
                )

        def albr_slvr(ques):
            side_1, side_2 = ques.split("=")
            side_1 = side_1.replace("x", "")
            c = float(side_2)
            if "+" in side_1:
                a, b = side_1.split("+")
                a = float(a)
                b = float(b)
                return (c - b) / a
            if "-" in side_1:
                a, b = side_1.split("-")
                a = float(a)
                b = float(b)
                return (c + b) / a

        def qabr_slvr(ques):
            side_1, side_2 = ques.split("=")
            side_1 = side_1.replace(" ", "")
            side_2 = float(side_2)
            if "x^2" in side_1:
                x2 = side_1.split("x^2")[0]
                if x2 == "" or x2 == "+":
                    x2 = 1
                elif x2 == "-":
                    x2 = -1
                side_1 = side_1.replace(x2 + "x^2", "")
                x2 = float(x2)
            if "x" in side_1:
                x1 = side_1.split("x")[0]
                if x1 == "" or x1 == "+":
                    x1 = 1
                elif x1 == "-":
                    x1 = -1
                side_1 = side_1.replace(x1 + "x", "")
                x1 = float(x1)
            if side_1:
                side_1 = float(side_1)
            else:
                side_1 = 0
            return (
                ((x1 * (-1)) + math.sqrt((x1**2) - (4) * (x2) * (side_1))) / (2 * x2)
            ), (((x1 * (-1)) - math.sqrt((x1**2) - (4) * (x2) * (side_1))) / (2 * x2))

        if operatorC == "ALG":
            algebra = input("What equation? (Format: ax ± b = c) ")
            print("x =", albr_slvr(algebra))
        elif operatorC == "QALG":
            algebra = input("What equation? (Format: ax^2 ± bx ± c = 0) ")
            print("x =", str(qabr_slvr(algebra)))
        elif operatorC == "A":
            memorydecider = input(
                "Choose from M1, M2, M3, and M4. Choose S to skip this step "
            )
            memorydeciderC = memorydecider.upper()
            if memorydeciderC == "M1":
                number2 = input("Second Number? ")
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                memoryANS = str(memory + number2).replace("j", "i")
                if "+ 0i" in memoryANS or "- 0i" in memoryANS or "0i" in memoryANS:
                    memoryANS = memoryANS.replace("+0i", "")
                    memoryANS = memoryANS.replace("-0i", "")
                    memoryANS = memoryANS.replace("0i", "")
                print("Your answer is:", memoryANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                equation = f"M1 + {number2}"
                equationcycle.insert(0, equation)
                savecycle.insert(0, memoryANS)
                if len(savecycle) > historylimit:
                    savecycle.pop()
                    equationcycle.pop()
                    continue
            if memorydeciderC == "M2":
                number2 = input("Second Number? ")
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                memory2ANS = str(memory2 + number2).replace("j", "i")
                if "+0i" in memory2ANS or "-0i" in memory2ANS or "0i" in memory2ANS:
                    memory2ANS = memory2ANS.replace("+0i", "")
                    memory2ANS = memory2ANS.replace("-0i", "")
                    memory2ANS = memory2ANS.replace("0i", "")
                print("Your answer is:", memory2ANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                equation = f"M2 + {number2}"
                equationcycle.insert(0, equation)
                savecycle.insert(0, memory2ANS)
                if len(savecycle) > historylimit:
                    savecycle.pop()
                    equationcycle.pop()
                continue
            if memorydeciderC == "M3":
                number2 = input("Second Number? ")
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                memory3ANS = str(memory3 + number2).replace("j", "i")
                if "+0i" in memory3ANS or "-0i" in memory3ANS or "0i" in memory3ANS:
                    memory3ANS = memory3ANS.replace("+0i", "")
                    memory3ANS = memory3ANS.replace("-0i", "")
                    memory3ANS = memory3ANS.replace("0i", "")
                print("Your answer is:", memory3ANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                equation = f"M3 + {number2}"
                equationcycle.insert(0, equation)
                savecycle.insert(0, memory3ANS)
                if len(savecycle) > historylimit:
                    savecycle.pop()
                    equationcycle.pop()
                continue
            if memorydeciderC == "M4":
                number2 = input("Second Number? ")
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                memory4ANS = str(memory4 + number2).replace("j", "i")
                if "+0i" in memory4ANS or "-0i" in memory4ANS or "0i" in memory4ANS:
                    memory4ANS = memory4ANS.replace("+0i", "")
                    memory4ANS = memory4ANS.replace("-0i", "")
                    memory4ANS = memory4ANS.replace("0i", "")
                print("Your answer is:", memory4ANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                equation = f"M4 + {number2}"
                equationcycle.insert(0, equation)
                savecycle.insert(0, memory4ANS)
                if len(savecycle) > historylimit:
                    savecycle.pop()
                    equationcycle.pop()
                continue
            if memorydeciderC == "S" or memorydeciderC == "s":
                number1 = input("Starting Number? ")
                number1 = str(number1).replace("i", "j")
                number1 = complex(number1)
                number2 = input("Second Number? ")
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                numberANS = str(number1 + number2).replace("j", "i")
                if "+0i" in numberANS or "-0i" in numberANS or "0i" in numberANS:
                    numberANS = numberANS.replace("+0i", "")
                    numberANS = numberANS.replace("-0i", "")
                    numberANS = numberANS.replace("0i", "")
                print("Your answer is:", numberANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                number1 = str(number1).replace("j", "i")
                if "+ 0i" in number1 or "- 0i" in number1 or "0i" in number1:
                    number1 = number1.replace("+0i", "")
                    number1 = number1.replace("-0i", "")
                    number1 = number1.replace("0i", "")
                equation = f"{number1} + {number2}"
                equationcycle.insert(0, equation)
                savecycle.insert(0, numberANS)
                if len(savecycle) > historylimit:
                    savecycle.pop()
                    equationcycle.pop()
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
                if "+0i" in memoryANS or "-0i" in memoryANS or "0i" in memoryANS:
                    memoryANS = memoryANS.replace("+0i", "")
                    memoryANS = memoryANS.replace("-0i", "")
                    memoryANS = memoryANS.replace("0i", "")
                print("Your answer is:", memoryANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memoryANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M1 - {number2}"
                continue
            if memorydeciderC == "M2":
                number2 = input("Second Number? ")
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                memory2ANS = str(memory2 - number2).replace("j", "i")
                if "+0i" in memory2ANS or "-0i" in memory2ANS or "0i" in memory2ANS:
                    memory2ANS = memory2ANS.replace("+0i", "")
                    memory2ANS = memory2ANS.replace("-0i", "")
                    memory2ANS = memory2ANS.replace("0i", "")
                print("Your answer is:", memory2ANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memory2ANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M2 - {number2}"
                continue
            if memorydeciderC == "M3":
                number2 = input("Second Number? ")
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                memory3ANS = str(memory3 - number2).replace("j", "i")
                if "+0i" in memory3ANS or "-0i" in memory3ANS or "0i" in memory3ANS:
                    memory3ANS = memory3ANS.replace("+0i", "")
                    memory3ANS = memory3ANS.replace("-0i", "")
                    memory3ANS = memory3ANS.replace("0i", "")
                print("Your answer is:", memory3ANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memory3ANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M3 - {number2}"
                continue
            if memorydeciderC == "M4":
                number2 = input("Second Number? ")
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                memory4ANS = str(memory4 - number2).replace("j", "i")
                if "+0i" in memory4ANS or "-0i" in memory4ANS or "0i" in memory4ANS:
                    memory4ANS = memory4ANS.replace("+0i", "")
                    memory4ANS = memory4ANS.replace("-0i", "")
                    memory4ANS = memory4ANS.replace("0i", "")
                print("Your answer is:", memory4ANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memory4ANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M4 - {number2}"
                continue
            if memorydeciderC == "S" or memorydeciderC == "s":
                number1 = input("Starting Number? ")
                number1 = str(number1).replace("i", "j")
                number1 = complex(number1)
                number2 = input("Second Number? ")
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                numberANS = str(number1 - number2).replace("j", "i")
                if "+0i" in numberANS or "-0i" in numberANS or "0i" in numberANS:
                    numberANS = numberANS.replace("+0i", "")
                    numberANS = numberANS.replace("-0i", "")
                    numberANS = numberANS.replace("0i", "")
                print("Your answer is:", numberANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                number1 = str(number1).replace("j", "i")
                if "+ 0i" in number1 or "- 0i" in number1 or "0i" in number1:
                    number1 = number1.replace("+0i", "")
                    number1 = number1.replace("-0i", "")
                    number1 = number1.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = numberANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"{number1} - {number2}"
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
                if "+0i" in memoryANS or "-0i" in memoryANS or "0i" in memoryANS:
                    memoryANS = memoryANS.replace("+0i", "")
                    memoryANS = memoryANS.replace("-0i", "")
                    memoryANS = memoryANS.replace("0i", "")
                print("Your answer is:", memoryANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memoryANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M1 * {number2}"
                continue
            if memorydeciderC == "M2":
                number2 = input("Second Number? ")
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                memory2ANS = str(memory2 * number2).replace("j", "i")
                if "+0i" in memory2ANS or "-0i" in memory2ANS or "0i" in memory2ANS:
                    memory2ANS = memory2ANS.replace("+0i", "")
                    memory2ANS = memory2ANS.replace("-0i", "")
                    memory2ANS = memory2ANS.replace("0i", "")
                print("Your answer is:", memory2ANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memory2ANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M2 * {number2}"
                continue
            if memorydeciderC == "M3":
                number2 = input("Second Number? ")
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                memory3ANS = str(memory3 * number2).replace("j", "i")
                if "+0i" in memory3ANS or "-0i" in memory3ANS or "0i" in memory3ANS:
                    memory3ANS = memory3ANS.replace("+0i", "")
                    memory3ANS = memory3ANS.replace("-0i", "")
                    memory3ANS = memory3ANS.replace("0i", "")
                print("Your answer is:", memory3ANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memory3ANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M3 * {number2}"
                continue
            if memorydeciderC == "M4":
                number2 = input("Second Number? ")
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                memory4ANS = str(memory4 * number2).replace("j", "i")
                if "+0i" in memory4ANS or "-0i" in memory4ANS or "0i" in memory4ANS:
                    memory4ANS = memory4ANS.replace("+0i", "")
                    memory4ANS = memory4ANS.replace("-0i", "")
                    memory4ANS = memory4ANS.replace("0i", "")
                print("Your answer is:", memory4ANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memory4ANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M4 * {number2}"
                continue
            if memorydeciderC == "S" or memorydeciderC == "s":
                number1 = input("Number to be multiplied? ")
                number1 = str(number1).replace("i", "j")
                number1 = complex(number1)
                number2 = input("Second Number? ")
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                numberANS = str(number1 * number2).replace("j", "i")
                if "+0i" in numberANS or "-0i" in numberANS or "0i" in numberANS:
                    numberANS = numberANS.replace("+0i", "")
                    numberANS = numberANS.replace("-0i", "")
                    numberANS = numberANS.replace("0i", "")
                print("Your answer is:", numberANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                number1 = str(number1).replace("j", "i")
                if "+ 0i" in number1 or "- 0i" in number1 or "0i" in number1:
                    number1 = number1.replace("+0i", "")
                    number1 = number1.replace("-0i", "")
                    number1 = number1.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = numberANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"{number1} * {number2}"
                continue
        elif operatorC == "D":
            memorydecider = input(
                "Choose from M1, M2, M3, and M4. Choose S to skip this step "
            )
            memorydeciderC = memorydecider.upper()
            if memorydeciderC == "M1":
                number2 = input("Divisor? ")
                number2 = number2.replace("i", "j")
                number2 = complex(number2)
                if number2 == 0:
                    print("Dividing by 0 can get you 60 years in math jail. ")
                    continue
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                memoryANS = str(memory / number2).replace("j", "i")
                if "+0i" in memoryANS or "-0i" in memoryANS or "0i" in memoryANS:
                    memoryANS = memoryANS.replace("+0i", "")
                    memoryANS = memoryANS.replace("-0i", "")
                    memoryANS = memoryANS.replace("0i", "")
                print("Your answer is:", memoryANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memoryANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M1 / {number2}"
                continue
            if memorydeciderC == "M2":
                number2 = input("Divisor? ")
                number2 = number2.replace("i", "j")
                number2 = complex(number2)
                if number2 == 0:
                    print("Dividing by 0 can get you 60 years in math jail. ")
                    continue
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                memory2ANS = str(memory2 / number2).replace("j", "i")
                if "+0i" in memory2ANS or "-0i" in memory2ANS or "0i" in memory2ANS:
                    memory2ANS = memory2ANS.replace("+0i", "")
                    memory2ANS = memory2ANS.replace("-0i", "")
                    memory2ANS = memory2ANS.replace("0i", "")
                print("Your answer is:", memory2ANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memory2ANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M2 / {number2}"
                continue
            if memorydeciderC == "M3":
                number2 = input("Divisor? ")
                number2 = number2.replace("i", "j")
                number2 = complex(number2)
                if number2 == 0:
                    print("Dividing by 0 can get you 60 years in math jail. ")
                    continue
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                memory3ANS = str(memory3 / number2).replace("j", "i")
                if "+0i" in memory3ANS or "-0i" in memory3ANS or "0i" in memory3ANS:
                    memory3ANS = memory3ANS.replace("+0i", "")
                    memory3ANS = memory3ANS.replace("-0i", "")
                    memory3ANS = memory3ANS.replace("0i", "")
                print("Your answer is:", memory3ANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memory3ANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M3 / {number2}"
                continue
            if memorydeciderC == "M4":
                number2 = input("Divisor? ")
                number2 = number2.replace("i", "j")
                number2 = complex(number2)
                if number2 == 0:
                    print("Dividing by 0 can get you 60 years in math jail. ")
                    continue
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                memory4ANS = str(memory4 / number2).replace("j", "i")
                if "+0i" in memory4ANS or "-0i" in memory4ANS or "0i" in memory4ANS:
                    memory4ANS = memory4ANS.replace("+0i", "")
                    memory4ANS = memory4ANS.replace("-0i", "")
                    memory4ANS = memory4ANS.replace("0i", "")
                print("Your answer is:", memory4ANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memory4ANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M4 / {number2}"
                continue
            if memorydeciderC == "S" or memorydeciderC == "s":
                number1 = input("Number to be divided? ")
                number1 = str(number1).replace("i", "j")
                number1 = complex(number1)
                number2 = input("Divisor? ")
                number2 = number2.replace("i", "j")
                number2 = complex(number2)
                if number2 == 0:
                    print("Dividing by 0 can get you 60 years in math jail. ")
                    continue
                numberANS = str(number1 / number2).replace("j", "i")
                if "+0i" in numberANS or "-0i" in numberANS or "0i" in numberANS:
                    numberANS = numberANS.replace("+0i", "")
                    numberANS = numberANS.replace("-0i", "")
                    numberANS = numberANS.replace("0i", "")
                print("Your answer is:", numberANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                number1 = str(number1).replace("j", "i")
                if "+ 0i" in number1 or "- 0i" in number1 or "0i" in number1:
                    number1 = number1.replace("+0i", "")
                    number1 = number1.replace("-0i", "")
                    number1 = number1.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = numberANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"{number1} / {number2}"
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
                if "+0i" in memoryANS or "-0i" in memoryANS or "0i" in memoryANS:
                    memoryANS = memoryANS.replace("+0i", "")
                    memoryANS = memoryANS.replace("-0i", "")
                    memoryANS = memoryANS.replace("0i", "")
                print("Your answer is:", memoryANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memoryANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M1 ^ {number2}"
                continue
            if memorydeciderC == "M2":
                number2 = input("Second Number? ")
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                memory2ANS = str(memory2**number2).replace("j", "i")
                if "+0i" in memory2ANS or "-0i" in memory2ANS or "0i" in memory2ANS:
                    memory2ANS = memory2ANS.replace("+0i", "")
                    memory2ANS = memory2ANS.replace("-0i", "")
                    memory2ANS = memory2ANS.replace("0i", "")
                print("Your answer is:", memory2ANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memory2ANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M2 ^ {number2}"
                continue
            if memorydeciderC == "M3":
                number2 = input("Second Number? ")
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                memory3ANS = str(memory3**number2).replace("j", "i")
                if "+0i" in memory3ANS or "-0i" in memory3ANS or "0i" in memory3ANS:
                    memory3ANS = memory3ANS.replace("+0i", "")
                    memory3ANS = memory3ANS.replace("-0i", "")
                    memory3ANS = memory3ANS.replace("0i", "")
                print("Your answer is:", memoryANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memory3ANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M3 ^ {number2}"
                continue
            if memorydeciderC == "S" or memorydeciderC == "s":
                number1 = input("What number? ")
                number1 = str(number1).replace("i", "j")
                number1 = complex(number1)
                number2 = input("What exponent? ")
                number2 = str(number2).replace("i", "j")
                number2 = complex(number2)
                numberANS = str(number1**number2).replace("j", "i")
                if "+0i" in numberANS or "-0i" in numberANS or "0i" in numberANS:
                    numberANS = numberANS.replace("+0i", "")
                    numberANS = numberANS.replace("-0i", "")
                    numberANS = numberANS.replace("0i", "")
                print("Your answer is:", numberANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                number1 = str(number1).replace("j", "i")
                if "+ 0i" in number1 or "- 0i" in number1 or "0i" in number1:
                    number1 = number1.replace("+0i", "")
                    number1 = number1.replace("-0i", "")
                    number1 = number1.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = numberANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"{number1} ^ {number2}"
                continue
            if number1 == 0 and number2 == 0:
                print("Error: 0^0 may land you 90 years in Math Jail")
        elif operatorC == "R":
            memorydecider = input(
                "Choose from M1, M2, M3, and M4. Choose S to skip this step "
            )
            memorydeciderC = memorydecider.upper()
            if memorydeciderC == "M1":
                number2 = float(input("Second Number? "))
                memoryANS = (memory + 0j) ** (1 / number2)
                memoryANS = str(memoryANS)
                memoryANS = memoryANS.replace("0j", "")
                print("Your answer is:", memoryANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memoryANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M1 ^ (1/{number2})"
                continue
            if memorydeciderC == "M2":
                number2 = float(input("Second Number? "))
                memory2ANS = (memory2 + 0j) ** (1 / number2)
                memory2ANS = str(memory2ANS)
                memory2ANS = memory2ANS.replace("0j", "")
                print("Your answer is:", memory2ANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memory2ANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M2 ^ (1/{number2})"
                continue
            if memorydeciderC == "M3":
                number2 = float(input("Second Number? "))
                memory3ANS = (memory + 0j) ** (1 / number2)
                memory3ANS = str(memory3ANS)
                memory3ANS = memory3ANS.replace("0j", "")
                print("Your answer is:", memory3ANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memory3ANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M3 ^ (1/{number2})"
                continue
            if memorydeciderC == "M4":
                number2 = float(input("Second Number? "))
                memory4ANS = (memory4 + 0j) ** (1 / number2)
                memory4ANS = str(memory4ANS)
                memory4ANS = memory4ANS.replace("0j", "")
                print("Your answer is:", memory4ANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = memory4ANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"M4 ^ (1/{number2})"
                continue
            if memorydeciderC == "S" or memorydeciderC == "s":
                number1 = float(input("What number? "))
                number2 = float(
                    input(
                        "What level of rooting? (2 for squaring, 3 for cubing etc... )"
                    )
                )
                numberANS = (number1 + 0j) ** (1 / number2)
                numberANS = str(numberANS)
                numberANS = numberANS.replace("0j", "")
                print("Your answer is:", numberANS)
                number2 = str(number2).replace("j", "i")
                if "+ 0i" in number2 or "- 0i" in number2 or "0i" in number2:
                    number2 = number2.replace("+0i", "")
                    number2 = number2.replace("-0i", "")
                    number2 = number2.replace("0i", "")
                number1 = str(number1).replace("j", "i")
                if "+ 0i" in number1 or "- 0i" in number1 or "0i" in number1:
                    number1 = number1.replace("+0i", "")
                    number1 = number1.replace("-0i", "")
                    number1 = number1.replace("0i", "")
                savecycle3 = savecycle2
                savecycle2 = savecycle1
                savecycle1 = numberANS
                equationcycle3 = equationcycle2
                equationcycle2 = equationcycle1
                equationcycle1 = f"{number1} ^ (1/{number2})"
                continue
            if number2 < 2:
                print(
                    "Error: Rooting in such a way can get 8 generations of your family in Math Jail"
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
            number1 = float(input("First Number? "))
            number2 = float(input("Second Number? "))
            if number2 == 0:
                print("Divided by 0, United by Math Jail")
            else:
                number3 = number1 % number2
                print("Your answer is", number3)
        elif operatorC == "SIN":
            memorydecider = input(
                "Choose from M1, M2, M3, and M4. Choose S to skip this step "
            )
            memorydeciderC = memorydecider.upper()
            if memorydeciderC == "M1":
                if angleUnit == "DEG":
                    memoryDEG = cmath.sin(degs(memory))
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    print("Your answer is:", memoryDEG)
                    equation = f"sin(M1) (Degrees)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "RAD":
                    memoryDEG = cmath.sin(memory)
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"sin(M1) (Radians)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "NOD":
                    decidertrig = input("(Deg)rees or (Rad)ians? ")
                    decidertrigC = decidertrig.upper()
                    if decidertrigC == "DEG":
                        memoryDEG = cmath.sin(degs(memory))
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                            print("Your answer is:", memoryDEG)
                            memoryDEG = cmath.sin(degs(memory))
                            memoryDEG = str(memoryDEG).replace("j", "i")
                            equation = f"sin(M1) (Degrees)"
                            equationcycle.insert(0, equation)
                            savecycle.insert(0, memoryDEG)
                            if len(savecycle) > historylimit:
                                savecycle.pop()
                                equationcycle.pop()
                                continue
                    elif decidertrigC == "RAD":
                        print("Your answer is:", cmath.sin(memory))
                        memoryDEG = cmath.sin(memory)
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"sin(M1) (Radians)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    else:
                        print("Invalid Choice = Invalid Brain")
                        continue
            if memorydeciderC == "M2":
                if angleUnit == "DEG":
                    memoryDEG = cmath.sin(math.radians(memory2))
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"sin(M2) (Degrees)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "RAD":
                    memoryDEG = cmath.sin(memory2)
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"sin(M2) (Radians)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "NOD":
                    decidertrig = input("(Deg)rees or (Rad)ians? ")
                    decidertrigC = decidertrig.upper()
                    if decidertrigC == "DEG":
                        memoryDEG = cmath.sin(math.radians(memory2))
                        print("Your answer is:", memoryDEG)
                        memoryDEG = cmath.sin(math.radians(memory2))
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"sin(M2) (Degrees)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    elif decidertrigC == "RAD":
                        print("Your answer is:", cmath.sin(memory2))
                        memoryDEG = cmath.sin(memory2)
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"sin(M2) (Radians)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    else:
                        print("Invalid Choice = Invalid Brain")
                        continue
            if memorydeciderC == "M3":
                if angleUnit == "DEG":
                    memoryDEG = cmath.sin(math.radians(memory3))
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"sin(M3) (Degrees)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "RAD":
                    memoryDEG = cmath.sin(memory3)
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"sin(M3) (Radians)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "NOD":
                    decidertrig = input("(Deg)rees or (Rad)ians? ")
                    decidertrigC = decidertrig.upper()
                    if decidertrigC == "DEG":
                        memoryDEG = cmath.sin(math.radians(memory3))
                        print("Your answer is:", memoryDEG)
                        memoryDEG = cmath.sin(math.radians(memory3))
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"sin(M3) (Degrees)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    elif decidertrigC == "RAD":
                        print("Your answer is:", cmath.sin(memory3))
                        memoryDEG = cmath.sin(memory3)
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"sin(M3) (Radians)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    else:
                        print("Invalid Choice = Invalid Brain")
                        continue
            if memorydeciderC == "M4":
                if angleUnit == "DEG":
                    memoryDEG = cmath.sin(math.radians(memory4))
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"sin(M4) (Degrees)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "RAD":
                    memoryDEG = cmath.sin(memory4)
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"sin(M4) (Radians)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "NOD":
                    decidertrig = input("(Deg)rees or (Rad)ians? ")
                    decidertrigC = decidertrig.upper()
                    if decidertrigC == "DEG":
                        memoryDEG = cmath.sin(math.radians(memory4))
                        print("Your answer is:", memoryDEG)
                        memoryDEG = cmath.sin(math.radians(memory4))
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"sin(M4) (Degrees)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    elif decidertrigC == "RAD":
                        print("Your answer is:", cmath.sin(memory4))
                        memoryDEG = cmath.sin(memory4)
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"sin(M4) (Radians)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    else:
                        print("Invalid Choice = Invalid Brain")
                        continue
            if memorydeciderC == "S" or memorydeciderC == "s":
                number1 = float(input("What number? "))
                if angleUnit == "DEG":
                    memoryDEG = cmath.sin(math.radians(number1))
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"sin({number1}) (Degrees)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "RAD":
                    memoryDEG = cmath.sin(number1)
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"sin({number1}) (Radians)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "NOD":
                    decidertrig = input("(Deg)rees or (Rad)ians? ")
                    decidertrigC = decidertrig.upper()
                    if decidertrigC == "DEG":
                        memoryDEG = cmath.sin(math.radians(number1))
                        print("Your answer is:", memoryDEG)
                        memoryDEG = cmath.sin(math.radians(number1))
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"sin({number1}) (Degrees)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    elif decidertrigC == "RAD":
                        print("Your answer is:", cmath.sin(number1))
                        memoryDEG = cmath.sin(number1)
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"sin({number1}) (Radians)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    else:
                        print("Invalid Choice = Invalid Brain")
                        continue
            if memorydeciderC not in [
                "M1",
                "M2",
                "M3",
                "M4",
                "S",
            ] or decidertrigC not in [
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
                if angleUnit == "DEG":
                    memoryDEG = cmath.cos(math.radians(memory))
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"cos(M1) (Degrees)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "RAD":
                    memoryDEG = cmath.cos(memory)
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"cos(M1) (Radians)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "NOD":
                    decidertrig = input("(Deg)rees or (Rad)ians? ")
                    decidertrigC = decidertrig.upper()
                    if decidertrigC == "DEG":
                        memoryDEG = cmath.cos(math.radians(memory))
                        print("Your answer is:", memoryDEG)
                        memoryDEG = cmath.cos(math.radians(memory))
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"cos(M1) (Degrees)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    elif decidertrigC == "RAD":
                        print("Your answer is:", cmath.cos(memory))
                        memoryDEG = cmath.cos(memory)
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"cos(M1) (Radians)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    else:
                        print("Invalid Choice = Invalid Brain")
                        continue
            if memorydeciderC == "M2":
                if angleUnit == "DEG":
                    memoryDEG = cmath.cos(math.radians(memory2))
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"cos(M2) (Degrees)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "RAD":
                    memoryDEG = cmath.cos(memory2)
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"cos(M2) (Radians)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "NOD":
                    decidertrig = input("(Deg)rees or (Rad)ians? ")
                    decidertrigC = decidertrig.upper()
                    if decidertrigC == "DEG":
                        memoryDEG = cmath.cos(math.radians(memory2))
                        print("Your answer is:", memoryDEG)
                        memoryDEG = cmath.cos(math.radians(memory2))
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"cos(M2) (Degrees)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    elif decidertrigC == "RAD":
                        print("Your answer is:", cmath.cos(memory2))
                        memoryDEG = cmath.cos(memory2)
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"cos(M2) (Radians)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    else:
                        print("Invalid Choice = Invalid Brain")
                        continue
            if memorydeciderC == "M3":
                if angleUnit == "DEG":
                    memoryDEG = cmath.cos(math.radians(memory3))
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"cos(M3) (Degrees)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "RAD":
                    memoryDEG = cmath.cos(memory3)
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"cos(M3) (Radians)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "NOD":
                    decidertrig = input("(Deg)rees or (Rad)ians? ")
                    decidertrigC = decidertrig.upper()
                    if decidertrigC == "DEG":
                        memoryDEG = cmath.cos(math.radians(memory3))
                        print("Your answer is:", memoryDEG)
                        memoryDEG = cmath.cos(math.radians(memory3))
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"cos(M3) (Degrees)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    elif decidertrigC == "RAD":
                        print("Your answer is:", cmath.cos(memory3))
                        memoryDEG = cmath.cos(memory3)
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"cos(M3) (Radians)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    else:
                        print("Invalid Choice = Invalid Brain")
                        continue
            if memorydeciderC == "M4":
                if angleUnit == "DEG":
                    memoryDEG = cmath.cos(math.radians(memory4))
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"cos(M4) (Degrees)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "RAD":
                    memoryDEG = cmath.cos(memory4)
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"cos(M4) (Radians)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "NOD":
                    decidertrig = input("(Deg)rees or (Rad)ians? ")
                    decidertrigC = decidertrig.upper()
                    if decidertrigC == "DEG":
                        memoryDEG = cmath.cos(math.radians(memory4))
                        print("Your answer is:", memoryDEG)
                        memoryDEG = cmath.cos(math.radians(memory4))
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"cos(M4) (Degrees)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    elif decidertrigC == "RAD":
                        print("Your answer is:", cmath.cos(memory4))
                        memoryDEG = cmath.cos(memory4)
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"cos(M4) (Radians)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    else:
                        print("Invalid Choice = Invalid Brain")
                        continue
            if memorydeciderC == "S" or memorydeciderC == "s":
                number1 = float(input("What number? "))
                if angleUnit == "DEG":
                    memoryDEG = cmath.cos(math.radians(number1))
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"cos({number1}) (Degrees)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "RAD":
                    memoryDEG = cmath.cos(number1)
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"cos({number1}) (Radians)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "NOD":
                    decidertrig = input("(Deg)rees or (Rad)ians? ")
                    decidertrigC = decidertrig.upper()
                    if decidertrigC == "DEG":
                        memoryDEG = cmath.cos(math.radians(number1))
                        print("Your answer is:", memoryDEG)
                        memoryDEG = cmath.cos(math.radians(number1))
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"cos({number1}) (Degrees)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    elif decidertrigC == "RAD":
                        print("Your answer is:", cmath.cos(number1))
                        memoryDEG = cmath.cos(number1)
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"cos({number1}) (Radians)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    else:
                        print("Invalid Choice = Invalid Brain")
                        continue
            if memorydeciderC not in [
                "M1",
                "M2",
                "M3",
                "M4",
                "S",
            ] or decidertrigC not in [
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
                if angleUnit == "DEG":
                    memoryDEG = cmath.tan(math.radians(memory))
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"tan(M1) (Degrees)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "RAD":
                    memoryDEG = cmath.tan(memory)
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"tan(M1) (Radians)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "NOD":
                    decidertrig = input("(Deg)rees or (Rad)ians? ")
                    decidertrigC = decidertrig.upper()
                    if decidertrigC == "DEG":
                        memoryDEG = cmath.tan(math.radians(memory))
                        print("Your answer is:", memoryDEG)
                        memoryDEG = cmath.tan(math.radians(memory))
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"tan(M1) (Degrees)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    elif decidertrigC == "RAD":
                        print("Your answer is:", cmath.tan(memory))
                        memoryDEG = cmath.tan(memory)
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"tan(M1) (Radians)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    else:
                        print("Invalid Choice = Invalid Brain")
                        continue
            if memorydeciderC == "M2":
                if angleUnit == "DEG":
                    memoryDEG = cmath.tan(math.radians(memory2))
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"tan(M2) (Degrees)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "RAD":
                    memoryDEG = cmath.tan(memory2)
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"tan(M2) (Radians)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "NOD":
                    decidertrig = input("(Deg)rees or (Rad)ians? ")
                    decidertrigC = decidertrig.upper()
                    if decidertrigC == "DEG":
                        memoryDEG = cmath.tan(math.radians(memory2))
                        print("Your answer is:", memoryDEG)
                        memoryDEG = cmath.tan(math.radians(memory2))
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"tan(M2) (Degrees)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    elif decidertrigC == "RAD":
                        print("Your answer is:", cmath.tan(memory2))
                        memoryDEG = cmath.tan(memory2)
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"tan(M2) (Radians)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    else:
                        print("Invalid Choice = Invalid Brain")
                        continue
            if memorydeciderC == "M3":
                if angleUnit == "DEG":
                    memoryDEG = cmath.tan(math.radians(memory3))
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"tan(M3) (Degrees)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "RAD":
                    memoryDEG = cmath.tan(memory3)
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"tan(M3) (Radians)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "NOD":
                    decidertrig = input("(Deg)rees or (Rad)ians? ")
                    decidertrigC = decidertrig.upper()
                    if decidertrigC == "DEG":
                        memoryDEG = cmath.tan(math.radians(memory3))
                        print("Your answer is:", memoryDEG)
                        memoryDEG = cmath.tan(math.radians(memory3))
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"tan(M3) (Degrees)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    elif decidertrigC == "RAD":
                        print("Your answer is:", cmath.tan(memory3))
                        memoryDEG = cmath.tan(memory3)
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"tan(M3) (Radians)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    else:
                        print("Invalid Choice = Invalid Brain")
                        continue
            if memorydeciderC == "M4":
                if angleUnit == "DEG":
                    memoryDEG = cmath.tan(math.radians(memory4))
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"tan(M4) (Degrees)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "RAD":
                    memoryDEG = cmath.tan(memory4)
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"tan(M4) (Radians)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "NOD":
                    decidertrig = input("(Deg)rees or (Rad)ians? ")
                    decidertrigC = decidertrig.upper()
                    if decidertrigC == "DEG":
                        memoryDEG = cmath.tan(math.radians(memory4))
                        print("Your answer is:", memoryDEG)
                        memoryDEG = cmath.tan(math.radians(memory4))
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"tan(M4) (Degrees)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    elif decidertrigC == "RAD":
                        print("Your answer is:", cmath.tan(memory4))
                        memoryDEG = cmath.tan(memory4)
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"tan(M4) (Radians)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    else:
                        print("Invalid Choice = Invalid Brain")
                        continue
            if memorydeciderC == "S" or memorydeciderC == "s":
                number1 = float(input("What number? "))
                if angleUnit == "DEG":
                    memoryDEG = cmath.tan(math.radians(number1))
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"tan({number1}) (Degrees)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "RAD":
                    memoryDEG = cmath.tan(number1)
                    print("Your answer is:", memoryDEG)
                    memoryDEG = str(memoryDEG).replace("j", "i")
                    if "+ 0i" in memoryDEG or "- 0i" in memoryDEG or "0i" in memoryDEG:
                        memoryDEG = memoryDEG.replace("+0i", "")
                        memoryDEG = memoryDEG.replace("-0i", "")
                        memoryDEG = memoryDEG.replace("0i", "")
                    equation = f"tan({number1}) (Radians)"
                    equationcycle.insert(0, equation)
                    savecycle.insert(0, memoryDEG)
                    if len(savecycle) > historylimit:
                        savecycle.pop()
                        equationcycle.pop()
                    continue
                elif angleUnit == "NOD":
                    decidertrig = input("(Deg)rees or (Rad)ians? ")
                    decidertrigC = decidertrig.upper()
                    if decidertrigC == "DEG":
                        memoryDEG = cmath.tan(math.radians(number1))
                        print("Your answer is:", memoryDEG)
                        memoryDEG = cmath.tan(math.radians(number1))
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"tan({number1}) (Degrees)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    elif decidertrigC == "RAD":
                        print("Your answer is:", cmath.tan(number1))
                        memoryDEG = cmath.tan(number1)
                        memoryDEG = str(memoryDEG).replace("j", "i")
                        if (
                            "+ 0i" in memoryDEG
                            or "- 0i" in memoryDEG
                            or "0i" in memoryDEG
                        ):
                            memoryDEG = memoryDEG.replace("+0i", "")
                            memoryDEG = memoryDEG.replace("-0i", "")
                            memoryDEG = memoryDEG.replace("0i", "")
                        equation = f"tan({number1}) (Radians)"
                        equationcycle.insert(0, equation)
                        savecycle.insert(0, memoryDEG)
                        if len(savecycle) > historylimit:
                            savecycle.pop()
                            equationcycle.pop()
                            continue
                    else:
                        print("Invalid Choice = Invalid Brain")
                        continue
            if memorydeciderC not in [
                "M1",
                "M2",
                "M3",
                "M4",
                "S",
            ] or decidertrigC not in [
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
            if memorydeciderC not in [
                "M1",
                "M2",
                "M3",
                "M4",
                "S",
            ] or decidertrigC not in [
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
            if memorydeciderC not in [
                "M1",
                "M2",
                "M3",
                "M4",
                "S",
            ] or decidertrigC not in [
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
            if memorydeciderC not in [
                "M1",
                "M2",
                "M3",
                "M4",
                "S",
            ] or decidertrigC not in [
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
            if memorydeciderC not in [
                "M1",
                "M2",
                "M3",
                "M4",
                "S",
            ] or decidertrigC not in [
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
            if memorydeciderC not in [
                "M1",
                "M2",
                "M3",
                "M4",
                "S",
            ] or decidertrigC not in [
                "DEG",
                "RAD",
            ]:
                print("Invalid Choice = Invalid Brain")
        elif operatorC == "TANH":
            memorydecider = input(
                "Choose from M1, M2, M3, and M4. Choose S to skip this step "
            )
            memorydeciderC = memorydecider.upper()
            if memorydeciderC == "M1":
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.tanh(math.radians(memory))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.tanh(memory))
                    continue
            if memorydeciderC == "M2":
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.tanh(math.radians(memory2))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.tanh(memory2))
                    continue
            if memorydeciderC == "M3":
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.tanh(math.radians(memory3))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.tanh(memory3))
                    continue
            if memorydeciderC == "M4":
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.tanh(math.radians(memory4))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.tanh(memory4))
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
            if memorydeciderC not in [
                "M1",
                "M2",
                "M3",
                "M4",
                "S",
            ] or decidertrigC not in [
                "DEG",
                "RAD",
            ]:
                print("Invalid Choice = Invalid Brain")
        elif operatorC == "ARCSINH":
            memorydecider = input(
                "Choose from M1, M2, M3, and M4. Choose S to skip this step "
            )
            memorydeciderC = memorydecider.upper()
            if memorydeciderC == "M1":
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.asinh(math.radians(memory))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.asinh(memory))
                    continue
            if memorydeciderC == "M2":
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.asinh(math.radians(memory2))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.asinh(memory2))
                    continue
            if memorydeciderC == "M3":
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.asinh(math.radians(memory3))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.asinh(memory3))
                    continue
            if memorydeciderC == "M4":
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.asinh(math.radians(memory4))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.asinh(memory4))
                    continue
            if memorydeciderC == "S" or memorydeciderC == "s":
                number1 = float(input("What number? "))
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.asinh(math.radians(number1))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.asinh(number1))
                    continue
        elif operatorC == "ARCCOSH":
            memorydecider = input(
                "Choose from M1, M2, M3, and M4. Choose S to skip this step "
            )
            memorydeciderC = memorydecider.upper()
            if memorydeciderC == "M1":
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.acosh(math.radians(memory))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.acosh(memory))
                    continue
            if memorydeciderC == "M2":
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.acosh(math.radians(memory2))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.acosh(memory2))
                    continue
            if memorydeciderC == "M3":
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.acosh(math.radians(memory3))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.acosh(memory3))
                    continue
            if memorydeciderC == "M4":
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.acosh(math.radians(memory4))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.acosh(memory4))
                    continue
            if memorydeciderC == "S" or memorydeciderC == "s":
                number1 = float(input("What number? "))
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.acosh(math.radians(number1))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.acosh(number1))
                    continue
        elif operatorC == "ARCTANH":
            memorydecider = input(
                "Choose from M1, M2, M3, and M4. Choose S to skip this step "
            )
            memorydeciderC = memorydecider.upper()
            if memorydeciderC == "M1":
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.atanh(math.radians(memory))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.atanh(memory))
                    continue
            if memorydeciderC == "M2":
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.atanh(math.radians(memory2))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.atanh(memory2))
                    continue
            if memorydeciderC == "M3":
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.atanh(math.radians(memory3))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.atanh(memory3))
                    continue
            if memorydeciderC == "M4":
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.atanh(math.radians(memory4))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.atanh(memory4))
                    continue
            if memorydeciderC == "S" or memorydeciderC == "s":
                number1 = float(input("What number? "))
                decidertrig = input("(Deg)rees or (Rad)ians? ")
                decidertrigC = decidertrig.upper()
                if decidertrigC == "DEG":
                    memoryDEG = math.atanh(math.radians(number1))
                    print("Your answer is:", memoryDEG)
                    continue
                elif decidertrigC == "RAD":
                    print("Your answer is:", math.atanh(number1))
                    continue
        elif operatorC == "HIST":
            print("=== History ===")
            for i in range(len(savecycle)):
                print(f"{i+1}) {equationcycle[i]} = {savecycle[i]}")
            continue
        elif operatorC == "CLEAR":
            savecycle.clear()
            equationcycle.clear()
            print("bye bye history (never coming back)")
            continue
        elif operatorC == "RAND":
            number1 = int(input("Lower Bound? "))
            number2 = int(input("Upper Bound? "))
            randomnum = random.randint(number1, number2)
            print(randomnum)
            savecycle3 = savecycle2
            savecycle2 = savecycle1
            savecycle1 = randomnum
            equationcycle3 = equationcycle2
            equationcycle2 = equationcycle1
            equationcycle1 = f"Random: {number1} to {number2} "
            continue
        elif operatorC == "EXP":
            historydecider = input("Export History, Memory, or both? (H/M/B) ")
            historydeciderC = historydecider.upper()
            if historydeciderC == "H":
                filename = input(
                    "What directory? (please end with .txt and start from C:/) "
                )
                try:
                    with open(filename, "w") as file:
                        file.write("Magic Calculator History Export\n")
                        file.write("===============================\n")
                        file.write(
                            f"Exported at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                        )
                        file.write("===============================\n")
                        for i in range(len(savecycle)):
                            file.write(f"{i+1}) {equationcycle[i]} = {savecycle[i]}\n")
                    print("Success!")
                    continue
                except Exception:
                    print(
                        "(Error Code 16) either you forgot to put .txt (80 years in math jail) or something went horribly wrong"
                    )
            elif historydeciderC == "M":
                filename = input(
                    "What directory? (please end with .txt and start from C:/) "
                )
                try:
                    with open(filename, "w") as file:
                        file.write("Magic Calculator Memory Export\n")
                        file.write("===============================\n")
                        file.write(
                            f"Exported at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                        )
                        file.write("===============================\n")
                        file.write(
                            f"Memory 1: {str(memory).replace('j', 'i').replace('+0i','').replace('-0i','').replace('0i','')}\n"
                        )
                        file.write(
                            f"Memory 2: {str(memory2).replace('j', 'i').replace('+0i','').replace('-0i','').replace('0i','')}\n"
                        )
                        file.write(
                            f"Memory 3: {str(memory3).replace('j', 'i').replace('+0i','').replace('-0i','').replace('0i','')}\n"
                        )
                        file.write(
                            f"Memory 4: {str(memory4).replace('j', 'i').replace('+0i','').replace('-0i','').replace('0i','')}\n"
                        )
                    print("Success!")
                    continue
                except Exception:
                    print(
                        "(Error Code 16) either you forgot to put .txt (80 years in math jail) or something went horribly wrong"
                    )
            elif historydeciderC == "B":
                filename = input(
                    "What directory? (please end with .txt and start from C:/) "
                )
                try:
                    with open(filename, "w") as file:
                        file.write("Magic Calculator Export\n")
                        file.write("===============================\n")
                        file.write(
                            f"Exported at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                        )
                        file.write("===============================\n")
                        file.write(
                            f"Memory 1: {str(memory).replace('j', 'i').replace('+0i','').replace('-0i','').replace('0i','')}\n"
                        )
                        file.write(
                            f"Memory 2: {str(memory2).replace('j', 'i').replace('+0i','').replace('-0i','').replace('0i','')}\n"
                        )
                        file.write(
                            f"Memory 3: {str(memory3).replace('j', 'i').replace('+0i','').replace('-0i','').replace('0i','')}\n"
                        )
                        file.write(
                            f"Memory 4: {str(memory4).replace('j', 'i').replace('+0i','').replace('-0i','').replace('0i','')}\n"
                        )
                        for i in range(len(savecycle)):
                            file.write(f"{i+1}) {equationcycle[i]} = {savecycle[i]}\n")
                    print("Success!")
                    continue
                except Exception:
                    print(
                        "(Error Code 16) either you forgot to put .txt (80 years in math jail) or something went horribly wrong"
                    )
                    continue
                else:
                    print("Invalid Choice = Invalid Brain")
                    continue
        elif operatorC == "ACC":
            decideracc = input(
                "Login, ID Search, Create, Change Username, Change Password, Change Deescription, or Delete Account? (L/ID/C/CU/CP/CD/DA) "
            )
            decideraccC = decideracc.upper()
            if decideraccC == "C":

                def createaccount():
                    while True:
                        createdname = input("What username? ")
                        cursor.execute(
                            "SELECT * FROM accountsList WHERE accounts = ?",
                            (createdname,),
                        )
                        if cursor.fetchone():
                            print("Beep Boop, username error")
                        else:
                            break
                    createdpassword = input("What password? ")
                    salt = os.urandom(16)
                    hashedpassword = hashlib.scrypt(
                        ((createdpassword).encode("utf-8")),
                        salt=salt,
                        n=8192,
                        r=2,
                        p=1,
                        dklen=128,
                    )
                    description = input(
                        "Would you like to have a description? (can put email, links, anything) "
                    )
                    cursor.execute(
                        "INSERT INTO accountsList (accounts, password, salt, description) VALUES (?, ?, ?, ?)",
                        (createdname, hashedpassword, salt, description),
                    )
                    cursor.execute(
                        "SELECT id FROM accountsList WHERE accounts = ?", (createdname,)
                    )
                    createdid = cursor.fetchone()
                    createdid = createdid[0]
                    print(f"Success! User ID is {createdid}")
                    datawire.commit()

                createaccount()
            elif decideraccC == "L":
                inputusername = input("What username? ")
                inputpassword = input("What password? ")
                cursor.execute(
                    "SELECT salt FROM accountsList WHERE accounts = ?", (inputusername,)
                )
                saltfetch = cursor.fetchone()
                if saltfetch is None:
                    print("Invalid Username: get thrown into 500 years of math jail")
                else:
                    saltfetch = saltfetch[0]
                    hashedinputpassword = hashlib.scrypt(
                        ((inputpassword).encode("utf-8")),
                        salt=saltfetch,
                        n=8192,
                        r=2,
                        p=1,
                        dklen=128,
                    )
                    cursor.execute(
                        "SELECT password FROM accountsList WHERE accounts = ?",
                        (inputusername,),
                    )
                    passwordfetch = cursor.fetchone()
                    passwordfetch = passwordfetch[0]
                    cursor.execute(
                        "SELECT id FROM accountsList WHERE accounts = ?",
                        (inputusername,),
                    )
                    idfetch = cursor.fetchone()
                    idfetch = idfetch[0]
                    if passwordfetch == hashedinputpassword:
                        print(
                            f"Login success! Now logged in to {inputusername} (id {idfetch})"
                        )
                        loggedin = True
                        accountin = inputusername
                        salt = os.urandom(16)
                        datawire.commit()
                    else:
                        print(
                            "This probably isnt't even your account (900 years in math jail) "
                        )
            elif decideraccC == "ID":
                idinput = input("What ID? ")
                cursor.execute(
                    "SELECT accounts, description FROM accountsList WHERE id = ?",
                    (idinput,),
                )
                fetched = cursor.fetchone()
                if fetched:
                    Username = fetched[0]
                    Description = fetched[1]
                    print(f"Username = {Username}, Description = {Description}")
            elif decideraccC == "CU":
                if loggedin == True:
                    createdname = input("What name? ")
                    cursor.execute(
                        "UPDATE accountsList SET accounts = ? WHERE accounts = ?",
                        (createdname, accountin),
                    )
                    createdname = createdname[0]
                    accountin = createdname
                    datawire.commit()
                else:
                    print(
                        "Error: Looks like you tried to change the username of [nonexistent account]!"
                    )
            elif decideraccC == "CP":
                if loggedin == True:
                    inputusername = input("What username? ")
                    inputpassword = input("What's the old password? ")
                    cursor.execute(
                        "SELECT salt FROM accountsList WHERE accounts = ?",
                        (inputusername,),
                    )
                    saltfetch = cursor.fetchone()
                    if saltfetch is None:
                        print(
                            "Invalid Username: get thrown into 500 years of math jail"
                        )
                    else:
                        saltfetch = saltfetch[0]
                        hashedinputpassword = hashlib.scrypt(
                            ((inputpassword).encode("utf-8")),
                            salt=saltfetch,
                            n=8192,
                            r=2,
                            p=1,
                            dklen=128,
                        )
                        cursor.execute(
                            "SELECT password FROM accountsList WHERE accounts = ?",
                            (inputusername,),
                        )
                        passwordfetch = cursor.fetchone()
                        passwordfetch = passwordfetch[0]
                        cursor.execute(
                            "SELECT id FROM accountsList WHERE accounts = ?",
                            (inputusername,),
                        )
                        idfetch = cursor.fetchone()
                        idfetch = idfetch[0]
                        if passwordfetch == hashedinputpassword:
                            print(f"Verification Success!")
                            newpassword = input("What new password will you pick? ")
                            hashednewpassword = hashlib.scrypt(
                                ((newpassword).encode("utf-8")),
                                salt=saltfetch,
                                n=8192,
                                r=2,
                                p=1,
                                dklen=128,
                            )
                            hashednewpassword = hashednewpassword.strip()
                            cursor.execute(
                                "UPDATE accountsList SET password = ? WHERE accounts = ?",
                                (
                                    hashednewpassword,
                                    inputusername,
                                ),
                            )
                            accountin = inputusername
                            salt = os.urandom(16)
                            datawire.commit()
                        else:
                            print(
                                "This probably isnt't even your account (900 years in math jail) "
                            )
                else:
                    print("Trying to change passwords of nonexistent?")
            elif decideraccC == "CD":
                if loggedin == True:
                    newdescription = input("What description? ")
                    cursor.execute(
                        "UPDATE accountsList SET description = ? WHERE accounts = ?",
                        (
                            newdescription,
                            accountin,
                        ),
                    )
                    newdescription = newdescription[0]
                    datawire.commit()
                else:
                    print("[add placeholder into code after dinner]")
            elif decideraccC == "DA":
                if loggedin == True:
                    inputusername = input("What username? ")
                    inputpassword = input("What's the password? ")
                    cursor.execute(
                        "SELECT salt FROM accountsList WHERE accounts = ?",
                        (inputusername,),
                    )
                    saltfetch = cursor.fetchone()
                    if saltfetch is None:
                        print(
                            "Invalid Username: get thrown into 500 years of math jail"
                        )
                    else:
                        saltfetch = saltfetch[0]
                        hashedinputpassword = hashlib.scrypt(
                            ((inputpassword).encode("utf-8")),
                            salt=saltfetch,
                            n=8192,
                            r=2,
                            p=1,
                            dklen=128,
                        )
                        cursor.execute(
                            "SELECT password FROM accountsList WHERE accounts = ?",
                            (inputusername,),
                        )
                        passwordfetch = cursor.fetchone()
                        passwordfetch = passwordfetch[0]
                        cursor.execute(
                            "SELECT id FROM accountsList WHERE accounts = ?",
                            (inputusername,),
                        )
                        idfetch = cursor.fetchone()
                        idfetch = idfetch[0]
                        if passwordfetch == hashedinputpassword:
                            print(f"Bye bye account")
                            cursor.execute(
                                "DELETE FROM accountsList WHERE accounts = ?",
                                (inputusername,),
                            )
                            datawire.commit()
                        else:
                            print(
                                "This probably isnt't even your account (900 years in math jail) "
                            )
        if operator == "SignIn":
            print(
                "Bonus code found! Go to the repository and share the code for v4.0: Account40"
            )
            continue
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
                "DTB",
                "DTH",
                "DTO",
                "KTP",
                "PTK",
                "FTM",
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
                "ARCSINH",
                "LOG",
                "R",
                "E",
                "ALG",
                "QALG",
                "ACC",
            ]
            or operatorC
            in [
                "C",
                "ME1",
                "ME2",
                "ME3",
                "ME4",
                "MI",
                "MRA",
                "MR1",
                "MR2",
                "MR3",
                "MR4",
                "HIS",
                "RAND",
                "CMD",
                "CMD1",
            ]
        ):
            continue
        else:
            print(
                f"Invalid: The rise and fall of Atuyeyi Operation. ({operator} is NOT valid.)"
            )
    except ValueError:
        print(
            "(Error Code 12) alphabet + mathematics = AUTOMATIC LIFE SENTENCE IN MATH JAIL"
        )
        continue
    except ZeroDivisionError:
        print("(Error Code 13) DIVIDING BY 0 IS A CRIME AGAINST HUMANITY")
        continue
    except FileNotFoundError:
        print(
            "(Error Code 14) NONEXISTENT FILE: YOUR NEXT 6 DESCENDANTS COME TO MATH JAIL"
        )
        continue
    except Exception as e:
        print(
            f"(Error Code 15) Something went horribly wrong. Please report the bug as {e}. If needed, launch in debug mode."
        )
        continue
