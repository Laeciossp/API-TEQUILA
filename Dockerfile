FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Esta linha copia o conteúdo do seu diretório 'app' local
# para o diretório '/app' dentro da imagem Docker.
# Isso significa que o seu arquivo 'main.py' (onde 'app = FastAPI()' está)
# ficará diretamente no diretório '/app' do contêiner.
COPY ./app .

# --- AQUI ESTÁ A CORREÇÃO ---
# REMOVIDO: ENV PORT 8080
# O Cloud Run já injeta a variável de ambiente PORT (com valor 8080).
# Não precisamos defini-la aqui, o Uvicorn vai detectá-la automaticamente.

# Comando para iniciar sua aplicação FastAPI com Uvicorn.
# O Uvicorn é inteligente o suficiente para usar automaticamente
# a variável de ambiente 'PORT' que o Cloud Run fornece (que será 8080).
# Garantimos que ele escute em '0.0.0.0' para que seja acessível
# de fora do contêiner.
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT}

