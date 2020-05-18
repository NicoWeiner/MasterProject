import HausScraper as HS

# import wohnungsGesuche as wG

# global variables
immo = "ImmoScout24"

# base urls ImmobilienScout24 for offers
url_haus_kaufen = "https://www.immobilienscout24.de/Suche/de/haus-kaufen"

# Scrape ImmobilienScout24 for offers
HS.scrapeResultPage(url_haus_kaufen)
HS.generateDataFrame(immo)

