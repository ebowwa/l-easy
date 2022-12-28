import selenium
from selenium import webdriver

def scrape_jobs(config):
    """
    Logs into LinkedIn, navigates to the job search page, and extracts the job listings from the search results.

    Parameters:
        config (dict): A dictionary containing the login credentials and search filters for the job search.

    Returns:
        list: A list of dictionaries, each containing the job ID, company name, job title, location, description, and URL for a specific job.
    """
    # Set up webdriver and log into LinkedIn
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/login")
    username_element = driver.find_element_by_id("username")
    username_element.send_keys(config["login"]["username"])
    password_element = driver.find_element_by_id("password")
    password_element.send_keys(config["login"]["password"])
    password_element.submit()

    # Navigate to the job search page and enter the search filters
    driver.get("https://www.linkedin.com/jobs/")
    keywords_element = driver.find_element_by_id("jobs-search-box-keyword-id-ember39")
    keywords_element.send_keys(config["search"]["keywords"])
    location_element = driver.find_element_by_id("jobs-search-box-location-id-ember39")
    location_element.send_keys(config["search"]["location"])
    location_element.submit()

     # Extract the job listings from the search results
    job_listings = []
    while True:
        # Extract the job data from each listing on the page
        listings = driver.find_elements_by_css_selector(".job-card-container")
        for listing in listings:
            job_data = {}
            # Extract the job ID
            job_id_element = listing.find_element_by_css_selector(".job-card-container__job-id")
            job_data["id"] = job_id_element.text
            # Extract the company name
            company_element = listing.find_element_by_css_selector(".job-card-container__company-name")
            job_data["company"] = company_element.text
            # Extract the job title
            title_element = listing.find_element_by_css_selector(".job-card-container__title")
            job_data["title"] = title_element.text
            # Extract the job location
            location_element = listing.find_element_by_css_selector(".job-card-container__location")
            job_data["location"] = location_element.text
            # Extract the job description
            description_element = listing.find_element_by_css_selector(".job-card-container__description")
            job_data["description"] = description_element.text
            # Extract the job URL
            url_element = listing.find_element_by_css_selector(".job-card-container__link")
            job_data["url"] = url_element.get_attribute("href")
            # Add the job data to the list of job listings
            job_listings.append(job_data)

        # Check if the "Load more jobs" button is present
        load_more_button = driver.find_elements_by_css_selector(".jobs-search-results__load-more-button")
        if not load_more_button:
            break
        # Click the "Load more jobs" button to load the next page of results
        load_more_button[0].click()

    # Return the list of job listings
    return job_listings
