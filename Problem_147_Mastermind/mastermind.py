"""В этом разделе мы займемся созданием электронной версии настольной игры
«Mastermind» (на отечественном рынке известной как «Властелин разума». — При-
меч. ред.). Компьютер автоматически генерирует комбинацию из четырех цветов из
списка возможных (предусмотрите возможность компьютера многократно выбирать
любой цвет). Например, компьютер может выбрать комбинацию «красный», «синий»,
«красный», «зеленый». Эта последовательность остается скрытой от пользователя.
Пользователь вводит комбинацию из четырех цветов из списка, использованного
компьютером. Например, он может выбрать цвета «розовый», «синий», «желтый»
и «красный».
Программа сообщает, сколько цветов находятся в правильной позиции и сколько
правильно угаданных цветов находятся в неправильных позициях. Так, в приведенном
примере должны выводиться сообщения «Правильный цвет в правильной позиции: 1»
и «Правильный цвет в неправильной позиции: 1».
Пользователь продолжает гадать, пока не введет все четыре цвета в правильном по-
рядке. В конце игры программа выводит соответствующий текст и сообщает, сколько
попыток ему понадобилось."""

import random

def main():
    print("Hello, my name is Botwal, I am a robot and I made 4 colors. Try to guess them in the correct order (they may repeat).")
    color1, color2, color3, color4 = colors_random()
    result = 0
    start = True
    while start == True:
        result = user_answer(color1, color2, color3, color4)
        if result == 4:
            start = False
    print("Win!")
    print(f"You took {result} guesses")

def colors_random():
    colors = ['red', 'yellow', 'orange', 'green', 'blue', 'purple', 'black', 'white']
    color1 = random.choice(colors)
    color2 = random.choice(colors)
    color3 = random.choice(colors)
    color4 = random.choice(colors)
    data_colors = (color1, color2, color3, color4)
    print(data_colors)
    return data_colors
    # num_select = 1 #трудно отследить (непонятно как привязаться)
    # colors_random = random.sample(colors, num_select) # помещает рандомновыбранные значения в список ['', '', ...]
    # print(colors_random)
    # for i in range(0, 3): #не подходит так как разбивает по строкам и невозможно отследить рандомные значения
    #     colors_random = random.choice(colors)
    #     print(colors_random)

def user_answer(color1, color2, color3, color4):
    start = True
    while start == True:
        user_answer1 = input("Enter color1: ")
        user_answer1.lower()
        if user_answer1 != "red" and user_answer1 != "yellow" and user_answer1 != "orange" and user_answer1 != "green" \
            and user_answer1 != "blue" and user_answer1 != "purple" and user_answer1 != "black" and user_answer1 != "white":
            print("Incorrtct selection")
        else:
            start = False
    start = True
    while start == True:
        user_answer2 = input("Enter color2: ")
        user_answer2.lower()
        if user_answer2 != "red" and user_answer2 != "yellow" and user_answer2 != "orange" and user_answer2 != "green" \
            and user_answer2 != "blue" and user_answer2 != "purple" and user_answer2 != "black" and user_answer2 != "white":
            print("Incorrtct selection")
        else:
            start = False
    start = True
    while start == True:
        user_answer3 = input("Enter color3: ")
        user_answer3.lower()
        if user_answer3 != "red" and user_answer3 != "yellow" and user_answer3 != "orange" and user_answer3 != "green" \
            and user_answer3 != "blue" and user_answer3 != "purple" and user_answer3 != "black" and user_answer3 != "white":
            print("Incorrtct selection")
        else:
            start = False
    start = True
    while start == True:
        user_answer4 = input("Enter color4: ")
        user_answer4.lower()
        if user_answer4 != "red" and user_answer4 != "yellow" and user_answer4 != "orange" and user_answer4 != "green" \
            and user_answer4 != "blue" and user_answer4 != "purple" and user_answer4 != "black" and user_answer4 != "white" :
            print("Incorrtct selection")
        else:
            start = False
    result = 0
    place = 0
    if  color1 == user_answer1:
        result =result+1 
    elif color1 == user_answer2 or color1 == user_answer3 or color1 == user_answer3:
        place = place+1
    if  color2 == user_answer2:
        result = result+1 
    elif color2 == user_answer1 or color2 == user_answer3 or color2 == user_answer4:
        place = place+1
    if  color3 == user_answer3:
        result = result+1 
    elif color3 == user_answer1 or color3 == user_answer2 or color3 == user_answer4:
        place = place+1
    if  color4 == user_answer4:
        result = result+1 
    elif color4 == user_answer1 or color4 == user_answer2 or color4 == user_answer3:
        place = place+1
    print(f"Correct color in the correct place - {result}")
    print(f"Correct color in the wrong place - {place}")
    print()
    # data = [result, place]
    return result

main()

#FIRST TRY DONT WORK............................................................................................
# def user_answer2(color2):
#     user_answer2 = input("Color2: ") 
#     user_answer2 = user_answer2.lower()
#     if user_answer2 == color2:
#         print("1 is 4")
#         result =+ 1
#         return result
#     else:
#         print("nop")
# def user_answer3(color3):
#     user_answer3 = input("Color3: ") 
#     user_answer3 = user_answer3.lower()
#     if user_answer3 == color3:
#         print("1 is 4")
#         result =+ 1
#         return result
#     else:
#         print("nop")
# def user_answer4(color4):
#     user_answer4 = input("Color4: ") 
#     user_answer4 = user_answer4.lower()
#     if user_answer4 == color4:
#         print("1 is 4")
#         result =+ 1
#         return result
#     else:
#         print("nop")

# def result(result):
#     print(result)