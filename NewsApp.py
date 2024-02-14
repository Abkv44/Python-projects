# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:00:50 2024

@author: Abk
"""

import requests
import json
 
print("News App")

def sports_news(query = "sports"):
    url = f"https://newsapi.org/v2/everything?q={query}&from=2023-12-30&sortBy=publishedAt&apiKey=c62b2fba1fc34f4691eaf89159c6514a"
    r = requests.get(url)
    news = json.loads(r.text)

    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print("--------------------------")
            
        
def politics_news(query = "politics"):
    url = f"https://newsapi.org/v2/everything?q={query}&from=2023-12-30&sortBy=publishedAt&apiKey=c62b2fba1fc34f4691eaf89159c6514a"
    r = requests.get(url)
    news = json.loads(r.text)

    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print("--------------------------")
        
        
def tech_news(query = "technology"):
    url = f"https://newsapi.org/v2/everything?q={query}&from=2023-12-30&sortBy=publishedAt&apiKey=c62b2fba1fc34f4691eaf89159c6514a"
    r = requests.get(url)
    news = json.loads(r.text)

    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print("--------------------------")

def city_news(query = "dewas, india"):
    url = f"https://newsapi.org/v2/everything?q={query}&from=2023-12-30&sortBy=publishedAt&apiKey=c62b2fba1fc34f4691eaf89159c6514a"
    r = requests.get(url)
    news = json.loads(r.text)

    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print("--------------------------")
        
print("type\n1 for sports\n2 for politics\n3 for city news\n4 for tech news\n")

user_input = int(input("Enter: "))

if user_input == 1:
    sports_news()
elif user_input == 2:
    politics_news()
elif user_input == 3:
    city_news()
elif user_input == 4:
    tech_news()
elif user_input == 5:
    sports_news()
    politics_news()
    city_news()
    tech_news()
else:
    print("Something went wrong!")
    
    
    
    
