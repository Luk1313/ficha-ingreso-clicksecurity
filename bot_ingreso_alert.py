# bot_ingreso_alert.py
import smtplib
import sqlite3
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- Configuración de correo ---
EMAIL_FROM = "tu_correo@gmail.com"
EMAIL_TO = "seguridad@clicksecurity.cl"
EMAIL_SUBJECT = "[Alerta] Nuevo ingreso o modificación de ficha"
EMAIL_PASS = "tu_clave_o_token"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# --- Base de datos ---
DB_PATH = "ficha_ingreso.db"

# --- Revisión cada 60 segundos ---
INTERVALO = 60

# --- Función para enviar correo ---
def enviar_alerta(nombre, accion):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = EMAIL_SUBJECT

    cuerpo = f"""
    Estimado equipo,

    Se ha detectado una acción en la base de datos de fichas:

    - Nombre: {nombre}
    - Acción detectada: {accion}

    Por favor revisar la ficha correspondiente.
    
    Saludos,
    Bot de Fichas Automatizado
    """
    msg.attach(MIMEText(cuerpo, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASS)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        server.quit()
        print(f"[OK] Alerta enviada: {nombre} - {accion}")
    except Exception as e:
        print(f"[Error] No se pudo enviar alerta: {e}")

# --- Bot principal ---
def monitorear_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS log_ingresos (nombre TEXT, timestamp TEXT)")

    fichas_vistas = set()

    while True:
        cursor.execute("SELECT nombre, fecha_ingreso FROM personal")
        registros = cursor.fetchall()

        for nombre, fecha in registros:
            id_ficha = f"{nombre}-{fecha}"
            if id_ficha not in fichas_vistas:
                enviar_alerta(nombre, "Nuevo ingreso o modificación")
                fichas_vistas.add(id_ficha)

        time.sleep(INTERVALO)

if __name__ == "__main__":
    print("[Bot Iniciado] Monitoreando cambios en fichas...")
    monitorear_db()
