#!/usr/bin/env python
# coding: utf-8

import pandas as pd
salesData = pd.read_csv("https://firebasestorage.googleapis.com/v0/b/my-thesis-c5a39.appspot.com/o/Others%2Fvgsales.csv?alt=media&token=a95ac813-e116-4280-8657-cdc1b706d1c9")
print(salesData.head())

salesData.info()

col_dict = {'Name': 'Product', 'Platform': 'Team', 'Genre': 'Product_Category', 'Publisher' : 'Sales_Engineer', 'NA_Sales': 'BKS_Sales',
            'EU_Sales': 'KWG_Sales', 'JP_Sales': 'TNG_Sales', 'Other_Sales': 'BGR_Sales', 'Global_Sales': 'Total_Sales'}
salesData.columns = [col_dict.get(x, x) for x in salesData.columns]
salesData.columns

salesData['Product_Category'].unique()

cat_dict = {'Action': 'Directional_Control_Valves', 'Sports': 'Air_Cylinders', 'Shooter':'Rotary_Actuators', 'Platform':'Electric_Actuators',
            'Misc': 'Vacuum_Equipment', 'Racing': 'Switches/Sensors', 'Role-Playing': 'Fittings/Tubing', 'Fighting': 'FRL', 'Simulation': 'Flow_Control',
            'Puzzle': 'Air_Preparation', 'Adventure': 'Lubrication', 'Strategy':'Accessories'}
salesData['Product_Category'] = [cat_dict.get(x, x) for x in salesData['Product_Category']]
salesData['Product_Category'].unique()

salesData['Team'].unique()

tm_dict = {'Wii': 'TMSales1', 'NES': 'TMSales2', 'GB': 'TMSales3', 'DS': 'TMSales4', 'X360':'TMSales5', 'PS3':'TMSales6', 'PS2':'TMSales7',
           'SNES':'TMSales8', 'GBA':'TMSales9', '3DS': 'TMSales10', 'PS4': 'TMSales11', 'N64':'TMSales12', 'PS':'TMSales13', 'XB':'TMSales14',
           'PC': 'TMSales15', '2600':'TMSales16', 'PSP':'TMSales17', 'XOne':'TMSales18', 'GC':'TMSales19', 'WiiU':'TMSales20', 'GEN':'TMSales21',
           'DC': 'TMSales22', 'PSV':'TMSales23', 'SAT':'TMSales24', 'SAT':'TMSales25', 'SCD':'TMSales26', 'WS':'TMSales27', 'NG':'TMSales27',
           'TG16':'TMSales28', '3DO':'TMSales29', 'GG':'TMSales30', 'PCFX':'TMSales31'}

salesData['Team'] = [tm_dict.get(x, x) for x in salesData['Team']]
salesData['Team'].unique()

se_dict = {'Nintendo':'Bayu', 'Electronic Arts':'Amir', 'Activision': 'Febby', 'Sony Computer Entertainment': 'Ferdi', 'Ubisoft':'Andrias', 'Take-Two Interactive': 'Faisal', 'THQ':'Yogi', 'Microsoft Game Studio':'Agus', 'Atari':'Kriston', 'Sega':'Amin', 'Namco Bandai Games':'Yaqub', 'Konami Digital Entertainment': 'Rizal'}

salesData['Sales_Engineer'] = [se_dict.get(x, x) for x in salesData['Sales_Engineer']]
salesData['Sales_Engineer'].unique()

salesData.head()

salesData.to_csv("salesSMC.csv", index=False)

