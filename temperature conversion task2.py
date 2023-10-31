def conversion(degree):
    fahrenheit = (degree * 9 / 5) + 32
    return fahrenheit


degree = int(input("enter the temperature"))
fahrenheit_degree = conversion(degree)
print(fahrenheit_degree)

