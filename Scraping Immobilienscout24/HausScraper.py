import beautifulsoupHelper
import time
import datetime
import pandas as pd
from time import sleep
import random



notAvailable = ""

scoutid_arr = []
typ_arr = []
item_id_arr = []
kaufpreis_arr = []
provision_arr = []
energieeffizienzklasse_arr = []
objektzustand_arr = []
anzahl_zimmer_arr = []
flaeche_arr = []
grundstueck_arr = []
baujahr_arr = []
bezugsfrei_ab_arr = []
title_arr = []
beschreibung_arr = []
ausstattung_arr = []
lagebeschreibung_arr = []
sonstiges_arr = []
plz_arr = []
stadt_arr = []
ortsteil_arr = []
date_arr = []

## drive through all result pages
def scrapeResultPage(url_base_result_page):
    ## get base result page as BS object
    try: 
        base_result_page_soup = beautifulsoupHelper.configBS(url_base_result_page)

        ## get number of sub pages
        num_pages = beautifulsoupHelper.getNumOfPages(base_result_page_soup)
        print("Anzahl an Ergebnisseiten: " + str(num_pages) + "\n------------------------------------\n")

        ## go through all result pages
        for subPage in range(1, num_pages):
        # for subPage in range(1, 3):
            print(str(subPage) + ". Ergebnisseite scrapen...")
            print("https://www.immobilienscout24.de/Suche/de/haus-kaufen?pagenumber=" + str(subPage))
            ## get each result page as BS object
            result_page_soup = beautifulsoupHelper.configBS(
                "https://www.immobilienscout24.de/Suche/de/haus-kaufen?pagenumber=" + str(subPage))

            ## get list of all items of the result page (ads)
            ulResultList = result_page_soup.find(id="resultListItems")

            ## find all items of result list excluding th hidden duplicates
            ads = ulResultList.find_all(
                lambda tag: tag.name == 'li' and tag.get('class') == ['result-list__listing'] and tag.get('class') != [
                    'result-list__listing--hidden'])

            ## loop through all items of a resultPage and call method to scrape each items detail website
            for index, item in enumerate(ads):

                # if index > 0:
                #     sleep(random.randint(2, 10))  # prevent getting blocked from the google API
                
                print(str(index + 1) + ". Item-Seite scrapen...")
                scrapeSubPage(item)

    except: 
        pass

## drive into the detail page
def scrapeSubPage(item):
    ## get item ID
    try: 
        item_id = item['data-id']
        url_detail_page = "https://www.immobilienscout24.de/expose/" + str(item_id)

        ## init BS
        item_soup = beautifulsoupHelper.configBS(url_detail_page)

        ##get html parent
        item_html = list(item_soup.children)[2]
        ##print(item_html)

        ## drive into body
        body = list(item_html.children)[3]
        ##print(body)


        if item_soup.find("div", {"class": "is24-scoutid__content"}):
            scoutid = item_soup.find(class_="is24-scoutid__content").get_text().strip()
        else:
            scoutid = notAvailable

        if item_soup.find("dd", {"class": "is24qa-typ"}):
            typ = item_soup.find(class_="is24qa-typ").get_text().strip()
        else:
            typ = notAvailable    

        if item_soup.find("div", {"class": "is24qa-kaufpreis"}):
            kaufpreis = item_soup.find(class_="is24qa-kaufpreis").get_text().strip()
        else:
            kaufpreis = notAvailable

        if item_soup.find("dd", {"class": "is24qa-provision"}):
            provision = item_soup.find(class_="is24qa-provision").get_text().strip()
        else:
            provision = notAvailable

        if item_soup.find("dd", {"class": "is24qa-energieeffizienzklasse"}):
            energieeffizienzklasse = item_soup.find(class_="is24qa-energieeffizienzklasse").get_text().strip()
        else:
            energieeffizienzklasse = notAvailable

        if item_soup.find("dd", {"class": "is24qa-objektzustand"}):
            objektzustand = item_soup.find(class_="is24qa-objektzustand").get_text().strip()
        else:
            objektzustand = notAvailable

        if item_soup.find("dd", {"class": "is24qa-zimmer"}):
            anzahl_zimmer = item_soup.find(class_="is24qa-zimmer").get_text().strip()
        else:
            anzahl_zimmer = notAvailable

        if item_soup.find("dd", {"class": "is24qa-wohnflaeche-ca"}):
            flaeche = item_soup.find(class_="is24qa-wohnflaeche-ca").get_text().split()[0].strip()
        else:
            flaeche = notAvailable

        if item_soup.find("dd", {"class": "is24qa-grundstueck-ca"}):
            grundstueck = item_soup.find(class_="is24qa-grundstueck-ca").get_text().split()[0].strip()
        else:
            grundstueck = notAvailable

        if item_soup.find("dd", {"class": "is24qa-baujahr"}):
            baujahr = item_soup.find(class_="is24qa-baujahr").get_text().strip()
        else:
            baujahr = notAvailable

        if item_soup.find("dd", {"class": "is24qa-bezugsfrei-ab"}):
            bezugsfrei_ab = item_soup.find(class_="is24qa-bezugsfrei-ab").get_text().strip()
        else:
            bezugsfrei_ab = notAvailable

        if item_soup.find("h1", {"class": "font-semibold font-xl margin-bottom margin-top-m palm-font-l font-line-s"}):
            title = item_soup.find(class_="font-semibold font-xl margin-bottom margin-top-m palm-font-l font-line-s").get_text().strip()
        else:
            title = notAvailable

        if item_soup.find("pre", {"class": "is24qa-objektbeschreibung"}):
            beschreibung = item_soup.find(class_="is24qa-objektbeschreibung").get_text().strip()
        else:
            beschreibung = notAvailable

        if item_soup.find("pre", {"class": "is24qa-ausstattung"}):
            ausstattung = item_soup.find(class_="is24qa-ausstattung").get_text().strip()
        else:
            ausstattung = notAvailable

        if item_soup.find("pre", {"class": "is24qa-lage"}):
            lagebeschreibung = item_soup.find(class_="is24qa-lage").get_text().strip()
        else:
            lagebeschreibung = notAvailable  

        if item_soup.find("pre", {"class": "is24qa-sonstiges"}):
            sonstiges = item_soup.find(class_="is24qa-sonstiges").get_text().strip()
        else:
            sonstiges = notAvailable       


        if item_soup.find("span", {"class": "zip-region-and-country"}):
            plz = item_soup.find(class_="zip-region-and-country").get_text().split()[0].strip()
            stadt = item_soup.find(class_="zip-region-and-country").get_text().split()[1].split(",")[0].strip()
            try:
                ortsteil = item_soup.find(class_="zip-region-and-country").get_text().split(",")[1].split(" (")[0].strip()
            except IndexError:
                ortsteil = notAvailable

        else:
            plz = notAvailable
            stadt = notAvailable
            ortsteil = notAvailable


        date = datetime.datetime.now().strftime("%Y-%m-%d")

        # fill global vars

        global item_id_arr
        item_id_arr.append(item_id)
        global scoutid_arr
        scoutid_arr.append(scoutid)
        global typ_arr
        typ_arr.append(typ)
        global kaufpreis_arr
        kaufpreis_arr.append(kaufpreis)
        global provision_arr
        provision_arr.append(provision)
        global energieeffizienzklasse_arr
        energieeffizienzklasse_arr.append(energieeffizienzklasse)
        global objektzustand_arr
        objektzustand_arr.append(objektzustand)
        global anzahl_zimmer_arr
        anzahl_zimmer_arr.append(anzahl_zimmer)
        global flaeche_arr
        flaeche_arr.append(flaeche)
        global grundstueck_arr
        grundstueck_arr.append(grundstueck)
        global baujahr_arr
        baujahr_arr.append(baujahr)
        global bezugsfrei_ab_arr
        bezugsfrei_ab_arr.append(bezugsfrei_ab)
        global title_arr
        title_arr.append(title)
        global beschreibung_arr
        beschreibung_arr.append(beschreibung)
        global ausstattung_arr
        ausstattung_arr.append(ausstattung)
        global lagebeschreibung_arr
        lagebeschreibung_arr.append(lagebeschreibung)
        global sonstiges_arr
        sonstiges_arr.append(sonstiges)
        global plz_arr
        plz_arr.append(plz)
        global stadt_arr
        stadt_arr.append(stadt)
        global ortsteil_arr
        ortsteil_arr.append(ortsteil)
        global date_arr
        date_arr.append(date)

    except: 
        pass

# use pandas to create dataFrame and export it to xlsx
def generateDataFrame(filename):
    apartments = pd.DataFrame({
          "ID": item_id_arr
        , "ScoutID": scoutid_arr
        , "Typ": typ_arr
        , "Kaufpreis": kaufpreis_arr
        , "Provision": provision_arr
        , "Energieeffizienzklasse": energieeffizienzklasse_arr
        , "Objektzustand": objektzustand_arr
        , "Anzahl_zimmer": anzahl_zimmer_arr
        , "Wohnflaeche (in m²)": flaeche_arr
        , "Grundstueck (in m²)": grundstueck_arr
        , "Baujahr": baujahr_arr
        , "Bezugsfrei_ab": bezugsfrei_ab_arr
        , "Title": title_arr
        , "Beschreibung": beschreibung_arr
        , "Ausstattung": ausstattung_arr
        , "Lagebeschreibung": lagebeschreibung_arr
        , "Sonstiges": sonstiges_arr
        , "PLZ": plz_arr
        , "Stadt": stadt_arr
        , "Ortsteil": ortsteil_arr
        , "ScrapingDate": date_arr
    })

    # apartments["warmmiete"] = apartments['kaltmiete (in €)'].str.replace(".", "").str.replace(",", ".").astype(float) + apartments['nebenkosten (in €)'].str.replace(".", "").str.replace(",", ".").astype(float)

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    file = str(st) + '_' + filename + '.csv'
    apartments.to_csv(file, encoding='utf-8', sep=";", index=False)




    # ts = time.time()
    # st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H-%M-%S')
    # file = str(st) + ' ' + filename + '.csv'

    # file = str(st) + ' ' + filename + '.xlsx'
    # engine = 'xlsxwriter'

    # writer = pd.ExcelWriter(file, engine=engine)

    # # Convert the dataframe to an XlsxWriter Excel object.
    # apartments.to_excel(writer, sheet_name=filename)

    # # Close the Pandas Excel writer and output the Excel file.
    # writer.save()
