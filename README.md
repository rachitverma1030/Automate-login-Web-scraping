# Concept

In this project,
first, we run the code through Visual Studio Code (IDE).

First Chrome get open:
When we run the code, the chrome will open automatically with the help of selenium as its 
module is install in VS code to create an environment between VS code and chrome.

Twitter login window:
When chrome get open, after that twitter login website will get open and total 10 seconds will 
be required for automatic login process for twitter account.

Twitter account page:
Now we will be login to twitter account page of the user for 1min 40 sec.

Start of scraping:
After the automate login process, the twitter account page will close automatically after 100 
seconds or we can close it manually. Within that fixed time, data get scraped that we want to 
scrap. To scrap or extract data from twitter one the module is used in the source code that is 
“snscrape.module”. During scraping large amount of data are present but we need specific and 
structured data, so another module is used that is “pandas”.

Storing of Scraped data:
Whatever the data we want extract from twitter, we need to pass command in code and run the 
code and after the whole process the CSV file will be created at the terminal side and scraped 
data will be displayed on it.
