# Initiate scraping from OQMD website ..
echo 'Initiating extraction from OQMD ...'
python OQMD_Database_scraper.py

# Execute scraping from periodic table website
echo 'initiating extraction from periodic table'
python scraper_v3.py

