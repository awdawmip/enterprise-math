"""GH-150 exact black-box square-trace observer ambiguity witness.
Witnesses are formal polynomials, NOT elliptic curves or independent point counts.
"""

def h0(p):
    n=(p-1)//2; h=[1]
    for j in range(n//2):
        h.append(h[-1]*(n-2*j)*(n-2*j-1)*pow(j+1,-2,p)%p)
    x=pow(8,-1,p);r=0
    for z in h[::-1]:r=(r*x+z)%p
    return r


def prod_differences(p,x,nodes):
    r=1
    for y in nodes:r=r*(x-y)%p
    return r


def witness(p):
    assert p>=11 and p%8==3
    m=(p-3)//8;w0=pow(144,-1,p);g0=h0(p)
    assert g0!=0
    nodes=[0,w0];seen=set(nodes)
    for v in range(1,p):
        w=v*v%p
        if w not in seen:
            seen.add(w);nodes.append(w)
        if len(nodes)==2*m:break
    assert len(nodes)==2*m
    A=nodes[:m];B=nodes[m:]
    assert 0 in A and w0 in (A+B)
    Q0=prod_differences(p,0,B)
    assert Q0!=0
    c=g0*pow(Q0,-1,p)%p
    for w in nodes:
        P=prod_differences(p,w,A)
        Q=prod_differences(p,w,B)
        G=c*(P+Q)%p;Gt=c*(Q-P)%p
        assert G*G%p==Gt*Gt%p
        if w==0: assert G==Gt==g0
    if w0 in A:
        Ap=prod_differences(p,w0,[a for a in A if a!=w0])
        B0=prod_differences(p,w0,B)
        difference=4*c*c*Ap*B0%p
    else:
        A0=prod_differences(p,w0,A)
        Bp=prod_differences(p,w0,[b for b in B if b!=w0])
        difference=4*c*c*A0*Bp%p
    assert difference!=0
    print('PASS_GH150_BLACK_BOX_WITNESS','p',p,'degree_G',m,
          'observed_square_class_samples',2*m,'anchor_G0',g0,
          'target_w0',w0,'Jprime_difference',difference)
    return difference

if __name__=='__main__':
    for p in [11,19,43,59,67,83,107,3347]:witness(p)
    print('PASS_GH150_SQUARE_CLASS_JET_NONIDENTIFIABILITY')
