Task1
length = int(input("Enter the length of the zander in centimeters: "))

if length < 42:
    print(f"The zander is too small. Release it back into the lake.")
    print(f"It is {42 - length} cm below the size limit.")
else:
    print("The zander meets the size limit.")
Task2
cabin_class = input("Enter the cabin class (LUX, A, B, C): ").upper()

if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("Above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")
Task3
gender = input("Enter biological gender (male/female): ").lower()
hemoglobin = int(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin level is low.")
    elif hemoglobin > 155:
        print("Hemoglobin level is high.")
    else:
        print("Hemoglobin level is normal.")
elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin level is low.")
    elif hemoglobin > 167:
        print("Hemoglobin level is high.")
    else:
        print("Hemoglobin level is normal.")
else:
    print("Invalid gender.")
Task4
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year.")
elif year % 100 == 0:
    print("Not a leap year.")
elif year % 4 == 0:
    print("Leap year.")
else:
    print("Not a leap year.")