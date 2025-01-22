from src.app.services.managers.news_manager import NewsManager
from src.app.services.managers.vector_manager import VectorManager
from src.config.logger_config import logger


class Utils:
    @staticmethod
    async def transform_all_news(news_manager: NewsManager,
                                 vector_manager: VectorManager,
                                 offset: int = 0,
                                 batch_size: int = 2 ** 15):
        while True:
            try:
                data = await news_manager.get_batch(batch_size, offset)
                if not data:
                    return
                encoded_data = vector_manager.vectorizer.fill_vector_batch(data)
                await vector_manager.insert_many(encoded_data)
                offset += batch_size
                logger.info(f"Utils.transform_all_news(): offset {offset}, OK!")
            except Exception as e:
                logger.error(f"Utils.transform_all_news(): {e}")
                return

# ░░░░░░░░░░░░░░░░░░░░
# ░░░░░ЗАПУСКАЕМ░░░░░░░
# ░ГУСЯ░▄▀▀▀▄░РАБОТЯГИ░░
# ▄███▀░◐░░░▌░░░░░░░░░
# ░░░░▌░░░░░▐░░░░░░░░░
# ░░░░▐░░░░░▐░░░░░░░░░
# ░░░░▌░░░░░▐▄▄░░░░░░░
# ░░░░▌░░░░▄▀▒▒▀▀▀▀▄
# ░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄
# ░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄
# ░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄
# ░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄
# ░░░░░░░░░░░▌▌░▌▌░░░░░
# ░░░░░░░░░░░▌▌░▌▌░░░░░
# ░░░░░░░░░▄▄▌▌▄▌▌░░░░░
