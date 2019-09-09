import configparser


def read_config_data(key,value):

    #read test configuration file
    config=configparser.ConfigParser()
    #Uncomment the respective paths based on Windows or Linux execution
    #config.read('../configuration_files/TestConfigurations.cnf')
    config.read('/var/lib/jenkins/workspace/NHSD_POC/NHS.Automation/FrameworkPython/configuration_files/TestConfigurations.cnf')
    return config.get(key,value)


def read_element_locator(key,value):
    #read element configuration file
    config=configparser.ConfigParser()
    #Uncomment the respective paths based on Windows or Linux execution
    #config.read('../configuration_files/ElementLocators.cnf')
    config.read('/var/lib/jenkins/workspace/NHSD_POC/NHS.Automation/FrameworkPython/configuration_files/ElementLocators.cnf')

    return config.get(key,value)