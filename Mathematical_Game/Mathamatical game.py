import pygame, sys, random, pickle, os

MAXQUESTIONS = 20

def quitprogram():
    """If the user wants to quite the program"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
def setbackgroundimage(screen):
    """sets an image to the background"""
    background = pygame.image.load("background.jpg")
    background = pygame.transform.scale(background,(875,425))
    backgroundrect = background.get_rect()
    backgroundrect.left = 45
    backgroundrect.top = 25
    screen.blit(background,backgroundrect)

def drawline(screen):
    """Draw lines on the outside as a frame, for asthetics"""
    ##draws lines horizontaly
    startpos = startpos_w,startpos_h = 38,20
    endpos = endpos_w,endpos_h = 30,7
    for m in range(1,700,50):
        pygame.draw.line(screen,(red),(startpos_w, startpos_h+m),(endpos_w,endpos_h+m),4)
        for i in range(1,950,50):
            pygame.draw.line(screen,(red),(startpos_w + i, startpos_h),(endpos_w + i,endpos_h),4)
    ##draws lines vertically
    startpos = startpos_w,startpos_h = 929,458
    endpos = endpos_w,endpos_h = 937,472
    for m in range(1,700,50):
        pygame.draw.line(screen,(red),(startpos_w, startpos_h-m),(endpos_w,endpos_h-m),4)
        for i in range(1,950,50):
            pygame.draw.line(screen,(red),(startpos_w - i, startpos_h),(endpos_w - i,endpos_h),4)

def setbackground(screensize): 
    """Set the background for the game""" 
    screen = pygame.display.set_mode(screensize)
    screen.fill(darkblue)
    ##draw line frame
    drawline(screen)    
    ##Set background Image
    setbackgroundimage(screen)   
    return screen

def createdifficultylabels():
    ##draw title label
    lblDifficulty = fntmonotitle.render("Please choose your difficulty!",1,red)
    screen.blit(lblDifficulty, (180, 120))
    ##draw easy label       
    lblEasy = fntmono.render("Easy?",1,black)
    lblEasyrect = lblEasy.get_rect()
    lblEasyrect.left = 380
    lblEasyrect.top = 180
    screen.blit(lblEasy, lblEasyrect)
    ## draw moderate label     
    lblmoderate = fntmono.render("Moderate?",1,black)
    lblmoderaterect = lblmoderate.get_rect()
    lblmoderaterect.left = 380
    lblmoderaterect.top = 250
    screen.blit(lblmoderate, lblmoderaterect)          
    ## draw difficult label
    lblDifficult = fntmono.render("Difficult?",1,black)
    lblDifficultrect = lblDifficult.get_rect()
    lblDifficultrect.left = 380
    lblDifficultrect.top = 320
    screen.blit(lblDifficult, lblDifficultrect)
 
    pygame.display.flip()
    return lblEasyrect,lblmoderaterect,lblDifficultrect

def displayquestions(questionlst,quesnum):
    """Asks the questions"""
    ##draws question number
    questions = ("Question Number "+ str(quesnum +1))
    lblQuestion= fntmonotitle.render(questions,0,red)
    screen.blit(lblQuestion, (250, 120))
    ##draws question      
    lblquestion = fntmono.render(questionlst[quesnum][0],1,black)
    lblquestionrect = lblquestion.get_rect()
    lblquestionrect.left = 70
    lblquestionrect.top = 180
    screen.blit(lblquestion, lblquestionrect)
    ##draws answer a  
    lblanswerA = fntmono.render(questionlst[quesnum][1],1,black)
    lblanswerArect = lblanswerA.get_rect()
    lblanswerArect.left = 90
    lblanswerArect.top = 250
    screen.blit(lblanswerA, lblanswerArect)
    ##draws answer b 
    lblanswerB = fntmono.render(questionlst[quesnum][2],1,black)
    lblanswerBrect = lblanswerB.get_rect()
    lblanswerBrect.left = 90
    lblanswerBrect.top = 320
    screen.blit(lblanswerB, lblanswerBrect)
    ##draws answer c  
    lblanswerC = fntmono.render(questionlst[quesnum][3],1,black)
    lblanswerCrect = lblanswerC.get_rect()
    lblanswerCrect.left = 90
    lblanswerCrect.top = 390
    screen.blit(lblanswerC, lblanswerCrect)
    return lblanswerArect, lblanswerBrect, lblanswerCrect

def displayscore(points,screen):
    "displays the score of the current person"
    ##clears screen
    screen.fill((0,0,0))
    screen = setbackground(screensize)
    ##displays score title label
    Highscore = fntmonotitle.render("Your Score is displayed below ",0,red)
    screen.blit(Highscore, (180,160))
    ##displays player's score
    thescore = ("Your score is " + str(points)+" out of 10")
    score = fntmono.render(thescore,1,black)
    screen.blit(score, (180,280))

def shufflingthelist(questionlst,answerlist):
    """The question and the answer list gets shuffled"""
    answertemplist = []
    templist = []
    ##places questions and answers into one list
    for i in range (0,MAXQUESTIONS):
        answertemplist += [[answerlist[i]]]        
    for i in range (0,MAXQUESTIONS):
        templist += [questionlst[i]+answertemplist[i]]
    ##shuffles the list
    random.shuffle(templist)
    ##seperates the questions and the answers
    answerlist = []
    questionlst = [] 
    for i in range(0,MAXQUESTIONS):
      answerlist += [templist[i][4]]
      questionlst += [templist[i][:4]] 
    return questionlst,answerlist
    
def askquestions(screen,Questions,Answers):
    """This is where the questions gets asked"""
    ##places the questions and answers from file to lists
    qtemplst = []
    questionlst =[]
    for i in range (0,MAXQUESTIONS):
        question = Questions.readline()
        question = question[:-1]
        answera = Questions.readline()
        answera = answera[:-1]
        answerb = Questions.readline()
        answerb = answerb[:-1]
        answerc = Questions.readline()
        answerc = answerc[:-1]
        qtemplst = [question,answera,answerb,answerc]
        questionlst += [qtemplst]
    answerlist = []
    for i in range (0,MAXQUESTIONS):
        answers = Answers.read()
        answerlist += answers
    ##shuffling the list
    questionlst,answerlist = shufflingthelist(questionlst,answerlist)    
    ##creating the running man
    runningman = pygame.image.load("runningman.jpg")
    runningman = pygame.transform.scale(runningman,(50,50))
    move = 50
    ##questions being asked
    points = 0
    for quesnum in range(0,10):
        quitprogram()
        screen.fill((0,0,0))
        screen = setbackground(screensize)
        lblanswerArect, lblanswerBrect, lblanswerCrect = displayquestions(questionlst,quesnum)
        pygame.display.flip()       
        ##gets mouse input from the user for answers
        answer = ("x")
        answered = False  
        while not answered:
            quitprogram()            
            mouse_pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]  and lblanswerArect.collidepoint(mouse_pos):
                Rectangle = pygame.draw.rect(screen,red,(80,240,800,50),4) 
                answer = ("A")
                answered = True               
            elif pygame.mouse.get_pressed()[0]  and lblanswerBrect.collidepoint(mouse_pos):
                Rectangle = pygame.draw.rect(screen,red,(80,310,800,50),4)
                answer = ("B")
                answered = True            
            elif pygame.mouse.get_pressed()[0]  and lblanswerCrect.collidepoint(mouse_pos):
                Rectangle = pygame.draw.rect(screen,red,(80,380,800,50),4)
                answer = ("C")
                answered = True
            ##points gets added up
            if answered == True:
                if answer == answerlist[quesnum]:
                    points +=  1
                    lblcorrect = fntmonotitle.render("CORRECT!!!",0,blue)
                else:
                    lblcorrect = fntmonotitle.render("WRONG!!!",0,black)
                screen.blit(lblcorrect, (700,125))     
                screen.blit(runningman,(move,50))
                move += 91                   
        pygame.display.flip()
        pygame.time.delay(500)       
    displayscore(points,screen)
    pygame.display.update()
    chooseDifficulty = False
    return (chooseDifficulty,points)

def DisplayHighScore(screen,Highscorelist):
    """Display top 5 highscores"""
    ## create button
    scores = fntmonotitle.render("Highscores?",1,black)
    scoresrect = scores.get_rect()
    scoresrect.left = 600
    scoresrect.top = 380
    screen.blit(scores, scoresrect)
    pygame.display.flip()
    ## Display highscore
    colour = black
    display = False
    while display == False:
        quitprogram()
        mouse_pos = pygame.mouse.get_pos()
        ##refreshes the screen if the button has been clicked
        if pygame.mouse.get_pressed()[0]  and scoresrect.collidepoint(mouse_pos):
          display = True
          screen.fill((0,0,0))
          screen = setbackground(screensize)
          move = 150
          fntscore = pygame.font.SysFont("monospace", 26, bold = True)      
          HighscoreTitle = fntmonotitle.render("High Scores",0,black)
          screen.blit(HighscoreTitle, (350,50))
          ##Displays all of the highscores
          for i in range(0,5):
              if i < len(Highscorelist):
                  playername = Highscorelist[i][1]
                  score = str(Highscorelist[i][0])
                  playmode = Highscorelist[i][2]
                  if playername == Playername:
                      colour = red
                  else :
                      colour = black
                  highscore = fntscore.render(playername+" got "+score+" points playing on "+playmode+" mode",0,colour)
                  screen.blit(highscore, (125,move))
                  move += 50

def StoreHighscores(screen,Playername,points):
    ##Initialises highscore lists
    Highscorelist = []
    Highscoretemplist = []
    ##reads / creates a dat file
    if os.path.isfile("Highscores.dat") == True:
        Highscores = open("Highscores.dat","rb")
        Highscoretemplist = pickle.load(Highscores)
        Highscores.close()
        ##stores only the top 5 people
        for i in range(0,5):
            if i < len(Highscoretemplist):
                Highscorelist += [Highscoretemplist[i]]    
    ##Place scores into a dat file
    Highscorelist += [[points,Playername,mode]]
    Highscorelist.sort(reverse = True)
    Highscores = open("Highscores.dat","wb")
    pickle.dump(Highscorelist,Highscores)
    Highscores.close()
    DisplayHighScore(screen,Highscorelist)
          
    
        
            
        

#################              Main Program            ######################
##Ask user to input their name
print("********* WELCOME TO THE MATHEMATICAL GAME **********")
print("*****************************************************")
print("\nBefore we start I'm going to need to take your name")
Playername = ("")
while len(Playername) > 6 or not Playername:
    Playername = str(input("What is your name <must be upto 6 characters > : "))
    
pygame.init()
##initialize variables
red = (255,0,0)
darkred = (139,0,0)
orangered = (255,69,0)
green = (0,255,0)
aqua = (0,255,255)
blue = (0,0,255)
darkblue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
yellow = (255,255,0)
brown = (165,42,42)
maroon = (128,0,0)
screensize = scrnWidth, scrnHeight = 950,500
chooseDifficulty = True
fntmonotitle = pygame.font.SysFont("monospace", 35, bold = True)
fntmono = pygame.font.SysFont("monospace", 30, bold = True)
mode = None
## start of the main program
screen = setbackground(screensize)
##load Welcome images
Welcomeimg = pygame.image.load("Welcome.jpg")
Welcomeimg = pygame.transform.scale(Welcomeimg,(700,200))
Welcomerect = Welcomeimg.get_rect()
Welcomerect.left = 130
Welcomerect.top = 95
##load press space bar image
PressSpace = pygame.image.load("PressSpace.jpg")
PressSpacerect = PressSpace.get_rect()
PressSpacerect.left = 90
PressSpacerect.top = 300

pygame.mixer.music.load("Kalimba.mp3")
pygame.mixer.music.play(0,0)

while True:
    quitprogram()
    screen.blit(Welcomeimg,Welcomerect)
    screen.blit(PressSpace,PressSpacerect)  
    if pygame.key.get_pressed()[pygame.K_SPACE] == True:
        screen.fill((0,0,0))
        screen = setbackground(screensize)
        PressSpace = pygame.transform.scale(PressSpace,(0,0))
        Welcomeimg = pygame.transform.scale(Welcomeimg,(0,0))
        while chooseDifficulty == True:
            quitprogram()  
            lblEasyrect,lblModeraterect,lblDifficultrect =  createdifficultylabels()        
            mouse_pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]  and lblEasyrect.collidepoint(mouse_pos):
                mode = "Easy"
                pygame.mouse.set_pos(870,130)                
                screen.fill((0,0,0))
                screen = setbackground(screensize)
                ##prepares to ask the questions
                Questions = open("EasyQuestions.txt","r")
                Answers = open("EasyAnswers.txt","r")
                chooseDifficulty,points = askquestions(screen,Questions,Answers)
                Questions.close()
                Answers.close()                                
            elif pygame.mouse.get_pressed()[0]  and lblModeraterect.collidepoint(mouse_pos):
                mode = "Moderate"
                pygame.mouse.set_pos(870,130)
                screen.fill((0,0,0))
                screen = setbackground(screensize)
                ##prepares to ask the questions
                Questions = open("ModerateQuestions.txt","r")
                Answers = open("ModerateAnswers.txt","r")
                chooseDifficulty,points = askquestions(screen,Questions,Answers)
                Questions.close()
                Answers.close()               
            elif pygame.mouse.get_pressed()[0]  and lblDifficultrect.collidepoint(mouse_pos):
                mode = "Difficult"
                pygame.mouse.set_pos(870,130)
                screen.fill((0,0,0))
                screen = setbackground(screensize)
                ##prepares to ask the questions
                Questions = open("DifficultQuestions.txt","r")
                Answers = open("DifficultAnswers.txt","r")
                chooseDifficulty,points = askquestions(screen,Questions,Answers)
                Questions.close()
                Answers.close()
        pygame.display.update()
        StoreHighscores(screen,Playername,points)
    pygame.display.flip()
