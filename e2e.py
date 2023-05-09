from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_scores_service(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode, no visible browser window
    service = Service('path_to_chromedriver')  # Replace with the path to your chromedriver executable
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)

    score_element = driver.find_element(By.CSS_SELECTOR, "selector_for_score_element")
    score_text = score_element.text

    try:
        score = int(score_text)
        if 1 <= score <= 1000:
            return True
        else:
            return False
    except ValueError:
        return False

    driver.quit()

def main_function():
    url = input("Enter the URL: ")

    if test_scores_service(url):
        print("Tests passed!")
        return 0
    else:
        print("Tests failed!")
        return -1

if __name__ == "__main__":
    exit_code = main_function()
    exit(exit_code)