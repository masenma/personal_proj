import pygame
import os
import math
from Game_Logic import get_result
from decimal import Decimal



WIDTH, HEIGHT = 1200, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crash")

PURPLEISH = (70, 62, 82)
BLACK = (0, 0, 0)

BACKGROUND = pygame.image.load(os.path.join("Assets", "Digital.png"))
BACKGROUND_SURFACE = pygame.transform.scale(BACKGROUND, (1200, 750))

BACKGROUND_MOVING = pygame.image.load(os.path.join("Assets", "Digital.png"))
BG = pygame.transform.scale(BACKGROUND_MOVING, (1200, 750))
BG_FLIPPED = pygame.transform.flip(BG, True, False)
BG_width = BG.get_width()
BG_height = BG.get_height()



FPS = 60
COIN_WIDTH, COIN_HEIGHT = 130, 130


YELLOW_COIN_IMAGE = pygame.image.load(os.path.join("Assets", "BitCOIN_image.png"))
YELLOW_COIN = pygame.transform.scale(YELLOW_COIN_IMAGE, (COIN_WIDTH, COIN_HEIGHT))

pygame.font.init()

button = pygame.Rect(480, 300, 140, 80)
button_color = (0, 0, 0)
text_color = (0, 222, 255)
font = pygame.font.Font(None, 36)
text = font.render("Start", True, (0, 222, 255))

end_button = pygame.Rect(480, 300, 140, 80)
end_button_color = (0, 222, 255)









    

WIN.blit(BG, (0, 0))

    


def main():

    with open('user_bank.txt', 'r') as file:
        bank_value = file.read()
        bank_value = round(float(bank_value), 2)
        print(bank_value)

    with open('prev_games.txt', 'r') as file:
        values_str = file.read().split(',')
        last_10_values = [val.strip(" '[]") for val in values_str[-10:] if val.strip(" '[]")]
        last_10_values = [float(x) for x in last_10_values]
        

    
    Flagged = True
    #Code for init_ input box
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = pygame.Rect(50, 200, 25, 500)
    color_active = (0, 0, 0)
    color_passive = (0, 0, 0)
    color = color_passive
    active = False
    


    yellow = pygame.Rect(275, 520, COIN_WIDTH, COIN_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    clock.tick(FPS)
    i = 0
    button_down = False
    end_button_down = False
    pull = False
    last_10_values = last_10_values[::-1]
    while run:
        
        pygame.draw.rect(WIN, (0,0,0), (0, 650, 2000, 100))
        
        
        prev_game_text = font.render(f'Last 10 Multipliers: {", ".join(str(val) + "x" for val in last_10_values)}', True, (0, 222, 255))
        prev_game_rect = prev_game_text.get_rect()
        prev_game_rect.center = (600, 700)
       
        WIN.blit(prev_game_text, prev_game_rect)
        

        pygame.draw.rect(WIN, (0, 0, 0), (0, 0, 2000, 100))
        bank_text = font.render(f"Balance: ${bank_value}", True, (0, 222, 255))

        # Get the rectangle that fits the text surface
        bank_rect = bank_text.get_rect()

        
        bank_rect.x = 500
        bank_rect.y = 25
        WIN.blit(bank_text, bank_rect)

        
        
        
        
        

        

    
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
                    

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    button_down = True
            
            

               
                
                
                



                if button_down:
                    


                    def count_down(start, end, step):
    
                        num = start
                        while num >= end:
                            yield num
                            num -= step
                    countdown_start = Decimal('3.0')
                    countdown_end = Decimal('0.0')
                    countdown_step = Decimal('1.0')
                    for num in count_down(countdown_start, countdown_end, countdown_step):
                        # update the timer text
                        
                        timer_text = font.render(str(num), True, (0, 222, 255))
                        timer_rect = timer_text.get_rect(center=(WIDTH/2, HEIGHT/2))
                        pygame.time.wait(1000)
                        WIN.blit(BG, (0, 0))
                        WIN.blit(YELLOW_COIN, (yellow.x, yellow.y))
                        WIN.blit(timer_text, timer_rect)
                        pygame.display.update()
                        clock.tick(FPS)
                    



                     

                


                    game_hash = "77b271fe12fca03c61863dfb79d4105726ba9d4a25bb3f1964e435ccf9cb209"
                    try:
                        result = str(get_result(game_hash))
                        print("Crash @: ", result + "x")
                        Prize = round(float(user_text) * float(result), 2)
                    except:
                        user_text = ""
                        main()
                    
                    

               
                    


                #if pull:
                    

                counter = 1
                counter_step = 0.1
                counter_speed_start = 0.01
                counter_speed_multiplier = 1.1
                counter_max = 1000.0

                while button_down:
                    

                    

                    pygame.draw.rect(WIN, end_button_color, end_button)
                    pygame.display.update()

                    WIN.fill((0, 0, 0))
                    WIN.blit(BG, (i, 0))
                    WIN.blit(BG, (WIDTH + i, 0))
                    if i == -WIDTH:
                        WIN.blit(BG, (WIDTH + i, 0))
                        i = 0
                    i -= 1
                    
                    pygame.draw.rect(WIN, end_button_color, end_button)
                    yellow.y = 425 + (math.sin(pygame.time.get_ticks() / 150) * 150)  # Adjust amplitude with 50

                    if yellow.y < 0:
                        yellow.y = 0

   
                    WIN.blit(YELLOW_COIN, (yellow.x, yellow.y))

                    counter_step = counter_speed_start * (counter_speed_multiplier ** counter/7) 
                    counter += counter_step

                # Render counter text
                    counter_text = pygame.font.SysFont(None, 36).render("{:.2f}x".format(counter), True, ((0, 222, 255)))
                    
                    
                    WIN.blit(counter_text, (10, 10))

                    

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if end_button.collidepoint(event.pos):
                                end_button_down = True
                    if end_button_down:
                        pulled_text = pygame.font.SysFont(None, 36).render("Bet pulled", True, (0, 0, 0))
                        WIN.blit(pulled_text, (500, 300))
                        pull = True
                        
                    if Flagged == True:
                        if pull == True:
                            real_prize = round(float(user_text) * counter, 2)
                            print("Pulled out")
                            print("Amount entered: ", user_text)
                            print("Multplier: ", round(counter, 2))
                            print("How much won: ", real_prize)
                            Flagged = False
                    

                    if counter >= float(result):
                        if pull == True:
                            counter = float(result)
                            
                            Winning_text = pygame.font.SysFont(None, 36).render("Winnings: ${:.2f}".format(real_prize), True, ((0, 222, 255)))
                            
                            
                           
                            with open('user_bank.txt', 'r') as f:
                                current_balance = float(f.read())


                                current_balance += real_prize


                            with open('user_bank.txt', 'w') as f:
                                f.write(str(current_balance))
                            with open('prev_games.txt', 'a', newline='') as f:
                                f.write(str(f'{result},'))
                            WIN.blit(BG, (0, 0))
                            WIN.blit(Winning_text, (250, 250))
                            main()

                        elif pull == False:
                            counter = float(result)
                            
                            Losing_text = pygame.font.SysFont(None, 36).render("Should've Pulled Out", True, ((0, 222, 255)))
                            
                            with open('user_bank.txt', 'r') as file:
                                bank_value = float(file.read())
                                user_value = float(user_text)
                                new_balance = bank_value - user_value
                                with open('user_bank.txt', 'w') as file:
                                    file.write(str(new_balance))
                                with open('prev_games.txt', 'a', newline='') as f:
                                    f.write(str(f'{result},'))
                            WIN.blit(BG, (0, 0))
                            WIN.blit(Losing_text, (250, 250))
                            main()

                    
                    
                    
                    
                    #pygame.wait
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            button_down = False
                            run = False
                    
            

            if event.type == pygame.QUIT:
                run = False

            
      
        
        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(WIN, color, input_rect)
        text_surface = base_font.render(f"${user_text}", True, ((0, 222, 255)))
        WIN.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, text_surface.get_width()+10)
        


        pygame.draw.rect(WIN, button_color, button)
        WIN.blit(text, (520, 325))

        
        




      

        WIN.blit(YELLOW_COIN, (yellow.x, yellow.y))

    

               
        
     
        
      

        


        
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
