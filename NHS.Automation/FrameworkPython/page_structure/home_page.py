from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from library_files import read_config
from page_structure import login


class HomePageClass:

    def __init__(self,obj):
        global driver
        driver=obj

        @property
        def drive(self):
            return driver

    def select_dropdown_value(self):

        select2=driver.find_element_by_xpath(read_config.read_element_locator('Home_Page', 'drop_down_click')).send_keys('RR3'+Keys.TAB)


    def validate_graph_trust_vs_region(self):

        WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//*[name()='svg']//*[name()='g']//*[text()='Trust RR3 vs Region R1']")))
        label_graph = driver.find_element_by_xpath("//*[name()='svg']//*[name()='g']//*[text()='Trust RR3 vs Region R1']")
        label_graph_text = label_graph.text
        print(label_graph_text)
        assert label_graph_text.find("RR3") != -1, "Test Passed"

    def select_graph_trust_vs_peers(self):
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='dv_chart_row_panel']/div[2]/div[2]/a/img")))
        graph_one = driver.find_element_by_xpath("//*[@id='dv_chart_row_panel']/div[2]/div[2]/a/img").click()


    def validate_graph_trust_vs_peers(self):

        WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//*[name()='svg']//*[name()='g']//*[text()='Trust RR3 vs Peers']")))
        label_graph_one=driver.find_element_by_xpath("//*[name()='svg']//*[name()='g']//*[text()='Trust RR3 vs Peers']")
        label_graph_one_text=label_graph_one.text
        print(label_graph_one_text)
        assert label_graph_one_text.find("RR3") != -1, "Label Verified"

    def select_graph_region_vs_peer_region(self):
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='dv_chart_row_panel']/div[2]/div[4]/a/img")))
        driver.find_element_by_xpath("//*[@id='dv_chart_row_panel']/div[2]/div[4]/a/img").click()

    def validate_graph_trust_vs_peer_region(self):
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, "//*[name()='svg']//*[name()='g']//*[text()='Region R1 vs others']")))
        label_graph_two=driver.find_element_by_xpath("//*[name()='svg']//*[name()='g']//*[text()='Region R1 vs others']")
        label_graph_two_text=label_graph_two.text
        print(label_graph_two_text)
        assert label_graph_two_text.find("others") != -1, "Label Verified"





        #label_graph = driver.find_element_by_xpath(read_config.read_element_locator('Home_page','Label_one'))
        #label_graph=label_graph.text
       # print(label_graph.text)
      #  assert label_graph.find("Trust RR3 vs Region R1") != -1, "Test Passed"
    # def read_label_RR1(self):
    #     label_rr1 = driver.find_element_by_xpath(read_config.read_element_locator('Home_Page', 'Label_RR1'))
    #     return label_rr1
    #
    # def read_label_RR8(self):
    #     label_rr8 = driver.find_element_by_xpath(read_config.read_element_locator('Home_Page', 'Label_RR8'))
    #     return label_rr8
    #
    # def read_label_average(self):
    #     label_average = driver.find_element_by_xpath(read_config.read_element_locator('Home_Page', 'Label_Average'))
    #     return label_average
    #
    # def read_label_transition_time(self):
    #     label_transition_time = driver.find_element_by_xpath(read_config.read_element_locator('Home_Page', 'Label_Transition_Time'))
    #     return label_transition_time
    #
    # def read_label_event1(self):
    #     label_e1 = driver.find_element_by_xpath(read_config.read_element_locator('Home_Page', 'Label_E1'))
    #     return label_e1
    #
    # def read_label_event2(self):
    #     label_e2 = driver.find_element_by_xpath(read_config.read_element_locator('Home_Page', 'Label_E2'))
    #     return label_e2
    #
    # def read_label_event3(self):
    #     label_e3 = driver.find_element_by_xpath(read_config.read_element_locator('Home_Page', 'Label_E3'))
    #     return label_e3