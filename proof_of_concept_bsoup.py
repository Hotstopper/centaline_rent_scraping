import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.undergraduate.study.cam.ac.uk/courses/search"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
subjects = soup.find_all("span", class_="field-content")
subject_titles = [subject.text.strip() for subject in soup.find_all("span", class_="field-content")]
print(subject_titles)