import datetime
import requests
import xml.etree.ElementTree as ET
import aiohttp
import ssl
from fastapi import HTTPException

from config import *


def date_refactor(date: str | None) -> str:
    if date is None:
        date = datetime.datetime.now()
    else:
        date_format = '%Y-%m-%d'
        try:
            date = datetime.datetime.strptime(date, date_format)
        except:
            raise HTTPException(
                status_code=429, detail='Unprocessable date entity')

    date = date.strftime('%d/%m/%Y')
    return date


def request_data(uri: str, date: str) -> str:
    params = {'date_req': date}
    request = requests.get(uri, params=params)
    return request.text


async def request_data_async(uri: str, date: str) -> str:
    async with aiohttp.ClientSession() as session:
        params = {'date_req': date}
        async with session.get(uri, params=params, ssl=ssl.SSLContext()) as response:
            return await response.text()


async def parse_data(currency: str | None, date: str) -> dict:
    '''Парсинг XML-файла получение JSON валют'''
    data = {}
    try:
        root = ET.fromstring(await request_data_async(URI, date))
    except:
        return {'message': '[ERROR] request unavailable'}

    for valute in root.findall('Valute'):
        char_code = valute.find('CharCode').text
        if currency is None or char_code == currency:
            value = float(valute.find('Value').text.replace(',', '.'))
            data[char_code] = value

    return data
