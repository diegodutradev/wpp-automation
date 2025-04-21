# 🤖 Automação de Envio de Imagens via WhatsApp 🤖

Este projeto é uma automação feita em Python com Selenium para **encaminhar imagens via WhatsApp Web** para uma lista de contatos, como por exemplo o cardápio diário de um restaurante.

---

## 📌 Pré-requisitos

- Python 3.10+
- Google Chrome
- ChromeDriver compatível com a versão do seu navegador
- Selenium (`pip install selenium`)
- Uma lista de contatos em um arquivo `lista_contatos.py` com o seguinte formato:

```python
contatos_destino = [
    "Cliente 1",
    "Cliente 2",
    "Cliente 3",
    ...
]
```

---

## ⚙️ Como usar

### 1. **Crie um grupo no WhatsApp com o nome que desejar** (ex: `Automation`)
- Este grupo servirá como **repositório temporário da imagem a ser enviada**.
- **Muito importante:** **Deixe apenas a imagem no grupo**, sem mensagens de texto ou outras mídias, para evitar que a automação encaminhe a mídia errada.
- Recomendado que este grupo tenha apenas você como participante.

### 2. **Coloque a imagem desejada no grupo**

- Envie **somente** a imagem (cardápio ou flyer) que deseja compartilhar com os contatos naquele momento.

### 3. **Edite a variável `nome_do_grupo` no script**

```python
nome_do_grupo = "Automation"  # substitua pelo nome do seu grupo, se necessário
```

### 4. **Rode o script**

```bash
python enviar_cardapio.py
```

- O script abrirá o WhatsApp Web em uma nova janela.
- Aguarde o carregamento e **pressione ENTER no terminal** quando tudo estiver pronto.
- O envio será feito em blocos de 5 contatos com pausas aleatórias para simular comportamento humano.

---

## ✅ Recursos do Script

- Encaminha a imagem de um grupo para múltiplos contatos.
- Envio feito em blocos de 5 contatos.
- Pausas aleatórias para evitar detecção como robô.
- Trata contatos não encontrados sem interromper o processo.
- Usa `Selenium` e `ActionChains` para automação precisa.

---

## ⚠️ Observações importantes

- Para evitar ser bloqueado pelo WhatsApp, **não reduza as pausas aleatórias demais** e **evite rodar várias instâncias do script ao mesmo tempo**.
- A automação simula comportamento humano, mas WhatsApp pode eventualmente detectar automações se usadas com excesso.
- Ideal para quem envia conteúdos recorrentes (como cardápios, promoções, convites) para uma base fiel de contatos.

---

## 📁 Estrutura do Projeto

```
whatsapp-automation/
│
├── enviar_cardapio.py        # Script principal
├── lista_contatos.py         # Contatos que receberão a imagem
├── README.md                 # Instruções e detalhes do projeto
└── .gitignore                # Arquivos/pastas ignorados pelo Git
```

---

## 👨‍💻 Autor

Desenvolvido por Diego Dutra — motivado por desafios reais de automação no dia a dia de um restaurante.

GitHub: [@diegodutradev](https://github.com/diegodutradev)

---

## ⭐ Contribua

Achou útil? Dê uma estrela ⭐ no repositório e compartilhe com outros que possam se beneficiar!