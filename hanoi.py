def hanoi(n,from_,to,via):
    if type(n)=='int':
        if n==1:
            print "%s=>%s" % (from_,to)
        else:
            hanoi(n-1,from_,via,to)
            print "%s=>%s" % (from_,to)
            hanoi(n-1,via,to,from_)
    else:
        print 'invalid type of parameter n,only int'
