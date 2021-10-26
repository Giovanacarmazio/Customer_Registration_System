# Sistema de Cadastro de Clientes - Provedor

O uso de matrizes em programação é muito comum para armazenar uma quantidade limitada de dados. Em Python, as matrizes podem armazenar conteúdos de diferentes tipos de dados; isso torna o seu uso bem interessante para guardar dados de clientes, como, por exemplo, nome, idade, CPF, entre outros, de uma loja ou supermercado.

Suponha que você trabalha como programador de um provedor de Internet e está desenvolvendo um sistema de cadastro de clientes. Seu supervisor solicitou que você implementasse uma nova funcionalidade no sistema: ele quer digitar pelo teclado dados de dois clientes (nome, idade, CPF) e armazená-los em uma matriz. Em seguida, ele deseja que esses dados sejam salvos em um arquivo de texto formatado em uma tabela, como mostra a figura a seguir:


![giphy](https://github.com/Giovanacarmazio/Sistema-Cadastro-Cliente/blob/a486c968b5bc2972a5a09ba28146334461fbb154/desafio_5_2_enunciado.jpg)

Para desenvolver esse código, deve-se seguir os seguintes passos:

* Criar uma matriz 2x3 para armazenar os dados dos clientes.

* Utilizar dois laços fors aninhados para preencher a matriz com os dados digitados pelo teclado.

* Dentro do laço mais interno, testar qual coluna da tabela está preenchendo: Nome - coluna 0, Idade - coluna 1 e CPF - coluna 2. E solicitar o dado de acordo com a coluna a ser preenchida.

* Após o preenchimento da matriz, armazenar os dados digitados em um arquivo. Para isso, abrir o arquivo utilizando o modo de abertura write, para criar o arquivo e preencher as duas primeiras linhas da formatação dos dados em tabela conforme solicitado.

* Antes de começar a percorrer a matriz com os dados e imprimir o conteúdo formatado como uma tabela, abrir o arquivo utilizando o modo de abertura append.

* Para imprimir os dados formatados em tabela, utilizar dois laços fors aninhados.
