import math
levels = [1, 2, 3, 4, 5]
coins = [5, 8, 3, 10, 7]
enemies = [2, 4, 1, 5, 3]
power_ups = ["Mushroom", "Star", "Flower", "Mushroom", "Star"]

#platform adventure
for i in range(len(levels)):
    print(f"Level {levels[i]}")
    print(f"Coins: {coins[i]}")
    print(f"Enemies: {enemies[i]}")
    print(f"Power-ups: {power_ups[i]}")
    print("------------------------")

#player information
player_name = "Hero"
lives = 3
score = 0
total_coins = 0
print(f"Player name: {player_name}")
print(f"Lives: {lives}")
print(f"Score: {score}")
print(f"Total coins: {total_coins}")
print("------------------------")
#level scores
coin_points = 10
enemy_points = -5
star_points = +25

level_scores = []
for i in range(len(levels)):
        level_points = (coin_points * coins[i] + enemy_points * enemies[i])
        if power_ups[i] == "Star":
            level_points += star_points
        level_scores.append(level_points)

        print(f"Level {levels[i]} score: {level_points}")
print("------------------------")
#adventure actions
actions = [0, 1, 0, 2, 1]
action_results = []
for i in range(len(levels)):
    if actions[i] == 0:
        action_results.append("collect coins")
    elif actions[i] == 1:
        action_results.append("fight enemies")
    elif actions[i] == 2:
        action_results.append("use power-ups")
    print(f"Level {levels[i]}: {action_results[i]}")
print("------------------------")
#life history
life_history = []
for i in range(len(levels)):
    if enemies[i] >= 4 and power_ups[i] != "Star":
        lives -= 1
    life_history.append(lives)
    print(f"After Level {levels[i]}: {life_history[i]} Lives")
print("------------------------")
#coin collection
bonus_coin_levels = [coin for coin in coins if coin >= 7]
total_coins = sum(coins)
print(f"Coins collected:{total_coins}")
print(f"Levels with 7 or more coins:{bonus_coin_levels}")
print("------------------------")
#power-up inventory
inventory=["Mushroom", "Star", "Flower"]
used_powerups = ["Mushroom", "Star"]
print(f"Starting inventory:{inventory}")
for used_powerup in used_powerups:
    inventory.pop(inventory.index(used_powerup))
print("Used power-ups",used_powerups)
print("remaining inventory", inventory )
print("------------------------")
#Level analysis
print("Total Coins:",sum(coins))
print("Most coins in one level:",max(coins))
print("Fewest coins in one level:", min(coins))
print("average coins per level", sum(coins)/levels[-1])
print("total enemies:", sum(enemies))
print("most enemies in one level:", max(enemies))
print("------------------------")
#high score
scores = [score for score in level_scores if score >= 50]
print("Scores of 50 or higher:", scores)
print("------------------------")
#score history
score_history = []
for i in range(len(level_scores)):
    score_history.append(sum(score_history)+level_scores[i])
    print(f"After level {i+1}: {score_history[i]}")
print("first 2 scores", score_history[:2])
print("last 2 scores", score_history[-2:])
print("------------------------")
#Final status
if lives == 0:
    print("Game over")
elif sum(level_scores) >= 250:
    print("Adventure Champion")
elif sum(level_scores) >=150:
    print("Great adventure")
else:
    print("Keep practicing")
print("------------------------")
print("final score:", sum(level_scores))
print("final lives:", lives)
print("rank: Legend")