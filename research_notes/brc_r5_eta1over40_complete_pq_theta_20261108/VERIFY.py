#!/usr/bin/env python3
"""Exact R5 finite BRC Blackwell certificates; Python standard library only."""
from fractions import Fraction as F
from pathlib import Path
import json

DATA=json.loads((Path(__file__).parent/'CERTIFICATES.json').read_text())
r=tuple(map(F,DATA['likelihoods']))
ZERO=F(0); ONE=F(1)
E0=(ZERO,)*7
E1=(ONE,)+(ZERO,)*6

def source(theta,p,q,eta=F(1,40)):
    return (ONE,ONE,eta,(F(13,40)+eta/80)*p,F(9,40)*eta+theta/10,
            (F(3,40)+F(21,80)*eta)*q,theta/10)

def mass(f):
    g,a,b,u,v,w,z=f
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
            F(13,40)*a+b/80-u,(g-a)/2,
            1-g+a/10+9*b/40-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2,F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def time(f):
    g,a,b,u,v,w,z=f
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)

def lawful(f):
    g,a,b,u,v,w,z=f
    return (0<=a<=g<=1 and 0<=b<=g and
            0<=u<=F(13,40)*a+b/80 and
            0<=w<=F(3,40)*a+F(21,80)*b and
            0<=z<=a/10 and 0<=v-z<=F(9,40)*b)

def seedless(f):
    g,a,b,u,v,w,z=f
    return 9*b*z==4*a*(v-z)

def face(f,name):
    g,a,b,u,v,w,z=f
    if name=='G':return b==0 and v==z
    if name=='F':return z==a/10 and v-z==9*b/40
    raise ValueError(name)

def diag(f):
    m=mass(f)
    return tuple(tuple(m[i] if i==j else ZERO for j in range(7)) for i in range(7))

def lin(weights,vectors):
    return tuple(sum(w*v[k] for w,v in zip(weights,vectors)) for k in range(7))

def linQ(weights,matrices):
    return tuple(tuple(sum(w*m[i][j] for w,m in zip(weights,matrices)) for j in range(7)) for i in range(7))

def mix(triples,weights):
    return (lin(weights,[tr[0] for tr in triples]),
            lin(weights,[tr[1] for tr in triples]),
            linQ(weights,[tr[2] for tr in triples]))

def identity(f):
    return (f,f,diag(f))

def check(tr,selected_face=None):
    x,y,q=tr
    assert lawful(x) and lawful(y), ('invalid flow',x,y)
    assert seedless(y),('not seedless',y)
    assert selected_face is None or face(y,selected_face)
    mx,my=mass(x),mass(y)
    assert sum(mx)==sum(my)==ONE
    assert sum(r[i]*mx[i] for i in range(7))==sum(r[i]*my[i] for i in range(7))==ONE
    assert time(x)==time(y)
    assert all(q[i][j]>=0 for i in range(7) for j in range(7))
    assert all(sum(q[i][j] for j in range(7))==my[i] for i in range(7))
    assert all(sum(q[i][j] for i in range(7))==mx[j] for j in range(7))
    assert all(sum(r[i]*q[i][j] for i in range(7))==r[j]*mx[j] for j in range(7))

def anchor(face_name,theta,p,q):
    key=f'{face_name}_t{theta}_p{p}_q{q}'
    d=DATA['certificates'][key]
    y=tuple(map(F,d['y']))
    qmat=[[ZERO for j in range(7)] for i in range(7)]
    for i,j,v in d['edges']:
        qmat[i][j]=F(v)
    tr=(source(theta,p,q),y,tuple(tuple(row) for row in qmat))
    check(tr,face_name)
    return tr

def normalized(theta,p,q):
    assert 0<=theta<=1 and 0<=p<=1 and 0<=q<=1
    if theta<=F(3,4):
        t=F(4,3)*theta
        def at(face_name,vp,vq):
            return mix((anchor(face_name,ZERO,vp,vq),
                        anchor(face_name,F(3,4),vp,vq)),(1-t,t))
        if 2*q<=p:
            wt=(1-p,p-2*q,2*q)
            tr=mix([at('G',0,0),at('G',1,0),at('G',1,F(1,2))],wt)
            check(tr,'G')
        else:
            t2=(q-p/2)/(1-p/2)
            wt=((1-t2)*(1-p),t2*(1-p),t2*p,(1-t2)*p)
            tr=mix([at('F',0,0),at('F',0,1),
                    at('F',1,1),at('F',1,F(1,2))],wt)
            check(tr,'F')
    else:
        t=4*theta-3
        weights=((1-p)*(1-q),(1-p)*q,p*(1-q),p*q)
        triples=[]
        for pp,qq in ((ZERO,ZERO),(ZERO,ONE),(ONE,ZERO),(ONE,ONE)):
            a=anchor('F',F(3,4),pp,qq)
            b=identity(source(ONE,pp,qq))
            triples.append(mix((a,b),(1-t,t)))
        tr=mix(triples,weights)
        check(tr,'F')
    assert tr[0]==source(theta,p,q)
    return tr

def scaled(theta,p,q,s,g,h):
    assert 0<=s<=g<=1 and 0<=h<=1
    tr=normalized(theta,p,q)
    vv=mix((identity(E0),identity(E1),tr),(1-g,g-s,s))
    ans=mix((vv,identity(vv[1])),(1-h,h))
    check(ans)
    target=(g,s,s/40,s*(F(13,40)+F(1,3200))*p,
            s*(F(9,1600)+theta/10),
            s*(F(3,40)+F(21,3200))*q,s*theta/10)
    assert vv[0]==target
    return ans

def main():
    for key,d in DATA['certificates'].items():
        anchor(d['face'],F(d['theta']),F(d['p']),F(d['q']))
    count=0
    ps=tuple(map(F,('0','1/7','1/3','1/2','2/3','1')))
    qs=tuple(map(F,('0','1/5','1/3','1/2','3/4','1')))
    thetas=tuple(map(F,('0','1/10','29/112','1/2','2/3','3/4','7/8','1')))
    for theta in thetas:
        for p in ps:
            for q in qs:
                scaled(theta,p,q,ONE,ONE,ZERO)
                count+=1
    for theta in map(F,('0','1/2','3/4','7/8','1')):
        for p,q in ((ZERO,ZERO),(ONE,ZERO),(ONE,ONE),(F(1,3),F(3,4))):
            for g,s,h in ((F(1,2),F(1,4),F(1,3)),
                          (ONE,ZERO,ONE),(ONE,ONE,F(1,2))):
                scaled(theta,p,q,s,g,h)
                count+=1
    print('EXACT_ANCHOR_CERTIFICATES_PASS',len(DATA['certificates']))
    print('EXACT_REGRESSION_TRIPLES_PASS',count)
    print('PASS_R5_ETA_1_40_FULL_PQ_THETA_RECTANGLE_TWO_FACE_CONSTRUCTION')

if __name__=='__main__':
    main()
