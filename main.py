import json

from scraper import scrape_jobs
from applicator import apply_to_jobs

def main():
    # Read the config file
    with open("config.json") as f:
        config = json.load(f)
    # Scrape the job listings
    job_listings = scrape_jobs(config)
    # Apply to the jobs
    apply_to_jobs(config, job_listings)

if __name__ == "__main__":
    main()
