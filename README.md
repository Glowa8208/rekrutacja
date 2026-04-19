TEST AUTOMATYCZNY WERYFIKACJI CIASTECZEK COOKIE + ANALITYCZNE NA STORNIE ING.PL

# ZAKRES ZADANIA 
1. WEJSCIE NA STRONE ING.PL (http://www.ing.pl/)
2. KLIKNIECIE PRZYCISKU [DOSTOSUJ] W MENU OPCJI CIASTECZEK
3. ZAZNACZENIE OPCJII [COOKIE ANALITYCZNE]
4. POTWIERDZENIE AKCEPTACJI WYBRANYCH OPCJI ZA POMOCĄ PRZYCISKU [ZAAKCEPTUJ ZAZNACZONE]
5. WERYFIKACJA ZAPISU ZAZNACZONYCH CIASTECZEK W PAMIĘCI PRZEGLĄDARKI

# WYMAGANIA NIEFUNKCJONALNE 
1. zadbaj by rezultat testu był powtarzalny
2. test zaimplementuj w języku python z wykorzystaniem frameworka playwright
3. swoje wyniki opublikuj na github i podejślij do nas jako rozwiązanie zadania rekrutacyjnego
4. kod wyposaż w plik README, w którym opiszesz w jaki sposób możemy uruchomić zrealizowane rozwiązanie
5. uruchom test w kilku przeglądarkach jednocześnie, zaprezentuj kod pipeline'a który przeprowadza taką automatyzację

# WYMAGANIA TECHNICZNE
1. PYTHON 3.13.9 (Anakonda) DLA WERSJI OPROGRAMOWANIA MAC OS SEQOIA 15.1.1
2. PLAYWRIGHT
3. GITHUB
4. POSIADANE PRZEGLĄDARKI (Chrome, Firefox)

# POBRANIE/INSTALACJA TESTU AUTOMATYCZNEGO
1. KLONOWANIE REPOZYTORIUM 
git clone
2. POWOŁANIE ŚRODOWISKA WIRTUALNEGO PYTHON
python -m venv venv
source venv/bin/activate
3. INSTALACJA ZAELŻNOŚCI
pip install -r requirements.txt
4. INSTALACJA PLAYWRIGHT'A
playwright install
5. URUCHOMIENIE TESTU
python test.rekrutacja.py
