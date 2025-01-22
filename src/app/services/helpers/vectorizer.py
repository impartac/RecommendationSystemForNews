from safetensors import torch
# from transformers import AutoTokenizer, AutoModel
import torch
from sentence_transformers import SentenceTransformer
import re
from src.config.logger_config import log_method_call, logger
from typing import Any

'''
MODELS
 - "bert-base-multilingual-cased"              7.5 for 128
 - "distilbert-base-multilingual-cased"        5.2 for 128
 - "microsoft/MiniLM-L12-H384-uncased"         5.3 for 128
 - "google/mobilebert-uncased"                 18.8 for 128 
 - "huawei-noah/TinyBERT_General_4L_312D"      4.7 for 128
 - "albert-base-v2"                            8.3 for 128
 - "sentence-transformers/all-MiniLM-L12-v2"   7.08 for 128
 - "sentence-transformers/all-MiniLM-L6-v2"    5.22 for 128
 - "sentence-transformers/paraphrase-MiniLM-L3-v2"  3.65 for 128
'''


class Vectorizer:
    def __init__(self, model_name: str = "sentence-transformers/paraphrase-MiniLM-L3-v2"):
        # self.tokenizer = AutoTokenizer.from_pretrained("huawei-noah/TinyBERT_General_4L_312D")
        # self.model = AutoModel.from_pretrained("huawei-noah/TinyBERT_General_4L_312D")
        self.model = SentenceTransformer(model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        logger.info(f"Using device: {self.device}")
        self.model.to(self.device)

    @log_method_call
    async def strip(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text

    @log_method_call
    async def tokenize(self, text: str) -> list:
        try:
            return list(map(float, list(self.model.encode(text, convert_to_tensor=True).cpu().numpy())))
        except Exception as e:
            logger.error(e)
            return []

    @log_method_call
    async def tokenize_batch(self, texts: list) -> list:
        ans = list(self.model.encode(texts, convert_to_tensor=True).cpu().numpy())
        return ans

    @log_method_call
    async def convert_news(self, news, orm_type: type) -> Any:
        try:
            encoded_data = await self.tokenize(str(news.body))
            vec = orm_type(
                news.id,
                encoded_data
            )
            logger.debug(f"{news.id=} encoded")
            return vec
        except Exception as e:
            logger.error(e)
            return None

    @log_method_call
    async def fill_vector_batch(self, news: list, orm_type: type) -> list:
        try:
            encoded_bodies = await self.tokenize_batch([x.body for x in news])
            converted_news = [orm_type(news[i].id, encoded_bodies[i]) for i in range(len(news))]
            return converted_news
        except Exception as e:
            logger.error(f"Error in fill_vector_batch: {e}")
            return []
