
temperature_mode = input("Vill du konvertera från Farenheit (F) eller Celsius (C)?: ")
input_temperature = float(input("Skriv in en temperatur : "))
if (temperature_mode == "C") or (temperature_mode == "c"):
    temperatur_farenheit = 1.8 * input_temperature + 32
    print("Det blir", temperatur_farenheit, "grader Fahrenheit.")
elif (temperature_mode == "F") or (temperature_mode == "f"):
    temperatur_celsius = (input_temperature - 32) / 1.8
    print("Det blir", temperatur_celsius, "grader Celsius.")
else:
    print("Vänligen ange F eller C som indata")

