-- This SQL script creates a stored procedure named `AddBonus`.
-- The procedure takes three input parameters:
-- 1. `user_id` (INT): The ID of the user.
-- 2. `project_name` (VARCHAR(255)): The name of the project.
-- 3. `score` (INT): The score to be added.
-- The procedure performs the following operations:
-- 1. Declares a variable `project_id` to store the ID of the project.
-- 2. Attempts to retrieve the `id` of the project from the `projects` table based on the `project_name`.
-- 3. If the project does not exist (`project_id` is NULL), it inserts a new project with the given `project_name` and retrieves the new `project_id`.
-- 4. Inserts a new record into the `corrections` table with the provided `user_id`, `project_id`, and `score`.
DELIMITER //
CREATE PROCEDURE `AddBonus` (
    IN `user_id` INT,
    IN `project_name` VARCHAR(255),
    IN `score` INT
) BEGIN DECLARE `project_id` INT;

SELECT
    `id` INTO `project_id`
FROM
    `projects`
WHERE
    `name` = `project_name`;

IF `project_id` IS NULL THEN
INSERT INTO
    `projects` (`name`)
VALUES
    (`project_name`);

SET
    `project_id` = LAST_INSERT_ID();

END IF;

INSERT INTO
    `corrections` (`user_id`, `project_id`, `score`)
VALUES
    (`user_id`, `project_id`, `score`);

END
// DELIMITER;
