import numpy as np

from matrix import Matrix


def main():
    np.random.seed(0)
    matrix_a = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix_b = Matrix(np.random.randint(0, 10, (10, 10)))

    # Perform matrix operations
    matrix_add = matrix_a + matrix_b
    matrix_multiply = matrix_a * matrix_b
    matrix_dot = matrix_a @ matrix_b

    # Save results to text files
    np.savetxt('artifacts/3.1/matrix_a.txt', matrix_a.data, fmt='%d')
    np.savetxt('artifacts/3.1/matrix_b.txt', matrix_b.data, fmt='%d')
    np.savetxt('artifacts/3.1/matrix+.txt', matrix_add.data, fmt='%d')
    np.savetxt('artifacts/3.1/matrix*.txt', matrix_multiply.data, fmt='%d')
    np.savetxt('artifacts/3.1/matrix@.txt', matrix_dot.data, fmt='%d')


if __name__ == "__main__":
    main()
