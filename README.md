# Projeto DELTA — Cifra de Integridade Primal (CIP)

# Projeto DELTA — Cifra de Integridade Primal (CIP)

A **Cifra de Integridade Primal (CIP)** é uma proposta inédita de integridade digital baseada em **estrutura, não em segredo**.

Em vez de criptografar, a CIP **projeta** cada bloco de dados em uma base harmônica derivada da estrutura espectral dos números primos:

$$
\Delta_\pi(x) = \pi(x) - 2\pi(x/2)
$$

O resultado é um sistema leve, auditável, pós-quântico e hipersensível:  
**se o conteúdo ressoa, é original — se não ressoa, é ruído.**

---

## Principais Características

- **Integridade vetorial absoluta**: projeção em base espectral derivada dos primos  
- **Verificação bloco a bloco** com hash SHA-256  
- **Sensível a mutações mínimas** — até 1 bit ou espaço em branco  
- **Resistência estrutural à computação quântica**  
- **Sem segredo, sem chave, sem encriptação**  
- **Funciona com qualquer conteúdo**: texto, PDF, imagem, código, áudio  

---

## Estrutura do Repositório

```bash
src/cip/core.py            # Funções principais de cifragem, assinatura e verificação vetorial
docs/                      # Whitepaper, resumo executivo, carta de apresentação e fundamentos jurídicos
notebooks/                 # Notebooks explicativos com demonstrações práticas
examples/                  # Arquivos reais utilizados nos testes (texto, binário, PDF)


## Saiba mais

- [Whitepaper técnico](docs/whitepaper.md)  
- [Resumo Executivo da CIP](docs/resumo_executivo.md)  
- [Repositório oficial no GitHub](https://github.com/costaalv/projeto-delta)

---

## Contato

**Alvaro Costa**  
Auditor Fiscal · Cientista de Dados · Fundador do Projeto DELTA  
Ex-aluno da FEA-USP (Economia) e da FDUSP (Direito)  
costaalv@alumni.usp.br

---

> **Não é segredo. É estrutura.**  
> **Ou a informação vibra — ou não é original.**

