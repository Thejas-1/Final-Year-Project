import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

Soup = BeautifulSoup(open("page.html"), "html.parser")
#print Soup

#url = "http://www.howstat.com/cricket/Statistics/Matches/MatchScorecard_ODI.asp?MatchCode=3878"
#Scorecard = requests.get(url).text
#Soup = BeautifulSoup(Scorecard, "html.parser")

match_name = Soup.find('a',class_="LinkBlack2").get_text()
match_name=match_name.strip()
#print("Match Name :" + match_name)


match_date = Soup.find('td',class_="TextBlack8").get_text()
match_date=match_date.strip()
#print("Match Date :" + match_date)
x=Soup.find('td',class_="TextBlack8").find_all_next("td")

j=1
#for i in x:
	#print(i.get_text().strip()) #To CSV file

print_string = ""

for i in x:
	#print(str(j) + " " + str(i.get_text().strip()))
	y = i.get_text().strip()
	if(j==3):
		match_venue=y
	if(j==8):
		toss=y
	if(j==10):
		match_result=y
	if(j==12):
		match_man=y #Man of the match!
	j=j+1
	if(j>25):
		break
		
#print(toss)
print_string = "Match Name :" + match_name + "\nMatch Date :" + match_date + print_string + "\nVenue :" + match_venue + "\nToss :"+toss + "\nResult :" + match_result + "\nMan of the match :" + match_man
print(print_string)


#R BF 4s 6s SR % of Total
