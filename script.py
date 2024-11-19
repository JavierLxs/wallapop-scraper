from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from redmail import EmailSender

from function import *

# Define the path to the Firefox Geckodriver:
geckodriver_path = '/home/jari/geckodriver'

# Set up the Firefox WebDriver with options:
options = Options()
options.add_argument('-headless')

# ------------------------------------------------------------
# Section 1: Create list of URLs
# ------------------------------------------------------------

# Alfa Romeo GTV:
url_gtv = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&min_horse_power=130&min_year=1974&max_year=1986&min_sale_price=200&max_sale_price=4000&brand=Alfa Romeo&category_ids=100&filters_source=default_filters&keywords=GTV"

# BMW E30:
url_e30 = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&max_km=320000&min_horse_power=100&max_horse_power=195&min_year=1982&max_year=1994&min_sale_price=200&max_sale_price=4000&max_num_doors=3&engine=gasoline&brand=BMW&model=Serie 3&category_ids=100"

# Documentación alemana:
url_doc_de = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&max_km=300000&min_sale_price=200&max_sale_price=8000&category_ids=100&filters_source=default_filters&keywords=documentacion alemana"
url_pap_de = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&max_km=300000&min_sale_price=200&max_sale_price=8000&category_ids=100&filters_source=default_filters&keywords=documentacion alemana"

# MB 190:
url_190 = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&max_km=300000&min_horse_power=115&min_year=1982&max_year=1993&min_sale_price=200&max_sale_price=3000&engine=gasoline&brand=Mercedes Benz&category_ids=100&filters_source=default_filters&keywords=190"

# MB SL:
url_sl = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&max_km=300000&max_year=2011&min_sale_price=200&max_sale_price=8000&brand=Mercedes-Benz&model=SL&category_ids=100"

# MB W123 TE:
url_w123_te = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&min_horse_power=125&min_year=1975&max_year=1984&min_sale_price=200&max_sale_price=10000&engine=gasoline&brand=Mercedes-Benz&category_ids=100&filters_source=default_filters&keywords=TE"

# MB W124:
url_w124 = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&max_km=300000&min_horse_power=160&min_year=1984&max_year=1995&min_sale_price=200&max_sale_price=5000&engine=gasoline&brand=Mercedes Benz&category_ids=100&filters_source=default_filters"

# Porsche 944:
url_944 = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&max_year=1991&min_sale_price=200&max_sale_price=5000&brand=Porsche&category_ids=100&keywords=944"

# Saab 900:
url_900 = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&max_km=300000&min_horse_power=140&max_year=1993&min_sale_price=200&max_sale_price=5000&max_num_doors=3&brand=Saab&category_ids=100&keywords=900"

# VW Golf 1:
url_golf1 = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&max_year=1983&min_sale_price=100&max_sale_price=2000&engine=gasoline&brand=Volkswagen&model=Golf&category_ids=100"

# VW Golf Country:
url_golf2_country = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&max_year=1992&max_sale_price=6000&brand=Volkswagen&model=Golf&keywords=country&category_ids=100&filters_source=default_filters"

## VW Golf 2 GTI:
url_golf2_gti = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&max_km=320000&min_horse_power=110&max_horse_power=200&max_year=1992&max_sale_price=3000&engine=gasoline&brand=Volkswagen&model=Golf&category_ids=100&filters_source=default_filters"
url_golf2_16v = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&max_km=320000&min_horse_power=120&max_horse_power=200&max_year=1992&max_sale_price=5000&engine=gasoline&brand=Volkswagen&model=Golf&category_ids=100&filters_source=default_filters"

# VW Golf 3 GTI 16V Jubi:
url_golf3_16v_jubi = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&max_km=320000&min_horse_power=145&max_horse_power=155&min_year=1991&max_year=1997&max_sale_price=5000&brand=Volkswagen&model=Golf&category_ids=100&keywords=aniversario"

# VW Scirocco MK1:
url_scirocco = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&max_year=1981&min_sale_price=200&max_sale_price=4000&brand=Volkswagen&model=Scirocco&category_ids=100"

# VW T4 TDI:
url_t4_tdi = "https://wallapop.com/app/search?time_filter=today&latitude=43.0120963&longitude=-7.5558311&min_horse_power=100&max_horse_power=110&min_year=1990&max_year=2002&min_sale_price=200&max_sale_price=1500&engine=gasoil&brand=Volkswagen&model=Transporter&category_ids=100"


# List with all variables starting with "url_". Commented variables will not be added.
urls = [value for key, value in globals().items() if key.startswith('url_')]

# ------------------------------------------------------------
# Section 2: Extract data
# ------------------------------------------------------------

ads_today = []

# Loop through URLs and extend the list with the ads from each URL
for url in urls:
    ads_today.extend(wallapop_search(url,geckodriver_path))

# ------------------------------------------------------------
# Section 3: Send e-mail with results
# ------------------------------------------------------------

# Configure your email server settings:
email = EmailSender(
    host='smtp.gmail.com',
    port=587,
    username='sender@gmail.com', #email address from which the message will be sent
    password='sender_mail_pwd', #16-character gmail app password for sender@gmail.com
                                #or equivalent for other email providers
    use_starttls=True
)

# Check if ads_heute list is not empty
if ads_today:

    # Transform list into string format
    urls_html = "".join(f'<li><a href="{url}">{title}</a></li>' for title, url in ads_today)

    # Specify the email details and send
    email.send(
        subject="Wallapop Results",
        sender="sender@gmail.com",
        receivers=["receiver@gmail.com"], #email address to which the message will be sent
        html=f"<h1>The following ads have been found today:</h1><ul>{urls_html}</ul>"
    )

    print("Email sent successfully.")

else:
    print("No ads found for today, no email sent.")
