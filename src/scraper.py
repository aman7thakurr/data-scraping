from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # WebDriver Manager
from bs4 import BeautifulSoup
import time

class SeleniumScraper:
    def __init__(self):
        pass

    def fetch_content(self, url):
        try:
            # Automatically download and set up ChromeDriver using WebDriver Manager
            chrome_service = Service(ChromeDriverManager().install())  # WebDriver Manager handles this
            options = Options()
            options.headless = True  # Run headless (without opening a browser window)

            driver = webdriver.Chrome(service=chrome_service, options=options)
            driver.get(url)

            time.sleep(5)  # Allow time for JavaScript to load content
            page_source = driver.page_source
            driver.quit()  # Close the browser window

            return page_source
        except Exception as e:
            print(f"Error fetching content: {e}")
            return None

    def parse_content(self, html):
        if not html:
            return {'error': 'No content to parse'}

        soup = BeautifulSoup(html, 'html.parser')

        # Extract title of the page
        title = soup.title.string if soup.title else 'No title found'

        # Extract meta description if available
        meta_description = soup.find('meta', attrs={'name': 'description'})
        description = meta_description['content'] if meta_description else 'No meta description available'

        # Extract all images
        images = [img['src'] for img in soup.find_all('img', src=True)]

        # Extract all paragraph text
        paragraphs = [p.get_text() for p in soup.find_all('p')]

        # Extract all headings (h1, h2, h3, etc.)
        headings = {f'h{i}': [h.get_text() for h in soup.find_all(f'h{i}')] for i in range(1, 7)}

        # Extract all links (anchor tags with href)
        links = [a['href'] for a in soup.find_all('a', href=True)]

        # Extract other text content (all text within body)
        body_text = soup.get_text()

        # Return structured data
        return {
            'title': title,
            'description': description,
            'images': images,
            'paragraphs': paragraphs,
            'headings': headings,
            'links': links,
            'body_text': body_text,
            'html': html,  # Store raw HTML if needed for debugging
        }

    def scrape(self, url):
        html = self.fetch_content(url)
        if html:
            return self.parse_content(html)
        else:
            return {'error': f"Failed to scrape {url}"}

# Example usage:
if __name__ == "__main__":
    scraper = SeleniumScraper()

    url = 'https://www.utopya.fr/vitre-arriere-complete-titane-sable-iphone-16-pro-avec-magsafe-sans-logo.html'
    scraped_data = scraper.scrape(url)

    if 'error' not in scraped_data:
        print(f"Title: {scraped_data['title']}")
        print(f"Description: {scraped_data['description']}")
        print(f"Images: {scraped_data['images'][:5]}")  # Print first 5 image URLs
        print(f"Paragraphs: {scraped_data['paragraphs'][:5]}")  # Print first 5 paragraphs
        print(f"Headings: {scraped_data['headings']}")
        print(f"Links: {scraped_data['links'][:5]}")  # Print first 5 links
        print(f"Body Text: {scraped_data['body_text'][:500]}...")  # Print the first 500 characters of body text
    else:
        print(scraped_data['error'])
