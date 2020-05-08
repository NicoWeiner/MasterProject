# MasterProject

All code regarding the Master of Science Thesis Project of Nicolas Weiner at the Amsterdam University of Applied Sciences. 
 

MASTER PROJECT TOPIC: 

                                           The Role of Text in Real Estate:

                                                Applying multi-level 
                                         Natural Language Processing (NLP) 
                                            on real estate descriptions 
                                                 to predict prices
                                                 
Research Question: 
To what extend can linguistics in real estate descriptions predict real estate price? 



Notes: 

1. As I aim to cross-validate my analysis, I do not only analyse the Dutch market (Funda dataset) but also the German market (Immobilienscout24 dataset). A basic Funda dataset was provided by the CMI of AUAS which was cleaned and enriched with demographic variables. For the German market, however, no dataset was given. I therefore built a webscraper using Beautifulsoup to scrape all recent real estate listings listed for sale on Germany's largest platform Immobilienscout24. Further, as Immobilienscout24 does not indicate the listing nor the selling date of a listing, the webscraper was repeatably run every 4 days for a span of three weeks and it was checked wether a particular listing was still active or not. While this method allows to make estimations about the time needed to sell a listing, it is limited in validity and reliability. Further research is recommended to collect more precise and accurate timeframes for sold listings on the German market. 

1.1. The code for the webscraper can be found in the folder "Scraping Immobilienscout24". The file "TriggerHausScraper.py" triggers the scraper "HausScraper.py". 

2. The file "Immobilienscout24 Data Preparation Notebook.ipynb" shows all code used to compile, clean and prepare the German housing data. 

3. The notebook containing all code used for the analysis of the German housing data "Immobilienscout24_Analysis_Notebook v2.ipynb" is too large to view within Github, so please open the html file instead. Alternatively, download the files and open them locally on your laptop. 

4. The notebook "Funda_Analysis_Notebook v2.ipynb" contains all code used to analyse the Dutch housing market. 


