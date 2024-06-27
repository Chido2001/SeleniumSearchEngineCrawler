from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=options)

# Get the search query from the user
search_query = input("Enter a search query: ")

# Set the number of results to retrieve per page
results_per_page = 10

# Set the total number of results to retrieve
total_results = 50

# Set the delay between queries (in seconds)
delay_between_queries = 5

# Create a list to store the URLs
urls = []

# Loop through the pages
for page in range(0, total_results, results_per_page):
    # Navigate to the DuckDuckGo search page
    driver.get(f"https://duckduckgo.com/html/?q={search_query}&kl=wt-wt&start={page}")

    # Wait for the search results to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.result__a")))

    # Get the search results
    search_results = driver.find_elements(By.CSS_SELECTOR, "a.result__a")

    # Loop through the search results and extract the URLs
    for result in search_results:
        url = result.get_attribute("href")
        urls.append(url)

    # Add a delay between queries
    time.sleep(delay_between_queries)

# Export the URLs to a text file
with open("search_results.txt", "w") as f:
    for url in urls:
        f.write(url + "\n")

# Close the browser
driver.quit()