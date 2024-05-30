# Użyj obrazu bazowego z Pythonem
FROM python:3.8-slim

# Ustaw zmienną środowiskową, aby Python nie buforował wyjść (dla lepszego logowania)
ENV PYTHONUNBUFFERED 1

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj plik requirements.txt i zainstaluj zależności
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install toposort

# Skopiuj cały projekt do katalogu roboczego
COPY . .

# Ustawienie domyślnego polecenia do uruchomienia Kedro
CMD ["kedro", "run"]
