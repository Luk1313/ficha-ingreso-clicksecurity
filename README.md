# 📋 ficha-ingreso-clicksecurity

Formulario digital automatizado para el ingreso de nuevo personal de seguridad en **CLIC Security**, con autenticación 2FA mediante OTP, generación de códigos QR y envío de notificaciones automáticas para validación.

---

## 🚀 Descripción del Proyecto

Este proyecto permite registrar digitalmente a nuevos colaboradores de seguridad a través de una interfaz interactiva basada en **Streamlit**.

### 🔐 Funcionalidades:
- Captura y registro de datos personales
- Generación automática de claves OTP (Google Authenticator)
- Autenticación en dos pasos (2FA)
- Generación de códigos QR para enrolamiento seguro
- Notificación por correo cuando un nuevo ingreso es detectado
- Verificación en base de datos (registro nuevo o modificado)

---

## 🧰 Requisitos del Sistema

- Python 3.10 o superior
- Navegador web (para interfaz Streamlit)

---

## 📦 Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/Luk1313/ficha-ingreso-clicksecurity.git
cd ficha-ingreso-clicksecurity


python -m venv venv
source venv/bin/activate  # en Linux/macOS
venv\Scripts\activate     # en Windows


pip install -r requirements.txt


