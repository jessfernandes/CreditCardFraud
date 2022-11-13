# Credit Card Fraud Classification API

---
## Introdução
Dadas as características das transações com cartão de crédito (.csv), formula-se um problema de detecção de anomalias para classificar as transações como fraudulentas ou não. Desta forma, são verificadas as características presentes no dataset, assim como: formato dos dados, dados faltantes, valores nulos, distribuição,além da verificação do balanceamento entre classes para posterior verificação de estratégias de pré-processamento. Ao utiliar estratégias de data engineering, nota-se que o melhor desempenho obtido entre os modelos testados para classificação fora Random Forest com data undersampling, o qual foi utilizado para classificar novas amostras nesta API.

Características do dataset [creditcard.csv](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud):
- *time*: número de segundos decorridos entre esta transação e a primeira transação no conjunto de dados;
- *v1...v28*: possível resultado de uma redução de dimensionalidade via PCA para proteger identidades de usuários e recursos confidenciais;
- *amount*: valor da transação;
- *class*: classificação da transação sendo 1 para transações fraudulentas e 0, caso contrário.

---
## API: step by step
1. Analisou-se os dados.
2. Baseando-se nos dados analisados, dividiu-se o conjunto em dois subconjuntos (treino 80% e teste 20%). Avaliou-se três modelos
supervisionados e gerou-se um modelo treinado com a abordagem de machine learning que obteve melhores resultados.
Utilizou-se apenas o conjunto de treinamento nessa atividade, sendo implementadas técnicas que melhorassem
o desempenho do modelo proposto, tais como aumento de dados, seleção de features, balanceamento das amostras de
treinamento entre outras.
3. Desenvolveu-se uma API com Pyhton (Django) que possibilite ao usuário (endpoints):
    - Sistema de login utilizando JWT (JSON Web Token)
      - Usuário Padrão
      - Tempo de validação de acesso
        - Renovação = 24 horas
        - Acesso = 30 minutos
    - Classificou-se uma nova amostra baseada no treinamento realizado na etapa 2.
      - Usuário informa os dados de “v1 a vn” e “Amount” que representam as features extraídas do processo financeiro
      - Sistema retorna à predição (classe e a probabilidade)
      - Salva-se os dados informados e a predição no banco de dados PostgreSQL.
    - Visualiza todas as predições realizadas.
    - Excluir uma predição realizada.

---
## Pré-requisitos
1. A utilização do ambiente requer a instalação do Python 3.x, assim como outras bibliotecas Python podem ser requeridas. Antes de começar, recomendo fortemente que leia a documentação do Django.
2. Foi utilizado o sistema operacional Ubuntu 20. LTS para preparo e desenvolvimento deste ambiente.
3. É necessária a instalação do Docker e dependências.

---
## Instalação e Execução
1. Para instalar este projeto, basta clonar o projeto através do link do repositório.
```
$ git clone https://github.com/jessfernandes/CreditCardFraud.git --branch develop
```
2. Após o clone deste projeto, acesse o diretório ```CredictCardFraud```.
```
$ cd CredictCardFraud
```
3. Para este projeto, utilizou-se para execução o Docker compose. Desta forma, considerando o Docker já instalado, basta testar o sistema através do comando:
```
$ sudo docker-compose up
```
