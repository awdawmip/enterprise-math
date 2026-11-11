"""Single-column separation for complete words with stock-dependent final gap.

Polynomials have ascending coefficients and are stored in SymPy's ZZ[c].
The second indeterminate is the unreduced tail likelihood Y_c, common to all words.
"""
from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction as F
from functools import cache
from itertools import combinations,product
from math import prod,ceil,comb
from pathlib import Path
import json
import sys
import sympy as sp
from sympy.polys.rings import ring
from sympy import ZZ

R,C=ring('c',ZZ)
AJ=(3,48,192)
BJ=(15,60,96)

def matmul(u,v):
    a,b,h,d=u
    e,f,g,i=v
    return a*e+b*g,a*f+b*i,h*e+d*g,h*f+d*i

def prim(mat):
    g=R.zero
    for p in mat:
        if p:g=g.gcd(p)
    return tuple(p.exquo(g) for p in mat)

@cache
def block(r,j,m):
    k=2*r+1
    v=C-j-m
    aa=prod(k+4*(C-j-i) for i in range(m+1))
    bb=prod(k+C-j-i for i in range(m+1))
    ee=(k-1+v)*prod(4*k+C-j-i for i in range(m+1))
    t=28*(k-1+4*v)*aa*bb
    return prim((t,aa*ee,t,4**m*ee*bb))

@cache
def window(r,word):
    if not word:return R.one,R.zero,R.zero,R.one
    j=sum(word[:-1])
    return prim(matmul(window(r,word[:-1]),block(r-len(word)+1,j,word[-1])))

@cache
def tail(s,j):
    v=C-s
    d=(v+2)*(v+3)*(v+4)
    up=prod((4*(C-i)+4 for i in range(s)),start=R.one)
    dn=prod((4*(C-i)+1 for i in range(s)),start=R.one)
    return prim(((840*AJ[j]+BJ[j]*d)*up,R.zero,840*AJ[j]*up,32*d*dn))

@cache
def column(word,j):
    return prim(matmul(window(len(word),word),tail(sum(word),j)))

def crossing(u,v):
    a,b,h,d=u;e,f,g,i=v
    return (b*i-f*d,a*i+b*g-e*d-f*h,a*g-e*h)

def evaluate(p,c):
    return int(p.evaluate(C,c))

def roots_at_and_after(p,c0):
    if p.degree()==0:return []
    # shift integer origin to the first legal stock and use Descartes' sign test.
    shift=p.compose(C,C+c0)
    if shift.LC<0:shift=-shift
    if all(v>0 for v in shift.values()):
        return [c0] if (0,) not in shift else []
    q=sp.Poly.from_dict(dict(p),sp.Symbol('c'),domain=ZZ)
    return sorted(int(z) for z in q.ground_roots() if z.q==1 and z>=c0)

def sumabs(p):return sum(abs(int(a)) for a in p.values())

def bound(coeff,c0):
    d=max(p.degree() for p in coeff if p)
    height=max(sumabs(p) for p in coeff)
    c=max(c0,2*d+1)
    # For c>=2d+1, (1+1/c)^d<2, so the bound holds forever thereafter.
    while 4**(c-2)<=height*c**d:
        c+=1
    return c

def allwords(r,total):
    if r==0:
        yield ()
    else:
        for i in range(total+1):
            for sub in allwords(r-1,total-i):yield (i,)+sub

def y_next(y,c):
    return y*F(4*c+1,4*c+4)

def matrix_value(mat,c,y):
    a,b,h,d=[evaluate(q,c) for q in mat]
    return (a*y+b)/(h*y+d)

def census(r,total,budget=None):
    words=(list(allwords(r,total)) if budget is None else
           [w for length in range(1,budget+1) for w in allwords(length,budget-length)])
    # Compare every column simultaneously; check actual integers below one common
    # denominator threshold once per legal word rather than once per equation.
    largest_start=0
    post=set()
    pairs=0
    degs=Counter()
    for u,v in combinations(words,2):
        for i,j in product(range(3),repeat=2):
            eq=crossing(column(u,i),column(v,j))
            nonzero=[p for p in eq if p]
            assert nonzero
            g=nonzero[0]
            for p in nonzero[1:]:g=g.gcd(p)
            # Retain g's positive integer roots; then remove this irrelevant scale
            # to reduce sizes in the rational-root bound at all remaining stocks.
            c0=max(sum(u),sum(v))+2
            post.update(roots_at_and_after(g,c0))
            reduced=tuple(p.exquo(g) for p in eq)
            largest_start=max(largest_start,bound(reduced,c0))
            degs[g.degree()]+=1
            pairs+=1
    last=max({largest_start-1}|post)
    yy=F(1)
    hits=[]
    count=0
    for c in range(2,last+1):
        if c>2:yy=y_next(yy,c)
        if c>=largest_start and c not in post:continue
        seen={}
        for w in words:
            if c<sum(w)+2:continue
            values=[matrix_value(column(w,j),c,yy) for j in range(3)]
            for j,v in enumerate(values):
                for other,k in seen.get(v,[]):
                    if other!=w:hits.append((c,other,k,w,j))
                seen.setdefault(v,[]).append((w,j))
                count+=1
    return dict(r=r if budget is None else None,max_pre_tail_fives=total if budget is None else None,
                varying_depth_length_plus_fives_budget=budget,words=len(words),cross_column_comparisons=pairs,
                gcd_degree_counts=sorted(degs.items()),candidate_gcd_root_stocks=sorted(post),
                first_stock_dominated_by_denominator=largest_start,largest_stock_evaluated=last,
                exact_column_values=count,cross_word_column_equalities=hits)
if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--r',type=int,default=3)
    p.add_argument('--total',type=int,default=2)
    p.add_argument('--budget',type=int)
    args=p.parse_args()
    print(json.dumps(census(args.r,args.total,args.budget),indent=2))
