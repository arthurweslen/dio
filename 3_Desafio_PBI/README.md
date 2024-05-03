### Projeto de Modelagem 👋

Na modelagem foi necessário criar tabelas Fatos:<br>
💻 f_Financials <br>
💻 f_Product_Details <br>
💻 f_Vendas<br>
<br>
e tabelas dimensões<br>
💻 d_details<br>
💻 d_product<br>
💻 d_desconto<br>
💻 d_categoria<br>

Removendo colunas desnecessárias para cada dimensão e tabela fato.
Criando ID de produto para criar relacionamento (necessário na modelagem Star Schema)
e no DAX foi criado a D_Calendario utilizando calendarauto()
