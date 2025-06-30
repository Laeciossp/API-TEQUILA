# app/core/config.py

# Importe BaseSettings do pacote correto: pydantic_settings
# Importe SettingsConfigDict para configurar o carregamento do .env (Pydantic v2 style)
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Defina suas variáveis de ambiente aqui.
    # Pydantic Settings irá automaticamente procurar e carregar a variável de ambiente
    # com o nome TEQUILA_API_KEY.
    # Se esta variável não for encontrada no ambiente onde a aplicação está rodando
    # (por exemplo, no Cloud Run), o Pydantic levantará um erro de validação ao iniciar.
    # Isso é um comportamento desejável para garantir que todas as configurações obrigatórias estejam presentes.
    TEQUILA_API_KEY: str

    # Configuração do modelo para Pydantic v2 (substitui a antiga 'class Config:')
    # Define como as variáveis de ambiente serão carregadas.
    model_config = SettingsConfigDict(
        # Especifica o arquivo .env a ser carregado.
        # Isso é útil para o desenvolvimento local.
        # No Cloud Run (e outros ambientes de produção), as variáveis de ambiente
        # serão injetadas diretamente no ambiente do contêiner e terão precedência
        # sobre o arquivo .env, então este arquivo .env não será usado lá.
        env_file=".env",

        # Define a codificação do arquivo .env. 'utf-8' é um bom padrão.
        env_file_encoding='utf-8',

        # Controla o comportamento para variáveis de ambiente que não são explicitamente
        # declaradas na classe Settings.
        # 'ignore': Ignora variáveis de ambiente que não estão na classe Settings.
        # 'allow': Permite que variáveis de ambiente extras sejam carregadas.
        # 'forbid': Proíbe variáveis de ambiente extras (levantará um erro se existirem).
        # 'ignore' é um bom padrão para não causar problemas com variáveis de sistema.
        extra='ignore'
    )

# Crie uma instância da sua classe Settings.
# Esta instância irá automaticamente carregar os valores das variáveis de ambiente
# quando a aplicação for iniciada.
settings = Settings()

