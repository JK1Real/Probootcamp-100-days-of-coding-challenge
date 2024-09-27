from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def rgba_to_color_name(color):
    color_names = {
        "rgba(0, 0, 0, 1)": "black",
        "rgba(255, 255, 255, 1)": "white",
        "rgba(238, 238, 238, 1)": "white",
        "rgba(128, 128, 128, 1)": "grey",
        "rgba(102, 102, 102, 1)": "grey",  # Add the specific shade of grey from your example
        # Add more colors as needed
    }
    
    # Find the color name based on the RGBA tuple
    return color_names.get((color), "unknown")



chromeOptions = ChromeOptions()
chromeOptions.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chromeOptions)

url = "https://orteil.dashnet.org/experiments/cookie/"



driver.get(url=url)

cook = driver.find_element(by=By.ID, value="cookie")


money = driver.find_element(by=By.ID, value="money")
print(money.text)


colors=[]
objects = []

values= ["#buyCursor", "#buyGrandma", "#buyFactory", "#buyMine", "#buyShipment", "#buyAlchemy lab", "#buyPortal", "#buyTime machine"]
ids = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime machine"]




start_time = time.time()
print(start_time)

while time.time() - start_time<300:
        objects=[]
        colors = []
        amounts=[]

        try:
            for i,j in zip(values, ids):
                objs = driver.find_element(by=By.CSS_SELECTOR, value=i.replace(" ",r"\ "))
                objects.append(objs)
                color = objs.value_of_css_property("background-color")
                colors.append(rgba_to_color_name(color=color))
                try:
                    xpath = f'//*[@id="{j}"]/div'
                    amount = driver.find_element(by=By.XPATH, value=xpath)
                    
                    amount = int(amount.text)
                except:
                    amount=0
                amounts.append(amount)
            print(colors)
            print(amounts)
            for i in range(0,15):
                 cook.click()
            for color in colors[::-1]:
                print(f"{color},{colors}")
                no = colors[::-1].index(color)
                print(no)
                value=7-int(no)
                print(value)

                amount = amounts[value]
                print(amount)
                if color=='white' and amount<8:
                    print("hello")      
                    objects[value].click()
            
        except :
            pass

cookies_seconds = driver.find_element(by=By.ID, value="#cps")
print(cookies_seconds.text.split(":")[-1])
