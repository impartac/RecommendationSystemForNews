from src.app.services.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import TEXT, DATETIME


class NewsORM(Base):
    __tablename__ = 'tmp_news'

    id: Mapped[TEXT] = mapped_column(TEXT, primary_key=True)
    title: Mapped[TEXT] = mapped_column(TEXT)
    anons: Mapped[TEXT] = mapped_column(TEXT)
    body: Mapped[TEXT] = mapped_column(TEXT)
    date_creation: Mapped[DATETIME] = mapped_column(DATETIME)

    def __repr__(self):
        return f"<News id='{self.id}', title='{self.title[:20]}...', anons='{self.anons[:20]}...', body='{self.body[:20]}...'"

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
