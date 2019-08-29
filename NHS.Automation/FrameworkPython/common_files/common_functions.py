from selenium import webdriver
from selenium.webdriver import Chrome,ie,firefox,safari
from selenium.webdriver.chrome.options import Options
from page_structure import login
from library_files import read_config
import openpyxl

def initalsetup():

    global str_excel_wb, str_excel_ws, str_browser, str_url, head_less_flag

    #Initialize browser and application URL
    str_browser = read_config.read_config_data('ConfigDetails', 'Test_Browser')
    str_url = read_config.read_config_data('ConfigDetails', 'Application_URL')

    #Initialize the excel path and load test data files
    wkBookName = read_config.read_config_data('ConfigDetails', 'Excel_Path')
    wkSheetName = read_config.read_config_data('ConfigDetails', 'Excel_Sheet')
    head_less_flag = read_config.read_config_data('ConfigDetails', 'Head_Less')
    str_excel_wb = openpyxl.load_workbook(wkBookName)
    str_excel_ws = str_excel_wb[wkSheetName]
    return str_excel_wb, str_excel_ws, str_browser, str_url

def launch_browser_url(str_browser,str_url):
    global driver

    #Check for Browser configurations and invole browser accordingly
    if str_browser == 'Chrome':
        strPath = read_config.read_config_data('ConfigDetails', 'Exe_Path')
        options = Options()
        if head_less_flag == 'True':
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(strPath, options=options)
    driver.get(str_url)
    driver.maximize_window()

    return driver

def login_application(login_cred,password):

    obj_login_class = login.LoginPageClass(driver)
    #Enter login credentials
    obj_login_class.enter_login(login_cred)
    obj_login_class.enter_password(password)

    #Click on Login button and validate Home page
    obj_login_class.btn_clk_login()
    obj_login_class.validate_home_page(login_cred)


def close_browser():

    #Close the browser at end of execution
    return driver.close()