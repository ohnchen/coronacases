import requests
from bs4 import BeautifulSoup
import re 


url = "https://www.worldometers.info/coronavirus/country/germany/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

approximate_search = soup.findAll(class_="maincounter-number")
exact_search = re.findall(r">(.*?)<", str(approximate_search))
pattern = "\d"

num = re.findall(pattern, str(exact_search))
print("There have been {} Coronacases in Germany.".format("".join(num[0:6])))
