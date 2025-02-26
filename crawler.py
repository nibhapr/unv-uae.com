import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import re
from collections import deque
import argparse
import logging


class WebCrawler:
    def __init__(self, base_url, output_file="urls.txt", delay=1):
        self.base_url = base_url
        self.domain = urlparse(base_url).netloc
        self.output_file = output_file
        self.delay = delay
        self.visited_urls = set()
        self.queue = deque([base_url])

        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

        # Headers to mimic a browser
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }

    def is_valid_url(self, url):
        """Check if URL is valid and belongs to the same domain"""
        try:
            parsed = urlparse(url)
            return bool(parsed.netloc) and parsed.netloc == self.domain
        except Exception:
            return False

    def clean_url(self, url):
        """Clean URL by removing fragments and query parameters"""
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

    def get_urls_from_page(self, url):
        """Extract all URLs from a webpage"""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            urls = set()

            # Find all <a> tags with href
            for link in soup.find_all('a', href=True):
                href = link['href']
                absolute_url = urljoin(url, href)
                urls.add(absolute_url)  # Save all URLs without domain filtering

            return urls

        except Exception as e:
            logging.error(f"Error fetching {url}: {str(e)}")
            return set()

    def crawl(self):
        """Main crawling method"""
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                url = self.base_url
                logging.info(f"Crawling: {url}")

                # Get URLs from the single page
                urls = self.get_urls_from_page(url)

                # Write URLs to file
                for url in urls:
                    f.write(f"{url}\n")

                logging.info(f"Crawling completed. Found {len(urls)} URLs")
                logging.info(f"Results saved to {self.output_file}")

        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")


def main():
    parser = argparse.ArgumentParser(
        description='Web Crawler for extracting URLs from a domain')
    parser.add_argument(
        'url', help='Base URL to start crawling (e.g., https://example.com)')
    parser.add_argument('--output', default='urls.txt',
                        help='Output file name (default: urls.txt)')
    parser.add_argument('--delay', type=float, default=1.0,
                        help='Delay between requests in seconds (default: 1.0)')

    args = parser.parse_args()

    crawler = WebCrawler(args.url, args.output, args.delay)
    crawler.crawl()


if __name__ == "__main__":
    main()
