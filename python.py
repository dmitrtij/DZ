def main():
    a, b = map(int, input("Введите два числа через пробел (пример: \"24 2\"): ").split())

    gcd = find_gcd(a, b)

    print(f"Наибольший общий делитель {a} и {b} = {gcd}")

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    main()
