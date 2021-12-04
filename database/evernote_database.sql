CREATE DATABASE `evernote`;
CREATE TABLE `evernote`.`users`(
	`id` INT AUTO_INCREMENT NOT NULL,
    `name` VARCHAR(60) NOT NULL,
    `email` VARCHAR(45) NOT NULL,
    `password` VARCHAR(45) NOT NULL,
    PRIMARY KEY (`id`)
    )
    ENGINE = InnoDB
    DEFAULT CHARACTER SET = utf8
    COLLATE = utf8_general_ci;
    
CREATE TABLE `evernote`.`notes`(
	`id` INT AUTO_INCREMENT NOT NULL,
    `user_id` INT NOT NULL,
    `name` VARCHAR(45) NOT NULL,
    `date` DATE NOT NULL,
    `text` MEDIUMTEXT,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES `evernote`.`users` (`id`) ON DELETE CASCADE
    )
    ENGINE = InnoDB
    DEFAULT CHARACTER SET = utf8
    COLLATE = utf8_general_ci;
    
CREATE TABLE `evernote`.`tags`(
	`id` INT AUTO_INCREMENT NOT NULL,
    `name` VARCHAR(45) NOT NULL,
    PRIMARY KEY (`id`)
    )
    ENGINE = InnoDB
    DEFAULT CHARACTER SET = utf8
    COLLATE = utf8_general_ci;

CREATE TABLE `evernote`.`note_has_tag`(
	`note_id` INT NOT NULL,
    `tag_id` INT NOT NULL,
    PRIMARY KEY (`note_id`, `tag_id`),
    FOREIGN KEY (`note_id`) REFERENCES `evernote`.`notes` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`tag_id`) REFERENCES `evernote`.`tags` (`id`) ON DELETE CASCADE
    )
    ENGINE = InnoDB
    DEFAULT CHARACTER SET = utf8
    COLLATE = utf8_general_ci;  
    
    