"""R33 exact quotient-prefix Farey checker. Python 3 standard library only."""
D=10**24

def step(p,t,k):
    a,q,c,j=p
    if t=='L':a,q=a+k*c,q+k*j
    else:c,j=c+k*a,j+k*q
    assert c*q-a*j==1
    return a,q,c,j

def direction(p,L,U):
    a,q,c,j=p
    x0=q*L-a*D;x1=q*U-a*D
    y0=c*D-j*L;y1=c*D-j*U
    assert min(x0,x1,y0,y1)>0
    if x0>y0 and x1>y1:
        k=min(x0//y0,x1//y1)
        assert k>0 and min(x0-k*y0,x1-k*y1)>0
        return 'L',k
    if x0<y0 and x1<y1:
        k=min(y0//x0,y1//x1)
        assert k>0 and min(y0-k*x0,y1-k*x1)>0
        return 'U',k
    raise ValueError('open enclosure cannot certify next mediant')

def stages(m,N,L,U,jump):
    p=(0,1,1,1);calls=0
    while p[1]+p[3]<=m:
        if jump:
            t,k=direction(p,L,U)
            h=p[3] if t=='L' else p[1]
            k=min(k,(m-p[1]-p[3])//h+1)
        else:
            a,q,c,j=p
            assert (a+c)*D<(q+j)*L or (a+c)*D>(q+j)*U
            t='L' if (a+c)*D<(q+j)*L else 'U';k=1
        p=step(p,t,k);calls+=1
    ans=[(m,min(p[1]+p[3],N),*p)]
    while ans[-1][1]<N:
        e=p[1]+p[3]
        if jump:
            t,k=direction(p,L,U)
            h=p[3] if t=='L' else p[1]
            k=min(k,(N-e-1)//h+1)
        else:
            a,q,c,j=p
            assert (a+c)*D<(q+j)*L or (a+c)*D>(q+j)*U
            t='L' if (a+c)*D<(q+j)*L else 'U';h=p[3] if t=='L' else p[1];k=1
        for s in range(1,k+1):
            v=step(p,t,s)
            ans.append((e+(s-1)*h+1,min(e+s*h,N),*v))
        p=step(p,t,k);calls+=1
    return ans,calls

def test(label,m,N,L,U):
    a,ca=stages(m,N,L,U,True)
    b,cb=stages(m,N,L,U,False)
    assert a==b
    print(label,'stages',len(a),'jump_decisions',ca,'one_step_comparisons',cb)
    return a,ca,cb

if __name__=='__main__':
    L=262204504569236716045286;U=L+1
    data,decisions,base=test('S23/AV',128,10**12+128,L,U)
    assert len(data)==78 and decisions==28 and base==88
    blocks=0;positive=0
    for n0,n1,a,q,c,j in data:
        if n1<=389:continue
        t=q+j;parts=[]
        for x,y in ((t-163,t-97),(t-60,t)):
            if max(x,n0)<=min(y,n1):parts.append((max(x,n0),min(y,n1)))
        if not parts:continue
        xlo=q*L-a*D;xhi=q*U-a*D;vlo=c*D-j*U;vhi=c*D-j*L
        assert xhi<vlo or vhi<xlo
        blocks+=len(parts);positive+=1
    assert blocks==148 and positive==74
    print('S23/AV positive phases',positive,'blocks',blocks)
    test('sqrt2-minus-one',8,10000,414213562373095048801688,414213562373095048801689)
    t=D//20001
    _,x,y=test('large-partial-quotient',8,20000,t,t+1)
    assert x==2 and y==19998
    print('PASS_R33_PORTABLE_EXACT_QUOTIENT_PREFIX_AND_148_BLOCKS')
