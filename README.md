# Selenium Scraper with Login Automation

This repository contains a Python script that uses **Selenium** to scrape content from a website, including handling login functionality. It automates the login process using the "Se connecter" button and extracts key information such as images, headings, links, paragraphs, and the meta description.

## Features

- **Login Automation**: The script automates logging into a website by clicking the "Se connecter" button and submitting the login credentials (username and password).
- **Content Extraction**: The scraper extracts the following content from the page:
  - Title of the page
  - Meta description
  - All images
  - All paragraphs
  - All headings (h1, h2, h3, etc.)
  - All links
  - Full body text of the page
- **Headless Mode**: Runs the script in headless mode (without opening the browser window) for faster execution.

## Prerequisites

Before running the script, you need to have the following Python packages installed:

- `selenium`
- `webdriver-manager`
- `beautifulsoup4`
- `time`

You can install the required dependencies by running the following command:

```bash
pip install selenium webdriver-manager beautifulsoup4
