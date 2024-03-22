import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Player:
	COLOR = BLACK
	VEL = 2
	Y_VEL = 6
	def __init__(self, x, y, width, height, y_weight, move_right, move_left, move_up, move_down, attack, heavy_attack, block, left_facing):
		self.x = self.original_x = x
		self.y = self.original_y = y
		self.width = width
		self.height = height
		self.y_weight = y_weight
		self.x_weight = 0
		self.move_right = move_right
		self.move_left = move_left
		self.move_up = move_up
		self.move_down = move_down
		self.attack = attack
		self.jumps = 20
		self.is_jumping = False
		self.air_time = 5
		self.left_sliding = False
		self.right_sliding = False
		self.dmg_taken = 0
		self.stocks = self.original_stocks = 3
		self.left_facing = left_facing
		self.heavy_attack = heavy_attack
		self.block = block
		self.is_blocking = False
		self.is_hit = False
		self.is_walking = False
		self.is_launched = False
		self.on_cooldown = False
		self.cooldown_timer = 0
		self.charging = False
		self.charging_time = 0
		self.spawn_timer = 30

	def draw(self, win):
		pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

	def handle_movement(self, keys):
		if not (keys[self.move_left] or keys[self.move_right]):
			self.is_walking = False
		if keys[self.move_left] and not self.right_sliding:
			self.x-= self.VEL
			self.left_facing = True
			self.is_walking = True
		if keys[self.move_right] and not self.left_sliding:
			self.x+=self.VEL
			self.left_facing = False
			self.is_walking = True
		if keys[self.move_up] and self.jumps >=1:
			self.is_jumping = True
			self.jumps-=1
			# for _ in range(10):
			self.y-=self.Y_VEL

	def handle_attack(self, keys, attack):
		if attack.hold and not keys[self.heavy_attack]:
			attack.hold = False
			attack.name = 'big'
			attack.exists = True
			attack.timer = 30
			attack.dmg = 1
			if self.left_facing == True:
				attack.move = 'L'
			else:
				attack.move = 'R'
			self.on_cooldown = True
			self.cooldown_timer = 30
			if self.left_facing == False:
				attack.hitbox = [self.x+self.width, self.y+self.width*5/4, 20, 10]
			else:
				attack.hitbox = [self.x-20 ,self.y+self.width*5/4, 20, 10]
		if keys[self.attack] and keys[self.move_down] and not attack.exists and not self.on_cooldown:
			attack.exists = True
			attack.timer = 20
			attack.name = "kick"
			attack.dmg = 2
			self.on_cooldown = True
			self.cooldown_timer = 30
			if self.left_facing == False:
				attack.hitbox = [self.x+self.width, self.y+self.height*5/9, 20, 10]
			else:
				attack.hitbox = [self.x-20 ,self.y+self.height*5/9, 20, 10]
		elif keys[self.attack] and not attack.exists and not self.on_cooldown:
			attack.exists = True
			attack.timer = 20
			attack.name = "punch"
			attack.dmg = 1
			self.on_cooldown = True
			self.cooldown_timer = 30
			if self.left_facing == False:
				attack.hitbox = [self.x+self.width, self.y+self.width*5/4, 20, 10]
			else:
				attack.hitbox = [self.x-20 ,self.y+self.width*5/4, 20, 10]
		elif keys[self.heavy_attack] and (keys[self.move_right] or keys[self.move_left]) and not attack.exists and not self.on_cooldown:
			attack.exists = True
			attack.timer = 20
			attack.dmg = 1
			attack.name = "ki"
			if self.left_facing == True:
				attack.move = 'L'
			else:
				attack.move = 'R'
			self.on_cooldown = True
			self.cooldown_timer = 30
			if self.left_facing == False:
				attack.hitbox = [self.x+self.width, self.y+4/5*self.width, 10, 5]
			else:
				attack.hitbox = [self.x-20 ,self.y+4/5*self.width, 10, 5]
		elif keys[self.heavy_attack] and not attack.exists and not self.on_cooldown and not keys[self.move_down]:
			attack.hold = True
		if keys[self.move_down] and keys[self.heavy_attack] and not attack.exists and not attack.hold:
			if self.dmg_taken > 0:
				self.dmg_taken-=1
			self.charging = True
			self.charging_time+=1
		else:
			self.charging = False
			self.charging_time = 0
	
	def reset(self):
		self.x = self.original_x
		self.y = self.original_y
		self.dmg_taken = 0
		self.spawn_timer = 30
	
	def reset_stocks(self):
		self.stocks = self.original_stocks
		self.dmg_taken = 0
		self.spawn_timer = 30

	def handle_getting_hit(self, attack, attacking_player):
		player_hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
		attack_hitbox = pygame.Rect(attack.hitbox[0], attack.hitbox[1], attack.hitbox[2], attack.hitbox[3])
		if pygame.Rect.colliderect(player_hitbox, attack_hitbox) and attack.exists:
			intersection = attack_hitbox.clip(player_hitbox) 
			point_of_contact_x = intersection[0]+intersection[2]
			point_of_contact_y = intersection[1]+intersection[3]
			# mid_x = self.x + self.width//2
			# dist_x = mid_x - point_of_contact_x
			# if dist_x < 0:
			# 	self.x_weight = -attack.dmg
			# else:
			# 	self.x_weight = attack.dmg 
			disp_direction = self.x - attacking_player.x
			disp_force = max(2,attack.dmg*self.dmg_taken*0.1)
			if disp_direction < 0:
				self.x_weight = -disp_force
			else:
				self.x_weight = disp_force
			self.dmg_taken+=attack.dmg
			self.isHit = True
			self.cooldown_timer+=attack.timer
			# attack.exists = False
			# print(self.cooldown_timer)

	def update_cooldown(self):
		if self.cooldown_timer >= 1:
			self.cooldown_timer-=1
		if self.cooldown_timer == 0:
			self.on_cooldown = False
		if self.spawn_timer > 0:
			self.spawn_timer-=1