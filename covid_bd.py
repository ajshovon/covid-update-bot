import requests
from bs4 import BeautifulSoup

def get_bd_data_24h():

    headers = {
        'authority': 'admin.corona.rultest.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://corona.gov.bd',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://corona.gov.bd/',
        'accept-language': 'en-US,en;q=0.9',
        'dnt': '1',
        'sec-gpc': '1',
    }

    response = requests.get('https://admin.corona.rultest.com/api/statistics/last-24-hours', headers=headers)

    data = response.json()

    infected_last_24_hours = data['infected_last_24_hours']
    recovered_last_24_hours = data['recovered_last_24_hours']
    death_last_24_hours = data['death_last_24_hours']
    tested_last_24_hours = data['tested_last_24_hours']
    infected_per_last_24_hours = "{:.2f}".format(( infected_last_24_hours / tested_last_24_hours ) * 100)

    result_list = [infected_last_24_hours, recovered_last_24_hours, death_last_24_hours, tested_last_24_hours, infected_per_last_24_hours]

    return result_list


def get_bd_data_7days():

    headers = {
        'authority': 'admin.corona.rultest.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://corona.gov.bd',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://corona.gov.bd/',
        'accept-language': 'en-US,en;q=0.9',
        'dnt': '1',
        'sec-gpc': '1',
    }

    response = requests.get('https://admin.corona.rultest.com/api/statistics/last-week', headers=headers)

    data = response.json()

    infected_ = data['infected_last_week']
    recovered_ = data['recovered_last_week']
    death_ = data['death_last_week']
    tested_ = data['tested_last_week']
    infected_per_ = "{:.2f}".format(( int(infected_) / int(tested_) ) * 100)

    result_list = [infected_, recovered_, death_, tested_, infected_per_ ]

    return result_list


def get_bd_data_month():

    headers = {
        'authority': 'admin.corona.rultest.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://corona.gov.bd',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://corona.gov.bd/',
        'accept-language': 'en-US,en;q=0.9',
        'dnt': '1',
        'sec-gpc': '1',
    }

    response = requests.get('https://admin.corona.rultest.com/api/statistics/current-month', headers=headers)

    data = response.json()

    infected_ = data['infected_current_month']
    recovered_ = data['recovered_current_month']
    death_ = data['death_current_month']
    tested_ = data['tested_current_month']
    infected_per_ = "{:.2f}".format(( int(infected_) / int(tested_) ) * 100)

    result_list = [infected_, recovered_, death_, tested_, infected_per_ ]

    return result_list




def get_bd_data_total():

    headers = {
        'authority': 'admin.corona.rultest.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://corona.gov.bd',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://corona.gov.bd/',
        'accept-language': 'en-US,en;q=0.9',
        'dnt': '1',
        'sec-gpc': '1',
    }

    response = requests.get('https://admin.corona.rultest.com/api/statistics/total-data', headers=headers)

    data = response.json()

    infected_ = data['infected_total']
    recovered_ = data['recovered_total']
    death_ = data['death_total']
    tested_ = data['tested_total']
    infected_per_ = "{:.2f}".format(( int(infected_) / int(tested_) ) * 100)

    result_list = [infected_, recovered_, death_, tested_, infected_per_ ]

    return result_list


def get_bd_data_24h_dghs():

    headers = {
        'authority': 'dghs-dashboard.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
        'dnt': '1',
        'sec-gpc': '1',
    }

    page = requests.get('https://dghs-dashboard.com/pages/covid19.php', headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
 
    results_24h = soup.select("body > div.wrapper > div > section > div:nth-child(6) > div.col-md-12.col-print-12 > div.box.box-primary > div.box-body > div > span") 
    res24 = list()

    for res in results_24h:
        res24.append(res.text)
    
    infected_per_ = "{:.2f}".format(( int(res24[1]) / int(res24[0]) ) * 100)

    res24.append(infected_per_)

    result_list = [res24[1], res24[3],res24[4], res24[0], infected_per_ ]

    return result_list