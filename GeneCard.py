
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service



#Build Diver: String in Service has to pint to local installation of GeckoDriver
#Webdriver has to be adjusted to used browser
def build_driver():
    #Run w/o open Browser
    options = Options()
    options.headless = True

    #Path to Geckodriver executable
    ser = Service('/Users/Lukas/Documents/geckodriver.exe') 
    # create webdriver object
    driver = webdriver.Firefox(options=options, service=ser)

    return driver



def find_gene(Gene_Name, driver):
    """
    @param Gene_Name: Official Gene Symbol of a Gene (e.g. APP)
    @param driver: selenium webdriver object
    """
    URL = f"https://www.genecards.org/cgi-bin/carddisp.pl?gene={Gene_Name}&keywords={Gene_Name}"
    driver.get(URL)
    print(URL)
    return driver



def get_data(driver):
    """
    Retrieve summary of gene defined in the function: find_gene.
    @param driver: driver object returned my find_gene()
    """
    try:
        summary = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/main/div[2]/div/div/section[2]/div[1]/ul").text
        print(summary)
    except:
        print("Gene does not exist")



