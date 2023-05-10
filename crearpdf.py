import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from reportlab.pdfgen import  canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from email import encoders


pdf=SimpleDocTemplate('Reporte_de_seguridad.pdf',pagesize=letter)
datos= [
    ["Nombre de Procesos", "ID","Estado"],
    ["Discord", "3600","Activado" ],
     ["LEDKeeper2", "21520","Activado" ]]
tabla = Table(datos)
estilo = TableStyle([
    ('BACKGROUND', (0,0), (-1, 0), colors.skyblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
])
tabla.setStyle(estilo)

datos2=[['Puertos escaneados','Estado'],
        ['80','abierto'],
        ['100','cerrado']]
tabla2=Table(datos2)
tabla2.setStyle(estilo)


datos3=[['Descargas'],
        ['80'],
        ['100']]
tabla3=Table(datos3)
tabla3.setStyle(estilo)

elementos=[tabla,tabla2,tabla3]
tabla2.spaceBefore=50
tabla2._argW[1] = 200
tabla._argW[1] = 200
tabla3._argW[0] = 200
tabla3.spaceBefore=50
pdf.build(elementos)

origen = ' PIAciber2023@gmail.com '   #agregar correos
destino= 'bsrc_14@hotmail.com'
#hacemos la ppeticion de acceso de conexion a SMTP para poder connectarnos y enviar correos
conn=smtplib.SMTP('smtp.gmail.com', 587)
conn.starttls()
conn.login(origen,'wyazbvbaxxyxjvor')#agregar contra correo
#agregamos los datos de envio
mensaje= MIMEMultipart()
mensaje['From']=origen
mensaje['To']= destino
mensaje['Subject']='Reporte de seguridad'
#adjunte el archivo pdf
nom_pdf= 'Reporte_de_Seguridad.pdf'
adjuntar= open('Reporte_de_Seguridad.pdf','rb')#se abre con el nombre del archivo y con lectura y binario
#esto es para adjuntar el archivo el 1arg indica  que es de una aplicacion 
#y el  2arg indica que  tipo de contenido en este caso  un binario
terpdf= MIMEBase('application','octet-stream')
terpdf.set_payload((adjuntar).read())
encoders.encode_base64(terpdf)
terpdf.add_header('Content-Disposition', 'attachment', filename='Reporte_de_Seguridad.pdf')
mensaje.attach(terpdf)
conn.sendmail(origen,destino,mensaje.as_string())
conn.quit() 