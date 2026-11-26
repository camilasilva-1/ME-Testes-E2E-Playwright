from pathlib import Path
from playwright.sync_api import Page, expect

def test_fluxo_completo_upload_e_remocao(page: Page):

    # 1. Localiza e abre a aplicação
    caminho_html = (
        Path(__file__).resolve().parent.parent.parent
        / "Projeto-Metaforando"
        / "index.html"
    )

    page.goto(caminho_html.as_uri())
    
        # 2. Localiza e envia uma imagem válida
    caminho_imagem = (
        Path(__file__).resolve().parent
        / "fixtures"
        / "EDA.png"
    )

    input_arquivo = page.locator("#imageInput")
    input_arquivo.set_input_files(str(caminho_imagem))

        # 3. Verifica se a imagem foi exibida
    preview_container = page.locator("#previewContainer")
    preview_imagem = page.locator("#imagePreview")

    expect(preview_container).to_be_visible()
    expect(preview_imagem).to_be_visible()

    imagem_carregada = preview_imagem.evaluate(
        "img => img.complete && img.naturalWidth > 0"
    )

    assert imagem_carregada is True

        # 4. Remove a imagem selecionada
    botao_remover = page.locator("#removeImage")
    botao_remover.click()

        # 5. Verifica se a pré-visualização desapareceu
    expect(preview_container).to_be_hidden()

        # 6. Verifica se o campo de arquivo foi limpo
    expect(input_arquivo).to_have_value("")