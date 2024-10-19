```markdown
```mermaid
graph TD
    A[Início] --> B[Carregar bibliotecas]
    B --> C[Buscar arquivo JSON]
    C --> D[Carregar dados no DataFrame]
    D --> E[Selecionar colunas necessárias]
    E --> F[Renomear colunas]
    F --> G[Carregar variáveis de ambiente]
    G --> H[Criar conexão com o banco de dados]
    H --> I[Habilitar cursor]
    I --> J[Deletar dados existentes na tabela]
    J --> K[Inserir dados no banco de dados]
    K --> L[Confirmar alterações]
    L --> M[Fechar cursor e conexão]
    M --> N[Fim]
