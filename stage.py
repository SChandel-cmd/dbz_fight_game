import pygame

WHITE = (255, 255, 255)
HEIGHT = 500
WIDTH = 700
class Stage:
	COLOR = WHITE
	def __init__(self, x, y, width, height):
		self.x = self.original_x = x
		self.y = self.original_y = y
		self.width = width
		self.height = height

	def draw(self, win):
		pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))
		
	def activate_y_gravity(self, entity):
		if (entity.x >= self.x and entity.x + entity.width <= self.x + self.width and
				entity.y + entity.height - 5 >= self.y and entity.y <= self.y + self.height):
			entity.is_jumping = False
			entity.jumps = 20
			pass
		else:
			if entity.left_sliding or entity.right_sliding:
				entity.y += entity.y_weight//2
			else:
				entity.y += entity.y_weight
	
	def activate_x_gravity(self, entity):
		entity.x += entity.x_weight

	def handle_sliding(self, entity):
		if entity.x + entity.width - 5 >= self.x and entity.x + entity.width <= self.x + 10 and entity.y + entity.height >= self.y and entity.y + entity.height <= self.y + self.height:
			entity.left_sliding = True
			entity.is_jumping = False
			entity.jumps = 20
		else:
			entity.left_sliding = False
		if entity.x <= self.x + self.width and entity.x >= self.x + self.width - 5 and entity.y + entity.height >= self.y and entity.y + entity.height <= self.y + self.height:
			entity.right_sliding = True
			entity.is_jumping = False
			entity.jumps = 20
		else:
			entity.right_sliding = False

	def handle_out_of_bounds(self, entity):
		if entity.x < 0 or entity.x > WIDTH or entity.y < 0 or entity.y > HEIGHT:
			entity.stocks-=1
			entity.reset()


