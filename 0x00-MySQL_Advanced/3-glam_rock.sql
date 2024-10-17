-- This SQL query retrieves the lifespan of glam rock bands from the `metal_bands` table.
-- It performs the following operations:
-- 1. Selects the `band_name` column.
-- 2. Calculates the lifespan of each band by subtracting the `formed` year from the `split` year.
--    If the `split` year is NULL, it uses 2022 as the default value.
-- 3. Aliases the calculated lifespan as `lifespan`.
-- 4. Filters the results to include only bands where the `style` column contains 'Glam rock'.
-- 5. Orders the results in descending order based on the `lifespan`.
SELECT
    `band_name`,
    COALESCE(`split`, 2022) - `formed` AS `lifespan`
FROM
    `metal_bands`
WHERE
    `style` LIKE '%Glam rock%'
ORDER BY
    `lifespan` DESC;
