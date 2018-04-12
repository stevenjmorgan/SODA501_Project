# GOP State Party Website Scraper

This script, written in Python 2.7, downloads webpages that hold press/news releases from 28 state parties with BeautifulSoup and Selenium. Releases from some states were collected manually, since there were so few releases (i.e. Indiana GOP has posted 3 press releases). We have eight more states to scrape so stay tuned for updates.

The files are written in UTF-8 encoding to .txt files. It should be noted that running these scripts at different times will produce slightly different data. This occurs because the script specifies pages to scrape from, and which pages press releases are located will change as more press releases are added. Code to write to specific directories (i.e. write files from a state to folder just for that state) is currently commented out.
