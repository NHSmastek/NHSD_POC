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

def prepare_test_data_sheet():
    obj_home_class = home_page.HomePageClass(driver)
    str_excel_ws.cell(row=2,column=1).value = obj_home_class.read_label_RR1()
    str_excel_ws.cell(row=3,column=1).value = obj_home_class.read_label_RR8()
    str_excel_ws.cell(row=4, column=1).value = obj_home_class.read_label_Average()
    str_excel_ws.cell(row=5, column=1).value = obj_home_class.read_label_Transition_Time()
    str_excel_ws.cell(row=6, column=1).value = obj_home_class.read_label_E1()
    str_excel_ws.cell(row=7, column=1).value = obj_home_class.read_label_E2()
    str_excel_ws.cell(row=8, column=1).value = obj_home_class.read_label_E3()
    str_excel_ws.cell(row=9, column=1).value = obj_home_class.read_label_E4()


def login_application(login_cred,password):
    obj_login_class = login.LoginPageClass(driver)
    obj_login_class.enter_login(login_cred)
    obj_login_class.enter_password(password)
    obj_login_class.btn_clk_login()
    obj_login_class.validate_home_page()


def close_browser():
    return driver.close()/