CIP — Cifra de Integridade Primal
=================================

O CIP (Cifra de Integridade Primal) é um sistema de autenticação vetorial baseado em projeção espectral sobre a estrutura dos números primos. Ele não utiliza criptografia clássica, não exige chaves secretas e oferece integridade absoluta de dados, mesmo diante de alterações microscópicas.

Este pacote implementa o núcleo funcional do CIP para uso local ou em notebooks.

Módulo: cip.core

FUNCIONALIDADES PRINCIPAIS
---------------------------
• delta_pi(x)
  - Função que calcula a dualidade primal dos primos.
  - Define a estrutura oscilatória central do sistema.

• construct_cosine_matrix(x, size)
  - Gera uma matriz simétrica a partir de |Δπ(x)|.
  - Essa matriz é usada para obter a base vetorial harmônica.

• codificar_bloco(texto, bloco_size)
  - Codifica um bloco de texto ou bytes em vetor float normalizado.

• decodificar_bloco(vetor)
  - Reconstrói os bytes a partir do vetor decodificado.

• cip_assinar_blocos_bytes(dados, x, size)
  - Assina os blocos de um conteúdo binário via projeção espectral + SHA-256.
  - Retorna lista de hashes e a chave estrutural usada.

• cip_verificar_blocos_bytes(dados, assinaturas_ref, chave)
  - Verifica a integridade estrutural de cada bloco comparando hashes.
  - Detecta qualquer alteração no conteúdo.

• cip_cifrar_blocos_bytes(dados, x, size)
  - Cifra blocos em vetores espectrais.
  - Os dados cifrados parecem ruído puro sem a base correta.

• cip_decifrar_blocos_bytes(data_or_path)
  - Reverte os vetores cifrados para bytes originais, usando a base harmônica.
  - Detecta e impede reconstrução com base incorreta.

CARACTERÍSTICAS TÉCNICAS
--------------------------
- Estrutura espectral baseada em |Δπ(x)|, sem uso da função zeta.
- Projeção vetorial reversível sobre base derivada dos números primos.
- Hash SHA-256 aplicado sobre projeções vetoriais (não sobre os dados).
- Compatível com qualquer tipo de dado binário: texto, PDF, imagem, áudio, etc.
- Resistente a ataques quânticos: não há fatoração, curva elíptica, nem segredo.

EXEMPLO DE USO BÁSICO
-----------------------
```python
from cip.core import (
    cip_assinar_blocos_bytes,
    cip_verificar_blocos_bytes,
    cip_cifrar_blocos_bytes,
    cip_decifrar_blocos_bytes
)

with open("documento.pdf", "rb") as f:
    dados = f.read()

assinaturas, chave = cip_assinar_blocos_bytes(dados)
alterados, total = cip_verificar_blocos_bytes(dados, assinaturas, chave)

print(f"Blocos alterados: {alterados} / {total}")
```

AUTOR
Desenvolvido por Alvaro Costa
São Paulo, Brasil
Projeto DELTA — Dual Eigenvalue Lattice for Transformative Arithmetic

Repositório oficial:
https://github.com/costaalv/projeto-delta

Licença: MIT

