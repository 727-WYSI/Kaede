import requests
from datetime import datetime

def get_time(city):
    url = f'http://worldtimeapi.org/api/timezone/{city}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        time = datetime.strptime(data['datetime'], '%Y-%m-%dT%H:%M:%S.%f%z')
        return time.strftime('%Y-%m-%d %H:%M:%S')
    return 'Failed to fetch time data'
