-- This SQL script creates a trigger named `decrease_quantity_after_order`.
-- The trigger is executed after a new row is inserted into the `orders` table.
-- It performs the following operations:
-- 1. Updates the `quantity` column in the `items` table.
-- 2. Decreases the `quantity` by the value of the `number` column from the newly inserted row in the `orders` table.
-- 3. Matches the row in the `items` table where the `name` column equals the `item_name` from the newly inserted row.
DELIMITER / / CREATE TRIGGER `decrease_quantity_after_order`
AFTER
INSERT
    ON `orders` FOR EACH ROW BEGIN
UPDATE
    `items`
SET
    `quantity` = `quantity` - NEW.`number`
WHERE
    `name` = NEW.`item_name`;

END / / DELIMITER;
