import random

def choose_options():
  human_options = (input("Choose rock, paper or scissors: "))
  human_options = human_options.lower()
  compu_options = ("rock", "paper", "scissors")

  if not human_options in compu_options:
    print("ingreso erroneo intente de nuevo!")

  compu_options = random.choice(compu_options)
  return human_options, compu_options

def game_rules(human_options,compu_options,score_human,score_compu, lives):
  if compu_options == human_options:
    print(
        f"tie, human = {human_options}and compu = {compu_options}, nothing change"
    )
  elif human_options == "rock":
    if compu_options == "scissors":
      score_human += 10

      print(
          f"human wings, human chose :{human_options} and the compu chose :{compu_options} \n the new score are: \n Human score: {score_human}\n Compu score:{score_compu} \n lives remaining: {lives}"
      )
    else:
      score_compu += 10
      lives -= 1
      print(
          f"human lost, human chose :{human_options} and the compu chose :{compu_options} \n the new score are: \n Human score: {score_human}\n Compu score:{score_compu} \n lives remaining: {lives}"
      )

  elif human_options == "paper":
    if compu_options == "rock":
      score_human += 10
      print(
          f"human wings, human chose :{human_options} and the compu chose :{compu_options} \n the new score are: \n Human score: {score_human}\n Compu score:{score_compu} \n lives remaining: {lives}"
      )
    else:
      score_compu += 10
      lives -= 1
      print(
          f"human lost, human chose :{human_options} and the compu chose :{compu_options} \n the new score are: \n Human score: {score_human}\n Compu score:{score_compu} \n lives remaining: {lives}"
      )

  elif human_options == "scissors":
    if compu_options == "paper":
      score_human += 10
      print(
          f"human wings, human chose :{human_options} and the compu chose :{compu_options} \n the new score are: \n Human score: {score_human}\n Compu score:{score_compu} \n lives remaining: {lives}"
      )
    else:
      score_compu += 10
      lives -= 1
      print(
          f"human lost, human chose :{human_options} and the compu chose :{compu_options} \n the new score are: \n Human score: {score_human}\n Compu score: {score_compu} \n lives remaining: {lives}"
      )
  return score_human,score_compu,lives
########################
def run_game():
  lives = 3
  score_compu = 0
  score_human = 0
  while lives > 0:
    human_options, compu_options = choose_options()
    score_human, score_compu,lives = game_rules(human_options, compu_options, score_human, score_compu, lives)
    if score_compu == 30 or score_human == 30:
      print("Game Over")
run_game()