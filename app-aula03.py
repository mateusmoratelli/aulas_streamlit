import streamlit as st
from datetime import date

st.set_page_config(page_title="Aula 03 - Widgets",
                   page_icon=":tada:",
                   layout="wide")
st.title("🚀Aula 03 - Widgets")

# MENU LATERAL - SIDER BAR
st.sidebar.title("Menu")
nome = st.sidebar.text_input("Digite seu nome")
idade = st.sidebar.number_input("Digite sua idade", min_value=0, max_value=120, step=1)
hobbies = st.sidebar.multiselect("Selecione seus hobbies", 
                                 ["Leitura", "Esportes", "Jogos", "Música", "Códigos"])
data_inicio = st.sidebar.date_input("Data de início", value=date.today())
plano = st.sidebar.selectbox("Escolha um plano", ["", "Básico", "Intermediário", "Avançado"])
bt_mostrar = st.sidebar.button("📄 Mostrar Resumo")

# CORPO DA PÁGINA - MAIN
st.header("Preencha o formulário no menu lateral e clique em 'Mostrar Resumo'")


if bt_mostrar:
    erros = []

    if not nome:
        erros.append("❌O campo 'Nome' é obrigatório.")
    if idade == 0:
        erros.append("❌O campo 'Idade' deve ser maior que zero.")
    if not plano:
        erros.append("❌Você deve selecionar um plano.")
    
    if erros:
        st.error("Por favor, corrija os seguintes erros:")
        for erro in erros:
            st.write(erro)
    else:
        data_inicio_formatado = data_inicio.strftime("%d/%m/%Y") 
        
        st.success("✅ Todas as informações foram preenchidas corretamente!")
        st.info(f"Nome: **{nome}** 🎉 Você está pronto para começar!, te esperamos dia **{data_inicio_formatado}**")
        
        st.subheader("Resumo das Informações")
        st.write(f"**Nome:** {nome}")
        st.write(f"**Idade:** {idade} anos")
        st.write(f"**Hobbies:** {', '.join(hobbies) if hobbies else 'Nenhum selecionado'}")
        st.write(f"**Data de Início:** {data_inicio.strftime('%d/%m/%Y')}")
        st.write(f"**Plano Escolhido:** {plano if plano else 'Nenhum plano selecionado'}")
        print(f"Botão 'Mostrar Resumo' foi clicado. - {nome}, {idade}, {hobbies}, {data_inicio}, {plano}")
        st.balloons()