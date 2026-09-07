def celsius_para_fahrenheit(fahrenheit):  # 'celsius' é o parâmetro
    """
    >>> celsius_para_fahrenheit(32)
    0.0

    >>> celsius_para_fahrenheit(212)
    100.0

    >>> celsius_para_fahrenheit(98.6)
    37.0

    >>> celsius_para_fahrenheit(-40)
    -40.0
    """

    return 5 * ((fahrenheit - 32) / 9)


if __name__ == "__main__":
    temperatura_fahrenheit = float(input("Digite a temperatura em fahrenheit: "))

    temperatura_celsius = celsius_para_fahrenheit(temperatura_fahrenheit)

    print(f"{temperatura_fahrenheit}°F é igual a {temperatura_celsius}°C")

# Taxionomia de Testes

# python -m doctest -v app.py