
# Web Scraper with Streamlit

## Overview

This project is a web scraping tool built with Python and Streamlit. It allows users to scrape hyperlinks from web pages and download the scraped data. The tool offers both a custom URL input option and a predefined URL option, making it versatile and user-friendly.

## Features

- **Custom URL Scraping**: Input any URL to scrape hyperlinks from that webpage.
- **Predefined URL Scraping**: Use a predefined URL to quickly scrape data without needing to input it.
- **Interactive User Interface**: Built with Streamlit, offering an easy-to-use web interface.
- **Downloadable Data**: Save and download the scraped data in a text file format.

## Installation

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org/).
- **pip**: Python package installer should be installed. It comes pre-installed with Python.

### Required Python Libraries

Install the required libraries using pip:

```bash
pip install requests beautifulsoup4 streamlit
```

## Project Structure

```
web_scraper_app/
    └── web_scraper_app.py
```

- **web_scraper_app.py**: The main Python script containing the web scraper logic and Streamlit integration.

## Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/asavoullis/web_scraper_app.git
   cd web_scraper_app
   ```

2. **Run the Streamlit Application**:

   ```bash
   streamlit run web_scraper_app.py
   ```

3. **Interact with the Application**:

   - Choose between entering a custom URL or using a predefined one.
   - Click "Scrape" to extract hyperlinks from the webpage.
   - Optionally, download the scraped data as a text file.

## Example

To scrape data from a custom URL:

1. Choose "Enter a custom URL".
2. Input the URL of the webpage you want to scrape.
3. Click "Scrape" to see the list of hyperlinks.
4. Click "Download Data" to save the links to a file.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements, bug fixes, or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
