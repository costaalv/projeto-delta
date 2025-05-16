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
```

## Saiba mais

- [Whitepaper técnico](docs/whitepaper.md)  
- [Resumo Executivo da CIP](docs/resumo_executivo.md)  
- [Repositório oficial no GitHub](https://github.com/costaalv/projeto-delta)

---

## Notebooks interativos (Google Colab)

Explore abaixo os notebooks do Projeto DELTA que demonstram passo a passo o funcionamento da **Cifra de Integridade Primal (CIP)** — da estrutura espectral dos primos à verificação digital infalível.

| Nº  | Notebook                                              | Descrição                                                                                          | Abrir no Colab |
|-----|--------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------|
| 01  | `01_estrutura_primal_e_matriz_cossenos.ipynb`         | Introdução à matriz harmônica e à estrutura espectral baseada em $\Delta_\pi(x)$.                            | [🔗 Abrir](https://colab.research.google.com/drive/https://drive.google.com/file/d/18uKKdsr5_bka8NblUSWzDO5j95PRv2jF/view?usp=sharing) |
| 02  | `02_cifragem_espectral_com_cip.ipynb`                 | Demonstra a cifragem vetorial dos dados com base espectral derivada dos primos.                    | [🔗 Abrir](https://colab.research.google.com/drive/https://drive.google.com/file/d/1ehnbiCWM8HBkSZlIGO3H4ZBwgORi2yuc/view?usp=sharing) |
| 03  | `03_verificacao_de_integridade_em_arquivos.ipynb`     | Verificação espectral da integridade de arquivos com detecção de alterações microscópicas.         | [🔗 Abrir](https://colab.research.google.com/drive/https://drive.google.com/file/d/1hfwhqadasCPwCsfG5vNmgA8w97YfKiJO/view?usp=sharing) |
| 04  | `04_aplicacoes_reais_e_verificacao_cip.ipynb`         | Casos práticos de aplicação da CIP para autenticação e segurança digital.                          | [🔗 Abrir](https://colab.research.google.com/drive/https://drive.google.com/file/d/1Syd7oKhWj6crsBq3UvdXXf1_R2S62P0a/view?usp=sharing) |
| 05  | `05_cip_demo.ipynb`                                   | Demonstração compacta de todo o ciclo: cifragem, assinatura, corrupção e verificação.              | [🔗 Abrir](https://colab.research.google.com/drive/https://drive.google.com/file/d/1CS7VKNX3zz9ruO4s0MkG2ElJYtIZBcfk/view?usp=sharing) |
> Todos os notebooks são autoexplicativos e funcionam direto no navegador com Python 3 e numpy.

---

## Contato

**Alvaro Costa**  
Auditor Fiscal · Cientista de Dados · Fundador do Projeto DELTA  
Ex-aluno da FEA-USP (Economia) e da FDUSP (Direito)  
costaalv@alumni.usp.br

---

> **Não é segredo. É estrutura.**  
> **Ou a informação vibra — ou não é original.**

