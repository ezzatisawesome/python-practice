foo = ('Mary had a little lamb whose fleece was white as snow, and everywhere that Mary went, the lamb was sure to go. It followed her to school one day, which was against the rule. It made the children laugh and play to see a lamb at school.')

ans1 = input('Name: ')
ans2 = input('Animal: ')
ans3 = input('Noun: ')
ans4 = input('Color: ')
ans5 = input('Noun: ')
ans6 = input('Noun: ')
ans7 = input('Noun again: ')

print(foo.replace('Mary',ans1).replace('lamb',ans2).replace('fleece',ans3).replace('white',ans4).replace('snow',ans5).replace('school',ans6).replace('children',ans7))

input()


