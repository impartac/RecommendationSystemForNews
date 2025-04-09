CREATE TABLE public.news (
    id text primary key not null,
    title text,
    anons text,
    body text,
    date_creation timestamp without time zone
);
create table public.news_to_vector(
    id text primary key not null,
    data float[],
    foreign key (id) REFERENCES  news(id) on delete cascade
);
create table public.news_recommendation(
    id text primary key not null,
    recommendations text[],
    foreign key (id) REFERENCES news(id) on delete cascade
);