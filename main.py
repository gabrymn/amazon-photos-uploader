from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time as t
import pyautogui
import os

class AutomUPL:

    def __init__(self, email, psw, path = False):
        self.email = email
        self.psw = psw
        self.path = path
        self.cdriver = AutomUPL.__get_chrome_driver()

        # Const
        self.LOGIN_LINK = "https://www.amazon.it/photos?sf=1/ref=s9_acss_bw_h1_EEEESSS_bn_w?ref_=BN_ES_C_U_E_M_CD_CG_417_ADAPSI&pf_rd_m=A1AT7YVPFBWXBL&pf_rd_s=merchandised-search-1&pf_rd_r=CKMHBDSC7YCPSMXR24KE&pf_rd_t=101&pf_rd_p=d284dade-6826-459b-9042-bf7f3d7341d1&pf_rd_i=12364776031"

    def login(self):
        name_field = self.cdriver.find_element(By.ID, "ap_email")
        password_field = self.cdriver.find_element(By.ID, "ap_password")
        name_field.clear()
        name_field.send_keys(self.email)
        password_field.clear()
        password_field.send_keys(self.psw)
        self.cdriver.find_element(By.ID, "signInSubmit").click()

    def upload(self):    
        if self.path == False:
            return False
        else:
            AutomUPL.upload(self, self.path)
            return True

    def upload_dir(self, dir):
        files = os.listdir(dir)
        for file in files:
            AutomUPL.upload(self, dir + file)
            t.sleep(1)

    def upload(self, file):
        self.cdriver.find_element(By.CLASS_NAME, "toggle").click()
        self.cdriver.find_element(By.XPATH, "/html/body/div[1]/div/header/section/div[2]/nav/ul/li[1]/button").click()
        t.sleep(1)
        pyautogui.write(file) 
        pyautogui.press('enter')

    def open_chrome(self):
        self.cdriver.get(self.LOGIN_LINK)

    def __get_chrome_driver():
        chrome_options = webdriver.ChromeOptions()

        # No save password request from chrome
        chrome_options.add_argument("--password-store=basic")
        chrome_options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
            },
        )

        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

        return webdriver.Chrome(options=chrome_options)

    def exec(self, upload = True):
        AutomUPL.open_chrome(self)
        self.cdriver.implicitly_wait(5)
        AutomUPL.login(self)

        if upload == True:       
            AutomUPL.upload(self)

def main():
    EMAIL = "***"
    PSW = "***"
    PATH = r'***'   # + chr(92)

    obj = AutomUPL(EMAIL, PSW, PATH)
    obj.exec()

    t.sleep(3600)

if __name__ == '__main__':
    main()
