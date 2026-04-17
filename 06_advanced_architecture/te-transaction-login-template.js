import { browser, markers } from 'thousandeyes';

// Template de Transação Sintética: Teste de Login em Portal Web
export default async function() {
    // 1. Inicia o navegador e abre a página
    await markers.start('Load_Login_Page');
    await browser.configure({'actionTimeout': 10000});
    await browser.visit('https://portal.suaempresa.com/login');
    await markers.stop('Load_Login_Page');

    // 2. Tira uma foto de como a tela carregou
    await browser.takeScreenshot();

    // 3. Preenche Usuário e Senha
    await markers.start('Submit_Credentials');
    await browser.type('#username', 'usuario_monitoramento');
    await browser.type('#password', 'SenhaSegura123!');
    
    // Clica no botão de Login e aguarda a nova página carregar
    await Promise.all([
        browser.waitForNavigation(),
        browser.click('#btnLogin')
    ]);
    await markers.stop('Submit_Credentials');

    // 4. Valida se o login deu certo procurando um elemento do Dashboard
    const dashboardExists = await browser.isElementPresent('.dashboard-header');
    if (!dashboardExists) {
        throw new Error("Falha no login: Header do Dashboard não encontrado.");
    }
    
    console.log("Transação concluída com sucesso!");
}