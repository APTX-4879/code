from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
import optparse 
import sys

parser=optparse.OptionParser()
parser.add_option("-u","--url",dest="url")
parser.add_option("-w","--wordlist",dest="file")
(optionss,arguments)=parser.parse_args()
var_url=optionss.url
var_wl=optionss.file
print(var_url)
options=webdriver.ChromeOptions()
#options.add_argument("user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data")

options.add_argument('--headless') #turn off chrome                                                                
options.add_argument('--disable-xss-auditor')  #disable xss security                                                   
options.add_argument('--disable-web-security')                                                    
options.add_argument('--ignore-certificate-errors')                                               
options.add_argument('--no-sandbox') #allow excute code js                                                                                                             
options.add_argument('--disable-notifications') #tat thong bao web
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(executable_path=r'C:\\drivechrome\\chromedriver.exe', options=options)


if not '{test}' in var_url:
	sys.exit()
else:
	web=optionss.url
wordlist = optionss.file
for payload in open(wordlist, "r").readlines():
    url = web.replace('{test}', payload)
    driver.get(url)
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present()) #appear xss pop up
        alert = driver.switch_to_alert()
        alert.accept()
        print("Appear alert pop-up payload: ", payload)
    except TimeoutException:
        print("Not appear alert pop-up payload: ", payload)