import selenium
from selenium import webdriver

def apply_to_jobs(config, job_listings):
    """
    Applies to a list of jobs on LinkedIn.

    Parameters:
        config (dict): A dictionary containing the login credentials, application materials, and contact information for the job application.
        job_listings (list): A list of dictionaries, each containing the job ID, company name, job title, location, description, and URL for a specific job.

    Returns:
        None
    """
    # Set up webdriver and log into LinkedIn
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/login")
    username_element = driver.find_element_by_id("username")
    username_element.send_keys(config["login"]["username"])
    password_element = driver.find_element_by_id("password")
    password_element.send_keys(config["login"]["password"])
    password_element.submit()

    # Iterate through the job listings and apply to each job
    for job in job_listings:
        # Navigate to the job listing page
        driver.get(job["url"])
        # Click the "Apply now" button
        apply_button = driver.find_elements_by_css_selector(".jobs-apply-button")
        apply_button[0].click()
          # Wait for the application form to load
        apply_form = driver.find_elements_by_css_selector(".jobs-apply-form")
        while not apply_form:
            apply_form = driver.find_elements_by_css_selector(".jobs-apply-form")
        # Upload the cover letter and resume
        cover_letter_element = driver.find_element_by_id("cover-letter-upload-input")
        cover_letter_element.send_keys(config["application"]["cover_letter"])
        resume_element = driver.find_element_by_id("resume-upload-input")
        resume_element.send_keys(config["application"]["resume"])
        # Submit the application
        submit_button = driver.find_element_by_css_selector(".jobs-apply-form__submit-button")
        submit_button.click()
        # Wait for the confirmation page to load
        confirmation_page = driver.find_elements_by_css_selector(".jobs-apply-success__title")
        while not confirmation_page:
            confirmation_page = driver.find_elements_by_css_selector(".jobs-apply-success__title")
        # Click the apply button
        apply_button = driver.find_elements_by_css_selector(".jobs-apply-success__apply-button")
        apply_button[0].click()
        # Wait for the application form to load
        apply_form = driver.find_elements_by_css_selector(".jobs-apply-form")
        while not apply_form:
            apply_form = driver.find_elements_by_css_selector(".jobs-apply-form")
        # Fill out the form with the contact information
        email_element = driver.find_element_by_id("email")
        email_element.send_keys(config["contact"]["email"])
        phone_element = driver.find_element_by_id("phone")
        phone_element.send_keys(config["contact"]["phone"])
        # Upload the resume again
        resume_element = driver.find_element_by_id("resume-upload-input")
        resume_element.send_keys(config["application"]["resume"])
        # Submit the application
        submit_button = driver.find_element_by_css_selector(".jobs-apply-form__submit-button")
        submit_button.click()
        # Wait for the confirmation page to load
        confirmation_page = driver.find_elements_by_css_selector(".jobs-apply-success__title")
        while not confirmation_page:
            confirmation_page = driver.find_elements_by_css_selector(".jobs-apply-success__title")
    # Close the webdriver
    driver.close()

