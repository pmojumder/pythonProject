import configparser

def get_credentials():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\Plabani\\PycharmProjects\\pythonProject\\features\\config.ini')
    username = config.get('credentials', 'username')
    password = config.get('credentials', 'password')
    return username, password
