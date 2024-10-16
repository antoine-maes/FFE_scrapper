from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def check_competition(url):
    # Configurer le WebDriver (assurez-vous d'avoir le bon driver pour votre navigateur)
    driver = webdriver.Chrome()

    try:
        # Naviguer vers l'URL de la page web cible
        driver.get(url)
        
        # Trouver l'élément de recherche
        search = driver.find_element(By.CSS_SELECTOR, "#main > div.flex-grow-1")
        
        # Recuperer le nombre d'enfants directs de l'élément de recherche
        direct_children = search.find_elements(By.CSS_SELECTOR, ":scope > *")

        driver.quit()

        if len(direct_children) > 3:
           print("L'inscription est ouverte!")
           return True
        else:
            print("L'inscription n'est pas encore ouverte.")
            return False
        
    except Exception as e:
        print(f"Erreur lors de la recherche de l'élément: {e}")
        driver.quit()
        return False
        


