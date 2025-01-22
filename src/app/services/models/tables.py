from sqlalchemy import Table, Column, MetaData, TIMESTAMP, ARRAY, TEXT, FLOAT, ForeignKey

metadata = MetaData()

news_table = Table(
    'tmp_news',
    metadata,
    Column('id', TEXT, primary_key=False),
    Column('title', TEXT),
    Column('anons', TEXT),
    Column('body', TEXT),
    Column('date_creation', TIMESTAMP),
    extend_existing=True
)

'''
Struct of JSON:
id : TEXT , from tmp_news table
similarity : float , show similarity score between news and recommendation 
(I think that ARRAy must have size 5/10/15, not bigger.)
'''
recommendation_table = Table(
    'news_recommendation',
    metadata,
    Column('id', TEXT, ForeignKey('tmp_news.id', ondelete='CASCADE'), primary_key=False),
    Column('recommendations', ARRAY(item_type=TEXT)),
    Column('updated_at', TIMESTAMP),
    extend_existing=True
)

'''
news_to_vector table contains \'encoded\' values for each column and general to.
ARRAYs size depends of length (of value inside each Column), will be counted in time.
'''
news_to_vector = Table(
    'news_to_vector',
    metadata,
    Column('id', TEXT, ForeignKey('tmp_news.id', ondelete='CASCADE'), primary_key=False),
    # Column('title', ARRAY(item_type=FLOAT)),
    # Column('anons', ARRAY(item_type=FLOAT)),
    Column('body', ARRAY(item_type=FLOAT)),
    # Column('overall', ARRAY(item_type=FLOAT)),
    extend_existing=True
)

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
