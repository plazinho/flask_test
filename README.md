# Telegram bot that recommends music artists by lyrics similarity
## Bot name: @recommend_an_artist_bot
## Bot works only with singers that perform in english
- TfidfVectorizer from sklearn library is used to calculate the TF-IDF of all words in the lyrics of singers and, on the basis of cosine similarity, likeness/similarity of artists is found
- If the requested singer is not present in the local database bot warns the user and begins to update and recalculate the DB
- Possibility of a "cold start" of the bot is implemented - when it is launched, the presence of the required data is checked. If something went wrong you should delete everything in directory 'api/data/' except 'init_names.txt' file which contains singers names to help create initial local DB. Then run 'bot.py' again

### In order to start bot on your machine:
- Create a bot with a help of @BotFather in telegram
- Clone repository
- Create '.env' file in main directory which will contain your Genius API TOKEN, telegram bot TOKEN and your telegram user id(you can check it with a help of @ShowJsonBot). '.env.dist' is an example of a '.env' file
- Install required libraries (pip install -r requirements.txt)
- Run 'bot.py' to start the bot

### In order to get a recommendation from the bot:
- Send artist name you are interested in
- Bot will check if the singer's name exists in local database. If not then with a help of Genius API local DB will be updated. Otherwise bot will make a recommendation of a top10 similar artists right away

![rec-x2](https://user-images.githubusercontent.com/88561819/138957735-ea65581d-f52d-4e0d-bf33-0280a3cab04e.jpg)

### Available commands:
- /start - welcome message
- /info - about bot
- /artists - list of singers in local DB
- /artists_count - number of singers in the database
- /help - available commands

![x2](https://user-images.githubusercontent.com/88561819/138955995-4fe974aa-b4eb-4347-9670-0fdb0eb68088.jpg)
