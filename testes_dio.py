def trocar_garrafas(N, K):
    if (K > N):
        return N

    else:
        resultado = (N // K) + (N % K)
        return resultado


T = int(input())

for i in range(T):
    N, K = map(int, input().split())  # essa linha recebe as varíaveis na mesma linha e as separa em substrings

    print(trocar_garrafas(N, K))




