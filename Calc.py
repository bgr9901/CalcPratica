import random

def roleta():
    numero_sorteado = random.randint(0, 100)
    print(f"O número sorteado foi: {numero_sorteado}")

if __name__ == "__main__":
    roleta()