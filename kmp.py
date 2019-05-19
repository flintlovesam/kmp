

def getPartialTable(pattern):
    if not pattern:
        return None
    lp = len(pattern)
    res = [-1, 0]
    if lp > 1:
        for curr in xrange(1, lp):
            ptr = curr
            while ptr > 0 and pattern[curr] != pattern[res[ptr]]:
                ptr = res[ptr]
            else:
                res.append(res[ptr] + 1)
    return res

def matchPatternKMP(string, pattern):
    if not string or not pattern:
        return None
    p_table = getPartialTable(pattern)
    start, matched = 0, 0
    ls, lp  = len(string), len(pattern)
    stop    = ls - lp + 1
    res     = list()
    while True:
        while matched == lp or string[start + matched] != pattern[matched]:
            if matched == lp:
                res.append(start)
            start   += matched - p_table[matched]
            matched  = max(0, p_table[matched])
            if not start < stop:
                return res
        else:
            matched += 1

if __name__ == '__main__':
    string  = 'abababaababacbababacb'
    pattern = 'aba'
    print 'string:\t\t%s\npattern:\t%s' % (string, pattern)
    print matchPatternKMP(string, pattern)