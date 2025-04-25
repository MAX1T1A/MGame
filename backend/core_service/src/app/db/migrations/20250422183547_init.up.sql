-- Таблица игровых сессий
CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    start_time TIMESTAMP,
    end_time TIMESTAMP
);

-- Таблица результатов игрока
CREATE TABLE game_players (
    id SERIAL PRIMARY KEY,
    game_id INTEGER REFERENCES games(id) ON DELETE CASCADE,
    user_id INTEGER NOT NULL,
    color VARCHAR(7) NOT NULL CHECK (color ~ '^#[0-9A-Fa-f]{6}$'),
    score INTEGER DEFAULT 0,
    clicks_total INTEGER DEFAULT 0,
    clicks_success INTEGER DEFAULT 0,
    clicks_failed INTEGER DEFAULT 0,
    is_winner BOOLEAN DEFAULT FALSE,
    UNIQUE (game_id, user_id) -- Игрок не может войти в игру дважды
);

-- Индексы
CREATE INDEX idx_game_players_game ON game_players (game_id);