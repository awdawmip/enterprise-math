"""EC49CI independent replay: actual signed-X6 BRC + n8 literal minor certificate."""
import base64,json,zlib
from fractions import Fraction
from native_signed_brc import endpoint_weight,endpoint_multiplicity
E=(0,)*6
S={'s1':(-1,-1),'s2':(-2,-2),'sA':(1,2,-1,-2),'sB':(2,1,-2,-1)}
S2={a+'>'+b:p+q for a,p in S.items() for b,q in S.items()}
S12={**S,**S2}
W=((2,3,3,2,1,1),(3,2,3,2,1,1))
P=1000003
def dz(word):
    z=[0]*6
    for a in word:z[abs(a)-1]+=1 if a>0 else -1
    return tuple(z)
def inv(z):return tuple(-x for x in z)
def sub(q,a,b,c):
    return 2 if q==2 or (q==1 and a==c) else int(a==b)
def advance(q,a):
    qa,qb=divmod(q,3)
    return 3*sub(qa,a,1,2)+sub(qb,a,2,1)
def end(q,w):
    for a in w:q=advance(q,a)
    return q
def atom(q):return 2*int(q//3==2)+int(q%3==2)
def weights(w):
    out=[1,1,1]
    for a in w:
        if a>0:
            for c in range(2):out[c]*=W[c][a-1]
    return tuple(out)
def column(word,suffixes):
    z=dz(word);q=end(0,word);v=weights(word)
    out=[]
    for s in suffixes.values():
        active=(z==inv(dz(s)))
        k=atom(end(q,s))
        w=weights(s)
        for j in range(4):
            out.extend(v[c]*w[c] if active and j==k else 0 for c in range(3))
    return out
def determinant_mod(matrix):
    a=[[x%P for x in row] for row in matrix]
    n=len(a);det=1
    for k in range(n):
        p=next((i for i in range(k,n) if a[i][k]),None)
        if p is None:return 0
        if k!=p:a[k],a[p]=a[p],a[k];det=-det
        t=a[k][k];det=det*t%P;iv=pow(t,-1,P)
        for i in range(k+1,n):
            if a[i][k]:
                f=a[i][k]*iv%P
                for j in range(k+1,n):a[i][j]=(a[i][j]-f*a[k][j])%P
                a[i][k]=0
    return det%P
def rational_rank(rows):
    if not rows:return 0
    a=[[Fraction(x) for x in row] for row in rows];r=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][col]),None)
        if pivot is None:continue
        a[pivot],a[r]=a[r],a[pivot]
        d=a[r][col]
        for j in range(col,len(a[0])):a[r][j]/=d
        for i in range(r+1,len(a)):
            f=a[i][col]
            if f:
                for j in range(col,len(a[0])):a[i][j]-=f*a[r][j]
        r+=1
        if r==len(a):break
    return r
def fiber_rank(suffixes):
    out={}
    for d in sorted({inv(dz(s)) for s in suffixes.values()}):
        rows=[]
        for s in suffixes.values():
            if inv(dz(s))!=d:continue
            lookup=[atom(end(q,s)) for q in range(9)]
            for j in range(4):rows.append([int(k==j) for k in lookup])
        out[str(d)]=rational_rank(rows)
    return out
D2={inv(dz(s)) for s in S2.values()}
def dp_return(n):
    state={(E,0):(1,1,1)}
    for depth in range(n):
        rem=n-depth-1;out={}
        for (z,q),v in state.items():
            for a in range(1,7):
                for sign in (1,-1):
                    step=sign*a; zz=list(z);zz[a-1]+=sign;zz=tuple(zz)
                    if not any(sum(abs(x-y) for x,y in zip(zz,d))<=rem and
                               (rem-sum(abs(x-y) for x,y in zip(zz,d)))%2==0
                               for d in D2):continue
                    key=(zz,advance(q,step));old=out.get(key,(0,0,0))
                    w=W[0][a-1] if sign>0 else 1
                    v1=W[1][a-1] if sign>0 else 1
                    out[key]=(old[0]+v[0]*w,old[1]+v[1]*v1,old[2]+v[2])
        state=out
    for s in S12.values():
        d=inv(dz(s));sw=weights(s)
        got=tuple(sum(v[c] for (z,q),v in state.items() if z==d)*sw[c]
                  for c in range(3))
        expect=(int(endpoint_weight(n,d,W[0],(1,)*6))*sw[0],
                int(endpoint_weight(n,d,W[1],(1,)*6))*sw[1],
                endpoint_multiplicity(n,d))
        assert got==expect,(n,s,got,expect)
    return len(state)
def main():
    assert list(fiber_rank(S2).values())==[3,5,4,5,4,4]
    assert list(fiber_rank(S12).values())==[3,6,4,6,4,4]
    cert=json.loads(zlib.decompress(base64.b64decode(open('EC49CI_N8_WITNESS.b64').read())))
    for key,suffixes,rank in [('n8_S2',S2,75),('n8_S_or_S2',S12,81)]:
        entry=cert[key];paths=entry['witness_paths'];inds=entry['selected_rows']
        assert len(paths)==len(inds)==rank and all(len(p)==8 for p in paths)
        cols=[column(path,suffixes) for path in paths]
        det=determinant_mod([[col[i] for col in cols] for i in inds])
        assert det==entry['determinant_mod'] and det!=0
        print(key, 'rank',rank,'determinant mod',P,'=',det)
    for n in (6,8,10):print('native BRC crosscheck n=',n,'terminal typed states',dp_return(n))
    a=(1,)*6;b=(3,)*6;s=S['s1']
    assert all(not any(column(p,S2)) for p in (a,b))
    assert dz(a+s+s+s)==E and dz(b+s+s+s)!=E
    print('PASS: ranks, native totals, and strict non-update witness')
if __name__=='__main__':main()
