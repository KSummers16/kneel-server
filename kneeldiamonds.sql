CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMBERIC(1,2) NOT NULL,
    `price` NUMBERIC(5,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    [metal_id] INTEGER NOT NULL,
    [size_id] INTEGER NOT NULL,
    [style_id] INTEGER NOT NULL,
    FOREIGN KEY (`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY (`size_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY (`style_id`) REFERENCES `Styles`(`id`)
);


insert into `metals` VALUES (1,"gold", 100.00);
insert into `metals` VALUES (2, "white gold", 100.00);
insert into `metals` values (3, "silver", 75.00);
insert into `metals` values (4, "titanium", 150.00);

insert into `styles` values (1, "modern", 250.00);
insert into `styles` values (2, "vintage", 300.00);
insert into `styles` values (3, "classic", 200.00)

insert into `sizes` values (1, 0.5, 405);
insert into `sizes` values (2, 0.75, 782);
insert into `sizes` values (3, 1, 1000);
insert into `sizes` values (4, 2, 2000);


insert into `orders` values (1, 1, 4, 2);
insert into `orders` values (2, 2, 3, 3);
insert into `orders` values (3, 3, 2, 1);
insert into `orders` values (4, 1, 2, 1);