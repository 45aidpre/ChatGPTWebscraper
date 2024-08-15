import time
import random
import requests


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC

import undetected_chromedriver as uc

from ChatGPTScraper import ChatGpt
from unitTests.loginTests import LoginTests
from unitTests.invalidTests import InvalidTests
from unitTests.unethicalTests import UnethicalTests
from unitTests.calculationTests import CalculationTests
from unitTests.longMemoryTests import LongMemoryTests
from unitTests.translationTests import TranslationTests
from unitTests.gptPlusTests import GptPlusTests
from unitTests.basicTests import BasicTests

def test1234():

    basicTestBot = BasicTests()

    basicTestBot.test_single()

