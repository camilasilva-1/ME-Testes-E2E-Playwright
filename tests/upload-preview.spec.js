const { test, expect } = require('@playwright/test');
const path = require('path');
const { pathToFileURL } = require('url');

test.describe('Upload e pré-visualização de imagem', () => {
  test('deve exibir a pré-visualização ao selecionar uma imagem válida', async ({ page }) => {
    // Aponta diretamente para o index.html na raiz do projeto
    const caminhoHtml = path.resolve(__dirname, '..', 'index.html');
    await page.goto(pathToFileURL(caminhoHtml).href);

    // Caminho para a imagem válida na pasta fixtures
    const caminhoImagem = path.resolve(__dirname, 'fixtures', 'EDA.png');

    // Localiza o input de arquivo e envia a imagem válida
    const inputArquivo = page.locator('input[type="file"]');
    await inputArquivo.setInputFiles(caminhoImagem);

    // Localiza o contêiner e a imagem de pré-visualização
    const previewContainer = page.locator('#previewContainer');
    const previewImagem = page.locator('#imagePreview');

    // Verifica se a área de pré-visualização e a imagem ficam visíveis
    await expect(previewContainer).toBeVisible();
    await expect(previewImagem).toBeVisible();

    // Confirma que a imagem carregou com dimensões válidas
    const imagemCarregada = await previewImagem.evaluate((img) => {
      return img.complete && img.naturalWidth > 0;
    });
    expect(imagemCarregada).toBe(true);
  });
});