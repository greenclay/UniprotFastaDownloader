__author__ = 'Yuki'

nameFile = open('yeast2.names.txt', 'r')
fastaFile = open('yeast2-curated.fasta', 'r')
resultFile = open('yeast-results.txt', 'w')

# nameFile = open('human1.names.txt', 'r')
# fastaFile = open('human1-curated.fasta', 'r')
# resultFile = open('human-results.txt', 'w')


name = nameFile.read().splitlines()
fasta = fastaFile.read().splitlines()

for geneName in name:
    found = False
    geneNameToFind = 'GN=' + geneName + ' '
    for line in fasta:
        if geneNameToFind in line:
            found = True
            print('found gene name: ' + geneName)
    if found == False:
        resultFile.write(geneName + '\n')
