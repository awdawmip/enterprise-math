from pathlib import Path
from fractions import Fraction as F
# Run compact1156.py as a separate verifier first, then use its data.
exec(Path('compact1156.py').read_text())
_,_,_,population=search(10**16,3*10**84,V1,W1)
records=Path('fiber1156_compact.txt').read_text().splitlines();assert len(records)==82
for signed,offset in [(False,0),(True,41)]:
    assert records[offset]=='signed '+str(signed)
    s=[-a*K/(2*(L*10**16)**2) for a in A];t=[b*H/(2*L*10**16) for b in B]
    cols=U+[s,t] if signed else U
    free=[j for j in range(len(cols)) if j not in piv]
    M=[[F(cols[j][i]) for j in piv]+[F(i==j) for i in range(N)] for i in range(N)]
    for i in range(N):
        j=next(j for j in range(i,N) if M[j][i]);M[i],M[j]=M[j],M[i];x=M[i][i];M[i]=[a/x for a in M[i]]
        for j in range(N):
            if j!=i:
                x=M[j][i];M[j]=[a-x*b for a,b in zip(M[j],M[i])]
    inv=[row[N:] for row in M]
    assert all(dot(row,cols[j])==(i==k) for i,row in enumerate(inv) for k,j in enumerate(piv))
    feasible=excluded=0;slacks=[]
    for (q,p,h),record in zip(population,records[offset+1:offset+41]):
        v=[a*(F(p,q)-r)+b*(F(h,q)-u)-c for a,b,c in zip(A,B,m)]
        if signed:v=[x-y-z for x,y,z in zip(v,s,t)]
        parts=record.split();zz=[F(0)]*len(cols)
        if parts[0]=='X':
            weights=list(map(int,parts[1].split(',')));assert len(weights)==N
            n=[dot(weights,col) for col in zip(*inv)]
            assert abs(dot(n,v))>sum(abs(dot(n,c)) for c in cols);excluded+=1
        else:
            mag=int(parts[0]);signs=parts[1];assert len(signs)==len(free)
            extra=iter(map(int,parts[2].split(',')) if len(parts)>2 else [])
            for j,sign in zip(free,signs):zz[j]=F(mag if sign=='+' else -mag if sign=='-' else next(extra),10**12)
            assert next(extra,None) is None
            target=[x-sum(zz[j]*cols[j][i] for j in free) for i,x in enumerate(v)]
            for j,row in zip(piv,inv):zz[j]=dot(row,target)
            assert all(dot(zz,col)==x for col,x in zip(zip(*cols),v));slack=1-max(map(abs,zz));assert slack>0;slacks.append(slack);feasible+=1
    assert (feasible,excluded)==((40,0) if signed else (36,4));assert min(slacks)>F(6,10000)
    print('PASS compact fibers',signed,feasible,excluded,'min slack',float(min(slacks)))
