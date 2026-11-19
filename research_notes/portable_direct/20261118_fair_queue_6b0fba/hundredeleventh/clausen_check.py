"""Block matrix factorials for the inert Clausen digit. Requires python-flint 0.9."""
from hashlib import sha256
from math import comb, isqrt
import json
from flint import fmpz_mod_poly_ctx


def polynomial_product(left, right, zero):
    n = len(left)
    result = [[zero for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j, a in enumerate(left[i]):
            if not a:
                continue
            for k, b in enumerate(right[j]):
                if b:
                    result[i][k] = result[i][k] + a*b
    return result


def direct_sum_vector(matrix, vector, modulus):
    return [sum(a*b for a,b in zip(row,vector)) % modulus for row in matrix]


def advance(matrix, start, end, vector, modulus, ledger):
    """Apply C(end-1)...C(start). Every polynomial remainder divisor is monic."""
    length = end-start
    if not length:
        return vector
    width = isqrt(length)
    groups, tail = divmod(length,width)
    ring = fmpz_mod_poly_ctx(modulus)
    X = ring.gen()
    zero = ring.zero()
    def block(i,j):
        if j == i+1:
            return [[ring(a) for a in row] for row in matrix(X+i)]
        k=(i+j)//2
        return polynomial_product(block(k,j),block(i,k),zero)
    polynomial=block(0,width)
    points=[start+g*width for g in range(groups)]
    def tree(lo,hi):
        if hi==lo+1:
            return (X-points[lo],None,None,lo)
        mid=(lo+hi)//2
        u,v=tree(lo,mid),tree(mid,hi)
        return (u[0]*v[0],u,v,None)
    factors=tree(0,groups)
    def eval_nodes(f,node,output):
        modulus_poly,left,right,index=node
        reduced=f % modulus_poly
        if index is not None:
            output[index]=int(reduced[0])
        else:
            eval_nodes(reduced,left,output)
            eval_nodes(reduced,right,output)
    dim=len(vector)
    blocks=[[[0]*dim for i in range(dim)] for g in points]
    degree=0
    for i,row in enumerate(polynomial):
        for j,value in enumerate(row):
            if value:
                degree=max(degree,value.degree())
                result=[0]*groups
                eval_nodes(value,factors,result)
                for g,z in enumerate(result):
                    blocks[g][i][j]=z
    for b in blocks:
        vector=direct_sum_vector(b,vector,modulus)
    for k in range(end-tail,end):
        vector=direct_sum_vector(matrix(k),vector,modulus)
    ledger.append([length,width,groups,tail,dim,degree])
    return vector


def W_and_E(x):
    # Common denominator 108*(k+1)^3. State is (w, W, e, E, denominator).
    d=108*(x+1)**3
    w=3*(2*x+1)*(3*x+1)*(3*x+2)
    e=-4*(3*x+1)**3
    u=6*x+7
    return [[w,0,0,0,0],[u*w,d,0,0,0],[0,0,e,0,0],[0,0,u*e,d,0],[0,0,0,0,d]]


def legendre(x):
    d=x+1
    return [[2*x+1,-2*x,0],[d,0,0],[0,0,d]]


def curvature(k,ur):
    d=4*(k+1)**3
    c=-(2*k+1)
    b=-c*(k*(k+1)-ur)
    u=6*k+7
    return [[b,0,0,0,0],[c,b,0,0,0],[0,c,b,0,0],[0,u*c,u*b,d,0],[0,0,0,0,d]]


def normalized(vector,modulus):
    inverse=pow(vector[-1],-1,modulus)
    return [v*inverse%modulus for v in vector[:-1]]


def read_A(n,vec,modulus):
    d,prev=normalized(vec,modulus)
    return pow(2,-n,modulus)*d*((6*n+1)*d-12*n*prev)%modulus


def block_values(p):
    r,H,M=(p-2)//3,p//2,(2*p-1)//3
    s=H-1
    mod=p**3
    ledger=[]
    v=[1,0,1]
    v=advance(legendre,0,r,v,mod,ledger)
    Ar=read_A(r,v,mod)
    v=advance(legendre,r,M,v,mod,ledger)
    AM=read_A(M,v,mod)
    L=((4*p+2)*Ar+(1-p)*AM)*pow(3*(p+1),-1,mod)%mod
    v=advance(lambda k:curvature(k,r*(r+1)%p),0,H,[1,0,0,0,1],p,ledger)
    R=normalized(v,p)[3]
    interpolated_W=(L-p*p*2*R*pow(81,-1,p))%mod

    v=[1,1,1,1,1]
    v=advance(W_and_E,0,s-1,v,mod,ledger)
    prefix=normalized(v,mod)[1]
    v=advance(W_and_E,s-1,s,v,mod,ledger)
    ws,through_s,_,_=normalized(v,mod)
    v=advance(W_and_E,s,M,v,mod,ledger)
    _,W,_,E=normalized(v,mod)
    # The products of (H+j)/j, 1<=j<=H, yield binom(2H,H).
    v=advance(lambda k:[[H+k+1,0],[0,k+1]],0,H,[1,1],mod,ledger)
    center=v[0]*pow(v[1],-1,mod)%mod
    U=pow(216,H-1,mod)*pow(H*center,-1,mod)%mod
    left=U*prefix%mod
    ws=(6*s+1)*ws%mod
    source=U*ws%mod
    target=-U*(p+W-through_s)%mod
    assert target%p==0 and (p==5 or source%p==0) and (through_s-prefix-ws)%mod==0
    B=(left+source-target)%mod
    assert W==interpolated_W and E==(mod-2*p)%mod
    assert B==U*(W+p)%mod and B==U*pow(2,-1,mod)*(2*W-E)%mod
    assert (2*W-E)%(p*p)==0 and B%(p*p)==0
    if p%24 in (17,23):
        assert U%p==pow(108,-1,p) and B==pow(216,-1,mod)*(2*W-E)%mod
    return dict(p=p,Ar=Ar,AM=AM,L=L,R=R,W=W,E=E,U=U,
                left=left,source=source,T_H=target//p,B=B,digit=B//(p*p),
                shifted_T_H_digit=(B//(p*p)-1)%p,blocks=ledger)


def raw_oracles(p):
    """Separate integer-binomial source, scalar backwards recurrence, and Lagrange weights."""
    H,r,M=p//2,(p-2)//3,(2*p-1)//3
    s=H-1
    mod=p**3
    def f(k):
        return (6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,mod)%mod
    weighted=[f(k) for k in range(M+1)]
    W=sum(weighted)%mod
    p2=p*p
    prefix=[0]
    for x in weighted:
        prefix.append((prefix[-1]+x)%mod)
    g=1; total=4
    chi=1 if pow(6,H,p)==1 else -1
    for j in range(1,(p+1)//6):
        g=g*9*(2*j-1)**3*pow(j*(36*j*j-1),-1,p)%p
        total=(total+4*(3*j+1)*g)%p
        n=H-j
        value=prefix[n]
        assert value%p==0 and value//p%p==(-1-chi*total)%p
        if j==2:
            den=n*(2*n+1)*comb(2*n,n)
            a_n=pow(216,n-1,p2)*value*pow(den,-1,p2)%p2
            assert a_n%p==0 and a_n//p!=0
    E=0
    term=1
    for k in range(M+1):
        E=(E+(6*k+1)*term)%mod
        term=-term*(3*k+1)**3*pow(27*(k+1)**3,-1,mod)%mod
    U=pow(216,H-1,mod)*pow(H*comb(2*H,H),-1,mod)%mod
    def source(n):
        return (6*n+1)*comb(2*n-1,n)*(comb(3*n,n)//(2*n+1))
    p2=p*p
    t=-pow(216,p-1,p2)*pow((2*p+1)*comb(2*p,p),-1,p2)%p2
    for n in range(p-1,H-1,-1):
        t=((2*n+3)*t-source(n))*pow(108*n,-1,p2)%p2
    a_s=(pow(216,s-1,mod)*sum(weighted[:s])*pow(s*(2*s+1)*comb(2*s,s),-1,mod))%mod
    left=108*s*a_s%mod
    B=(left+source(s)-p*t)%mod
    shifted=(left+source(s)-p*((t+p)%p2))%mod
    assert (B-shifted)%mod==p*p
    vals=[]
    old,cur=0,1
    for n in range(M+1):
        vals.append(pow(2,-n,mod)*cur*((6*n+1)*cur-12*n*old)%mod)
        old,cur=cur,((2*n+1)*cur-2*n*old)*pow(n+1,-1,mod)%mod
    R=-162*vals[r]
    for j in range(H+1):
        if j==r:continue
        z=pow(r*(r+1)-j*(j+1),-1,p)
        weight=-(z*z-9*z)
        if j==H:weight*=pow(2,-1,p)
        R+=weight*vals[j]
    return dict(Ar=vals[r],AM=vals[M],R=R%p,W=W,E=E,U=U,left=left,
                source=source(s)%mod,T_H=t,B=B,digit=B//p2,shifted_T_H_digit=shifted//p2)


def integer_product(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def prefix_tree(matrix, initial, requests):
    """All prefix products [0,n) applied to a common vector at the requested moduli."""
    sites={}
    for n,p,mod in requests:
        sites.setdefault(n,{})[p]=mod
    def upwards(lo,hi):
        if hi==lo+1:
            m=1
            for mod in sites.get(lo,{}).values():
                m*=mod
            return (matrix(lo),m,None,None,lo)
        mid=(lo+hi)//2
        l,r=upwards(lo,mid),upwards(mid,hi)
        return integer_product(r[0],l[0]),r[1]*l[1],l,r,None
    found={}
    def descend(node,vector):
        _,m,l,r,index=node
        if m==1:
            return
        if index is not None:
            for p,mod in sites[index].items():
                found[index,p]=[a%mod for a in vector]
            return
        descend(l,[v%l[1] for v in vector])
        if r[1]>1:
            small=[[a%r[1] for a in row] for row in l[0]]
            descend(r,direct_sum_vector(small,vector,r[1]))
    root=upwards(0,max(sites)+1)
    descend(root,initial)
    return found


def fixed_curvature(k):
    d=36*(k+1)**3
    c=-9*(2*k+1)
    b=(2*k+1)*(9*k*(k+1)+2)
    u=6*k+7
    return [[b,0,0,0,0],[c,b,0,0,0],[0,c,b,0,0],[0,u*c,u*b,d,0],[0,0,0,0,d]]


def batch_values(primes,reference):
    def req(positions,a):
        return [(n,p,p**a) for p in primes for n in positions(p)]
    lm=prefix_tree(legendre,[1,0,1],req(lambda p:((p-2)//3,(2*p-1)//3),3))
    ws=prefix_tree(W_and_E,[1,1,1,1,1],req(lambda p:(p//2-2,p//2-1,(2*p-1)//3),3))
    hs=prefix_tree(fixed_curvature,[1,0,0,0,1],req(lambda p:(p//2,),1))
    fac=prefix_tree(lambda k:[[k+1]],[1],req(lambda p:(p//2,p-1),3))
    totals={}
    for p in primes:
        mod=p**3
        H=p//2; r=(p-2)//3; M=(2*p-1)//3; s=H-1
        ar=read_A(r,lm[r,p],mod)
        am=read_A(M,lm[M,p],mod)
        R=normalized(hs[H,p],p)[3]
        U=pow(216,H-1,mod)*fac[H,p][0]**2*pow(H*fac[p-1,p][0],-1,mod)%mod
        before=normalized(ws[s-1,p],mod)[1]
        full=normalized(ws[s,p],mod)[1]
        _,w,_,e=normalized(ws[M,p],mod)
        left=U*before%mod; source=U*(full-before)%mod
        target=-U*(p+w-full)%mod
        B=(left+source-target)%mod
        results=dict(Ar=ar,AM=am,R=R,W=w,E=e,U=U,left=left,source=source,T_H=target//p,B=B)
        assert target%p==0 and all(reference[p][k]==v for k,v in results.items())
        totals[p]=results
    return {"prime_count":len(primes),"modular_prefix_outputs":sum(map(len,(lm,ws,hs,fac))),
            "all_channels_sha256":sha256(json.dumps(totals,sort_keys=True).encode()).hexdigest()}


def lost_jet_control(p):
    r=(p-2)//3
    state=[1,0,0,0,1]
    at_root=None
    for k in range(p//2):
        matrix=curvature(k,r*(r+1))
        if k==r:
            at_root=normalized(direct_sum_vector(matrix,state,p),p)
            matrix[1][0]=matrix[2][1]=matrix[3][1]=0
        state=direct_sum_vector(matrix,state,p)
    return {"true_after_root":at_root,"wrong_curvature":normalized(state,p)[3]}


def neighbor_divided(p):
    n=p//2-2
    modulus=p*p
    weighted=sum((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,modulus) for k in range(n))
    denom=n*(2*n+1)*comb(2*n,n)
    value=pow(216,n-1,modulus)*weighted*pow(denom,-1,modulus)%modulus
    assert value%p==0 and value!=0
    return value//p


def third_exception(p):
    assert all(p%d for d in range(2,isqrt(p)+1))
    n=p//2-3; modulus=p**3; ledger=[]
    v=advance(W_and_E,0,n-1,[1,1,1,1,1],modulus,ledger)
    prefix=normalized(v,modulus)[1]
    v=advance(lambda k:[[n+k+1,0],[0,k+1]],0,n,[1,1],modulus,ledger)
    binomial=v[0]*pow(v[1],-1,modulus)%modulus
    a=pow(216,n-1,modulus)*prefix*pow(n*(2*n+1)*binomial,-1,modulus)%modulus
    assert a%(p*p)==0 and a!=0
    return a//(p*p)


def main():
    samples=[]
    reference={}
    offset_counts=0
    bounds=[p for p in range(5,1251,6) if all(p%d for d in range(2,isqrt(p)+1))]
    digest=sha256()
    for p in bounds:
        row=block_values(p)
        reference[p]=row
        offset_counts+=(p+1)//6-1
        independent=raw_oracles(p)
        assert all(row[k]==v for k,v in independent.items()),p
        digest.update(json.dumps([p,independent],sort_keys=True).encode()+b'\n')
        if p>7:
            numer,denom={5:(319,3780),11:(-83,1260),17:(83,1260),23:(-319,3780)}[p%24]
            assert row['left']%p==0 and row['left']//p%p==numer*pow(denom,-1,p)%p
            assert (row['left']%(p*p)==0)==(p in (29,83)) and row['left']!=0
        if p in (5,17,23,29,83,311,1229):
            small=dict(row)
            small.pop('blocks')
            samples.append(small)
    # At the interior root, a vanishing constant coefficient must not zero the jet.
    assert all((r:=((p-2)//3)) < p//2 and (2*r+1)%p for p in bounds)
    assert all(10007%d for d in range(2,isqrt(10007)+1))
    large=block_values(10007)
    # Linear-time, small-coefficient direct recurrences check the larger sample too.
    mod=10007**3; vec=[1,1,1,1,1]
    for k in range((2*10007-1)//3):
        vec=direct_sum_vector(W_and_E(k),vec,mod)
    _,w,_,e=normalized(vec,mod)
    assert (w,e)==(large['W'],large['E'])
    faults={p:lost_jet_control(p) for p in (17,23,311)}
    assert all(f["wrong_curvature"]!=reference[p]["R"] for p,f in faults.items())
    print(json.dumps(dict(singular_factor_negative_control=faults,composite_ring='prime powers p^3, monic remainder tree',
          old_domain_bound=1250,all_prime_count=len(bounds),
          target_prime_count=sum(p%24 in (17,23) for p in bounds),
          verified_positive_offsets=offset_counts,
          third_offset_divided_twice={p:third_exception(p) for p in (149,71987)},
          neighbor_divided_samples={p:neighbor_divided(p) for p in (17,23,29,83)},
          exceptional_divided_left={p:reference[p]['left']//p for p in (29,83)},
          simultaneous_tree=batch_values(bounds,reference),
          exact_integer_reference_sha256=digest.hexdigest(),samples=samples,
          larger_direct_W_E_control=large),sort_keys=True,indent=2))


if __name__=='__main__':
    main()
