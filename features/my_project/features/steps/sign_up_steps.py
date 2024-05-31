import time
import pathlib
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import sys
import re
from selenium.webdriver.common.alert import Alert
import logging
from os import path
import json


class Base(object):
    def __init__(self):
        super(Base, self).__init__()

    # click the button using label
    @given("I open the Demoblaze home page")
def step_open_home_page(context):
    service = ChromeService(executable_path=ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.implicitly_wait(10)
    context.driver.get("https://www.demoblaze.com/")
    context.driver.maximize_window()

# Sign up steps

@when("I click the Sign up button")
def step_click_sign_up_button(context):
    base_methods.click_button_with_label(context, "Sign up")

    try:
        WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "signInModal"))
        )
        print("Sign up modal appeared successfully.")
    except TimeoutException:
        print("Timed out waiting for sign up modal to appear.")


@when('I enter "{username}" into the username field')
def step_enter_username(context, username):
    base_methods.input_data_with_id(context, username, "sign-username")

    print(f"Entered username: {username}")


@when('I enter "{password}" into the password field')
def step_enter_password(context, password):
    base_methods.input_data_with_id(context, password, "sign-password")

    print(f"Entered password: {password}")


@when("I click the Sign up modal button")
def step_click_sign_up_modal_button(context):
    base_methods.click_button_with_label(context, "Sign up")

    time.sleep(3)


@then("I should see the Sign up modal disappear")
def step_see_modal_disappear(context):
    WebDriverWait(context.driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "signInModal"))
    )
    context.driver.quit()


@then("I accept the alert")
def step_accept_alert(context):
    base_methods.accept_alert(context)

    print("Accepted the alert")

# Additional scenarios for validation messages

@when("I leave the password field empty")
def step_leave_password_empty(context):
    password_field = context.driver.find_element(By.ID, "sign-password")
    password_field.clear()


@then("The Sign up modal should remain visible")
def step_sign_up_modal_visible(context):
    sign_up_modal = context.driver.find_element(By.ID, "signInModal")
    assert sign_up_modal.is_displayed()


@when("I click on a product card")
def step_click_on_product_card(context):
    product_card = context.driver.find_element(By.CLASS_NAME, "card")
    product_card.click()


@then("I should be directed to the product details page")
def step_check_product_details_page(context):
    assert "prod.html" in context.driver.current_url


@when("I view the price of a product")
def step_view_product_price(context):
    product_price = context.driver.find_element(By.CLASS_NAME, "card-title")
    context.product_price = product_price.text


@then("I should see the correct price displayed")
def step_check_correct_price_displayed(context):
    product_details_price = context.driver.find_element(By.ID, "product-price").text
    assert context.product_price == product_details_price


@when("I view the description of a product")
def step_view_product_description(context):
    product_description = context.driver.find_element(By.ID, "article")
    context.product_description = product_description.text


@then("I should see the correct description displayed")
def step_check_correct_description_displayed(context):
    product_details_description = context.driver.find_element(
        By.ID, "product-description"
    ).text
    assert context.product_description == product_details_description


@when("I click on different product categories (e.g., smartphones, laptops)")
def step_click_on_product_categories(context):
    product_categories = context.driver.find_elements(By.CLASS_NAME, "nav-item")
    product_categories[
        0
    ].click()  # Click on smartphones category, change index for other categories


@then("I should be directed to the corresponding category page")
def step_check_category_page(context):
    assert "category.html" in context.driver.current_url


@when("I sort products by price (ascending/descending)")
def step_sort_products_by_price(context):
    sort_dropdown = context.driver.find_element(By.ID, "sort")
    sort_dropdown.click()
    option_asc = context.driver.find_element(
        By.XPATH, "//option[text()='Sort by price: low to high']"
    )
    option_asc.click()


@then("Products should be displayed in the correct price order")
def step_check_price_order(context):
    product_prices = context.driver.find_elements(By.CLASS_NAME, "card-title")
    prices = [price.text for price in product_prices]
    sorted_prices = sorted(prices)
    assert prices == sorted_prices


@when("I search for a product")
def step_search_for_product(context):
    search_input = context.driver.find_element(By.ID, "searchQuery")
    search_input.send_keys("product name")  # Replace with actual product name
    search_button = context.driver.find_element(By.ID, "btnsearch")
    search_button.click()


@then("I should see the search results")
def step_check_search_results(context):
    search_results = context.driver.find_elements(By.CLASS_NAME, "card-title")
    assert len(search_results) > 0
