from bs4 import BeautifulSoup
import requests
from datetime import datetime
import csv

url = "https://www.boursorama.com/cours/1rPNOKIA/"

def object_soup(url):
	#get an url and transform into an object soup
	#returns an object soup
	response = requests.get(url)
	document = response.text
	return BeautifulSoup(document, "html.parser")


#get text from object soup
values = object_soup(url).find("div", class_="c-faceplate__values").text

def current_date():
	#current date in day-month-year format hour-minute-second
	#returns an date
	return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def closing_time():
	#nokia stock market closing time
	#returns an boolean
	return "18:30:00" in current_date()


def write_csv(file):
	while not closing_time:
		data = [[values[0:6],values[12:20],current_date()]]
		write_file = csv.writer(file)
		write_file.writerows(data)


with open("nokia_stock_market.csv", "w+") as file:
	write_csv(file)

