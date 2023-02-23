# в виде строки целиком
# f = open('text.txt', 'r')
# print(f.read())
# print(type(f.read()))
# f.close()

#в виде списка
#  
#по одной строке
#manager contexta
# with open('text.txt') as f:
#     res = f.readline()
#     res2 = f.readline()
#     print(res)
#     print(res2)
#     print(type(res))

#считывание из файла из другой директории
# with open('C:/Users/Asus ONE/Desktop/ДЗ НЕТОЛОГИЯ/NEWDIR/text2.txt', encoding='utf-8') as f:
#     res = f.read()
#     print(res)


# f = open('text3.txt', 'w')
# f.writelines(['Salam\n', "aleykum\n", 'pidor\n', 'gnoyniy'])
# f.close()

# with open('text4.txt', 'x') as f:
#      f.write('POSHEL NAXYU\n')

# f = open('text.txt', 'a+')
# f.read()
# f.write('check')
# f.close
import os
current = os.getcwd()
print(f'directory:    {os.getcwd()}')
foldername = 'textwork'
filename = 'text.txt'
path = os.path.join(current, foldername, filename)
with open(path, 'r') as f:
    print(f.read())