import mailbox
import csv

writer = csv.writer(open("example.csv", "wb")) #wb = write binary

for message in mailbox.mbox('example.mbox'):
	writer.writerow([message['date'], message['X-Gmail-Labels'], message['subject'],  message['from']]) #Add here mail's labels to show in the csv
