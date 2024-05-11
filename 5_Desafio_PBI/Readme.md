## 1) Home Page:
 <b><u>Capa</u></b><br>
Inicia com o resumo do que o Relatório representa, meu nome e um botão para acessar a página principal do relaório <br><br>

## 2) <b><u> Principal</u></b>
Ja veio criada, mas inseri o botão de home e navegação para direita e esqueda.
Nessa aba é composta por <b>CARDS</b>:
 - Total de Vendas
 - Unidades Vendidas
 - Soma de Disconts
 - Máximo sold **** Fiz isso pois estava repetido oc ard de Soma Disconts
 - Soma COGS

<b><u>GRÁFICO DE LINHA:</u></b>
Vendas por Período (Mês)

<b><u>GRÁFICO BARRAS CUSTERIZADO</u></b>
Vendas por Produto

<b><u>GRÁFICO BAR CHART E PIER CHAT</u></b>
Vendas por Segmento

<b><u>TREEMAP</u></b>
Vendas por Países<br><br>

## 3) Detalhes

<b><u>GRÁFICO COLUNA CLUSTERIZADO:</u></b>
 - Total de Vendas por Mes
 - Total de Vendas por Semestres
 
<b><u>GRÁFICO MATRIZ</u></b>
 - Ttal de Vendas (Trimestre x Ano)

<b><u>GRÁFICO DE COLUNA CUSTERIZADO (histograma)</u></b>
 - Total de Unidades Vendidas x Buckets

<b><u>GRÁFICO DE BARRA CUSTERIZADO </u></b>
 - Total de Unidades Vendidas x Buckets
<br><br>

## 4) TOP 3 Produtos

Foi criado um parâmetro para ser utilizado no GRÁFICO DE COLUNAS EMPILHADOS por TOP 3 PRODUTOS com linha da META

```
Parâmetro 2 = {
    ("Continentes", NAMEOF('financials'[Continentes]), 0),
    ("Country", NAMEOF('financials'[Country]), 1),
    ("Segmentos", NAMEOF('financials'[Segment]), 2),
    ("Segmentos agrupados", NAMEOF('financials'[Segmentos agrupados]), 3),
    ("Discount Band", NAMEOF('financials'[Discount Band]), 4),
    ("Mês", NAMEOF('financials'[Month Name]), 5)
}
```
<br><br>
## 5) MAIORES VENDAS

Foi utilizado o parâmetro criado anteriormente para ser utilizado no GRÁFICO DE COLUNAS EMPILHADOS por MAIORES VENDAS com linha da META <br><br>

## 6) GRÁFICO DE DISPERSÃO 
Eixo X com os nomes dos meses e Exo Y com o seguinte parâmentro
```
Parâmetro 3 = {
    ("total sales", NAMEOF('financials'[total sales]), 0),
    ("total de vendidos", NAMEOF('financials'[total de vendidos]), 1),
    ("Máximo sold", NAMEOF('financials'[Máximo sold]), 2),
    ("Média sales", NAMEOF('financials'[avg sales]), 3),
    ("Outlier", NAMEOF('financials'[outlier]), 4)
}```
