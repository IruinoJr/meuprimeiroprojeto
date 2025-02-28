import streamlit as st
import pandas as pd
import datetime
from datetime import date 

def gravar_dados(nome, data_nasc, tipo):
    if nome and data_nasc <= date.today():        
        with open(file="clientes.csv", mode="a", encoding="utf-8") as file:
            file.write (f"{nome},{data_nasc},{tipo}\n")
        st.session_state['sucesso'] = True    
    else:
        st.session_state['sucesso'] = False

st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon="📒"
)

st.title("Cadastro de clientes")
st.divider()

nome = st.text_input("Digite o nome do cliente", key="nome_cliente")

data_nasc = st.date_input("Data de nascimento", key="data_nasc", format="DD/MM/YYYY", min_value=datetime.date(1932, 1, 1))

tipo = st.selectbox("Tipo do cliente", ["Pessoa Jurídica", "Pessoa Física"])

btn_cadastrar = st.button("Cadastrar", on_click=gravar_dados, args=[nome, data_nasc, tipo])

if btn_cadastrar:
    if (st.session_state["sucesso"]):
        st.success("Cliente cadastrado com sucesso!",
                   icon="👌")
    else:
        st.error("Houve algum problema no cadastro!",
                   icon="🚨")    
