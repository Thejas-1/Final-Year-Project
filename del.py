import requests
from bs4 import BeautifulSoup
import json
import csv
from pprint import pprint
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#<a class="LinkOff"


#Soup = BeautifulSoup(open("page.html"), "html.parser")
#print Soup

url = "http://www.howstat.com/cricket/Statistics/Matches/MatchScorecard_ODI.asp?MatchCode=3878"
Scorecard = requests.get(url).text
Soup = BeautifulSoup(Scorecard, "html.parser")

match_name = Soup.find('a',class_="LinkBlack2").get_text()
match_name=match_name.strip()
#print("Match Name :" + match_name)


match_date = Soup.find('td',class_="TextBlack8").get_text()
match_date=match_date.strip()
#print("Match Date :" + match_date)
x=Soup.find('a',class_="LinkOff").find_all_next("td")

j=1
#for i in x:
	#print(i.get_text().strip()) #To CSV file

productDivs = Soup.findAll('a', attrs={'class' : 'LinkOff'})
for div in productDivs:
	if "PlayerOverview" in str(div):
		print(div.get_text().strip())


#print_string = ""


'''
name=[]
run=[]
ball=[]
four=[]
six=[]
sr=[]
count_name=22
count_run=24
count_ball=25
count_four=26
count_six=27
count_sr=28


#x=u' '.encode('utf-8').strip()

unicode.join(u'\n',map(unicode,x))
#print(type(x))
#print(x)


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
	if(j==count_name):
		if(len(name)>=11):
			continue
		name.append(y)
		count_name+=8
	if(j==count_run):
		if(len(run)>=11):
			continue
		run.append(y)
		count_run+=8
	if(j==count_ball):
		if(len(ball)>=11):
			continue
		ball.append(y)
		count_ball+=8
	if(j==count_four):
		if(len(four)>=11):
			continue
		four.append(y)
		count_four+=8
	if(j==count_six):
		if(len(six)>=11):
			continue
		six.append(y)
		count_six+=8
	if(j==count_sr):
		if(len(sr)>=11):
			continue
		sr.append(y)
		count_sr+=8
	j=j+1
	if(j>500):
		break
		
#print(toss)
#print_string = "Match Name :" + match_name + "\nMatch Date :" + match_date + print_string + "\nVenue :" + match_venue + "\nToss :"+toss + "\nResult :" + match_result + "\nMan of the match :" + match_man
#print(print_string)

#print(sr)


#R BF 4s 6s SR % of Total


i=0
with open('example2.csv', 'w') as csvfile:
    fieldnames = ["player_name", "runs_scored", "balls_faced", "fours", "sixes", "strike_rate"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    while i<11:
    	writer.writerow({'player_name': name[i], 'runs_scored': run[i], 'balls_faced': ball[i], 'fours': four[i], 'sixes': six[i], 'strike_rate': sr[i]})
    	i=i+1
'''


