
# Análise de Dados Governamentais: Receitas e Despesas 📊

Este projeto foi desenvolvido para analisar e visualizar **receitas** e **despesas governamentais**, oferecendo uma visão clara do **superávit** ou **déficit** de diferentes órgãos públicos. Através do uso de **Python** e bibliotecas poderosas como **Pandas** e **Plotly**, o projeto apresenta uma solução robusta para extrair insights financeiros e identificar quais órgãos possuem maior peso no orçamento público.

## ⚙️ Funcionalidades

- **Análise de Superávit/Deficit**: Comparação de receitas e despesas para cada órgão, destacando aqueles que operam com saldo positivo ou negativo.
- **Identificação dos Órgãos com Maior Peso no Orçamento**: Determina quais órgãos têm maior impacto financeiro através de sua participação percentual no total de receitas e despesas.
- **Visualizações Interativas**: Gráficos de barras, pizza e linhas para facilitar a compreensão dos dados, tudo de forma interativa com a biblioteca Plotly.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Pandas**: Manipulação e agregação de dados.
- **Plotly**: Visualizações interativas, como gráficos de barras, pizza e linhas.
- **JSON**: Formato de entrada para os dados de receitas e despesas.

## 📊 Visualizações

As visualizações geradas pelo projeto incluem:

- **Gráfico de Barras**: Comparação de receitas e despesas por órgão.
- **Gráfico de Pizza**: Participação percentual de cada órgão no total de receitas e despesas.
- **Gráfico de Linhas**: Exibição do superávit ou déficit de cada órgão.
- **Gráfico de Barras - Peso no Orçamento**: Mostra a participação relativa dos órgãos nas receitas e despesas.

## 📂 Estrutura de Arquivos

- `receitas.json`: Arquivo JSON contendo as receitas por órgão.
- `despesas.json`: Arquivo JSON contendo as despesas por órgão.
- `analisereceitas_despesas.py`: Script principal que carrega os dados, realiza as análises e gera as visualizações.
  
## 🚀 Como Executar o Projeto

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/usuario/repo
   cd repo
   ```

2. **Instale as dependências**:
   Certifique-se de que você tenha o Python e pip instalados.
   ```bash
   pip install pandas plotly
   ```

3. **Substitua os arquivos de receitas e despesas pelos seus dados**:
   Coloque os arquivos `receitas.json` e `despesas.json` na pasta raiz do projeto.

4. **Execute o script**:
   ```bash
   python analisereceitas_despesas.py
   ```

5. **Visualize os gráficos**:
   As visualizações interativas serão abertas diretamente no seu navegador.

## 📈 Exemplo de Uso

Ao executar o script, você verá gráficos interativos que mostram:

- A comparação entre receitas e despesas por órgão.
- A proporção de receitas e despesas de cada órgão no orçamento total.
- Órgãos que apresentam superávit ou déficit.
- Os órgãos com maior participação no orçamento público.

## 📝 Licença

Este projeto está licenciado sob os termos da licença MIT. Para mais informações, consulte o arquivo LICENSE.
