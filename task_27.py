#task_27
'''
По рзелульаттам илссеовадний одонго анлигйсокго унвиертисета, не иеемт занчнеия, в кокам пряокде рсапожолены бкувы в солве. Галвоне, чотбы преавя и пслоендяя бквуы блыи на мсете. Осатьлыне бкувы мгоут селдовтаь в плоонм бсепордяке, все-рвано ткест чтаитсея без побрелм. Пичрионй эгото ялвятеся то, что мы чиатем не кдаужю бкуву по отдльенотси, а все солво цликеом.

Напишите функцию, которая преобразует переданный ей текст способом, похожим на описанный выше. В качестве алгоритма перемешивания букв в слове используйте следующий:

Для каждого слова в тексте:
	1. Фиксируем первый и последний символы слова.
	2. Из оставшихся берём первые три символа, произвольно перемешиваем.
	3. Полученную тройку фиксируем, т.е. она уже не будет участвовать в дальнейшем перемешивании.

'''
import random

def pemrtuate(text):
    words = []
    for word in text.split():
        if len(word) > 3:
            words.append(word[0]
                         + ''.join(random.sample( [char for char in word[1:-1]], len(word) - 2))
                         + word[-1])
        else:
            words.append(word)
    return ' '.join(words)


print (pemrtuate("Master of Puppets"))