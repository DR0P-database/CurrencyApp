from fastapi import APIRouter

from config import *

router = APIRouter()


@router.get('/info')
async def get_info():
    return {
        'version': VERSION,
        'service': SERVICE,
        'author': 'a.ukhanov'
    }
