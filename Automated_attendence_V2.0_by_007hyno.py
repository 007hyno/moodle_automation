from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time  
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://45.116.207.96/moodle/login/index.php') # opens the following link in chrome browser in safe mode
name = 'Username'# your user name here
pas = 'Password'# your password here
#Your subject links as List elements
subjects=["http://45.116.207.96/moodle/mod/attendance/view.php?id=3","http://45.116.207.96/moodle/mod/attendance/view.php?id=17","http://45.116.207.96/moodle/mod/attendance/view.php?id=77","http://45.116.207.96/moodle/mod/attendance/view.php?id=592"] 
# Your are all done🙏🏼 
# Have fun 💜
name_feild = driver.find_element_by_xpath('//*[@id="username"]')
name_feild.send_keys(name)
password_feild = driver.find_element_by_xpath('//*[@id="password"]')
password_feild.send_keys(pas)
login_in = driver.find_element_by_xpath('//*[@id="loginbtn"]')
login_in.send_keys(Keys.RETURN)
# open following subject link for attendence (007hyno)
print("💚Start💚")
for subject in subjects:
    flag=1
    n=1
    driver.get(subject)
    while(flag==1):
        # print("💝🌹🌹💐🚀")
        # print(subject)
        # time.sleep(1)
        n1=str(n)
        n=n+1
        an = "/a"
        link ='//*[@id="region-main"]/div[1]/table[1]/tbody/tr['+n1+']/td[3]'
        # print("link 💚")
        # time.sleep(2)
        try:
            driver.find_element_by_xpath(link)
            att=driver.find_element_by_xpath(link)
            sa=att.text
            # print(subject)        #subject name 
            # print(sa)             #text inside 

            if(sa=="Submit attendance"):
                driver.find_element_by_xpath(link+an).click()
                driver.find_element_by_xpath('//*[@id="fgroup_id_statusarray"]/div[2]/fieldset/div/label[1]/span').click()
                driver.find_element_by_xpath('//*[@id="id_submitbutton"]').click()
                print("---------------------------------------------------")
                print("💜")
                print(subject)
                print(" - Present")
                print("💜")
                print("---------------------------------------------------")
                flag=0
        except :
            print("💛")
            print("No attendece for today at - ")
            print(subject)
            break
# time.sleep(1)
print("💗Success💗")        