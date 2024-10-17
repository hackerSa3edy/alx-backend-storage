-- This SQL script creates a table named `users` if it does not already exist.
-- The `users` table has the following columns:
-- - `id`: An auto-incrementing integer that serves as the primary key.
-- - `email`: A varchar field with a maximum length of 255 characters, which must be unique and cannot be null.
-- - `name`: A varchar field with a maximum length of 255 characters, which can be null.
-- - `country`: An ENUM field that can only take one of the following values: 'US', 'CO', 'TN'. It cannot be null and defaults to 'US'.
CREATE TABLE IF NOT EXISTS `users` (
    `id` INTEGER AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255),
    `country` ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (`id`)
);
