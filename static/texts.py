START = """
Привет, %s!\nПришли мне имя иностранного исполнителя, а я в ответ порекомендую top10 похожих по тексту песен исполнителей.
Возможно, что твоего исполнителя не будет в локальной базе, тогда нужно будет немного подождать, когда база обновится.
Имей ввиду, что бот рекомендует исполнителей не по схожести жанра/стиля, а по близости текстов песен исполнителей.
*Список команд*:
/start - перезапуск
/info - расскажу о себе
/artists - выведет всех исполнителей в базе
/artists\_count - количество исполнителей в базе
/help - список доступных команд"""

HELP = """/start - перезапуск
/info - расскажу о себе
/artists - выведет всех исполнителей в базе
/artists_count - количество исполнителей в базе
/help - список доступных команд"""

INFO = 'Отправь мне имя иностранного исполнителя. Запрос должен быть в текстовом виде и не более 30 символов.'

INPUT_ERROR = """Запрос должен быть в текстовом виде.
Напомню, что /help выведет список доступных команд"""
