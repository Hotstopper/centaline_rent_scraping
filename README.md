# centaline_rent_scraping
I scraped rent prices for around 9000 past transactions on Centaline from May 2024 to August 2024 using Selenium.

## proof_of_concept_bsoup.py
In which I scraped a static site with Beautiful Soup. Largely irrelevant to the project except as a "proof of concept".

## webscraping.py
As Centaline is a dynamic site, static scrapings such as Beautiful Soup don't work.
I used Selenium to scrape the site and to press buttons to load more data. I identified relevant elements by their CSS selectors and XPATHs.
Finally, I exported the data into a csv file (results.csv), there is also an excel version (rent results.xlsx)
