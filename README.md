# CloudflareScraper

## Overview
This script scrapes the Cloudflare scheduled changes page at https://developers.cloudflare.com/waf/change-log/scheduled-changes/ and outputs the table of changes posted as valid json in an external file

## Instructions
Either copy or fork this repo and set up this script on your local. Install the python BeautifulSoup module for web scraping (pip install bs4). Be sure to insert your own file path for the json data to output to towards the bottom of the script. If you want to set this script to automatically run and not have your output file contain past changes from an earlier scrape, you might want to add a starter script that removes the output file and then creates it again as I am using append to write each json event to the output file.

## Dependencies 
BeautifulSoup Python Module

## Possible Use-Cases
Ingesting output of scraped data into a log monitoring tool (i.e. Splunk)
Set up custom alerting when new changes are posted on the Cloudflare site without having to check

### Creator
William White
