from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from myid1 import iid, ppw
import time



try:
    driver = webdriver.Chrome('./chromedriver')
    # driver.set_window_size(1024, 880)
    # driver.maximize_window()
    driver.get('http://gdadmin.mediworldmall.com/member/member_sleep_list.php?pageNum=2000&searchFl=y&key=memId&keyword=&sleepDt%5B%5D=2000-01-01&sleepDt%5B%5D=2018-12-06')

    time.sleep(2)

    elem = driver.find_element_by_xpath("//*[contains(@class, 'btn_administrator_add_close')]")
    elem.click()


    time.sleep(1)

    elem = driver.find_element_by_name('managerId')
    elem.send_keys(iid)
    elem = driver.find_element_by_name('managerPw')
    elem.send_keys(ppw)
    elem.send_keys(Keys.RETURN)

    time.sleep(4)

    fofo = driver.find_element_by_xpath('//*[@id="frmList"]/div[1]/div[1]/strong[1]').text
    print(fofo)
    ac = ActionChains(driver)

    for i in range(1, 1250):
        elem = driver.find_element_by_xpath('//*[@id="frmList"]/div[2]/table/tbody/tr[1]/td[9]/button')
        elem.click()
        time.sleep(1)

        elem = driver.find_element_by_xpath('//*[@class="bootstrap-dialog-footer-buttons"]/*[text()="해제"]')
        elem.click()

        time.sleep(1)

        
        ac.reset_actions()
        ac.send_keys(Keys.F5)
        ac.perform()

        time.sleep(4)

        

except:
    print('종료')

    
    

#     elem = driver.find_element_by_xpath("//span[text()='검색']/..")
#     ac = ActionChains(driver)
#     ac.move_to_element(elem)
#     ac.click()
#     ac.key_down('#라포르몰')
#     ac.perform()

#     time.sleep(2)

#     ac.reset_actions()
#     ac.move_by_offset(0, 50)
#     ac.click()
#     ac.perform()

#     time.sleep(2)

#     divs = 0
#     atag_list = []

#     try:
#         time.sleep(2)
#         elem = driver.find_element_by_xpath("//*[contains(@class, 'zwlfE')]//*[text()='팔로우']")
#         elem.click()
#     except:
#         print('이미 팔로우')
    

#     while True:
#         time.sleep(1)

#         divs = driver.find_elements_by_class_name('v1Nh3')
#         tempDivs = len(divs)
#         print(tempDivs)

#         for i in divs:
#             atag_list += [i.find_element_by_tag_name('a').get_attribute('href')]

#         ac = ActionChains(driver)
#         ac.reset_actions()
#         ac.send_keys(Keys.END)
#         ac.send_keys(Keys.END)
#         ac.perform()
#         # html = driver.find_element_by_xpath("//*[contains(@class, 'SCxLW')]")
#         # html.send_keys(Keys.END)

#         time.sleep(2)

#         divs = driver.find_elements_by_class_name('v1Nh3')
#         tempDivs2 = len(divs)
#         print(tempDivs2)

#         for i in divs:
#             atag_list += [i.find_element_by_tag_name('a').get_attribute('href')]


#         if tempDivs == tempDivs2:
#             ac = ActionChains(driver)
#             atag_list = list(set(atag_list))
#             for i in atag_list:
#                 print(i)
#             print(len(atag_list))
#             break
        
#     for i in atag_list:
#         driver.get(i)
#         time.sleep(1)
#         try:
#             ac.reset_actions()
#             elem = driver.find_element_by_xpath("//*[contains(@class, 'ltpMr')]//*[@aria-label='좋아요']")
#             # elem = driver.find_element_by_xpath("//*[contains(@aria-label,'좋아요')]")
#             ac.move_to_element(elem)
#             ac.click()
#             ac.perform()
#         except:
#             print('이미 좋아요')
#         time.sleep(1)
#     driver.quit()
# except Exception as e:
#     print(e)
# finally:
#     driver.quit()
