import pygame
import math

pygame.mixer.init()
class Vegeta:
    charging_sound = pygame.mixer.Sound("assets/sound_fx/vegeta_power_up.mp3")
    charging_sound.set_volume(0.35)
    charging_aura_sound = pygame.mixer.Sound("assets/sound_fx/charge_aura.mp3")
    teleport_sound = pygame.mixer.Sound("assets/sound_fx/teleport.mp3")
    teleport_sound.set_volume(0.5)
    jump_1_sound = pygame.mixer.Sound("assets/sound_fx/jump_1_new.mp3")
    galick_sound = pygame.mixer.Sound("assets/sound_fx/galick.mp3")
    galick_sound.set_volume(0.5)
    galick_beam_sound = pygame.mixer.Sound("assets/sound_fx/galick_beam.mp3")
    galick_gun_sound = pygame.mixer.Sound("assets/sound_fx/galick_gun.mp3")
    galick_gun_sound.set_volume(0.5)
    galick_gun_beam_sound = pygame.mixer.Sound("assets/sound_fx/galick_gun_beam.mp3")
    ki_blast_1_sound = pygame.mixer.Sound("assets/sound_fx/ki_blast_1.mp3")
    ki_blast_2_sound = pygame.mixer.Sound("assets/sound_fx/ki_blast_2.mp3")
    icon = pygame.image.load('assets/sprites/vegeta_processed/vegeta_icon.png')
    icon = pygame.transform.scale(icon, (50, 220))
    crop_area = pygame.Rect(0, 10, icon.get_width(), icon.get_height() // 3)
    cropped_icon = pygame.Surface((crop_area.width, crop_area.height))
    cropped_icon.blit(icon, (0, 0), crop_area)
    cropped_icon.set_colorkey((0,0,0))
    def draw(self, win, player, attack):
        attack_image = None
        vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_idle.png').convert()
        if not player.charging:
            self.charging_sound.stop()
            self.charging_aura_sound.stop()
        if not attack.hold:
            self.galick_sound.stop()
            self.galick_beam_sound.stop()
        if player.spawn_timer!=0:
            if player.spawn_timer == 29:
                self.teleport_sound.play()
            if player.spawn_timer>=20:
                vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_spawn_1.png').convert()
            elif player.spawn_timer>=10:
                vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_spawn_2.png').convert()
            else:
                vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_spawn_3.png').convert()

        if player.left_sliding:
            vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_slide.png').convert()
            vegeta_image = pygame.transform.flip(vegeta_image, True, False)
        if player.right_sliding:
            vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_slide.png').convert()
        if player.is_jumping:
            if player.jumps == 19:
                self.jump_1_sound.play()
            if player.jumps > 16:
                vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_jump_1.png').convert()
            elif player.jumps > 12:
                vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_jump_2.png').convert()
            elif player.jumps > 8:
                vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_jump_3.png').convert()
            elif player.jumps > 4:
                vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_jump_4.png').convert()
            else:
                vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_jump_5.png').convert()
        if player.is_walking:
            vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_move.png').convert()         
        if player.charging:
            if player.charging_time == 1:
                self.charging_sound.play()
                self.charging_aura_sound.play(loops=-1)
            if player.charging_time <= 10:
                vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_charge_1.png').convert()
            elif player.charging_time <= 60:
                if player.charging_time%30 > 15:
                    vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_charge_2.png').convert()
                else:
                    vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_charge_3.png').convert()
            else:
                if player.charging_time%20 > 10:
                    vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_charge_2.png').convert()
                else:
                    vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_charge_3.png').convert()
        if attack.exists:
            if attack.name == 'punch':
                if attack.timer >= 15:
                    vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_punch_1.png').convert()
                elif attack.timer >= 10:
                    vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_punch_2.png').convert()
                else:
                    vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_punch_3.png').convert()
            elif attack.name == 'kick':
                if attack.timer >= 15:
                    vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_kick_1.png').convert()
                elif attack.timer >= 10:
                    vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_kick_2.png').convert()
                else:
                    vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_kick_3.png').convert()
            elif attack.name == 'big':
                if attack.timer == 29:
                    self.galick_gun_sound.play()
                    self.galick_gun_beam_sound.play()
                if attack.timer%8 < 4:
                    vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_big_8.png').convert()
                else:
                    vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_big_9.png').convert()
                stage = math.ceil((31-attack.timer)/4)
                attack_image = pygame.image.load('assets/sprites/entities_processed/galick_gun_'+str(stage)+'.png').convert()
            elif attack.name == 'ki':
                if attack.timer == 19:
                    self.ki_blast_2_sound.play()
                if attack.timer >= 19:
                    vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_ki_2.png').convert()
                elif attack.timer >= 17:
                    vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_ki_3.png').convert()
                if attack.timer%10 > 5:
                    attack_image = pygame.image.load('assets/sprites/entities_processed/ki_1.png').convert()
                else:
                    attack_image = pygame.image.load('assets/sprites/entities_processed/ki_2.png').convert()

        if attack.hold:
            if attack.timer == 1:
                self.galick_sound.play()
                self.galick_beam_sound.play(loops=-1)
            if attack.timer <= 15:
                vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_big_1.png').convert()
            elif attack.timer < 32:
                vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_big_2.png').convert()
            elif attack.timer%40 >= 32:
                vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_big_3.png').convert()
            elif attack.timer%40 >= 24:
                vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_big_4.png').convert()
            elif attack.timer%40 >= 16:
                vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_big_5.png').convert()
            elif attack.timer%40 >= 8:
                vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_big_6.png').convert()
            else:
                vegeta_image = pygame.image.load('assets/sprites/vegeta_processed/vegeta_big_7.png').convert()
        if player.left_facing and not (player.left_sliding or player.right_sliding):
                vegeta_image = pygame.transform.flip(vegeta_image, True, False)  
        vegeta_image.set_colorkey((0,0,0))
        # image_width, image_height = vegeta_image.get_size()
        # square_size = 48
        # square_surface = pygame.Surface((square_size, square_size))
        # offset_x = (square_size - image_width) // 2
        # offset_y = (square_size - image_height) // 2
        # square_surface.blit(vegeta_image, (offset_x, offset_y))
        # win.blit(square_surface, (560,20))
        win.blit(self.cropped_icon, (560,10))
        if player.charging and not attack.hold:
            vegeta_image = pygame.transform.scale(vegeta_image, (player.width*5/4, player.height*5/4))
            win.blit(vegeta_image, (player.x, player.y-player.height*1/4))
        elif attack.hold:
            if attack.timer <= 15:
                vegeta_image = pygame.transform.scale(vegeta_image, (player.width, player.height))
                win.blit(vegeta_image, (player.x, player.y))
            elif attack.timer < 32:
                vegeta_image = pygame.transform.scale(vegeta_image, (player.width*1.2, player.height*1.2))
                win.blit(vegeta_image, (player.x-10, player.y-10))
            elif attack.timer%40 >= 32:
                vegeta_image = pygame.transform.scale(vegeta_image, (player.width*1.21, player.height*1.21))
                win.blit(vegeta_image, (player.x-11, player.y-11))
            elif attack.timer%40 >= 24:
                vegeta_image = pygame.transform.scale(vegeta_image, (player.width*1.2, player.height*1.2))
                win.blit(vegeta_image, (player.x-9, player.y-1))
            elif attack.timer%40 >= 16:
                vegeta_image = pygame.transform.scale(vegeta_image, (player.width*1.2, player.height*1.2))
                win.blit(vegeta_image, (player.x-10, player.y-6))
            elif attack.timer%40 >= 8:
                vegeta_image = pygame.transform.scale(vegeta_image, (player.width*1.1, player.height*1.1))
                win.blit(vegeta_image, (player.x-9, player.y-5))
            else:
                vegeta_image = pygame.transform.scale(vegeta_image, (player.width*1.2, player.height*1.2))
                win.blit(vegeta_image, (player.x-8, player.y-6))
        else:
            vegeta_image = pygame.transform.scale(vegeta_image, (player.width, player.height))
            win.blit(vegeta_image, (player.x, player.y))
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
    
