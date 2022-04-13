# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:12:35 2022

@author: ruben
"""
import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(PlastificationTime, MaximumInjection, Cushion, M2, Pos8, Pos4, BlocoHR1, Pos3, TempBico, TZ1, TZ2, TZ3):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[PlastificationTime, MaximumInjection, Cushion, M2, Pos8, Pos4, BlocoHR1, Pos3, TempBico, TZ1, TZ2, TZ3]])
    print(prediction)
    return prediction



def main():
    st.title("Classificador Vipex")
    html_temp = """
    <div style="background-color:orange;padding:7px">
    <h2 style="color:white;text-align:center;">Processo de Injeção Sopro III </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    PlastificationTime=st.text_input("Tempo de Plastificaca","Escreve Aqui")
    MaximumInjection=st.text_input("Máxima Pressao Injecao","Escreve Aqui")
    Cushion=st.text_input("Almofada","Escreve Aqui")
    M2=st.text_input("M2","Escreve Aqui")
    Pos8=st.text_input("Pos8","Escreve Aqui")
    Pos4=st.text_input("Pos4","Escreve Aqui")
    Pos3=st.text_input("Pos3","Escreve Aqui")
    BlocoHR1=st.text_input("BlocoHR1", "Escreve Aqui")
    TempBico=st.text_input("TempBico","Escreve Aqui")
    TZ1=st.text_input("TZ1","Escreve Aqui")
    TZ2=st.text_input("TZ2","Escreve Aqui")
    TZ3=st.text_input("TZ3","Escreve Aqui")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(PlastificationTime, MaximumInjection, Cushion, M2, Pos8, Pos4, BlocoHR1, Pos3, TempBico, TZ1, TZ2, TZ3)
    # st.success('The output is {}'.format(result))
    if result == 0:
        st.success('A peça esta NOK')
    if result == 1:
        st.success('A peça esta quase estragada')
    if result == 2:
        st.success('O processo esta a perder qualidade')
    if result == 3:
        st.success('O processo esta otimo')
    if st.button("Infos"):
        st.text("Versao 16 - Classificador de Injecao de Plasticos")
        st.text("")

if __name__=='__main__':
    main()
    
    
