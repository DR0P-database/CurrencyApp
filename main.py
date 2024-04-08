import uvicorn

from config import *


if __name__ == '__main__':
    uvicorn.run('currency_app.app:app', port=PORT, reload=True)
