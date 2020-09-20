import selenium, time
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
#browser = webdriver.Chrome('C:/Users/Elena/Desktop/chromedriver.exe')
browser.set_page_load_timeout(30)
browser.implicitly_wait(5)
browser.set_script_timeout(30)
browser.maximize_window() 

browser.get('https://accounts.google.com/AccountChooser/signinchooser?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser')

email_field = browser.find_element_by_id('identifierId')
email_field.clear()

email_field.send_keys('testgmln@gmail.com')

email_next_button = browser.find_element_by_id('identifierNext')
email_next_button.click()

time.sleep(3)

password_field =  browser.find_element_by_name('password')
password_field.clear()

password_field.send_keys('smbtestgm')

password_next_button = browser.find_element_by_id('passwordNext')
password_next_button.click()

name2find = "Елена Арсланова"
found_names_length = 0

if browser.find_elements_by_css_selector('div.afn [name="'+name2find+'"]') or browser.find_elements_by_css_selector('div.afn [email="'+name2find+'"]'):
    found_names_length =  len(browser.find_elements_by_css_selector('div.afn [name="'+name2find+'"]')) + len(browser.find_elements_by_css_selector('div.afn [email="'+name2find+'"]'))
    print("Length of found Names/Emails: "+str(found_names_length)+" letters")
    
    addr_from = "testgmln@gmail.com"                 
    addr_to   = "testgmln@gmail.com"                   
    password  = "smbtestgm"                                  

    msg = MIMEMultipart()                              
    msg['From']    = addr_from                          
    msg['To']      = addr_to                            
    msg['Subject'] = 'Тестовое задание. <Арсланова>'                   

    body = (str(found_names_length)+" letters from: "+name2find)
    msg.attach(MIMEText(body, 'plain'))                 

    server = smtplib.SMTP('smtp.gmail.com', 587)           
    server.set_debuglevel(True)                         
    server.starttls()                                   
    server.login(addr_from, password)                   
    server.send_message(msg)                            
    server.quit() 
else:
    print("Length of found Names/Emails: "+str(found_names_length)+" letters")

time.sleep(1000)
#browser.quit()



