# Project: 0x00. MySQL Advanced

## Description

This directory contains advanced projects focused on MySQL. The tasks cover a wide range of topics, including creating tables with constraints, optimizing queries with indexes, implementing stored procedures and functions, creating views, and using triggers. These projects are designed to provide hands-on experience with advanced MySQL features and techniques.

## Resources

- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.percona.com/blog/2019/02/20/mysql-performance-how-to-leverage-mysql-database-indexing/)
- [Stored Procedure](https://dev.mysql.com/doc/refman/8.0/en/stored-routines.html)
- [Triggers](https://dev.mysql.com/doc/refman/8.0/en/triggers.html)
- [Views](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)
- [Functions and Operators](https://dev.mysql.com/doc/refman/8.0/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/8.0/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/8.0/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/8.0/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)

## Learning Objectives

### General

- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL

## Tasks

| Task                                | File                                                               | Description                                                                                              |
| ----------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| 0. We are all unique!               | [0-uniq_users.sql](./0-uniq_users.sql)                             | Write a script that creates a table `users` with a unique constraint on the `email` column.              |
| 1. In and not out                   | [1-country_users.sql](./1-country_users.sql)                       | Write a script that lists all users from a specific country.                                             |
| 2. Best band ever!                  | [2-fans.sql](./2-fans.sql)                                         | Write a script that lists all fans of a specific band.                                                   |
| 3. Old school band                  | [3-glam_rock.sql](./3-glam_rock.sql)                               | Write a script that lists all bands from the `glam_rock` genre.                                          |
| 4. Buy buy buy                      | [4-store.sql](./4-store.sql)                                       | Write a script that calculates the total amount of purchases made in a store.                            |
| 5. Email validation to sent         | [5-valid_email.sql](./5-valid_email.sql)                           | Write a script that validates email addresses and lists the valid ones.                                  |
| 6. Add bonus                        | [6-bonus.sql](./6-bonus.sql)                                       | Write a script that adds a bonus to the salaries of employees.                                           |
| 7. Average score                    | [7-average_score.sql](./7-average_score.sql)                       | Write a script that calculates the average score of students.                                            |
| 8. Optimize simple search           | [8-index_my_names.sql](./8-index_my_names.sql)                     | Write a script that adds an index to the `names` column to optimize search queries.                      |
| 9. Optimize search and score        | [9-index_name_score.sql](./9-index_name_score.sql)                 | Write a script that adds indexes to the `name` and `score` columns to optimize search and score queries. |
| 10. Safe divide                     | [10-div.sql](./10-div.sql)                                         | Write a script that safely divides two numbers, handling division by zero.                               |
| 11. No table for a meeting          | [11-need_meeting.sql](./11-need_meeting.sql)                       | Write a script that lists all meetings that do not have a designated table.                              |
| 12. Average weighted score          | [100-average_weighted_score.sql](./100-average_weighted_score.sql) | Write a script that calculates the average weighted score of students.                                   |
| 13. Average weighted score for all! | [101-average_weighted_score.sql](./101-average_weighted_score.sql) | Write a script that calculates the average weighted score for all students, grouped by class.            |

## Additional Notes

- Ensure you have the necessary permissions to execute the scripts and commands.
- Test the scripts and commands in a safe environment to avoid any unintended changes to your system.
- Refer to the resources provided for a deeper understanding of each concept and its practical applications.
- Regularly review and update your skills to maintain proficiency in advanced MySQL techniques.
