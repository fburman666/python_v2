goals_tottenham = int(input("Hur många mål gjorde Tottenhamn? "))
goals_Liverpool = int(input("Hur många mål gjorde Liverpool? "))
goal_difference = abs(goals_tottenham - goals_Liverpool)

if goals_Liverpool > goals_tottenham:
    print("Liverpool vann med", goal_difference, "mål")
elif goals_Liverpool < goals_tottenham:
    print("Tottenham vann med", goal_difference, "mål")
elif goals_Liverpool == goals_tottenham:
    print("Det blev oavgjort!")
else:
    print("Nånting gick fel!")
