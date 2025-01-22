import time
# from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors
import numpy as np
import joblib
from src.config.logger_config import logger
from src.app.services.managers.news_manager import NewsManager
from src.app.services.managers.vector_manager import VectorManager
from typing import List
from src.config.logger_config import log_method_call


class RecommendationBuilder:
    def __init__(self,
                 news_manager: NewsManager,
                 vector_manager: VectorManager):
        self.news_manager = news_manager
        self.vector_manager = vector_manager
        self.knn = None

    @log_method_call
    async def build_knn(self, n_neighbors: int = 5):
        """Build KNN model and fit the data"""
        start_time = time.time()
        ts = time.time()
        self.knn = NearestNeighbors(n_neighbors=n_neighbors, metric="cosine")
        async for chunk in self.vector_manager.get_all():
            vector_body = [np.array(vector.body) for vector in chunk]
            logger.info(f"Vector bodies got batch. time: {time.time() - ts}")
            ts = time.time()
            self.knn.fit(vector_body)
            logger.info(f"Vector bodies fitted. time: {time.time() - ts}")
            ts = time.time()
        logger.info(f"KNN model is built, time: {time.time() - start_time}")

    @log_method_call
    async def _train_knn(self, vectors: List):
        if self.knn is None:
            logger.error(f"KNN is None")
            raise Exception("KNN is None")
        self.knn.fit(vectors)

    def safe_model(self, name: str = "knn.joblib"):
        joblib.dump(self.knn, name)

    def load_model(self, name: str = "knn.joblib"):
        self.knn = joblib.load(name)

    # @log_method_call
    # async def fill_recommendations(self):
    #     offset = 0
    #     data = self.vector_manager.get_batch()
    #     while data:
    #         rec = []
    #         for news_vector in data:
    #             rec.append(
    #                 RecommendationsORM(
    #                     news_vector.id,
    #                     self.knn.kneighbors(news_vector.body)
    #                 )
    #             )


    # async def get_news_data(self, ids: List[str]) -> List[NewsORM]:
    #     """Fetch all data for news by ids"""
    #     try:
    #         async with self.news_manager.async_session() as session:
    #             query = select(NewsORM).where(NewsORM.id.in_(ids))
    #             result = await session.execute(query)
    #             news = result.scalars().all()
    #             return list(news)
    #     except SQLAlchemyError as e:
    #         logger.error(f"Error during get_news_{e}")
    #         return []
    #
    # async def _get_recommendations(self, knn: NearestNeighbors, vector: VectorORM, vector_to_id: dict):
    #     """get recommendations for news"""
    #     vector_body = np.array(vector.body).reshape(1, -1)
    #     distances, indices = knn.kneighbors(vector_body)
    #     recommendations = []
    #     for index in indices[0][1:]:
    #         id = vector_to_id[index]
    #         recommendations.append(id)
    #     return recommendations

    # async def _batch_update_recommendations(self, recommendations: List[RecommendationsORM]) -> None:
    #     """Batch update recommendations in the database"""
    #     try:
    #         async with self.news_manager.async_session() as session:
    #             session.add_all(recommendations)
    #             await session.commit()
    #
    #     except SQLAlchemyError as e:
    #         logger.error(f"Error during _batch_update_recommendations: {e}")
    #         await session.rollback()
    #
    # async def build_recommendations(self, n_neighbors: int = 5, batch_size: int = 2 ** 6):
    #     ts = time.time()
    #     news_vectors = await self.vector_manager.get_all()
    #     vector_to_id = {index: vector.id for index, vector in enumerate(news_vectors)}
    #     knn = await self._build_knn(news_vectors, n_neighbors)
    #     logger.info(f"Knn has build time: {time.time() - ts}")
    #     all_recommendations = []
    #     for vector in news_vectors:
    #         recommendations = await self._get_recommendations(knn, vector, vector_to_id)
    #         all_recommendations.append(
    #             RecommendationsORM(id=vector.id, recommendations=recommendations, updated_at=datetime.now())
    #         )
    #     for i in range(0, len(all_recommendations), batch_size):
    #         batch = all_recommendations[i:i + batch_size]
    #         await self._batch_update_recommendations(batch)
    #         logger.info(f"Batch update time: {time.time() - ts}, batch : {i}")
    #     logger.info(f"Build recommendations {time.time() - ts}")
