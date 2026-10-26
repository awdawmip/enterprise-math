from fractions import Fraction as F
import random, json

def check(P,Q):
    H,Y=len(P),len(P[0]); assert all(x>0 for row in P+Q for x in row)
    ps,qs=sum(map(sum,P)),sum(map(sum,Q))
    p=[[F(x,ps) for x in row] for row in P]
    q=[[F(x,qs) for x in row] for row in Q]
    R=[[p[h][y]/q[h][y] for y in range(Y)] for h in range(H)]
    rs=sorted({r for row in R for r in row})
    cuts=[rs[0]/2]+[(x+y)/2 for x,y in zip(rs,rs[1:])]+[rs[-1]+1]
    K=max(len({tuple(int(x>c) for x in row) for row in R}) for c in cuts)
    face=0; exact=0; multi=0; maxD=0; maxB=0
    for r in rs:
        tied=[h for h in range(H) if r in R[h]]
        multi+=len(tied)>1
        C=sorted({tuple(int(x>r) for x in R[h]) for h in range(H) if h not in tied})
        ci={word:i for i,word in enumerate(C)}
        pair={h:(tuple(int(x>=r) for x in R[h]),tuple(int(x>r) for x in R[h])) for h in tied}
        D=sorted({ab for ab in pair.values() if ab[0] not in ci or ab[1] not in ci})
        di={ab:len(C)+i for i,ab in enumerate(D)}
        maxD=max(maxD,len(D)); maxB=max(maxB,len(C)+len(D))
        assert len(C)+len(D)<=K+max(0,len(D)-1)
        for s in (F(0),F(1,5),F(1,2),F(4,5),F(1)):
            bank=[list(map(F,c)) for c in C]+[[s*a+(1-s)*b for a,b in zip(*ab)] for ab in D]
            w=[]
            for h in range(H):
                if h not in pair:
                    word=tuple(int(x>r) for x in R[h]); out=bank[ci[word]]
                else:
                    a,b=pair[h]
                    if (a,b) in di: out=bank[di[(a,b)]]
                    else: out=[s*bank[ci[a]][y]+(1-s)*bank[ci[b]][y] for y in range(Y)]
                assert all(out[y]==(1 if R[h][y]>r else 0 if R[h][y]<r else s) for y in range(Y))
                w.append(out)
            alpha=sum(p[h][y]*w[h][y] for h in range(H) for y in range(Y))
            beta=sum(q[h][y]*w[h][y] for h in range(H) for y in range(Y))
            support=sum(max(p[h][y]-r*q[h][y],0) for h in range(H) for y in range(Y))
            Qr=sum(q[h][y] for h in range(H) for y in range(Y) if R[h][y]==r)
            tie=sum(q[h][y]*w[h][y] for h in range(H) for y in range(Y) if R[h][y]==r)
            assert alpha-r*beta==support and tie==s*Qr
            exact+=1
        face+=1
    return K,H,maxD,maxB,face,exact,multi

rng=random.Random(202610270730)
example_P=[[1,3,5],[2,3,7],[2,3,7],[8,4,9]]
example_Q=[[1,1,1] for _ in range(4)]
assert check(example_P,example_Q)[:4]==(3,4,1,3)
count=dict(models=0,structured=0,random=0,faces=0,exact=0,cross_faces=0,bank_equality=0,nontrivial=0,maxD=0)
for j in range(900):
    Y=rng.choice((2,3,4)) if j<350 else rng.randint(2,4)
    if j<350:
        groups=rng.randint(2,4);H=rng.randint(groups+1,groups+5)
        ratios=[[50*g+rng.randint(1,15) for _ in range(Y)] for g in range(groups)]
        assignments=list(range(groups))+[rng.randrange(groups) for _ in range(H-groups)]
        rng.shuffle(assignments)
        Q=[[rng.randint(1,5) for _ in range(Y)] for _ in range(H)]
        P=[[Q[h][y]*ratios[assignments[h]][y] for y in range(Y)] for h in range(H)]
    else:
        H=rng.randint(3,8)
        Q=[[rng.randint(1,5) for _ in range(Y)] for _ in range(H)]
        P=[[Q[h][y]*rng.randint(1,7) for y in range(Y)] for h in range(H)]
    K,H,d,b,faces,exact,multi=check(P,Q)
    count['models']+=1;count['structured']+=j<350;count['random']+=j>=350
    count['faces']+=faces;count['exact']+=exact;count['cross_faces']+=multi
    count['bank_equality']+=d<=1;count['nontrivial']+=(d<=1 and K<H and multi>0)
    count['maxD']=max(count['maxD'],d)
print(json.dumps({'status':'PASS','example':check(example_P,example_Q),'counts':count},sort_keys=True))
