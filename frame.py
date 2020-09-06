import pygame

pygame.init()  # 초기화

# 화면크기 설정
screen_width = 480
screen_heigth = 640
screen = pygame.display.set_mode((screen_width, screen_heigth))

# 화면 타이틀 설정
pygame.display.set_caption("Sechan Game")  # 게임이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/백세찬/Desktop/pygame/background.png")

# 캐릭터 불러오기
character = pygame.image.load("C:/Users/백세찬/Desktop/pygame/character.png")
character_size = character.get_rect().size  # 이미지 크기 불러오기
character_width = character_size[0]  # 캐릭터 가로 크기
character_heigth = character_size[1]  # 캐릭터 세로 크기
character_x_pos = screen_width / 2  # x축 - 화면 가운데에 캐릭터 위치
character_y_pos = screen_heigth - character_heigth  # y축 - 가장 아래에 캐릭터 위치

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생했는가
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 발생여부
            running = False  # 게임이 진행중이 아님

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.update()  # 게임화면을 다시 그리기


# pygame 종료
pygame.quit()
