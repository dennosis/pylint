# extensions suggestions

## Creating the Virtualenv

Criação do ambiente de teste

```bash
# create virtualenv
python3 -m venv python_env

# active virtualenv
source python_env/bin/activate

# install dependencies
pip3 install -r requirements.txt

```

## vscode extensions and config

A pasta .vscode possui sugestões de extensions e uma configuração customizada para formatar automaticamente o código após salvar os arquivos .py

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## pylint

Caso você precise de auxílio apenas na hora de escrever o código, a extensão do VS Code Pylint já ajuda. Caso precise fazer uma análise de todo o código, pode utilizar a biblioteca Pylint. Em ambos os casos, pode ser utilizado o arquivo .pylintrc, que é um arquivo de configuração de análise de código customizado. Se ele não existir na raiz do projeto, tanto a extensão quanto a biblioteca usarão a configuração padrão para fazer as análises.

## pylint lib

Instalação da biblioteca Pylint para análise de código. Caso precise de alguma configuração customizada, copie o arquivo .pylintrc de algum projeto existente ou use um comando para criar um arquivo com configurações padrão.

```bash
# Install dependencies
pip install pylint

#create file for custom config
pylint --generate-rcfile > .pylintrc

# Run lint
pylint src
```
