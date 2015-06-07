__author__ = 'Yuki'

# Read the gene names from yeast2.names.txt line by line and append _YEAST to the end
# fileToRead = open('yeast-results.txt', 'r')
# fileToWrite = open('yeast-unreviewednames.txt','w')
def make_query_string():
    fileToRead = open('human-results.txt', 'r')
    fileToWrite = open('human1-unreviwednames.txt','w')

    temp = fileToRead.read().splitlines()

    write = 1
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

    if write == 1:
        fileToWrite.write('\'query\': \'reviewed:no and organism:"baker\\\'s yeast" and (' + wholeline + ')\'')
    else:
        fileToWrite.write('\'query\': \'reviewed:no and organism:"Homo sapiens (Human) [9606]" and (' + wholeline + ')\'')

# fileToRead = open('human1.names.txt', 'r')
# fileToWrite = open('human1_HUMAN.names.txt','w')
# temp = fileToRead.read().splitlines()
#
# for line in temp:
#     newline = line + '_HUMAN'
#     print(newline)
#     fileToWrite.write(newline + '\n')