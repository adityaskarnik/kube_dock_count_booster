def run_on_user(ua):
    import os
    from selenium import webdriver
    import time

    chromedriver_path = os.getcwd() + "/chromedriver"
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC

    chrome_options = Options()

    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    chrome_options.add_argument('--log-level=3')

    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("enable-automation")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-browser-side-navigation")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--user-agent="+ua)
    capabilities = {
        'browserName': 'chrome',
        'chromeOptions': {
            'useAutomationExtension': False,
            'forceDevToolsScreenshot': True,
            'args': ['start-maximized', '--disable-infobars']
        }
    }

    driver = webdriver.Chrome(chromedriver_path, desired_capabilities=capabilities, options=chrome_options)
    driver.delete_all_cookies()
    driver.maximize_window()

    for i in range(500):
        link_list = ['https://www.youtube.com/watch?v=oh-BY_G8xGM&list=PLV1HSYr34sqNLZvHxkwB2d3Rg7R7nlnk_',\
                        'https://adityakarnik.com', \
                        'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjlqPCBt7b3AhUIWsAKHT_uCEEQFnoECAIQAQ&url=https%3A%2F%2Fadityakarnik.com%2Fblog%2Fdocker_compose&usg=AOvVaw3A6uicrH7uX6zJsgoz5t9P', \
                        'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiy7Ney-LzyAhWGiVwKHQkUAesQFnoECAQQAQ&url=https%3A%2F%2Fadityakarnik.com%2Fblog%2Fdocker_compose&usg=AOvVaw3A6uicrH7uX6zJsgoz5t9P', \
                        'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiOoazu9bzyAhXRTcAKHX9yAss4ChAWegQIAxAB&url=https%3A%2F%2Fadityakarnik.com%2Fblog%2Fchatbot&usg=AOvVaw03fi3x7hkdWZ2C7o-43Lh1', \
                        'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiqlt2DtLb3AhWKa8AKHY3vCakQFnoECAQQAQ&url=https%3A%2F%2Fadityakarnik.com%2Fblog%2Fchatbot&usg=AOvVaw03fi3x7hkdWZ2C7o-43Lh1', \
                        'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj_yNDItLb3AhWWSEEAHUrGD5cQFnoECAUQAQ&url=https%3A%2F%2Fadityakarnik.com%2Fblog%2Fexception_notifier&usg=AOvVaw0CutRfxD6bV9ipULQ6ECIk', \
                        'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjx4K2k9bzyAhULhVwKHRvcCBs4ChAWegQIERAB&url=https%3A%2F%2Fadityakarnik.com%2F&usg=AOvVaw1JlM6PRcBPlGmkDQCfkSRk', \
                        'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjGxsfg84LzAhVR8OAKHefjADI4HhAWegQIERAB&url=https%3A%2F%2Fadityakarnik.com%2Fblog%2Fexception_notifier&usg=AOvVaw0CutRfxD6bV9ipULQ6ECIk', \
                        'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwia7MuotYb4AhV1zIsBHaspCLYQFnoECAIQAQ&url=https%3A%2F%2Fyoutube.com%2Fchannel%2FUCmyiGTOXvXGnEWf2lmTZ__w&usg=AOvVaw0OK-ptXhLT0TMtAjeDKe6b', \
                        'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=video&cd=&cad=rja&uact=8&ved=2ahUKEwi6sZOZs4b4AhWMSJQKHQkNBvYQtwJ6BAgCEAI&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DlK2CUVXVfXs&usg=AOvVaw2iZ50pcSgcNGICuOXbQ_kp', \
                        'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwia7MuotYb4AhV1zIsBHaspCLYQFnoECAQQAQ&url=https%3A%2F%2Fwww.youtube.com%2Fchannel%2FUCmyiGTOXvXGnEWf2lmTZ__w%2Fvideos&usg=AOvVaw3iMiybldx4jOG9fXliVuvv']
        for link in link_list:
            driver.get(link)
            print("Running" , link)
            time.sleep(1200)
    driver.quit()


import pandas as pd
df = pd.read_excel("user-agents.xlsx")
for i in df['USER_AGENT']:
    run_on_user(i)