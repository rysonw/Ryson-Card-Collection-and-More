
import random, pygame, os, sys
from pygame.locals import *

class Card(object):
    def __init__(self, number, suit, value):
        self.suit = suit
        self.number = number
        self.value = value

    
    def show(self):
        print("{} of {}".format(self.number, self.suit))
    
    
    def card_value(self):
        return self.value

    
    
class emptyDeck(object):
    def __init__(self):
        self.cards = []

    
    def showDeck(self):
        for c in self.cards:
            c.show()


    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    
    def drawCard(self):
        return self.cards.pop()

    
    def addCard(self, player):
        self.cards.append(player.playCard())




class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    
    def showDeck(self):
        for c in self.cards(1):
            c.show()


    def emptyDeck(self):
        for i in self.cards:
            self.cards.pop()

    def build(self):
        for suit in ["♥", "♠️", "♣️", "♦️"]:
            for v in range(1, 14):
                if v == 11:
                    self.cards.append(Card("Jack", suit, v))
                elif v == 12:
                    self.cards.append(Card("Queen", suit, v))
                elif v == 13:
                    self.cards.append(Card("King", suit, v))
                elif v == 14:
                    self.cards.append(Card("Ace", suit, v))
                elif v == 1:
                    pass
                else:
                    self.cards.append(Card(v, suit, v))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    
    def drawCard(self):
        return self.cards.pop()


class Player(object): #Create different types of players for each game
    def __init__(self):
        self.hand = []

    def drawDeck(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def playCard(self):
        return self.hand.pop(0)

    def showHand(self):
        for c in self.hand:
            c.show()

    def discard(self, suit, number):
        for c in self.hand:
            if c.number == number and c.suit == suit:
                self.hand.pop()
            else:
                pass

    def cardValue(self):
        for c in self.hand:
            return c.value

    def cardSuit(self):
        for c in self.hand:
            return c.suit
    

    # def war_play_card(self):
    #     x = self.hand.pop()
    #     return x.value
        


Heart_2 = pygame.image.load(os.path.join("Hearts", "2 of Hearts.png"))
Heart_3 = pygame.image.load(os.path.join("Hearts", "3 of Hearts.png"))
Heart_4 = pygame.image.load(os.path.join("Hearts", "4 of Hearts.png"))
Heart_5 = pygame.image.load(os.path.join("Hearts", "5 of Hearts.png"))
Heart_6 = pygame.image.load(os.path.join("Hearts", "6 of Hearts.png"))
Heart_7 = pygame.image.load(os.path.join("Hearts", "7 of Hearts.png"))
Heart_8 = pygame.image.load(os.path.join("Hearts", "8 of Hearts.png"))
Heart_9 = pygame.image.load(os.path.join("Hearts", "9 of Hearts.png"))
Heart_10 = pygame.image.load(os.path.join("Hearts", "10 of Hearts.png"))
Heart_J = pygame.image.load(os.path.join("Hearts", "Jack of Hearts.png"))
Heart_Q = pygame.image.load(os.path.join("Hearts", "Queen of Hearts.png"))
Heart_K = pygame.image.load(os.path.join("Hearts", "King of Hearts.png"))
Heart_A = pygame.image.load(os.path.join("Hearts", "Ace of Hearts.png"))

Clubs_2 = pygame.image.load(os.path.join("Clubs", "2 of Clubs.png"))
Clubs_3 = pygame.image.load(os.path.join("Clubs", "3 of Clubs.png"))
Clubs_4 = pygame.image.load(os.path.join("Clubs", "4 of Clubs.png"))
Clubs_5 = pygame.image.load(os.path.join("Clubs", "5 of Clubs.png"))
Clubs_6 = pygame.image.load(os.path.join("Clubs", "6 of Clubs.png"))
Clubs_7 = pygame.image.load(os.path.join("Clubs", "7 of Clubs.png"))
Clubs_8 = pygame.image.load(os.path.join("Clubs", "8 of Clubs.png"))
Clubs_9 = pygame.image.load(os.path.join("Clubs", "9 of Clubs.png"))
Clubs_10 = pygame.image.load(os.path.join("Clubs", "10 of Clubs.png"))
Clubs_J = pygame.image.load(os.path.join("Clubs", "Jack of Clubs.png"))
Clubs_Q = pygame.image.load(os.path.join("Clubs", "Queen of Clubs.png"))
Clubs_K = pygame.image.load(os.path.join("Clubs", "King of Clubs.png"))
Clubs_A = pygame.image.load(os.path.join("Clubs", "Ace of Clubs.png"))

Spades_2 = pygame.image.load(os.path.join("Spades", "2 of Spades.png"))
Spades_3 = pygame.image.load(os.path.join("Spades", "3 of Spades.png"))
Spades_4 = pygame.image.load(os.path.join("Spades", "4 of Spades.png"))
Spades_5 = pygame.image.load(os.path.join("Spades", "5 of Spades.png"))
Spades_6 = pygame.image.load(os.path.join("Spades", "6 of Spades.png"))
Spades_7 = pygame.image.load(os.path.join("Spades", "7 of Spades.png"))
Spades_8 = pygame.image.load(os.path.join("Spades", "8 of Spades.png"))
Spades_9 = pygame.image.load(os.path.join("Spades", "9 of Spades.png"))
Spades_10 = pygame.image.load(os.path.join("Spades", "10 of Spades.png"))
Spades_J = pygame.image.load(os.path.join("Spades", "Jack of Spades.png"))
Spades_Q = pygame.image.load(os.path.join("Spades", "Queen of Spades.png"))
Spades_K = pygame.image.load(os.path.join("Spades", "King of Spades.png"))
Spades_A = pygame.image.load(os.path.join("Spades", "Ace of Spades.png"))

Diamonds_2 = pygame.image.load(os.path.join("Diamonds", "2 of Diamonds.png"))
Diamonds_3 = pygame.image.load(os.path.join("Diamonds", "3 of Diamonds.png"))
Diamonds_4 = pygame.image.load(os.path.join("Diamonds", "4 of Diamonds.png"))
Diamonds_5 = pygame.image.load(os.path.join("Diamonds", "5 of Diamonds.png"))
Diamonds_6 = pygame.image.load(os.path.join("Diamonds", "6 of Diamonds.png"))
Diamonds_7 = pygame.image.load(os.path.join("Diamonds", "7 of Diamonds.png"))
Diamonds_8 = pygame.image.load(os.path.join("Diamonds", "8 of Diamonds.png"))
Diamonds_9 = pygame.image.load(os.path.join("Diamonds", "9 of Diamonds.png"))
Diamonds_10 = pygame.image.load(os.path.join("Diamonds", "10 of Diamonds.png"))
Diamonds_J = pygame.image.load(os.path.join("Diamonds", "Jack of Diamonds.png"))
Diamonds_Q = pygame.image.load(os.path.join("Diamonds", "Queen of Diamonds.png"))
Diamonds_K = pygame.image.load(os.path.join("Diamonds", "King of Diamonds.png"))
Diamonds_A = pygame.image.load(os.path.join("Diamonds", "Ace of Diamonds.png"))


# deck = Deck()
# deck.build()
# deck.shuffle()


# player = Player()

# player.hand.append(deck.drawCard()) WORKS!!!
# player.showHand()


WIDTH, HEIGHT = 1000, 1000 #Make constant variables CAPITAL
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ryson's Card Game Collection!")
pygame.init()

baby_blue = (33, 171, 240)
click = False
FPS = 144
font = pygame.font.SysFont(None, 20)



def draw_main_menu(): #Multiple draw functions for each game
    WIN.fill(baby_blue)
    # WIN.blit(Spades_A, (100, 950))
    WIN.blit((show_card_image("♠️", 14)), (100, 950))
    pygame.display.update()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    mainClock = pygame.time.Clock()
    while True:
        draw_main_menu()
        draw_text("Ryson's Card Game Collection", font, (255, 255, 255), WIN, 400, 60)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 100, 200, 50)
        button_3 = pygame.Rect(50, 100, 200, 50)
        button_4 = pygame.Rect(50, 100, 200, 50)

        if button_1.collidepoint((mx, my)): #if you hover cursor over button, button should change color
            if click:
                war()

        if button_2.collidepoint((mx, my)): #if you hover cursor over button, button should change color
            if click:
                pass
                #blackjack()

        if button_3.collidepoint((mx, my)): #if you hover cursor over button, button should change color
            if click:
                pass
                #go_fish()

        if button_4.collidepoint((mx, my)): #if you hover cursor over button, button should change color
            if click:
                pass
                #RPS()
        
                
        pygame.draw.rect(WIN, (255, 0, 0), button_1)
        draw_text("WAR", font, (255, 255, 255), WIN, 100, 100)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        mainClock.tick(60)
        

if __name__ == "__main__":
    main_menu()


def war():
    running = True
    p1 = Player() #Player

    war_deck = Deck() #Main deck
    war_deck.build()
    war_deck.shuffle()
    
    play_deck = emptyDeck() #Deck to be used as a "cache", all cards will then be added to the winning player's deck


    cpu = Player()
    for i in range(26): #Deals out cards to the players
        p1.hand.append(war_deck.drawCard())
        cpu.hand.append(war_deck.drawCard())
        

    # if n == 1: #Need to figure out best way to implement multiple players
    #     cpu1 = Player()
    #     for i in range(26): #Deals out cards to the players
    #         p1.hand.append(deck.drawCard())
    #         cpu1.hand.append(deck.drawCard())
        

    # elif n == 2:
    #     cpu1 = Player()
    #     cpu2 = Player()
    #     for i in range(17):
    #         p1.hand.append(deck.drawCard())
    #         cpu1.hand.append(deck.drawCard())
    #         cpu2.hand.append(deck.drawCard())
        
    #     p1.hand.append(deck.drawCard())

    # elif n == 3:
    #     cpu1 = Player()
    #     cpu2 = Player()
    #     cpu3 = Player()
    #     for i in range(13): 
    #         p1.hand.append(deck.drawCard())
    #         cpu1.hand.append(deck.drawCard())
    #         cpu2.hand.append(deck.drawCard())
    #         cpu3.hand.append(deck.drawCard())


    value_played = []
    suit_played = []
    while running: #Is this needed?
        if len(p1.hand) == 0:
            a = str(input("YOU LOSE, PLAY AGAIN?(Y/N):")) #These will be replaced by buttons
            if a == "Y": #Deals out cards and continues the loop
                war_deck.build()
                war_deck.shuffle()
                for i in range(26):
                    p1.hand.append(war_deck.drawCard())
                    cpu.hand.append(war_deck.drawCard())
            elif a == 'N':
                running = False

        elif len(cpu.hand) == 0:
            if len(p1.self.hand) == 0:
                b = str(input("YOU WIN, PLAY AGAIN?(Y/N):")) #These will be replaced by buttons
                if b == "Y": #Deals out cards and continues the loop
                    war_deck.build()
                    war_deck.shuffle()
                    for i in range(26):
                        p1.hand.append(war_deck.drawCard())
                        cpu.hand.append(war_deck.drawCard())
            elif b == 'N':
                running = False
                
        else: #The actual game loop, everything above checks if somebody has won the game
            print("You have", len(p1.hand), "cards.")
            input("Press Enter to play card")
            print()
            value_played.append(p1.cardValue()) #Compares values to see who wins
            value_played.append(cpu.cardValue())

            suit_played.append(p1.cardSuit()) #Adds suits to call image
            suit_played.append(cpu.cardSuit())

            #p1.showHand()
            #print()
            print(value_played)
            print()
            # print(len(p1.hand))
            # print()

            play_deck.addCard(p1) #Adds cards to the "pot"
            play_deck.addCard(cpu)
            #Input Code here
            print("You played", value_played[0])
            input("Press Enter to continue")



            
            if value_played[0] > value_played[1]: #Player One wins the round
                print("You won this round. Gain 2 Cards")
                p1.drawDeck(play_deck)
                p1.drawDeck(play_deck)
            elif value_played[0] < value_played[1]: #CPU WINS the round
                print("You lost this round. Lose 2 Cards")
                cpu.drawDeck(play_deck)
                cpu.drawDeck(play_deck)
            elif value_played[0] == value_played[1]: #WAR
                    print("THIS IS WAR")
                    print()
                    for i in range(4): #Write exception if a player does not have enough cards to play, while loop?
                        value_played.append(p1.cardValue())
                        value_played.append(cpu.cardValue())
                        play_deck.addCard(p1)
                        play_deck.addCard(cpu)

                    print()
                    print(value_played)
                    print()

                    if value_played[8] > value_played[9]: #Player One WAR
                        for i in range(10):
                            p1.drawDeck(play_deck)
                        print("You won this round. Gain 10 Cards")
                    elif value_played[8] < value_played[9]: #CPU WINS WAR
                        for i in range(10):
                            cpu.drawDeck(play_deck)
                        print("You lost this round. Gain 10 Cards")
            
            while len(value_played) > 0: #Clears value_played list
                value_played.pop()

#main_menu()                

            


def show_card_image(suit, value): #Use cards suit to select array and then value to point at correct image ---> (value - 2)
    if suit == "♥":
        x = value - 2
        Hearts = [Heart_2, Heart_3, Heart_4, Heart_5, Heart_6, Heart_7, Heart_8, Heart_9, Heart_10, Heart_J, Heart_Q, Heart_K, Heart_A]
        return Hearts[x]
    elif suit == "♣️":
        x = value - 2
        Clubs = [Clubs_2, Clubs_3, Clubs_4, Clubs_5, Clubs_6, Clubs_7, Clubs_8, Clubs_9, Clubs_10, Clubs_J, Clubs_Q, Clubs_K, Clubs_A]
        return Clubs[x]
    elif suit == "♠️":
        x = value - 2
        Spades = [Spades_2, Spades_3, Spades_4, Spades_5, Spades_6, Spades_7, Spades_8, Spades_9, Spades_10, Spades_J, Spades_Q, Spades_K, Spades_A]
        y = Spades[x]
        return y
    elif suit == "♦️":
        x = value - 2
        Diamonds = [Diamonds_2, Diamonds_3, Diamonds_4, Diamonds_5, Diamonds_6, Diamonds_7, Diamonds_8, Diamonds_9, Diamonds_10, Diamonds_J, Diamonds_Q, Diamonds_K, Diamonds_A]
        return Diamonds[x]



war()

    
        




        
    







# def blackjack():

#     print("Welcome to BlackJack!")
#     print("")

#     Jack, Queen, King = 10
#     Ace1 = 11
#     Ace2 = 1
#     finish = False

#     #card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
#     card = [2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace1, Ace2]
#     suit = ["♥", "♠️", "♣️", "♦️"]

#     hand = []
#     h_total = 0
#     dealer = []
#     d_total = 0

#     card = 0
#     item = ""
#     yn = ""

#     while finish == False:
#         while h_total < 21 or d_total < 21:
#             c = card[random(0, 14)] #Need to generate 2 CARDS on startup
#             s = suit[random(0, 3)] 
#             if c == card[9] or card[10] or card[11] or card[12] or card[13]:
#                 h_total = h_total + c
#                 str(c) = c
#                 hand.append(str(c + " of " + s))
#                 print("You have been dealt a " + hand)
#                 print("")
#                 choice = input("Enter H for hit OR S for stand")

#                 while choice != "H" or "h" or "S" or "s":
#                     if choice == "H" or "h":
#                         item, card = randomCard(random(0, 14), random(0, 3))
#                         hand.append(item)
#                         if h_total > 21:
#                             print("Your hand is a bust! You LOSE!")
#                             while yn != 'Y' or 'N':
#                                 yn = input("Play Again? (Y/N)")
#                                 if yn == "Y":
#                                     yn == ""
#                                     blackjack()
#                                 elif yn == "N":
#                                     yn = ""
#                                     menu()
#                                 else:
#                                     yn = input("Play Again? (Y/N)")
#                         else:
                            

                        

                    
#                     elif choice == "S" or "s":
#                         if 19 < d_total <= 21:
#                             print("The dealer has took a stand")
#                             if d_total


#                     else:
#                         choice = input("ERROR. Enter H for hit OR S for stand")

#             else:
#                 h_total = h_total + c
#                 hand.append(c + " of " + s)
#                 print("You have been dealt a" + c + " of ", s + ".")
#                 print("")
#                 choice = input("Please enter HIT or STAND")
    



# def goFish():
#     print("Welcome to GO FISH!")


# def war():
#     print("Welcome to WAR!")
#     print("")
#     print("In this game, you will be given 26 random cards")

#     card = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace1", "Ace2"]
#     suit = ["♥", "♠️", "♣️", "♦️"]




# def RPS():
#     print("Welcome to Rock, Paper, Scissors")
#     print("")
    
#     p_score = 0
#     cpu_score = 0
#     plays = [Rock, Paper, Scissors]
#     cpu = ""
    
#     choice = input("Instructions? (Y/N)")
#     if choice == "Y":
#         print("This game is simple. Type 'R' to throw out rock, 'S' to throw out scissors or 'P' to throw you paper")
#         print("")
#         print("Paper beats Rock, Rock beats Scissors and Scissors beats Paper. You get one point for every match. First to 10 wins!")
#     elif choice == "N":
#         return ""
#     while p_score or cpu_score < 9:
#         print("The score is " + p_score + " - " + cpu_score)
#         choice = input("Please enter 'R', 'P', or 'S' to pick your move: ")
#         cpu = plays[random(0, 2)]
#         if choice == R:
#             if cpu == Rock:
            
#             elif cpu == Paper:
            
#             elif cpu == Scissors:
            
#         elif choice == S:
#             if cpu == Rock:
            
#             elif cpu == Paper:
            
#             elif cpu == Scissors:
            
#         elif choice == P:
#             if cpu == Rock:
            
#             elif cpu == Paper:
            
#             elif cpu == Scissors:
            
         
             
        
        
        
        
    
    




