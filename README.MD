# Análise de sentimentos de textos -  Linguagem de programação - Unilasalle 2021.1

1. Quantas palavras existem no texto
2. Uma análise de sentimentos do texto:
   1. Quantas palavras ofensivas (swear) existem no texto
   2. Quantas palavras de ansiedade (anx) existem no texto
3. Qual é o tom geral do texto: positivo (posemo) ou negativo (negemo) em relação a quantidade de palavras

No processo de busca dessas respostas, teremos que limpar a string removendo por exemplo vírgulas e pontos e transformar tudo em minúsculos. Também teremos que dividir nosso string em uma lista de palavras, um processo conhecido como "tokenização". Cada token deverá ser consultado no LIWC para fazer a análise de sentimentos gerais do texto.

## Sua tarefa é criar três programas, em três paradigmas diferentes, que resolvem o mesmo problema acima.

## Programação Estruturada (2.0pt):

* Os únicos métodos de manipulação de strings que você pode usar são: split, append e length. Todo o resto (modificações, remoções) deve ser feito com loops.
* Organize suas funções como quiser.
* Organize seus dados como quiser.

## Programação Orientada a Objetos (2.0pt):

* Você deve implementar PELO MENOS três classes:
  * Uma que manipula uma string, limpa ela e retorna uma lista de tokens.
  * Uma que manipula uma lista de tokens sem caracteres especiais e retorna as respostas
  * Uma classe, filha da segunda, que trata de tokens COM caracteres especiais e retorna as respostas.
* Você deve usar encapsulamento, mesmo que a linguagem não tenha suporte padrão (i.e. getters e setters)
* implementar pelo menos um método sobrecarregado na classe filha.
* Pode adaptar suas funções da programação imperativa como métodos em OO

## Programação Funcional (2.0pt):

* Você NÃO pode permitir efeitos colaterais
* Você NÃO pode alterar o estado de forma nenhuma ( i.e., tudo é const)
* Não use loops. Se quiser repetição faça com funções ou com recursão.
* Pode usar loops, desde que dentro de funções.
* Use funções map,filter,reduce a vontade
* Você pode adaptar funções/métodos anteriores, desde-que aderentes ao funcional

## opcional (2,0pt adicionais):

* Implemente uma interface gráfica para consulta de texto em pelo menos um paradigma.
* Consumir textos de APIs de redes sociais (twitter,facebook,etc..) é um plus.

Você pode usar Python ou Javascript/TS

Para realizar a análise de sentimento, você verá abaixo o dicionário LIWC e um conjunto de funções que acessa o LIWC e dá a resposta para um token solicitado.

Python: ( entende português)

[https://replit.com/@RaphaelAbreu/liwc#main.py](https://replit.com/@RaphaelAbreu/liwc#main.py)

NodeJS: ( entende inglês)

[https://replit.com/@RaphaelAbreu/liwcNodeJS#index.js](https://replit.com/@RaphaelAbreu/liwcNodeJS#index.js)
