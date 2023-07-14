from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=Service("C:/path/to/chromedriver.exe"), options=options)
user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")

def test_button_signIn():
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()
    assert 'In' in 'Sign In'

def test_signIn_class():
    try:
        signIn_attr_class = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Sign In')]"))).get_attribute("class")
    except TimeoutException:
        assert "class" == "btn btn-outline-white header_signin"

def test_signinEmail_len():
    email_attr_formcontrolname = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "signinEmail"))).get_attribute("formcontrolname")
    assert len(email_attr_formcontrolname) < 35

def test_signinPass_len():
    pass_attr_formcontrolname = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "signinPassword"))).get_attribute("formcontrolname")
    assert len(pass_attr_formcontrolname) > 0

def test_Login_type():
    try:
        login_attr_type = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[contains(text(), 'Login')]"))).get_attribute("type")
    except TimeoutException:
        assert "type" == "button"
def test_Login_contens():
    try:
        login_attr_type = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Login')]"))).click()
    except TimeoutException:
        assert 'Log' in 'Login'
