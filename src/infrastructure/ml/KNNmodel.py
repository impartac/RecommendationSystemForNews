from typing import Iterable, List

import joblib
import numpy
import numpy as np
import torch
from sklearn.neighbors import NearestNeighbors

from core.entities.abstractions.vector_entity_abs import VectorEntityABS
from core.entities.abstractions.recommender_model_abs import RecommendationModelAbstraction
from config.logger_config import logger
import pandas as pd


class KNN(RecommendationModelAbstraction):
    _instance = None

    def __new__(cls, n_neighbors=5, device=torch.device('cpu')):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        logger.info("Model is already initialized")
        return cls._instance

    def __init__(self, n_neighbors=5, device=torch.device('cpu')):
        if not self.__initialized:
            logger.info('Initializing KNN model')
            super().__init__()
            self.model = NearestNeighbors(n_neighbors=n_neighbors, n_jobs=-1)
            self.news_ids: List[str] = []
            self.device = device
            self.has_built = False
            self.__initialized = True
            logger.info('KNN model initialized')

    def save(self, name: str = "knn"):
        joblib.dump(self.model, name)

    def build(self, data: Iterable[VectorEntityABS]) -> None:
        """Инициализация модели на существующих данных"""
        logger.info('Building KNN model')
        logger.info(f"vectors length: {len(list(data))}")
        self.news_ids = [news.id for news in data]
        self.model.fit(np.array([i.data for i in data]))
        self.has_built = True

    def train(self, additional_data: Iterable[VectorEntityABS]) -> None:
        """Добавление новых данных в модель"""
        logger.info('Training KNN model')
        logger.info(f"vectors length: {len(list(additional_data))}")
        new_ids = [news.id for news in additional_data]
        new_vectors = [news.data for news in additional_data]

        self.news_ids.extend(new_ids)
        self.vectors.extend(new_vectors)
        self.model.fit(np.array(self.vectors))

    def predict(self, target_vectors: VectorEntityABS) -> List[str]:

        _, indices = self.model.kneighbors([target_vectors.data])
        recommendations = []

        for idx in indices[0]:
            recommended_id = self.news_ids[int(idx)]
            if recommended_id != target_vectors.id:
                recommendations.append(str(recommended_id))

        return recommendations

    def predict_batch(self, target_vectors: List[VectorEntityABS]) -> List[List[str]]:
        _, indices = self.model.kneighbors([vector.data for vector in target_vectors])
        logger.info(f"Model processed")
        recommendations = []
        for i, predicted_indices in enumerate(indices):
            recommendations.append([])
            for idx in predicted_indices:
                recommended_id = self.news_ids[int(idx)]
                if recommended_id != target_vectors[i].id:
                    recommendations[i].append(recommended_id)
        return recommendations

    def get_state(self):
        return self.has_built
