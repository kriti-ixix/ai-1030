p1_score = 0
p2_score = 0

while True:
    if(p1_score == 2 or p2_score == 2):
        break

    p1 = input("Player 1 enter your choice: ").lower()
    p2 = input("Player 2 enter your choice: ").lower()
    
    p1_conditions = [p1 == 'rock' and p2 == 'scissor',
                     p1 == 'paper' and p2 == 'rock',
                     p1 == 'scissor' and p2 == 'paper']

    p2_conditions = [p2 == 'rock' and p1 == 'scissor',
                     p2 == 'paper' and p1 == 'rock',
                     p2 == 'scissor' and p1 == 'paper']

    if (p1 == p2):
        print("Tie")
    elif any(p1_conditions):
        print("Player 1 wins this round")
        p1_score += 1
    elif any(p2_conditions):
        print("Player 2 wins this round")
        p2_score += 1
    else:
        print("Error")

if(p1_score > p2_score):
    print("Player 1 wins the match")
elif(p2_score > p1_score):
    print("Player 2 wins the match")
