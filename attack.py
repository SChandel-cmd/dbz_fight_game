import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Attack:
	COLOR = WHITE
	def __init__(self, player):
		self.player = player
		self.exists = False
		self.hitbox = [0, 0, 0, 0]
		self.timer = 0
		self.dmg = 0
		self.move = False
		self.hold = False
		self.name = ""
	
	def draw(self, win):
		if self.exists:
			pygame.draw.rect(win, self.COLOR, (self.hitbox[0], self.hitbox[1], self.hitbox[2], self.hitbox[3]))

	def update(self, player):
		if self.hold == True:
			self.timer+=1
			return 
		if self.move == 'R':
			if self.name =='ki':
				self.hitbox[0]+=3
			if self.name == 'big':
				self.hitbox[2]+=3
		if self.move == 'L':
			if self.name == 'ki':
				self.hitbox[0]-=3
			if self.name == 'big':
				self.hitbox[2]+=3
				self.hitbox[0]-=3
		if self.timer > 0:
			self.timer -= 1
		if self.timer == 0:
			self.move = False
			player.x_weight = 0
			self.exists = False
			self.hitbox = [0, 0, 0, 0]
	
