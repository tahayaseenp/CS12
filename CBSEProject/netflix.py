# NETFLIX SIMULATOR 
# AUTHOR: Taha Yaseen Parker

import os
import sys
os.system("clear")  # Clear the whole terminal before starting app

print("""
███    ██ ███████ ████████ ███████ ██      ██ ██   ██
████   ██ ██         ██    ██      ██      ██  ██ ██ 
██ ██  ██ █████      ██    █████   ██      ██   ███  
██  ██ ██ ██         ██    ██      ██      ██  ██ ██ 
██   ████ ███████    ██    ██      ███████ ██ ██   ██
""")

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

if sys.version_info[0] < 3:
    print("Please download Python3 from the link below")
    print("https://www.python.org/downloads/")
    input("Press any key to exit!")
    sys.exit("Python3 not installed")

try:  # Install all required modules
    print("Installing dependencies...")
    os.system("pip3 install -qqq --disable-pip-version-check --no-cache-dir --no-color --no-warn-conflicts --user --no-python-version-warning --no-input --no-warn-script-location mysql-connector-python")
    os.system("pip3 install -qqq --disable-pip-version-check --no-cache-dir --no-color --no-warn-conflicts --user --no-python-version-warning --no-input --no-warn-script-location ipinfo")
    os.system("pip3 install -qqq --disable-pip-version-check --no-cache-dir --no-color --no-warn-conflicts --user --no-python-version-warning --no-input --no-warn-script-location datetime")
    os.system("python -m pip install -U -qqq --disable-pip-version-check --no-cache-dir --no-color --no-warn-conflicts --user --no-python-version-warning --no-input --no-warn-script-location cffi pip setuptools")
    os.system("pip3 install -qqq --disable-pip-version-check --no-cache-dir --no-color --no-warn-conflicts --user --no-python-version-warning --no-input --no-warn-script-location argon2-cffi")
    os.system("pip3 install -qqq --disable-pip-version-check --no-cache-dir --no-color --no-warn-conflicts --user --no-python-version-warning --no-input --no-warn-script-location termcolor")
    os.system("pip3 install -qqq --disable-pip-version-check --no-cache-dir --no-color --no-warn-conflicts --user --no-python-version-warning --no-input --no-warn-script-location lxml")
except:
    sys.exit("Unable to install required dependencies!")  # Exit if modules cannot be installed

try:
    print("Importing dependencies...")
    import argon2  # Password hashing module
    import ipinfo  # Find details of IP address
    import datetime  # Get current date and time 
    import time  # Used for debugging purposes
    import termcolor  # Color the output in the terminal
    import base64  # Used for Gmail + OAuth2 in Python
    import imaplib  # Used for Gmail + OAuth2 in Python
    import json  # Used for Gmail + OAuth2 in Python
    import smtplib  # Used for Gmail + OAuth2 in Python
    import urllib.parse  # Used for Gmail + OAuth2 in Python
    import urllib.request  # Used for Gmail + OAuth2 in Python
    import lxml.html  # Used for Gmail + OAuth2 in Python
    import random  # Used for generation of OTPs
    from getpass import getpass  # Mask passwords while they are being inputted
    from mysql.connector import connect  # Connect to MySQL Server
    from email.mime.multipart import MIMEMultipart  # Used for Gmail + OAuth2 in Python
    from email.mime.text import MIMEText  # Used for Gmail + OAuth2 in Python

except:
    sys.exit("Unable to import required dependencies")  # Exit if modules cannot be imported

ip_details = ipinfo.getHandler("eb85c6b947bbc4").getDetails()  # Global variable for fetching IP address details

cdb = connect(host="localhost", user="TP", password="17102005")  # Connecting to the MySQL server
db = cdb.cursor()  # Creating the cursor for the MySQL Server
db.execute("CREATE DATABASE IF NOT EXISTS netflix")  # Create the database if it doesn't exist
cdb.commit()  # Save changes
db.close()  # Close the cursor and ensure that the cursor object has no reference to its original connection object
cdb.close()  # Close the connection to the server

cdb = connect(host="localhost", user="TP", password="17102005", database="netflix")  # Reopen connection to the MySQL server
db = cdb.cursor()  # Creating the cursor for the MySQL Server

# TABLE CREATION START

print("Setting up database...")
db.execute("CREATE TABLE IF NOT EXISTS content(netflix_id BIGINT PRIMARY KEY NOT NULL, title LONGTEXT NOT NULL, type VARCHAR(10) NOT NULL, rating VARCHAR(15) NOT NULL, release_year YEAR NOT NULL, actor1 CHAR(5) NOT NULL, actor2 CHAR(5) NOT NULL, actor3 CHAR(5) NOT NULL, actor4 CHAR(5) NOT NULL, director CHAR(5) NOT NULL, category VARCHAR(255) NOT NULL, imdb VARCHAR(20) NOT NULL, runtime VARCHAR(50) NOT NULL, description LONGTEXT NOT NULL, language VARCHAR(255) NOT NULL, price FLOAT NOT NULL, VAT FLOAT NOT NULL DEFAULT 5.0)")
db.execute("CREATE TABLE IF NOT EXISTS actors(id CHAR(5) PRIMARY KEY NOT NULL, name LONGTEXT)")
db.execute("CREATE TABLE IF NOT EXISTS directors(id CHAR(5) PRIMARY KEY NOT NULL, name LONGTEXT)")
db.execute("CREATE TABLE IF NOT EXISTS customers(name LONGTEXT NOT NULL, email LONGTEXT NOT NULL, phone_number LONGTEXT NOT NULL, username LONGTEXT NOT NULL, country_code CHAR(3) NOT NULL, balance FLOAT NOT NULL DEFAULT 0.0, PRIMARY KEY index_username(username(100)))")
db.execute("CREATE TABLE IF NOT EXISTS auth(username LONGTEXT NOT NULL, passhash LONGTEXT NOT NULL, PRIMARY KEY index_username(username(100)))")
db.execute("CREATE TABLE IF NOT EXISTS orders(id BIGINT AUTO_INCREMENT PRIMARY KEY NOT NULL, customer_username LONGTEXT NOT NULL, date DATETIME)")
db.execute("CREATE TABLE IF NOT EXISTS order_details(order_id BIGINT NOT NULL, content_id BIGINT NOT NULL, amount BIGINT NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS cart(username LONGTEXT, netflix_id BIGINT NOT NULL, title LONGTEXT NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS sudo_logs(query LONGTEXT, query_timestamp LONGTEXT)")

# TABLE CREATION END

# ADDING CONTENT START

try:
    print("Adding information to database...")
    info = open('info.txt', encoding='utf-8')  # Open the text file for executing SQL commands to insert default data
    for l in info:  # For every line in the text file
        db.execute(l)  # Execute line
        cdb.commit()  # Save the changes
    info.close()  # Close the file

except:
    print("Fatal error occurred! Information text is unavailable.")
    sys.exit("Download the program again from https://github.com/tahayaseenp/CBSEProj without deleting any files.")

# ADDING CONTENT END

# GMAIL + OAUTH2 IN PYTHON GLOBAL VARIABLES START
GOOGLE_ACCOUNTS_BASE_URL = 'https://accounts.google.com'
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

GOOGLE_CLIENT_ID = '240231485024-4robsujnfa4plv2gkt6anv8u6km078p7.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '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'
GOOGLE_REFRESH_TOKEN = '1//03ne3YSR8H7FqCgYIARAAGAMSNwF-L9Ir7H1IcM0ngAFkcWs-baiIjqW5ZSetztfcyjyUsmTmBlaVG5l9I4AOTVt01nIVCWyqWVg'

# GMAIL + OAUTH2 IN PYTHON GLOBAL VARIABLES END

login_status = False  # Global Variable: Login Status

# Global dictionary for actors
actors = {}
db.execute("SELECT * FROM actors")
for i in db.fetchall():
    key = i[0]
    value = i[1]
    actors.update({key: value})

# Global dictionary for directors
directors = {}
db.execute("SELECT * FROM directors")
for i in db.fetchall():
    key = i[0]
    value = i[1]
    directors.update({key: value})


# EMAIL DEFINITIONS START
def command_to_url(command):
    return '%s/%s' % (GOOGLE_ACCOUNTS_BASE_URL, command)


def url_escape(text):
    return urllib.parse.quote(text, safe='~-._')


def url_unescape(text):
    return urllib.parse.unquote(text)


def url_format_params(params):
    param_fragments = []
    for param in sorted(params.items(), key=lambda x: x[0]):
        param_fragments.append('%s=%s' % (param[0], url_escape(param[1])))
    return '&'.join(param_fragments)


def generate_permission_url(client_id, scope='https://mail.google.com/'):
    params = {}
    params['client_id'] = client_id
    params['redirect_uri'] = REDIRECT_URI
    params['scope'] = scope
    params['response_type'] = 'code'
    return '%s?%s' % (command_to_url('o/oauth2/auth'), url_format_params(params))


def call_authorize_tokens(client_id, client_secret, authorization_code):
    params = {}
    params['client_id'] = client_id
    params['client_secret'] = client_secret
    params['code'] = authorization_code
    params['redirect_uri'] = REDIRECT_URI
    params['grant_type'] = 'authorization_code'
    request_url = command_to_url('o/oauth2/token')
    response = urllib.request.urlopen(request_url, urllib.parse.urlencode(params).encode('UTF-8')).read().decode('UTF-8')
    return json.loads(response)


def call_refresh_token(client_id, client_secret, refresh_token):
    params = {}
    params['client_id'] = client_id
    params['client_secret'] = client_secret
    params['refresh_token'] = refresh_token
    params['grant_type'] = 'refresh_token'
    request_url = command_to_url('o/oauth2/token')
    response = urllib.request.urlopen(request_url, urllib.parse.urlencode(params).encode('UTF-8')).read().decode('UTF-8')
    return json.loads(response)


def generate_oauth2_string(username, access_token, as_base64=False):
    auth_string = 'user=%s\1auth=Bearer %s\1\1' % (username, access_token)
    if as_base64:
        auth_string = base64.b64encode(auth_string.encode('ascii')).decode('ascii')
    return auth_string


def test_imap(user, auth_string):
    imap_conn = imaplib.IMAP4_SSL('imap.gmail.com')
    imap_conn.debug = 4
    imap_conn.authenticate('XOAUTH2', lambda x: auth_string)
    imap_conn.select('INBOX')


def test_smpt(user, base64_auth_string):
    smtp_conn = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_conn.set_debuglevel(True)
    smtp_conn.ehlo('test')
    smtp_conn.starttls()
    smtp_conn.docmd('AUTH', 'XOAUTH2 ' + base64_auth_string)


def get_authorization(google_client_id, google_client_secret):
    scope = "https://mail.google.com/"
    print('Navigate to the following URL to auth:', generate_permission_url(google_client_id, scope))
    authorization_code = input('Enter verification code: ')
    response = call_authorize_tokens(google_client_id, google_client_secret, authorization_code)
    return response['refresh_token'], response['access_token'], response['expires_in']


def refresh_authorization(google_client_id, google_client_secret, refresh_token):
    response = call_refresh_token(google_client_id, google_client_secret, refresh_token)
    return response['access_token'], response['expires_in']


def send_mail(fromaddr, toaddr, subject, message):
    access_token, expires_in = refresh_authorization(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN)
    auth_string = generate_oauth2_string(fromaddr, access_token, as_base64=True)

    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg.preamble = 'This is a multi-part message in MIME format.'
    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)
    part_text = MIMEText(lxml.html.fromstring(message).text_content().encode('utf-8'), 'plain', _charset='utf-8')
    part_html = MIMEText(message.encode('utf-8'), 'html', _charset='utf-8')
    msg_alternative.attach(part_text)
    msg_alternative.attach(part_html)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo(GOOGLE_CLIENT_ID)
    server.starttls()
    server.docmd('AUTH', 'XOAUTH2 ' + auth_string)
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()

# EMAIL DEFINITIONS END


def record_checker(tablename, fieldname, variable):  # Check if a particular record exists in the one of the database's tables
    db.execute("SELECT {mycolumn} FROM {mytablename} WHERE {mycolumn} = %s".format(
        mycolumn=fieldname, mytablename=tablename), (variable,))
    rs = db.fetchall()
    if len(rs) == 0:
        return False

    else:
        if rs[0][0] == variable:
            return True
        else:
            return False


def get_price(nid):  # Get the final price of content using content ID
    db.execute("SELECT (price + ((price*vat) / 100)) 'Price' FROM content WHERE netflix_id = %s", (nid,))
    rs = db.fetchall()[0][0]
    return rs


def pass_hasher(password):  # Hash a given password
    return argon2.PasswordHasher().hash(password)


def pass_verify(hash, inputpass):  # Verify that an inputted password and the hash are similar
    return argon2.PasswordHasher().verify(hash, inputpass)


def gen_otp():  # Generate an OTP
    return str(int(random.random()*1000000))


def add_content():  # Add content to the database
    netflix_id = int(input("Enter Netflix ID: "))
    title = input("Enter content title: ")
    print("Content types:")
    print("1. Movie")
    print("2. TV Show")
    c = int(input("Select content type:"))
    if c == 1:
        type = "Movie"
    elif c == 2:
        type = "TV Show"
    else:
        sys.exit("Invalid content type")
    rating = input("Enter PG rating: ")
    release_year = int(input("Enter release year: "))
    actor1 = input("Enter actor1 code:")
    actor2 = input("Enter actor2 code (use AC000 for NULL): ")
    actor3 = input("Enter actor3 code (use AC000 for NULL): ")
    actor4 = input("Enter actor4 code (use AC000 for NULL): ")
    rc1 = record_checker("actors", 'id', actor1)  # Check if the actor ID entered exists in the database
    rc2 = record_checker("actors", 'id', actor2)
    rc3 = record_checker("actors", 'id', actor3)
    rc4 = record_checker("actors", 'id', actor4)
    director = input("Enter director code: ")
    rc5 = record_checker("directors", 'id', director)  # Check if the director ID entered exists in the database
    category = input("Enter content category: ")
    imdb = input("Enter IMDB rating: ")
    runtime = int(input("Enter content length in minutes: "))
    runtime += "min"
    description = input("Enter content description: ")
    language = input("Enter content language: ")
    price = float(input("Enter content price: "))
    vat = float(input("Enter content VAT: "))
    # Enter the record into the database only if all Actor ID's and Director ID exist
    db.execute("INSERT INTO content(netflix_id, title, type, rating, release_year, actor1, actor2, actor3, actor4, director, category, imdb, runtime, description, language, price, vat)  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (netflix_id, title, type, rating, release_year, actor1, actor2, actor3, actor4, director, category, imdb, runtime, description, language, price, vat)) if rc1 == True and rc2 == True and rc3 == True and rc4 == True and rc5 == True else print("Record not added!")
    cdb.commit()
    print("Content successfully added!")


def add_actor():  # Add actors to the database
    id = input("Enter actor ID: ")
    name = input("Enter actor's full name: ")
    db.execute("INSERT INTO actors VALUES(%s, %s)", (id, name))
    cdb.commit()
    print("Actor successfully added!")


def add_director():  # Add directors to the database
    id = input("Enter director ID: ")
    name = input("Enter director's full name: ")
    db.execute("INSERT INTO directors VALUES(%s, %s)", (id, name))
    cdb.commit()
    print("Director successfully added!")


def register_customer():  # Register a new customer
    name = input("Enter your Full Name: ")
    email = input("Enter your email: ")
    phone_number = input("Enter your phone number in international format: ")
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")  # Mask the password while it's being inputted
    passhash = pass_hasher(password)  # Hash the password
    db.execute("INSERT INTO customers (name, email, phone_number, username, country_code) VALUES(%s, %s, %s, %s, %s)",
            (name, email, phone_number, username, ip_details.country))
    cdb.commit()
    db.execute("INSERT INTO auth VALUES(%s, %s)", (username, passhash))
    cdb.commit()
    os.system("clear")  # Clear the terminal window to remove any personal data
    print("You have successfully registered! Please run the program again and login!")
    sys.exit(0)  # Tells the system that the program exited successfully


def edit_actor():  # Edit an existing actor
    acn = input("Enter actor ID: ")
    db.execute("SELECT name FROM actors WHERE id = %s", (acn,))
    print("Actor name: ", db.fetchall()[0][0])
    new = input("Enter new actor name: ")
    db.execute("UPDATE actors SET name = %s WHERE id = %s", (new, acn)) if acn else print("Actor editing failed!")
    cdb.commit()
    print("Actor successfully edited!")


def edit_director():  # Edit an existing director
    drn = input("Enter director ID: ")
    db.execute("SELECT name FROM directors WHERE id = %s", (drn,))
    print("Director name: ", db.fetchall()[0][0])
    new = input("Enter new director name: ")
    db.execute("UPDATE directors SET name = %s WHERE id = %s", (new, drn)) if drn else print("Director editing failed!")
    cdb.commit()
    print("Director successfully edited!")


def edit_content():  # Edit existing content details
    nid = input("Enter Netflix ID: ")
    db.execute("SELECT title FROM content WHERE netflix_id = %s", (nid,))

    print("Content title: ", db.fetchall()[0][0])

    print("What would you like to edit?")
    print("1. Content Title     		9.  Director")
    print("2. Content Type 				10. Content category")
    print("3. Content PG Rating 		11. IMDB Rating")
    print("4. Content release year		12. Runtime")
    print("5. Actor 1 					13. Description")
    print("6. Actor 2 					14. Language")
    print("7. Actor 3 					15. Price")
    print("8. Actor 4 					16. VAT")

    c = input("Enter your choice: ")

    if c == 1:
        title = input("Enter content title: ")

        if title:
            db.execute("UPDATE content SET title = %s WHERE netflix_id = %s", (title, nid))
            cdb.commit()
            print("Title changed successfully!")

        else:
            print("No title provided!")
        
    elif c == 2:
        type = input("Enter content type: ")

        if type:
            db.execute("UPDATE content SET type = %s WHERE netflix_id = %s", (type, nid))
            cdb.commit()
            print("Type changed successfully!")

        else:
            print("No type provided!")
            
    elif c == 3:
        rating = input("Enter content PG Rating: ")

        if rating:
            db.execute("UPDATE content SET rating = %s WHERE netflix_id = %s", (rating, nid))
            cdb.commit()
            print("Rating changed successfully!")

        else:
            print("No rating provided!")
        
    elif c == 4:
        release_year = input("Enter content release year: ")

        if release_year:
            db.execute("UPDATE content SET release_year = %s WHERE netflix_id = %s", (release_year, nid))
            cdb.commit()
            print("Release year changed successfully!")

        else:
            print("No title provided!")
            
    elif c == 5:
        actor1 = input("Enter Actor 1: ")

        if actor1:
            rc = record_checker('actors', 'id', actor1)
            db.execute("UPDATE content SET actor1 = %s WHERE netflix_id = %s",
                    (actor1, nid)) if rc == True else print("Record not added")
            cdb.commit()
            print("Actor 1 changed successfully!")

        else:
            print("No actor provided!")
            
    elif c == 6:
        actor2 = input("Enter Actor 2: ")

        if actor2:
            rc = record_checker('actors', 'id', actor2)
            db.execute("UPDATE content SET actor2 = %s WHERE netflix_id = %s",
                    (actor2, nid)) if rc == True else print("Record not added")
            cdb.commit()
            print("Actor 2 changed successfully!")

        else:
            print("No actor provided!")
            
    elif c == 7:
        actor3 = input("Enter Actor 3: ")

        if actor3:
            rc = record_checker('actors', 'id', actor3)
            db.execute("UPDATE content SET actor3 = %s WHERE netflix_id = %s",
                    (actor3, nid)) if rc == True else print("Record not added")
            cdb.commit()
            print("Actor 3 changed successfully!")

        else:
            print("No actor provided!")
            
    elif c == 8:
        actor4 = input("Enter Actor 4: ")

        if actor4:
            rc = record_checker('actors', 'id', actor4)
            db.execute("UPDATE content SET actor4 = %s WHERE netflix_id = %s",
                    (actor4, nid)) if rc == True else print("Record not added")
            cdb.commit()
            print("Actor 4 changed successfully!")

        else:
            print("No actor provided!")
            
    elif c == 9:
        director = input("Enter Director: ")

        if director:
            rc = record_checker('directors', 'id', director)
            db.execute("UPDATE content SET director = %s WHERE netflix_id = %s",
                    (director, nid)) if rc == True else print("Record not added")
            cdb.commit()
            print("Director changed successfully!")

        else:
            print("No director provided!")
            
    elif c == 10:
        category = input("Enter content Title: ")

        if category:
            db.execute("UPDATE content SET category = %s WHERE netflix_id = %s", (category, nid))
            cdb.commit()
            print("Category changed successfully!")

        else:
            print("No category provided!")
            
    elif c == 11:
        rating = input("Enter IMDB rating: ")

        if rating:
            db.execute("UPDATE content SET rating = %s WHERE netflix_id = %s", (rating, nid))
            cdb.commit()
            print("IMDB rating changed successfully!")

        else:
            print("No rating provided!")
            
    elif c == 12:
        runtime = int(input("Enter content length in minutes: "))

        if runtime:
            runtime += "min"
            db.execute("UPDATE content SET runtime = %s WHERE netflix_id = %s", (runtime, nid))
            cdb.commit()
            print("Content length changed successfully!")

        else:
            print("No length provided!")
            
    elif c == 13:
        desc = input("Enter content description: ")

        if desc:
            db.execute("UPDATE content SET desc = %s WHERE netflix_id = %s", (desc, nid))
            cdb.commit()
            print("Description changed successfully!")

        else:
            print("No description provided!")
            
    elif c == 14:
        lang = input("Enter language: ")

        if lang:
            db.execute("UPDATE content SET language = %s WHERE netflix_id = %s", (lang, nid))
            cdb.commit()
            print("Language changed successfully!")

        else:
            print("No language provided!")
    
    elif c == 15:
        price = float(input("Enter content price: "))

        if price:
            db.execute("UPDATE content SET price = %s WHERE netflix_id = %s", (price, nid))
            cdb.commit()
            print("Price changed successfully!")

        else:
            print("No price provided!")
    
    elif c == 16:
        vat = float(input("Enter content VAT: "))

        if vat:
            db.execute("UPDATE content SET vat = %s WHERE netflix_id = %s", (vat, nid))
            cdb.commit()
            print("VAT changed successfully!")

        else:
            print("No VAT provided!")


def edit_customer():  # Edit customer details
    print()
    print("1. Change name")
    print("2. Change email")
    print("3. Change phone number")
    print("4. Change password")
    
    ch = int(input("Enter your choice: "))
    
    while True:
        if ch == 1:
            name = input("Enter new name: ")
            db.execute("UPDATE customers SET name = %s WHERE username = %s", (name, login_username))
            cdb.commit()
            print("Name changed successfully!")
            print()
            break
            
        elif ch == 2:
            email = input("Enter new email: ")
            db.execute("UPDATE customers SET email = %s WHERE username = %s", (email, login_username))
            cdb.commit()
            print("Email changed successfully!")
            print()
            break
            
        elif ch == 3:
            phone_number = input("Enter new phone number in international format: ")
            db.execute("UPDATE customers SET phone_number = %s WHERE username = %s", (phone_number, login_username))
            cdb.commit()
            print("Phone number changed successfully!")
            print()
            break
        
        elif ch == 4:
            password = getpass("Enter your current password: ")
            db.execute("SELECT passhash FROM auth WHERE username = %s", (login_username,))
            rs = db.fetchall()[0][0]
            try:
                c = pass_verify(rs, password)  # Verify if current password matches the hash existing in the database
            except argon2.exceptions.VerifyMismatchError:
                sys.exit("Incorrect password!")  # Exit the program if the password entered was incorrect
            
            if c == True:
                newpass = getpass("Enter new password: ")
                passhash = pass_hasher(newpass)
                db.execute("UPDATE auth SET passhash = %s WHERE username = %s", (passhash, login_username))
                cdb.commit()
                print("Password changed successfully!")
                print()
                break
            
        elif ch == 0:
            break


def remove_actor():  # Remove actors from the database
    # Confirmation to ensure that no records are deleted by accident
    x = input("WARNING! YOU ARE ATTEMTPING TO REMOVE RECORDS FROM THE DATABASE! TYPE 'I know what I'm doing' (Case Sensitive) TO CONTINUE: ")
    if x != "I know what I'm doing":
        sys.exit("Wrong phrase entered!")

    else:
        acn = input("Enter actor ID: ")
        db.execute("SELECT name FROM actors WHERE id = %s", (acn,))
        print("Actor name: ", db.fetchall()[0][0])
        print("Would you like to delete this actor? NOTE: THIS ACTION IS IRREVERSIBLE")
        # Confirmation to ensure that no records are deleted by accident
        cfm = input("Type 'I Confirm' (Case Sensitive) to continue: ")

        if cfm != "I Confirm":
            sys.exit("Wrong phrase entered!")

        else:
            db.execute("DELETE FROM actors WHERE id = %s", (acn,))
            cdb.commit()
            print("Actor successfully deleted!")


def remove_director():  # Remove directors from the database
    # Confirmation to ensure that no records are deleted by accident
    x = input("WARNING! YOU ARE ATTEMTPING TO REMOVE RECORDS FROM THE DATABASE! TYPE 'I know what I'm doing' (Case Sensitive) TO CONTINUE: ")
    if x != "I know what I'm doing":
        sys.exit("Wrong phrase entered!")

    else:
        drn = input("Enter director ID: ")
        db.execute("SELECT name FROM directors WHERE id = %s", (drn,))
        print("Director name: ", db.fetchall()[0][0])
        print("Would you like to delete this director? NOTE: THIS ACTION IS IRREVERSIBLE")
        # Confirmation to ensure that no records are deleted by accident
        cfm = input("Type 'I Confirm' (Case Sensitive) to continue: ")

        if cfm != "I Confirm":
            sys.exit("Wrong phrase entered!")

        else:
            db.execute("DELETE FROM directors WHERE id = %s", (drn,))
            cdb.commit()
            print("Director successfully deleted!")


def remove_content():  # Remove content from the database
    # Confirmation to ensure that no records are deleted by accident
    x = input("WARNING! YOU ARE ATTEMTPING TO REMOVE RECORDS FROM THE DATABASE! TYPE 'I know what I'm doing' (Case Sensitive) TO CONTINUE: ")
    if x != "I know what I'm doing":
        sys.exit("Wrong phrase entered!")

    else:
        cid = input("Enter content ID: ")
        db.execute("SELECT name FROM content WHERE netflix_id = %s", (cid,))
        print("Content name: ", db.fetchall()[0][0])
        print("Would you like to delete this actor? NOTE: THIS ACTION IS IRREVERSIBLE")
        # Confirmation to ensure that no records are deleted by accident
        cfm = input("Type 'I Confirm' (Case Sensitive) to continue: ")
        
        if cfm != "I Confirm":
            sys.exit("Wrong phrase entered!")

        else:
            db.execute("DELETE FROM content WHERE netflix_id = %s", (cid,))
            cdb.commit()
            print("Content successfully deleted!")


def login():  # Log in the user
    global login_status
    global login_username
    login_username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    db.execute("SELECT username, passhash FROM auth")
    rs = db.fetchall()

    if len(rs) == 0:
        sys.exit("Username doesn't exist!")

    while True:

        for i in rs:

            try:
                c = pass_verify(i[1], password)
            except argon2.exceptions.VerifyMismatchError:
                sys.exit("Incorrect password!")  # Exit if password is incorrect

            if i[0] == login_username and c == True:
                login_status = True  # Set login status to True
                os.system('clear')  # Clear terminal to remove personal information
                print("Login successful!")
                print("Hello,", login_username + "!" "\n")
                return login_status

            elif i[0] != login_username or c == False:
                login_status = False
                sys.exit("Username doesn't exist!")

            else:
                login_status = False
                sys.exit("Unknown error occurred!")

        break


def logout():  # Log out and exit the program
    global login_status
    global login_username
    login_status = False
    login_username = None
    print("Thank You for using Netflix Simulator!")
    sys.exit("Successfully logged out!")


def search_content(c):  # Search for content when a part of the title is given
    db.execute("SELECT netflix_id, title FROM content WHERE title LIKE %s", ('%' + c + '%',))
    rs = db.fetchall()
    if len(rs) == 0:
        return "No content found!"
    else:
        return rs


def list_info(id):  # List all the info about some content with given content ID
    db.execute("SELECT title, release_year, rating, type, runtime, language, actor1, actor2, actor3, actor4, director, imdb, description, (price + ((price*vat)/100)) FROM content WHERE netflix_id = %s", (id,))
    rs = db.fetchall()[0]
    print()

    ac1 = actors.get(rs[6])
    ac2 = '| ' + actors.get(rs[7]) if actors.get(rs[7]) != "NULL" else ''
    ac3 = '| ' + actors.get(rs[8]) if actors.get(rs[8]) != "NULL" else ''
    ac4 = '| ' + actors.get(rs[9]) if actors.get(rs[9]) != "NULL" else ''

    if rs[7] == "NULL":
        ac2 = ac3 = ac4 = ''

    elif rs[8] == "NULL":
        ac3 = ac4 = ''

    elif rs[9] == "NULL":
        ac4 = ''

    print(termcolor.colored(rs[0].upper(), 'red', attrs=['bold', 'underline']))
    print("Release Year:", rs[1])
    print("Rating:", rs[2])
    print("Content Type:", rs[3])
    print("Runtime:", rs[4])
    print("Language:", rs[5])
    print("Starring:", ac1, ac2, ac3, ac4)
    print("Directors:", directors.get(rs[10]))
    print("IMDB Rating:", rs[11])
    print("Description:", rs[12])
    print("Price: AED", rs[13])
    print()


def luhn(ccn):  # Check if the credit card number entered is correct
    c = [int(x) for x in str(ccn)[::-2]]
    u2 = [(2*int(y))//10+(2*int(y)) % 10 for y in str(ccn)[-2::-2]]
    return sum(c+u2) % 10 == 0


def add_credit():  # Add credit to the customer's account
    print("Add credit to your account")
    amnt = float(input("Amount to credit: "))
    ccno = input("Card number (without spaces or dashes): ")
    exdt = input("Expiration date (MM/YY): ")
    cvv = getpass("CVV: ")
    name = input("Cardholder Name: ")
    adl1 = input("Billing Address: ")
    city = input("City: ")
    country = input("Country: ")

    # Verifies that the credit card number is correct and card is not expired
    if luhn(ccno) == True and (datetime.datetime.now().month <= int(exdt[0:2]) or int(str(datetime.datetime.now().year)[2:]) <= int(exdt[3:])):
        db.execute("UPDATE customers SET balance = balance + %s WHERE username = %s", (amnt, login_username))
        cdb.commit()

        print("Account balance updated successfully!")

    else:
        print("Incorrect card details!")
        

def check_if_bought(nid):  # Check if content has already been bought with given content ID
    db.execute("SELECT content_id FROM order_details, orders, customers WHERE order_details.order_id=orders.id AND orders.customer_username=customers.username")
    rs = db.fetchall()

    if len(rs) == 0:
        return False

    else:
        for i in rs:
            if i[0] == nid:
                return True

            else:
                return False


def buy_now(nid):  # Buy content
    cib = check_if_bought(nid)
    if cib == False:
        db.execute("SELECT balance FROM customers WHERE username = %s", (login_username,))
        balance = db.fetchall()[0][0]
        price = get_price(nid)
        
        if price <= balance:
            db.execute("INSERT INTO orders(customer_username, date) VALUES(%s, %s)", (login_username, datetime.datetime.now()))
            cdb.commit()

            db.execute("SELECT id FROM orders ORDER BY date DESC LIMIT 1")
            id = db.fetchall()[0][0]

            db.execute("INSERT INTO order_details VALUES(%s, %s, %s)", (id, nid, price))
            cdb.commit()

            db.execute("UPDATE customers SET balance = balance - %s WHERE username = %s", (price, login_username))
            print("Successfully bought content!")
        
        else:
            # Time to add more credits (and break the bank :) )
            print("Insufficient credits!")

    else:
        print("You already bought this content!")


def list_all_bought():  # List out all content bought
    print(termcolor.colored("All owned content", attrs=['bold', 'underline']))
    print()
    db.execute("SELECT content_id FROM order_details, orders, customers WHERE order_details.order_id=orders.id AND orders.customer_username=customers.username")
    rs = db.fetchall()
    j = 1
    if len(rs) == 0:
        # Go on, buy something, and have fun :)
        print(termcolor.colored("Your purchase history looks empty :(", attrs=['bold']))
        print('\x1B[3m' + "What are you waiting for?" + '\x1B[0m')
    
    else:
        for i in rs:
            nid = i[0]
            db.execute("SELECT title FROM content WHERE netflix_id = %s", (nid,))
            title = db.fetchall()[0][0]
            print(str(j) + '.', title)
            j = j + 1
        print()


def sudo_mode():  # SUDO MODE
    # USE THIS MODE TO RUN ANY SQL COMMAND FROM THE TERMINAL
    # THIS MODE IS NOT ACCESSIBLE TO NORMAL USERS AND IS HIDDEN FROM THE MENU
    otp = gen_otp()
    # Send an OTP to the concerned people to enter SUDO MODE
    send_mail("tp.cs50test@gmail.com", "tahayparker@gmail.com", "Your Netflix Admin OTP",
            "Here's your Netflix Admin OTP<br>" + "<b>" + otp + "</b>" + "<br><b> DO NOT SHARE THIS CODE WITH ANYONE!</b>")
    input_otp = int(input("Enter OTP: "))
    if str(input_otp) == otp:
        print("Access granted")
    else:
        # Exit if OTP is incorrect
        sys.exit("Access denied - Incorrect OTP")

    # SUDO MODE WARNING
    print("""
===============================================================================================================
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  WARNING  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

YOU HAVE ENTERED SUDO MODE!
THIS MODE ALLOWS YOU TO EXECUTE ANY SQL COMMAND THROUGH THE PROGRAM
DO NOT TYPE COMMANDS IF YOU DO NOT KNOW WHAT YOU ARE DOING!
PRESS "quit" (all lowercase) TO EXIT IMMEDIATELY!
ALL COMMANDS TYPED WILL BE LOGGED
TYPE "I understand the implications of using this mode" (Case Sensitive) IN THE INPUT FIELD BELOW TO CONTINUE: 
===============================================================================================================
    """)

    # Confirmation to enter SUDO MODE
    cfm = input("Enter 'I understand the implications of using this mode' over here, or type 'quit' to quit now: ")
    if cfm == 'quit':
        sys.exit("Application exited successfully!")

    elif cfm != 'I understand the implications of using this mode':
        sys.exit("Wrong phrase entered!")
    
    else:
        print("TYPE 'quit' TO QUIT THE PROGRAM AT ANY TIME!")
        print("INCORRECT SQL QUERIES WILL AUTOMATICALLY EXIT THE PROGRAM")

        while True:
            cmd = input("Enter SQL Query: ")
            if cmd.upper().startswith("SELECT") or cmd.upper().startswith("SHOW"):
                # Log the SQL Query, even if it doesn't run successfully
                db.execute("INSERT INTO sudo_logs VALUES(%s, %s)", (cmd, datetime.datetime.now()))
                cdb.commit()
                db.execute(cmd)
                
                for i in db.fetchall():
                    print(i)
                    print()
            
            elif cmd.upper().startswith("CREATE") or cmd.upper().startswith("UPDATE") or cmd.upper().startswith("INSERT") or cmd.upper().startswith("DELETE"):
                # Log the SQL Query, even if it doesn't run successfully
                db.execute("INSERT INTO sudo_logs VALUES(%s, %s)", (cmd, datetime.datetime.now()))
                cdb.commit()

                db.execute(cmd)
                cdb.commit()

                print("Command successfully executed!")
            
            elif cmd == 'quit':
                sys.exit("Application exited successfully!")


# LOGIN MENU
while True:
    print("\n1. SIGN IN")
    print("2. JOIN NETFLIX")
    print("0. Exit")
    ch = input("Enter your choice: ")
    if ch == '1':
        login()

    elif ch == '2':
        register_customer()

    elif ch == 'setgoogle':
        if GOOGLE_REFRESH_TOKEN is None:
            print('No refresh token found, obtaining one')
            refresh_token, access_token, expires_in = get_authorization(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET)
            print('Set the following as your GOOGLE_REFRESH_TOKEN:', refresh_token)
            sys.exit(0)

    elif ch == 'admin':  # ADMIN MODE
        # USE THIS MODE TO ADD, EDIT OR DELETE CONTENT FROM THE DATABASE
        # THIS MODE IS NOT ACCESSIBLE TO NORMAL USERS AND IS HIDDEN FROM THE MENU

        otp = gen_otp()
        # Send an OTP to the concerned people to enter ADMIN mode
        send_mail("tp.cs50test@gmail.com", "tahayparker@gmail.com", "Your Netflix Admin OTP",
                "Here's your Netflix Admin OTP<br>" + "<b>" + otp + "</b>" + "<br><b> DO NOT SHARE THIS CODE WITH ANYONE!</b>")
        input_otp = int(input("Enter OTP: "))
        if str(input_otp) == otp:
            print("Access granted")
        else:
            # Exit if OTP is incorrect
            sys.exit("Access denied - Incorrect OTP")
        
        # ADMIN MODE Menu
        while True:
            print("1. Add Functions")
            print("2. Edit Functions")
            print("3. Delete functions")
            print("0. Exit")
            a = int(input("Enter your choice: "))
            if a == 1:
                while True:
                    print("1. Add Content")
                    print("2. Add Actors")
                    print("3. Add Directors")
                    print("0. Exit")
                    
                    b = int(input("Enter your choice: "))
                    if b == 1:
                        add_content()
                    
                    elif b == 2:
                        add_actor()

                    elif b == 3:
                        add_director()

                    elif b == 0:
                        break
            
            elif a == 2:
                while True:
                    print("1. Edit Content")
                    print("2. Edit Actors")
                    print("3. Edit Directors")
                    print("0. Exit")

                    c = int(input("Enter your choice: "))
                    if c == 1:
                        edit_content()

                    elif c == 2:
                        edit_actor()
                    
                    elif c == 3:
                        edit_director()

                    elif c == 0:
                        break

            elif a == 3:
                while True:
                    print("1. Delete Content")
                    print("2. Delete Actors")
                    print("3. Delete Directors")
                    print("0. Exit")

                    d = int(input("Enter your choice: "))
                    if d == 1:
                        remove_content()

                    elif d == 2:
                        remove_actor()
                    
                    elif d == 3:
                        remove_director()

                    elif d == 0:
                        break

            elif a == 0:
                sys.exit("Application exited successfully!")

    elif ch == 'sudo':
        sudo_mode()

    elif ch == '0':
        sys.exit("Application exited successfully!")

    else:
        sys.exit("Option not found!")

    break

while True:
    if login_status != True:  # Check if user has logged in
        sys.exit("Please login to continue")        
    else:
        # MAIN MENU
        print()
        print("1. Search for content")
        print("2. View Cart")
        print("3. Account Management")
        print("4. About")
        print("0. Logout")

        sch = input("Enter your choice: ")

        if sch == '1':
            print()
            print("1. Search for content using title")
            print("2. Search for content using Netflix ID")
            print("3. List all content")
            
            ch = int(input("Enter your choice: "))
            if ch == 1:
                while True:
                    name = input("Enter content title to search: ")
                    rs = search_content(name)  # Search for content using (part of) title
                    if rs == "No content found!":
                        print("No content found!")
                        print()
                        break
                    
                    for i in range(0, len(rs)):
                        print(str(i+1)+".", rs[i][1])
                    print()
                    s = int(input("Enter content number for more options:"))
                    sid = rs[s-1][0]
                    list_info(sid)

                    print("1. Buy now!")
                    print("2. Add to cart")
                    co = int(input("Enter your choice: "))
                    if co == 1:
                        print()
                        # Buy content
                        buy_now(sid)
                        break

                    elif co == 2:
                        # Add to cart
                        db.execute("INSERT INTO cart VALUES(%s, %s, %s)", (login_username, sid, rs[s-1][1]))
                        cdb.commit()
                        print("Added to cart!")
                        print()
                        break

                    elif co == 0:
                        break

            elif ch == 2:
                while True:
                    # Search using Content ID
                    nid = int(input("Enter Netflix ID: "))
                    db.execute("SELECT netflix_id, title FROM content WHERE netflix_id = %s", (nid,))
                    rs = db.fetchall()
                    if len(rs) == 0:
                        print("No content found!")
                        print()
                        break
                    else:
                        rs = rs[0]
                    list_info(nid)

                    print("1. Buy now!")
                    print("2. Add to cart")
                    ct = int(input("Enter your choice: "))
                    if ct == 1:
                        print()
                        # Buy content
                        buy_now(nid)
                        break
                    
                    elif ct == 2:
                        # Add to cart
                        db.execute("INSERT INTO cart VALUES(%s, %s, %s)", (login_username, nid, rs[1]))
                        cdb.commit()
                        print("Added to cart!")
                        print()
                        break

                    elif ct == 0:
                        break
                
            elif ch == 3:
                while True:
                    # List all the content in the database, for those who can never decide on what to watch
                    db.execute("SELECT netflix_id, title FROM content ORDER BY title")
                    rs = db.fetchall()
                    print()
                    for i in range(0, len(rs)):
                        print(str(i+1)+".", rs[i][1])
                    print()

                    s = int(input("Enter content number for more options:"))
                    if s == 0:
                        print()
                        break
                    sid = rs[s-1][0]
                    list_info(sid)
                    print("1. Buy now!")
                    print("2. Add to cart")
                    cr = int(input("Enter your choice: "))
                    if cr == 1:
                        print()
                        # Buy content
                        buy_now(sid)
                        break
                
                    elif cr == 2:
                        # Add to cart
                        db.execute("INSERT INTO cart VALUES(%s, %s, %s)", (login_username, sid, rs[s-1][1]))
                        cdb.commit()
                        print("Added to cart!")
                        print()
                        break

                    elif cr == 0:
                        break
            
            elif ch == 0:
                continue

        elif sch == '2':  # CART
            while True:
                # Made using ANSI characters
                # Check Bibliography for source
                print("""                                
██████   █████  ██████  ████████ 
██      ██   ██ ██   ██    ██    
██      ███████ ██████     ██    
██      ██   ██ ██   ██    ██    
██████  ██   ██ ██   ██    ██    
                """)
                db.execute("SELECT DISTINCT * FROM cart WHERE username = %s", (login_username,))
                # Select all content in cart without duplication
                rs = db.fetchall()
                
                if len(rs) == 0:
                    # C'mon, buy movies and TV Shows and add some to the cart to buy later
                    print(termcolor.colored("Your cart looks empty :(", attrs=['bold']))
                    print('\x1B[3m' + "What are you waiting for?" + '\x1B[0m')
                    print()
                    break
                    
                for i in range(0, len(rs)):
                    print(str(i+1)+".", rs[i][2])
                print()

                print("1. View movie details")
                print("2. Delete specific items")
                print("3. Empty cart")

                s = int(input("Enter your choice: "))
                
                if s == 1:
                    c = int(input("Enter content number: "))
                    sid = rs[c-1][1]
                    list_info(sid)  # List all info

                    c = int(input("Press 1 to buy now: "))

                    if c == 1:
                        print()
                        buy_now(sid)
                        # Delete content from cart when it is bought
                        db.execute("DELETE FROM cart WHERE username = %s AND netflix_id = %s", (login_username, sid))
                        cdb.commit()
                        break
                    
                    elif c == 0:
                        break

                elif s == 2:
                    c = int(input("Enter content number: "))
                    sid = rs[c-1][1]
                    # Delete certain content from cart ("You COULD do that.. But why? Why would you do that? Why would you do any of that?")
                    db.execute("DELETE FROM cart WHERE username = %s AND netflix_id = %s", (login_username, sid))
                    cdb.commit()
                    print("Successfully deleted content!")
                    print()

                elif s == 3:
                    # Delete all content from cart ("You COULD do that.. But why? Why would you do that? Why would you do any of that?")
                    db.execute("DELETE FROM cart WHERE username = %s", (login_username,))
                    cdb.commit()
                    print("Successfully emptied cart!")
                    print()
                    break

                elif s == 0:
                    break
        
        elif sch == '3':  # Account Management Menu
            while True:
                print()
                print("1. Credit Management")
                print("2. View all purchases")
                print("3. Edit account details")
                print("4. Delete your account")

                t = int(input("Enter your choice: "))

                if t == 1:
                    print()
                    print("1. View current balance")
                    print("2. Add credits to account")

                    v = int(input("Enter your choice: "))
                    
                    if v == 1:  # Check current balance
                        db.execute("SELECT balance FROM customers WHERE username = %s", (login_username,))
                        rs = db.fetchall()[0][0]
                        balance = "AED " + str(rs)
                        print("Current balance:", balance)
                        print()
                        break

                    elif v == 2:  # Add credits [and break the bank :) ]
                        add_credit()
                        print()
                        break

                    elif v == 0:
                        break
                
                elif t == 2:  # List all the good content you've bought
                    list_all_bought()
                    print()
                    break

                elif t == 3:  # Edit customer details
                    edit_customer()
                    print()
                    break

                elif t == 4:  # Delete your account (NOOOOOOOOOO.....PLEASE DON'T LEAVE US😭😭)
                    print("WARNING: THIS WILL DELETE YOUR ACCOUNT PERMANENTLY!")
                    print("YOU WILL LOSE ACCESS TO ALL MOVIES BOUGHT!")
                    print("MOVIES PREVIOUSLY BOUGHT WILL HAVE TO BE BOUGHT AGAIN!")
                    print("CURRENT BALANCE WILL NOT BE REFUNDED!")
                    # Confirmation to delete account [You really wanna leave us? :_ _( ]
                    confirm = input("TO PROCEED, TYPE 'I confirm the deletion' (Case Sensitive): ")

                    if confirm != 'I confirm the deletion':
                        sys.exit("Wrong phrase entered!")
                    
                    else:
                        # Delete account and exit the program
                        db.execute("DELETE FROM customers WHERE username = %s", (login_username,))
                        cdb.commit()
                        db.execute("DELETE FROM auth WHERE username = %s", (login_username,))
                        cdb.commit()
                        sys.exit("Account deleted successfully!")
                
                elif t == 0:
                    break

        elif sch == '4':
            # Licenses and disclaimers
            # and acknowledging everyone who has made this a huge success :)
            print(termcolor.colored("ABOUT THIS PROJECT", attrs=['bold']))

            print("""
Netflix Simulator © 2022 by Taha Yaseen Parker is licensed under Attribution-NonCommercial-NoDerivatives 4.0 International.
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-nd/4.0/

Netflix Simulator is not affiliated, associated, authorized, endorsed by, or in any way officially connected with Netflix Inc., or any of its subsidiaries or its affiliates.
The official Netflix website can be found at http://www.netflix.com.

The name Netflix as well as related names, marks, emblems, and images are registered trademarks of Netflix Inc.
The Netflix service, including all content provided on the Netflix service, is protected by copyright, trade secret or other intellectual property laws and treaties.

Gmail™ email service is a registered trademark of Google LLC.

Other company and product names mentioned herein are trademarks of their respective companies.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Many thanks to the developers of the following Python libraries used in this program:
    
    argon2
    cffi
    ipinfo
    datetime
    termcolor
    getpass
    and many more...
    
Many thanks to Seppe "Macuyiko" vanden Broucke for making public the code to send electronic mails with OAuth2 and Gmail in Python.
Read more at https://blog.macuyiko.com/post/2016/how-to-send-html-mails-with-oauth2-and-gmail-in-python.html

Thanks to Reddit user 'alexnag26' (https://www.reddit.com/user/alexnag26/) for providing the data used in the database.
The data can be found at https://drive.google.com/drive/folders/1Xh-qE7mV8zhFhrPTDWLvgIRUUgrNWmXv?usp=sharing

The author would like to express his sincere gratitude to Mrs. Shenooja Pareed for her valuable guidance, comments, and suggestions.

Thank you to all those who spent their valuable time to find bugs and test the program in every possible use case. 

Thank you to all those who have, directly or indirectly, lent a helping hand in the successful completion of this project.
            """)

        elif sch == '0':
            logout()  # Exit the program
            # See ya soon!
