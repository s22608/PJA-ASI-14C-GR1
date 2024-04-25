# Polityka Branchowania

W celu zmergowania nowej funkcjonalności tworzymy nowego brancha z `main` np:
* `feature/new-functionality`

Branch powinien mieć unikalną nazwę.

Następnie tworzymy pull requesta z danego brancha i przeprowadzamy code review. Wymagane jest aby conajmniej jedna osoba zaakceptowała zmiany. Następnie pull requesta mergujemy do głównego brancha tzn. `main`.

# Cel ML
 
Nasz model uczenia maszynowego ma za zadanie przewidywać czy pracownik firmy zostanie na swoim obecnym stanowisku.
 
# Instrukcja instalacji condy
 
1. conda config --add channels conda-forge
2. conda config --set channel_priority strict
3. conda create --name {environment name}
4. conda install --file environment.yml
5. pip freeze

nowe środowisko zrobić, kedro run --starter =spaceflight