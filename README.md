# Enron Emails
 Using Regex to comb through Enron Emails

This program uses regex to go through 10,000 enron emails and store relevant data.

Pulls the following -

message_id: the message-id that is unique to each email.

date: date associated with each email.

subject: the subject of each email.

sender: the sender of each email.

receiver: the receiver of each email.

body: the body message of each email.


Requires installation of the argparse module.

https://pypi.org/project/argparse/

Make sure that both the txt file and regex.py are in the same directory and run the program via the terminal.

python3 regex.py --path emails_10k.txt
