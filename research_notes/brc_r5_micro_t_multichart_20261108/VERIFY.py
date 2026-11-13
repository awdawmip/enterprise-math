#!/usr/bin/env python3
"""Exact R5 tiny-positive-ratio Blackwell certificate checker. Standard library only.
The embedded 64 sparse rational certificates and multi-affine proof certify
four continuous t slabs; randomized rational interior points check code only.
"""
from fractions import Fraction as F
from itertools import product
import random

R = [F(1, 10), F(1, 2), F(3, 4), F(1), F(5, 4), F(3, 2), F(19, 10)]


def source(t, p, q, theta):
    return (F(1), t, F(1), (F(13, 40)*t + F(1, 80))*p,
            t*theta/10 + F(27, 160),
            (F(3, 40)*t + F(21, 80))*q, t*theta/10)


def target(c, tau):
    g, a, b, u, w = c
    z = tau*a/10
    return (g, a, b, u, z + F(9, 40)*tau*b, w, z)


def masses(x):
    g, a, b, u, v, w, z = x
    return (F(509, 900)*u + F(47, 180)*z + F(67, 162)*(v-z) + w/100,
            F(13, 40)*a + b/80-u,
            (g-a)/2,
            1-g+a/10+F(9, 40)*b-v+F(191, 450)*(u+w)
             +F(43, 90)*z+F(14, 81)*(v-z),
            (g-b)/2,
            F(3, 40)*a+F(21, 80)*b-w,
            u/100+F(47, 180)*z+F(67, 162)*(v-z)+F(509, 900)*w)


def stops(x):
    g, a, b, u, v, w, z = x
    return (1+g+F(3, 8)*a+F(5, 8)*b+u/2+v+F(3, 2)*w,
            1+g+(a+b)/2+u+v+w)


def lawfulness(x, seedless=False):
    g,a,b,u,v,w,z=x
    assert 0 <= a <= g <= 1 and 0 <= b <= g
    assert 0 <= u <= F(13,40)*a + b/80
    assert 0 <= w <= F(3,40)*a + F(21,80)*b
    assert 0 <= z <= a/10 and 0 <= v-z <= F(9,40)*b
    m=masses(x)
    assert all(mi >= 0 for mi in m)
    assert sum(m) == 1 and sum(ri*mi for ri,mi in zip(R,m)) == 1
    if seedless: assert 9*b*z==4*a*(v-z)


def check(x, y, edge_map):
    lawfulness(x)
    lawfulness(y, True)
    mx,my=masses(x),masses(y)
    assert stops(x)==stops(y)
    q=[[F(0) for _ in range(7)] for _ in range(7)]
    for idx,val in edge_map.items():
        assert 0<=idx<49 and val>0
        q[idx//7][idx%7]=val
    for i in range(7):assert sum(q[i])==my[i]
    for j in range(7):
        assert sum(q[i][j] for i in range(7))==mx[j]
        assert sum(R[i]*q[i][j] for i in range(7))==R[j]*mx[j]


ALPHABET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
# 64 exact sparse supports with 27 optional rational free-value pins.
# Positions 0..48 map to (i,j) via idx=7*i+j; positions 49..53 are
# the five target parameters (g,a,b,u,w).
SEEDS = """0128FGNOXelmnpqr 0128FGNOXelmnpqr 0189FGHNOjmnpqr 0189FGHNOjmnpqr 03GOXcelmnopqr 03GOXcelmnopqr 02GHOVbjmnopqr~V:123573931663/5440829599273226300 02GHOVbjmnopqr~V:111065131663/5440829599273226300 0158FGOelmnopqr 0158FGOelmnopqr 0189FGHNOjmnopqr~r:4835/18419 0189FGHNOjmnopqr~r:4625/17619 03GOXcelmnopqr 03GOXcelmnopqr 02GHOcijmnopqr~r:4793/18259 02GHOcijmnopqr~r:4604/17539
0128FGNOXelmnpqr 0128FGNOXelmnpqr 0189FGHNOjmnpqr 0189FGHNOjmnpqr 03GOXcelmnopqr 03GOXcelmnopqr 02GHOVbjmnopqr~r:3082/11741 02GHNOVjmnopqr~r:21/80 0158FGOelmnopqr 0158FGOelmnopqr 0189FGHNOjmnopqr~r:488/1859 0189FGHNOjmnopqr~r:467/1779 03GOXcelmnopqr 03GOXcelmnopqr 02GHOVbjmnopqr~r:2309/8796 023GHObjmnopqr~r:467/1779
018GMOXelmnopqr 018GMOXelmnopqr 0189FGHNOjmnpqr 0189FGHNOjmnpqr 039GNOVXelmnopqr~r:1/7247 039GNOVXelmnopqr~r:1/7410 02GHOVbjmnopqr~r:310/1181 02GHOVbjmnopqr~r:331/1261 018GMOXelmnopqr 018GMOXelmnopqr 0189FGHNOjmnopqr~r:397/1512 0189FGHNOjmnopqr~r:1201/4574 039GNOVXelmnopqr~r:1/7246 039GNOVXelmnopqr~r:1/9291 02GHOVbjmnopqr~r:115/438 023GHObjmnopqr~r:47/179
0128FGNOXelmnpqr 0128FGNOXelmnpqr 0189FGHNOjmnpqr 0189FGHNOjmnpqr 03GOXcelmnopqr 03GOXcelmnopqr 02GHOVijmnopqr~r:21/80 02GHNOcjmnopqr~r:21/80 018FGOQelmnopqr 018FGOQelmnopqr 018GHMOjmnopqr 0189GHMOijmnopqr~r:196/745 03GOXcelmnopqr 03GOXcelmnopqr 02GHOVijmnopqr~r:121/460 02GHNOcjmnopqr~r:96/365"""

def build_system(x, tau):
    zero = (F(0),)*5
    m0 = masses(target(zero, tau)); s0 = stops(target(zero, tau))
    basis = [tuple(F(int(i==k)) for i in range(5)) for k in range(5)]
    bm = [masses(target(b, tau)) for b in basis]
    bs = [stops(target(b, tau)) for b in basis]
    yM = [[bm[k][i]-m0[i] for k in range(5)] for i in range(7)]
    yT = [[bs[k][i]-s0[i] for k in range(5)] for i in range(2)]
    mx = masses(x); tx = stops(x)
    rows=[]; rhs=[]
    def add(terms, r):
        row=[F(0)]*54
        for i,v in terms.items(): row[i]=v
        rows.append(row); rhs.append(r)
    for i in range(7):
        add({**{7*i+j:F(1) for j in range(7)},
             **{49+k:-yM[i][k] for k in range(5)}}, m0[i])
    for j in range(7):add({7*i+j:F(1) for i in range(7)},mx[j])
    for j in range(7):add({7*i+j:R[i] for i in range(7)},R[j]*mx[j])
    for i in range(2):add({49+k:yT[i][k] for k in range(5)},tx[i]-s0[i])
    return rows,rhs

def solve_cert(x,tau,seed):
    ss,sep,freeze = seed.partition('~')
    support=[ALPHABET.index(c) for c in ss]
    assert len(support)==len(set(support)) and all(i<54 for i in support)
    rows,rhs=build_system(x,tau)
    mat=[[row[i] for i in support]+[b] for row,b in zip(rows,rhs)]
    if sep:
        col,sval=freeze.split(':',1)
        j=support.index(ALPHABET.index(col))
        mat.append([F(int(i==j)) for i in range(len(support))]+[F(sval)])
    rank=0
    n=len(support)
    pivots=[]
    for col in range(n):
        pivot=next((k for k in range(rank,len(mat)) if mat[k][col]),None)
        if pivot is None:continue
        mat[rank],mat[pivot]=mat[pivot],mat[rank]
        d=mat[rank][col]
        mat[rank]=[v/d for v in mat[rank]]
        for k in range(len(mat)):
            if k!=rank and mat[k][col]:
                mult=mat[k][col]
                mat[k]=[mat[k][j]-mult*mat[rank][j] for j in range(n+1)]
        pivots.append(col);rank+=1
    assert rank==n, ('not uniquely certified',rank,n)
    for row in mat[rank:]:assert row[-1]==0,('inconsistent',row)
    vals=[F(0)]*54
    for i,col in enumerate(pivots):vals[support[col]]=mat[i][-1]
    assert all(vals[i]>0 for i in support)
    return target(vals[49:],tau),{i:vals[i] for i in range(49) if vals[i]}

def vertex(t,p,q,theta,tau,seed):
    x=source(t,p,q,theta)
    y,kernel=solve_cert(x,tau,seed)
    check(x,y,kernel)
    return x,y,kernel

def interp(verts, t, p, q, theta, lo, hi):
    v=(t-lo)/(hi-lo)
    theta_v=4*(theta-F(3,4))
    xt=[F(0)]*7; yt=[F(0)]*7; Q={}
    for (t_i,p_i,q_i,theta_i),(x,y,kernel) in verts.items():
        w=(v if t_i==hi else 1-v)
        w*=p if p_i else 1-p
        w*=q if q_i else 1-q
        w*=theta_v if theta_i==1 else 1-theta_v
        for i in range(7):xt[i]+=w*x[i];yt[i]+=w*y[i]
        for ij,val in kernel.items():Q[ij]=Q.get(ij,F(0))+w*val
    assert tuple(xt)==source(t,p,q,theta)
    return tuple(xt),tuple(yt),{i:v for i,v in Q.items() if v}


def main():
    rng=random.Random(20261108)
    n=0; edges=0; interiors=0
    intervals=[(F(1,10**6),F(1,10**5),F(300001,400000)),
               (F(1,10**5),F(1,10**4),F(30001,40000)),
               (F(1,10**4),F(1,10**3),F(3001,4000)),
               (F(1,10**3),F(369,43076),F(301,400))]
    assert len(SEEDS.splitlines())==len(intervals)
    for (lo,hi,tau),line in zip(intervals,SEEDS.splitlines()):
        tokens=line.split()
        assert len(tokens)==16
        verts={}
        for key,seed in zip(product((lo,hi),(F(0),F(1)),(F(0),F(1)),(F(3,4),F(1))),tokens):
            verts[key]=vertex(*key,tau,seed)
            n+=1;edges+=len(verts[key][2])
        for _ in range(251):
            z=lambda:F(rng.randrange(0,1001),1000)
            t=lo+(hi-lo)*z();p,q=z(),z();theta=F(3,4)+z()/4
            x,y,kernel=interp(verts,t,p,q,theta,lo,hi)
            check(x,y,kernel)
            h=z()
            xh=tuple((1-h)*x[i]+h*y[i] for i in range(7))
            qh={idx:(1-h)*val for idx,val in kernel.items()}
            for i,mi in enumerate(masses(y)):
                idx=8*i;qh[idx]=qh.get(idx,F(0))+h*mi
            check(xh,y,{i:v for i,v in qh.items() if v})
            interiors+=1
        print('PASS_INTERVAL',lo,hi,'tau',tau,'EXACT_VERTICES',len(verts),'EXACT_INTERIORS',251)
    assert n==64 and edges==642 and interiors==1004
    print('PASS_EXACT_64_RATIONAL_BLACKWELL_VERTICES',n,'POSITIVE_EDGES',edges)
    print('PASS_EXACT_1004_MULTIAFFINE_INTERIORS_AND_SOURCE_TARGET_INTERPOLANTS',interiors)
    print('THEOREM_R5_LOW_T_BRIDGE_PROOF_BY_FOUR_COMMON_CHART_SLABS')

if __name__=='__main__':main()
