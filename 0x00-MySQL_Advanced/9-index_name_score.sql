-- This SQL script creates a composite index named `idx_name_first_score` on the `names` table.
-- The index is created on the first character of the `name` column and the entire `score` column.
-- This composite index can improve query performance for searches that filter by the initial character of the `name` and the `score`.
CREATE INDEX `idx_name_first_score` ON `names` (`name`(1), `score`);
