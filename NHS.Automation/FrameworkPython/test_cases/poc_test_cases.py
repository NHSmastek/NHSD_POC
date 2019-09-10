import time
import json
import urllib3

from common_files import common_functions
from library_files import read_config
from page_structure import home_page
from page_structure import login
from page_structure import  home_page

def test_tc01_login_to_application():

    global driver,str_excel_wb, str_excel_ws
    #Initialize the configuration variables required for executing tests
    str_excel_wb, str_excel_ws, str_browser, str_url = common_functions.initalsetup()
    login_cred = str_excel_ws.cell(row=2,column=9).value
    password = str_excel_ws.cell(row=2,column=10).value

    #Launch the application browser and URL
    driver = common_functions.launch_browser_url(str_browser, str_url)

    #Log in to the application
    common_functions.login_application(login_cred,password)

    #Logout From the Application
    obj_home_page_class = home_page.HomePageClass(driver)
    obj_home_page_class.click_logout()

    #Closing the Browser
    close = common_functions.close_browser()

def test_tc02_verify_trust_vs_region_graphs():

    global driver,str_excel_wb, str_excel_ws
    #Initialize the configuration variables required for executing tests
    str_excel_wb, str_excel_ws, str_browser, str_url = common_functions.initalsetup()
    login_cred = str_excel_ws.cell(row=2,column=9).value
    password = str_excel_ws.cell(row=2,column=10).value
    str_Label_text = str_excel_ws.cell(row=3, column=2).value
    str_region = str_excel_ws.cell(row=3,column=3).value
    str_trust_name = str_excel_ws.cell(row=3,column=3).value

    value_e1 = str_excel_ws.cell(row=3, column=5).value
    value_e2 = str_excel_ws.cell(row=3, column=6).value
    value_e3 = str_excel_ws.cell(row=3, column=7).value
    value_e4 = str_excel_ws.cell(row=3, column=8).value

    #Launch the application browser and URL
    driver = common_functions.launch_browser_url(str_browser, str_url)

    #Log in to the application
    common_functions.login_application(login_cred,password)

    #Select trust
    obj_home_page_class = home_page.HomePageClass(driver)
    obj_home_page_class.select_dropdown_value(str_region,str_Label_text)

    #Validate graph
    obj_home_page_class.validate_graph_trust_vs_region(str_excel_ws)

    #Validate trust data by analyzing API response
    common_functions.validate_trust_data(str_trust_name,value_e1,value_e2,value_e3,value_e4)

    # Logout From the Application
    obj_home_page_class.click_logout()

    #Close browser
    close = common_functions.close_browser()

def test_tc03_verify_trust_vs_peers_graphs():
    global driver, str_excel_wb, str_excel_ws
    # Initialize the configuration variables required for executing tests
    str_excel_wb, str_excel_ws, str_browser, str_url = common_functions.initalsetup()
    login_cred = str_excel_ws.cell(row=2, column=9).value
    password = str_excel_ws.cell(row=2, column=10).value
    str_region = str_excel_ws.cell(row=4, column=3).value
    str_Label_text = str_excel_ws.cell(row=4, column=2).value
    str_trust_name = str_excel_ws.cell(row=3, column=3).value

    value_e1 = str_excel_ws.cell(row=4, column=5).value
    value_e2 = str_excel_ws.cell(row=4, column=6).value
    value_e3 = str_excel_ws.cell(row=4, column=7).value
    value_e4 = str_excel_ws.cell(row=4, column=8).value

    # Launch the application browser and URL
    driver = common_functions.launch_browser_url(str_browser, str_url)

    # Log in to the application
    common_functions.login_application(login_cred, password)


    # Select trust
    obj_home_page_class = home_page.HomePageClass(driver)
    obj_home_page_class.select_dropdown_value(str_region,str_Label_text)

     #Click on the Trust vr peers graph & Validate
    obj_home_page_class.select_graph_trust_vs_peers()
    obj_home_page_class.validate_graph_trust_vs_peers(str_excel_ws)

    #Validate trust data by analyzing API response
    common_functions.validate_trust_data(str_trust_name,value_e1,value_e2,value_e3,value_e4)

    # Logout From the Application
    obj_home_page_class.click_logout()

    #Close browser
    close = common_functions.close_browser()


def test_tc04_verify_region_vs_peer_regions_graphs():
    global driver, str_excel_wb, str_excel_ws
    # Initialize the configuration variables required for executing tests
    str_excel_wb, str_excel_ws, str_browser, str_url = common_functions.initalsetup()
    login_cred = str_excel_ws.cell(row=2, column=9).value
    password = str_excel_ws.cell(row=2, column=10).value
    str_region = str_excel_ws.cell(row=5, column=3).value
    str_Label_text = str_excel_ws.cell(row=5, column=2).value

    # Launch the application browser and URL
    driver = common_functions.launch_browser_url(str_browser, str_url)

    # Log in to the application
    common_functions.login_application(login_cred, password)

    # Select trust
    obj_home_page_class = home_page.HomePageClass(driver)
    obj_home_page_class.select_dropdown_value(str_region,str_Label_text)

    # Click on the Region vs peer Regions graph & Validate
    obj_home_page_class.select_graph_region_vs_peer_region()
    obj_home_page_class.validate_graph_trust_vs_peer_region(str_excel_ws)

    # Logout From the Application
    obj_home_page_class.click_logout()

    # Close browser
    close = common_functions.close_browser()
