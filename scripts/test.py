from library.basic_functions import open_browser_to_link 
import time
def main():
    driver = open_browser_to_link("https://login.raman.devzinier.net")
    time.sleep(20)


main()