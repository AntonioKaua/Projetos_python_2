# Automação de Cadastro de Produtos

Este projeto realiza uma automação para cadastrar produtos em um sistema web utilizando Python. Ele interage com o navegador para preencher formulários automaticamente com dados extraídos de um arquivo CSV.

## Funcionalidades

- **Automação do Navegador**: Abre o navegador, acessa o sistema e preenche os campos do formulário.
- **Leitura de Dados**: Lê os dados de um arquivo CSV (`produtos.csv`).
- **Preenchimento Automático**: Preenche os campos do formulário com os dados dos produtos.
- **Interrupção Segura**: Permite interromper o script pressionando a tecla `ESC`.

## Estrutura do Projeto

```plaintext
automacao-cadastro-produtos/
├── README.md              # Documentação do projeto
├── requirements.txt       # Dependências do projeto
├── scripts/
│   ├── projeto01.py       # Script principal
│   ├── posicao.py         # Utilitário para capturar coordenadas
├── data/
│   ├── produtos.csv       # Dados dos produtos

Requisitos:
Python 3.x
Bibliotecas:
pyautogui
pandas
keyboard
```

Instalação
Clone o repositório:

git clone https://github.com/AntonioKaua/automacao-cadastro-produtos.git
Instale as dependências:

pip install -r requirements.txt
Configuração
Abra o arquivo posicao.py para identificar as coordenadas dos campos no formulário do sistema.
Atualize os valores de x e y no projeto01.py conforme as posições identificadas.
Execução
Certifique-se de que o arquivo produtos.csv contém os dados no seguinte formato:

| código | marca    | tipo          | categoria  | preço_unitário | custo | obs          |
|--------|----------|---------------|------------|----------------|-------|--------------|
| 1001   | Marca A  | Tipo Exemplo  | Categoria  | 10.99          | 8.50  | Nenhuma obs  |

Execute o script principal:

python scripts/projeto01.py
Para interromper a execução, pressione a tecla ESC.

Observações
Certifique-se de que o navegador Chrome está instalado e configurado como navegador padrão.
Ajuste as coordenadas no script para corresponderem à resolução da sua tela e à posição da janela do navegador.
