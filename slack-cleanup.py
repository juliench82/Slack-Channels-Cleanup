import time
import os
from dotenv import load_dotenv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

load_dotenv()  # Environment variables

firefox_profile_path = os.getenv("firefox_profile_path")
csv_file_path = os.getenv("csv_file_path")
slack_workspace_url = os.getenv("slack_workspace_url")

# Firefox options and profile path
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('-profile')
firefox_options.add_argument(firefox_profile_path)

# Initialize Firefox with options
driver = webdriver.Firefox(options=firefox_options)

# Slack URL
driver.get(slack_workspace_url)

time.sleep(3)

# CSV file with channel names to archive
channels_to_delete = pd.read_csv(csv_file_path)['channelName'].tolist()

# Function to update the CSV file
def update_csv(channel_list):
    pd.DataFrame(channel_list, columns=['channelName']).to_csv(csv_file_path, index=False)
    print('Updated CSV file.')

# Function to keep awake
def keep_awake():
    current_position = pyautogui.position()
    pyautogui.moveTo(current_position[0] + 1, current_position[1] + 1)
    pyautogui.moveTo(current_position)
    print('Simulated mouse movement to keep system awake.')

# Iterate through channels and delete
for channelName in channels_to_delete.copy():  # Using a copy to iterate safely while modifying the original list
    try:
        # Clear the search input field
        search_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-qa="data_table_header-search_input"]'))
        )
        search_input.clear()

        # Enter the channel name in the search field
        search_input.send_keys(channelName)
        time.sleep(1)  # Wait for results to update

        try:
            # Check if the channel's options button is available
            ellipsis_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'//button[@aria-label="Actions for {channelName}"]'))
            )
            ellipsis_button.click()
            print(f'Opened menu for channel: {channelName}')

            time.sleep(1)  # Wait for the options menu to appear

            # Click on the "Delete" option
            delete_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="channel_mgmt_menu_item__delete"]'))
            )
            delete_button.click()
            print('Clicked "Delete channel" button.')

            time.sleep(1)

            # Confirm the delete action
            confirm_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="channel_mgmt_delete_modal_go_btn"]'))
            )
            confirm_button.click()
            print('Clicked "Confirm" button in confirmation modal.')

            # Wait for the modal to disappear and the channel to be deleted
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, 'button[data-qa="channel_mgmt_delete_modal_go_btn"]'))
            )
            print(f'Successfully deleted channel: {channelName}')
        
        except Exception as delete_exception:
            print(f'Channel {channelName} not found or could not be deleted: {delete_exception}')
        
        # Remove the channel from the list and update the CSV
        channels_to_delete.remove(channelName)
        update_csv(channels_to_delete)
        print(f'Removed {channelName} from the CSV file.')

        # Keep the system awake
        keep_awake()

        time.sleep(1)

    except Exception as e:
        print(f'Error processing channel {channelName}: {e}')

# Close when done
driver.quit()
