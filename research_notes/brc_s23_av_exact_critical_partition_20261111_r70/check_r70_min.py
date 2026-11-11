#!/usr/bin/env python3
"""R70 minimal exact finite-event checker; auxiliary circle model only."""
from fractions import Fraction as Q

def valid(a,b,L,U):
    return all((s*L).numerator//(s*L).denominator ==
               (s*U).numerator//(s*U).denominator for s in (a,b)) and all(
               (a*th)%1 < (b*th)%1 for th in (L,U))

def member(t,a,b,th):
    return (a*th)%1 <= (t*th)%1 < (b*th)%1

def old(t,a,b,L,U):
    if not valid(a,b,L,U) or (t*L)//1 != (t*U)//1: return '?'
    v=[((t*x)%1,(a*x)%1,(b*x)%1) for x in (L,U)]
    if all(ra<=rt<rb for rt,ra,rb in v): return 'I'
    if all(rt<ra for rt,ra,rb in v) or all(rt>=rb for rt,ra,rb in v):return 'O'
    return '?'

def complete(t,a,b,L,U,windings=12):
    if not valid(a,b,L,U):return '?'
    k0,k1=int((t*L)//1),int((t*U)//1)
    if k1-k0>windings:return '?'
    ka,kb=int((a*L)//1),int((b*L)//1)
    cuts={L,U}
    for k in range(k0-1,k1+2):
        for den,num in ((t,k),(t-a,k-ka),(t-b,k-kb)):
            if den:
                x=Q(num,den)
                if L<x<U:cuts.add(x)
    cs=sorted(cuts)
    values=set()
    for i,p in enumerate(cs):
        values.add(member(t,a,b,p))
        if i+1<len(cs):values.add(member(t,a,b,(p+cs[i+1])/2))
    return 'I' if values=={True} else 'O' if values=={False} else '?'

def main():
    a,b,t=1,2,4;L=Q(249,1000);U=Q(251,1000)
    assert old(t,a,b,L,U)=='?' and complete(t,a,b,L,U)=='O'
    assert complete(1,a,b,L,U)=='I' and complete(2,a,b,L,U)=='O'
    assert complete(6,1,2,Q(199,1000),Q(201,1000))=='?'
    tested=recovered=transition=0
    for t in range(61):
        for L,U in ((Q(249,1000),Q(251,1000)),(Q(199,1000),Q(201,1000)),
                    (Q(3,10),Q(31,100)),(Q(33,100),Q(34,100))):
            for a,b in ((1,2),(0,1),(2,3)):
                if not valid(a,b,L,U):continue
                result=complete(t,a,b,L,U,windings=200)
                probes={member(t,a,b,L+(U-L)*Q(k,100)) for k in range(101)}
                if result!='?':assert probes==({'I':{True},'O':{False}}[result])
                if result=='?' and len(probes)>1:transition+=1
                recovered+=int(old(t,a,b,L,U)=='?' and result!='?')
                tested+=1
    assert (tested,recovered,transition)==(671,86,315)
    print('R70_MIN_PASS',tested,recovered,transition)

if __name__=='__main__':main()
