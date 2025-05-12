import os
import sys
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import cip_blocos as cip

ARQUIVOS = {
    "original": "texto_original.txt",
    "espaco_inicio": "texto_espaco_inicio.txt",
    "espaco_fim": "texto_espaco_fim.txt",
}

def carregar_texto(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        return f.read()

def projetar_bloco(texto, chave):
    bloco = texto[:chave['size']]
    vetor = cip.codificar_bloco(bloco, chave['size'])
    matriz = cip.construct_cosine_matrix(chave['x'], chave['size'])
    _, autovetores = np.linalg.eigh(matriz)
    base = autovetores[:, -chave['size']:]
    base_inv = np.linalg.pinv(base)
    return base_inv @ vetor  # vetor projetado

def main():
    print("===> Assinando texto original...")
    texto_original = carregar_texto(ARQUIVOS["original"])
    assinatura, chave = cip.cip_assinar_bloco_hibrido(texto_original)

    print("\n===> Verificando texto original...")
    alt, total = cip.cip_verificar_bloco_hibrido(texto_original, assinatura, chave)
    print(f"Blocos alterados: {alt} / {total}")

    for nome, caminho in ARQUIVOS.items():
        if nome == "original":
            continue
        print(f"\n===> Verificando {nome.replace('_', ' ')}...")
        texto = carregar_texto(caminho)
        alt, total = cip.cip_verificar_bloco_hibrido(texto, assinatura, chave)
        print(f"{nome}: Blocos alterados = {alt} / {total}")

    # Projeções espectrais do bloco 0
    print("\n===> Comparando vetores projetados do bloco 0:")

    v_orig = projetar_bloco(carregar_texto(ARQUIVOS["original"]), chave)
    v_inicio = projetar_bloco(carregar_texto(ARQUIVOS["espaco_inicio"]), chave)
    v_fim = projetar_bloco(carregar_texto(ARQUIVOS["espaco_fim"]), chave)

    print("🔹 Original (bloco 0)   →", v_orig[:5])
    print("🔹 Espaço no início     →", v_inicio[:5])
    print("🔹 Espaço no final      →", v_fim[:5])

    # Salvando vetores para análise futura
    np.save("vetor_original.npy", v_orig)
    np.save("vetor_espaco_inicio.npy", v_inicio)
    np.save("vetor_espaco_fim.npy", v_fim)
    print("\nVetores salvos como .npy para análise posterior.")

if __name__ == "__main__":
    main()

