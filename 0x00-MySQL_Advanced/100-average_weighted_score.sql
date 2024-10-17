-- This SQL script creates a stored procedure named `ComputeAverageWeightedScoreForUser`.
-- The procedure takes one input parameter:
-- 1. `user_id` (INT): The ID of the user for whom the average weighted score is to be computed.
-- The procedure performs the following operations:
-- 1. Updates the `average_score` column in the `users` table for the specified `user_id`.
-- 2. Sets the `average_score` to the weighted average of the `score` values from the `corrections` table,
--    where the weights are taken from the `weight` column in the `projects` table.
--    The weighted average is calculated as the sum of the product of `score` and `weight` divided by the sum of `weight`.
--    Only the records where the `user_id` matches are considered.
-- This ensures that the `average_score` in the `users` table is kept up-to-date based on the weighted scores in the `corrections` table.
DELIMITER / / CREATE PROCEDURE `ComputeAverageWeightedScoreForUser` (IN `user_id` INT) BEGIN
UPDATE
    `users`
SET
    `average_score` = (
        SELECT
            SUM(`c`.`score` * `p`.`weight`) / SUM(`p`.`weight`)
        FROM
            `corrections` AS `c`
            INNER JOIN `projects` `p` ON `c`.`project_id` = `p`.`id`
        WHERE
            `c`.`user_id` = `user_id`
    )
WHERE
    `id` = `user_id`;

END / / DELIMITER;
