# TEST AUTOMATYCZNY COOKIES
from playwright.sync_api import sync_playwright, expect
import time
ING_URL = "http://www.ing.pl/"

def test_cookie(przegladarka):
    with sync_playwright() as p:
        # URUCHOMIENIE PRZEGLĄDARKI
        if przegladarka == 'firefox':
            browser = p.firefox.launch(headless=False)
        elif przegladarka == 'chromium':
            browser = p.chromium.launch(headless=False)
        else:
            print(f'Nieznana przeglądarka: {przegladarka}')
            return False
        
        print(f'Uruchamianie testów na przeglądarce: {przegladarka}')
        context = browser.new_context()
        page = context.new_page()

        # 1. WEJŚCIE NA STRONE ING 
        page.goto("http://www.ing.pl/")
        time.sleep(1)  #oczekiwanie na zaladowanie storny

        # 2. KLIKAM PRZYCISK [DOSTOSUJ]
        page.get_by_role("button", name="Dostosuj").click()
        time.sleep(1)

        # 3. ZAZNACZENIE OPCJI COOKIE ANALITYCZNE
        page.get_by_role("switch", name="Cookies analityczne").locator("span").first.click() 
        time.sleep(1)

        #4. KLIKAM ZAAKCEPTUJ ZAZNACZONE
        page.get_by_role("button", name="Zaakceptuj zaznaczone").click()
        time.sleep(1)

        #5 WERYFIKACJA CZY CIASTECZKA ZOSTAŁY ZAPISANE
        page.get_by_role("link", name="Wholesale Banking").click() 
        
        # WEJŚCIE NA PODSTRONE I WERYFIKACJA ZAPISU CIASTECZEK
        cookies = context.cookies() #weryfikacja w pamiecie przegladarki
            
        # CISTECZKO Z POLITYKĄ
        policy_cookie = None
        for cookie in cookies:
            if 'name' in cookie and cookie["name"] == "cookiePolicyGDPR":
                policy_cookie = cookie
                break
        
        # SPRAWDZENIE CISTECZKA Z POLITYKĄ PLIKÓW COOKIES
        if policy_cookie is None:
            print("Brak ciateczka z polityką cookiePolicyGDPR!")
            browser.close()
            return False
        
        print(f"Znaleziono cookiePolicyGDPR z wartoscia: {policy_cookie.get('value') or 'BEZ WARTOŚCI'}")
        
        #WERYFIKACJA POPRAWNOŚI [1 zgoda na analityczne]
        if 'value' not in policy_cookie or policy_cookie["value"]!= "3":
            print(f"Nieporawna wartosc ciasteczka. Oczekiwane 1, otrzymano {policy_cookie.get('value') or 'BEZ WARTOŚCI'}")
            browser.close()
            return False
        
        # SZUKANIE ANALITYCZNYCH CIASTECZEK
        analytics_cookies = []
        for cookie in cookies:
            if 'name' in cookie and (cookie["name"].startswith("_ga") or cookie["name"].startswith("AMCV") or cookie["name"] =="s_cc"):
                analytics_cookies.append(cookie)

        print("Testy pozytywne - ciasteczka poprawne!")
        browser.close()
        return True
    return False

# URUCHOM TEST
if __name__=="__main__":
    przegladarki = ['chromium', 'firefox']

    for przegladarka in przegladarki:
        wynik = test_cookie(przegladarka)
        if wynik:
            print(f"{przegladarka}: OK")
        else:
            print(f"{przegladarka}: FAIL")
            exit(1)
