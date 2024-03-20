# Python Projects

Repository for Expense Tracker web application using Python 3, FastAPI, SQLAlchemy, Alembic and PyTest

This repository features web application named Expense Tracker using FastAPI features.

It has mainly two entities.
(1) Users 
(2) Expenses (Groceries, Travel, House etc.)

One User can have many expenses.

ORM used is SQLAlchemy which talks to MySQL database.

CRUD operationns are handled and exception handling is done with proper response codes.

Basic testcases are also there. 

Lastly, it features Alembic scripts which are required for database migrations.
Alembic offers the following functionality:

(1) Can emit ALTER statements to a database in order to change the structure of tables and other constructs

(2) Provides a system whereby “migration scripts” may be constructed; each script indicates a particular series of steps that can “upgrade” a target database to a new version, 
and optionally a series of steps that can “downgrade” similarly, doing the same steps in reverse.

(3) Allows the scripts to execute in some sequential manner.


