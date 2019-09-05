import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from library_files import read_config

class HomePageClass:

    def __init__(self,obj):
        global driver
        driver=obj

        @property
        def drive(self):
            return driver

    def select_dropdown_value(self,str_region,str_Label_text):

        driver.find_element_by_xpath(read_config.read_element_locator('Home_Page', 'drop_down_click')).send_keys(str_region+Keys.TAB)
        WebDriverWait(driver, 120).until(ec.visibility_of_element_located( (By.XPATH, "//*[@id='region_display']")))


    def validate_graph_trust_vs_region(self,str_excel_ws):

        value_graph_two = str_excel_ws.cell(row=3, column=2).value

        #wait for the graph to display on browser
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='region_nd_other']")))
        label_graph = driver.find_element_by_xpath(read_config.read_element_locator('Home_Page', 'graph_label'))
        label_graph_text = label_graph.text

        #Validate the graph labels through assestions
        assert label_graph_text.find(value_graph_two) != -1, print("Verified that graph is loaded successfully")

    def select_graph_trust_vs_peers(self):

        #wait for the graph trust vs peers to display
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='chart_div']/div/div[1]/div/svg/g[2]/rect")))

        #click on the graph link
        image_trust_vs_peer = driver.find_element_by_xpath(read_config.read_element_locator('Home_Page', 'image_trust_vs_peer'))
        image_trust_vs_peer.click()


    def validate_graph_trust_vs_peers(self,str_excel_ws):

        value_graph_one= str_excel_ws.cell(row=4, column=4).value

        #wait for the graph to display
        WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='chart_div']/div/div[1]/div/svg/g[2]/rect")))
        label_graph = driver.find_element_by_xpath(read_config.read_element_locator('Home_Page', 'graph_label'))
        label_graph_one_text=label_graph.text

        #assert that the graph is loaded sucessfully
        assert label_graph_one_text.find(value_graph_one) != -1, print("Verified that graph is loaded successfully")

    def select_graph_region_vs_peer_region(self):

        #wait for the graph to display
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='dv_chart_row_panel']/div[2]/div[4]/a/img")))
        img_reg_vs_peer = driver.find_element_by_xpath(read_config.read_element_locator('Home_Page', 'image_region_vs_peer'))

        #click on the graph link to display on page
        img_reg_vs_peer.click()

    def validate_graph_trust_vs_peer_region(self,str_excel_ws):

        value_graph_one = str_excel_ws.cell(row=5, column=4).value
        # wait for the graph to display
        WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='region_nd_other']")))
        label_graph = driver.find_element_by_xpath(read_config.read_element_locator('Home_Page', 'graph_label'))
        label_graph_two_text=label_graph.text

        #assert that the graph is loaded correctly
        assert label_graph_two_text.find(value_graph_one) != -1, print("Verified that graph is loaded successfully")


    def click_logout(self):

        #click on Log out button
        driver.find_element_by_xpath(read_config.read_element_locator('Home_Page','logout_click')).click()
        time.sleep(3)