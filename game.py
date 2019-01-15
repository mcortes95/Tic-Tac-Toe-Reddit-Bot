class gameboard:
    board=[[' ' for i in range(3)] for i in range(3)]
    def printboard(self):
        for y,yvalue in enumerate(self.board):
            for x,xvalue in enumerate(self.board):
                if x<2:
                    print(""+self.board[x][y]+" | ",end="")
                else:
                    print(""+self.board[x][y])
            if y<2:
                print("--------")
    def clearBoard(self):
        for x in range(0,3):
            for y in range(0,3):
                self.board[x][y]=' '
        self.printboard()

    def getChar(self,pos):
        return self.board[int(pos[0])][int(pos[1])]

    def setCharAI(self,player,pos):
        self.board[int(pos[0])][int(pos[1])]=player

    def setChar(self,player,pos):
        try:
            if self.board[int(pos[0])][int(pos[1])]!=" ":
                self.printboard()
                print("Space taken!")
                return False
            else:
                self.board[int(pos[0])][int(pos[1])]=player
                return True
        except:
            print("!!Reminder!!\n!!Move position for both integers must be between 0 and 2!!\nExample: for bottom right slot, input '22'")

class tttRules:
    count=0
    tttboard=gameboard()
    win1=0
    win2=0
    draw=0
    continueGame=True

    def displayScore(self):
        print("Player 1: "+str(self.win1)+"\nPlayer 2: "+str(self.win2)+"\nDraws: "+str(self.draw))

    def setCount(self):
        self.count=0

    def play(self):
        self.tttboard.clearBoard()
        self.setCount()
        self.continueGame=True
        while self.continueGame:
            self.checkTurn()

    def checkTurn(self):
        if self.count%2 is 0:
            self.turn1()
        else:
            self.turn2()
        self.tttboard.printboard()

    def turn1(self):
        full=0
        spaceTaken=False
        while spaceTaken is False:
            space=input("Player 1, make move:")
            spaceTaken=self.tttboard.setChar('x',space)
        self.count+=1
        for x in range(0,3):
            for y in range(0,3):
                if self.tttboard.board[x][y]!=" ":
                    full+=1
        if checkforwin(self.tttboard,'x'):
            self.continueGame=False
            self.win1+=1
        elif full is 9:
            self.continueGame=False
            self.draw+=1

    def turn2(self):
        print("Minimax")
        move=self.returnbestmove(self.tttboard)
        self.tttboard.setChar('o',move)
        self.count+=1
        full=0
        for x in range(0,3):
            for y in range(0,3):
                if self.tttboard.board[x][y]!=" ":
                    full+=1
        if checkforwin(self.tttboard,'o'):
            self.continueGame=False
            self.win2+=1
        elif full is 9:
            self.continueGame=False
            self.draw+=1

    def returnbestmove(self,tempBoard):
        bestScore=-1000
        for x in possibleMoves(tempBoard):
            tempBoard.setCharAI('o',x)
            moveScore=self.minimax(tempBoard,'x')
            tempBoard.setCharAI(" ",x)
            if moveScore>bestScore:
                bestMove=x 
                bestScore=moveScore
        return bestMove

    def minimax(self,tempBoard,currentPlayer):
        availablemoves=possibleMoves(tempBoard)
        if checkforwin(tempBoard,'o'):
            return 10
        elif checkforwin(tempBoard,'x'):
            return -10
        elif  len(availablemoves) is 0:
            return 0

        if currentPlayer is 'o':
            bestscore=-1000
            for x in availablemoves:
                tempBoard.setCharAI('o',x)
                score=self.minimax(tempBoard,'x')
                if score>bestscore:
                    bestscore=score
                tempBoard.setCharAI(' ',x)
            return bestscore
        
        else:
            bestscore=1000
            for x in availablemoves:
                tempBoard.setCharAI('x',x)
                score=self.minimax(tempBoard,'o')
                if score<bestscore:
                    bestscore=score
                tempBoard.setCharAI(' ',x) 
            return bestscore
def possibleMoves(tboard):
    posMoves=[]
    for x in range(0,3):
        for y in range(0,3):
            if tboard.board[x][y]==' ':
                posMoves.append(str(x)+str(y))
    return posMoves

def checkforwin(tboard,player):
    counter=0
    if tboard.board[0][0]==player:
        if tboard.board[0][1]==player and tboard.board[0][2]==player:
            return True
        if tboard.board[1][1]==player and tboard.board[2][2]==player:
            return True
        if tboard.board[1][0]==player and tboard.board[2][0]==player:
            return True
    if tboard.board[2][2]==player:
        if tboard.board[2][1]==player and tboard.board[2][0]==player:
            return True
        if tboard.board[1][2]==player and tboard.board[0][2]==player:
            return True
    if tboard.board[0][1]==player and tboard.board[1][1]==player and tboard.board[2][1]==player:
        return True
    if tboard.board[1][0]==player and tboard.board[1][1]==player and tboard.board[1][2]==player:
        return True
    if tboard.board[2][0]==player and tboard.board[1][1]==player and tboard.board[0][2]==player:
        return True
    return False

def start():
    print("This is Tic Tac Toe ")
    newgame=tttRules()
    keepPlaying=True
    while keepPlaying==True:
        newgame.play()
        newgame.displayScore()
        if input("Play again?: ")=='y':
            keepPlaying=True
        else:
            keepPlaying==False
    print("Thanks for playing:\n")
    newgame.displayScore()


















