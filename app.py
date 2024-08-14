import streamlit as st
import pandas as pd
import numpy as np

#++++++++++++++++++++++++++++++++++++++++++
# Sidebar
st.sidebar.markdown("# OPLYZER")

#++++++++++++++++++++++++++++++++++++++++++

# Botão para mostrar/esconder o campo de entrada
col1, col2 = st.sidebar.columns([1, 2])

with col1:
    mostrar_campo = st.button("Taxa")

# Estado do campo de entrada
if 'campo_visivel' not in st.session_state:
    st.session_state.campo_visivel = False

# Alternar visibilidade do campo de entrada
if mostrar_campo:
    st.session_state.campo_visivel = not st.session_state.campo_visivel

# Exibir o campo de entrada apenas se o estado estiver visível
if st.session_state.campo_visivel:
    opcao = st.sidebar.number_input("Juros (%)", value=10.40)
else:
    opcao = 10.40  # Valor fixo

# Exibir o texto "Juros: 10.4%" ao lado do botão
with col2:
    st.write(f"**Juros: {opcao}%**")

#++++++++++++++++++++++++++++++++++++++++++

# Colocar Vol Implícita, KA e KD lado a lado
col1, col2, col3 = st.sidebar.columns(3)

# Botão para mostrar/esconder KA e KD
mostrar_campos = st.sidebar.button("Módulo DT")

# Estado dos campos de entrada
if 'campos_visiveis' not in st.session_state:
    st.session_state.campos_visiveis = False

# Alternar visibilidade dos campos KA e KD
if mostrar_campos:
    st.session_state.campos_visiveis = not st.session_state.campos_visiveis

# Vol Implícita sempre visível
with col1:
    vol_impl = st.number_input("Vol Implícita", value=20.0, step=None)

# Exibir KA e KD apenas se o estado estiver visível
if st.session_state.campos_visiveis:
    with col2:
        KA = st.number_input("KA", value=0.0, step=None)
    with col3:
        KD = st.number_input("KD", value=0.0, step=None)
else:
    KA = 0.0
    KD = 0.0

# Exemplo de uso dos valores
st.write(f"Vol Implícita: {vol_impl}% | KA: {KA} | KD: {KD}")

#++++++++++++++++++++++++++++++++++++++++++

# Colocar Ativo e Vencimento lado a lado
col1, col2 = st.sidebar.columns(2)

with col1:
    ativo = st.selectbox(
        "Ativo",
        ("PETR4", "VALE3", "ITUB4", "ABEV3", "WEGE3", "BBAS3", "CMIG4")
    )

with col2:
    vencimento = st.selectbox(
        "Vencimento",
        (
            "2024-08-16", "2024-09-20", "2024-10-18", "2024-11-14", "2024-12-20", 
            "2025-01-17", "2025-02-21", "2025-03-21", "2025-04-17", "2025-05-16", 
            "2025-06-20", "2025-07-18", "2025-08-15", "2025-09-19", "2025-10-17", 
            "2025-11-21", "2025-12-19", "2026-01-16", "2026-02-20", "2026-03-20", 
            "2026-04-17"
        )
    )

#++++++++++++++++++++++++++++++++++++++++++

# Opção de seleção de "Call" e "Put" com checkboxes
col1, col2 = st.sidebar.columns(2)

with col1:
    opcao_call = st.checkbox("Call", value=True)

with col2:
    opcao_put = st.checkbox("Put", value=False)

# Verificar quais opções foram selecionadas
opcoes_selecionadas = []
if opcao_call:
    opcoes_selecionadas.append("Call")
if opcao_put:
    opcoes_selecionadas.append("Put")

# Colocar os botões "Calcular" e "Save as" lado a lado
col1, col2 = st.sidebar.columns(2)

with col1:
    calcular = st.button("Calcular")

with col2:
    save_as = st.button("Save as")

# Exemplo de uso
if calcular:
    st.write("Cálculo realizado.")
if save_as:
    st.write("Arquivo salvo.")
