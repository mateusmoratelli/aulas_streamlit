import streamlit as st

st.set_page_config(page_title="Cadastro", page_icon=":tada:", layout="centered")
st.title("📜Cadastro de Usuário")
st.write("Preencha os campos abaixo para simular um cadastro")

# Formulário de cadastro
with st.form(key='cadastro_form'):
    nome = st.text_input("Nome Completo")
    idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
    email = st.text_input("Email")
    opcao = st.selectbox("Escolha uma opção", ["Opção 1", "Opção 2", "Opção 3"])
    receber_emails = st.checkbox("Desejo receber emails promocionais")
    enviado = st.form_submit_button("Enviar")

if enviado:
    erros = []

    #validações 
    if not nome:
        erros.append("O campo 'Nome Completo' é obrigatório.")
    if idade == 0:
        erros.append("O campo 'Idade' deve ser maior que zero.")
    if "@" not in email or "." not in email:
        erros.append("O campo 'Email' deve ser um email válido.")      

    if erros: 
        for err in erros:
            st.error(err)
    else:
        st.success("Cadastro realizado com sucesso!")
        st.write(f"Nome: {nome}")
        st.write(f"Idade: {idade}")
        st.write(f"Email: {email}")
        st.write(f"Opção escolhida: {opcao}")
        if receber_emails:
            st.write("Você optou por receber emails promocionais.")
        else:
            st.write("Você não optou por receber emails promocionais.")
        st.balloons()  # Animação de balões ao enviar o formulário
