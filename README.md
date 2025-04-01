### Creating the Virtualenv

Criação do ambiente de teste

```bash
# create virtualenv
python -m venv python_env

# active virtualenv
source python_env/bin/activate

```

### vscode extensions

A pasta .vscode possui sugestões de extensions e uma configuração customizada para formatar automaticamente o código após salvar


### pylint

Caso vc precise de de algum auxilio somente na hora de escrever o codigo a extension do pylint ja ajuda, caso precise, fazer alguma analise de todo o codigo pode utilizar a lib do pylint, am ambos os casos podem ser utilizados o arquivo .pylintrc; ele não vai afetar o comportamento da biblioteca, 


### pylint lib

Instalaçao da lib de análise de código, caso precise de agluma configuração customizada, copiar o .pylintrc de algum projeto existe ou usar o comando para criar um arquivos com condigs default.

```bash
# Install dependencies
pip install pylint

#create file for custom config
pylint --generate-rcfile > .pylintrc

# Run lint
pylint src
```