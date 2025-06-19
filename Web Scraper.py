from bs4 import BeautifulSoup
import requests
import csv

# Input link: https://quotes.toscrape.com/
page_to_scrape = requests.get(input())
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# Highlight text/objects on page > right click > inspect > look for tag.
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

writer.writerow(["Quotes", "Authors"])

for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])
file.close()