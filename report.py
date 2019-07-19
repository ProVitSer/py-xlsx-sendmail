# -*- coding: utf-8
import mysql.connector 
import smtplib 
from email.MIMEMultipart import MIMEMultipart 
from email.MIMEText import MIMEText 
from email.MIMEBase import MIMEBase 
from openpyxl import Workbook 
from datetime import datetime 
from io import BytesIO 
from email import encoders 

def main():
    db = mysql.connector.connect( user='MySQL User', password='MySQL Password', host='MySQL Host', database='DB Name')
    cur = db.cursor()
    workbook = Workbook()
    SQL = 'SELECT date,time,ext,number,val FROM valuation;' #Insert your sql query
    cur.execute(SQL)
    results = cur.fetchall()
    sheet = workbook.active
    sheet.title = u'Report' #Title name
    column_names = [u'Date', u'Time', u'Extension' ,u'External Number', u'Valuation'] #Columns Name for excel 
    sheet.append(column_names)
    for row in results:
        sheet.append(row)
    dt = datetime.now();
    dt = dt.strftime("%d.%m.%Y %H-%M")
    file_extension = ".xlsx"
    filename = "report_" + dt + file_extension
    workbook.save(filename)
    attach = BytesIO()
    workbook.save(attach)
	
    msg = MIMEMultipart()
    fromaddr = "module@localhost.ru"
    toaddr = "admin@admin.ru"
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = u"Report " + dt
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attach.getvalue())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP("localhost")
    #server = smtplib.SMTP("SMTP IP", 25)
    server.set_debuglevel(1)
    #server.ehlo()
    #server.starttls()
    server.ehlo()
    #server.esmtp_features['auth'] = 'LOGIN PLAIN'
    #server.login("username", "password")
    msg = msg.as_string()
    server.sendmail(fromaddr, toaddr, msg)
    server.quit() 

if __name__ =='__main__': main()
