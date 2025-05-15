# White Paper Técnico — Projeto DELTA  
## Integridade Criptográfica por Estrutura Primal

---

## Visão Geral

O Projeto DELTA propõe uma cifra vetorial baseada na estrutura espectral dos números primos, expressa pela função aritmética:

$$
\Delta_\pi(x) = \pi(x) - 2\pi(x/2)
$$

O pacote `delta-cip`, disponível no PyPI, implementa a **Cifra de Integridade Primal (CIP)**, que opera por projeção espectral em bases derivadas da matriz de cossenos construída com os valores de \(\Delta_\pi(x)\). O sistema oferece:

- **Cifragem por blocos vetoriais em formato binário**
- **Decodificação com fidelidade absoluta (também em binário)**
- **Assinatura híbrida por bloco com SHA-256**
- **Verificação com sensibilidade extrema a alterações**

---

## Instalação

```bash
pip install delta-cip
```

---

## Funções principais

### `cip_cifrar_blocos_bytes(dados_binarios: bytes, x: int, size: int) -> list`
Recebe os dados como `bytes`, divide em blocos, projeta vetorialmente e retorna uma lista de blocos cifrados (listas de floats).

### `cip_decifrar_blocos_bytes(blocos_cifrados: list, x: int, size: int) -> bytes`
Reconstrói os `bytes` originais a partir dos blocos cifrados, com precisão absoluta se nenhum bloco for alterado.

### `cip_assinar_bloco_hibrido(mensagem: bytes, x: int, size: int) -> str`
Gera uma assinatura SHA-256 da projeção vetorial do bloco fornecido.

### `cip_verificar_bloco_hibrido(mensagem: bytes, assinatura: str, x: int, size: int) -> bool`
Verifica se a assinatura fornecida corresponde à mensagem atual. Retorna `True` ou `False`.

---

## Validações experimentais

### Teste de integridade absoluta
- Arquivo com **356.886 caracteres** cifrado e decifrado.
- **Resultado**: reconstrução perfeita.
- **Blocos alterados:** 0 / 349

### Teste de mutação mínima — espaço no final
- Inserido 1 espaço ao final.
- **Blocos alterados:** 1 / 349

### Teste de mutação mínima — espaço no início
- Inserido 1 espaço no início.
- **Blocos alterados:** 349 / 349

> O CIP detecta até perturbações invisíveis, pois assina vetores projetados — não o texto diretamente.

---

## Vantagens criptográficas

- Sem chave privada, sem fatoração, sem curva elíptica.
- Imune a ataques quânticos: **não há segredo a quebrar**.
- Segurança garantida por **ressonância estrutural**.
- Assinatura vetorial rastreia mutações posicionalmente.

---

## Análise visual da projeção vetorial

### Figura: Vetores projetados do bloco 0 em diferentes condições

![Vetores projetados](https://raw.githubusercontent.com/costaalv/projeto-delta/main/examples/vetores_bloco0.png)

Cada curva representa o vetor espectral do primeiro bloco de um texto sob diferentes versões:

- 🔵 Texto original
- 🟠 Texto com espaço no início
- 🟢 Texto com espaço no final

> A integridade, aqui, é registrada como coerência de forma — não como cadeia de símbolos.
> O CIP não guarda segredo: ele grava a estrutura que vibra com precisão.

---

## Tentativa de leitura direta de blocos cifrados

Mesmo com acesso aos blocos cifrados, sem a base correta, o conteúdo é ilegível.

### Exemplo: inspeção de um vetor cifrado (via numpy)

```python
from delta_cip import cip_decifrar_blocos_bytes

# Supondo que 'blocos' seja uma lista de vetores cifrados (floats)
# e que x, size sejam os mesmos usados na cifragem

dados_decifrados = cip_decifrar_blocos_bytes(blocos, x=7213, size=1024)
texto = dados_decifrados.decode("utf-8", errors="replace")
print(texto)
```

---

## Implicações
- A integridade no Projeto DELTA é garantida por estrutura, não por segredo.
- O conteúdo cifrado é ilegível sem a base exata.
- A verificação por forma permite detectar até mutações microscópicas.
- O CIP é funcional, auditável, leve — e radicalmente seguro.

> A integridade não é mais protegida por segredo.  
> Ela é ressonância.  
> Ela é forma.

---

## Status

- Pacote disponível via `pip install delta-cip`
- Pronto para auditoria pública
- Documentado e testado
- Em estruturação institucional

## Repositório oficial

[github.com/costaalv/projeto-delta](https://github.com/costaalv/projeto-delta)

---

## Valor comercial da verificação espectral

### Experimento real

- **Arquivo**: `ue000185.pdf`
- **Tamanho**: 185 MB
- **Verificação por blocos**: 181.133 blocos de 1024 bytes
- **Alteração proposital**: 1 único byte
- **Resultado**:

```
Blocos alterados: 1 / 181133
```

### O que isso significa?

Essa verificação demonstra que o CIP:

- Detecta **uma única mutação** em centenas de megabytes
- Identifica **exatamente o bloco alterado**
- Opera com **tempo de verificação em segundos**
- **Não depende de chaves privadas, certificados digitais ou leitura semântica**
- Funciona mesmo com arquivos **binários não editáveis ou protegidos**

---

## Valor comercial

### Confiança documental

Permite verificar documentos de grande porte (contratos, laudos, balanços, decisões judiciais) com **granularidade espectral**:

- Sem SHA ou PKI
- Sem recalcular tudo de novo
- Com detecção vetorial **por forma**

### Auditoria e rastreabilidade

- Detecção estrutural em pipelines
- Rastreabilidade posicional em arquivos versionados
- Compressão vetorial de autenticidade

### Segurança por forma, não por segredo

O CIP não se baseia em segredo:
> Ele projeta — e ouve.  
> Sem a base certa, **não há ressonância.**  
> Só ruído.

---

## Aplicações potenciais

- Governo e setor fiscal (provas, leis, autos, relatórios)
- Compliance e auditoria de grandes empresas
- Backup e revalidação local em armazenamento distribuído
- Blockchain leve e verificável
- Certificação de datasets científicos, periciais e jurídicos

---

> **Integridade não é mais um segredo bem guardado.**  
> **É uma forma que vibra com exatidão.**

---

### Conclusão

> Detectar 1 byte alterado em 185 MB — com velocidade e precisão — não é mais teoria. É código funcionando.  
> E ele não grita porque foi violado.  
> Ele grita porque a harmonia foi quebrada.

> **O Projeto DELTA propõe uma nova forma de garantir a verdade:**  
> **por estrutura, não por sigilo.**

## Autor

**Alvaro Costa**  
Auditor Fiscal · Cientista de Dados · Fundador do Projeto DELTA  
Ex-aluno da FEA-USP (Economia) e da FDUSP (Direito)  
costaalv@alumni.usp.br

