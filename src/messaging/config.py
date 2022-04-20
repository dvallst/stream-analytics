class Config:
    HOST = 'localhost'  # Change default server host if required
    PORT = 9092  # Change default server port if required
    TOPIC = 'flights'  # Topic name

    @staticmethod
    def get_broker():
        """
        Get broker to publish messages to and consume messages from

        :return: String: Hostname and port number
        """
        return f"{Config.HOST}:{Config.PORT}"
