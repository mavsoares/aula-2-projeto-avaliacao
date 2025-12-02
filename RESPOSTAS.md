# Respostas do Trabalho - Pipeline de ML

## Identificação do Grupo

- **Integrantes:**
    1. Nome: Guilherme Silveira Rabelo
    2. Nome: Marcos Vinícius Soares
    3. Nome: Modestino André Rodrigues Neto
    4. Nome: Thiago Marques Silva

---

## Parte 1: Resultados do Pipeline

### 1.1 O pipeline executou sem erros?

<!-- Marque com X a opção correta -->

- [X] Sim
- [ ] Não

### 1.2 F1-Score obtido:

<!-- Copie o valor exibido ao final da execução -->

```
F1-Score: 0.4043
```

### 1.3 Cole aqui o output final do pipeline:

<!-- Execute: python main.py e copie a saída -->

```
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
INICIANDO PIPELINE DE ML
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀


[ETAPA 1/4] Carregando dados...
==================================================
EXPLORAÇÃO DOS DADOS
==================================================
Shape: (5000, 8)

cliente_id              int64
idade                   int64
renda_mensal          float64
tempo_conta_meses       int64
num_produtos            int64
tem_cartao_credito      int64
score_credito         float64
respondeu_campanha      int64
dtype: object

   cliente_id  idade  renda_mensal  tempo_conta_meses  num_produtos  tem_cartao_credito  score_credito  respondeu_campanha
0           1     56      46917.46                229             4                   1          600.0                   1
1           2     69      41274.41                  9             3                   0          758.2                   0
2           3     46      40649.98                 25             2                   1          595.7                   1
3           4     32      44336.79                217             5                   1          584.3                   0
4           5     60      35301.68                225             4                   0          797.8                   0
==================================================

DISTRIBUIÇÃO DO TARGET
------------------------------

respondeu_campanha
0    2803
1    2197
Name: count, dtype: int64

respondeu_campanha
0    0.5606
1    0.4394
Name: proportion, dtype: float64
------------------------------

[ETAPA 2/4] Validando dados...
✅ Dados válidos!

[ETAPA 3/4] Treinando modelo...
Dados de treino: 4000 registros
Dados de teste: 1000 registros

Treinando modelo...
✅ Modelo treinado!

Modelo salvo em: models/modelo_campanha.pkl

[ETAPA 4/4] Avaliando modelo...

==================================================
RESULTADOS DA AVALIAÇÃO
==================================================

📊 MÉTRICAS:
   Accuracy:  0.5550 (55.50%)
   Precision: 0.4951
   Recall:    0.3416
   F1-Score:  0.4043

📋 MATRIZ DE CONFUSÃO:
   Verdadeiros Negativos (TN): 404
   Falsos Positivos (FP):      154
   Falsos Negativos (FN):      291
   Verdadeiros Positivos (TP): 151

==================================================
🎯 F1-SCORE FINAL: 0.4043
==================================================

✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅
PIPELINE CONCLUÍDO COM SUCESSO!
✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅
```

---

## Parte 2: Interpretação dos Resultados

### 2.1 O modelo é bom ou ruim? Por quê?

O modelo é ruim, pois:

- F1 < 0.5 → pior que aleatório
- Previsões positivas têm precisão baixa (0.49).
- O modelo deixa escapar muitos positivos reais: recall = 0.34.

### 2.2 O dataset é balanceado ou desbalanceado? Como você descobriu?

O dataset é praticamente balanceado, pois as duas classes aparecem em proporções próximas (56% vs 44%).

### 2.3 Por que usamos F1-Score e não apenas Accuracy neste caso?

Embora o dataset seja relativamente balanceado, Accuracy pode dar uma falsa impressão de bom desempenho, porque ela só mede quantas previsões o modelo
acertou — mas não mostra como acertou.

Mediante análise do modelo, verificamos:

- Ele erra muitos positivos → Recall = 0.34 (muito baixo)
- Ele acerta pouco quando diz que é positivo → Precision = 0.49
- Ele tem mais falsos negativos (291) do que verdadeiros positivos (151)

Ademais, se o modelo previsse sempre 0 já teria acurácia comparável à atual.

Portanto, usamos F1-Score porque ele:

- é mais sensível a erros importantes (FN e FP)
- avalia o desempenho no que realmente importa: previsões positivas
- evita ilusões criadas pela acurácia
- indica que o modelo está pior que aleatório, algo que a Accuracy não mostra

---

## Parte 3: Validação de Dados

### 3.1 Liste as validações Pandera que você implementou:

1. cliente_id: Column(int, nullable=False, unique=True)
2. idade: Column(int, Check.in_range(18, 80))
3. renda_mensal: Column(float, Check.in_range(1000, 50000))
4. score_credito: Column(float, Check.in_range(300, 850))
5. respondeu_campanha: Column(int, Check.isin([0, 1]))

### 3.2 Por que validar dados ANTES de treinar o modelo?

Validar dados antes de treinar é crucial para garantir que o modelo aprenda padrões reais e confiáveis.

Sem validação, o modelo pode ter desempenho ruim, previsões instáveis e comportamento inesperado — mesmo que pareça funcionar no treinamento.

Se dados inválidos entrarem no modelo em produção, os impactos podem ser sérios — desde quedas na performance até decisões totalmente erradas. Isso pode
gerar prejuízo financeiro, desgaste com clientes ou decisões estratégicas ruins.

Por isso, validar dados antes da entrada no modelo e monitorá-los continuamente é fundamental.

---

## Parte 4: Versionamento

### 4.1 Liste os commits que vocês fizeram (copie do git log):

<!-- Execute: git log --oneline e cole aqui -->

```
d43bbf9 (HEAD -> main, origin/main) Implementação do treinamento do modelo
9498412 Implementação do treinamento do modelo
a28da36 Implementação da validação utilizando Pandera
6ba623f Implementação da validação utilizando Pandera
5ea5bba Implementação do carregamento dos dados
c7e220d Implementação do carregamento dos dados
8b2a849 Criação do projeto
```

### 4.2 Por que mensagens de commit descritivas são importantes?

Mensagens de commit descritivas são fundamentais porque ajudam a manter a clareza, a organização e a rastreabilidade do projeto. Elas explicam por que uma
mudança foi feita e o que exatamente foi alterado, facilitando a vida de todos que trabalham no código.

---

## Parte 5: Reflexão (Opcional)

### 5.1 Qual foi a maior dificuldade do grupo?

A maior dificuldade foi analisar corretamente os resultados e entender como ajustar o modelo, especialmente no que diz respeito ao rebalanceamento e às
métricas (como F1-score) que indicaram um desempenho abaixo do esperado. Interpretar o impacto dos falsos negativos e falsos positivos também exigiu
atenção.

### 5.2 O que vocês fariam diferente se fossem refazer?

Refaríamos o treinamento aplicando técnicas de rebalanceamento e testaríamos outros algoritmos para buscar um F1-Score mais alto e um equilíbrio melhor
entre precisão e recall. 

Além disso, consideraríamos coletar mais dados ou enriquecer o dataset, pois um volume maior e mais variado de informações poderia
ajudar o modelo a aprender padrões mais sólidos e melhorar o desempenho geral.

---

**Data de entrega:** 02/12/2025
