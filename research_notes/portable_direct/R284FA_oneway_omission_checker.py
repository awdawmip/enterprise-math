"""Exact finite checker for R284FA, using only integer Hamming arithmetic."""
from itertools import combinations
import json

def errors(n, budget):
    for k in range(min(n, budget)+1):
        for inds in combinations(range(n), k):
            yield sum(1 << p for p in inds)

def code(u,q):
    v=u+q
    if v==0:
        return (0, 1, 3, 2), ([0],[1],[0],[1])
    p=v+1; r=3*u+q; s=v+1
    A=list(range(p)); B=list(range(p,p+r)); C=list(range(p+r,p+r+s))
    def mask(bits): return sum(1<<j for j in bits)
    tags=(0,mask(B+C),mask(A+C),mask(A+B))
    orders=[]
    for i in range(4):
        others = C if i%2==0 else A
        if u>=1:
            lead=2*u-1
            order=B[:lead]
            for k in range(len(others)):
                order.extend([others[k],B[lead+k]])
        else:
            order=[]
            for k in range(q):
                order.extend([B[k],others[k]])
            order.append(others[-1])
        assert len(order)==(tags[i]^tags[(i+1)%4]).bit_count()
        assert len(set(order))==len(order)
        assert sum(1<<j for j in order)==tags[i]^tags[(i+1)%4]
        orders.append(order)
    return tags,orders

def check(u,q):
    tags, orders=code(u,q)
    n=max(tags).bit_length() if u+q else 2
    v=u+q
    W=list(errors(n,u))
    passes=0; prefixes=0; omission_states=0; no_rollback_pairs=0
    for edge,order in enumerate(orders):
        a=edge; b=(edge+1)%4; X=tags[a]
        for j in range(len(order)+1):
            prefixes+=1
            ideal_dist = [((X^z).bit_count()) for z in tags]
            for idx in range(min(q,j)+1):
                for omit in combinations(order[:j],idx):
                    omission_states+=1
                    P=X ^ sum(1<<k for k in omit)
                    m=(P^tags[a]).bit_count()
                    assert (P^tags[b]).bit_count()==len(order)-m
                    for noise in W:
                        y=P^noise
                        cand=[z for z,c in enumerate(tags) if (y^c).bit_count()<=v]
                        dec=cand[0] if len(cand)==1 else None
                        if dec is not None:
                            assert dec in (a,b),(u,q,edge,j,omit,noise,dec)
                            if dec==a: assert m<=2*u+q
                            if dec==b: assert len(order)-m<=2*u+q
                            if j==0: assert dec==a
                            if j==len(order): assert dec==b
                        else:
                            if j in (0,len(order)):
                                raise AssertionError((u,q,edge,j,'endpoint RETRY'))
                        passes+=1
            if j<len(order): X ^= 1<<order[j]
        # If any two reads yield new then old, m1<=m2 (omissions stay omitted).
        # Such reads require d-m1<=T and m2<=T, hence d<=2T,
        # contradicted by every adjacent code distance d>=2T+1.
        assert len(order)>=2*(2*u+q)+1
        no_rollback_pairs+=1
    A=4*u+2*q+1; B=2*(u+q)+1
    if u+q:
        assert min((tags[i]^tags[(i+1)%4]).bit_count() for i in range(4))>=A
        assert all((tags[i]^tags[(i+2)%4]).bit_count()>=B for i in (0,1))
    assert n==5*u+3*q+2
    assert 4*(n-1)<4*A+2*B<=4*n
    return dict(u=u,q=q,n=n,decoder_checks=passes,omission_states=omission_states,prefixes=prefixes,no_rollback_edges=no_rollback_pairs,endpoint_verified=True)

if __name__=='__main__':
    results=[check(u,q) for u in range(3) for q in range(3)]
    print(json.dumps({'schema':'R284FA_CHECK_V1','verified_domain':{'u':[0,1,2],'q':[0,1,2]},'results':results,'totals':{k:sum(r[k] for r in results) for k in ('decoder_checks','omission_states','prefixes','no_rollback_edges')},'status':'PASS'},ensure_ascii=False,indent=2))
