import configparser


def read_config_data(key,value):
    config=configparser.ConfigParser()
    config.read('../configuration_files/TestConfigurations.cnf')
    return config.get(key,value)


def read_element_locator(key,value):
    config=configparser.ConfigParser()
    config.read('../configuration_files/ElementLocators.cnf')
    return config.get(key,value)