import requests
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import re
from babel.numbers import parse_decimal
import string 
import locale
locale.setlocale(locale.LC_ALL, 'C')
import csv
import spacy
nlp = spacy.load('en_core_web_sm')
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from bs4 import BeautifulSoup as bs
from csv import DictWriter
import template_retrieval



st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
def main():
    menu =["Template Selection","Tree Surgery","Interior Design"]
    with st.sidebar:
      #  url_search = st.text_input("//TODO Database URL")
        st.subheader("Main Menu")
        choice = st.selectbox("Menu List",menu)
        choice_value = choice
        st.subheader("Set Budget")
        budget = st.number_input("Enter Budget",key="budget")
      
        st.subheader("Set Max CPC")
        max_cpc = st.number_input("Enter Max Cpc",key = "cpc")
        st.write("currently not functional.")

        st.subheader("Input Generic Final URL")
        max_cpc = st.number_input("Enter Final URL for Ads",key = "final_url")
        st.write("currently not functional.")

       
    st.header("Ad editor template application 1.0")

    st.write("The current proof of concept demonstrator can be used select csv templates to import into google ads editor" )
    st.write("Use the side bar on the left to select: the desired template" )

    st.title("Template")  

    if choice == choice_value:
        st.subheader(choice_value)
        csv_name = choice_value.lower()+".csv"
        csv_name.replace(" ", "_")
        csv_df = pd.read_csv(csv_name)
        st.dataframe(csv_df)
        csv_df_ad_editor_csv = template_retrieval.convert_df(csv_df)
        st.download_button("Press to Download",csv_df_ad_editor_csv, csv_name+"_template.csv","text/csv",key='download-csv')







    
   # if choice == "Interior Design":
   #     st.subheader("Interior Design")
   #     interior_design_df = pd.read_csv('interior_design_test.csv')
   #     st.dataframe(interior_design_df)
   #     interior_design_ad_editor_csv = template_retrieval.convert_df(interior_design_df)
   #     st.download_button("Press to Download",interior_design_ad_editor_csv,"interior_design_template.csv","text/csv",key='download-csv')

   # elif choice == "Tree Surgery/Arborist":
   #     st.subheader("Tree Surgery/Arborist")
   #     tree_surgery_df = pd.read_csv('tree_surgery_test.csv')
   #     st.dataframe(tree_surgery_df)
    #    tree_suregery_ad_editor_csv = template_retrieval.convert_df(tree_surgery_df)
   #     st.download_button("Press to Download",funeral_ad_editor_csv,"tree_surgery_template.csv","text/csv",key='download-csv')

#-------------------------------------------------------------------------------------------------
  
  
if __name__ == "__main__":
    main()



