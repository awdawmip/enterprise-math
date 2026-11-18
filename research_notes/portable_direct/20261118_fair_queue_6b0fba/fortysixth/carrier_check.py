"""Labeled edge multiplicities in the zero-sum K4 integer edge box."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import comb
import json


def mult(H, matching, e):
    if sum(matching) or any(abs(t)>2*H for t in matching):
        return 0
    L=2*H+1
    p,q,r=matching
    product_size=(L-abs(p))*(L-abs(q))*(L-abs(r))
    imbalance=(-1)**(H+e) if all(t%2==0 for t in matching) else 0
    return (product_size+imbalance)//2


def shell_counts(H,m):
    L=2*H+1
    K=(L-1)//m
    total=L**3
    for s in range(1,K+1):
        w=L-m*s
        pair_sum=(s-1)*(L**2-L*m*s)+m*m*s*(s*s-1)//6
        total+=6*(L*w*w+w*pair_sum)
    ev=K if m%2==0 else K//2
    parity=(-1)**H*(1+3*ev*(ev+1))
    legal=(L**3+(-1)**H)//2
    tagged=(total+parity)//2
    return legal,tagged,total if m%2 else tagged


def all_solutions(H):
    C=Counter()
    for prefix in product(range(-H,H+1),repeat=5):
        last=-sum(prefix)
        if abs(last)>H:
            continue
        a,b,c,d,e=prefix
        C[(a+last,b+e,c+d,(a+b+c)%2)]+=1
    return C


def modular_vertex_image(m):
    return {tuple((v[i]+v[j])%m for i,j in [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])
            for a,b,c in product(range(m),repeat=3) for v in [(a,b,c,(-a-b-c)%m)]}


def natural_exact_test(m):
    image=modular_vertex_image(m)
    for prefix in product(range(m),repeat=5):
        x=prefix+((-sum(prefix))%m,)
        matching=[x[i]+x[5-i] for i in range(3)]
        pred=all(t%m==0 for t in matching) and (m%2 or sum(x[:3])%2==0)
        assert (x in image)==bool(pred)
    return dict(m=m,total_edge_classes=m**5,image_size=len(image))


def shape(a):
    K=int(1/a)
    positive=lambda v:max(Q(0),1-a*abs(v))
    return sum(positive(i)*positive(j)*positive(i+j)
               for i in range(-K,K+1) for j in range(-K,K+1))


def derivative_at(k,side):
    a=Q(1,k)
    K=k if side=='below' else k-1
    result=Q(0)
    for i in range(-K,K+1):
        for j in range(-K,K+1):
            l=-i-j
            if abs(l)>K:
                continue
            terms=[abs(i),abs(j),abs(l)]
            for v,b,c in [(0,1,2),(1,2,0),(2,0,1)]:
                result-=terms[v]*(1-a*terms[b])*(1-a*terms[c])
    return result


def check():
    small={}
    for H in range(5):
        C=all_solutions(H)
        L=2*H+1
        expected={(p,q,-p-q,e):mult(H,(p,q,-p-q),e)
                  for p,q,e in product(range(-2*H,2*H+1),range(-2*H,2*H+1),(0,1))
                  if mult(H,(p,q,-p-q),e)}
        assert C==expected
        eh=sum((-1)**j*comb(6,j)*comb(6*H-j*L+5,5) for j in range(3) if 6*H-j*L>=0)
        assert sum(C.values())==eh==(11*L**5+5*L**3+4*L)//20
        assert len(C)==(1 if H==0 else 2*(1+3*(2*H)*(2*H+1)))
        snapshots=[]
        for m in range(1,4*H+4):
            true,tagged,natural=shell_counts(H,m)
            assert true==C.get((0,0,0,0),0)
            assert tagged==sum(c for (p,q,r,e),c in C.items() if not (p%m or q%m or e))
            assert natural==sum(c for (p,q,r,e),c in C.items() if not (p%m or q%m) and (m%2 or e==0))
            sig_tag={(p%m,q%m,e) for p,q,r,e in C}
            sig_mod={(p%m,q%m,e if m%2==0 else 0) for p,q,r,e in C}
            assert (len(sig_tag)==len(C))==(H==0 or m>4*H)
            assert (len(sig_mod)==len(C))==(H==0 or m%2==0 and m>4*H)
            assert (tagged==true)==(H==0 or m>2*H)
            assert (natural==true)==(H==0 or m%2==0 and m>2*H)
            if H<m<=2*H:
                assert tagged-true==3*L*(L-m)**2+3*(-1)**H*(m%2==0)
            snapshots.append(dict(m=m,true=true,tagged_false=tagged-true,natural_false=natural-true))
        small[H]=dict(integer_edges=sum(C.values()),attained_residue_classes=len(C),mod_checks=snapshots)
    nat=[natural_exact_test(m) for m in range(1,10)]
    deriv=[]
    for k in range(1,17):
        right,left=derivative_at(k,'above'),derivative_at(k,'below')
        assert right-left==k*k-1
        deriv.append(dict(k=k,left=str(left),right=str(right),jump=str(right-left)))
    shapes={str(a):str(shape(a)) for a in (Q(4,3),Q(3,4),Q(1,2),Q(1,3),Q(1,4),Q(1,10),Q(1,25))}
    assert shape(Q(3,4))==Q(11,8)
    wide=[]
    for H,m in [(50,100),(50,99),(50,51),(100,10),(100,11),(250,100),(25000,25000)]:
        v,t,n=shell_counts(H,m)
        wide.append(dict(H=H,m=m,true=v,parity_retained_accept=t,natural_accept=n))
    print(json.dumps(dict(model='external labeled integer edges, no native task replay',
        small_integer_boxes=small,full_mod_m_images=nat,derivative_jumps=deriv,
        scaling_factors=shapes,large_exact_totals=wide),indent=2,sort_keys=True))


if __name__=='__main__':
    check()
