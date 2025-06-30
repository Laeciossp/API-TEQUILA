# Importe BaseSettings do pacote correto: pydantic_settings
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Defina suas variáveis de ambiente aqui.
    # Pydantic Settings irá automaticamente carregar a variável de ambiente
    # com o nome TEQUILA_API_KEY.
    TEQUILA_API_KEY: str

    class Config:
        # Pydantic Settings irá carregar variáveis do arquivo .env
        # para uso em ambiente de desenvolvimento local.
        # No Cloud Run, as variáveis de ambiente serão injetadas diretamente
        # e não usarão o .env, mas ter isso aqui é bom para o desenvolvimento local.
        env_file = ".env"
        # Opcional: Se você quiser que ele ignore variáveis não definidas no .env
        # env_file_encoding = 'utf-8' # Adicione se precisar de encoding específico

# Crie uma instância da sua classe Settings.
# Esta instância irá automaticamente carregar os valores das variáveis de ambiente
# (do .env em desenvolvimento ou diretamente do ambiente no Cloud Run).
settings = Settings()
