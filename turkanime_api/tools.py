from sys import exit as kapat
import subprocess as sp
from os import name

from prompt_toolkit import styles
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import SessionNotCreatedException

def gereksinim_kontrol():
    """ Gereksinimlerin erişilebilir olup olmadığını kontrol eder """
    eksik=False
    stdout="\n"
    for gereksinim in ["chromedriver","youtube-dl","mpv"]:
        status = sp.Popen(f'{gereksinim} --version',stdout=sp.PIPE,stderr=sp.PIPE,shell=True).wait()
        if status>0:
            stdout += f"x {gereksinim} bulunamadı.\n"
            eksik=True
        else:
            stdout += f"+ {gereksinim} bulundu.\n"
    if eksik:
        print(stdout+"\nBelirtilen program yada programlar",
            "program dizininde yada sistem PATH'ında bulunamadı.",
            "Lütfen klavuzdaki kurulum talimatlarını uygulayın.")
        kapat(1)

def webdriver_hazirla(progress):
    """ Selenium webdriver'ı hazırla """
    parser = ConfigParser()
    parser.read("./config.ini")
    options = Options()
    #options.headless = True
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.set_capability("dom.webdriver.enabled", False)
    options.set_capability('useAutomationExtension', False)
    options.set_capability('permissions.default.image', 2)
    options.add_argument("--disable-logging")
    options.set_capability("network.proxy.type", 0)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument('--disable-blink-features=AutomationControlled')

    if name == 'nt':
        try:
            return webdriver.Chrome(
             options=options,service_log_path='NUL',
                executable_path=r'chromedriver.exe'
            )
        except SessionNotCreatedException:
            progress.stop()
            input("Program Chrome'un kurulu olduğu dizini tespit edemedi.Chromedriver ve chromeun aynı sürümde olduğuna emin olun ")
            kapat()
    return webdriver.Chrome(
         options=options,
        service_log_path='/dev/null'
        )

prompt_tema = styles.Style([
    ('qmark', 'fg:#5F819D bold'),
    ('question', 'fg:#289c64 bold'),
    ('answer', 'fg:#48b5b5 bg:#hidden bold'),
    ('pointer', 'fg:#48b5b5 bold'),
    ('highlighted', 'fg:#07d1e8'),
    ('selected', 'fg:#48b5b5 bg:black bold'),
    ('separator', 'fg:#6C6C6C'),
    ('instruction', 'fg:#77a371'),
    ('text', ''),
    ('disabled', 'fg:#858585 italic')
])
