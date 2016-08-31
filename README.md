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

-- Adding the files and directorys can be done via the setup.sh script, then you just need to added the variables above.

Details of the above can be found at the site https://erikberg.com/account/token and https://erikberg.com/api

Once the above steps are complete:

* go to the tests directory and you can run "nosetests *.py" to check the unit tests complete
* go to the xmlstatsnbaeventdownloader directory and run the main.py file to run a short download test - assuming your credentials are correct - you can check the log file in the logging dir

To Do: See Issues
