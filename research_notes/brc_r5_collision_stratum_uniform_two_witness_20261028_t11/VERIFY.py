"""Exact rational support-envelope and collision certificate: external P/Q tree."""
from fractions import Fraction as F
from itertools import product

LEAVES=(('A','C','low',F(1,24),F(1,12)),
        ('A','C','high',F(1,8),F(1,12)),
        ('A','L','side',F(1,12),F(1,3)),
        ('B','C','low',F(1,32),F(1,8)),
        ('B','C','high',F(7,32),F(1,8)),
        ('B','H','side',F(1,2),F(1,4)))
L0=(912,456,128,-194)
L1=(400,600,-88,34)
ROOTS=('A','B')
TERMS=('A_low','A_high','B_low','B_high')
ACT=('P','Q','cont')
STOP=('P','Q')
LO,HI=-F(1,12),F(1,12)

def leaves(e):
    return [(g,n,z,p,q+(e if i==0 else -e if i==1 else 0))
            for i,(g,n,z,p,q) in enumerate(LEAVES)]

def model_check(e):
    assert LO<e<HI
    rows=leaves(e)
    assert all(p>0 and q>0 for _,_,_,p,q in rows)
    assert sum(p for *_,p,q in rows)==sum(q for *_,p,q in rows)==1
    def pq(g,n):
        return tuple(sum(t[i] for t in rows if t[0]==g and t[1]==n) for i in (3,4))
    assert pq('A','C')==(F(1,6),F(1,6))
    assert pq('B','C')==(F(1,4),F(1,4))
    assert pq('A','L')==(F(1,12),F(1,3))
    assert pq('B','H')==(F(1,2),F(1,4))

def policies():
    for t1 in product(ACT,repeat=2):
        for side in product(STOP,repeat=2):
            for t3 in product(STOP,repeat=4):
                for c in product(ACT,repeat=2):
                    yield t1,c,side,t3

def observation(pol,e):
    t1,ac,side,t3=pol
    out=[F(0)]*4
    for g,n,z,p,q in leaves(e):
        i=ROOTS.index(g)
        if t1[i]!='cont':
            t,d=1,t1[i]
        elif n!='C':
            t,d=2,side[i]
        elif ac[i]!='cont':
            t,d=2,ac[i]
        else:
            t,d=3,t3[TERMS.index(g+'_'+z)]
        if d=='Q':out[0]+=p
        else:out[1]+=q
        out[2]+=p*t
        out[3]+=q*t
    return tuple(out)

def value(v,lam):
    return sum(x*y for x,y in zip(v,lam))

def line(pol,lam):
    a=value(observation(pol,F(0)),lam)
    b=(value(observation(pol,F(1,48)),lam)-a)*48
    return a,b

def at(ell,e):
    return ell[0]+ell[1]*e

def distinct_lines(lam):
    full=set()
    lr=set()
    nf=nl=0
    for pol in policies():
        nf+=1
        ell=line(pol,lam)
        full.add(ell)
        if pol[1][0]==pol[1][1]:
            nl+=1
            lr.add(ell)
    assert (nf,nl)==(5184,1728)
    return full,lr

def envelope(lines,cands):
    assert all(c in lines for c in cands)
    knots={LO,HI}
    for i,(a,b) in enumerate(cands):
        for c,d in cands[i+1:]:
            if b!=d:
                x=(c-a)/(b-d)
                if LO<x<HI:knots.add(x)
    for e in sorted(knots):
        top=max(at(c,e) for c in cands)
        assert all(at(ell,e)<=top for ell in lines),e
    return tuple(sorted(knots))

def actual_lr(pol,e):
    if pol[1][0]!=pol[1][1]:return False
    rr=[p/q for g,n,z,p,q in leaves(e) if n=='C']
    return all(pol[3][i]==pol[3][j] for i in range(4)
               for j in range(i+1,4) if rr[i]==rr[j])

def expected(lam,kind,e):
    if lam==L0:
        return max(F(868),F(857)+456*e) if kind=='full' else max(F(857),F(857)+456*e)
    if lam==L1:
        if kind=='full':
            return max(F(1499,3)-600*e,F(547),F(533)+600*e)
        return max(F(1496,3)-600*e,F(547),F(532)+600*e)
    raise ValueError(lam)

def collisions(e):
    rr=[p/q for g,n,z,p,q in leaves(e) if n=='C']
    return [(TERMS[i],TERMS[j]) for i in range(4)
            for j in range(i+1,4) if rr[i]==rr[j]]

def check_at(e):
    model_check(e)
    full={L0:None,L1:None}
    lr={L0:None,L1:None}
    n=0
    for pol in policies():
        o=observation(pol,e)
        inside=actual_lr(pol,e)
        if inside:n+=1
        for lam in (L0,L1):
            v=value(o,lam)
            if full[lam] is None or v>full[lam]:full[lam]=v
            if inside and (lr[lam] is None or v>lr[lam]):lr[lam]=v
    for lam in (L0,L1):
        assert full[lam]==expected(lam,'full',e)
        assert lr[lam]==expected(lam,'LR',e)
    print('EXACT CHECK eps=',e,'terminal_collisions=',collisions(e),
          'lr_descriptions=',n,'gaps=',full[L0]-lr[L0],full[L1]-lr[L1])

def main():
    for lam,fc,lc,counts in (
      (L0,((F(868),F(0)),(F(857),F(456))),
          ((F(857),F(0)),(F(857),F(456))),(137,85)),
      (L1,((F(1499,3),F(-600)),(F(547),F(0)),(F(533),F(600))),
          ((F(1496,3),F(-600)),(F(547),F(0)),(F(532),F(600))),(140,88)),
    ):
        f,r=distinct_lines(lam)
        assert (len(f),len(r))==counts
        print('DIRECTION',lam,'SCORE LINES',len(f),len(r))
        print('  FULL ENVELOPE KNOTS',envelope(f,fc))
        print('  RELAXED LR ENVELOPE KNOTS',envelope(r,lc))
    # Terminal Bayes declaration is a function only of p/q for both directions.
    for e in (F(-5,84),F(-1,24),F(0),F(1,84),F(7,300),
              F(11,456),F(25,1056),F(1,40),F(1,30)):
        check_at(e)
    star=F(25,1056)
    assert F(7,300)<star<F(11,456)<F(1,40)
    assert expected(L0,'full',star)-expected(L0,'LR',star)==F(9,44)
    assert expected(L1,'full',star)-expected(L1,'LR',star)==F(9,44)
    for e in (LO,F(0),F(7,300),star,F(11,456),F(1,40),HI):
        gaps=[expected(l,'full',e)-expected(l,'LR',e) for l in (L0,L1)]
        assert max(gaps)>=F(9,44)
    print('SHARP TWO-DIRECTION GAP >= 9/44 ON REAL |eps|<1/12')
    print('ALL EXACT AFFINE ENVELOPE AND COLLISION CHECKS PASSED')

if __name__=='__main__':main()
