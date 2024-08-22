import requests
from bs4 import BeautifulSoup
import streamlit as st


class WebScraper:
    def __init__(self):
        pass

    def scrape(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.find_all("a")
            return [link.get("href") for link in links]
        else:
            return []


def main():
    st.title("Web Scraper with Streamlit")
    scraper = WebScraper()

    option = st.radio(
        "Choose an option:", ["Enter a custom URL", "Use a predefined URL"]
    )

    if option == "Enter a custom URL":
        custom_url = st.text_input("Enter the URL you want to scrape:")
        if st.button("Scrape"):
            if custom_url:
                scraped_links = scraper.scrape(custom_url)
                if scraped_links:
                    st.header("Scraped Links:")
                    for link in scraped_links:
                        st.write(link)

                    # Add functionality to store and download the data
                    if st.button("Download Data"):
                        with open("scraped_links.txt", "w") as file:
                            for link in scraped_links:
                                file.write(link + "\n")
                        st.success("Data has been saved and is ready for download.")
                        st.download_button(
                            label="Download Scraped Data",
                            data="\n".join(scraped_links),
                            file_name="scraped_links.txt",
                            mime="text/plain",
                        )
                else:
                    st.warning("No links were scraped.")
            else:
                st.warning("Please enter a valid URL.")
    elif option == "Use a predefined URL":
        predefined_url = "https://example.com"  # Replace with your predefined URL
        if st.button("Scrape predefined URL"):
            scraped_links = scraper.scrape(predefined_url)
            if scraped_links:
                st.header("Scraped Links:")
                for link in scraped_links:
                    st.write(link)

                # Add functionality to store and download the data
                if st.button("Download Data"):
                    with open("scraped_links.txt", "w") as file:
                        for link in scraped_links:
                            file.write(link + "\n")
                    st.success("Data has been saved and is ready for download.")
                    st.download_button(
                        label="Download Scraped Data",
                        data="\n".join(scraped_links),
                        file_name="scraped_links.txt",
                        mime="text/plain",
                    )
            else:
                st.warning("No links were scraped.")


# streamlit run web_app_strmlit.py
if __name__ == "__main__":
    main()
