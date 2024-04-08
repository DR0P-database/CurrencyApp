from fastapi import APIRouter

from config import *
from ..modules.app_module import *


router = APIRouter()


@router.get('/info/{service}')
async def get_info_revice(service, currency: str = None, date: str = None):
    date = date_refactor(date)
    return {
        'data': await parse_data(currency, date),
        'date': date
    }
