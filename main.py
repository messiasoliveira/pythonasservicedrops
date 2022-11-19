import logging
import time
from service import Service

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class PyAAS(Service):
    def __init__(self, *args, **kwargs):
        super(PyAAS, self).__init__(*args, **kwargs)

    def run(self):
        while not self.got_sigterm():
            logging.debug(f"Serviço ativo PID: {self.get_pid()}")
            time.sleep(5)

    def processar(self):
        logging.info('Iniciando processamento...')
        for i in range(10):
            print(f'Processando {i}')
        logging.info('Processamento concluido!!!')


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        logging.error(f"Erro de sintaxe: {sys.argv[1]} ")
        sys.exit()

    cmd = sys.argv[1].lower()
    service = PyAAS('python-as-a-service', pid_dir='/tmp')

    if cmd == 'start':
        service.start()
        logging.info('Iniciando o serviço...')

    elif cmd == 'stop':
        service.stop()

    elif cmd == 'processar':
        service.processar()

    elif cmd == 'status':
        if service.is_running():
            logging.info("O serviço está rodando.")
        else:
            logging.info("O serviço não está rodando")
    else:
        logging.error(f'Não foi possivel localizar o comando: {cmd}')
        sys.exit()