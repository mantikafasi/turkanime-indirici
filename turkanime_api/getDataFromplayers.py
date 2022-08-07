from time import sleep
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By

# POPUP PLAYERLAR
def getExternalVidOf(driver):
    """ Türkanimenin yeni sekmede açtığı playerlar """
    try:
        iframe_1 = driver.find_element_by_css_selector(".video-icerik iframe") #iframe'in içine gir
        driver.switch_to.frame(iframe_1)
        url = driver.find_element_by_css_selector("#link").get_attribute("href") #linki ceple
    except Exception as e: # HTML DOSYASI HATA VERİRSE
        print(e)
        return False
    else:
        return url

# TÜRKANİME PLAYER
def getTurkanimeVid(driver):
    try: # iki iframe katmanından oluşuyor
        iframe_1 = driver.find_element_by_css_selector(".video-icerik iframe")
        driver.switch_to.frame(iframe_1)
        iframe_2 = driver.find_element_by_css_selector("iframe")
        driver.switch_to.frame(iframe_2)
        url = driver.find_element_by_css_selector(".jw-media").get_attribute("src")
    except Exception as f:
        print(f)
        return False
    else:
        return url

# MAİLRU
def getMailVid(driver):
    try: # iki iframe katmanından oluşuyor
        iframe_1 = driver.find_element_by_css_selector(".video-icerik iframe")
        driver.switch_to.frame(iframe_1)
        iframe_2 = driver.find_element_by_css_selector("iframe")
        driver.switch_to.frame(iframe_2)
        url = driver.find_element_by_css_selector(".b-video-controls__mymail-link").get_attribute("href")
    except Exception as f:
        print(f)
        return False
    else:
        return url

# OPENLOAD
def getOLOADVid(driver):
    driver.find_element_by_xpath("//div[@class='panel-body']/div[@class='video-icerik']/iframe").click()
    driver.switch_to.window(driver.window_handles[1])
    i = 0
    while i<7:
        sleep(1)
        try:
            driver.find_element_by_tag_name('body').click()
            sleep(2)
            while len(driver.window_handles)>2:
                driver.switch_to.window(driver.window_handles[2])
                driver.close()
            driver.switch_to.window(driver.window_handles[1])
            sleep(2.3)
            url = driver.find_elements_by_tag_name('video')[0].get_attribute('src')
        except:
            i+=1
            continue
        else:
            driver.switch_to.window(driver.window_handles[0])
            return url
    return False

# VK
def getVKvid(driver):
    try:
        iframe_1 = driver.find_element_by_css_selector(".video-icerik")
        driver.switch_to.frame(iframe_1)
        iframe_2 = driver.find_element_by_tag_name("iframe")
        driver.switch_to.frame(iframe_2)
        url = driver.find_element_by_css_selector('.videoplayer_btn_vk').get_attribute('href')
    except Exception as f:
        print(f)
        return False
    else:
        return url



players = { # Bütün desteklenen playerlar
    "SIBNET":getDefault,
    "FEMBED":getDefault,
    "OPENLOAD":getOLOADVid,
    "MAIL":getMailVid,
    "VK":getVKvid,
    "GPLUS":getDefault,
    "MYVI":getDefault,
    "TÜRKANİME":getTurkanimeVid,
    "ODNOKLASSNIKI":getDefault,
    "RAPIDVIDEO":getExternalVidOf,
    "UMPLOMP":getExternalVidOf,
    "HDVID":getExternalVidOf,
    "SENDVID":getExternalVidOf,
    "STREAMANGO":getExternalVidOf
}
