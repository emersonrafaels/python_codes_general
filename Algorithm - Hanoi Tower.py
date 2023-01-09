def towerOfHanoi(N, source, destination, auxiliary):

    if N == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return

    towerOfHanoi(N - 1, source, auxiliary, destination)
    print("Move disk", N, "source", source, "to destination", destination)
    towerOfHanoi(N - 1, auxiliary, destination, source)  # Código do driver


N = 3
towerOfHanoi(N, 'A', 'B', 'C')
# A, C, B são os nomes das hastes