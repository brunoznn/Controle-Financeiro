import pandas as pd
import streamlit as st
import json

dfp = pd.read_json('adicionar.json')
dfn = pd.read_json('remover.json')

while True:

    with open('adicionar.json', 'r') as saldop:
        saldop = json.load(saldop)


    with open('remover.json', 'r') as saldon:
        saldon = json.load(saldon)

    somap = 0
    soman = 0

    for item in saldon:
        soman += item["quantia"]

    for item in saldop:
        somap += item["quantia"]

    st.subheader(somap - soman)

    st.title('Você deseja adicionar ou remover dinheiro?')

    st.button("Adicionar", type="primary")
    if st.button('Remover'):
        opcao = "r"
    else:
        opcao = "a"

    if opcao == "s" or opcao == "S":
        print("Até mais!")
        break

    elif opcao == "a" or opcao == "A":

        while True:

            quantia = st.number_input('Qual o valor da entrada?')

            try:
                quantia = int(quantia)
                break
            except ValueError:
                print("Por favor, insira somente números inteiros.")

        dici = [
            {
                "quantia": quantia
            }
        ]

        with open('adicionar.json', 'r') as manter:
            historico = json.load(manter)

        adicionar = historico + dici

        with open('adicionar.json', 'w') as storage_json:
            json.dump(adicionar, storage_json, indent=4)

    elif opcao == "r" or opcao == "R":

        while True:
         
            quantia = st.number_input('Qual o valor da saida?')

            try:
                quantia = int(quantia)
                break
            except ValueError:
                print("Por favor, insira somente números inteiros.")

        dici = [
            {
                "quantia": quantia
            }
        ]

        with open('remover.json', 'r') as manter:
            historico = json.load(manter)

        remover = historico + dici

        with open('remover.json', 'w') as storage_json:
            json.dump(remover, storage_json, indent=4)

