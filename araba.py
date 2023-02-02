#yazılımfuryası technopat stackoverflow yt github pygame google(pixelartmaker pngindir) bilsem bilişim
#mthnzbkgitbookio pixelartmaker probot.io
from email import contentmanager
from msilib.schema import Font
from pickle import TRUE
from numpy import true_divide
import pygame
import random
import time
pygame.init()

#ekran
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)
screen=pygame.display.set_mode((1500,950)) #ekran boyutu
pygame.display.set_caption("AutoBan") #uygulama adı (sol üst)
pygame.display.iconify()
#ekran

#gerekli global değişkenler
score=0
level=0
redcar=pygame.image.load("redcar.png")
redcar=pygame.transform.scale(redcar,(220,280))
yol=pygame.image.load('yol.png')
yol=pygame.transform.scale(yol,(1500,950))
menubg=pygame.image.load("bg.jpg")
menubg=pygame.transform.scale(menubg,(1500,950))
gobg=pygame.image.load("gameover.jpg")
gobg=pygame.transform.scale(gobg,(1500,950))
#gerekli global değişkenler

#FONKSİYONLAR 

#oyun anamenüsü
def anamenu():
    #menü açıksa
    pygame.mixer.music.load("riders.mp3")
    pygame.mixer.music.play(loops=-1, start=5.0, fade_ms=0)
    menu=True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
        screen.blit(menubg,(0,0)) #gösterilecek ekran

        cursor=pygame.mouse.get_pos() #mouse konumunu algılar
        click=pygame.mouse.get_pressed() #mouse tıklamasını algılar

        #menü ekranında gösterilecekler
        font=pygame.font.Font("yazıtipi.ttf",150)
        title=font.render("AUTO",True,"yellow")
        title2=font.render("BAN",True,"RED")
        screen.blit(title,(50,50))
        screen.blit(title2,(400,50))
        font1=pygame.font.SysFont(None,30)
        by=font1.render("CREATED BY:",True,"black")
        screen.blit(by,(1200,700))
        by1=font1.render("AHMET RÜCHAN DORA",True,"black")
        screen.blit(by1,(1200,750))
        by2=font1.render("MAHMUT EMİN ULUSOY",True,"black")
        screen.blit(by2,(1200,800))
        by3=font1.render("DOĞUKAN ÇELİK",True,"black")
        screen.blit(by3,(1200,850))

        #buton oluşturma
        pygame.draw.rect(screen,"GREY",(625,500,250,80))
        pygame.draw.rect(screen,"GREY",(625,600,250,80))

        #butonlara tıklayınca gerçekleşecek eylemler
        if cursor[1]> 500 and cursor[1] <580 and cursor[0]>625 and cursor[0]<875:
            pygame.draw.rect(screen,"GREEN",(625,500,250,80))
            if click==(1,0,0):
                pygame.mixer.music.load("tokyo.mp3","mp3")
                pygame.mixer.music.play(-1,0.0,0)
                game_loop()
        if cursor[1]> 600 and cursor[1] <680 and cursor[0]>625 and cursor[0]<875 and menu:
            pygame.draw.rect(screen,"RED",(625,600,250,80))
            if click==(1,0,0):
                pygame.quit
                quit()

        #menü ekranı içeriği
        playfont=pygame.font.Font("yazıtipi.ttf",30)
        playtext,msg=text("START",playfont)
        msg.center=((625+(250/2)),(500+(80/2)))
        screen.blit(playtext,msg)
        playtext,msg=text("QUIT",playfont)
        msg.center=((625+(250/2)),(600+(80/2)))
        screen.blit(playtext,msg)
        pygame.display.update()
#oyun anamenüsü

#font ve text ayarlayan fonksiyon
def text(text,font):
    content=font.render(text,False,(0,0,0))
    return content,content.get_rect()
#font ve text ayarlayan fonksiyon

#gameover ekranında gösterilecek skor için özel font text fonksiyonu
def text2(text,font):
    content=font.render(text,True,("RED"))
    return content,content.get_rect()
#gameover ekranında gösterilecek skor için özel font text fonksiyonu

#ana arabanın konumunu gösterir
def carloc(x,y):
    screen.blit(redcar, (x,y))
#ana arabanın konumunu gösterir

#oyun içinde yolun akışını sağlar
def background():
    screen.blit(yol,(0,0))
    screen.blit(yol,(0,350))
    screen.blit(yol,(0,700))
    screen.blit(yol,(0,1000))
    screen.blit(yol,(1500,0))
    screen.blit(yol,(1500,350))
    screen.blit(yol,(1500,700))
    screen.blit(yol,(1500,1000))
#oyun içinde yolun akışını sağlar

#oyun sonu ekranı
def gameover():
    #oyun bittiğinde
    isgameover=True
    while isgameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
        screen.blit(gobg,(0,0)) #gösterilecek ekran

        cursor=pygame.mouse.get_pos() #mouse konumunu algılar
        click=pygame.mouse.get_pressed() #mouse tıklamasını algılar

        #menü ekranında gösterilecekler

        #buton oluşturma
        pygame.draw.rect(screen,"GREY",(20,400,250,60))
        pygame.draw.rect(screen,"GREY",(20,530,250,60))
        pygame.draw.rect(screen,"GREY",(20,660,250,60))
        pygame.draw.rect(screen,"GREY",(610,460,290,0))

        #butonlara tıklayınca gerçekleşecek eylemler
        if 400<cursor[1]<460 and 20<cursor[0]<270:
            pygame.draw.rect(screen,"GREEN",(20,400,250,60))
            if click==(1,0,0):
                pygame.mixer.music.load("tokyo.mp3","mp3")
                pygame.mixer.music.play(0,0.0,0)
                game_loop()
        if 530 < cursor[1] <590 and cursor[0]>20 and cursor[0]<270:
            pygame.draw.rect(screen,"YELLOW",(20,530,250,60))
            if click==(1,0,0):
                anamenu()
        if 660 <cursor[1] <760 and cursor[0]>20 and cursor[0]<270:
            pygame.draw.rect(screen,"RED",(20,660,250,60))
            if click==(1,0,0):
                pygame.quit
                quit()

        #oyun sonu ekranı içeriği
        fontscore=pygame.font.Font("yazıtipi.ttf",70)
        skorget=fontscore.render("SCORE",0,("BLACK"))
        screen.blit(skorget,(670,360))

        sfont=pygame.font.Font("yazıtipi.ttf",70)
        gofont=pygame.font.Font("yazıtipi.ttf",30)
        gotext,msg=text("RETRY",gofont)
        msg.center=((20+(250/2)),(400+(60/2)))
        screen.blit(gotext,msg)
        gotext,msg=text("MAIN MENU",gofont)
        msg.center=((20+(250/2)),(530+(60/2)))
        screen.blit(gotext,msg)
        gotext,msg=text("QUIT",gofont)
        msg.center=((20+(250/2)),(660+(60/2)))
        screen.blit(gotext,msg)
        skorgett,msg=text2(str(score),sfont)
        msg.center=((620+(290/2)),(460+(60/2)))
        screen.blit(skorgett,msg)
        pygame.display.update()
clock=pygame.time.Clock()
#oyun sonu ekranı

#pause ekranı
def paused():
    #oyun durdurulduğunda
    ispause=True
    while ispause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        pygame.mixer.music.pause()

        #pause ekranında gösterilecekler
        pmenu=pygame.font.Font("yazıtipi.ttf",91)
        pcontent=pmenu.render("PAUSED",0,("white"))
        screen.blit(pcontent,(600,200))

        #buton oluşturma 
        pygame.draw.rect(screen,"GREY",(600,400,300,80))

        cursor=pygame.mouse.get_pos() #mouse konumunu algılar
        click=pygame.mouse.get_pressed() #mouse tıklamasını algılar

        #butona tıklayınca gerçekleşecek eylemler
        if cursor[0]>600 and cursor[0]<950 and cursor[1]>400 and cursor[1]<480:
            pygame.draw.rect(screen,"GREEN",(600,400,300,80))
            if click == (1,0,0):
                pygame.mixer.music.unpause()
                ispause=False

        rmenu=pygame.font.Font("yazıtipi.ttf",80)
        rcontent,rmsg=text("RESUME",rmenu)
        rmsg.center=((600+(300/2)),(400+(80/2)))
        screen.blit(rcontent,rmsg)
        pygame.display.update()
        clock.tick(30)
#pause ekranı 

#diğer arabaları spawnlayan fonskiyon
def engelloc(engelx,engely,engel):
        if engel == 0:
            bluecar=pygame.image.load("bluecar.png")
            arabalar=pygame.transform.scale(bluecar,(120,220))
        elif engel == 1:
            greencar=pygame.image.load("greencar.png")
            arabalar=pygame.transform.scale(greencar,(120,220))
        elif engel == 2:
            redcar=pygame.image.load("redcarr.png")
            arabalar=pygame.transform.scale(redcar,(120,220))
        elif engel == 3:
            minibüs=pygame.image.load("engel.png")
            arabalar=pygame.transform.scale(minibüs,(360,400))
        elif engel == 4:
            kaza=pygame.image.load("kaza.png")
            arabalar=pygame.transform.scale(kaza,(720,400))

        screen.blit(arabalar,(engelx,engely))
#diğer arabaları spawnlayan fonskiyon

#skor gösterme fonksiyonu
def skor(score):
    font=pygame.font.Font("yazıtipi.ttf",50)
    score = font.render("Score  "+str(score),True,(0,0,0))
    screen.blit(score, (0,100))
#skor gösterme fonksiyonu

#oyun döngüsü
def game_loop():
    on=True
    x=560
    y=690
    hız=30  
    xloc=0
    global level
    engel = 0  
    engelx=random.randrange(320,1080)
    engely=-950
    engelw=70
    engelh=180
    pas=0
    global score
    score=0
    level=0
    y2=15

    #oyun başladığında
    while on:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                on=False


        
    #araba hareket ettirme
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if x<=1300-220:
                        x+=165
                    else: x+=0

                if event.key == pygame.K_LEFT:
                    if x>=320:
                        x-=165
                    else: x+=0
                xloc+=x

        #yolu hareketlendirme
        rel_y=y2%475
        screen.blit(yol,(0,rel_y-570))
        screen.blit(yol,(1500,rel_y-570))
        if rel_y<900:
            screen.blit(yol,(0,rel_y))
            screen.blit(yol,(1500,rel_y))
        y2+=hız



        #diğer arabaları çağır
        engely -= (hız/4)
        engelloc(engelx,engely,engel)
        engely+=hız

        #araba konumu
        carloc(x,y)
        #skoru gösterir
        skor(score)

        #diğer arabaların spawn durumu
        if engely > 950:
            engely=0-engelh
            engelx=random.randrange(320,1080)
            if level==0 or level == 1:
                engel=random.randrange(0,3)
            if level==2:
                engel=random.randrange(3,4)
            if level==3:
                engel=random.randrange(4,5)
            if level > 3:
                engel=random.randrange(0,5)
            if engel==0 or engel ==1 or engel ==2:
                score+=10
            if engel==3:
                score+=20
            if engel==4:
                score+=30
            pas +=1
            if int(pas)%3==0:
                level+=1
                hız+=20
                levelfont=pygame.font.Font("yazıtipi.ttf",70)
                levelyazı=levelfont.render("Level "+str(level),1,("white"))
                screen.blit(levelyazı,(630,400))
                pygame.display.update()
                time.sleep(2)

        #araba çarpışması 
        if engel == 0 or engel ==1 or engel == 2:
            if y<=engely+engelh:
                if x>=engelx and x<=engelx+engelw or x+120>=engelx and x+120<=engelx+engelw:
                    pygame.mixer.music.load("kaza.mp3","mp3")
                    pygame.mixer.music.play(0,0.0,0)
                    gameover()
        if engel == 3:
            if y<=engely+150:
                if x>=engelx and x<=engelx+300 or x+120>=engelx and x+120<=engelx+10:
                    pygame.mixer.music.load("kaza.mp3","mp3")
                    pygame.mixer.music.play(0,0.0,0)
                    gameover()
        if engel == 4:
            if y<=engely+150:
                if x>=engelx and x<=engelx+400 or x+120>=engelx and x+120<=engelx+10:
                    pygame.mixer.music.load("kaza.mp3","mp3")
                    pygame.mixer.music.play(0,0.0,0)
                    gameover()

        cursor=pygame.mouse.get_pos() #mouse konumunu algılar
        click=pygame.mouse.get_pressed() #mouse tıklamasını algılar

        #pause butonu oluşturma
        pygame.draw.rect(screen,"GREY",(675,0,150,50))
        pausetext=pygame.font.Font("yazıtipi.ttf",50)
        pcont,prect=text("PAUSE",pausetext)
        prect.center=((675+(150/2)),(0+(50/2)))
        screen.blit(pcont,prect)

        #pause butnonuna basılırsa
        if cursor[0]>675 and cursor[0]<800 and cursor[1]>0 and cursor[1]<50:
            pygame.draw.rect(screen,"BLUE",(675,0,150,50))
            pausetext=pygame.font.Font("yazıtipi.ttf",50)
            pcont,prect=text("PAUSE",pausetext)
            prect.center=((675+(150/2)),(0+(50/2)))
            screen.blit(pcont,prect)
            
            if click == (1,0,0):
                paused()
        
        pygame.display.update() #ekranda değişiklikleri uygular

#FONKSİYONLAR 

anamenu()
game_loop()
pygame.quit()
quit()