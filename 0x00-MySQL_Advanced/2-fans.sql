-- This SQL query retrieves the total number of fans for each origin from the `metal_bands` table.
-- It performs the following operations:
-- 1. Selects the `origin` column.
-- 2. Calculates the sum of the `fans` column for each `origin` and aliases it as `nb_fans`.
-- 3. Groups the results by the `origin` column.
-- 4. Orders the grouped results in descending order based on the total number of fans (`nb_fans`).
SELECT
    `origin`,
    SUM(`fans`) AS `nb_fans`
FROM
    `metal_bands`
GROUP BY
    `origin`
ORDER BY
    `nb_fans` DESC;
