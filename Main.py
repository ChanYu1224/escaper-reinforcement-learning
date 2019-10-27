#encode:utf-8

#ライブラリ読み込み
import pygame
from pygame.locals import * 
import sys



#ソース読み込み
import GridMap
import Agent



#色の定義
WHITE = (255,255,255)
BLACK = (0  ,0  ,0  )
RED   = (255,0  ,0  )
GREEN = (0  ,255,0  )
BLUE  = (0  ,0  ,255)



#パラメータ変数
SCREEN_SIZE = (1200, 600)
CAPTION = "Oni Gkko"
CELLS_SIZE = (1100, 500)



#マップ変数
width = 0
hight = 0



#グリッドマップ読み込み
def ReadMap( filePath ):
  """
  ReadMap( filePath ):
  .txtファイルよりグリッドマップを読み込む．
  入力ファイルはwidthとhightが示されたヘッダと'#'を壁，'.'を通路とした文字列のマップで構成される．
  （例）
  5 5
  #####
  #.#.#
  #.#.#
  #...#
  #####

    filePath: グリッドマップを記したテキストファイル(.txt)のパス

    return: 　壁の位置をTrue，そうでない位置をFalseとした二次元リスト
  """
  with open(filePath) as f:
    
    #ヘッダ読み込み
    global width
    global hight
    width, hight = map(int, f.readline().split())
    print("Width = "+ str(width) +", Hight = "+ str(hight) +"  Environment Readed!")

    #マップ読み込み
    isWall = [[False for _ in range(hight)] for _ in range(width)]

    for i in range(hight):
      line = list( f.readline() )
      for j in range(width):
        if line[j] == '#':
          isWall[j][i] = True
  
  return isWall



#グリッドマップ描写
def drawGridMap( screen, grid: GridMap ):
  """
  drawGridMap( screen, grid: GridMap ):
  GUIへグリッド線及び壁を書き込む

    screen: pygameのGUI変数
    grid: 　グリッドマップ用のクラス変数
  """
  for i in range(grid.width):
    pygame.draw.line(screen, BLACK, (grid.pos_x[i], grid.pos_y[0]), (grid.pos_x[i], grid.pos_y[-2]), 1)
  for i in range(grid.hight):
    pygame.draw.line(screen, BLACK, (grid.pos_x[0], grid.pos_y[i]), (grid.pos_x[-2], grid.pos_y[i]), 1)
  
  for i in range(grid.width):
    for j in range(grid.hight):
      if grid.isWall[i][j]:
        wall_rect = ((grid.pos_x[i], grid.pos_y[j]), (grid.cell_size, grid.cell_size))
        screen.fill(BLACK, wall_rect) 



def main():
  #マップ読み込み
  print("FilePath (Environment_*.txt) :", end="")
  tmpMap = ReadMap( input() )
  Grid = GridMap.GridMap(width, hight, tmpMap, SCREEN_SIZE, CELLS_SIZE)

  #pygame初期化
  pygame.init()

  #ウィンドウサイズ設定
  screen = pygame.display.set_mode(SCREEN_SIZE)

  #キャプション設定
  pygame.display.set_caption(CAPTION)

  #グリッドマップ描写
  screen.fill(WHITE)
  drawGridMap(screen, Grid)

  #GUI更新
  while True:
    pygame.display.update()

    #イベント処理
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()



if __name__ == "__main__":
  main()