from info import InfoBot

name = input("Input name : ")
info_bot = InfoBot(name)

print(f"Hey {name}\n"
      f"I think you are {info_bot.get_gender()}\n"
      f"And maybe {info_bot.get_age()} years old.")
