def fibonacci(f):
    if f <= 0:
        return 0
    elif f == 1:
        return 1

    f1 = 0
    f2 = 1

    for _ in range(2, f + 1):
        fib_atual = f1 + f2
        f1, f2 = f2, fib_atual

    return f2

# Exemplo de uso:
resultado = fibonacci(6)
print(resultado)  # Deve retornar 8