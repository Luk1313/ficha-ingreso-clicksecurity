import streamlit as st
from datetime import date

st.title("Ficha de Ingreso - ClickSecurity")

with st.form("ficha_formulario"):
    st.subheader("Datos Personales")
    nombre = st.text_input("Nombre completo")
    rut = st.text_input("RUT")
    fecha_nacimiento = st.date_input("Fecha de nacimiento")
    direccion = st.text_input("Dirección")
    comuna = st.text_input("Comuna")
    celular = st.text_input("Celular")
    correo = st.text_input("Correo electrónico")

    st.subheader("Datos Laborales")
    cargo = st.text_input("Cargo")
    fecha_ingreso = st.date_input("Fecha de ingreso")
    fonasa_isapre = st.text_input("FONASA / ISAPRE")
    afp = st.text_input("AFP")

    st.subheader("Datos de Ropa")
    talla_polera = st.text_input("Talla Polera")
    talla_pantalon = st.text_input("Talla Pantalón")
    talla_softshell = st.text_input("Talla Softshell")
    numero_calzado = st.text_input("Número de Calzado")

    st.subheader("Datos Bancarios")
    banco = st.text_input("Banco")
    tipo_cuenta = st.selectbox("Tipo de cuenta", ["Cuenta RUT", "Cuenta Vista", "Cuenta Corriente"])
    desea_anticipo = st.radio("¿Desea anticipo?", ["Sí", "No"])

    st.subheader("En caso de emergencia")
    nombre_contacto = st.text_input("Nombre de contacto")
    relacion = st.text_input("Relación")
    telefono_contacto = st.text_input("Teléfono contacto")

    enviado = st.form_submit_button("Enviar")

if enviado:
    st.success("Formulario enviado correctamente. ¡Gracias!")
