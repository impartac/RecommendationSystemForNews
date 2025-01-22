from src.app.services.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import TEXT, FLOAT, ARRAY


class VectorORM(Base):
    __tablename__ = 'news_to_vector'

    id: Mapped[TEXT] = mapped_column(TEXT, primary_key=True)
    # title: Mapped[ARRAY] = mapped_column(ARRAY(item_type=FLOAT))
    # anons: Mapped[ARRAY] = mapped_column(ARRAY(item_type=FLOAT))
    body: Mapped[ARRAY] = mapped_column(ARRAY(item_type=FLOAT))
    # overall: Mapped[ARRAY] = mapped_column(ARRAY(item_type=FLOAT))

    def __init__(self, id: TEXT, body: ARRAY) -> None:
        super(VectorORM, self).__init__()
        self.id = id
        # self.title = title
        # self.anons = anons
        self.body = body
        # self.overall = overall

    def __repr__(self) -> str:
        return (f"<News id='{self.id}', "
                # f"title='{self.title[:20]}...', "
                # f"anons='{self.anons[:20]}...', "
                f"body='{self.body[:20]}...', ")
                # f"overall='{self.overall[:20]}...'>'")

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
