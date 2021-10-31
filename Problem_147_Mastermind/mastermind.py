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

#Я ХЗ НЕ РАБОТАЕТ ЕСЛИ КТО СМОЖЕТ РЕШИТЬ СООБЩИТЕ (дней убитых на это 2)
#I HZ DOES NOT WORK IF WHO CAN DECIDE TO REPORT (days killed for this 2) 

import random
colors = ['red', 'yellow', 'orange', 'green', 'blue', 'purple', 'black', 'white']
result = 0
def main():
    print("Hello, my name is Botwal, I am a robot and I made 4 colors. Try to guess them in the correct order (they may repeat).")
    color1, color2, color3, color4 = colors_random()
    user_answer1(color1)
    user_answer2(color2)
    user_answer3(color3)
    user_answer4(color4)
    result(color1)
    result(color2) 
    result(color3)
    result(color4)
    print(result)

def colors_random():
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

def user_answer1(color1):
    user_answer1 = input("Color1: ") 
    user_answer1 = user_answer1.lower()
    if user_answer1 == color1:
        print("1 is 4")
        result =+ 1
        return result
    else:
        print("nop")
def user_answer2(color2):
    user_answer2 = input("Color2: ") 
    user_answer2 = user_answer2.lower()
    if user_answer2 == color2:
        print("1 is 4")
        result =+ 1
        return result
    else:
        print("nop")
def user_answer3(color3):
    user_answer3 = input("Color3: ") 
    user_answer3 = user_answer3.lower()
    if user_answer3 == color3:
        print("1 is 4")
        result =+ 1
        return result
    else:
        print("nop")
def user_answer4(color4):
    user_answer4 = input("Color4: ") 
    user_answer4 = user_answer4.lower()
    if user_answer4 == color4:
        print("1 is 4")
        result =+ 1
        return result
    else:
        print("nop")

# def result(result):
#     print(result)
main()
