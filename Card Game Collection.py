from multiprocessing.connection import wait
import random, pygame, os, sys
from pygame.locals import *


# ! ALWAYS define the main variables at the top

WIDTH, HEIGHT = 1200, 800  # Make constant variables CAPITAL
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ryson's Card Game Collection!")
pygame.init()

baby_blue = (33, 171, 240)
click = False
FPS = 60

coins = 0 # For money system, will be used in to buy card skins

# fonts
font = pygame.font.SysFont("Sans", 20)
main_font = pygame.font.Font("fonts/lm2.otf", 25)
azonix = pygame.font.Font("fonts/Azonix.otf", 60)
azonix_large = pygame.font.Font("fonts/Azonix.otf", 40)
azonix_l = pygame.font.Font("fonts/Azonix.otf", 65)
main_font_large = pygame.font.Font("fonts/lm2.otf", 100)

# colors
BLACK = (0, 0, 0)
BROWN = (155, 155, 155)
LIGHT_BROWN = (195, 155, 119)
WHITE = (255, 255, 255)

# images

WAR = pygame.image.load("images/war_heading.png")
MAIN_MENU = pygame.image.load("images/main_menu.png")

green_deck = pygame.transform.scale(pygame.image.load("images/green_deck.png"), (100, 150))
green_card = pygame.transform.scale(pygame.image.load("images/green_deck.png"), (100, 150))
green_card_turning1 = pygame.transform.scale(pygame.image.load("images/green_card_turning1.png"), (100, 150))
green_card_turning2 = pygame.transform.scale(pygame.image.load("images/green_card_turning2.png"), (100, 150))

Heart_2 = pygame.transform.scale(pygame.image.load("images/hearts/2 of Hearts.png"), (100, 150))
Heart_3 = pygame.transform.scale(pygame.image.load("images/hearts/3 of Hearts.png"), (100, 150))
Heart_4 = pygame.transform.scale(pygame.image.load("images/hearts/4 of Hearts.png"), (100, 150))
Heart_5 = pygame.transform.scale(pygame.image.load("images/hearts/5 of Hearts.png"), (100, 150))
Heart_6 = pygame.transform.scale(pygame.image.load("images/hearts/6 of Hearts.png"), (100, 150))
Heart_7 = pygame.transform.scale(pygame.image.load("images/hearts/7 of Hearts.png"), (100, 150))
Heart_8 = pygame.transform.scale(pygame.image.load("images/hearts/8 of Hearts.png"), (100, 150))
Heart_9 = pygame.transform.scale(pygame.image.load("images/hearts/9 of Hearts.png"), (100, 150))
Heart_10 = pygame.transform.scale(pygame.image.load("images/hearts/10 of Hearts.png"), (100, 150))
Heart_J = pygame.transform.scale(pygame.image.load("images/hearts/Jack of Hearts.png"), (100, 150))
Heart_Q = pygame.transform.scale(pygame.image.load("images/hearts/Queen of Hearts.png"), (100, 150))
Heart_K = pygame.transform.scale(pygame.image.load("images/hearts/King of Hearts.png"), (100, 150))
Heart_A = pygame.transform.scale(pygame.image.load("images/hearts/Ace of Hearts.png"), (100, 150))

Clubs_2 = pygame.transform.scale(pygame.image.load("images/clubs/2 of Clubs.png"), (100, 150))
Clubs_3 = pygame.transform.scale(pygame.image.load("images/clubs/3 of Clubs.png"), (100, 150))
Clubs_4 = pygame.transform.scale(pygame.image.load("images/clubs/4 of Clubs.png"), (100, 150))
Clubs_5 = pygame.transform.scale(pygame.image.load("images/clubs/5 of Clubs.png"), (100, 150))
Clubs_6 = pygame.transform.scale(pygame.image.load("images/clubs/6 of Clubs.png"), (100, 150))
Clubs_7 = pygame.transform.scale(pygame.image.load("images/clubs/7 of Clubs.png"), (100, 150))
Clubs_8 = pygame.transform.scale(pygame.image.load("images/clubs/8 of Clubs.png"), (100, 150))
Clubs_9 = pygame.transform.scale(pygame.image.load("images/clubs/9 of Clubs.png"), (100, 150))
Clubs_10 = pygame.transform.scale(pygame.image.load("images/clubs/10 of Clubs.png"), (100, 150))
Clubs_J = pygame.transform.scale(pygame.image.load("images/clubs/Jack of Clubs.png"), (100, 150))
Clubs_Q = pygame.transform.scale(pygame.image.load("images/clubs/Queen of Clubs.png"), (100, 150))
Clubs_K = pygame.transform.scale(pygame.image.load("images/clubs/King of Clubs.png"), (100, 150))
Clubs_A = pygame.transform.scale(pygame.image.load("images/clubs/Ace of Clubs.png"), (100, 150))

Spades_2 = pygame.transform.scale(pygame.image.load("images/spades/2 of Spades.png"), (100, 150))
Spades_3 = pygame.transform.scale(pygame.image.load("images/spades/3 of Spades.png"), (100, 150))
Spades_4 = pygame.transform.scale(pygame.image.load("images/spades/4 of Spades.png"), (100, 150))
Spades_5 = pygame.transform.scale(pygame.image.load("images/spades/5 of Spades.png"), (100, 150))
Spades_6 = pygame.transform.scale(pygame.image.load("images/spades/6 of Spades.png"), (100, 150))
Spades_7 = pygame.transform.scale(pygame.image.load("images/spades/7 of Spades.png"), (100, 150))
Spades_8 = pygame.transform.scale(pygame.image.load("images/spades/8 of Spades.png"), (100, 150))
Spades_9 = pygame.transform.scale(pygame.image.load("images/spades/9 of Spades.png"), (100, 150))
Spades_10 = pygame.transform.scale(pygame.image.load("images/spades/10 of Spades.png"), (100, 150))
Spades_J = pygame.transform.scale(pygame.image.load("images/spades/Jack of Spades.png"), (100, 150))
Spades_Q = pygame.transform.scale(pygame.image.load("images/spades/Queen of Spades.png"), (100, 150))
Spades_K = pygame.transform.scale(pygame.image.load("images/spades/King of Spades.png"), (100, 150))
Spades_A = pygame.transform.scale(pygame.image.load("images/spades/Ace of Spades.png"), (100, 150))

Diamonds_2 = pygame.transform.scale(pygame.image.load("images/diamonds/2 of Diamonds.png"), (100, 150))
Diamonds_3 = pygame.transform.scale(pygame.image.load("images/diamonds/3 of Diamonds.png"), (100, 150))
Diamonds_4 = pygame.transform.scale(pygame.image.load("images/diamonds/4 of Diamonds.png"), (100, 150))
Diamonds_5 = pygame.transform.scale(pygame.image.load("images/diamonds/5 of Diamonds.png"), (100, 150))
Diamonds_6 = pygame.transform.scale(pygame.image.load("images/diamonds/6 of Diamonds.png"), (100, 150))
Diamonds_7 = pygame.transform.scale(pygame.image.load("images/diamonds/7 of Diamonds.png"), (100, 150))
Diamonds_8 = pygame.transform.scale(pygame.image.load("images/diamonds/8 of Diamonds.png"), (100, 150))
Diamonds_9 = pygame.transform.scale(pygame.image.load("images/diamonds/9 of Diamonds.png"), (100, 150))
Diamonds_10 = pygame.transform.scale(pygame.image.load("images/diamonds/10 of Diamonds.png"), (100, 150))
Diamonds_J = pygame.transform.scale(pygame.image.load("images/diamonds/Jack of Diamonds.png"), (100, 150))
Diamonds_Q = pygame.transform.scale(pygame.image.load("images/diamonds/Queen of Diamonds.png"), (100, 150))
Diamonds_K = pygame.transform.scale(pygame.image.load("images/diamonds/King of Diamonds.png"), (100, 150))
Diamonds_A = pygame.transform.scale(pygame.image.load("images/diamonds/Ace of Diamonds.png"), (100, 150))


#Classes

#War Classes
class Card:
    def __init__(self, number, suit, value):
        self.suit = suit
        self.number = number
        self.value = value

    def card_value(self):
        return self.value

    def animate(direction):
        pass


class emptyDeck:
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

    #Added drawDeck to draw whole deck
    def drawDeck(self, deck):
        for card in self.cards:
            deck.append(card)

        self.cards.clear()

    def addCard(self, player):
        self.cards.append(player.playCard())


class Deck:
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
        for suit in ["heart", "spade", "club", "diamond"]:
            for v in range(2, 15):
                if v == 11:
                    self.cards.append(Card("Jack", suit, v))
                elif v == 12:
                    self.cards.append(Card("Queen", suit, v))
                elif v == 13:
                    self.cards.append(Card("King", suit, v))
                elif v == 14:
                    self.cards.append(Card("Ace", suit, v))
                else:
                    self.cards.append(Card(v, suit, v))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class war_player(object):  # Create different types of players for each game
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

class WarGame:
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2

    #Checking for winner
    def war_winner(self, p1, cpu, deck):
        if len(p1.hand) == 0 and len(deck) == 0:
            return cpu
        elif len(cpu.hand) == 0 and len(deck) == 0:
            return p1

        return None

    #Comparing cards for direction
    def compare_cards(self, value1, value2):
        if value1 > value2:
            return True
        elif value1 < value2:
            return False

        return "war"
    
# ----------------------------------------- #

#RPS Classes

class RPSGame:
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.score = 0
        self.scoreLimit = 0

    #Checking for winner
    def rps_winner(self, p1, cpu):
        if p1.score == self.scoreLimit:
            return p1
        elif cpu.score == self.scoreLimit:
            return cpu

        return None

    def compare_choices(self, p1_choice, cpu_choice, p1_score, cpu_score): # Rock Beats Scissors, Scissors Beats Paper, Paper Beats Rock
        match p1_choice: #Usage of switch cases
            case "rock":
                if cpu_choice == "scissors":
                    p1_score += 1
                elif cpu_choice == "paper":
                    cpu_score += 1
                else:
                    pass #Tie
            case "scissors":
                if cpu_choice == "paper":
                    p1_score += 1
                elif cpu_choice == "rock":
                    cpu_score += 1
                else:
                    pass #Tie
            case "paper":
                if cpu_choice == "rock":
                    p1_score += 1
                elif cpu_choice == "scissors":
                    cpu_score += 1
                else:
                    pass #Tie

class rps_player(object):  # Create different types of players for each game
    def __init__(self):
        self.score = 0
        self.current_choice = None

    def updateChoice(self, choice): #When player chooses rock, paper or scissors
        self.current_choice = choice
    


def RPS():
    running = True
    clock = pygame.time.Clock()
    p1 = rps_player()
    cpu = rps_player()
    rps_game_session = RPSGame(p1, cpu)
    FPS = 60

    def redraw_initial_rps_window():
        #Drawing Initial Screen on RPS startup

        WIN.fill("Purple")
        WIN.blit(WAR, (0, 0)) # Background

        pygame.display.update()

    #def set_rps_score_limit():

    while running:
        clock.tick(FPS)

        redraw_initial_rps_window()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #Winner Check
        if rps_game_session.rps_winner(p1, cpu, p1.score, cpu.score):
            if rps_game_session.rps_winner(p1, cpu, p1.score, cpu.score) == p1:
                winner = "you"
                rps_restart_menu(winner)
            else:
                winner = "cpu"
                rps_restart_menu(winner)


        
        



def war():
    running = True
    clock = pygame.time.Clock()
    p1 = war_player()
    cpu = war_player()
    war_game_session = WarGame(p1, cpu)
    FPS = 144

    war_deck = Deck()  # Main deck
    war_deck.build()
    war_deck.shuffle()

    play_deck = emptyDeck()  # Deck to be used as a "cache", all cards will then be added to the winning player's deck

    for i in range(26):  # Deals out cards to the players
        p1.hand.append(war_deck.drawCard())
        cpu.hand.append(war_deck.drawCard())

    value_played = []
    suit_played = []

    # text, img, coordinates

    p1_cards_left = main_font.render(str(len(p1.hand)) + " left ", False, BLACK)
    cpu_cards_left = main_font.render(str(len(cpu.hand)) + " left ", False, BLACK)
    war_text = azonix_large.render("WAR", False, BLACK)
    p1_deck_rect = pygame.Rect(WIDTH / 2 - green_deck.get_width() / 2, HEIGHT - green_deck.get_height() * 1.5,
                               green_deck.get_width(), green_deck.get_height())
    cpu_deck_rect = pygame.Rect(WIDTH / 2 - green_deck.get_width() / 2, green_deck.get_height() * 0.5,
                                green_deck.get_width(), green_deck.get_height())

    current_card = green_card
    current_card2 = green_card

    # ! animation variables for coordinates and card moving animations

    p1_card_x, p1_card_y = (p1_deck_rect.x, p1_deck_rect.y)
    cpu_card_x, cpu_card_y = (cpu_deck_rect.x, cpu_deck_rect.y)

    p1_war_card_x, p1_war_card_y = (p1_deck_rect.x, p1_deck_rect.y)
    p1_war_card_x2, p1_war_card_y2 = (p1_deck_rect.x, p1_deck_rect.y)
    p1_war_card_x3, p1_war_card_y3 = (p1_deck_rect.x, p1_deck_rect.y)

    cpu_war_card_x, cpu_war_card_y = (cpu_deck_rect.x, cpu_deck_rect.y)
    cpu_war_card_x2, cpu_war_card_y2 = (cpu_deck_rect.x, cpu_deck_rect.y)
    cpu_war_card_x3, cpu_war_card_y3 = (cpu_deck_rect.x, cpu_deck_rect.y)

    # ! animation variables: animations in pygame get messy; usage of flags to determine which animation to run

    p1_move_card = False
    cpu_move_card = False
    move_back = False
    direction = True
    moving = False
    winner = None

    # counters
    wait_time = 0
    wait_time_war = 0

    def redraw_initial_war_window():
        #Drawing Initial Screen on War Startup

        # bg = pygame.image.load("images/war_background.png") THIS IS SUPER LAGGY FROM SOME REASON
        # WIN.blit(bg, (0, 0))

        WIN.fill("Dark Green")

        WIN.blit(WAR, (0, 0)) # Background
        WIN.blit(green_deck, (p1_deck_rect.x, p1_deck_rect.y)) # Player 1 Deck
        WIN.blit(green_deck, (cpu_deck_rect.x, cpu_deck_rect.y))    # CPU Deck
        WIN.blit(current_card, (p1_card_x, p1_card_y)) # Player 1 Card
        WIN.blit(current_card2, (cpu_card_x, cpu_card_y)) # CPU Card

        WIN.blit(current_card, (p1_card_x, p1_card_y)) 
        WIN.blit(current_card, (cpu_card_x, cpu_card_y))

        WIN.blit(green_card, (p1_war_card_x, p1_war_card_y)) 
        WIN.blit(green_card, (cpu_war_card_x, cpu_war_card_y))
        WIN.blit(green_card, (p1_war_card_x2, p1_war_card_y2))
        WIN.blit(green_card, (cpu_war_card_x2, cpu_war_card_y2))
        WIN.blit(green_card, (p1_war_card_x3, p1_war_card_y3))
        WIN.blit(green_card, (cpu_war_card_x3, cpu_war_card_y3))

        #Checking a few things to blit over when animating, socards have been layed on top, coming from top, etc.

        if direction != "war":
            WIN.blit(current_card, (p1_card_x, p1_card_y))
            WIN.blit(current_card, (cpu_card_x, cpu_card_y))
            WIN.blit(current_card, (p1_card_x, p1_card_y))
            WIN.blit(current_card2, (cpu_card_x, cpu_card_y))

        if move_back:
            WIN.blit(green_deck, (p1_deck_rect.x, p1_deck_rect.y))
            WIN.blit(green_deck, (cpu_deck_rect.x, cpu_deck_rect.y))

        if wait_time >= 1 and wait_time <= FPS:
            if direction == "war":
                WIN.blit(war_text, (WIDTH / 2 - war_text.get_width() / 2, HEIGHT / 2 - war_text.get_height() / 2))

        #Cards Left

        WIN.blit(p1_cards_left, (p1_deck_rect.x + p1_deck_rect.width * 1.25,
                                 p1_deck_rect.y + p1_deck_rect.height / 2 - p1_cards_left.get_height() / 2))
        WIN.blit(cpu_cards_left, (cpu_deck_rect.x + cpu_deck_rect.width * 1.25,
                                  cpu_deck_rect.y + cpu_deck_rect.height / 2 - cpu_cards_left.get_height() / 2))

        pygame.display.update()
    

    while running:  #Main WarGame Loop
        clock.tick(FPS)

        #Updates cards left
        p1_cards_left = main_font.render(str(len(p1.hand)) + " left ", False, BLACK)
        cpu_cards_left = main_font.render(str(len(cpu.hand)) + " left ", False, BLACK)

        #Winner Check
        if war_game_session.war_winner(p1, cpu, value_played):
            if war_game_session.war_winner(p1, cpu, value_played) == p1:
                winner = "you"
                war_restart_menu(winner)
            else:
                winner = "cpu"
                war_restart_menu(winner)

        # ! checking for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                # ! if clicked
                m = pygame.mouse.get_pos()
                # ! if player clicked on his deck
                if p1_deck_rect.collidepoint(m):
                    # ! if not in animation or winner
                    if not moving and not winner:
                        # ! appending values, etc.
                        moving = True

                        value_played.append(p1.cardValue())
                        suit_played.append(p1.cardSuit())
                        play_deck.addCard(p1)
                        p1_move_card = True

                        value_played.append(cpu.cardValue())
                        suit_played.append(cpu.cardSuit())
                        play_deck.addCard(cpu)

                        cpu_move_card = True

                        # ! getting direction
                        direction = war_game_session.compare_cards(value_played[0], value_played[1])

        # !
        # ! The animations in pygame can get messy. You can put everything in functions and classes if you want and the main loop of the game will look better
        # ! I have not done that because it will get event more confusing because you will have to give many unclear parameters to the functions and then work with them in the classes
        # !

        # ! starting moving the cards (for animation)

        if p1_move_card:
            if p1_card_y > HEIGHT / 2 - p1_deck_rect.height / 2 or p1_card_x > p1_deck_rect.x - p1_deck_rect.width / 2:
                p1_card_y -= 9
                p1_card_x -= 2.75
            else:
                p1_move_card = False
                # ! showing image when at place
                img = show_card_image(suit_played[0], value_played[0])
                current_card = img

                p1_war_card_x, p1_war_card_y = p1_war_card_x2, p1_war_card_y2 = p1_war_card_x3, p1_war_card_y3 = (
                p1_deck_rect.x, p1_deck_rect.y)

        if cpu_move_card:
            if cpu_card_y < HEIGHT / 2 - cpu_deck_rect.height / 2 or cpu_card_x < cpu_deck_rect.x + cpu_deck_rect.width / 2:
                cpu_card_y += 9
                cpu_card_x += 2.75
            else:
                cpu_move_card = False
                img = show_card_image(suit_played[1], value_played[1])
                current_card2 = img
                wait_time = 1

                cpu_war_card_x, cpu_war_card_y = cpu_war_card_x2, cpu_war_card_y2 = cpu_war_card_x3, cpu_war_card_y3 = (
                cpu_deck_rect.x, cpu_deck_rect.y)

        # ! waiting a bit when card layed (1 sec)
        if wait_time >= 1:
            if wait_time < FPS:  # ! change wait time here if you want
                wait_time += 1
            else:
                wait_time = 0
                move_back = True

                if direction == "war":
                    wait_time_war = 1

        # ! moving cards back
        if move_back: # move back is true when wait time is over
            done = True

            if direction == True:
                if p1_card_x < p1_deck_rect.x:
                    p1_card_x += 5
                    done = False
                if p1_card_y < p1_deck_rect.y:
                    p1_card_y += 10
                    done = False
                if cpu_card_x > p1_deck_rect.x:
                    cpu_card_x -= 5
                    done = False
                if cpu_card_y < p1_deck_rect.y:
                    cpu_card_y += 10
                    done = False

                if done:
                    # ! when completely moved back, reset variables, allow to move again and append won cards
                    move_back = False
                    moving = False
                    p1_card_x, p1_card_y = (p1_deck_rect.x, p1_deck_rect.y)
                    cpu_card_x, cpu_card_y = (cpu_deck_rect.x, cpu_deck_rect.y)
                    value_played.clear()
                    suit_played.clear()
                    play_deck.drawDeck(p1.hand)

                current_card = green_card
                current_card2 = green_card

            elif direction == False:
                if p1_card_x < cpu_deck_rect.x:
                    p1_card_x += 5
                    done = False
                if p1_card_y > cpu_deck_rect.y:
                    p1_card_y -= 10
                    done = False
                if cpu_card_x > cpu_deck_rect.x:
                    cpu_card_x -= 5
                    done = False
                if cpu_card_y > cpu_deck_rect.y:
                    cpu_card_y -= 10
                    done = False

                if done:
                    move_back = False
                    moving = False
                    p1_card_x, p1_card_y = (p1_deck_rect.x, p1_deck_rect.y)
                    cpu_card_x, cpu_card_y = (cpu_deck_rect.x, cpu_deck_rect.y)
                    value_played.clear()
                    suit_played.clear()
                    print("clear")
                    play_deck.drawDeck(cpu.hand)

                current_card = green_card
                current_card2 = green_card


            #War
            elif direction == "war":

                #Move 3 cards and append cards to list
                if wait_time_war >= 1 and wait_time_war < FPS / 2:
                    if wait_time_war == 1:
                        play_deck.addCard(p1)
                        play_deck.addCard(cpu)

                    if p1_war_card_y > HEIGHT / 2 - p1_deck_rect.height / 2 or p1_war_card_x > p1_deck_rect.x - p1_deck_rect.width / 2:
                        p1_war_card_y -= 9
                        p1_war_card_x -= 2.75
                    if cpu_war_card_y < HEIGHT / 2 - cpu_deck_rect.height / 2 or cpu_war_card_x < cpu_deck_rect.x + cpu_deck_rect.width / 2:
                        cpu_war_card_y += 9
                        cpu_war_card_x += 2.75

                elif wait_time_war >= FPS / 2 and wait_time_war < FPS:
                    if wait_time_war == FPS / 2:
                        play_deck.addCard(p1)
                        play_deck.addCard(cpu)

                    if p1_war_card_y2 > HEIGHT / 2 - p1_deck_rect.height / 2 or p1_war_card_x2 > p1_deck_rect.x - p1_deck_rect.width / 2:
                        p1_war_card_y2 -= 9
                        p1_war_card_x2 -= 2.75

                    if cpu_war_card_y2 < HEIGHT / 2 - cpu_deck_rect.height / 2 or cpu_war_card_x2 < cpu_deck_rect.x + cpu_deck_rect.width / 2:
                        cpu_war_card_y2 += 9
                        cpu_war_card_x2 += 2.75

                elif wait_time_war >= FPS and wait_time_war < FPS * 1.5:
                    if wait_time_war == FPS:
                        play_deck.addCard(p1)
                        play_deck.addCard(cpu)

                    if p1_war_card_y3 > HEIGHT / 2 - p1_deck_rect.height / 2 or p1_war_card_x3 > p1_deck_rect.x - p1_deck_rect.width / 2:
                        p1_war_card_y3 -= 9
                        p1_war_card_x3 -= 2.75

                    if cpu_war_card_y3 < HEIGHT / 2 - cpu_deck_rect.height / 2 or cpu_war_card_x3 < cpu_deck_rect.x + cpu_deck_rect.width / 2:
                        cpu_war_card_y3 += 9
                        cpu_war_card_x3 += 2.75

                # Resetting variables and allowing moving again. Then moving normally again and earning all war cards if won
                elif wait_time_war > FPS * 1.5:
                    wait_time_war = 0
                    moving = False
                    move_back = False
                    current_card = current_card2 = green_card
                    p1_card_x, p1_card_y = (p1_deck_rect.x, p1_deck_rect.y)
                    cpu_card_x, cpu_card_y = (cpu_deck_rect.x, cpu_deck_rect.y)
                    value_played.clear()
                    suit_played.clear()
                    print("cleared")

                if wait_time_war >= 1:
                    wait_time_war += 1

        redraw_initial_war_window()

        pygame.display.update()


#Restart Menu
def war_restart_menu(winner):
    clock = pygame.time.Clock()
    FPS = 60
    run = True

    # ! text and rect var
    if winner == "you":
        won = main_font_large.render("YOU WON", False, WHITE)
    else:
        won = main_font_large.render("YOU LOST", False, WHITE)

    restart = main_font.render("RESTART GAME", False, WHITE)
    back = main_font.render("MAIN MENU", False, WHITE)
    leave = main_font.render("QUIT", False, WHITE)

    leave_rect = pygame.Rect(WIDTH / 2 - 125 - 300, HEIGHT / 2 + 100, 250, 50)
    back_rect = pygame.Rect(WIDTH / 2 - 125, HEIGHT / 2 + 100, 250, 50)
    restart_rect = pygame.Rect(WIDTH / 2 + 125 + 50, HEIGHT / 2 + 100, 250, 50)

    def redraw_war_restart_window():
        #Draws restart menu

        WIN.blit(won, (WIDTH / 2 - won.get_width() / 2, HEIGHT / 2 - won.get_height()))

        pygame.draw.rect(WIN, (255, 0, 0), leave_rect, 5)
        pygame.draw.rect(WIN, (120, 0, 0), leave_rect)

        pygame.draw.rect(WIN, (100, 100, 100), back_rect, 5)
        pygame.draw.rect(WIN, (20, 20, 20), back_rect)

        pygame.draw.rect(WIN, (0, 255, 0), restart_rect, 5)
        pygame.draw.rect(WIN, (0, 100, 0), restart_rect)

        WIN.blit(leave, (leave_rect.x + leave_rect.width / 2 - leave.get_width() / 2,
                         leave_rect.y + leave_rect.height / 2 - leave.get_height() / 2))
        WIN.blit(back, (back_rect.x + back_rect.width / 2 - back.get_width() / 2,
                        back_rect.y + back_rect.height / 2 - back.get_height() / 2))
        WIN.blit(restart, (restart_rect.x + restart_rect.width / 2 - restart.get_width() / 2,
                           restart_rect.y + restart_rect.height / 2 - restart.get_height() / 2))

        pygame.display.update()

    while run:
        clock.tick(FPS)

        # ! checking for clicking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                m = pygame.mouse.get_pos()

                if leave_rect.collidepoint(m):
                    pygame.quit()
                    sys.exit()
                if back_rect.collidepoint(m):
                    main_menu()
                if restart_rect.collidepoint(m):
                    return war()

        redraw_war_restart_window()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    clock = pygame.time.Clock()
    FPS = 60
    run = True

    # ! to calculate the right pos, all the text variables have to be defined normally, not with "draw_text"

    # heading = azonix_large.render("Ryson's Card Game Collection", False, WHITE)

    play = azonix.render("Play", False, WHITE)
    options = azonix.render("Options", False, WHITE)
    about = azonix.render("About", False, WHITE)
    help = azonix.render("Help", False, WHITE)

    # ! variables that need to be defined for hover animation

    play_rect = pygame.Rect(WIDTH / 2 - play.get_width() / 2 - 10, HEIGHT / 2 - 200 - 4, play.get_width() + 20,
                            play.get_height() - 4)
    options_rect = pygame.Rect(WIDTH / 2 - options.get_width() / 2 - 10, HEIGHT / 2 - 50 - 4, options.get_width() + 20,
                               options.get_height() - 4)
    about_rect = pygame.Rect(WIDTH / 2 - about.get_width() / 2 - 10, HEIGHT / 2 + 50 + about.get_height() - 4,
                             about.get_width() + 20, about.get_height() - 4)
    help_rect = pygame.Rect(WIDTH / 2 - help.get_width() / 2 - 10, HEIGHT / 2 + 200 + help.get_height() - 4,
                            help.get_width() + 20, help.get_height() - 4)

    def draw_main_menu():
        WIN.fill((24, 24, 24))
        WIN.blit(MAIN_MENU, (0, 0))
        # WIN.blit(heading, (WIDTH / 2 - heading.get_width() / 2, 200))

        # ! hover animation
        m = pygame.mouse.get_pos()
        if play_rect.collidepoint(m):
            pygame.draw.rect(WIN, (80, 80, 80), play_rect, 2)
        elif options_rect.collidepoint(m):
            pygame.draw.rect(WIN, (80, 80, 80), options_rect, 2)
        elif about_rect.collidepoint(m):
            pygame.draw.rect(WIN, (80, 80, 80), about_rect, 2)
        elif help_rect.collidepoint(m):
            pygame.draw.rect(WIN, (80, 80, 80), help_rect, 2)

        WIN.blit(play, (WIDTH / 2 - play.get_width() / 2, HEIGHT / 2 - 200))
        WIN.blit(options, (WIDTH / 2 - options.get_width() / 2, HEIGHT / 2 - 50))
        WIN.blit(about, (WIDTH / 2 - about.get_width() / 2, HEIGHT / 2 + 50 + about.get_height()))
        WIN.blit(help, (WIDTH / 2 - help.get_width() / 2, HEIGHT / 2 + 200 + help.get_height()))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        draw_main_menu()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                # ! have not put hover animation with check clicked in one block
                m = pygame.mouse.get_pos()
                if play_rect.collidepoint(m):
                    return play_menu()  # TODO: go to play options
                elif options_rect.collidepoint(m):
                    pass  # TODO: go to options
                elif about_rect.collidepoint(m):
                    pass  # TODO: go to about
                elif help_rect.collidepoint(m):
                    pass  # TODO: go to help


def play_menu():
    clock = pygame.time.Clock()
    FPS = 60
    run = True

    heading = azonix_l.render("Ryson's", False, WHITE)
    under_heading = azonix_l.render("Card Game Collection", False, WHITE)

    war_text = azonix_large.render("WAR", False, WHITE)
    blackjack = azonix_large.render("BLACKJACK", False, WHITE)
    go_fish = azonix_large.render("GO FISH", False, WHITE)
    rps = azonix_large.render("RPS", False, WHITE)

    # ! variables that need to be defined for hover animation

    war_text_rect = pygame.Rect(WIDTH * 0.25 - war_text.get_width() / 2 - 10, HEIGHT / 2 - 50 - 4,
                                war_text.get_width() + 20, war_text.get_height())
    blackjack_rect = pygame.Rect(WIDTH * 0.75 - blackjack.get_width() / 2 - 10, HEIGHT / 2 - 50 - 4,
                                 blackjack.get_width() + 20, blackjack.get_height())
    go_fish_rect = pygame.Rect(WIDTH * 0.25 - go_fish.get_width() / 2 - 10, HEIGHT / 2 + 200 + go_fish.get_height() - 4,
                               go_fish.get_width() + 20, go_fish.get_height())
    rps_rect = pygame.Rect(WIDTH * 0.75 - rps.get_width() / 2 - 10, HEIGHT / 2 + 200 + rps.get_height() - 4,
                           rps.get_width() + 20, rps.get_height())

    def draw_play_menu():
        WIN.fill((24, 24, 24))
        WIN.blit(heading, (WIDTH / 2 - heading.get_width() / 2, 100))
        WIN.blit(under_heading, (WIDTH / 2 - under_heading.get_width() / 2, 170))

        # ! hover animation
        m = pygame.mouse.get_pos()
        if war_text_rect.collidepoint(m):
            pygame.draw.rect(WIN, (80, 80, 80), war_text_rect, 2)
        elif blackjack_rect.collidepoint(m):
            pygame.draw.rect(WIN, (80, 80, 80), blackjack_rect, 2)
        elif go_fish_rect.collidepoint(m):
            pygame.draw.rect(WIN, (80, 80, 80), go_fish_rect, 2)
        elif rps_rect.collidepoint(m):
            pygame.draw.rect(WIN, (80, 80, 80), rps_rect, 2)

        WIN.blit(war_text, (WIDTH * 0.25 - war_text.get_width() / 2, HEIGHT / 2 - 50))
        WIN.blit(blackjack, (WIDTH * 0.75 - blackjack.get_width() / 2, HEIGHT / 2 - 50))
        WIN.blit(go_fish, (WIDTH * 0.25 - go_fish.get_width() / 2, HEIGHT / 2 + 200 + go_fish.get_height()))
        WIN.blit(rps, (WIDTH * 0.75 - rps.get_width() / 2, HEIGHT / 2 + 200 + rps.get_height()))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        draw_play_menu()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                # ! have not put hover animation with check clicked in one block
                m = pygame.mouse.get_pos()
                if war_text_rect.collidepoint(m):
                    return war()  # TODO: go to play options
                elif blackjack_rect.collidepoint(m):
                    pass  # TODO: go to blackjack
                elif go_fish_rect.collidepoint(m):
                    pass  # TODO: go to go fish
                elif rps_rect.collidepoint(m):
                    return RPS()


def show_card_image(suit,
                    value):  # Use cards suit to select array and then value to point at correct image ---> (value - 2)
    if suit == "heart":
        x = value - 2
        Hearts = [Heart_2, Heart_3, Heart_4, Heart_5, Heart_6, Heart_7, Heart_8, Heart_9, Heart_10, Heart_J, Heart_Q,
                  Heart_K, Heart_A]
        return Hearts[x]
    elif suit == "club":
        x = value - 2
        Clubs = [Clubs_2, Clubs_3, Clubs_4, Clubs_5, Clubs_6, Clubs_7, Clubs_8, Clubs_9, Clubs_10, Clubs_J, Clubs_Q,
                 Clubs_K, Clubs_A]
        return Clubs[x]
    elif suit == "spade":
        x = value - 2
        Spades = [Spades_2, Spades_3, Spades_4, Spades_5, Spades_6, Spades_7, Spades_8, Spades_9, Spades_10, Spades_J,
                  Spades_Q, Spades_K, Spades_A]
        y = Spades[x]
        return y
    elif suit == "diamond":
        x = value - 2
        Diamonds = [Diamonds_2, Diamonds_3, Diamonds_4, Diamonds_5, Diamonds_6, Diamonds_7, Diamonds_8, Diamonds_9,
                    Diamonds_10, Diamonds_J, Diamonds_Q, Diamonds_K, Diamonds_A]
        return Diamonds[x]


main_menu()

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














