# Polityka Branchowania

W celu zmergowania nowej funkcjonalności tworzymy nowego brancha z `main` np:
* `feature/new-functionality`

Branch powinien mieć unikalną nazwę.

Następnie tworzymy pull requesta z danego brancha i przeprowadzamy code review. Wymagane jest aby conajmniej jedna osoba zaakceptowała zmiany. Następnie pull requesta mergujemy do głównego brancha tzn. `main`.

# Cel ML
 
Nasz model uczenia maszynowego ma za zadanie przewidywać czy pracownik firmy zostanie na swoim obecnym stanowisku.
 
# Instrukcja stawiania środowiska
## Conda
1. pip3 install conda
2. conda config --add channels conda-forge
3. conda config --set channel_priority strict
4. conda create --name {environment name}
5. conda install --file environment.yml
6. pip freeze

## Kedro
1. pip install -r requirements.txt
2. kedro new --name=spaceflights
3. kedro run --from-inputs aug_train
4. kedro viz

# Uruchomienie Kedro w Dockerze na Windows

## 1. Zainstaluj Docker Desktop

1. Pobierz Docker Desktop z oficjalnej strony [Docker](https://www.docker.com/products/docker-desktop).
2. Zainstaluj Docker Desktop, postępując zgodnie z instrukcjami instalatora.
3. Po zakończeniu instalacji uruchom Docker Desktop i upewnij się, że działa poprawnie.
4. docker build -t docker-kedro-project .
5. docker run --rm -it -v %cd%:/app docker-kedro-project
6. EXPOSE 8888 5000
7. docker run --rm -it -v %cd%:/app -e MY_ENV_VAR=value docker-kedro-project

