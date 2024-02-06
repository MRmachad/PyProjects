import smtplib

class SmtpConnect():

    smtp_serv = 0
    do_email = ""

    def __init__(self, host = "smtp-mail.outlook.com", port = 587, do_email = "machado.leonardo@academico.ifg.edu.br", token_do_email = "senha123"):
        print(host)
        print(port)
        self.do_email = do_email
        self.smtp_serv = smtplib.SMTP(host= host, port= str(port))
        self.smtp_serv.ehlo()
        self.smtp_serv.starttls()
        self.smtp_serv.login(do_email, token_do_email)

    def Envia_email(self, para_email = "leonardo.silva@tsea.com.br", assunto = "Teste", msg_texto = "Oi"):

        msg = """From: %s
        To: %s
        Subject: Mensagem do Leo

        %s.""" % (self.do_email, ', '.join([para_email]),msg_texto)

        self.smtp_serv.sendmail(self.do_email, [para_email], msg)

    def Serv_quit(self):
        self.smtp_serv.quit()