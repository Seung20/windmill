import pygame
import numpy as np

# 게임 윈도우 크기
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700

# 색 정의
BLACK = (0, 0, 0)
BLUE = (135,206,235)
GREY= (150, 150, 150)

def Rmat(deg):
    radian = np.deg2rad(deg)
    c = np.cos(radian)
    s = np.sin(radian)
    R = np.array( [[ c, -s, 0], [s, c, 0], [0, 0, 1] ] )
    return R
#rpimat함수는 풍차의 wing을 회전시켜줘 wing2, wing3, wing4를 만드는 함수이다.
def rpimat(n):
    radian = np.deg2rad(90*n)
    c = np.cos(radian)
    s = np.sin(radian)
    R = np.array( [[ c, -s, 0], [s, c, 0], [0, 0, 1] ] )
    return R

def Tmat(a,b):
    H = np.eye(3)
    H[0,2] = a
    H[1,2] = b
    return H


# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Drawing")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# 게임 종료 전까지 반복
done = False
# 폰트 선택(폰트, 크기, 두껍게, 이탤릭)
font = pygame.font.SysFont('FixedSys', 40, True, False)

# poly: 4 x 3 matrix
poly = np.array( [[0, 25, 1], [200, 0, 1], [200, 50, 1]])
poly = poly.T # 3x4 matrix 

cor = np.array([25, 25, 1])

degree = 0

# 게임 반복 구간
while not done:
# 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

# 윈도우 화면 채우기
    screen.fill(BLUE)
    degree += 1
    
    H = Tmat(WINDOW_WIDTH/2, WINDOW_HEIGHT/2) @ Tmat(0, 0) @ Rmat(degree) @ Tmat(0, 0)
    H_2 = Tmat(WINDOW_WIDTH/2, WINDOW_HEIGHT/2) @ Tmat(0, 0)  @ Rmat(degree) @ Tmat(0, 10) @rpimat(1)
    H_3 = Tmat(WINDOW_WIDTH/2, WINDOW_HEIGHT/2) @ Tmat(0, 0)  @ Rmat(degree) @ Tmat(0, 10) @rpimat(2)
    H_4 = Tmat(WINDOW_WIDTH/2, WINDOW_HEIGHT/2) @ Tmat(0, 0)  @ Rmat(degree) @ Tmat(0, 10) @rpimat(3)

    pp = H @ poly
    pp_2 = H_2 @ poly
    pp_3 = H_3 @ poly
    pp_4 = H_4 @ poly


    corp = H @ cor
    # print(pp.shape, pp, pp.T )

    wing_1 = pp[0:2, :].T # N x 2 matrix
    wing_2 = pp_2[0:2, :].T
    wing_3 = pp_3[0:2, :].T
    wing_4 = pp_4[0:2, :].T

    pygame.draw.rect(screen, GREY, [285,335,30,365])
    pygame.draw.polygon(screen, GREY, wing_1)
    pygame.draw.polygon(screen, GREY, wing_2)
    pygame.draw.polygon(screen, GREY, wing_3)
    pygame.draw.polygon(screen, GREY, wing_4)


    pygame.draw.circle(screen, GREY, [WINDOW_WIDTH/2, WINDOW_HEIGHT/2], 30)
    


    # 안티얼리어스를 적용하고 검은색 문자열 렌더링
    text = font.render("Windmill", True, BLACK)
    screen.blit(text, [250, 0])

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

# 게임 종료
pygame.quit()