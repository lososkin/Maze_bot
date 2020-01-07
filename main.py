import telebot
import labirint
import sql
import private
from settings import height,width,wall_cell,gamer_cell,space_cell

"""
Настраивыемые параметры из файла settings.py:
height, width - высота и ширина соответсвено, следует делать нечетными (int)
wall_cell - определяет как будет отрисовываться клетка со стеной
gamer_cell - определяет как будет отрисовываться клетка с игроком
space_cell - определяет как будет отрисовываться пустая клетка
token - уникальный токен для управления ботом
"""

token = private.token
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def create_first_lab(message):
	markup = telebot.types.ReplyKeyboardMarkup(True)
	markup.row('new','up',' ')
	markup.row('left', 'down', 'right')
	bot.send_message(message.chat.id, "Приффки", reply_markup=markup)
	lab=sql.get_lab(message.chat.id)
	if lab==0:
		lab = labirint.Labirint(height,width,wall_cell,space_cell,gamer_cell,1)
		lab = lab.to_text()
		sql.create_lab(message.chat.id,lab)
	else:
		lab=labirint.Labirint(height,width,wall_cell,space_cell,gamer_cell,1)
		lab=lab.to_text()
		sql.update_lab(message.chat.id,lab)
	bot.send_message(message.chat.id, lab)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
	lab=sql.get_lab(message.chat.id)
	is_win=0
	if lab!=0:
		if message.text=='left':
				is_win=lab.move_left()
		elif message.text == 'right':
				is_win=lab.move_right()
		elif message.text == 'down':
				is_win=lab.move_down()
		elif message.text == 'up':
				is_win=lab.move_up()
		lab=lab.to_text()
		sql.update_lab(message.chat.id,lab)
		bot.send_message(message.chat.id, lab)
		if is_win==1 or message.text=='new':
			message_text="Вот тебе новый:"
			bot.send_message(message.chat.id, message_text)
			lab=labirint.Labirint(height,width,wall_cell,space_cell,gamer_cell,1)
			lab=lab.to_text()
			sql.update_lab(message.chat.id,lab)
			bot.send_message(message.chat.id, lab)

#@bot.message_handler(commands=['new'])
#def create_new_lab(message):
#	message_text="Вот тебе новый:"
#	bot.send_message(message.chat.id, message_text)
#	lab=labirint.Labirint(height,width,wall_cell,space_cell,gamer_cell,1)
#	lab=lab.to_text()
#	sql.update_lab(message.chat.id,lab)
#	bot.send_message(message.chat.id, lab)

if __name__ == '__main__':
	bot.polling(none_stop=True)
