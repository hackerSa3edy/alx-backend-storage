-- This SQL script creates a user-defined function named `SafeDiv`.
-- The function takes two integer input parameters: `a` and `b`.
-- It returns a FLOAT value and is marked as DETERMINISTIC, indicating that it always produces the same result for the same input parameters.
-- The function performs the following operations:
-- 1. Checks if the divisor `b` is 0.
-- 2. If `b` is 0, it returns 0 to avoid division by zero errors.
-- 3. If `b` is not 0, it returns the result of the division `a / b`.
DELIMITER / / CREATE FUNCTION SafeDiv (a INT, b INT) RETURNS FLOAT DETERMINISTIC BEGIN IF b = 0 THEN RETURN 0;

END IF;

RETURN a / b;

END / / DELIMITER;
