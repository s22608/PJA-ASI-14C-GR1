# Polityka Branchowania

W celu zmergowania nowej funkcjonalności tworzymy nowego brancha z `main` np:
* `feature/new-functionality`

Branch powinien mieć unikalną nazwę.

Następnie tworzymy pull requesta z danego brancha i przeprowadzamy code review. Wymagane jest aby conajmniej jedna osoba zaakceptowała zmiany. Następnie pull requesta mergujemy do głównego brancha tzn. `main`.

Link do pobrania condy:
https://conda-forge.org/download/

Tworzenie środowiska:
conda env create -f environment.yml
