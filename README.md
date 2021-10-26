# Telegram bot that recommends musical artists by lyrics similarity
## Bot name: @recommend_an_artist_bot
## Bot works only with artists that perform in english
- recommendation system of the bot was build using TF-IDF and allows to find artist that have similar lyrics;
- bot will show top 5 similar artists;
- you are also able to check what artists bot currently knows

### In order to start bot on your machine:
- Create a bot with a help of @BotFather in telegram
- Clone repository
- Create '.env' file in main directory which will contain your Genius API TOKEN, telegram bot TOKEN and your telegram user id(you can check it with a help of @ShowJsonBot). '.env.dist' is an example of a '.env' file
- Install required libraries (pip install -r requirements.txt)
- Run 'bot.py' to start the bot

### In order to get a recommendation from the bot:
- In order to get a recommendation from the bot send artist name you are interested in
- Bot will check if the artist exists in local database. If not then with a help of Genius API local DB will be updated. Otherwise bot will make a recommendation of a top10 similar artists right away


### Available commands:
- /start - welcome message
- /info - about bot
- /artists - list of artists in local DB
- /artists_count - number of music artists in the database
- /help - available commands
