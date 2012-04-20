# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

#High Card: Highest value card.
#One Pair: Two cards of the same value.
#Two Pairs: Two different pairs.
#Three of a Kind: Three cards of the same value.
#Straight: All cards are consecutive values.
#Flush: All cards of the same suit.
#Full House: Three of a kind and a pair.
#Four of a Kind: Four cards of the same value.
#Straight Flush: All cards are consecutive values of same suit.
#Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#The cards are valued in the order:
#2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

#If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

#Consider the following five hands dealt to two players:

#The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

# How many hands does Player 1 win?

# Take the input line by line, split into two hands (5, 5)

# f = open(poker.txt, "r")
# hands = f.readline()

hands = "8C TS KC 9H 4S 7D 2S 5D 3S AC"

# Split the string into 2 arrays of 5, 2 char strings, hand1 and hand2

hand1 = []
hand2 = []

hands = "8C TS KC 9H 4S 7D 2S 5D 3S AC"
hand_working = hands.split()

for i in range(0, 10, 1):
	
	if i <= 5:
		hand1[i] = hand_working[i]	
		print hand1
	else:
		hand2[i-5] = hand_working[i]
		print hand2
		
# For the two hands, identify if a hand is a:
	# 1. Royal Flush
	# 2. Straight Flush
	# 3. Four of a Kind
	# 4. Full House
	# 5. Flush
	# 6. Straight
	# 7. Three of a Kind							
	# 8. Two Pairs		
	# 9. One pair	
	# 10. Failing else
										
# Identify if both hands are the same rank.
	# Then identify highest card
	
# Identify the winner, add one to their total.
										
# Answer = player 1 total 