
import pandas as pd
import numpy as np


#python -m spacy download en_core_web_sm

#python -m textblob.download_corpora If required
#def retrieve_csv_dict():
  #  dog_trainer_df = pd.read_csv("Daniel Garrigan Dog Training test.csv")
  #  gearbox_df = pd.read_csv("Halifax Gearbox N Clutch Center Lt test.csv")
  #  hair_salon_df = pd.read_csv("Hiikuss Ltd Ta Hiikus Hair Salon test.csv")
 #   tattoo_df = pd.read_csv("Inkredible Tattoo test.csv")
  #  funeral_df = pd.read_csv("Hillier Funeral Care test.csv")

  #  csv_dict = {
  #      'dog_trainer':dog_trainer_df,
   #     'gearbox':gearbox_df,
   #     'hair_salon':hair_salon_df,
   #     'tattoo_parlour':tattoo_df,
   #     'funeral':funeral_df

   # }
  #  return csv_dict

def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

