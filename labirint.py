import random
class Labirint:

	x=1
	y=1
	height = 0
	width = 0
	maze = []
	wall = "l"
	space = " "
	gamer = "i"

	def __init__(self,height_, width_,wall_,space_,gamer_, generate_valid_maze):
		"""
		https://habr.com/post/262345/ - описание алгоритма построения
		genearte_valid_maze - нужно ли генерировать валидный лабиринт или он будет считан из бд
		"""
		self.x=1
		self.y=1
		self.maze = []
		self.wall = wall_
		self.height = height_
		self.width = width_
		self.space = space_
		self.gamer = gamer_

		for x1 in range(0,height_):
			self.maze.append(list(wall_*width_))
		for x1 in range(0,height_):
			for x2 in range(0,width_):
				if x1 % 2 != 0  and x2 % 2 != 0 and x1!=height_-1 and x2!= width_-1 and x1!=0 and x2!=0:
					self.maze[x1][x2]=space_
		if generate_valid_maze==1:
			x=1
			y=1
			stack=[[x,y]]
			history = [[x,y]]
			while 1:
				cages_is_available_for_move = [0,0,0,0] #left,right,up,down
				if x!=1 and self.maze[y][x-1]==self.wall and [x-2,y] not in history:
					cages_is_available_for_move[0]=1
				if x!=self.width-2 and self.maze[y][x+1]==self.wall  and [x+2,y] not in history:
					cages_is_available_for_move[1]=1
				if y!=1 and self.maze[y-1][x]==self.wall  and [x,y-2] not in history:
					cages_is_available_for_move[2]=1
				if y!=self.height-2 and self.maze[y+1][x]==self.wall  and [x,y+2] not in history:
					cages_is_available_for_move[3]=1
				
				is_cage_available_for_move=0
				for i in range(0,4):
					is_cage_available_for_move+=cages_is_available_for_move[i]

				if(is_cage_available_for_move):
					while 1:
						ran = int(random.random()*10)%4
						if(cages_is_available_for_move[ran]==1):
							move_direction = ran
							break

					if ran==0:
						self.maze[y][x-1]=self.space
						x-=2
					elif ran==1:
						self.maze[y][x+1]=self.space
						x+=2
					elif ran==2:
						self.maze[y-1][x]=self.space
						y-=2
					elif ran==3:
						self.maze[y+1][x]=self.space
						y+=2
					stack.append([x,y])
					history.append([x,y])
				else:
					stack.pop()
					x=stack[len(stack)-1][0]
					y=stack[len(stack)-1][1]
					if x==1 and y==1:
						break
		self.maze[height_-2][width_-2]= u'\U0001F3C1'

	def print_lab(self):
		for x in range(self.height):
			for x2 in range(self.width):
				if x==self.y and x2==self.x :
					print(self.gamer,end="")
				else:
					print(self.maze[x][x2],end="")
			print()

	def move_left(self):
		if self.maze[self.y][self.x-1]==self.wall:
			print("left_ne_vishlo")
			return -1
		else:
			self.x-=1
			print("poshel na levo",self.x,self.y)
			if self.x==self.width-2 and self.y==self.height-2:
				print("Ты классный!")
				return 1
			else: 
				return 0

	def move_right(self):
		if self.maze[self.y][self.x+1]==self.wall:
			print("right_ne_vishlo")
			return -1
		else:
			self.x+=1
			print("poshel na right",self.x,self.y)
			if self.x==self.width-2 and self.y==self.height-2:
				print("Ты классный!")
				return 1
			else: 
				return 0

	def move_up(self):
		if self.maze[self.y-1][self.x]==self.wall:
			print("up_ne_vishlo")
			return -1
		else:
			self.y-=1
			print("poshel up",self.x,self.y)
			if self.x==self.width-2 and self.y==self.height-2:
				print("Ты классный!")
				return 1
			else: 
				return 0

	def move_down(self):
		if self.maze[self.y+1][self.x]==self.wall:
			print("down_ne_vishlo")
			return -1
		else:
			self.y+=1
			print("poshel down",self.x,self.y)
			if self.x==self.width-2 and self.y==self.height-2:
				print("Ты классный!")
				return 1
			else: 
				return 0

	def to_text(self):
		str_lab=""
		for y in range(self.height):
			for x in range(self.width):
				if self.y==y and x==self.x:
					str_lab+=self.gamer
				else:
					str_lab+=str(self.maze[y][x])
			str_lab+="\n"
		return str_lab

