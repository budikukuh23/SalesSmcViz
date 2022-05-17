import streamlit as st
import pandas as pd
from visualization import *
import plotly.graph_objs as go

def readData():
    Video_Games = pd.read_csv('salesSMC.csv')
    Video_Games['Year'] = Video_Games['Year'].fillna(0).astype('int')
    return Video_Games



df = readData()


sidebar = st.sidebar

sidebar.title('User Options')


def introduction():
        st.image('wisma47.jpg', width=None)
        st.markdown("""
        ## EDA and Viz. of SMC Product Sales data\n

|             |     |                                 |
| ----------- | :-: | :------------------------------ |
| Nama        | :   | Muhhamad Kukuh Budi Martono     |
| Pekerjaan   | :   | Engineer                        |
| Email       | :   | engineer.jbk1@smcindonesia.com  |
| Perusahaan  | :   | PT. SINAR MUTIARA CAKRABUANA    |
| Alamat      | :   | Gedung Wisma 47 Jakarta Pusat   |
        \nThis Project is to perform the analysis on the SMC Product Sales data.
        Here I used manipulated video game sales data and used various libraries of Python
        for visualization of Data. The Dataset which is Used in Project is
        from [Kaggle](https://www.kaggle.com/datasets/gregorut/videogamesales).       
        \nThe Libraries I used in Project are: [Matplotlib](https://matplotlib.org/), 
        [Seaborn](https://seaborn.pydata.org/), [Plotly](https://plotly.com/python/), 
        [Pandas](https://pandas.pydata.org/), dan [Streamlit](https://streamlit.io/)
        """)

def execute():
    
    st.image('SMC-Selection.png')
    st.markdown("""# Let's Begin Analysis""")
    st.dataframe(df)

    st.markdown("""
       - ##### 500 product are ranked based on their sales in billions
       - ##### Product sold between 1980 to 2020""")


    # sales in numbers

    st.markdown("## Sales in Various Regions")
    start, end = st.slider("Double Ended Slider",value=[2005,2008], min_value=1980, max_value=2020)
    selRegion = st.selectbox("Select Region", ['BKS_Sales', 'KWG_Sales', 'TNG_Sales','BGR_Sales','Total_Sales'])
    year_count = (i for i in range(start,end))
    count_in_range = df.loc[df['Year'].isin(year_count)] 
    ns = sum(count_in_range[selRegion])
    st.header(round(ns))

    st.markdown(""" 
    - With the Help of Above Slider (in years):
            - As seen in the above Slider, you can select any range Start and End.
            - Then Select any Region, and it Shows the Total No. of sales(in billions)""")

    # Product Category in various area

    st.markdown("## Top Product Category in Various Regions")
    prodregion = st.selectbox("Select Regions", ['BKS_Sales', 'KWG_Sales', 'TNG_Sales','BGR_Sales','Total_Sales'])
    data = df.groupby('Product_Category', as_index=False).sum().sort_values(prodregion, ascending=False)
    #st.dataframe(data)
    fig = plotBar(data, 'Product_Category', prodregion)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(""" 
    - With the Help of Above Selectbox Area(in sales):
            - As seen in the above Dropdown selectbox, you can select any Region.
            - Then it shows the Top Product Category from that Selected Region.
            - it Seems Action Genre is most Popular in Most Regions""")

    # Top 10 Sales Engineers in various regions

    st.markdown("## Top 10 Sales Engineers in Various Regions")
    salregion = st.selectbox("Select any Regions", ['BKS_Sales', 'KWG_Sales', 'TNG_Sales','BGR_Sales','Total_Sales'])
    data2 = df.groupby('Sales_Engineer', as_index=False).sum().sort_values(salregion, ascending=False).head(10)
    
    fig = plotBar(data2,'Sales_Engineer', salregion)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(""" 
    - With the Help of Above Selectbox Region(in sales):
            - As seen in the above Dropdown selectbox, you can select any Region.
            - Then it shows the Top Sales Engineers from that Selected Region.""")
    
    # No. of Product Sold per year

    st.markdown('## No. of Product Sold per Year')
    data3 = df[df['Year'] != 0].groupby('Year', as_index=False).count()
    #st.dataframe(data)
    fig = plotLine(data3, 'Year', 'Product')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    - Observations Based on above linear Graph 
            - As seen in the graph above product sales peaked in 2005-2010 across the globe.
            - With the Highest of 1428 millions Product were sold.""")


    # Most popular Product Category
    st.markdown('## Most Popular Product Category Globally')
    data4 = df.groupby('Product_Category', as_index=False).count()
    fig= px.pie(data4, labels='Product_Category', values='Rank', names='Product_Category')

    data5 = df[df['Year']!=0].groupby('Year', as_index=False).sum()
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    - Observations Based on above Pie Chart 
            - As seen in the graph above, Directional Control Valves Category is the Highest across the globe.
            - so this Data Shows Customer need more Directional Control Valves Category related to any other.""")

    
    
    # Various Sales in years according to their Regions
    
    st.markdown('## Sales in Various Regions')
    data6 = df[df['Year'] != 0].groupby('Year', as_index=False).count()
    px.line(data6, 'Year', 'Product')

    fig = go.Figure()
    fig.add_trace(go.Line(x = data5.Year, y = data5.BKS_Sales, name="Bekasi Sales"))
    fig.add_trace(go.Line(x = data5.Year, y = data5.KWG_Sales, name="Karawang Sales"))
    fig.add_trace(go.Line(x = data5.Year, y = data5.TNG_Sales, name="Tangerang Sales"))
    fig.add_trace(go.Line(x = data5.Year, y = data5.BGR_Sales, name="Bogor Sales"))
    fig.add_trace(go.Line(x = data5.Year, y = data5.Total_Sales, name="Total Sales"))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    - Observations Based on above linear Graph 
            - As seen in the graph above SMC Product sales from 1980-2020 across the Indonesia.
            - as you can see in 2008 it was the Highest of all time sales with 678.9 million.""")



options = ['Project Introduction', 'Execution']

selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    execute()