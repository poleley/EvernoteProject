import mysql.connector
from mysql.connector import Error
from evernote import create_connection, execute_query, execute_read_query


create_users = """
INSERT INTO 
    `evernote`.`users` (`id`, `name`, `email`, `password`)
VALUES
    (1, 'Иванов Иван', 'ivanov@gmail.com', 'qwerty123456'),
    (2, 'Петрова Светлана', 'petrova@gmail.com', '123456'),
    (3, 'Жуков Степан', 'zhukov@mail.ru', 'qwerty');
"""

create_notes = """
INSERT INTO 
    `evernote`.`notes` (`user_id`, `name`, `date`, `text`)
VALUES
    (1, 'Список дел', '2021-12-04', '1.Погулять с собакой 2.Купить продукты 3.Приготовить ужин'),
    (1, 'Не забыть!', '2021-11-29', 'Пройти курс на степике'),
    (2, 'Дни рождения', '2021-07-01', 'Иван: 01.03.1994, Ирина: 16.11.2000, Женя: 07.07.2001'),
    (3, 'Задачи на завтра', '2021-12-04', '1.Доделать лабу по ЧМ 2.Подготовиться к зачету по ассемблеру'),
    (3, 'Фильмы', '2021-12-04', NULL),
    (3, 'Сериалы', '2021-11-20', 'Игра престолов, Рик и Морти, В её глазах');
"""

create_tags = """
INSERT INTO
    `evernote`.`tags` (`name`)
VALUES
    ('список дел'),
    ('развлечения'),
    ('не забыть');
"""

create_note_has_tag = """
INSERT INTO
    `evernote`.`note_has_tag` (`note_id`, `tag_id`)
VALUES
    (1, 1),
    (2, 3),
    (3, 3),
    (4, 1),
    (5, 2),
    (6, 2);
"""


connection = create_connection("localhost", "root", "", "evernote") #"хост" "имя_пользователя" "пароль" "база_данных"


delete_user = """DELETE FROM users WHERE id = 1;"""
delete_note = """DELETE FROM notes WHERE id = 1;"""
delete_tag = """DELETE FROM tags WHERE id = 1;"""

select_users = """SELECT * FROM `evernote`.`users`;"""
select_notes = """SELECT * FROM `evernote`.`notes`;"""
select_tags = """SELECT * FROM `evernote`.`tags`;"""

filter_by_date = """SELECT 
`notes`.`name`,
`notes`.`date`,
`notes`.`text`
    FROM `note_has_tag` 
    INNER JOIN `notes` 
    ON `note_has_tag`.`note_id` = `notes`.`id` 
    INNER JOIN `users`
    ON `users`.`id`=`notes`.`user_id`
    INNER JOIN `tags` 
    ON `note_has_tag`.`tag_id` = `tags`.`id`
    WHERE `users`.`id` = 1
    ORDER BY date DESC;"""

filter_by_tag = """SELECT 
`notes`.`name`,
`notes`.`date`,
`notes`.`text`
    FROM `note_has_tag` 
    INNER JOIN `notes` 
    ON `note_has_tag`.`note_id` = `notes`.`id` 
    INNER JOIN `users`
    ON `users`.`id`=`notes`.`user_id`
    INNER JOIN `tags` 
    ON `note_has_tag`.`tag_id` = `tags`.`id`
    WHERE `tags`.`name` = 'развлечения' AND `users`.`id` = 3;"""

#execute_query(connection, create_users)
#execute_query(connection, create_notes)
#execute_query(connection, create_tags)
#execute_query(connection, create_note_has_tag)

#execute_query(connection, delete_user)

users = execute_read_query(connection, select_users)
notes = execute_read_query(connection, filter_by_date)
tags = execute_read_query(connection, select_tags)

for note in notes:
    print(note)

for tag in tags:
    print(tag)

for user in users:
    print(user)

