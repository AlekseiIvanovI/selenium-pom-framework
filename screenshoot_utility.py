import os
from datetime import datetime

def take_screenshot(driver, name="screenshoot"):
    folder = "screenshoots"
    if not os.path.exists(folder):
        os.makedirs(folder)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filepath = os.path.join(folder, f"{name}-{timestamp}.png")
    driver.save_screenshot(filepath)
    print(f"Screenshot saved to {filepath}")