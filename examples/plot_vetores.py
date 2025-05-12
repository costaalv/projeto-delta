import numpy as np
import matplotlib.pyplot as plt

# Carregar vetores salvos
v_orig = np.load("vetor_original.npy")
v_inicio = np.load("vetor_espaco_inicio.npy")
v_fim = np.load("vetor_espaco_fim.npy")

# Tamanho da base (deve ser 1024)
size = len(v_orig)
x = np.arange(size)

plt.figure(figsize=(14, 6))
plt.plot(x, v_orig, label="Original", linewidth=1.5)
plt.plot(x, v_inicio, label="Espaço no início", linewidth=1.2, linestyle='--')
plt.plot(x, v_fim, label="Espaço no final", linewidth=1.2, linestyle=':')

plt.title("Comparação dos Vetores Projetados — Bloco 0", fontsize=14)
plt.xlabel("Índice do vetor projetado")
plt.ylabel("Amplitude espectral")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Mostrar e salvar o gráfico
plt.savefig("vetores_bloco0.png", dpi=300)
plt.show()

