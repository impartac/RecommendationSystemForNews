from typing import Optional

from core.entities.implementation.domain_news import DomainNews
from core.factories.abstractions.news_factory_abs import NewsFactoryABS
from ..implementation.factory import Factory
from infrastructure.db.models.news_orm import NewsORM


class NewsFactory(NewsFactoryABS, Factory):
    def to_entity(self, instance: Optional[NewsORM]) -> Optional[DomainNews]:
        return DomainNews(
            id=instance.id,
            anons=instance.anons,
            title=instance.title,
            body=instance.body,
            date_creation=instance.date_creation,
        ) if instance else None

    def to_orm(self, instance: Optional[DomainNews]) -> Optional[NewsORM]:
        return NewsORM(
            id=instance.id,
            anons=instance.anons,
            title=instance.title,
            body=instance.body,
            date_creation=instance.date_creation,
        ) if instance else None
