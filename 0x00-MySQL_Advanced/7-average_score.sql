-- This SQL script creates a stored procedure named `ComputeAverageScoreForUser`.
-- The procedure takes one input parameter:
-- 1. `user_id` (INT): The ID of the user for whom the average score is to be computed.
-- The procedure performs the following operations:
-- 1. Updates the `average_score` column in the `users` table for the specified `user_id`.
-- 2. Sets the `average_score` to the average of the `score` values from the `corrections` table where the `user_id` matches.
-- This ensures that the `average_score` in the `users` table is kept up-to-date based on the scores in the `corrections` table.
DELIMITER //
CREATE PROCEDURE `ComputeAverageScoreForUser` (IN `user_id` INT) BEGIN
UPDATE
    `users`
SET
    `average_score` = (
        SELECT
            AVG(`score`)
        FROM
            `corrections` AS `cor`
        WHERE
            `cor`.`user_id` = `user_id`
    )
WHERE
    `id` = `user_id`;

END
// DELIMITER;
