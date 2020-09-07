import pygame

pygame.init()  # 초기화

# 화면크기 설정
screen_width = 480
screen_heigth = 640
screen = pygame.display.set_mode((screen_width, screen_heigth))

# 화면 타이틀 설정
pygame.display.set_caption("Sechan Game")  # 게임이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/백세찬/Desktop/pygame/background.png")

# 캐릭터 불러오기
character = pygame.image.load("C:/Users/백세찬/Desktop/pygame/character.png")
character_size = character.get_rect().size  # 이미지 크기 불러오기
character_width = character_size[0]  # 캐릭터 가로 크기
character_heigth = character_size[1]  # 캐릭터 세로 크기
character_x_pos = (screen_width / 2) - \
    (character_width / 2)  # x축 - 화면 가운데에 캐릭터 위치
character_y_pos = screen_heigth - character_heigth  # y축 - 가장 아래에 캐릭터 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 enemy character
enemy = pygame.image.load("C:/Users/백세찬/Desktop/pygame/enemy.png")
enemy_size = enemy.get_rect().size  # 이미지 크기 불러오기
enemy_width = enemy_size[0]  # 캐릭터 가로 크기
enemy_heigth = enemy_size[1]  # 캐릭터 세로 크기
enemy_x_pos = (screen_width / 2) - \
    (enemy_width / 2)  # x축화면 가운데에 캐릭터 위치
enemy_y_pos = (screen_heigth / 2) - (enemy_heigth / 2)  # y축가장 아래에 캐릭터 위치


# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수 설정
    for event in pygame.event.get():  # 어떤 이벤트가 발생했는가
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 발생여부
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키 누름여부 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP:  # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                to_y += character_speed
        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_heigth - character_heigth:
        character_y_pos = screen_heigth - character_heigth

# 충돌 처리를 위한 rect 정보 업데이트
character_rect = character.get_rect()
character_rect.left = character_x_pos
character_rect.top = character_y_pos

enemy_rect = enemy.get_rect()
enemy_rect.left = enemy_x_pos
enemy_rect.top = enemy_y_pos

# 충돌 체크
if character_rect.colliderect(enemy_rect):
    print("충돌했습니다")
    running = False

screen.blit(background, (0, 0))  # 배경 그리기
screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기

pygame.display.update()  # 게임화면을 다시 그리기


# pygame 종료
pygame.quit()
