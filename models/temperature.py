# Importa las bibliotecas necesarias
from django.shortcuts import render
from django.views import View
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.http import JsonResponse
import json
import re


driver = webdriver.Chrome()
driver.get("https://wokwi.com/projects/375043962406971393")
start_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Start the simulation']"))
)
start_button.click()

def get_latest_wokwi_data():
    logs = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "serial-monitor_monitorContainer__L2dnu"))
    )
    data = logs.text
    data_lines = data.split('\n')
    latest_data = data_lines[-1] if data_lines else ''

    return latest_data


class WokwiDataViewTemperature(View):
    def get(self, request):
        latest_wokwi_data = get_latest_wokwi_data()
        data_string = latest_wokwi_data
        input_string = data_string
        pattern = r'(\w+):\s([\d.]+)'
        matches = re.findall(pattern, input_string)
        result = {}
        for match in matches:
            prop_name = match[0]
            prop_value = float(match[1])
            result[prop_name] = prop_value


        json_result = json.dumps(result, indent=4)
        return JsonResponse(result)
