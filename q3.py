def WPGMA():
    with open('matrix1.txt', 'r') as file:
        m = [[num.replace('\n', '') for num in line.split(' ')]
             for line in file]
        m.pop(0)
        for i in range(len(m)):
            m[i].pop(0)
        

WPGMA()
