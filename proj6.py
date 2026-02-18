#its a C to F convertor
def c_to_f(c):
    f = (9/5*c) + 32
    return f
def f_to_c(f):
    c = (5/9*f )- 32
    return c

input_1 = float(input("Enter a temperature: "))
input_2 = input("Is it in Celsius or Fahrenheit? (C/F): ")
if input_2 == "C":
    print(f"The temperature in Fahrenheit is: {c_to_f(input_1)}")
elif input_2 == "F":
    print(f"The temperature in Celsius is: {f_to_c(input_1)}")