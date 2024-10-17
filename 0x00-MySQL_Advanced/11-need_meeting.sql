-- This SQL script creates a view named `need_meeting`.
-- The view selects the `name` column from the `students` table.
-- It filters the results to include only students who meet the following criteria:
-- 1. The `score` is less than 80.
-- 2. Either the `last_meeting` is NULL or the difference between the current date and the `last_meeting` date is greater than 30 days.
-- This view helps identify students who need a meeting based on their score and the time since their last meeting.
CREATE VIEW `need_meeting` AS
SELECT
    `name`
FROM
    `students`
WHERE
    `score` < 80
    AND (
        `last_meeting` IS NULL
        OR DATEDIFF(CURDATE(), `last_meeting`) > 30
    );
