import time

from behave import given, then, when
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


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
    sign_up_button = context.driver.find_element(By.ID, "signin2")
    sign_up_button.click()
    try:
        WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "signInModal"))
        )
        print("Sign up modal appeared successfully.")
    except TimeoutException:
        print("Timed out waiting for sign up modal to appear.")


@when('I enter "{username}" into the username field')
def step_enter_username(context, username):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "sign-username"))
    )
    username_field = context.driver.find_element(By.ID, "sign-username")
    username_field.clear()
    username_field.send_keys(username)
    print(f"Entered username: {username}")


@when('I enter "{password}" into the password field')
def step_enter_password(context, password):
    password_field = context.driver.find_element(By.ID, "sign-password")
    password_field.clear()
    password_field.send_keys(password)
    print(f"Entered password: {password}")


@when("I click the Sign up modal button")
def step_click_sign_up_modal_button(context):
    sign_up_modal_button = context.driver.find_element(
        By.XPATH, '//button[@onclick="register()"]'
    )
    sign_up_modal_button.click()
    time.sleep(3)


@then("I should see the Sign up modal disappear")
def step_see_modal_disappear(context):
    WebDriverWait(context.driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "signInModal"))
    )
    context.driver.quit()


@then("I accept the alert")
def step_accept_alert(context):
    alert = context.driver.switch_to.alert
    alert.accept()
    print("Accepted the alert")


# Login steps


@when("I navigate to the login page")
def step_navigate_to_login_page(context):
    login_link = context.driver.find_element(By.ID, "login2")
    login_link.click()


@when('I enter the registered "{username}" and "{password}"')
def step_enter_registered_credentials(context, username, password):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "logInModal"))
    )
    username_field = context.driver.find_element(By.ID, "loginusername")
    username_field.clear()
    username_field.send_keys(username)
    print(f"Entered login username: {username}")

    password_field = context.driver.find_element(By.ID, "loginpassword")
    password_field.clear()
    password_field.send_keys(password)
    print(f"Entered login password: {password}")


@when("I click the Log in modal button")
def step_click_log_in_modal_button(context):
    log_in_modal_button = context.driver.find_element(
        By.XPATH, '//button[@onclick="logIn()"]'
    )
    log_in_modal_button.click()
    time.sleep(3)


@then("I should be successfully logged in")
def step_check_successful_login(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "nameofuser"))
    )
    user_dashboard = context.driver.find_element(By.ID, "nameofuser")
    assert user_dashboard.is_displayed()
    print("Successfully logged in")


# Additional scenarios for validation messages


@then("I should see an alert message indicating the username is already taken")
def step_see_username_taken_alert(context):
    alert_message = context.driver.switch_to.alert
    assert alert_message.text == "Username already exists! Please choose another one."
    alert_message.accept()


@then("I should see an alert message indicating the password is invalid")
def step_see_invalid_password_alert(context):
    alert_message = context.driver.switch_to.alert
    assert alert_message.text == "Password is invalid! Please choose another one."
    alert_message.accept()


@then("I should see alert messages indicating both fields are required")
def step_see_required_fields_alert(context):
    alert_messages = context.driver.find_elements(By.CLASS_NAME, "alert-danger")
    assert len(alert_messages) == 2
    assert alert_messages[0].text == "Username is required!"
    assert alert_messages[1].text == "Password is required!"


@when("I enter an existing username into the username field")
def step_enter_existing_username(context):
    username_field = context.driver.find_element(By.ID, "sign-username")
    username_field.clear()
    username_field.send_keys("existing_user")


@when("I enter a valid password into the password field")
def step_enter_valid_password(context):
    password_field = context.driver.find_element(By.ID, "sign-password")
    password_field.clear()
    password_field.send_keys("valid_password")


@when("I enter an invalid password into the password field")
def step_enter_invalid_password(context):
    password_field = context.driver.find_element(By.ID, "sign-password")
    password_field.clear()
    password_field.send_keys("invalid")


@when("I leave the username field empty")
def step_leave_username_empty(context):
    username_field = context.driver.find_element(By.ID, "loginusername")
    username_field.clear()


@when("I leave the password field empty")
def step_leave_password_empty(context):
    password_field = context.driver.find_element(By.ID, "loginpassword")
    password_field.clear()


@then("The Log in modal should remain visible")
def step_log_in_modal_visible(context):
    login_modal = context.driver.find_element(By.ID, "logInModal")
    assert login_modal.is_displayed()


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
