# MindHive_Assignment

Scraping, storing and processing v2


Part 1: Web Scraping and Database Storage
Url to scrap: https://subway.com.my/find-a-subway
First, filter the search by “kuala lumpur”. Scrape the names, addresses, operating hours, waze link of
outlets from a given webpage that has multiple pages of content. Ensure your script can handle
pagination to navigate through all available pages.
Store the scraped data into a database, designing the schema in a way that you find suitable for this
task.

answer:
The code is in test2.py. This is to scrape the data from [subway outlets](https://subway.com.my/find-a-subway) and i use firebase database to store the scrapped datas.

output:
Name: Subway Menara UOA Bangsar  Jalan Bangsar Utama 1
Address: Unit 1-2-G, Menara UOA Bangsar, Kuala Lumpur, 59000
Operating Hours: Monday - Sunday, 8:00 AM - 8:00 PM
Waze Link: https://www.waze.com/en/live-map/directions/my/federal-territory-of-kuala-lumpur/kuala-lumpur/subway-@-menara-uoa-bangsar?place=ChIJPWFRH5RJzDERvHvlO1uTQpY

Name: Subway Jln Pinang  G9
Address: Wisma UOA II, 19, Jalan Pinang, Kuala Lumpur, 50450
Operating Hours: Monday - Saturday, 8:00 AM – 9:00PMSunday, 11:30 AM – 6:30PM
Waze Link: https://www.waze.com/en/live-map/directions/my/wilayah-persekutuan-kuala-lumpur/kuala-lumpur/subway-@-jalan-pinang-kl?place=ChIJIzvym9Q3zDER9MZj809Opn0
...
...
...

firebase database:
![image](https://github.com/izzatmars/MindHive_Assignment/assets/76147148/31b834b6-6a0a-48f0-be02-ec85370ad2f8)


Part 2: Geocoding
For each outlet, retrieve its geographical coordinates based on the stored address.


answer:
The code is in geocoding.ipynb
It extracts the latitude and logitude of the outlets and store them in the firebase datbase.
![image](https://github.com/izzatmars/MindHive_Assignment/assets/76147148/740e9b1e-6004-48b5-99d3-adb73005fc69)



Part 3: API Development
Develop a backend API (FastAPI, Flask, Django) to serve the outlet data, including their geographical
coordinates.


answer:
The output was on google chrome 
![image](https://github.com/izzatmars/MindHive_Assignment/assets/76147148/c9b1fb52-54ed-4d30-9c41-9fbb9ad0bcd3)

_____________________________________________________________________________________________________________________________________________________________________________________________________________________
I was unable to complete the rest due to time restrictions :( 
_____________________________________________________________________________________________________________________________________________________________________________________________________________________

Part 4: Frontend Development and Visualization
Create a web application that interacts with your API to visualise the outlets on a map.
Implement functionality to display a 5KM radius catchment around each outlet on the map.
Highlight or mark the outlets that intersect with any other outlet’s 5KM radius catchment.


Part 5: Documentation and Instructions
Add a search box to allow the user to enter a query. Examples of query that you would need to handle
include:
1. Which are the outlets that closes the latest
2. How many outlets are located in Bangsar
You are free to use RAG, LLM or NLP to achieve this.


Part 6: Documentation and Instructions
Provide documentation with instructions on how to set up and run your application, and any other
necessary information required to understand and use your solution.
