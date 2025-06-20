
# Sistema de Monitoramento de Vício em Jogos

## Visão Geral
O sistema implementado no `app.py` é uma ferramenta sofisticada para monitorar e avaliar comportamentos potencialmente viciantes relacionados a jogos, utilizando diversos indicadores e métricas para identificar padrões de risco.

## Instalação e Execução do Sistema

### Requisitos Prévios
- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

### Passo a Passo para Instalação

1. **Criar e ativar ambiente virtual (venv)**

No Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

No Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. **Instalar dependências**
```bash
pip install -r requirements.txt
```

3. **Executar o sistema**
```bash
python app.py
```

### Observações Importantes
- Certifique-se de que o ambiente virtual (venv) está ativado antes de instalar as dependências
- O ambiente virtual deve ser ativado sempre que for executar o sistema
- Para desativar o ambiente virtual, use o comando `deactivate`


## Funcionamento do Sistema

### 1. Coleta de Dados
O sistema monitora três variáveis principais:
- **Sessões (S)**: Número de vezes que o usuário acessa o jogo
- **Tempo Jogado (T)**: Duração total do tempo de jogo em minutos
- **Valor Apostado (A)**: Quantidade de dinheiro apostada em Reais

### 2. Índices de Monitoramento
O sistema calcula quatro índices principais:

#### a) IFA (Índice de Frequência Aumentada)
- Mede o aumento na frequência de sessões de jogo
- Calculado pela variação no número de sessões ao longo do tempo

#### b) IAT (Índice de Aceleração do Tempo)
- Monitora o aumento no tempo gasto jogando
- Analisa a variação do tempo de jogo entre dias consecutivos

#### c) IAG (Índice de Aceleração de Gastos)
- Acompanha o aumento nos valores apostados
- Calcula a variação nos gastos ao longo do tempo

#### d) ICRV (Índice Composto de Risco de Vício)
- Combina os três índices anteriores com pesos específicos:
  - 40% para gastos (IAG)
  - 30% para tempo (IAT)
  - 30% para frequência (IFA)

### 3. Avaliação de Risco
O sistema classifica o comportamento do usuário em diferentes níveis de risco:

1. **Risco Baixo**: Comportamento normal
2. **Possível Comportamento Compulsivo**: Quando IAG > 50
3. **Alto Risco**: Quando IAT > 30
4. **Comportamento Viciante Emergente**: Quando IFA > 100
5. **Necessidade de Intervenção**: Quando ICRV > 100

### 4. Alertas Especiais
- O sistema possui um mecanismo específico para detectar comportamento compulsivo quando o IAG permanece elevado (>50) por três dias consecutivos


### 5. Visualização Diagrama de Venn
- O Sistema irá abrir, no final, uma janela com o Diagrama de Venn indicando em ordem onde houve:
- 1. **Necessidade de Intervenção**: Quando ICRV > 100
- 2. **Possível Comportamento Compulsivo**: Quando IAG > 50
- 3. **Alto Risco**: Quando IAT > 30
- 4. **Risco Baixo**: Comportamento normal


## Funcionamento Técnico
- Utiliza a biblioteca Pandas para manipulação de dados
- Realiza cálculos diários para todos os índices
- Mantém um histórico temporal das métricas
- Implementa tratamento para evitar divisões por zero
- Preenche valores ausentes no início do monitoramento

## Benefícios do Sistema
1. **Monitoramento Contínuo**: Acompanhamento diário do comportamento
2. **Detecção Precoce**: Identifica padrões problemáticos antes que se tornem severos
3. **Análise Multifatorial**: Considera diferentes aspectos do comportamento viciante
4. **Classificação de Risco**: Fornece alertas baseados em níveis de gravidade

## Recomendações de Uso
1. Manter registros diários consistentes
2. Monitorar especialmente períodos de aumento súbito nos índices
3. Prestar atenção especial quando múltiplos índices apresentarem elevação simultânea
4. Considerar intervenção profissional quando alertas de alto risco forem emitidos

Este sistema representa uma ferramenta importante para o monitoramento e prevenção de comportamentos viciantes em jogos, oferecendo uma abordagem sistemática e baseada em dados para identificação de riscos.