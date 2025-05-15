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

- **Integridade vetorial absoluta**: projeção em base espectral primitiva
- **Verificação bloco a bloco** com hash SHA-256
- **Sensível a mutações mínimas** — até 1 bit ou espaço em branco
- **Resistência estrutural à computação quântica**
- **Sem segredo, sem chave, sem encriptação**
- **Funciona com qualquer conteúdo**: texto, PDF, imagem, código, áudio

---

## Estrutura do Repositório

```bash
src/cip_bloco.py           # Código principal da CIP: cifragem, verificação e assinatura vetorial
docs/whitepaper.md         # Documento técnico detalhado
docs/resumo_executivo.md   # Versão institucional resumida para órgãos públicos e privados
docs/artigo_estadao.md     # Artigo enviado como resposta ao jornal O Estado de S. Paulo
examples/                  # Arquivos reais utilizados em testes (PDFs, textos, binários)
```

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

