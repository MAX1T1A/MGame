-- Таблица игровых сессий
CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    STATUS VARCHAR(20) DEFAULT 'waiting' CHECK (STATUS IN ('waiting', 'active', 'finished'))
);

-- Таблица игроков в сессии (user_id хранится как число, без внешнего ключа)
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

-- Таблица ячеек игрового поля
CREATE TABLE cells (
    id SERIAL PRIMARY KEY,
    game_id INTEGER REFERENCES games(id) ON DELETE CASCADE,
    x INTEGER NOT NULL CHECK (
        x BETWEEN 0
        AND 9
    ),
    y INTEGER NOT NULL CHECK (
        y BETWEEN 0
        AND 9
    ),
    color VARCHAR(7) NOT NULL CHECK (color ~ '^#[0-9A-Fa-f]{6}$'),
    player_id INTEGER,
    UNIQUE (game_id, x, y)
);

-- Индексы
CREATE INDEX idx_game_players_game ON game_players (game_id);

CREATE INDEX idx_cells_game ON cells (game_id);