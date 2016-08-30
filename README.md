# xmlstats-nba-event-downloader
Python 3.5 project to download NBA basketball events from [xmlstats](https://erikberg.com/api) for a date range defined in the main.py file.

This project is me learning as I go about writing better python code as I go and is compiled with python 3.5.

There may be dependencies which are not defined correctly this will be updated as I go along.

To setup:

1. Clone the repo
2. add directories for "data" and "logging"
3. add a config.py file with the following contents

accessToken = 'my token'

user_agent = 'my user agent'

Details of the above can be found at the site https://erikberg.com/account/token and https://erikberg.com/api

To Do:

1. Migrate this list to github issues
2. Investigate pythonic naming conventions for files, functions and methods
3. Check if the Object Orientation is well used in the project
4. Improve unit test coverage
5. Package the code
6. Possibly automate the deployment
7. Fix the install as a package with config file and directories as above
