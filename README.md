# 📋 ficha-ingreso-clicksecurity

Formulario digital automatizado de ingreso para nuevo personal de seguridad en CLIC Security, con autenticación 2FA mediante OTP y generación de QR para verificación.

---

## 🚀 Descripción del Proyecto

Este proyecto permite registrar digitalmente a nuevos colaboradores de seguridad utilizando una interfaz amigable con [Streamlit](https://streamlit.io/). Incluye:

- Captura de datos personales
- Generación automática de claves OTP tipo Google Authenticator
- Autenticación en dos pasos (2FA)
- Generación de QR para enrolamiento rápido
- Almacenamiento en base de datos local con SQLAlchemy
- Preparado para integraciones futuras (Dashboards, reportes, alertas, etc.)

---

## 🧰 Tecnologías y librerías utilizadas

- `Python 3.10+`
- `Streamlit` - Interfaz web simple y rápida
- `PyOTP` - Generación de claves 2FA (TOTP)
- `qrcode[pil]` - Códigos QR de enrolamiento
- `SQLAlchemy` - ORM para guardar datos
- `pandas` - Manipulación de datos

---

## 🛠️ Instalación y ejecución

1. Clona el repositorio:

```bash
git clone https://github.com/Luk1313/ficha-ingreso-clicksecurity.git
cd ficha-ingreso-clicksecurity
