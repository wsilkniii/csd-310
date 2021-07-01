 -- Drops test user if exists
DROP USER IF EXISTS 'pysports_user'@'localhost';

CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON pysports.* TO 'pysports_user'@'localhost';

DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;

CREATE TABLE team (
    team_id INT NOT NULL AUTO_INCREMENT,
    team_name VARCHAR(75) NOT NULL,
    mascot VARCHAR(75) NOT NULL,
    PRIMARY KEY(team_id)
);

CREATE TABLE player (
    player_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL,
    team_id INT NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);

INSERT INTO team(team_name, mascot)
    VALUES
        ('Team Pirates', 'Giant Hand Hook'),
        ('Team Mac', 'MacBook Laptop Guy');

INSERT INTO player(first_name, last_name, team_id)
    VALUES
        ('Hill', 'Clontun', (SELECT team_id FROM team WHERE team_name = 'Team Pirates')),
        ('Donny', 'Plump', (SELECT team_id FROM team WHERE team_name = 'Team Pirates')),
        ('Jack', 'Sparow', (SELECT team_id FROM team WHERE team_name = 'Team Pirates')),
        ('Ben', 'Shape', (SELECT team_id FROM team WHERE team_name = 'Team Mac')),
        ('Bernie', 'Spandex', (SELECT team_id FROM team WHERE team_name = 'Team Mac')),
        ('Beau', 'Lydon', (SELECT team_id FROM team WHERE team_name = 'Team Mac'));
