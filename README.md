# Projeto DELTA — Cifra de Integridade Primal (CIP)

O Projeto DELTA propõe uma cifra pós-quântica baseada na estrutura espectral dos números primos.
A **Cifra de Integridade Primal (CIP)** opera por projeção vetorial em uma base harmônica construída com a função primal dos primos:

$$
\Delta_\pi(x) = \pi(x) - 2\pi(x/2)
$$

## Características

- Cifragem e decifragem com fidelidade absoluta por forma espectral
- Assinatura vetorial por bloco com verificação hash SHA-256
- Sensível a alterações mínimas (até um espaço em branco)
- Resistente a ataques quânticos: não depende de segredo, fatoração ou curva elíptica
- Baseada na ressonância com a estrutura primal dos números primos

## Estrutura

```bash
src/cip_bloco.py          # Código principal da cifra e verificação
docs/whitepaper.md        # Documento técnico explicando o funcionamento
docs/artigo_estadao.md    # Artigo de resposta enviado ao jornal O Estado de S. Paulo
examples/                 # Exemplos de arquivos testados e validados

