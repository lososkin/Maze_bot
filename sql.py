import sqlite3
import labirint
import settings

def get_lab(chat_id):
	conn = sqlite3.connect('lab.db')
	cursor = conn.cursor()
	chat_id=str(chat_id)
	cursor.execute("SELECT lab FROM user_and_lab where chat_id="+chat_id)
	result = cursor.fetchall()
	conn.close()
	if result==[]:
		return 0
	lab = labirint.Labirint(settings.height,settings.width,settings.wall_cell,settings.space_cell,settings.gamer_cell,0)
	strin = result[0][0]
	x=0
	y=0
	for i in range(0,len(strin)):
		if strin[i]=='\n':
			y+=1
			x=0
		elif strin[i]==settings.gamer_cell:
			lab.x=x
			lab.y=y
			lab.maze[y][x]=settings.space_cell
			x+=1
		else:
			lab.maze[y][x]=strin[i]
			x+=1
	return lab

def create_lab(chat_id,lab):
	conn = sqlite3.connect('lab.db')
	cursor = conn.cursor()
	chat_id=str(chat_id)
	#print(chat_id,lab)
	cursor.execute("INSERT INTO user_and_lab VALUES ({0}, '{1}') ".format(chat_id,lab))
	conn.commit()
	conn.close()

def update_lab(chat_id,lab):
	conn = sqlite3.connect('lab.db')
	cursor = conn.cursor()
	chat_id=str(chat_id)
	print(lab)
	cursor.execute("UPDATE user_and_lab SET lab = '{0}' WHERE chat_id = {1}".format(lab,chat_id))
	conn.commit()
	conn.close()
