"""Exact R203 row-descriptor mixed moment test; source pinned at 43ec6098b1330ae86d0a7863be336c5d97f6ef34."""
from fractions import Fraction as F
from random import Random
import json

def mm(A,B):
    return tuple(tuple(sum((a*b for a,b in zip(row,col)),F()) for col in zip(*B)) for row in A)

def trans(A): return tuple(zip(*A))

def add(A,B): return tuple(tuple(x+y for x,y in zip(u,v)) for u,v in zip(A,B))

def scaled(A,q): return tuple(tuple(q*x for x in r) for r in A)

def rows_phys(A,b,d):
    n=len(b); return tuple(tuple(r)+(F(0),)*d+(b[i],) for i,r in enumerate(A))

def rows_desc(desc,n):
    D=len(desc); rows=[]
    for src,val in desc:
        r=[F(0)]*(n+D+1)
        r[n+src if src is not None else -1]=F(1 if src is not None else val)
        rows.append(tuple(r))
    return tuple(rows)

def dense(A,b,desc,M):
    N=len(b)+len(desc)
    H=rows_phys(A,b,len(desc))+rows_desc(desc,len(b))+((F(0),)*N+(F(1),),)
    return mm(mm(H,M),trans(H))

def sparse(A,b,desc,M):
    n=len(b); D=len(desc); z=n+D
    P=[tuple(sum((A[i][t]*M[t][v] for t in range(n)),b[i]*M[z][v]) for v in range(z+1)) for i in range(n)]
    out=[[F(0)]*(z+1) for _ in range(z+1)]
    for i in range(n):
        for j in range(n): out[i][j]=sum((P[i][t]*A[j][t] for t in range(n)),P[i][z]*b[j])
        for j,(src,c) in enumerate(desc):
            out[i][n+j]=out[n+j][i]=P[i][n+src] if src is not None else c*P[i][z]
        out[i][z]=out[z][i]=P[i][z]
    for i,(u,c) in enumerate(desc):
        iu=n+u if u is not None else z
        cu=1 if u is not None else c
        for j,(v,e) in enumerate(desc[i:],i):
            iv=n+v if v is not None else z
            cv=1 if v is not None else e
            out[n+i][n+j]=out[n+j][n+i]=cu*cv*M[iu][iv]
        out[n+i][z]=out[z][n+i]=cu*M[iu][z]
    out[z][z]=M[z][z]
    return tuple(tuple(r) for r in out)

def then(d,e): return tuple(d[j] if j is not None else (None,v) for j,v in e)

def gen(a,k,L,labels,x):
    b=a.bit_length();D=k+k*(k-1)//2+b*L; d=k+k*(k-1)//2
    r=[(i,0) for i in range(D)]; label=labels[x]
    if label>=0:
        r[label]=(None,1); t=k
        for i in range(k):
            for j in range(i+1,k):
                if label==i:r[t]=(None,1)
                elif label==j:r[t]=(None,0)
                t+=1
    for slot in range(L):
        for bit in range(b):
            idx=d+slot*b+bit
            r[idx]=((None,((x+1)>>bit)&1) if slot==L-1 else (idx+b,0))
    return tuple(r)

def word(a,k,L,labels,seq):
    D=k+k*(k-1)//2+a.bit_length()*L
    d=tuple((i,0) for i in range(D))
    for x in seq:d=then(d,gen(a,k,L,labels,x))
    return d

def actthen(A,b,C,c):
    return mm(C,A),tuple(sum((C[i][j]*b[j] for j in range(len(b))),c[i]) for i in range(len(b)))

def packet_moment(H,M):
    N=len(M); out=tuple(tuple(F() for _ in range(N)) for _ in range(N))
    for weight,count,A,b,desc in H:
        out=add(out,scaled(sparse(A,b,desc,M),weight*count))
    return out

def run():
    rng=Random(20261116); checks={'descriptors':0,'mixed_moments':0,'serial_packets':0}
    for a,k,L,labels in ((3,2,2,(-1,0,1)),(5,3,2,(0,1,2,-1,1)),(84,6,2,tuple(i%7-1 for i in range(84)))):
        D=k+k*(k-1)//2+a.bit_length()*L
        for _ in range(25):
            w=tuple(rng.randrange(a) for _ in range(4)); v=tuple(rng.randrange(a) for _ in range(4))
            assert then(word(a,k,L,labels,w),word(a,k,L,labels,v))==word(a,k,L,labels,w+v)
            checks['descriptors']+=1
        for _ in range(25 if a!=84 else 4):
            A=tuple(tuple(F(rng.randrange(-2,3),rng.randrange(1,4)) for j in range(2)) for i in range(2))
            b=tuple(F(rng.randrange(-2,3),3) for i in range(2))
            desc=word(a,k,L,labels,tuple(rng.randrange(a) for _ in range(4)))
            z=2+D+1; U=tuple(tuple(F(rng.randrange(-2,3),3) for j in range(z)) for i in range(3))
            M=mm(trans(U),U)
            assert dense(A,b,desc,M)==sparse(A,b,desc,M)
            checks['mixed_moments']+=1
        if a!=84:
            for _ in range(12):
                def branch():
                    A=tuple(tuple(F(rng.randrange(-2,3),3) for j in range(2)) for i in range(2))
                    b=tuple(F(rng.randrange(-2,3),3) for i in range(2))
                    return (F(rng.randrange(1,4),7),rng.randrange(1,4),A,b,word(a,k,L,labels,(rng.randrange(a),)))
                H=[branch(),branch()];G=[branch(),branch()]
                T=[]
                for q,c,A,b,d in H:
                    for r,e,B,h,f in G:
                        C,t=actthen(A,b,B,h);T.append((q*r,c*e,C,t,then(d,f)))
                z=2+D+1;U=tuple(tuple(F(rng.randrange(-2,3),3) for j in range(z)) for i in range(2));M=mm(trans(U),U)
                assert packet_moment(T,M)==packet_moment(G,packet_moment(H,M))
                checks['serial_packets']+=1
    left=(F(1,2)*1*0+F(1,2)*(-1)*1)
    right=(F(1,2)*1*1+F(1,2)*(-1)*0)
    assert left==F(-1,2) and right==F(1,2)
    return {'result':'PASS','backend':'exact_independent_Fraction_reference','checks':checks,
            'paired_cross_moment':{'pairing_A':str(left),'pairing_B':str(right)},
            'x6':{'D':35,'n':2,'dense_extra_fraction_slots':1400,'descriptor_bits_per_row':6,'descriptor_total_bits':210}}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
