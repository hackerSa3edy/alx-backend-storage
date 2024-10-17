-- This SQL script creates a stored procedure named `ComputeAverageWeightedScoreForUsers`.
-- The procedure does not take any input parameters.
-- The procedure performs the following operations:
-- 1. Updates the `average_score` column in the `users` table for each user.
-- 2. Sets the `average_score` to the weighted average of the `score` values from the `corrections` table,
--    where the weights are taken from the `weight` column in the `projects` table.
--    The weighted average is calculated as the sum of the product of `score` and `weight` divided by the sum of `weight`.
--    If the sum of `weight` is 0, it returns 0 to avoid division by zero errors.
-- 3. Only updates the `average_score` for users who have corresponding records in the `corrections` table.
-- This ensures that the `average_score` in the `users` table is kept up-to-date based on the weighted scores in the `corrections` table.
DELIMITER / / CREATE PROCEDURE `ComputeAverageWeightedScoreForUsers` () BEGIN
UPDATE
    `users` AS `u`
SET
    `average_score` = (
        SELECT
            COALESCE(
                SUM(`c`.`score` * `p`.`weight`) / NULLIF(SUM(`p`.`weight`), 0),
                0
            )
        FROM
            `corrections` AS `c`
            INNER JOIN `projects` `p` ON `c`.`project_id` = `p`.`id`
        WHERE
            `c`.`user_id` = `u`.`id`
    )
WHERE
    EXISTS (
        SELECT
            1
        FROM
            `corrections` `c`
        WHERE
            `c`.`user_id` = `u`.`id`
    );

END / / DELIMITER;
