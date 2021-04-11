import csv 
from switchmart.models import Browse #Change App Name

with open('/home/nikijraj/Documents/all_products.csv', encoding='utf-8') as csvfile:   
    reader=csv.DictReader(csvfile)
    for row in reader:
            p = Browse(prod_name=row['Product Name'],category=row['Category'],price=row['Price'],details=row['Details'])
            p.save()

