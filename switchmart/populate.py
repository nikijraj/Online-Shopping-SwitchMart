import csv 
from switchmart.models import Browse #Change App Name

with open('/home/nikijraj/Documents/updated_products.csv', encoding='utf-8') as csvfile:   
    reader=csv.DictReader(csvfile)
    pkey=0
    for row in reader:
            p = Browse(prod_name=row['Product Name'],category=row['Category'],price=row['Price'],details=row['Details'],pk=pkey)
            pkey+=1
            p.save()

