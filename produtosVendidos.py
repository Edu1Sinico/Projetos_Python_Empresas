import matplotlib as plt
import pandas as pd
import yaml

# Carregar dados do arquivo YAML
with open("Biblioteca-matplot-seaborn-8/Projeto/empresa.yaml", "r") as file:
    dados = yaml.safe_load(file)

# Criar DataFrame com os dados
df_vendas = pd.DataFrame(dados('vendas'))
df_comp_cliente: pd.DataFrame(dados('comportamento_do_cliente:'))
df_desen_prod: pd.DataFrame(dados('desempenho_do_produto:'))

# Plotar histograma da idade com Matplotlib
plt.figure(figsize=(8, 6))  # Criar uma figura com tamanho específico
plt.hist(df_vendas["preco_unitario"], bins=5, color="skyblue", edgecolor="black")  # Plotar histograma
plt.title("Produtos Mais vendidos")  # Definir título do gráfico
plt.xlabel("Valor")  # Definir rótulo do eixo x
plt.ylabel("Frequência")  # Definir rótulo do eixo y
plt.grid(True)  # Habilitar grade no gráfico
plt.show()  # Mostrar o gráfico
