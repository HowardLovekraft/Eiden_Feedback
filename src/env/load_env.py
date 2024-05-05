import dotenv, os


class EnvVars:
    def __init__(self, path):
        dotenv.load_dotenv(path)

    @staticmethod
    async def get_auh_token():
        return os.getenv("BOT_TOKEN")

    @staticmethod
    async def get_feedback_getter_id():
        return os.getenv("ID_FEEDBACK_TO")


env_vars = EnvVars("env\\venv.env")
