# MasterProject

All code regarding the Master of Science Thesis Project of Nicolas Weiner at the Amsterdam University of Applied Sciences. 
 

MASTER PROJECT TOPIC: 

                                          Advancing real estate pricing methods
                                      by applying text classification and LIWC analysis 
                                         on Dutch and German real estate listings 
                                                 
Research Question: 
How do informal features and linguistic features deriving from real estate descriptions moderate the relationship of traditional features and price?


Notes: 

As I aim to cross-validate my analysis, I do not only analyse the Dutch market (Funda dataset) but also the German market (Immobilienscout24 dataset). A basic Funda dataset was provided by the CMI of AUAS which was cleaned and enriched with demographic variables. For the German market, however, no dataset was given. I therefore built a webscraper using Beautifulsoup to scrape all recent real estate listings listed for sale on Germany's largest platform Immobilienscout24. Further, as Immobilienscout24 does not indicate the listing nor the selling date of a listing, the webscraper was repeatably run every 4 days for a span of three weeks and it was checked wether a particular listing was still active or not. While this method allows to make estimations about the time needed to sell a listing, it is limited in validity and reliability. Further research is recommended to collect more precise and accurate timeframes for sold listings on the German market. 

Table of Contents:

1. The code for the webscraper can be found in the folder "Step 1 - Scraping Immobilienscout24". The file "TriggerHausScraper.py" triggers the scraper "HausScraper.py". 

2. Folder "Step 2 - Data Extension & Cleaning" includes the code for extending the data with additional economic and demographic variables.

3. Folder "Step 3 - Text Classification & LIWC Analysis" includes the Text Classification & LIWC analysis code.

4. Folder "Step 4 - Correlation & Regression Analysis" includes the Correlation & Regression analysis code. The Notebooks are created in Google Colab which allows to easily open them directly in the browser. No installations needed. They are further working documents and regularily updated until the project is finished.


