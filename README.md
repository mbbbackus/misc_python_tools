# misc_python_tools

This repo is for miscellaneous python tools I've created.
As of right now, it contains:

	- An employee check in/out executable program 
		- writes to csv file date, in/out times, time worked
		- bug fixes:
			- fixed bug where 10:01 would look like 10:1 for example 
    - A json tools module
        - Formatting function to make json readable to humans
        - Function that aggregates dictionaries
        - bug fixes:
            - Fixed bug where formatting would not indent dictionaries
            - Changed json tools from script to a module
    - NBA stats application
        - Parses HTML info to create a small database of nba player stats
        - Can take player and stat arguments and return any player's stats
        - Stat source: http://basketball.realgm.com/nba/stats
        - To do:
            - Improve stat gathering, possibly create scraper to get info
                or retrieve stats straight from webpage
            - Use Django to create web UI
