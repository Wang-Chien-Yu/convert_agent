def read(filename):
    list = []
    with open(filename, 'r') as f:
        for i in f:
            list.append(i.strip().split())
        return list


def write(filname, list):
    with open(filname, 'w') as f:
        for i in list:
            f.write('v09' + ',' + i[0] + ',' + i[1] + '\n')


def main():
    line = read('123.txt')
    write('printout.txt', line)

main()
