import logging, logging.config
from Lab_4_CasinoAndGeese.src.logging_config import LOGGING_CONFIG

class Logger:
    def __init__(self):
        logging.config.dictConfig(LOGGING_CONFIG)
        self.logger = logging.getLogger("CasinoAndGeese")
        self.current_step = None

    def set_step(self, step: int):
        self.current_step = step

    def logging_message(self, message, with_step: bool = True) -> None:
        message = str(message)

        prefix = ''
        if with_step and self.current_step is not None:
            prefix = f'[Ход {self.current_step}] '

        full_message = prefix + message
        self.logger.info(full_message)
        print(full_message)
