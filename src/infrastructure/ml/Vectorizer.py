from typing import Iterable, AsyncIterable, List

import torch
from sentence_transformers import SentenceTransformer

from core.entities.implementation.domain_news import DomainNews
from core.entities.implementation.domain_vector import DomainVector
from src.core.entities.abstractions.vectorizer_model_abs import VectorizerModelABS
from src.config.logger_config import logger


class VectorizerModel(VectorizerModelABS):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L3-v2').to('cuda')
            logger.info("Vectorizer model has been initialized")
        return cls._instance

    async def vectorize(self, news: DomainNews) -> DomainVector:
        logger.debug(f"News : {news.id} is on vectorize")
        data = self.model.encode(news.body).tolist()
        logger.debug(f"Vectorized news : {data}")
        return DomainVector(id=news.id, data=data)

    async def vectorize_batch(self, news: List[DomainNews]) -> List[DomainVector]:
        data = self.model.encode([i.body for i in news]).tolist()
        vectors = [DomainVector(id=news[i].id, data=data[i]) for i in range(len(news))]
        return vectors
