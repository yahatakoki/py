#from curses.ascii import SP
from math import e
from pyxel import *
from hashlib import algorithms_available
from os import times_result
from re import S
from turtle import pu
import time
SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200
PUPU_SPEED = 5
# シーン番号の定義
SNO_TITLE    = 0
SNO_STAGESET = 10
SNO_PLAY     = 11
SNO_STOP     = 12
SNO_FINISH  = 13
SNO_GAMEOVER = 14
STAGE_SETUP = False
scene = SNO_TITLE   # ゲームの進行を管理する変数
tmr = 0             # シーン内でカウントするタイマー変数
pupu_entities = []

def update_entities(entities):
    for entity in entities:
        entity.update()

def draw_entities(entities):
    for entity in entities:
        entity.draw()

class PUPU:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.xdir = 1
        self.ydir = 1
        pupu_entities.append(self)

    def update(self):
        #要素の移動と方向転換
        if (self.x >= SCREEN_WIDTH -10):
            self.xdir = -1
        elif (self.x <= 10):
            self.xdir = 1
        
        if (self.y >= SCREEN_HEIGHT -10):
            self.ydir = -1
        elif (self.y <= 10):
            self.ydir = 1
        
        self.x += self.xdir * PUPU_SPEED
        self.y += self.ydir * PUPU_SPEED
        time.sleep(0.01)

#ここ本当は引数としてピクセルエディタ内の描画位置を受け取るべきなんだけど、まあいいや
    def draw(self):
        blt(self.x, self.y, 0,0,0,10,10,colkey=7)


class App:
    def __init__(self):
        init(SCREEN_WIDTH, SCREEN_HEIGHT,title="PUPUNPUPU")
        load("my_resource.pyxres")
        self.scene = SNO_TITLE
        self.player_x =SCREEN_WIDTH // 2
        self.player_y =SCREEN_HEIGHT // 2
        self.score = 0
        self.lefteye_x = 0
        self.lefteye_y = 0
        self.righteye_x = 0
        self.righteye_y = 0
        self.x = 0
        self.y = 0
        self.life = 3
        self.stagesetup_done =False

        run(self.update, self.draw)

    def update(self):
        global tmr
        tmr += 1
        if self.scene == SNO_TITLE:
            self.update_title_scene()

        elif self.scene == SNO_STAGESET:
            self.update_stageset_scene()

        elif self.scene == SNO_PLAY:
            self.update_play_scene()

        elif self.scene == SNO_STOP:
            self.update_stop_scene()

        elif self.scene == SNO_FINISH:
            self.update_finish_scene()

        elif self.scene == SNO_GAMEOVER:
            self.update_gameover_scene()

    def update_title_scene(self):
        if btnp(KEY_SPACE):
            self.scene = SNO_STAGESET
#            time.sleep(2)  

    def update_stageset_scene(self):
        global tmr
        if tmr >30:
            print("STAGE SET DONE")
            self.scene = SNO_PLAY
            tmr = 0
        
    def update_play_scene(self):
        if self.life == 0:
            self.scene = SNO_GAMEOVER
            tmr = 0
    
        if btnp(KEY_SPACE):
            self.scene = SNO_STOP
            tmr = 0

        if not pupu_entities:
            print("PUPU生成")   
            for i in range(3):
                i = PUPU(rndi(0,  SCREEN_WIDTH), rndi(0, SCREEN_HEIGHT))
        
        update_entities(pupu_entities)

    def update_stop_scene(self):
        for i in range(3):
            hoge = pupu_entities[i] 
            print(hoge.x,hoge.y)

        if self.score >= 100:
            time.sleep(3)
            self.scene = SNO_FINISH
            tmr = 0

        if self.score < 100 and self.score >= 1:
            time.sleep(3)
            self.scene = SNO_STAGESET
            tmr = 0

    def update_finish_scene(self):
        if btnp(KEY_SPACE):
            self.scene = SNO_TITLE
            tmr = 0

    def update_gameover_scene(self):
        if btnp(KEY_SPACE):
            self.scene = SNO_TITLE
            tmr = 0     


    def draw(self):
        cls(6)
        if self.scene == SNO_TITLE:
            self.draw_title_scene()

        elif self.scene == SNO_STAGESET:
            self.draw_stageset_scene()

        elif self.scene == SNO_PLAY:
            self.draw_play_scene()

        elif self.scene == SNO_STOP:
            self.draw_stop_scene()

        elif self.scene == SNO_FINISH:
            self.draw_finish_scene()
            
        elif self.scene == SNO_GAMEOVER:
            self.draw_gameover_scene() 


    def draw_title_scene(self):
        # タイトル用の画像表示
        text(60, 90, "PUPUNPUPU", 8)
        text(40, 110, "PRESS SPACE KEY", 4)

    def draw_stageset_scene(self):
        #ここにふれーむれーと調整コードを入れる
        cls(6)
        blt(10,160,0,0,0,16,32,colkey=7)
        circ(100, 60,50, 2)            
        text(80, 90, "STAGE SET...", 8)
        
    def draw_play_scene(self):
        text(10,10,"SCORE:",8)
        text(0,10,"X",8)
        if self.score < 100 and self.score >= 1:
            #スコア表示
            play(0,1)
            text(10,10,"SCORE:"+str(self.score),8)
            time.sleep(3)
            self.score = 0
        if pupu_entities:
            draw_entities(pupu_entities)

    def draw_stop_scene(self):
        draw_entities(pupu_entities)


    def draw_finish_scene(self):
            text(80, 90, "CLEAR!", 8)
            text(40, 110, "PRESS SPACE KEY", 8)

    def draw_gameover_scene(self):
            text(70, 90, "GAME OVER", 8)
        

App()

