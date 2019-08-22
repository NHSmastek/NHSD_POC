from library_files import read_config

class LoginPageClass:

    def __init__(self,obj):
        global driver
        driver=obj

        @property
        def drive(self):
            return driver

    def enter_login(self,login_cred):

      driver.find_element_by_xpath(read_config.read_element_locator('Login_page', 'txt_User_Name')).send_keys(login_cred)

    def enter_password(self,password):
      driver.find_element_by_xpath(read_config.read_element_locator('Login_page', 'txt_Password')).send_keys(password)

    def btn_clk_login(self):
      driver.find_element_by_xpath(read_config.read_element_locator('Login_page', 'btn_login')).click()
      label_welcome = driver.find_element_by_xpath(read_config.read_element_locator('Login_page', 'Label_Hello_Admin'))
      label_welcome_text = label_welcome.text
      #print(label_welcome_text)
      #print('Hello')
      #assert label_welcome_text.find("Hello admin")

    def validate_home_page(self):

      label_welcome = driver.find_element_by_xpath(read_config.read_element_locator('Login_page','Label_Hello_Admin'))
      label_welcome_text = label_welcome.text
      print(label_welcome_text)
      assert label_welcome_text.find("Hello") != -1,"Test Passed"


