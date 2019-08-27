import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from library_files import read_config
from page_structure import login
import openpyxl
from common_files import common_functions

class HomePageClass:

    def __init__(self,obj):
        global driver
        driver=obj

        @property
        def drive(self):
            return driver

    def select_dropdown_value(self):

        select2=driver.find_element_by_xpath(read_config.read_element_locator('Home_Page', 'drop_down_click')).send_keys('RR8'+Keys.TAB)
        #time.sleep(10)
        WebDriverWait(driver, 120).until(ec.visibility_of_element_located( (By.XPATH, "//*[name()='svg']//*[name()='g']//*[text()='Trust RR8 vs Region R1']")))

    def validate_graph_trust_vs_region(self,str_excel_ws):

        WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//*[name()='svg']//*[name()='g']//*[text()='Trust RR8 vs Region R1']")))
        label_graph = driver.find_element_by_xpath("//*[name()='svg']//*[name()='g']//*[text()='Trust RR8 vs Region R1']")
        label_graph_text = label_graph.text
        #print(label_graph_text)
        value_graph_two = str_excel_ws.cell(row=3, column=2).value
        assert label_graph_text.find(value_graph_two) != -1, print("Verified that graph is loaded successfully")

    def select_graph_trust_vs_peers(self):
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='dv_chart_row_panel']/div[2]/div[2]/a/img")))

        #graph_one = driver.find_element_by_xpath("//*[@id='dv_chart_row_panel']/div[2]/div[2]/a/img").click()
        graph_one = driver.find_element_by_xpath("//*[@id='dv_chart_row_panel']/div[2]/div[2]/a/span").click()


    def validate_graph_trust_vs_peers(self,str_excel_ws):

        WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH, "//*[name()='svg']//*[name()='g']//*[text()='Trust RR8 vs Peers']")))
        label_graph_one=driver.find_element_by_xpath("//*[name()='svg']//*[name()='g']//*[text()='Trust RR8 vs Peers']")
        label_graph_one_text=label_graph_one.text
        #print(label_graph_one_text)
        value_graph_one= str_excel_ws.cell(row=4, column=2).value
        assert label_graph_one_text.find(value_graph_one) != -1, print("Verified that graph is loaded successfully")

    def select_graph_region_vs_peer_region(self):
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='dv_chart_row_panel']/div[2]/div[4]/a/img")))
        driver.find_element_by_xpath("//*[@id='dv_chart_row_panel']/div[2]/div[4]/a/img").click()

    def validate_graph_trust_vs_peer_region(self,str_excel_ws):
        WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH, "//*[name()='svg']//*[name()='g']//*[text()='Region R1 vs others']")))
        label_graph_two=driver.find_element_by_xpath("//*[name()='svg']//*[name()='g']//*[text()='Region R1 vs others']")
        label_graph_two_text=label_graph_two.text
        #print(label_graph_two_text)
        value_graph = str_excel_ws.cell(row=5, column=2).value
        assert label_graph_two_text.find(value_graph) != -1, print("Verified that graph is loaded successfully")


    def click_logout(self):
        driver.find_element_by_xpath(read_config.read_element_locator('Home_Page','logout_click')).click()
        time.sleep(3)
