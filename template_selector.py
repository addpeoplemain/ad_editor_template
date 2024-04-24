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



def budget_click_button():
    st.session_state.clicked = True

def url_click_button():
    st.session_state.clicked = True


st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
def main():
    final_url= "temporary url"
    budget = 0
    menu =["Tree Surgery","Interior Design"]
    with st.sidebar:
        st.subheader("Main Menu")
        choice = st.selectbox("Menu List",menu)
        choice_value = choice
        st.subheader("Set Budget")
        budget_input = st.number_input("Enter Budget",key="budget")
        st.subheader("Input Generic Final URL")
        final_url_input= st.text_input("Enter Final URL for Ads",key = "final_url")
       
        if st.button('Update Values'):
            budget = budget_input
            final_url = final_url_input
          
    st.header("Ad editor template application 1.0")

    st.write("The current proof of concept demonstrator can be used select csv templates to import into google ads editor" )
    st.write("Use the side bar on the left to select: the desired template" )

    if choice == choice_value:
        st.title(choice_value +" Template")
        csv_name = choice_value.lower()+"_template.csv"
        csv_name= "_".join( csv_name.split())
        csv_df = pd.read_csv(csv_name)
        st.dataframe(csv_df)
        csv_df_ad_editor_csv = template_retrieval.convert_df(csv_df)
        st.download_button("Press to Download",csv_df_ad_editor_csv, csv_name,"text/csv",key='download-csv')

    st.title("Edited Template")
    edit_csv_df = csv_df.copy()
    edit_csv_df.at[0, 'Budget'] = budget
    edit_csv_df.loc[edit_csv_df['Ad type'] == 'Responsive search ad', 'Final URL'] = "--"
    edit_csv_df.loc[edit_csv_df['Ad type'] == 'Responsive search ad', 'Final URL'] = final_url

    edit_csv_df_ad_editor_csv = template_retrieval.convert_df(edit_csv_df)
    st.dataframe(edit_csv_df)
    st.download_button("Press to Download",edit_csv_df_ad_editor_csv, "edited_"+csv_name,"text/csv",key='download-edited_csv')
  
if __name__ == "__main__":
    main()



 #st.subheader("Set Max CPC")
     #   max_cpc_input = st.number_input("Enter Max Cpc",key = "cpc")
     #   if st.button('Set Max CPC'):
      #      max_cpc = max_cpc_input

      #  st.subheader("Input Generic Final URL")
      #  final_url_input= st.number_input("Enter Final URL for Ads",key = "final_url")
      #  if st.button('Set Final URL'):
      #      final_url = final_url_input