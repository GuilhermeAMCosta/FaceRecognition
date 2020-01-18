file = open("Experiment.csv", "r")

file1 = open('entrada.txt', 'r+')
file2 = open('entrada2.txt', 'r+')

multiplas = []
singulares = []

for l1 in file1:
    n1 = l1.replace('\n', '')
    multiplas.append(n1)

for l2 in file2:
    n2 = l2.replace('\n', '')
    singulares.append(n2)

#print(multiplas)
#print(singulares)
'''
for i in multiplas:
    for l in singulares:
        for line in file:
            print(line)
'''
palavra = file.readlines()
print(palavra[3])