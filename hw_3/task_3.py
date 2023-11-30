from matrix import Matrix

A = Matrix([[11, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])
C = Matrix([[1, 12], [3, 4]])
D = Matrix([[5, 6], [7, 8]])

print("Hashes", hash(A), hash(C))

AB = A @ B
CD = C @ D

# Сохраняем матрицы в файлы
with open("artifacts/3.3/A.txt", "w") as file:
    file.write(str(A.data))
with open("artifacts/3.3/B.txt", "w") as file:
    file.write(str(B.data))
with open("artifacts/3.3/C.txt", "w") as file:
    file.write(str(C.data))
with open("artifacts/3.3/D.txt", "w") as file:
    file.write(str(D.data))
with open("artifacts/3.3/AB.txt", "w") as file:
    file.write(str(AB.data))
with open("artifacts/3.3/CD.txt", "w") as file:
    file.write(str(CD.data))

# Сохраняем хэши в файл
with open("artifacts/3.3/hash.txt", "w") as file:
    file.write(str(hash(AB)))
