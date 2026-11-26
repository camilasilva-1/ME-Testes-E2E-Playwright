
from pathlib import Path
from playwright.sync_api import Page, expect


def test_rejeitar_arquivo_invalido(page: Page):

    # 1. Localiza e abre a aplicação
    caminho_html = (
        Path(__file__).resolve().parent.parent.parent
        / "Projeto-Metaforando"
        / "index.html"
    )

    page.goto(caminho_html.as_uri())

    # 2. Prepara a captura da mensagem de alerta
    alertas = []

    def verificar_alerta(dialog):
        alertas.append(dialog.message)
        dialog.accept()

    page.on("dialog", verificar_alerta)

    # 3. Localiza o campo de seleção de arquivos
    input_arquivo = page.locator("#imageInput")

    # 4. Tenta enviar um arquivo que não é imagem
    input_arquivo.set_input_files({
        "name": "teste.txt",
        "mimeType": "text/plain",
        "buffer": b"Arquivo de teste invalido"
    })

    # 5. Verifica se o alerta correto apareceu
    assert alertas == [
        "Por favor, selecione apenas arquivos de imagem."
    ]

    # 6. Confirma que o arquivo foi rejeitado
    expect(input_arquivo).to_have_value("")

    # 7. Confirma que a pré-visualização não apareceu
    preview_container = page.locator("#previewContainer")
    expect(preview_container).to_be_hidden()
