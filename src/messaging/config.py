class Config:
    HOST = 'localhost'  # Change default server host if required
    PORT = 9092  # Change default server port if required
    TOPIC = 'flights'

    @staticmethod
    def get_broker():
        return f"{Config.HOST}:{Config.PORT}"
