import random


def initiateMatrix(n, a, b):
    matrix = []
    for _ in range(n):
        line = []
        for _ in range(n):
            element = int(random.uniform(a, b))
            line.append(element)
        matrix.append(line)
    return matrix


def showMatrix(matrix):
    for line in matrix:
        print(line)


def lowerAverage(matrix):
    x = 0
    sum = 0
    count = 0

    for line in matrix:
        for i in range(x):
            print(line[i], end=" ")
            sum += line[i]
            count += 1
        x += 1
        print()
    return sum / count


def upperAverage(matrix, n):
    x = n
    z = 1
    sum = 0
    count = 0

    for line in matrix:
        print("x " * z, end=" ")
        for i in range(x - z):
            print(line[i + z], end=" ")
            sum += line[i + z]
            count += 1
        z += 1
        print()
    return sum / count


def main():
    n = int(input("Enter matrix dimension 'n': "))
    a = int(input("Enter lower data limit: "))
    b = int(input("Enter upper data limit: ")) + 1
    # n = 10
    # a = 1
    # b = 100
    matrix = initiateMatrix(n, a, b)
    print("Matrix:")
    showMatrix(matrix)
    print("Lower average: ", lowerAverage(matrix))
    print()
    print("Upper average: ", upperAverage(matrix, n))


if __name__ == "__main__":
    main()
