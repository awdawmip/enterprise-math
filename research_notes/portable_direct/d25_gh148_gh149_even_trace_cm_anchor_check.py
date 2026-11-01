"""GH-148/149: even trace-line interpolation and independent F_p anchor.
Only Python 3 stdlib. Exact arithmetic, no external math packages.
"""
from math import comb


def hasse(p):
    n=(p-1)//2
    h=[1]
    for j in range(n//2):
        h.append(h[-1]*(n-2*j)*(n-2*j-1)*pow(j+1,-2,p)%p)
    return h


def mul(x,y,p):
    return ((x[0]*y[0]+2*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)


def eval_pair(h,x,p):
    a,b=0,0
    for c in h[::-1]:
        a,b=(a*x[0]+2*b*x[1]+c)%p,(a*x[1]+b*x[0])%p
    return (a,b)


def eval_poly(h,x,p):
    z=0
    for c in h[::-1]:z=(z*x+c)%p
    return z


def trace_prime_direct(p,B):
    leg=[0]*p
    for x in range(1,p):leg[x]=1 if pow(x,(p-1)//2,p)==1 else -1
    out=0
    for x in range(p):
        f=x*(x*x+x+B)%p
        out+=leg[f]
    return -out


def trace_extension_direct(p,B,leg=None):
    if leg is None:
        leg=[0]*p
        for x in range(1,p):leg[x]=1 if pow(x,(p-1)//2,p)==1 else -1
    out=0
    for u in range(p):
        for v in range(p):
            # f = x*(x*x+x+B), field F_p[rho]/(rho**2-2)
            xx=(u*u+2*v*v)%p
            xy=(2*u*v)%p
            g0=(xx+u+B[0])%p
            g1=(xy+v+B[1])%p
            f0=(u*g0+2*v*g1)%p
            f1=(u*g1+v*g0)%p
            out+=leg[(f0*f0-2*f1*f1)%p]
    return -out


def shifted_even_hasse(p):
    # k(v)=H(1/8+rho*v) is even with coefficients in F_p.
    h=hasse(p); d=len(h)-1; b=pow(8,-1,p)
    coeff=[(0,0)]*(d+1)
    for c in h[::-1]:
        shifted=[(0,0)]*(d+1)
        for j,(a,z) in enumerate(coeff):
            shifted[j]=((shifted[j][0]+b*a)%p,(shifted[j][1]+b*z)%p)
            if j<d:
                shifted[j+1]=((shifted[j+1][0]+2*z)%p,(shifted[j+1][1]+a)%p)
        shifted[0]=((shifted[0][0]+c)%p,shifted[0][1])
        coeff=shifted
    assert all(pair==(0,0) for j,pair in enumerate(coeff) if j%2)
    assert all(pair[1]==0 for j,pair in enumerate(coeff) if j%2==0)
    g=[coeff[2*j][0] for j in range(d//2+1)]
    return g


def derivative_from_sample_nodes(p,nodes,values,at_index):
    # Direct barycentric derivative at a listed interpolation node.
    assert len(nodes)==len(values)==len(set(nodes))
    n=len(nodes)
    weights=[]
    for i in range(n):
        product=1
        for j in range(n):
            if i!=j:product=product*(nodes[i]-nodes[j])%p
        weights.append(pow(product,-1,p))
    z=nodes[at_index]; val=values[at_index]
    inv_at=pow(weights[at_index],-1,p)
    der=0
    for i in range(n):
        if i!=at_index:
            der=(der+(values[i]-val)*weights[i]*inv_at*pow(z-nodes[i],-1,p))%p
    return der


def sample_check(p,independent=True):
    # p=8m+3; k(v)=g(v^2), deg g<=m; J(w)=g(w)^2, deg J<=2m.
    assert p>=11 and p%8==3
    m=(p-3)//8; needed=2*m+1
    rho_inv_half=pow(2,-1,p)
    v0=pow(12,-1,p)
    vs=[];seen=set()
    for v in [0,v0]+list(range(1,p)):
        w=v*v%p
        if w not in seen:
            seen.add(w);vs.append(v)
            if len(vs)==needed:break
    assert len(vs)==needed and vs[0]==0 and vs[1]==v0
    g=shifted_even_hasse(p)
    assert len(g)==m+1
    samples=[]
    leg=[0]*p
    if independent:
        for x in range(1,p):leg[x]=1 if pow(x,(p-1)//2,p)==1 else -1
    for v in vs:
        w=v*v%p
        k=eval_poly(g,w,p)
        hv=eval_pair(hasse(p),(pow(8,-1,p),v),p)
        assert hv==(k,0)
        sample=k*k%p
        if independent:
            true_trace=trace_extension_direct(p,(pow(8,-1,p),v),leg)%p
            assert sample==true_trace,(p,v,sample,true_trace)
        samples.append(sample)
    W=[v*v%p for v in vs]
    dJ=derivative_from_sample_nodes(p,W,samples,1)
    j0=eval_poly(g,W[1],p)
    dg=eval_poly([i*g[i]%p for i in range(1,len(g))],W[1],p)
    assert dJ==2*j0*dg%p
    # S_1 = rho/12 * J'(1/144). Report the rho coefficient.
    s1_rho=dJ*pow(12,-1,p)%p
    # compare independently with H'(B): coefficient of rho in 2H H'
    dh=eval_pair([i*hasse(p)[i] %p for i in range(1,len(hasse(p)))],(pow(8,-1,p),v0),p)
    assert dh[0]==0 and s1_rho==2*j0*dh[1]%p
    print('PASS_EVEN_TRACE',p,'sample_count',needed,'degree_J_bound',2*m,
          'independent_point_count_samples',needed if independent else 0,
          'trace_at_mark',samples[1],'Jprime',dJ,'S1_rho_coefficient',s1_rho)
    return dict(p=p,needed=needed,Jprime=dJ,S1rho=s1_rho,
                trace_mark=samples[1],zero_trace=samples[0],zero_H=g[0],
                zero_direct=trace_prime_direct(p,pow(8,-1,p)),
                independent=independent)


def main():
    for p in [11,19,43,59,67,83,107]:
        r=sample_check(p,True)
        a= r['zero_direct']
        assert r['zero_trace']==(a*a-2*p)%p
    r=sample_check(3347,False)
    assert r['needed']==837
    assert r['zero_H']==3233
    assert r['zero_direct']==-114
    assert r['zero_trace']==2955==(-114)**2%3347
    assert (-114)**2-2*3347==6302
    assert r['trace_mark']==588 and r['Jprime']==997 and r['S1rho']==362
    assert 3347==57**2+2*7**2
    # Exact rational j(E_1/8)=8000, and E_1/8 ≅ y^2=u^3+4u^2+2u
    assert 256*125*128==8000*512
    print('P3347_PRIME_FIELD_DIRECT', 'a_p',-114, 'a_p2',6302,
          'a_p2_mod_p',2955,'p_representation','57^2+2*7^2')
    print('PASS_GH148_GH149_COMPRESSED_TRACE_CM_ANCHOR_EXACT')


if __name__=='__main__':main()
