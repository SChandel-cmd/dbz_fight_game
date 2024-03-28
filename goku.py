import pygame
import math

pygame.mixer.init()
class Goku:
	# music_file = "assets/music/fight_music.mp3"
    charging_sound = pygame.mixer.Sound("assets/sound_fx/goku_power_up.mp3")
    charging_sound.set_volume(0.4)
    charging_aura_sound = pygame.mixer.Sound("assets/sound_fx/charge_aura.mp3")
    teleport_sound = pygame.mixer.Sound("assets/sound_fx/teleport.mp3")
    teleport_sound.set_volume(0.5)
    jump_1_sound = pygame.mixer.Sound("assets/sound_fx/jump_1_new.mp3")
    kamehame_sound = pygame.mixer.Sound("assets/sound_fx/kamehame.mp3")
    kamehame_beam_sound = pygame.mixer.Sound("assets/sound_fx/kamehame_beam.mp3")
    ha_sound = pygame.mixer.Sound("assets/sound_fx/ha.mp3")
    ha_beam_sound = pygame.mixer.Sound("assets/sound_fx/ha_beam.mp3")
    ki_blast_1_sound = pygame.mixer.Sound("assets/sound_fx/ki_blast_1.mp3")
    ki_blast_2_sound = pygame.mixer.Sound("assets/sound_fx/ki_blast_2.mp3")
    icon = pygame.image.load('assets/sprites/goku_processed/goku_icon.png')
    icon = pygame.transform.scale(icon, (70, 250))
    crop_area = pygame.Rect(0, 10, icon.get_width(), icon.get_height() // 3.25)
    cropped_icon = pygame.Surface((crop_area.width, crop_area.height))
    cropped_icon.blit(icon, (0, 0), crop_area)
    cropped_icon.set_colorkey((0,0,0))
    def draw(self, win, player, attack):
        attack_image = None
        goku_image = pygame.image.load('assets/sprites/goku_processed/goku_idle.png').convert()
        if not player.charging:
            self.charging_sound.stop()
            self.charging_aura_sound.stop()
        if not attack.hold:
            self.kamehame_sound.stop()
            self.kamehame_beam_sound.stop()
        if player.spawn_timer!=0:
            if player.spawn_timer == 29:
                self.teleport_sound.play()
            if player.spawn_timer>=20:
                goku_image = pygame.image.load('assets/sprites/goku_processed/goku_spawn_1.png').convert()
            elif player.spawn_timer>=10:
                goku_image = pygame.image.load('assets/sprites/goku_processed/goku_spawn_2.png').convert()
            else:
                goku_image = pygame.image.load('assets/sprites/goku_processed/goku_spawn_3.png').convert()

        if player.left_sliding:
            goku_image = pygame.image.load('assets/sprites/goku_processed/goku_slide.png').convert()
            goku_image = pygame.transform.flip(goku_image, True, False)
        if player.right_sliding:
            goku_image = pygame.image.load('assets/sprites/goku_processed/goku_slide.png').convert()
        if player.is_jumping:
            if player.jumps == 19:
                self.jump_1_sound.play()
            if player.jumps > 16:
                goku_image = pygame.image.load('assets/sprites/goku_processed/goku_jump_1.png').convert()
            elif player.jumps > 12:
                goku_image = pygame.image.load('assets/sprites/goku_processed/goku_jump_2.png').convert()
            elif player.jumps > 8:
                goku_image = pygame.image.load('assets/sprites/goku_processed/goku_jump_3.png').convert()
            elif player.jumps > 4:
                goku_image = pygame.image.load('assets/sprites/goku_processed/goku_jump_4.png').convert()
            else:
                goku_image = pygame.image.load('assets/sprites/goku_processed/goku_jump_5.png').convert()
        if player.is_walking:
            goku_image = pygame.image.load('assets/sprites/goku_processed/goku_move.png').convert()         
        if player.charging:
            if player.charging_time == 1:
                self.charging_sound.play()
                self.charging_aura_sound.play(loops=-1)
            if player.charging_time <= 10:
                goku_image = pygame.image.load('assets/sprites/goku_processed/goku_charge_1.png').convert()
            elif player.charging_time <= 60:
                if player.charging_time%30 > 15:
                    goku_image = pygame.image.load('assets/sprites/goku_processed/goku_charge_2.png').convert()
                else:
                    goku_image = pygame.image.load('assets/sprites/goku_processed/goku_charge_3.png').convert()
            else:
                if player.charging_time%20 > 10:
                    goku_image = pygame.image.load('assets/sprites/goku_processed/goku_charge_2.png').convert()
                else:
                    goku_image = pygame.image.load('assets/sprites/goku_processed/goku_charge_3.png').convert()
        if attack.exists:
            if attack.name == 'punch':
                if attack.timer >= 15:
                    goku_image = pygame.image.load('assets/sprites/goku_processed/goku_punch_1.png').convert()
                elif attack.timer >= 10:
                    goku_image = pygame.image.load('assets/sprites/goku_processed/goku_punch_2.png').convert()
                else:
                    goku_image = pygame.image.load('assets/sprites/goku_processed/goku_punch_3.png').convert()
            elif attack.name == 'kick':
                if attack.timer >= 15:
                    goku_image = pygame.image.load('assets/sprites/goku_processed/goku_kick_1.png').convert()
                elif attack.timer >= 10:
                    goku_image = pygame.image.load('assets/sprites/goku_processed/goku_kick_2.png').convert()
                else:
                    goku_image = pygame.image.load('assets/sprites/goku_processed/goku_kick_3.png').convert()
            elif attack.name == 'big':
                if attack.timer == 29:
                    self.ha_sound.play()
                    self.ha_beam_sound.play()
                if attack.timer%8 < 4:
                    goku_image = pygame.image.load('assets/sprites/goku_processed/goku_big_8.png').convert()
                else:
                    goku_image = pygame.image.load('assets/sprites/goku_processed/goku_big_9.png').convert()
                stage = math.ceil((31-attack.timer)/3)
                attack_image = pygame.image.load('assets/sprites/entities_processed/kamehameha_'+str(stage)+'.png').convert()
            elif attack.name == 'ki':
                if attack.timer == 19:
                    self.ki_blast_2_sound.play()
                if attack.timer >= 19:
                    goku_image = pygame.image.load('assets/sprites/goku_processed/goku_ki_2.png').convert()
                elif attack.timer >= 17:
                    goku_image = pygame.image.load('assets/sprites/goku_processed/goku_ki_3.png').convert()
                if attack.timer%10 > 5:
                    attack_image = pygame.image.load('assets/sprites/entities_processed/ki_1.png').convert()
                else:
                    attack_image = pygame.image.load('assets/sprites/entities_processed/ki_2.png').convert()

        if attack.hold:
            if attack.timer == 1:
                self.kamehame_sound.play()
                self.kamehame_beam_sound.play(loops=-1)
            if attack.timer <= 15:
                goku_image = pygame.image.load('assets/sprites/goku_processed/goku_big_1.png').convert()
            elif attack.timer < 32:
                goku_image = pygame.image.load('assets/sprites/goku_processed/goku_big_2.png').convert()
            elif attack.timer%40 >= 32:
                goku_image = pygame.image.load('assets/sprites/goku_processed/goku_big_3.png').convert()
            elif attack.timer%40 >= 24:
                goku_image = pygame.image.load('assets/sprites/goku_processed/goku_big_4.png').convert()
            elif attack.timer%40 >= 16:
                goku_image = pygame.image.load('assets/sprites/goku_processed/goku_big_5.png').convert()
            elif attack.timer%40 >= 8:
                goku_image = pygame.image.load('assets/sprites/goku_processed/goku_big_6.png').convert()
            else:
                goku_image = pygame.image.load('assets/sprites/goku_processed/goku_big_7.png').convert()
        if player.left_facing and not (player.left_sliding or player.right_sliding):
                goku_image = pygame.transform.flip(goku_image, True, False)  
        goku_image.set_colorkey((0,0,0))
        # image_width, image_height = self.icon.get_size()
        # square_size = 48
        # square_surface = pygame.Surface((square_size, square_size))
        # offset_x = (square_size - image_width) // 2
        # offset_y = (square_size - image_height) // 2
        # square_surface.blit(self.icon, (offset_x, offset_y))
        win.blit(self.cropped_icon, (90,0))
        if player.charging and not attack.hold:
            goku_image = pygame.transform.scale(goku_image, (player.width*5/4, player.height*5/4))
            win.blit(goku_image, (player.x, player.y-player.height*1/4))
        elif attack.hold:
            if attack.timer <= 15:
                goku_image = pygame.transform.scale(goku_image, (player.width, player.height))
                win.blit(goku_image, (player.x, player.y))
            elif attack.timer < 32:
                goku_image = pygame.transform.scale(goku_image, (player.width*1.2, player.height*1.2))
                win.blit(goku_image, (player.x-10, player.y-10))
            elif attack.timer%40 >= 32:
                goku_image = pygame.transform.scale(goku_image, (player.width*1.21, player.height*1.21))
                win.blit(goku_image, (player.x-11, player.y-11))
            elif attack.timer%40 >= 24:
                goku_image = pygame.transform.scale(goku_image, (player.width*1.2, player.height*1.2))
                win.blit(goku_image, (player.x-9, player.y-1))
            elif attack.timer%40 >= 16:
                goku_image = pygame.transform.scale(goku_image, (player.width*1.2, player.height*1.2))
                win.blit(goku_image, (player.x-10, player.y-6))
            elif attack.timer%40 >= 8:
                goku_image = pygame.transform.scale(goku_image, (player.width*1.1, player.height*1.1))
                win.blit(goku_image, (player.x-9, player.y-5))
            else:
                goku_image = pygame.transform.scale(goku_image, (player.width*1.2, player.height*1.2))
                win.blit(goku_image, (player.x-8, player.y-6))
        else:
            goku_image = pygame.transform.scale(goku_image, (player.width, player.height))
            win.blit(goku_image, (player.x, player.y))
            if attack_image:
                attack_image.set_colorkey((0,0,0))
                if attack.move == 'L':
                    attack_image = pygame.transform.flip(attack_image, True, False)  
                attack_x = attack.hitbox[0]
                attack_y = attack.hitbox[1]
                if attack.name == 'big':
                    attack_image = pygame.transform.scale(attack_image, (attack_image.get_width()*0.4, attack_image.get_height()*0.4))
                    if player.left_facing:
                        attack_x-=35
                    else:
                        attack_x-=10
                    attack_y-=20
                elif attack.name =='ki':
                    attack_image = pygame.transform.scale(attack_image, (attack_image.get_width()*0.2, attack_image.get_height()*0.2))

                win.blit(attack_image, (attack_x ,attack_y))
                
		# pygame.draw.rect(win, self.COLOR, (player.x, player.y, self.width, self.height))
    
