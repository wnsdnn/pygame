import pygame

# pygame 초기화
pygame.init()

# 화면의 크기
screen_width = 700
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 40)
total_time = 60
start_ticks = pygame.time.get_ticks()

game_result = "Game Over"

# 배경 이미지 정의
background = pygame.image.load("C:\\Users\\User\\Desktop\\pikachyu_baegu\\image\\background.jpg")

# 밑바닥 이미지 정의
stage = pygame.image.load("C:\\Users\\User\\Desktop\\pikachyu_baegu\\image\\stage.jpg")
stage_size = stage.get_rect().size
stage_width = stage_size[0]
stage_height = stage_size[1]
stage_x_pos = 0
stage_y_pos = screen_height - stage_height

# 캐릭터 이미지 정의
character = pygame.image.load("C:\\Users\\User\\Desktop\\pikachyu_baegu\\image\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height
character_to_x = 0
character_speed = 10

# 공 이미지 정의
ball = pygame.image.load("C:\\Users\\User\\Desktop\\pikachyu_baegu\\image\\ball.png")
ball_size = ball.get_rect().size
ball_width = ball_size[0]
ball_height = ball_size[1]
ball_x_pos = 50
ball_y_pos = 50
ball_speed_x = 5
ball_speed_y = -25


running = True

# 시작
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 캐릭터 방향 조종 키 이벤트
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
        
    # 캐릭터가 화면 밖으로 안 나가게 하는 조건문
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    character_x_pos += character_to_x

    # 공의 x축 화면 밖으로 안 나가게 하는 조건문
    if ball_x_pos < 0 or ball_x_pos > screen_width - ball_width:
        ball_speed_x = ball_speed_x * -1

    ball_rect = ball.get_rect()
    ball_rect.left = ball_x_pos
    ball_rect.top = ball_y_pos

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    if character_rect.colliderect(ball_rect):
        ball_speed_y = -25
    else:
        ball_speed_y += 1
    
    if ball_y_pos + ball_height > screen_height - stage_height:
        ball_speed_y = 0
        running = False

    ball_x_pos += ball_speed_x
    ball_y_pos += ball_speed_y



    # 화면에 이미지 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (stage_x_pos, stage_y_pos))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ball, (ball_x_pos, ball_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render("Time: {}".format(int(total_time - elapsed_time)), True, (255, 255, 255))

    if total_time - elapsed_time <= 0:
        game_result = "Mission Complate"
        running = False

    screen.blit(timer, (10, 10))

    pygame.display.update()

# 게임 오버 메세지
msg = game_font.render(game_result, True, (255, 255, 0)) # 노란색
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

# 2초 대기
pygame.time.delay(2000)

pygame.quit()
