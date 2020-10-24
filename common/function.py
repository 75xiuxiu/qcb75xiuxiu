import time
def login_page(driver,username,password):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()
def open_url(driver,url): #打开网页
    driver.get(url)
    driver.maximize_window()
def search_key(driver,url,username,password,s_key):
    open_url(driver,url)
    login_page(driver,username,password)
    driver.find_element_by_xpath('//span[text()="零售出库"]').click()
    P_id=driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")
    F_id=P_id+"-frame"
    #1.根据id切换
    driver.switch_to.frame(F_id)
    #2.元素定位切换
    # driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(F_id)).get_attribute("id"))
    #3.下标切换
    # driver.switch_to.frame(1)
    driver.find_element_by_id("searchNumber").send_keys(s_key)
    driver.find_element_by_id("searchBtn").click()
    time.sleep(1)
    num=driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']//div").text
    return num