# 📁 Proyecto: ficha-personal-2FA
# Automatización de fichas de ingreso con control de acceso 2FA

# ------------------------
# 🔹 REQUERIMIENTOS:
# pip install streamlit pyotp qrcode[pil] sqlalchemy pandas
# ------------------------

import streamlit as st
import pyotp
import qrcode
import io
import pandas as pd
from sqlalchemy import create_engine

# ------------------------
# CONFIGURACIÓN BÁSICA
# ------------------------
st.set_page_config(page_title="Ficha de Ingreso con 2FA", layout="centered")
st.title("📋 Ficha de Ingreso de Personal con 2FA")

# ------------------------
# FORMULARIO DE INGRESO
# ------------------------
with st.form("ficha_form"):
    nombre = st.text_input("Nombre Completo")
    rut = st.text_input("RUT")
    correo = st.text_input("Correo Electrónico")
    telefono = st.text_input("Teléfono")
    cargo = st.selectbox("Cargo", ["Guardia", "Supervisor", "Analista", "Otro"])
    submit = st.form_submit_button("Registrar")

# ------------------------
# FUNCIONES AUXILIARES
# ------------------------
def generar_2fa_qr(usuario: str):
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    uri = totp.provisioning_uri(name=usuario, issuer_name="ClickSecurity")
    qr_img = qrcode.make(uri)
    buffer = io.BytesIO()
    qr_img.save(buffer, format="PNG")
    return buffer.getvalue(), secret

# ------------------------
# PROCESO DE REGISTRO + 2FA
# ------------------------
if submit and nombre and correo:
    qr_img_bytes, secret = generar_2fa_qr(correo)

    st.success("✅ Registro exitoso. Escanea este QR con tu app 2FA (Google Authenticator, Authy...)")
    st.image(qr_img_bytes, caption="Código QR de 2FA", use_column_width=False)

    # Guardar en base de datos temporal (puede conectarse a MySQL, PostgreSQL, etc.)
    data = pd.DataFrame([{"Nombre": nombre, "RUT": rut, "Correo": correo, "Tel": telefono, "Cargo": cargo, "Secret2FA": secret}])
    engine = create_engine("sqlite:///ficha_personal.db")
    data.to_sql("personal", engine, if_exists="append", index=False)

    st.info("🔐 Se ha generado un token secreto para 2FA. Esto permite control de acceso seguro.")

# ------------------------
# NOTA FINAL
# ------------------------
st.markdown("""
---
✅ Este sistema permite registrar personal y asociarles un token 2FA de manera automatizada para reforzar la seguridad de acceso.
Puedes integrarlo con validaciones de ingreso y control de personal en sistemas mayores.
""")

