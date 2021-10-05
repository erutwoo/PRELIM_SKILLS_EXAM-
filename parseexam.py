import xml.etree.cElementTree as et
import pandas as pd
tree = et.parse("try.xml")
root = tree.getroot()
date_rep = []
country = []
cases = []
deaths = []

for d in root.iter('dateRep'):
    date_rep.append(d.text)

for count in root.iter('countriesAndTerritories'):
    country.append(count.text)

for case in root.iter('cases'):
    cases.append(case.text)
    
for death in root.iter('deaths'):
    deaths.append(death.text)

df = pd.DataFrame(columns= [date_rep,country,cases,deaths])

df.to_csv('exam.csv')