#!/usr/bin/env python3
"""PREFIX-474: exact finite regression certificate for the aa suffix theorem.
Uses only Python standard-library integers. Extrapolation to all n rests on the paper proof.
"""
from collections import Counter
from math import comb

ORD = 'aAbBcCdDeE'
WEIGHTS = dict(zip(ORD, (6,1,12,1,18,1,24,1,36,1)))
A_COEF = (0,1,0,2,1)
C_COEF = (0,0,1,0,1)
ZERO = (0, 0,0,0,0,0, 0,0, 0)  # x-count, 5 signed coords, A,C, KMP q


def advance(st, letter):
    if letter == 'x':
        return (st[0]+1, *st[1:8], 0)
    idx = ORD.index(letter)
    axis, sign = divmod(idx,2)[0], (1 if idx%2 == 0 else -1)
    v = list(st)
    old_y = v[axis+1]
    v[axis+1] += sign
    if sign*old_y < 0:
        v[6] += A_COEF[axis]
        v[7] += C_COEF[axis]
    v[8] = min(2,st[8]+1) if letter == 'a' else 0
    return tuple(v)


def base_word(word):
    st = ZERO
    for ch in word: st = advance(st,ch)
    return st[:8]


def pad(f,word):
    st = f + (0,)
    for ch in word: st=advance(st,ch)
    return st[:8]


def polynomial_product(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):r[i+j]+=x*y
    return r

# B(z)=(1+2z^2)(1+z)^2(1+z-z^3)/((1-z)^8(1-z^3)).
NUM = polynomial_product(polynomial_product([1,0,2],[1,2,1]),[1,1,0,-1])

def B(n):
    if n<0:return 0
    return sum(c*comb(n-i-3*t+7,7) for i,c in enumerate(NUM)
               for t in range(max(0,(n-i)//3)+1) if n-i-3*t>=0)

def u(n):
    return 0 if n<=0 else (2 if n==2 else 1)

def F(n):
    return B(n)+B(n-1)+B(n-2)-u(n)-u(n-1)

def N1(n):
    return B(n) if n<2 else B(n)+B(n-2)-1

def direct_enumeration(n):
    # Independent full words -> occupancies, not the incremental BRC update.
    hist=Counter(); masses=Counter()
    def visit(word,mass):
        if len(word)==n:
            cnt=[(word.count(ORD[2*i]),word.count(ORD[2*i+1])) for i in range(5)]
            y=tuple(p-m for p,m in cnt)
            pair=tuple(min(p,m) for p,m in cnt)
            f=(word.count('x'),*y,pair[1]+2*pair[3]+pair[4],pair[2]+pair[4])
            q=2 if word.endswith('aa') else 1 if word.endswith('a') else 0
            key=f+(q,)
            hist[key]+=1;masses[key]+=mass
            return
        for ch in ORD:
            visit(word+ch,mass*WEIGHTS[ch])
        if not word or word.endswith('aa'):
            visit(word+'x',mass)
    visit('',1)
    return hist,masses


def main():
    paths=Counter({ZERO:1}); masses=Counter({ZERO:1})
    bases=[]
    prev_count=[1];prev_mass=[1]
    for n in range(9):
        supports=[{st[:8] for st in paths if st[8]==q} for q in range(3)]
        base=set.union(*supports)
        bases.append(base)
        E=set()
        if n>=1:E.add(base_word('a'*n))
        if n==2:E.add(base_word('xa'))
        assert supports[0]==base-E,('q0_holes',n)
        if n>=1:assert supports[1]=={pad(f,'a') for f in bases[n-1]-({base_word('a'*(n-1))} if n-1>=1 else set()) - ({base_word('xa')} if n-1==2 else set())},('q1_image',n)
        if n>=2:assert supports[2]=={pad(f,'aa') for f in bases[n-2]},('q2_image',n)
        assert len(base)==B(n),('B',n,len(base),B(n))
        assert len(paths)==F(n),('F',n,len(paths),F(n))
        assert len(supports[0])==B(n)-u(n)
        assert len(supports[1])==B(n-1)-u(n-1)
        assert len(supports[2])==B(n-2)
        h0=len(base)
        h1=len({(st[:8],int(st[8]==2)) for st in paths})
        h2=len(paths)
        assert (h0,h1,h2)==(B(n),N1(n),F(n)),('horizon',n,h0,h1,h2)
        count=sum(paths.values());weight=sum(masses.values())
        if n>=1:
            cexpected=10*prev_count[-1]+(prev_count[n-3] if n>=3 else (1 if n==1 else 0))
            mexpected=101*prev_mass[-1]+(36*prev_mass[n-3] if n>=3 else (1 if n==1 else 0))
            assert count==cexpected and weight==mexpected,('series',n,count,weight,cexpected,mexpected)
            prev_count.append(count);prev_mass.append(weight)
        if n<=4:
            h,m=direct_enumeration(n)
            assert h==paths,('independent_ordered_paths',n)
            assert m==masses,('independent_weighted_paths',n)
        print(f'n={n} B={len(base)} q0={len(supports[0])} q1={len(supports[1])} q2={len(supports[2])} F={len(paths)} H1={h1} paths={count} mass={weight}')
        if n==8:break
        np=Counter();nm=Counter()
        for st,k in paths.items():
            for ch in ORD:
                z=advance(st,ch);np[z]+=k
            if n==0 or st[8]==2:
                z=advance(st,'x');np[z]+=k
        for st,m in masses.items():
            for ch in ORD:
                z=advance(st,ch);nm[z]+=m*WEIGHTS[ch]
            if n==0 or st[8]==2:
                z=advance(st,'x');nm[z]+=m
        paths,masses=np,nm
    print('COUNTEREXAMPLE: aa n=2, a^2 belongs to T_a(S_1) but q1 excludes it; q2 contains it.')
    print('UNIVERSAL_PROOF_IS_IN_PAPER; FINITE_CHECKS_0_THROUGH_8_PASS')
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
