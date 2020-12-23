import re 
import argparse
import sys

class Server:
    """A class for storing the data of all emails found in the dataset.
    
    Attributes:
        emails: a list of email objects where each object is one email.
    """
    def __init__(self, path):
        """
        Initializes a Server object. 
        
        Attributes:
            emails: see class documentation.
            s: using regex to find the sender of an email and passing it into the Email class by creating an instance of the Email class.
            r: using regex to find the receiver of an email and passing it into the Email class by creating an instance of the Email class.
            m: using regex to find the message ID of an email and passing it into the Email class by creating an instance of the Email class.
            d: using regex to find the date of an email and passing it into the Email class by creating an instance of the Email class.
            sub: using regex to find the subject of an email and passing it into the Email class by creating an instance of the Email class.
            b: using regex to find the body of an email and passing it into the Email class by creating an instance of the Email class.
            
        Args:
            path: contains for file path for the dataset.
        """
        self.emails = []
        file = open(path, 'r', encoding="utf8")
        txt = file.read()
        self.emails = txt.split('End Email"')
        file.close()
        
        index = 0
        while index < (len(self.emails)-1):
            
            s = re.findall(r"From\: ([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", self.emails[index])
            r = re.findall(r"To\: ([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", self.emails[index])
            m = re.findall(r"Message-ID\:.*[\d]", self.emails[index])
            d = re.findall(r"Date\: \w+\W+\d+\W+\w+\W+\d+", self.emails[index])
            sub = re.findall(r"Subject\: .*", self.emails[index])
            b = re.findall(r'^\w+\s.*', self.emails[index])
            Email(m,d,sub,s,r,b)
            index += 1 
        
class Email:
    """A class for storing the data related to individual email messages.
    
    Attributes:
        message_id: the message-id that is unique to each email.
        date: date associated with each email.
        subject: the subject of each email.
        sender: the sender of each email.
        receiver: the receiver of each email.
        body: the body message of each email.
    """
    def __init__(self, msg_id, date, subject, sender, receiver, body):
        """
        Initializes an Email object. 
        
        Parameters:
            msg_id: see class documentation.
            date: see class documentation.
            subject: see class documentation.
            sender: see class documentation.
            receiver: see class documentation.
            body: see class documentation.
        """
        self.message_id = msg_id
        self.date = date
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.body = body
        
def parse_args(args_list):
    """ Creates args so that the path of the email dataset can be passed when program is run.
    
    Parameters:
        args_list: command-line argument.
        
    Returns:
        args: parsed command-line argument that contains the path of the email dataset.
    """
    
    parser = argparse.ArgumentParser(description="Created instance of Argument Parser")
    parser.add_argument('--path', '--path', type=str, help= 'add path')
    args = parser.parse_args(args_list)
    
    return args

def main(path):
    """Creates an instance of the server class using a path that is passed in. Prints the length of the emails attribute in the class instance.
    
    Parameters:
        path: the path of the file that contains the email dataset.
    """
    
    Server(path)
    print("The length of the emails attribute is", len(Server(path).emails)-1)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.path)