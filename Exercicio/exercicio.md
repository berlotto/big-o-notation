## Análise de Complexidade dos Algoritmos para Cálculo de Pi

### Introdução
Neste documento, vamos analisar a complexidade dos três algoritmos implementados para calcular o valor de Pi: Leibniz, Machin e Gauss-Legendre. A complexidade de um algoritmo nos dá uma ideia de como o tempo de execução cresce à medida que o tamanho da entrada aumenta.

### Método de Leibniz
* **Complexidade:** O(n)
* **Explicação:** A cada iteração, uma operação é realizada, resultando em uma complexidade linear.

### Método de Machin
* **Complexidade:** O(n)
* **Explicação:** Apesar de envolver duas chamadas à função arctan, a complexidade geral permanece linear devido à estrutura dos loops.

### Método de Gauss-Legendre
* **Complexidade:** Quase linear (melhor que O(n))
* **Explicação:** A cada iteração, o número de dígitos significativos aproximadamente dobra, resultando em uma convergência quadrática.

### Comparação e Considerações
* **O(n):** Algoritmos de Leibniz e Machin apresentam uma complexidade linear, o que significa que o tempo de execução cresce proporcionalmente ao número de iterações.
* **Quase linear:** O algoritmo de Gauss-Legendre converge mais rapidamente, sendo mais eficiente para obter uma alta precisão.
* **Fatores adicionais:** A escolha do algoritmo ideal depende de diversos fatores, como a precisão desejada, os recursos computacionais disponíveis e a complexidade de implementação.

### Como Analisar a Complexidade
* **Identificar as operações básicas:** Quais operações são repetidas?
* **Expressar o número de operações em função do tamanho da entrada:** Como o número de operações varia com o aumento do tamanho da entrada?
* **Identificar o termo dominante:** Qual termo cresce mais rapidamente?
* **Descartar constantes e termos de ordem inferior:** Esses termos não afetam significativamente a complexidade assintótica.
* **Expressar a complexidade na notação Big O:** Utilizar a notação O(n), O(log n), O(n^2), etc.

**Observação:** Para uma análise mais profunda, pode-se utilizar ferramentas de profiling para medir o tempo de execução real dos algoritmos e comparar os resultados.

### Conclusão
A análise de complexidade é fundamental para escolher o algoritmo mais adequado para uma determinada tarefa. Ao entender a complexidade de cada algoritmo, podemos tomar decisões mais informadas sobre a implementação e otimização de nossos programas.