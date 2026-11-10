# M.E. de Testes de Software — Playwright (Python)

## Sobre o projeto

Este repositório reúne a **M.E. da disciplina de Testes de Software**, dedicada ao estudo e à aplicação de **testes de sistema ponta a ponta (E2E)** usando **Playwright para Python** e **pytest**.

O sistema escolhido para os testes é o [Projeto-Metaforando](https://github.com/Gioh-jpg/Projeto-Metaforando), protótipo web de **Reconhecimento de Expressões Faciais**, desenvolvido na disciplina de Inteligência Artificial e Data Science.

> **Status:** planejamento e preparação. Os testes automatizados ainda serão implementados e executados. A utilização do projeto na M.E. deve ser validada com a professora, conforme as orientações da atividade.

## Objetivo

Automatizar interações reais de um usuário com o navegador — abrir a aplicação, selecionar arquivos e verificar as respostas da interface — para demonstrar como funcionam os testes E2E.

O protótipo atual permite selecionar imagens, mostrar uma pré-visualização, rejeitar arquivos incompatíveis, arrastar imagens para a área de upload e remover uma imagem selecionada. **A classificação pelo modelo de IA ainda não está integrada**; portanto, os testes iniciais não pretendem validar predições de IA.

## Cenários de teste planejados

| Cenário | Ação do usuário | Verificação esperada |
| --- | --- | --- |
| **1. Sucesso** | Selecionar uma imagem válida | A imagem é exibida na área de pré-visualização |
| **2. Erro** | Tentar selecionar um arquivo não compatível (ex.: `.txt`) | A aplicação rejeita o arquivo e apresenta um alerta |
| **3. Fluxo completo** | Selecionar imagem → visualizar → remover | A pré-visualização aparece e desaparece após a remoção |

Cada cenário terá **asserções** (por exemplo, `expect()`) para verificar o comportamento observado. Os detalhes serão ajustados e validados durante a implementação.

## Tecnologias

- **Python** — linguagem dos testes;
- **Playwright** — automação do navegador;
- **pytest / pytest-playwright** — organização e execução dos testes;
- **HTML, CSS e JavaScript** — tecnologias da aplicação testada.

## Estrutura prevista

```text
ME-Testes-E2E-Playwright/
├── testes/             # Cenários E2E em Python
├── arquivos_teste/     # Imagens válidas e arquivos inválidos
├── evidencias/         # Capturas e resultados da execução
├── apresentacao/       # Slides da M.E.
├── requirements.txt    # Dependências, quando configuradas
└── README.md
```

> As pastas e os arquivos acima representam a **organização planejada** e serão adicionados gradualmente. O código do sistema original continuará no repositório Projeto-Metaforando.

## Preparação e execução (após a implementação)

É necessário ter **Python 3** e **Git** instalados.

**1. Clone os dois repositórios lado a lado:**

```bash
git clone https://github.com/Gioh-jpg/Projeto-Metaforando.git
git clone https://github.com/camilasilva-1/ME-Testes-E2E-Playwright.git
cd ME-Testes-E2E-Playwright
```

**2. Crie um ambiente virtual e instale o Playwright:**

No Windows (PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install pytest-playwright
.\.venv\Scripts\python.exe -m playwright install chromium
```

**3. Execute o site em um terminal separado**, a partir da pasta do repositório de testes:

```powershell
py -m http.server 8000 --directory ../Projeto-Metaforando
```

Abra `http://localhost:8000` para conferir a interface. Mantenha esse terminal aberto.

**4. Execute os testes (quando forem adicionados)**, em outro terminal, dentro da pasta de testes:

```powershell
.\.venv\Scripts\python.exe -m pytest testes/ -v
```

Os testes serão configurados para acessar `http://localhost:8000`. **Este comando ainda não terá testes para executar enquanto os arquivos da pasta `testes/` não forem criados.**

## Apresentação da M.E.

A apresentação terá duração prevista de **15 a 20 minutos**, com participação dos integrantes, e deverá abordar:

1. O que é o Playwright e para que serve;
2. Instalação, estrutura e execução dos testes;
3. Principais recursos, incluindo localizadores e verificações;
4. Código e demonstração dos três cenários E2E;
5. Vantagens e limitações da ferramenta;
6. Diferença entre testes unitários com pytest e testes de sistema E2E.

**Entrega prevista pela disciplina:** slides, código dos testes e instruções de execução, com demonstração ao vivo ou registro em vídeo como alternativa.

## Referências

- [Projeto-Metaforando — aplicação original](https://github.com/Gioh-jpg/Projeto-Metaforando)
- [Documentação oficial do Playwright para Python](https://playwright.dev/python/)
- [Integração do Playwright com pytest](https://playwright.dev/python/docs/test-runners)
- [Documentação oficial do pytest](https://docs.pytest.org/)

---

**Projeto acadêmico — Testes de Software | 2026**
