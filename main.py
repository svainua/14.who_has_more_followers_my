# рандомно выбрать из списка пару для сравнения
# сделать выбор и сравнить, у кого больше подписчиков
# если угадал: накопительно считать выигрыши, предоставить на выбор одного из предыдущего списка(который до этого не участвовал) и добавить нового.
# если не угадал, остановить игру, указать кол-во побед
from replit import clear
import random
import art
from game_data import data
game_data = data
should_continue = True

current_score = 0

a = random.choice(data)
b = random.choice(data)

while should_continue:
  print(art.logo)
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']} and has {a['follower_count']} followers")
  print(art.vs)
  print(f"Against B: {b['name']}, a {b['description']}, from {b['country']} and has {b['follower_count']} followers")

  choice = input("Who has more followers? Type 'A' or 'B':")
  if choice == "a" and a["follower_count"] > b["follower_count"]:
    current_score +=1
    clear()
    print(f"You're right! Current score: {current_score}")
    a = b
    b = random.choice(data)
  elif choice == "b" and b["follower_count"] > a["follower_count"]:
    current_score +=1
    clear()
    print(f"You're right! Current score: {current_score}")
    a = b
    b = random.choice(data)
  elif choice == "a" and choice == "b" and a["follower_count"] == b["follower_count"]:
    clear()
    print("you have draw. persons will be updated")
    a = random.choice(data)
    b = random.choice(data)
  else:
    print(f"You lose! Current score: {current_score}")
    should_continue = False


