from app import app
from libs.logger import logger

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 5000
    try:
        app.run(host=HOST, port=PORT, debug=True)
        logger.info('Server start success!')
    except Exception as e:
        logger.error(f'{e}')
    
    