import uvicorn

from config import PORT


if __name__ == '__main__':
    uvicorn.run('currency_app.app:app', port=PORT, host='0.0.0.0', reload=True)
