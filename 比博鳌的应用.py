def line_conf(a,b):
    def line(x):
        return a*x +b
    return  line

line1 = line_conf(1,1)

print(line_conf(1,2)(5))