from selenium import webdriver # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.common.by import By # type: ignore
import time

driver = webdriver.Chrome()

file = 0
query='laptop'
for i in range(1,20):
    driver.get("https://www.amazon.in/s?k={query}&page={i}&ref=nb_sb_noss")

    elems = driver.find_element(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html","w", encoding="utf-8") as f:
            f.write(d)
            file += 1
        time.sleep(2)

driver.close()