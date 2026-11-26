# M.E. — Testes E2E com Playwright

Projeto da disciplina de **Testes de Software** para automatizar testes de sistema utilizando **Python, Playwright e pytest**.

**Aplicação testada:** [Projeto-Metaforando](https://github.com/Gioh-jpg/Projeto-Metaforando), um protótipo de reconhecimento de expressões faciais.

## Objetivo

Automatizar testes End-to-End (E2E) para verificar o funcionamento do envio, da pré-visualização e da remoção de imagens na aplicação.

## Cenários de teste

1. **Sucesso:** selecionar uma imagem válida e verificar se a pré-visualização é exibida corretamente.
2. **Erro:** enviar um arquivo inválido e verificar se a aplicação apresenta o alerta esperado.
3. **Fluxo completo:** selecionar uma imagem, verificar sua pré-visualização, removê-la e confirmar que o campo de arquivo foi limpo.

## Tecnologias utilizadas

- Python
- Playwright
- pytest
- pytest-playwright
- Chromium

## Instalação

Com o Python instalado, execute os comandos abaixo no terminal:

```bash
python -m pip install pytest playwright pytest-playwright
```

Instale o navegador Chromium:

```bash
python -m playwright install chromium
```

## Organização dos projetos

O repositório dos testes e a aplicação Metaforando devem ficar em pastas vizinhas.

Clone a aplicação com:

```bash
git clone https://github.com/Gioh-jpg/Projeto-Metaforando.git Projeto-Metaforando
```

Após baixar os projetos, a organização das pastas deve ficar desse jeito:

```text
Nome da pasta em que você baixou o projeto/
├── ME-Testes-E2E-Playwright/
│   ├── tests/
│   │   ├── fixtures/
│   │   ├── test_arquivo_invalido.py
│   │   ├── test_fluxo_completo.py
│   │   └── test_upload_preview.py
│   ├── .gitignore
│   └── README.md
│
└── Projeto-Metaforando/
    ├── index.html
    ├── script.js
    └── style.css
```

## Execução dos testes

Para executar todos os testes:

```bash
python -m pytest -v
```

Para executar um cenário específico:

```bash
python -m pytest tests/test_upload_preview.py -v
```

```bash
python -m pytest tests/test_arquivo_invalido.py -v
```

```bash
python -m pytest tests/test_fluxo_completo.py -v
```

O pytest apresenta o resultado de cada teste, indicando se foi aprovado (PASSED) ou se ocorreu alguma falha (FAILED).

## Resultados

Os três cenários foram executados com sucesso no Chromium:

- Teste de pré-visualização: PASSED.
- Teste de arquivo inválido: PASSED.
- Teste de fluxo completo: PASSED.

**Resultado da execução conjunta: 3 passed, 0 failed.**

## Limitações

A integração com o modelo de Inteligência Artificial ainda não está concluída. Portanto, os testes deste projeto verificam os comportamentos relacionados ao envio, à validação, à pré-visualização e à remoção de imagens, não o reconhecimento de expressões faciais.
