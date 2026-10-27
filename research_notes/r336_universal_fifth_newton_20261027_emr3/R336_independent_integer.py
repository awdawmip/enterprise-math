#!/usr/bin/env python3
"""Independent exact-check of R336 fifth-highest Newton claim.
Pure Python integer/Fraction reconstruction of untruncated signed BRC kernel.
Does not import the symbolic argument or precomputed coefficient tables.
"""
from fractions import Fraction
from math import comb
from hashlib import sha256
import argparse, json

def choose(n,k):return comb(n,k) if 0<=k<=n else 0
def padd(a,b):
    out=[0]*max(len(a),len(b))
    for i,v in enumerate(a):out[i]+=v
    for i,v in enumerate(b):out[i]+=v
    return out
def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        if not v: continue
        for j,w in enumerate(b): out[i+j]+=v*w
    return out
def mon(n,v,shift):return [0]*shift+[v*choose(n,k) for k in range(n+1)] if n>=0 else [0]
def K(i):
    d=(-choose(4,i)+choose(2,i-1), choose(5,i-1)-choose(5,i-2),choose(7,i-2),-choose(9,i-3))
    out=[0]
    for j,v in enumerate(d,1):
        if v:out=padd(out,mon(i+1-j,-v,i-1))
    return out
def J(s):
    out=[0]
    for v,n in ((-choose(3,s-1),s),(-choose(6,s-1),s-1),(choose(8,s-2),s-2)):
        if v:out=padd(out,mon(n,v,s))
    return out
def rows(max_s):
    Bs=[[1,1]]
    Ks=[None]+[K(i) for i in range(1,13)]
    for s in range(1,max_s+1):
        row=J(s)
        for i in range(1,min(s,12)+1):row=padd(row,pmul(Ks[i],Bs[s-i]))
        while len(row)>1 and not row[-1]:row.pop()
        Bs.append(row)
    return Bs

def directD(B,q,k):
    return sum((-1)**(k-v)*choose(k,v)*2**(q-v)* (B[q+v][q] if q<len(B[q+v]) else 0)
               for v in range(k+1))

def differences(seq):
    out=[];c=list(seq)
    while c:
        out.append(c[0]);c=[c[i+1]-c[i] for i in range(len(c)-1)]
    return out

def fifth(r):
    return Fraction(6**r*(39366*r**4 - 185652*r**3 + 89864*r*r + 126192*r + 170815),455625)

def run(max_r=64):
    assert max_r>=4
    Bs=rows(3*max_r+2)
    positive=0;negative_exterior=0
    for s,row in enumerate(Bs):
        for q in range(s+1):
            assert q<len(row) and row[q]>0,(s,q, row[q] if q<len(row) else None)
            positive+=1
        negative_exterior+=sum(v<0 for v in row[s+1:])
    sig=sha256();samples=[]
    for r in range(4,max_r+1):
        H=[Fraction(directD(Bs,r+u,u),5**u) for u in range(r+2)]
        c=differences(H)
        actual=c[r-4]; pred=fifth(r)
        assert actual==pred,(r,actual,pred)
        assert c[r-3]==Fraction(2*6**r*(1458*r**3-3681*r*r-1304*r+1425),10125),(r,'fourth-high')
        assert c[r-2]==Fraction(2*6**r*(243*r*r-245*r-182),675),(r,'third-high')
        assert c[r-1]==Fraction(6**r*(6*r-1),5),(r,'second-high')
        assert c[r]==6**r,(r,'top-high')
        assert c[r+1]==0,(r,'degree bound point')
        assert all(x>0 for x in c[:r+1]),(r,'full difference cone',[(k,x) for k,x in enumerate(c[:r+1]) if x<=0])
        sig.update(f'{r}:{actual.numerator}/{actual.denominator}\n'.encode('ascii'))
        if r<=10 or r==max_r:
            samples.append({'r':r,'c_r_rminus4':f'{actual.numerator}/{actual.denominator}'})
    return {'schema':'R336_FIFTH_HIGHEST_INDEPENDENT_INTEGER_EVIDENCE_V1','status':'PASS',
        'r_checked':[4,max_r],'fifth_count':max_r-3,'prior_four_count':max_r-3,
        'extra_degree_nodes':max_r-3,'untruncated_B_rows':[0,len(Bs)-1],
        'positive_inside_triangle':positive,'negative_outside_triangle_retained':negative_exterior,
        'sha256_fifth_sequence':sig.hexdigest(),'samples':samples,
        'arithmetic':'integer plus Fraction; exact; no floating-point signs',
        'mathematical_status':'finite crosscheck; universal symbolic claim depends on R330 author-side extraction/degree lemma',
        'admission':'AUTHOR_SIDE/UNREVIEWED/NOT_ADMITTED'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--max-r',type=int,default=64);p.add_argument('--out',default='/mnt/data/em_r336/R336_INTEGER_EVIDENCE.json')
    a=p.parse_args();res=run(a.max_r)
    with open(a.out,'w',encoding='utf-8') as f:json.dump(res,f,ensure_ascii=False,indent=2);f.write('\n')
    print('PASS',res)
