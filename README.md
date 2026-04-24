# Playwright - Not Inserted Capture

## Descrição

Este projeto automatiza o acesso ao sistema VSN utilizando Playwright. Realiza login, navega até a área de contratos comerciais, executa a importação de anúncios e captura o total de registros "Not Inserted".

## Tecnologias

* Python
* Playwright

## Como executar

### 1. Clonar o repositório

```bash
git clone <url-do-repo>
cd <nome-do-repo>
```

### 2. Instalar dependências

```bash
pip install playwright
playwright install
```

### 3. Executar o script

```bash
python nome_do_arquivo.py
```

## Configuração

Atualize as credenciais no código:

```python
page.locator('#email').fill('SEU_USUARIO')
page.locator('#password').fill('SUA_SENHA')
```

## Funcionalidade

* Login automático no sistema
* Navegação até contratos comerciais
* Abertura de playlist de anúncios
* Execução de importação
* Captura e soma dos valores da tabela "Not Inserted"
* Exibição do total no console

## Observações

* O script depende da estrutura atual da página e seletores podem mudar
* Pode ser necessário ajustar tempos de espera (timeouts)
* Recomenda-se uso em ambiente controlado
