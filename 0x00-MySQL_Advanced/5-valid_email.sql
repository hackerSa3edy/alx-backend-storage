-- This SQL script creates a trigger named `reset_email_validation`.
-- The trigger is executed before a row in the `users` table is updated.
-- It performs the following operations:
-- 1. Checks if the new value of the `email` column (`NEW.email`) is different from the old value (`OLD.email`).
-- 2. If the email has changed, it sets the `valid_email` column to 0 in the new row.
-- This ensures that the email validation status is reset whenever the email is updated.
DELIMITER / / CREATE TRIGGER `reset_email_validation` BEFORE
UPDATE
    ON `users` FOR EACH ROW BEGIN IF NEW.`email` != OLD.`email` THEN
SET
    NEW.`valid_email` = 0;

END IF;

END / / DELIMITER;
