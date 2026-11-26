from pathlib import Path
from playwright.sync_api import Page, expect


def test_exibir_pre_visualizacao_ao_selecionar_imagem_valida(page: Page):
    caminho_html = Path(__file__).resolve().parent.parent.parent / "index.html"
    page.goto(caminho_html.as_uri())

    caminho_imagem = Path(__file__).resolve().parent / "fixtures" / "EDA.png"

    input_arquivo = page.locator('input[type="file"]')
    input_arquivo.set_input_files(str(caminho_imagem))

    preview_container = page.locator("#previewContainer")
    preview_imagem = page.locator("#imagePreview")

    expect(preview_container).to_be_visible()
    expect(preview_imagem).to_be_visible()

    imagem_carregada = preview_imagem.evaluate(
        "img => img.complete && img.naturalWidth > 0"
    )
    assert imagem_carregada is True
