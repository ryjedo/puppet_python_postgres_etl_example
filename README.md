This repo contains some example code for an ETL process. it extracts data from the "facter" command, converts that data into a dictionary and then inputs the uptime in seconds of the host machine into a database called facterstore (table facterstats).

This is meant to be expanded to include a bunch of other stats, and then run over night from cron. Ultimately providing a data set to begin learning typical database operations from (backups, restores, etc)

This represents an afternoon/evening of learning some python, TDD via unittest, and the beginings of database management in the form of creating a database, adding a table and a column and putting data into it.