import  pygame

import time

import calendar

text_list = pygame.font.get_fonts().copy()

text_list.sort()

pygame.init()

# while True:
#
#     event = pygame.event.get()
#
#     print(event)

result_0 = time.clock()

i = 200000

time.sleep(0)

sum = 1

while i > 0 :

    sum *= 2

    i = i - 1

result_1 = time.clock()

result = result_1 - result_0

print(result)