import logging
import logging.config
from logging.handlers import RotatingFileHandler, SMTPHandler

# Configuração básica de logging
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = logging.DEBUG

# Configurações do logger
logger = logging.getLogger('pagbank.logger')
logger.setLevel(LOG_LEVEL)

# Criando um handler para o arquivo de log (com rotação)
file_handler = RotatingFileHandler(
    'app.log', maxBytes=1024*1024*5, backupCount=5)  # 5MB por arquivo, com até 5 backups
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Criando um handler para exibição no console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Criando um handler para envio de e-mails em caso de erro crítico
email_handler = SMTPHandler(
    mailhost=('smtp.example.com', 587),
    fromaddr='your_email@example.com',
    toaddrs=['admin@example.com'],
    subject='Critical Error in Your Application',
    credentials=('your_email@example.com', 'your_password'),
    secure=()
)
email_handler.setLevel(logging.CRITICAL)
email_handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Adicionando os handlers ao logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.addHandler(email_handler)

log = logger
# Exemplo de uso do logger
if __name__ == '__main__':
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
