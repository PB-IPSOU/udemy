"""Cribleur S&P500 et prédiction boursière.

Usage:
======
    python nom_de_ce_super_script.py argument1 argument2

    argument1: un entier signifiant un truc
    argument2: une chaîne de caractères décrivant un bidule
"""

__authors__ = ("Patrick BOUTARD", "Analyse de valeurs boursières")
__contact__ = ("patrick.boutard@outlook.fr", "boutard@eu")
__copyright__ = "PBO"
__date__ = "2023-06-01"
__version__ = "1.0.0"

import streamlit as st
import pandas as pd
from pandas_datareader import data as pdr
import plotly.express as px
import numpy as np
from PIL import Image

PATH_MEDIA = "initial_version/project/"
PATH_DATA = "initial_version/project/"
DESCRIPTIF_SCREENER = """
    Dans le tableau ci-dessous, vous trouverez la plupart des entreprises du S&P500 (indice boursier des 500 plus grandes entreprises américaines) avec certains critères tels que :

        - Le nom de l'entreprise : The name of the company
        - Le secteur d'activité : The sector of activity
        - La capitalisation : Market capitalization
        - Les dividendes : Dividend payout percentage (dividend/stock price)
        - Profits de l'entreprise : The company's profit margin in percentage
        ⚠️ Ces données sont extraites en temps réel de l’API Yahoo Finance. ⚠️

        i️ Vous pouvez filtrer / rechercher une entreprise avec les filtres sur la gauche. i️
    """

def display_media(type, path, codec, caption):
    image = Image.open(path)
    #st.image(image, caption=caption, width=180)
    st.image(image, caption=caption)

def display_expander(label, texte):
    with st.expander(label=label, expanded=False) :
        st.write(texte)

def display_data(type, path):
    df = pd.read_csv(path)
    df.columns = ['Symbole', 'Nom', 'Secteur', 'Capitalisation', 'Dividendes',  'Profits']
    st.write("Nombre d'actions : ", len(df))
    st.dataframe(df.iloc[:, 1:])   #// iloc(toutes les lignes, toutes les colonnes à partir de la 2 ème)

if __name__ == "__main__":

    st.set_page_config(
        page_title="PBO-BOURSE",
        page_icon="📈",
        initial_sidebar_state="expanded",
        layout="centered"
    )
  
    #sidebar
    st.sidebar.title("Critères de recherche :")
    
   
    st.title("Cribleur S&P500 et prédiction boursière")

    _,col2,_ = st.columns([1,3,1])
    with col2 :
        display_media("image", PATH_MEDIA+"stock.jpeg", "jpeg", "@austindistel")
    
    st.header("Partie 1 - Screener S&P 500")
    display_expander("Partie 1 - Screener S&P 500", DESCRIPTIF_SCREENER)
    display_data("csv", PATH_DATA+"s&p500.csv" )