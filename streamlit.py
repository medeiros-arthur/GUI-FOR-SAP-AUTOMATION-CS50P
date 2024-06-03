import streamlit as st
import pandas as pd
import numpy as np
import glob
import sapCred
import plotly.express as px

exportPath = sapCred.exportPath

st.set_page_config(
    page_title="REQUISIÇÃO DE COMPRAS - SPOT",
    page_icon="✅",
    layout="wide",  # Use "wide" layout for a wider container
)

# LAYOUT
header = st.container()
dataframe_container_ce34 = st.container(border=True)
col1, col2 = st.columns(2)
dataframe_container_ce37 = st.container(border=True)
col3, col4 = st.columns(2)



def main():
    
    # Specify the path to the CSV files
    
    path = exportPath + '/CE34'  # Update this to your CSV files' directory

    # Use glob to get all the CSV files in the specified path
    all_files = glob.glob(path + "/*.csv")

    # Create an empty list to store individual DataFrames
    dfs = []

    # Loop through all the files and read them into a DataFrame
    for filename in all_files:
        df = pd.read_csv(filename, encoding= 'ISO-8859-1', on_bad_lines= 'skip', header= 4, sep='\t')
        dfs.append(df)

    # Concatenate all DataFrames into one
    merged_df34 = pd.concat(dfs, ignore_index=True)

        # Print the merged DataFrame
    df34 = merged_df34.copy()

    df34 = df34.rename(columns = {
            ' DIA' : 'DATE', 
            'Nº ORDEM' : 'ORDER', 
            'DESCRIÇÃO DO MATERIAL' : 'PRODUCT',
            'Unnamed: 11' : 'EXPECTED PRODUCTION',
            'Unnamed: 17' : 'GROSS PRODUCTION',
            'Unnamed: 21' : 'REAL DAILY PRODUCTION',
            'Unnamed: 24' : 'DAILY SCRAP',
            'Unnamed: 26' : 'DAILY PRODUCTIVITY %',
            'Unnamed: 29' : 'DAILY SCRAP %'
    })  

    df34 = df34.dropna(subset=['PRODUCT'], how='any')
    df34 = df34[df34['DATE'] != ' DIA']
    df34 = df34.dropna(axis = 1, how = 'all')
    df34 = df34.reset_index(drop = True)
    df34 = df34.drop(columns=['Unnamed: 32', 'Unnamed: 34', 'POR PROD.', 'Unnamed: 41'])
    df34['DATE'] = pd.to_datetime(df34['DATE'], format= r"%d.%m.%Y")
    df34['DATE'] = df34['DATE'].dt.date
    df34 = df34.sort_values('DATE')
    df34['REAL DAILY PRODUCTION'] = df34['REAL DAILY PRODUCTION'].str.strip().str.replace('.','').str.replace(',','')
    df34['REAL DAILY PRODUCTION'] = df34['REAL DAILY PRODUCTION'].astype(int)
    df34['REAL DAILY PRODUCTION'] = df34['REAL DAILY PRODUCTION']/100
    df34['DAILY SCRAP %'] = df34['DAILY SCRAP %'].str.strip().str.replace(',','.').astype(float)
    df34din = df34.groupby(by = 'PRODUCT').agg(CE34_PRODUCTION = ('REAL DAILY PRODUCTION','sum')).copy()
    df34din['CE34_PRODUCTION'] = df34din['CE34_PRODUCTION'].apply(lambda x: '{:,}'.format(x).replace(',', '.'))

    df34prod = df34.groupby(by = 'DATE').agg(DAILY_PRODUCTION = ('REAL DAILY PRODUCTION', 'sum')).copy()

    def format_value_production(value):
        return f"{value/1000:.0f}k"

    df34prod['formated'] = df34prod['DAILY_PRODUCTION'].apply(format_value_production)

    df34scrap = df34.groupby(by = 'DATE').agg(DAILY_SCRAP = ('DAILY SCRAP %', 'mean')).copy()

    def format_value_scrap(value):
        return f"{value:.1f}"
    
    df34scrap['formated'] = df34scrap['DAILY_SCRAP'].apply(format_value_scrap)

    df34stype = df34.copy()
    df34stype['DAILY SCRAP'] = df34stype['DAILY SCRAP'].str.strip().str.replace('.00','').str.replace('.','').str.replace(',','').astype(int)
    df34stype = df34stype.groupby(by = 'PRODUCT').agg(SCRAP_TYPE = ('DAILY SCRAP', 'sum'))




    # Specify the path to the CSV files
    
    path = exportPath + '/CE37'  # Update this to your CSV files' directory

    # Use glob to get all the CSV files in the specified path
    all_files = glob.glob(path + "/*.csv")

    # Create an empty list to store individual DataFrames
    dfs = []

    # Loop through all the files and read them into a DataFrame
    for filename in all_files:
        df = pd.read_csv(filename, encoding= 'ISO-8859-1', on_bad_lines= 'skip', header= 4, sep='\t')
        dfs.append(df)

    # Concatenate all DataFrames into one
    merged_df37 = pd.concat(dfs, ignore_index=True)

    df37 = merged_df37.copy()

    df37 = df37.rename(columns = {
            ' DIA' : 'DATE', 
            'Nº ORDEM' : 'ORDER', 
            'DESCRIÇÃO DO MATERIAL' : 'PRODUCT',
            'Unnamed: 11' : 'EXPECTED PRODUCTION',
            'Unnamed: 17' : 'GROSS PRODUCTION',
            'Unnamed: 21' : 'REAL DAILY PRODUCTION',
            'Unnamed: 24' : 'DAILY SCRAP',
            'Unnamed: 26' : 'DAILY PRODUCTIVITY %',
            'Unnamed: 29' : 'DAILY SCRAP %'
    })  

    df37['REAL DAILY PRODUCTION'] = df37['REAL DAILY PRODUCTION'].str.strip().str.replace(',00','').str.replace('.','').astype(float)
    df37['DAILY SCRAP'] = df37['DAILY SCRAP'].str.strip().str.replace(',00','').str.replace('.','').astype(float)
    df37['DAILY SCRAP %'] = df37['DAILY SCRAP %'].str.strip().str.replace(',','.').astype(float)

    df37 = df37.dropna(subset=['PRODUCT'], how='any')
    df37 = df37[df37['DATE'] != ' DIA']
    df37 = df37.dropna(axis = 1, how = 'all')
    df37 = df37.reset_index(drop = True)
    df37 = df37.drop(columns=['Unnamed: 32', 'Unnamed: 34', 'POR PROD.', 'Unnamed: 41'])
    df37['DATE'] = pd.to_datetime(df37['DATE'], format= r"%d.%m.%Y")
    df37['DATE'] = df37['DATE'].dt.date
    df37 = df37.sort_values('DATE')

    df37din = df37.groupby(by = 'PRODUCT').agg(CE37_PRODUCTION = ('REAL DAILY PRODUCTION','sum')).copy()
    df37din['CE37_PRODUCTION'] = df37din['CE37_PRODUCTION'].apply(lambda x: '{:,}'.format(x).replace(',', '.'))


    df37prod = df37.groupby(by = 'DATE').agg(DAILY_PRODUCTION = ('REAL DAILY PRODUCTION', 'sum')).copy()

    df37prod['formated'] = df37prod['DAILY_PRODUCTION'].apply(format_value_production)

    df37scrap = df37.groupby(by = 'DATE').agg(DAILY_SCRAP = ('DAILY SCRAP %', 'mean')).copy()

    df37scrap['formated'] = df37scrap['DAILY_SCRAP'].apply(format_value_scrap)

    df37stype = df37.copy()
    # df37stype['DAILY SCRAP'] = df37stype['DAILY SCRAP'].str.strip().str.replace('.00','').str.replace('.','').str.replace(',','').astype(int)
    df37stype = df37stype.groupby(by = 'PRODUCT').agg(SCRAP_TYPE = ('DAILY SCRAP', 'sum'))


    



    with header:
        # Title and description
        st.title('PRODUCTION DASHBORAD ✅')
        st.write('This is an example of a simple Streamlit dashboard from an automated report extracted from SAP GUI developed with python.')

    with dataframe_container_ce34:
        with st.expander('CE34 PRODUCTION DATA'):
            st.dataframe(df34, hide_index= True)

        

    with col1:
        st.markdown(':blue[**SUM OF COST CENTER CE34 PRODUCTION**]')
        st.dataframe(df34din, hide_index= False, height=300)


        fig1 = px.line(df34scrap, 
            #x='DATE', 
            y='DAILY_SCRAP', 
            # color='STATUS', 
 
            # labels= {'MONTH_YEAR':'MÊS A MÊS','STATUS2':'CONTAGEM DE RCs'},
            # hover_data='STATUS',
            text='formated',
            markers=True,

        
            
        )
        fig1.update_layout(title='SCRAP BY DATE') 
        fig1.update_traces(textposition='bottom center')
        st.plotly_chart(fig1, theme="streamlit",use_container_width=True)

     
    with col2: 
        fig2 = px.line(df34prod, 
            #x='DATE', 
            y='DAILY_PRODUCTION', 
            # color='STATUS', 
 
            # labels= {'MONTH_YEAR':'MÊS A MÊS','STATUS2':'CONTAGEM DE RCs'},
            # hover_data='STATUS',
            text='formated',
            markers=True,
            
        )
        fig2.update_layout(title='PRODUCTION BY DATE')  
        fig2.update_traces(textposition='bottom center')
        st.plotly_chart(fig2, theme="streamlit",use_container_width=True)


        fig3 = px.pie(df34stype, 
            names=df34stype.index, 
            values='SCRAP_TYPE', 
            # color='STATUS', 
 
            # labels= {'MONTH_YEAR':'MÊS A MÊS','STATUS2':'CONTAGEM DE RCs'},
            # hover_data='STATUS',
            # names='PRODUCT',
            #markers=True,
            
        )

        fig3.update_layout(title='SCRAP BY PRODUCT')  
        st.plotly_chart(fig3, theme="streamlit",use_container_width=True) 

        

    with dataframe_container_ce37:
        with st.expander('CE37 PRODUCTION DATA'):
            st.dataframe(df37, hide_index= True)


    with col3:
        st.markdown(':blue[**SUM OF COST CENTER CE37 PRODUCTION**]')
        st.dataframe(df37din, hide_index= False, height=300)


        fig4 = px.line(df37scrap, 
            #x='DATE', 
            y='DAILY_SCRAP', 
            # color='STATUS', 
 
            # labels= {'MONTH_YEAR':'MÊS A MÊS','STATUS2':'CONTAGEM DE RCs'},
            # hover_data='STATUS',
            text='formated',
            markers=True,

        
            
        )
        fig4.update_layout(title='SCRAP BY DATE') 
        fig4.update_traces(textposition='bottom center')
        st.plotly_chart(fig4, theme="streamlit",use_container_width=True)

    with col4:
        fig5 = px.line(df37prod, 
            #x='DATE', 
            y='DAILY_PRODUCTION', 
            # color='STATUS', 
 
            # labels= {'MONTH_YEAR':'MÊS A MÊS','STATUS2':'CONTAGEM DE RCs'},
            # hover_data='STATUS',
            text='formated',
            markers=True,
            
        )
        fig5.update_layout(title='PRODUCTION BY DATE')  
        fig5.update_traces(textposition='bottom center')
        st.plotly_chart(fig5, theme="streamlit",use_container_width=True)

        fig6 = px.pie(df37stype, 
            names=df37stype.index, 
            values='SCRAP_TYPE', 
            # color='STATUS', 
 
            # labels= {'MONTH_YEAR':'MÊS A MÊS','STATUS2':'CONTAGEM DE RCs'},
            # hover_data='STATUS',
            # names='PRODUCT',
            #markers=True,
            
        )

        fig6.update_layout(title='SCRAP BY PRODUCT')  
        st.plotly_chart(fig6, theme="streamlit",use_container_width=True) 


        



main()
