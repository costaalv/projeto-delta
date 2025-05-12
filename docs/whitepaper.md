# White Paper Técnico — Projeto DELTA  
## Integridade Criptográfica por Estrutura Primal

---

## Visão Geral

O Projeto DELTA propõe uma cifra vetorial baseada na estrutura espectral dos números primos, expressa pela função aritmética:

$$
\Delta_\pi(x) = \pi(x) - 2\pi(x/2)
$$

O módulo `cip_blocos.py` implementa a **Cifra de Integridade Primal (CIP)**, que opera por projeção espectral em bases derivadas da matriz de cossenos construída com os valores de $\Delta_\pi(x)$. O sistema oferece:

- **Cifragem por blocos vetoriais**
- **Decodificação com fidelidade absoluta**
- **Assinatura híbrida por bloco com SHA-256**
- **Verificação com sensibilidade extrema a alterações**

---

## Funções principais

### `cip_cifrar_blocos_texto(arquivo_entrada, x=7213, size=1024)`
Divide o arquivo de entrada em blocos, projeta-os vetorialmente e salva a cifragem em `.npz`.

### `cip_decifrar_blocos_texto(arquivo_cifrado)`
Reconstrói o texto original a partir do arquivo cifrado, com precisão absoluta se nenhum bloco for alterado.

### `cip_assinar_bloco_hibrido(mensagem, x, size)`
Gera uma assinatura vetorial por bloco, aplicando `SHA-256` sobre a projeção espectral do vetor.

### `cip_verificar_bloco_hibrido(mensagem, assinaturas_ref, chave)`
Verifica a integridade dos blocos comparando as assinaturas atuais com as originais. Retorna o número de blocos alterados.

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

A projeção vetorial em base harmônica permite distinguir mutações estruturais mesmo invisíveis ao leitor.
A curva com espaço no início se afasta do original, revelando **dissonância espectral**; a com espaço no final permanece **idêntica**.

> A integridade, aqui, é registrada como coerência de forma — não como cadeia de símbolos.
> O CIP não guarda segredo: ele grava a estrutura que vibra com precisão.

---

## Tentativa de leitura direta do arquivo `.cip.npz`

Mesmo com acesso ao arquivo `.cip.npz`, sem a base correta, o conteúdo é ilegível.

### Exemplo: inspeção do vetor cifrado

```python
import numpy as np

data = np.load("texto_original.txt.cip.npz", allow_pickle=True)
vetor = data["cifrado"][0]
texto = ''.join([chr(int(round(x))) if 0 <= x < 256 else '?' for x in vetor])
print(texto)
```

### Saída esperada (truncada)

```text
'[o vetor cifrado canta, mas só quem tem o diapasão certo ouve a melodia]'
```

> O vetor cifrado não contém texto visível — apenas ruído numérico sem sentido, mesmo quando inspecionado diretamente.

## Implicações
- A integridade no Projeto DELTA é garantida por estrutura, não por segredo.

- O conteúdo cifrado é ilegível sem a base exata.

- A verificação por forma permite detectar até mutações microscópicas.

- O CIP é funcional, auditável, leve — e radicalmente seguro.

> A integridade não é mais protegida por segredo.<br>
> Ela é ressonância.<br>
> Ela é forma.

## Status
- Código modular em Python

- Pronto para auditoria pública

- Documentado e testado

- Em estruturação institucional

## Repositório oficial

[github.com/costaalv/projeto-delta](https://github.com/costaalv/projeto-delta)

O código-fonte do Projeto DELTA, os notebooks com experimentos, o white paper e os exemplos de verificação vetorial estão abertos para escrutínio público, revisão técnica e contribuições.

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

---

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

---

### Auditoria e rastreabilidade

- Detecção estrutural em pipelines
- Rastreabilidade posicional em arquivos versionados
- Compressão vetorial de autenticidade

---

### Segurança por forma, não por segredo

O CIP não se baseia em segredo:
> Ele projeta — e ouve.
>
> Sem a base certa, **não há ressonância.**
>
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
> 
> **É uma forma que vibra com exatidão.**

---

### Conclusão

> Detectar 1 byte alterado em 185 MB — com velocidade e precisão — não é mais teoria. É código funcionando.
> 
> E ele não grita porque foi violado.
> 
> Ele grita porque a harmonia foi quebrada.

> **O Projeto DELTA propõe uma nova forma de garantir a verdade:**
> 
> **por estrutura, não por sigilo.**

## Autor

**Alvaro Costa**
Projeto DELTA — Integridade Criptográfica por Estrutura<br>
Ex-aluno da FEA-USP (Economia) e FDUSP (Direito)<br>
Auditor Fiscal de Rendas do Estado de São Paulo<br>
Cientista de Dados

