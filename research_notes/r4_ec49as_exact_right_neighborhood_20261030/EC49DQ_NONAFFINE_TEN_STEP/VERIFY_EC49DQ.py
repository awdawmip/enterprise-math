#!/usr/bin/env python3
"""EC49DP: exact signed-X6 affine-BRC universal witness; Python stdlib only.
All paths are genuine ordered signed steps and are generated, not assumed.
"""
import itertools, json

TARGET=(-2,0,0,0,0,0)
GROUPS=((1,0,0,0,0,0),(0,1,0,0,0,0),(0,0,1,0,0,0),
        (0,0,0,1,0,0),(0,1,0,0,1,0),(0,0,1,0,0,1))
OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),
     'd':(2,1,-2,-1),'e':(3,1,1,-3)}

def observe(word):
    A=B=0; last=0; loc=[0]*6; counts=[0]*6
    for s in word:
        assert 1<=abs(s)<=6
        loc[abs(s)-1]+=1 if s>0 else -1
        if s>0:counts[s-1]+=1
        A=int(A or (last==1 and s==2))
        B=int(B or (last==2 and s==1))
        last=s if s in (1,2) else 0
    z=(int(not A and not B),int(not A and B),int(A and not B),
       int(A and B),int(not A and last==1),int(not B and last==2))
    return tuple(loc),tuple(counts),z,(A,B)

def select(pos,z):
    neg=tuple(v+(2 if j==0 else 0) for j,v in enumerate(pos))
    states={(pos,neg,0,0,0):()}
    for _ in range(2*sum(pos)+2):
        following={}
        for (p,q,A,B,L),hist in states.items():
            for j in range(len(pos)):
                for s in (j+1,-j-1):
                    pp,qq=list(p),list(q)
                    if s>0:
                        if not pp[j]:continue
                        pp[j]-=1
                    else:
                        if not qq[j]:continue
                        qq[j]-=1
                    a=int(A or (L==1 and s==2))
                    b=int(B or (L==2 and s==1))
                    last=s if s in (1,2) else 0
                    following.setdefault((tuple(pp),tuple(qq),a,b,last),hist+(s,))
        states=following
    return min((w for w in states.values() if observe(w)[2]==z),default=None)

def histories(case):
    out=[]
    for z in GROUPS:
        for j in range(3):
            if case=='A':w=select((j+1,3-j),z)
            else:
                w=next((w for p in range(6-j)
                        if (w:=select((p,5-j-p,j),z)) is not None),None)
            assert w is not None,(case,z,j)
            loc,pos,found,_=observe(w)
            assert loc==TARGET and found==z and len(w)==(10 if case=='A' else 12)
            assert (pos[0]==j+1 if case=='A' else pos[2]==j)
            out.append(w)
    return out

def weight(word,x):
    a=1
    for s in word:
        if s>0:a*=x[s-1]
    return a

def rank_mod(rows,p):
    basis={}
    for row in rows:
        a=[v%p for v in row]
        for j,b in sorted(basis.items()):
            c=a[j]
            if c:a=[(v-c*w)%p for v,w in zip(a,b)]
        j=next((j for j,v in enumerate(a) if v),None)
        if j is not None:
            c=pow(a[j],-1,p);basis[j]=[(v*c)%p for v in a]
    return len(basis)

def det_exact(rows):
    M=[list(r) for r in rows];n=len(M); sign=1; old=1
    for k in range(n-1):
        if not M[k][k]:
            j=next((j for j in range(k+1,n) if M[j][k]),None)
            if j is None:return 0
            M[j],M[k]=M[k],M[j];sign=-sign
        pivot=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                a=M[i][j]*pivot-M[i][k]*M[k][j]
                assert a%old==0
                M[i][j]=a//old
            M[i][k]=0
        old=pivot
    return sign*M[-1][-1]

def return_words(h):
    out=[]
    for seq in itertools.product(OPS,repeat=h):
        w=tuple(s for op in seq for s in OPS[op]);loc=[0]*6
        for s in w:loc[abs(s)-1]+=1 if s>0 else -1
        if tuple(loc)==(2,0,0,0,0,0):out.append(w)
    return out

def direct_rank(paths,x,y,hs):
    fut=[w for h in hs for w in return_words(h)]
    rows=[]
    for history in paths:
        row=[]
        for wt in (x,y,None):
            for f in fut:
                label=observe(history+f)[3]
                fac=weight(history+f,wt) if wt else 1
                row.extend(fac*int(label==tag) for tag in ((0,0),(0,1),(1,0),(1,1)))
        rows.append(row)
    return (len(fut),rank_mod(rows,1000003),rank_mod(rows,1000033))

def triple_det(m):
    return (m[0][0]*(m[1][1]-m[2][1]) + m[1][0]*(m[2][1]-m[0][1]) + m[2][0]*(m[0][1]-m[1][1]))

def check(paths,x,y,gate,label):
    assert len(paths)==18 and all(len(w)==10 for w in paths)
    rows=[]
    for w in paths:
        loc,pos,z,_=observe(w)
        assert loc==TARGET and sum(pos)==4
        rows.append(tuple(weight(w,x)*f for f in z)+tuple(weight(w,y)*f for f in z)+z)
    exact=det_exact(rows)
    assert exact==-gate**6 and gate != 0,(label,exact,gate)
    assert rank_mod(rows,1000003)==rank_mod(rows,1000033)==18
    checks={k:direct_rank(paths,x,y,hs) for k,hs in [('h2',[2]),('h3',[3]),('cumulative',[1,2]),('h4',[4]),('h5',[5])]}
    for k,v in checks.items():assert v[1:]==((15,15) if k in ('h2','h4') else (18,18)),(label,k,v)
    return {'case':label,'x':x,'y':y,'gate':str(gate),'det18':str(exact),'verified_original_histories':len(paths),'return_word_rank_checks':checks,'witnesses':[list(w) for w in paths]}

def run():
    out=[]
    # Type I: three non-collinear geometric points from E1/E2 count variation
    x=(2,3,5,2,4,6);y=(3,5,8,7,2,11)
    u,v=x[:2];U,V=y[:2]
    gate=-u*v*U*V*(u-v)*(U-V)*(u*V-v*U)
    assert gate==-180
    out.append(check(histories('A'),x,y,gate,'I_first_two_multiplicative_distinct'))
    # Type II: E1 and E2 may be exactly equal, but three spare-axis points are noncollinear
    # A=B historical label and both history ports survive for all 3 choices of spare axis.
    for label,x,y in [
       ('II_x1_x2_y1_y2_equal', (2,2,1,2,4,5),(3,3,1,4,2,7)),
       ('II_first_two_proportional', (2,3,1,2,4,5),(4,6,1,4,2,7))]:
        axes=(2,3,4)
        co=[[x[q],y[q],1] for q in axes]
        geom=triple_det(co)
        gate=x[0]**2*x[1]*y[0]**2*y[1]*geom
        paths=[]
        for z in GROUPS:
            for q in axes:
                pos=[0]*6;pos[0]=2;pos[1]=1;pos[q]=1
                w=select(tuple(pos),z)
                assert w is not None,(label,z,q)
                assert observe(w)[2]==z
                paths.append(w)
        d=check(paths,x,y,gate,label)
        d['spare_axis_det']=str(geom)
        out.append(d)
    print(json.dumps({'status':'PASS','source_basis':'EC49DP_PORTABLE witness generator at 0fa60548','precision':'exact integer determinants and ranks modulo 1000003 and 1000033','results':out},ensure_ascii=False,sort_keys=True))

if __name__=='__main__':run()
