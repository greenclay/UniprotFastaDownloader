__author__ = 'Yuki'

# Read the gene names from yeast2.names.txt line by line and append _YEAST to the end
fileToRead = open('yeast2.names.txt', 'r')
fileToWrite = open('yeast2_YEAST.names.txt','w')
temp = fileToRead.read().splitlines()

i = 0
stop = 1000
wholeline = ''
for line in temp:
    wholeline = wholeline + 'gene_exact:' + line + ' or '
    # print(wholeline)

    i = i + 1
    if i > stop:
        break

    # fileToWrite.write(newline + '\n')
print i
fileToWrite.write('\'query\':\'organism:"baker\\\'s yeast" and (' + wholeline + ')\'')
# fileToRead = open('human1.names.txt', 'r')
# fileToWrite = open('human1_HUMAN.names.txt','w')
# temp = fileToRead.read().splitlines()
#
# for line in temp:
#     newline = line + '_HUMAN'
#     print(newline)
#     fileToWrite.write(newline + '\n')