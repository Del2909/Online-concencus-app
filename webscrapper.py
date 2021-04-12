
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import boto3
import json
import sd_algorithm

subject = "Bananas"
#keyword = "forecast"
unincluded_sites = ["facebook", "instagram", "youtube","twitter","linkedin"]
relevant_data = ""

for link in search(subject, tld="co.in", num=2, stop=2, pause=3):
	print("Now looking at : " + link)
	if any(x in link for x in unincluded_sites):
		print("Skipping.....")
		continue
	else:
		sd = sd_algorithm.SDAlgorithm()
		sd.url = link
		sd.analyze_page()
		print("The function works: ")
		print(sd.totalarticle)
		print("Looking inside the link " + link + " gives us : \n")
		relevant_data= sd.totalarticle

    
print("############################################################################################################# \n")
print(relevant_data[:4000])
comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
print('Calling DetectSentiment')
print(json.dumps(comprehend.detect_sentiment(Text=relevant_data[:4000], LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectSentiment\n')

