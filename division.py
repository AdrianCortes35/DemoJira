# division.py

def dividir(a, b):
    if b != 0:
        return a/b
    else:
        return "error"

if __name__ == "__main__":
    print(dividir(5, 3))