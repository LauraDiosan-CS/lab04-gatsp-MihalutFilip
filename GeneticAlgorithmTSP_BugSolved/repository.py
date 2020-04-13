import math

class Repository:
    def readNet(self, fileName):
        f = open(fileName, "r")
        net = {}
        n = int(f.readline())
        net['noNodes'] = n
        mat = []
        for i in range(n):
            mat.append([])
            line = f.readline()
            elems = line.split(",")
            for j in range(n):
                mat[-1].append(int(elems[j]))
        net["mat"] = mat
        degrees = []
        noEdges = 0
        for i in range(n):
            d = 0
            for j in range(n):
                if (mat[i][j] == 1):
                    d += 1
                if (j > i):
                    noEdges += mat[i][j]
            degrees.append(d)
        net["noEdges"] = noEdges
        net["degrees"] = degrees
        f.close()
        return n, net

    def readHardTest(self, fileName):
        f = open(fileName, "r")
        net = {}
        f.readline()
        f.readline()
        f.readline()
        n = int(f.readline().split(' : ')[1])
        net['noNodes'] = n

        f.readline()
        f.readline()
        lineEdge = f.readline()
        list = []

        while(lineEdge != "EOF"):
            fields = lineEdge.split(' ')
            city = int(fields[0]) - 1
            x = int(fields[1]) - 1
            y = int(fields[2])
            list.append([city, x, y])
            lineEdge = f.readline()

        mat = []

        for i in range(n):
            array = []
            for j in range(n):
                first = list[i]
                second = list[j]
                cost = round(math.sqrt((first[1] - second[1])*(first[1] - second[1]) + (first[2] - second[2])*(first[2] - second[2])))
                array.append(cost)
            mat.append(array)

        net["mat"] = mat
        f.close()
        return n, net