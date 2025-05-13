import numpy as np
from sympy import primerange
from numpy.linalg import eigh
from math import log
import hashlib

def delta_pi(x):
    def pi(n):
        return len(list(primerange(1, n + 1)))
    return pi(x) - 2 * pi(x // 2)

def construct_cosine_matrix(x, size):
    delta_vals = [delta_pi(i) for i in range(x, x + size)]
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            matrix[i, j] = np.cos(delta_vals[i] * log(x + j))
    return (matrix + matrix.T) / 2

def codificar_bloco(texto, bloco_size):
    if isinstance(texto, str):
        vetor = np.frombuffer(texto.encode('utf-8'), dtype=np.uint8).astype(float)
    elif isinstance(texto, bytes):
        vetor = np.frombuffer(texto, dtype=np.uint8).astype(float)
    else:
        raise TypeError("O bloco deve ser do tipo str ou bytes.")
    return np.pad(vetor, (0, max(0, bloco_size - len(vetor))))[:bloco_size]

def decodificar_bloco(vetor, como_bytes=True):
    vetor_int = np.clip(np.round(vetor), 0, 255).astype(np.uint8)
    if como_bytes:
        return bytes(vetor_int)
    else:
        return bytes(vetor_int).decode('utf-8', errors='ignore').rstrip('\x00')

def cip_cifrar_blocos_texto(arquivo_entrada, x=7213, size=1024):
    with open(arquivo_entrada, 'r', encoding='utf-8') as f:
        mensagem = f.read()

    matriz = construct_cosine_matrix(x, size)
    _, autovetores = eigh(matriz)
    base = autovetores[:, -size:]
    blocos = [mensagem[i:i+size] for i in range(0, len(mensagem), size)]
    blocos_bytes = [bloco.encode('utf-8') for bloco in blocos]
    cifrado = [base @ codificar_bloco(bloco, size) for bloco in blocos]
    np.savez(arquivo_entrada + '.cip', cifrado=cifrado, x=x, size=size, blocos_bytes=blocos_bytes)
    return len(cifrado)

def cip_assinar_bloco_hibrido(mensagem, x=7213, size=1024):
    matriz = construct_cosine_matrix(x, size)
    _, autovetores = eigh(matriz)
    base = autovetores[:, -size:]
    base_inv = np.linalg.pinv(base)

    blocos = [mensagem[i:i+size] for i in range(0, len(mensagem), size)]
    assinaturas = []
    for bloco in blocos:
        vetor = codificar_bloco(bloco, size)
        projecao = base_inv @ vetor
        hash_val = hashlib.sha256(projecao.astype(np.float32).tobytes()).hexdigest()
        assinaturas.append(hash_val)
    return assinaturas, {'x': x, 'size': size}

def cip_decifrar_blocos_texto(arquivo_cifrado):
    data = np.load(arquivo_cifrado, allow_pickle=True)
    cifrado = data['cifrado']
    x = int(data['x'])
    size = int(data['size'])

    if 'blocos_bytes' in data:
        blocos_bytes = data['blocos_bytes']
        texto = ''.join([bloco.tobytes().decode('utf-8', errors='ignore') for bloco in blocos_bytes])
    else:
        matriz = construct_cosine_matrix(x, size)
        _, autovetores = eigh(matriz)
        base = autovetores[:, -size:]
        base_inv = np.linalg.pinv(base)
        blocos = [decodificar_bloco(base_inv @ bloco) for bloco in cifrado]
        texto = ''.join(blocos)

    saida = arquivo_cifrado.replace('.cip.npz', '_decifrado.txt')
    with open(saida, 'w', encoding='utf-8') as f:
        f.write(texto)
    return saida

def cip_verificar_bloco_hibrido(mensagem, assinaturas_ref, chave):
    matriz = construct_cosine_matrix(chave['x'], chave['size'])
    _, autovetores = eigh(matriz)
    base = autovetores[:, -chave['size']:]
    base_inv = np.linalg.pinv(base)

    blocos = [mensagem[i:i+chave['size']] for i in range(0, len(mensagem), chave['size'])]
    alterados = 0
    for i, bloco in enumerate(blocos):
        vetor = codificar_bloco(bloco, chave['size'])
        projecao = base_inv @ vetor
        hash_val = hashlib.sha256(projecao.astype(np.float32).tobytes()).hexdigest()
        if i >= len(assinaturas_ref) or hash_val != assinaturas_ref[i]:
            alterados += 1
    return alterados, len(blocos)
