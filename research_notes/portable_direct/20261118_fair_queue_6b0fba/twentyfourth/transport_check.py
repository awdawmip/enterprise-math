"""Exact Shannon calculations and a bounded-step Gaussian walk realizing equality."""
from collections import Counter
from fractions import Fraction
from math import isqrt
import json


def log_integer(n):
    out = Counter()
    d = 2
    while d*d <= n:
        while n%d == 0:
            out[d] += 1
            n //= d
        d += 1
    if n > 1:
        out[n] += 1
    return out


def combine(*terms):
    result = Counter()
    for scalar, vec in terms:
        for p,x in vec.items():
            result[p] += scalar*x
    return {p:v for p,v in result.items() if v}


def entropy(rows, names):
    counts = Counter()
    for row, weight in rows:
        counts[tuple(row[name] for name in names)] += weight
    n = sum(counts.values())
    return combine((1,log_integer(n)), *((-Fraction(c,n),log_integer(c)) for c in counts.values()))


def conditional(rows, a, given):
    return combine((1,entropy(rows,a+given)),(-1,entropy(rows,given)))


def mi(rows, a, b, given=()):
    return combine((1,conditional(rows,a,given)),(-1,conditional(rows,a,given+b)))


def ledger(rows):
    s,o,x,op,xp,w=((v,) for v in ('s','o','x','op','xp','word'))
    prior = mi(rows,x,s+w,o)
    terminal = mi(rows,xp,w,op)
    loss = combine((1,prior),(-1,terminal))
    hs = entropy(rows,s)
    items = [mi(rows,s,o),conditional(rows,s,x+o),mi(rows,s,w+op),
             conditional(rows,s,xp+w+op),mi(rows,s,xp,op)]
    assert combine((1,loss),(-2,hs),*((1,t) for t in items)) == {}
    return hs,prior,terminal,loss,items


def prime_for(m, length):
    p=m*m+1+2*length+1
    while p%4!=1 or any(p%d==0 for d in range(2,isqrt(p)+1)):
        p+=1
    return p


def marked_walk(m,p=None):
    length=(m-1).bit_length()
    p=p or prime_for(m,length)
    base=m+1
    assert p%4==1 and p>m*m+1+2*length
    path=[base]
    marks=[]
    for v in range(m):
        for s in range(m):
            anchor=p*(m*v+s)+base+m*v-s
            while path[-1]<anchor:
                step=2 if (path[-1]+1)%p==0 else 1
                path.append(path[-1]+step)
            assert path[-1]==anchor
            time=len(path)-1
            for _ in range(s):
                path.append(path[-1]+1)
            terminal=len(path)-1
            digit=(v+s)%m
            for bit in range(length-1,-1,-1):
                path.append(path[-1]+1+((digit>>bit)&1))
            marks.append((v,s,time,terminal))
    # The same skip rule supplies the infinite tail. Test three complete periods.
    limit=path[-1]+3*p
    while path[-1]<limit:
        path.append(path[-1]+(2 if (path[-1]+1)%p==0 else 1))
    assert all(x%p for x in path) and all(y-x in (1,2) for x,y in zip(path,path[1:]))
    observations=[]
    for v,s,t,u in marks:
        read=tuple(path[j+1]-path[j] for j in range(u,u+length))
        assert path[u]-path[t]==s and path[u]%p==base+m*v
        assert sum((z-1)<<i for i,z in enumerate(reversed(read)))==(v+s)%m
        observations.append(dict(v=v,s=s,o=0,x=path[t]%p,op=0,xp=path[u]%p,word=read))
    return p,len(path),observations


def serial(vec):
    return {str(p):str(v) for p,v in sorted(vec.items())}


def case(m,p=None):
    p,walk_length,values=marked_walk(m,p)
    results=[]
    for probs in ([1]*m,list(range(1,m+1))):
        rows=[(v,probs[v['s']]) for v in values]
        hs,prior,terminal,loss,items=ledger(rows)
        assert items==[{}]*5 and loss==combine((2,hs))
        results.append(dict(weights=probs,H_s=serial(hs),checkpoint_information=serial(prior),
                            terminal_information=serial(terminal),loss=serial(loss)))
    result=dict(m=m,p=p,word_length=(m-1).bit_length(),verified_path_positions=walk_length,
                marks=len(values),information_examples=results)
    if m==2:
        result['four_marks']=values
    return result


def unit_step_case():
    path = [(9,0)]
    observations = []
    def step(dx,dy):
        x,y = path[-1]
        path.append((x+dx,y+dy))
    def connect(target):
        while path[-1][0] < target:
            x,y = path[-1]
            assert y == 0
            if (x+1)%13:
                step(1,0)
            else:
                for dx,dy in ((0,1),(1,0),(1,0),(0,-1)):
                    step(dx,dy)
        assert path[-1] == (target,0)
    for v in range(2):
        for s in range(2):
            anchor = 9 + 2*v - s + 13*(2*v+s)
            connect(anchor)
            connect(anchor+s)
            terminal = len(path)-1
            if (v+s)%2:
                step(0,1)
                for _ in range(3 if anchor+s==37 else 1):
                    step(1,0)
                step(0,-1)
            else:
                step(1,0)
            dx = path[terminal+1][0] - path[terminal][0]
            dy = path[terminal+1][1] - path[terminal][1]
            assert (dx,dy) == ((0,1) if (v+s)%2 else (1,0))
            observations.append(dict(s=s,x=anchor%13,xp=(anchor+s)%13,o=0,op=0,word=(dx,dy)))
    connect(1309)
    assert len(set(path)) == len(path)
    assert all(abs(x-u)+abs(y-v)==1 for (x,y),(u,v) in zip(path,path[1:]))
    assert all((x+5*y)%13 and (x-5*y)%13 for x,y in path)
    hs,prior,terminal,loss,items = ledger([(row,1) for row in observations])
    assert items == [{}]*5 and loss == combine((2,hs)) == {2:2}
    return dict(p=13,maximum_step=1,verified_positions=len(path),marks=observations,
                checkpoint_information=serial(prior),terminal_information=serial(terminal),
                shift_entropy=serial(hs),loss=serial(loss))


def smoothed_case():
    path = [3]
    while len(path) < 40:
        path.append(path[-1] + (2 if (path[-1]+1)%13 == 0 else 1))
    rows = []
    span = 4
    for a in [0, 4, 11]:
        for lag in [0, 3]:
            b = a + lag
            for j in range(span):
                end = b+j
                rows.append((dict(a=a,b=b,end=end,s=path[end]-path[a],o=0,
                                  x=path[a]%13,op=0,xp=path[end]%13,
                                  word=path[end+1]-path[end]),1))
    hs,prior,terminal,loss,items = ledger(rows)
    extra_time = mi(rows,('end',),('b',),('a',))
    extra_start = mi(rows,('s',),('a',),('x','o'))
    assert conditional(rows,('s',),('a','b')) == log_integer(span)
    assert items[1] == combine((1,log_integer(span)),(1,extra_time),(1,extra_start))
    return dict(span=span,loss=serial(loss),shift_entropy=serial(hs),
                exact_checkpoint_uncertainty=serial(items[1]),
                preoffset_time_information=serial(extra_time),start_information=serial(extra_start))


def main():
    # A separate nonsaturating law with both old and new smaller-batch residues.
    nonsaturating=[]
    for x in range(3):
        for s in range(3):
            for o in range(4):
                row=dict(x=x,xp=(x+s)%3,s=s,o=o,op=(o+s)%4,word=(x*s+o)%5)
                nonsaturating.append((row,1+(x+2*s+3*o)%4))
    left=ledger(nonsaturating)
    assert any(left[-1])
    print(json.dumps(dict(unit='bits; a map p:r represents the exact sum of r*log2(p)',
        equality_cases=[case(2,13),case(3),case(5),case(8)],
        unit_step_binary=unit_step_case(), independent_uniform_offset=smoothed_case(),
        nonsaturating_ledger_residual_terms=[serial(x) for x in left[-1]]),indent=2))


if __name__=='__main__':
    main()
