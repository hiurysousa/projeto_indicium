# Desafio LH Nautical — Jornada de Dados

Projeto desenvolvido como parte do processo seletivo da Indicium, simulando a atuação de um profissional de dados na LH Nautical, empresa de varejo de peças e acessórios para embarcações.

---

## Contexto

A LH Nautical enfrenta um cenário de desorganização de dados: controle de estoque em planilhas manuais, desconexão entre sistemas e decisões baseadas em "feeling". O objetivo deste projeto é transformar esse cenário através de uma jornada completa de dados, da limpeza e modelagem até a geração de insights preditivos e sistemas de recomendação.

---

## Estrutura do Projeto

```
projeto_indicium/
│
├── datasets/
│   ├── raw/                          # Dados brutos originais — nunca modificados
│   │   ├── produtos_raw.csv
│   │   ├── vendas_2023_2024.csv
│   │   ├── custos_importacao.json
│   │   ├── clientes_crm.json
│   │   └── clientes.csv
│   │
│   ├── processed/                    # Dados após limpeza e tratamento
│   │   ├── produtos_clean.csv
│   │   ├── vendas_clean.csv
│   │   └── df_importacao_final.csv
│   │
│   └── output/                       # Resultados finais das análises
│       ├── prejuizo_com_nomes.csv
│       ├── prejuizo_por_produto.csv
│       └── vendas_com_prejuizo.csv
│
├── docs/                             # Documentação técnica
│   ├── modelagem.png                 # Diagrama ER das tabelas
│   ├── passo_a_passo.png             # Fluxo de desenvolvimento
│   └── documentacao_projeto.docx     # Documentação completa
│
├── scripts/
│   ├── funcoes/                      # Funções reutilizáveis
│   │   ├── __init__.py
│   │   └── tratamento.py
│   ├── venv/                         # Ambiente virtual
│   ├── questao_1.ipynb               # EDA
│   ├── questao_2.ipynb               # Tratamento de Dados
│   ├── questao_3.ipynb               # Análise de Vendas
│   ├── questao_4.ipynb               # Análise de Clientes
│   ├── questao_5.ipynb               # Previsão de Demanda
│   ├── questao_6.ipynb               # Dimensão de Calendário
│   ├── questao_7.ipynb               # Sistema de Recomendação
│   └── questao_8.ipynb
│
├── README.md                         # Este arquivo
└── requirements.txt                  # Dependências do projeto
```

---

## Fontes de Dados

| Arquivo | Formato | Descrição |
|---|---|---|
| `produtos_raw.csv` | CSV | Catálogo de produtos com preço e categoria |
| `vendas_2023_2024.csv` | CSV | Histórico de vendas de 2023 e 2024 |
| `custos_importacao.json` | JSON | Custos históricos em USD por produto |
| `clientes_crm.json` | JSON | Cadastro de clientes com localização e e-mail |

---

## Frentes de Entrega

| Questão | Frente | Descrição |
|---|---|---|
| 1 | EDA | Análise exploratória do dataset de vendas |
| 2 | Tratamento de Dados | Limpeza, padronização e modelagem das 4 fontes |
| 3 | Análise de Vendas | KPIs de faturamento, produtos e prejuízo |
| 4 | Análise de Clientes | Segmentação, ticket médio e diversidade de categorias |
| 5 | Previsão de Demanda | Modelo baseline com média móvel de 7 dias |
| 6 | Dimensão de Calendário | Média de vendas por dia da semana com dias zero |
| 7 | Sistema de Recomendação | Similaridade de cosseno para recomendação de produtos |

---

## Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/hiurysousa/projeto_indicium.git
cd projeto_indicium
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv scripts/venv

# Windows
scripts\venv\Scripts\activate

# Linux/Mac
source scripts/venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute os notebooks
Abra os notebooks na pasta `scripts/` em ordem cada questão parte dos dados tratados pela anterior.

---

## Decisões Técnicas Relevantes

- **Arquitetura de pastas**: separação em `raw/processed/output` garantindo que dados brutos nunca são sobrescritos
- **Câmbio BCB**: cotação de venda do dólar obtida via API pública do Banco Central para cada data única de venda
- **Custo vigente**: uso de `merge_asof` com `direction='backward'` para buscar o preço de custo mais recente anterior à data da venda
- **Dias sem venda**: construção de dimensão de calendário para incluir dias com venda zero nas médias
- **Data leakage**: modelo preditivo treinado exclusivamente com dados até 31/12/2023

---

## Stakeholders

| Stakeholder | Perfil |
|---|---|
| Gabriel Santos | Tech Lead — valoriza organização, documentação e clareza |
| Marina Costa | Gerente de Negócios — focada em resultados e margens |
| Sr. Almir | Fundador — precisa ser convencido por dados sólidos |

---

## Autor

Desenvolvido por **Hiury** como parte do processo seletivo Indicium — Março/2026.
