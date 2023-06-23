# Acosta Porcayo Alan Omar 320206102.

import numpy as np
import matplotlib.pyplot as plt

def main():
    asistentes = np.random.randint(1, 50, 12)
    print("Asistentes en cada mes: ", asistentes)

    contador1, contador2, contador3 = 0, 0, 0
    for i in range(12):
        if asistentes[i] < 10:
            contador1 += 1
        elif asistentes[i] >= 11 and asistentes[i] <= 40:
            contador2 += 1
        elif asistentes[i] > 40:
            contador3 += 1

    print("\nMeses con menos de 10 asistentes: ", contador1)
    print("Meses con entre 11 y 40 asistentes: ", contador2)
    print("Meses con mas de 40 asistentes: ", contador3)

    plt.plot(asistentes)
    plt.title("Asistentes en cada mes")
    plt.xlabel("Meses")
    plt.ylabel("Asistentes")
    plt.show()


if __name__ == '__main__':
    main()
