try:
    import os, platform, time
except Exception as error:
    print("[ERROR] -> %s"%error)
else:
    def displayMagicSquareDirichlet(table):
        try:
           for y in range(len(table)):
               for x in range(len(table)):
                    table[y][x] = float(table[y][x])
        except Exception as error:
            return "[ERROR] -> %s"%error
        else:
            size = len(table)
            differenceSize = 0
            for k in range(len(table)):
                if len(table[k]) != size:
                    differenceSize += 1
            
            if differenceSize == 0:
                print("\n")
                line = ""
                for y in range(len(table)):
                    for x in range(len(table)):
                        line += f"{table[y][x]} "
                    print(line)
                    line = ""
    def calculMagicSquareDirichlet(size, top, bottom, right, left):
        try:
            size = int(size)
            for k in range(len(top)):
                if float(top[k]) % 1 == 0:
                    top[k] = int(top[k])
                else:
                    top[k] = float(top[k])
            for k in range(len(bottom)):
                if float(bottom[k]) % 1 == 0:
                    bottom[k] = int(bottom[k])
                else:
                    bottom[k] = float(bottom[k])
            for k in range(len(left)):
                if float(left[k]) % 1 == 0:
                    left[k] = int(left[k])
                else:
                    left[k] = float(left[k])
            for k in range(len(right)):
                if float(right[k]) % 1 == 0:
                    right[k] = int(right[k])
                else:
                    right[k] = float(right[k])
        except Exception as error:
            return "[ERROR] -> %s"%error
        else:
            differenceSize, total = 0, [top, bottom, left, right]
            for k in range(len(total)):
                if size != len(total[k]):
                    diffrenceSize += 1
            if size >= 2 and differenceSize == 0:
                realSize = size+2
                table = []
                for y in range(realSize):
                    table.append([])
                    for x in range(realSize):
                        table[y].append(0)
                for k in range(1, realSize-1):
                    table[0][k] = top[k-1]
                    table[realSize-1][k] = bottom[k-1]
                    table[k][0] = left[k-1]
                    table[k][realSize-1] = right[k-1]
                errors = 1
                average = 0
                while errors > 0:
                    errors = 0
                    for y in range(1, realSize-1):
                        for x in range(1, realSize-1):
                            average = (table[y-1][x]+table[y+1][x]+table[y][x-1]+table[y][x+1])/4
                            table[y][x] = average
                    for y in range(1, realSize-1):
                        for x in range(1, realSize-1):
                            average = (table[y-1][x]+table[y+1][x]+table[y][x-1]+table[y][x+1])/4
                            if average != table[y][x]:
                                errors += 1
            return table


    if __name__ == "__main__":
        table = calculMagicSquareDirichlet(3, [6, 2, 5], [2, 4, 7], [8, 4, 5], [4, 7, 8])
        displayMagicSquareDirichlet(table)



