def start():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    driver = webdriver.Chrome()
    driver.get('http://45.116.207.67/moodle/') # opens the following link in chrome browser in safe mode
    login = driver.find_element_by_xpath('//*[@id="page-wrapper"]/nav/ul[2]/li[3]/div/span/a')
    login.send_keys(Keys.RETURN)
    name = 'username'# your user name 
    pas = 'password'# your password
    name_feild = driver.find_element_by_name('username')
    name_feild.send_keys(name)
    password_feild = driver.find_element_by_name('password')
    password_feild.send_keys(pas)
    login_in = driver.find_element_by_xpath('//*[@id="loginbtn"]')
    login_in.send_keys(Keys.RETURN)
    # open following subject link for attendence
    driver.get('http://45.116.207.67/moodle/course/view.php?id=26')
    time.sleep(1)
    driver.get('http://45.116.207.67/moodle/course/view.php?id=16')
    time.sleep(1)
    driver.get('http://45.116.207.67/moodle/course/view.php?id=39')
    time.sleep(1)
    driver.get('http://45.116.207.67/moodle/course/view.php?id=4')
    time.sleep(1)
    driver.get('http://45.116.207.67/moodle/course/view.php?id=50')
    time.sleep(1)
    driver.get('http://45.116.207.67/moodle/course/view.php?id=8')
    time.sleep(1)
    driver.get('http://45.116.207.67/moodle/course/view.php?id=36')
    time.sleep(1)
    driver.quit()
start()
