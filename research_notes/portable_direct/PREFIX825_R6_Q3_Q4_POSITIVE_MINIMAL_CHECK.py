#!/usr/bin/env python3
"""Exact reproducible q=3/4 positive-source BRC observer-carrier verification.

All operations are named weighted removals plus a marked-source insertion, with
cardinality ≤q. Nonnegative counts, exact integer/rational arithmetic; no
physical/native heartbeat interpretation. Requires Python3 standard library.
"""
from itertools import combinations, product
from fractions import Fraction
from collections import defaultdict
import json
from pathlib import Path


def labels(q):
    return ([('U',k,h) for k in range(q+1) for h in range(k+1)]
            +[('V',k,h) for k in range(q) for h in range(k+1)])


def moment_vector(state,beta,L):
    present,S=state
    e=[1]+[0]*len(S)
    for idx in S:
        for j in range(len(S),0,-1):e[j]+=beta[idx]*e[j-1]
    d={('V' if present else 'U',len(S),h):e[h] for h in range(len(S)+1)}
    return [d.get(label,0) for label in L]


def transitions(state,beta,q,a,b):
    mark,S=state
    for i in S:
        yield (mark,tuple(j for j in S if j!=i)),beta[i]
    if mark:yield (False,S),b
    elif len(S)<q:yield (True,S),a


def states(q,beta):
    return [(mark,S) for mark in (False,True)
            for k in range(q+1-int(mark))
            for S in combinations(range(len(beta)),k)]


def model_operator(q,a,b,L):
    idx={key:i for i,key in enumerate(L)}
    M=[[0]*len(L) for _ in L]
    for i,(t,k,h) in enumerate(L):
        if t=='U':
            if k<q:M[i][idx['U',k+1,h+1]]=h+1
            if k<q:M[i][idx['V',k,h]]=b
        else:
            if k<q-1:M[i][idx['V',k+1,h+1]]=h+1
            M[i][idx['U',k,h]]=a
    return M


def output_operator(q,L):
    idx={key:i for i,key in enumerate(L)}
    C=[[0]*len(L) for _ in range(q+1)]
    for l in range(q+1):
        C[l][idx['U',l,0]]=1
        if l:C[l][idx['V',l-1,0]]=1
    return C


def q3_rows(a,b):
    return [
        {('U',0,0):1},{('U',2,0):1},{('U',2,1):1},{('U',2,2):1},
        {('V',1,0):1},{('V',1,1):1},
        {('U',3,0):1,('V',2,0):1},{('U',3,1):1,('V',2,0):b},
        {('U',1,0):1,('V',0,0):1},{('U',1,1):1,('V',0,0):b},
        {('U',3,2):2,('V',2,1):b},{('U',3,3):3,('V',2,2):b},
        {('V',2,1):1,('U',1,0):a},{('V',2,2):2,('U',1,1):a}]


def q4_rows(a,b):
    omit={('U',4,0),('U',4,1),('V',3,0),
          ('U',2,0),('U',2,1),('U',4,2),('U',4,3),
          ('V',1,0),('V',3,1),('V',3,2)}
    rows=[{key:1} for key in labels(4) if key not in omit]
    assert len(rows)==15
    return rows+[
        {('U',4,0):1,('V',3,0):1},{('U',4,1):1,('V',3,0):b},
        {('U',2,0):1,('V',1,0):1},{('U',2,1):1,('V',1,0):b},
        {('U',4,2):2,('V',3,1):b},{('U',4,3):3,('V',3,2):b},
        {('V',3,1):1,('U',2,0):a},{('V',3,2):2,('U',2,1):a}]


def rows_to_matrix(rows,L):
    idx={k:i for i,k in enumerate(L)}
    out=[[0]*len(L) for _ in rows]
    for i,d in enumerate(rows):
        for label,value in d.items():out[i][idx[label]]=value
    return out


def q3_update(x,a,b):
    return [x[9],x[7],x[10],x[11],x[12],x[13],
            a*x[1],a*b*x[1],
            x[2]+b*x[4]+x[5]+a*x[0],
            2*x[3]+2*b*x[5]+a*b*x[0],
            a*b*x[2],a*b*x[3],
            2*a*x[2]+a*b*x[4],4*a*x[3]+a*b*x[5]]


def q4_update(x,a,b):
    return [x[2]+b*x[9],x[18],2*x[3]+b*x[10],3*x[7]+b*x[13],
            x[16],x[19],x[20],4*x[8]+b*x[14],0,
            a*x[0]+x[10],a*x[2]+2*x[13],x[21],x[22],a*x[3]+3*x[14],
            a*x[7],a*x[4],a*b*x[4],
            a*x[1]+x[5]+b*x[11]+x[12],
            a*b*x[1]+2*x[6]+2*b*x[12],
            a*b*x[5],a*b*x[6],2*a*x[5]+a*b*x[11],4*a*x[6]+a*b*x[12]]


def output(x,q):
    return [x[0],x[8],x[1]+x[4],x[6]] if q==3 else [x[0],x[1]+x[9],x[17],x[4]+x[11],x[15]]


def matmul(A,B):
    return [[sum(x*B[k][j] for k,x in enumerate(row))
             for j in range(len(B[0]))] for row in A]


def rank(A):
    R=[list(map(Fraction,row)) for row in A]
    pivot=0
    for j in range(len(R[0])):
        i=next((z for z in range(pivot,len(R)) if R[z][j]),None)
        if i is None:continue
        R[pivot],R[i]=R[i],R[pivot]
        z=R[pivot][j]
        R[pivot]=[v/z for v in R[pivot]]
        for k in range(pivot+1,len(R)):
            z=R[k][j]
            if z:R[k]=[v-z*w for v,w in zip(R[k],R[pivot])]
        pivot+=1
        if pivot==len(R):break
    return pivot


def bareiss(A):
    M=[row[:] for row in A];n=len(M);prior=1;sign=1
    for k in range(n-1):
        if not M[k][k]:
            p=next((i for i in range(k+1,n) if M[i][k]),None)
            if p is None:return 0
            M[k],M[p]=M[p],M[k];sign=-sign
        d=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=M[i][j]*d-M[i][k]*M[k][j]
                assert num%prior==0
                M[i][j]=num//prior
        for i in range(k+1,n):M[i][k]=0
        prior=d
    return sign*M[-1][-1]


CERT={
    3:{'rows':[0,1,2,3,4,5,6,7,8,9,10,11,12,14],
       'cols':[0,1,2,3,4,5,6,7,8,9,10,11,12,14],
       'det':lambda a,b:96*a**5*b,'rank':14},
    4:{'rows':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,22,25,30],
       'cols':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24],
       'det':lambda a,b:21233664*a**11*b**7,'rank':23},
}


def verify(q,a,b,beta,counts):
    L=labels(q);T=rows_to_matrix(q3_rows(a,b) if q==3 else q4_rows(a,b),L)
    up=q3_update if q==3 else q4_update
    Q=model_operator(q,a,b,L);C=output_operator(q,L)
    # Exact quotient identity on full abstract moment space.
    for j in range(len(L)):
        tcol=[r[j] for r in T]
        projected=up(tcol,a,b)
        assert [sum(x*Q[k][j] for k,x in enumerate(row)) for row in T]==projected
        assert [r[j] for r in C]==output(tcol,q)
        counts['abstract_coordinate_intertwining']+=1
    assert rank(T)==CERT[q]['rank']
    if a==1 and b==1:
        O=[];cur=C
        for _ in range(10):
            O.extend(cur);cur=matmul(cur,Q)
        rows,cols=CERT[q]['rows'],CERT[q]['cols']
        D=bareiss([[O[i][j] for j in cols] for i in rows])
        assert D==CERT[q]['det'](a,b)
        assert rank(O)==CERT[q]['rank']
        counts['rational_rank_and_determinant_checks']+=1
    S=states(q,beta)
    cols=[moment_vector(s,beta,L) for s in S]
    # Named-state moments span each conditional moment block.
    if a==1 and b==1:
        assert rank([list(row) for row in zip(*cols)])==len(L)
        counts['named_moment_full_rank_checks']+=1
    car={s:[sum(x*y for x,y in zip(row,v)) for row in T] for s,v in zip(S,cols)}
    for s in S:
        v=car[s]
        nxt=[sum(w*car[dst][i] for dst,w in transitions(s,beta,q,a,b)) for i in range(len(v))]
        assert nxt==up(v,a,b)
        assert output(v,q)==[int(len(s[1])+s[0]==i) for i in range(q+1)]
        assert all(z>=0 for z in v+nxt)
        counts['named_basis_checks']+=1
        dist={s:1};x=v
        for h in range(10):
            hist=[0]*(q+1)
            for u,weight in dist.items():hist[len(u[1])+u[0]]+=weight
            assert hist==output(x,q)
            new=defaultdict(int)
            for u,weight in dist.items():
                for dst,w in transitions(u,beta,q,a,b):new[dst]+=weight*w
            dist=new;x=up(x,a,b)
            counts['named_future_histogram_checks']+=1
    counts['configurations']+=1
    counts['named_states_total']+=len(S)
    return {'q':q,'a':a,'b':b,'beta':list(beta),'named_states':len(S),
            'carrier_dimension':len(T),'conditional_moment_dimension':len(L)}


def main():
    counts=defaultdict(int); configs=[]
    for q,beta_sets in ((3,((1,2,3,4),(1,2,3,5,8),(1,2,3,4,7,11))),
                        (4,((1,2,3,4,5),(1,2,4,7,9,11)))):
        for beta,a,b in product(beta_sets,range(1,4),range(1,4)):
            configs.append(verify(q,a,b,beta,counts))
    output_json={
       'schema':'PREFIX825_R6_Q3_Q4_POSITIVE_CARRIER_V1',
       'result':'ALL_EXACT_ASSERTIONS_PASSED',
       'arithmetic':'arbitrary-precision integers, Fraction exact rational Gaussian elimination, Bareiss integer determinant',
       'q3_dimension':14,'q4_dimension':23,
       'scope':'q=3 with 3 named-beta sets; q=4 with 2 sets; a,b=1,2,3; all named admissible states; depths 0..9',
       'counts':dict(counts),'configurations':configs,
       'not_claimed':['native X6 Cell/Link/Port event semantics','signed phase/amplitude cancellation','unrestricted observer language','nonlinear minimum dimension','formal task CLAIM or acceptance']}
    p=Path(__file__).with_name('PREFIX825_R6_Q3_Q4_POSITIVE_MINIMAL_RESULTS.json')
    p.write_text(json.dumps(output_json,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'result':output_json['result'],'counts':dict(counts)},ensure_ascii=False))


if __name__=='__main__':main()
