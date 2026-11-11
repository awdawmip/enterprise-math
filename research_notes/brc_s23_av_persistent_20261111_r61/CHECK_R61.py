#!/usr/bin/env python3
"""R61 immutable AVL source-time phase index, exact finite checker."""
from dataclasses import dataclass
from bisect import bisect_right
from random import Random
from collections import Counter
import json

PIN='43ec6098b1330ae86d0a7863be336c5d97f6ef34'

@dataclass(frozen=True, slots=True)
class Node:
    key: tuple
    time: int
    left: 'Node|None'
    right: 'Node|None'
    height: int
    size: int
    max_time: int
    min_phase: int
    max_phase: int

def height(a): return a.height if a else 0
def size(a): return a.size if a else 0

def mk(key,t,left=None,right=None):
    ph=key[0]; vals=[t]; lows=[ph]; highs=[ph]
    for a in (left,right):
        if a:
            vals.append(a.max_time); lows.append(a.min_phase); highs.append(a.max_phase)
    return Node(key,t,left,right,1+max(height(left),height(right)),1+size(left)+size(right),max(vals),min(lows),max(highs))

def rotate_right(a):
    b=a.left
    return mk(b.key,b.time,b.left,mk(a.key,a.time,b.right,a.right))

def rotate_left(a):
    b=a.right
    return mk(b.key,b.time,mk(a.key,a.time,a.left,b.left),b.right)

def balance(a):
    if height(a.left)-height(a.right)>1:
        l=a.left
        if height(l.left)<height(l.right):
            a=mk(a.key,a.time,rotate_left(l),a.right)
        return rotate_right(a)
    if height(a.right)-height(a.left)>1:
        r=a.right
        if height(r.right)<height(r.left):
            a=mk(a.key,a.time,a.left,rotate_right(r))
        return rotate_left(a)
    return a

def put(a,key,t):
    if a is None:return mk(key,t)
    if key==a.key:raise KeyError('duplicate source')
    if key<a.key:return balance(mk(a.key,a.time,put(a.left,key,t),a.right))
    return balance(mk(a.key,a.time,a.left,put(a.right,key,t)))

def pop_min(a):
    if a.left is None:return (a.key,a.time,a.right)
    k,t,newleft=pop_min(a.left)
    return (k,t,balance(mk(a.key,a.time,newleft,a.right)))

def erase(a,key):
    if a is None:raise KeyError('source absent')
    if key<a.key:return balance(mk(a.key,a.time,erase(a.left,key),a.right))
    if key>a.key:return balance(mk(a.key,a.time,a.left,erase(a.right,key)))
    if a.left is None:return a.right
    if a.right is None:return a.left
    k,t,right=pop_min(a.right)
    return balance(mk(k,t,a.left,right))

def range_max(a,lower,upper,stats=None):
    if not a:return None
    if stats is not None:stats['nodes']+=1
    if a.max_phase<lower or a.min_phase>=upper:return None
    if lower<=a.min_phase and a.max_phase<upper:return a.max_time
    vals=[a.time] if lower<=a.key[0]<upper else []
    for v in (range_max(a.left,lower,upper,stats),range_max(a.right,lower,upper,stats)):
        if v is not None:vals.append(v)
    return max(vals) if vals else None

class Index:
    def __init__(self,p,q,m,anchor=0):
        assert 0<p<q and 1<=m<=q
        self.p=p;self.q=q;self.M=2*q;self.m=m;self.anchor=anchor
        self.bounds=sorted((2*((z*p)%q),z) for z in range(m))
        self.by_label={z:(b,self.bounds[(i+1)%m][0]) for i,(b,z) in enumerate(self.bounds)}
    def key(self,t):return (2*((t-self.anchor)*self.p%self.q),t)
    def insert(self,root,t):return put(root,self.key(t),t)
    def delete(self,root,t):return erase(root,self.key(t))
    def query(self,root,j,x,labels=None,stats=None):
        if root and root.max_time>=j:raise ValueError('source must precede observation')
        selected=list(range(self.m)) if labels is None else list(labels)
        rot=(x-2*(j-self.anchor)*self.p)%self.M
        out=[]
        for z in selected:
            start,end=self.by_label[z]
            a=(start-rot)%self.M;b=(end-rot)%self.M
            if self.m==1:latest=root.max_time if root else None
            elif a>=b:
                vals=[range_max(root,a,self.M,stats),range_max(root,0,b,stats)]
                latest=max((v for v in vals if v is not None),default=None)
            else:latest=range_max(root,a,b,stats)
            out.append(None if latest is None else j-latest)
        return out
    def oracle(self,source_set,j,x,labels):
        res={z:None for z in labels}
        bs=[b for b,z in self.bounds]
        for t in source_set:
            assert t<j
            y=(x+2*(t-j)*self.p)%self.M
            z=self.bounds[bisect_right(bs,y)-1][1]
            if z in res and (res[z] is None or t>res[z]):res[z]=t
        return [None if res[z] is None else j-res[z] for z in labels]

def check(root):
    if root is None:return 0
    lh=check(root.left);rh=check(root.right)
    assert abs(lh-rh)<=1
    assert root.height==1+max(lh,rh)
    assert root.size==1+size(root.left)+size(root.right)
    assert root.max_time==max([root.time]+[n.max_time for n in (root.left,root.right) if n])
    if root.left:assert root.left.key<root.key
    if root.right:assert root.key<root.right.key
    return root.height

def small_cases():
    rng=Random(6117)
    cases=queries=updates=branch_queries=oldroot_checks=0
    for m in (1,2,3,5,8):
        for H in (1,2,4,8,17):
            for rep in range(9):
                q=1009;p=rng.randrange(1,q);j=rng.choice([10**18+314,123,-10**18])
                anchor=j-2*H
                ix=Index(p,q,m,anchor)
                root=None;S=set()
                for r in range(1,H+1):
                    t=j-r;root=ix.insert(root,t);S.add(t)
                versions=[(root,frozenset(S),j)]
                for step in range(14):
                    base=rng.randrange(len(versions))
                    old_root,old_set,old_j=versions[base]
                    newset=set(old_set)
                    newroot=old_root
                    if newset and rng.randrange(3)>0:
                        t=rng.choice(sorted(newset));newroot=ix.delete(newroot,t);newset.remove(t)
                    else:
                        t=old_j-rng.randrange(1,H+30)
                        if t not in newset:
                            newroot=ix.insert(newroot,t);newset.add(t)
                    updates+=1
                    newj=old_j+rng.randrange(0,10)
                    versions.append((newroot,frozenset(newset),newj))
                    for vr,vs,vj in (versions[base],versions[-1]):
                        x=rng.randrange(2*q)
                        subset=rng.sample(range(m),rng.randrange(0,m+1))
                        assert ix.query(vr,vj,x,subset)==ix.oracle(vs,vj,x,subset)
                        queries+=1
                    if step%4==0:
                        check(newroot);oldroot_checks+=1
                for _ in range(7):
                    vr,vs,vj=rng.choice(versions)
                    x=rng.randrange(2*q)
                    labels=rng.sample(range(m),rng.randrange(0,m+1))
                    assert ix.query(vr,vj,x,labels)==ix.oracle(vs,vj,x,labels)
                    branch_queries+=1
                cases+=1
    return {'cases':cases,'persistent_versions':cases*15,'mutations':updates,'queries':queries,'retrospective_queries':branch_queries,'structural_checks':oldroot_checks}

def frozen_cases():
    pL=262204504569236716045286;pU=pL+1;q=10**24;m=128;H=225;J=10**12+128
    out=[]
    for p in (pL,pU):
        ix=Index(p,q,m,anchor=J-500)
        roots=[];sets=[];root=None;S=set()
        for r in range(1,H+1):
            t=J-r;root=ix.insert(root,t);S.add(t)
        roots.append(root);sets.append(frozenset(S))
        for k in range(10):
            t=J-(5+17*k)
            root=ix.delete(root,t);S.remove(t)
            roots.append(root);sets.append(frozenset(S))
        for k in range(10):
            t=J-(5+17*k)
            root=ix.insert(root,t);S.add(t)
            roots.append(root);sets.append(frozenset(S))
        check(root)
        rng=Random(611+int(p-pL));oracle_checks=0;cnt=Counter()
        for t in range(len(roots)):
            for _ in range(6):
                x=rng.randrange(2*q)
                labels=rng.sample(range(m),3)
                got=ix.query(roots[t],J,x,labels,cnt)
                assert got==ix.oracle(sets[t],J,x,labels)
                oracle_checks+=1
        out.append({'endpoint_p':str(p),'q':str(q),'m':m,'H':H,'persistent_roots':len(roots),'source_update_operations':20,'sparse_queries':oracle_checks,'labels_per_query':3,'actual_tree_nodes_visited':cnt['nodes'],'max_height':root.height})
    return out

def safe_order_certificate(p,q,m,H):
    """theta in [p/q,(p+1)/q]. Verify relevant relative phase-index orderings."""
    ks=set(range(m))|set(range(-H,0))
    ds={a-b for a in ks for b in ks if a!=b}
    minmargin=min((min((d*p)%q,(-d*p)%q),d) for d in ds)
    failures=[d for d in ds if min((d*p)%q,(-d*p)%q)<=abs(d)]
    return {'index_count':len(ks),'difference_count':len(ds),'min_period_distance_num':str(minmargin[0]),'at_difference':minmargin[1],'max_abs_difference':max(map(abs,ds)),'min_strict_margin_minus_d':str(min(min((d*p)%q,(-d*p)%q)-abs(d) for d in ds),'certificate':not failures,'failure_examples':failures[:5]}

def drift_counterexample():
    """Two interior rational parameters of the frozen interval reverse label."""
    q=10**24;p=262204504569236716045286
    out=[]
    for eps in (1,3):
        a=4*p+eps;b=4*q
        ix=Index(a,b,2,anchor=0)
        root=ix.insert(None,0)
        y=(-q*a)%b
        got=ix.query(root,q,0,[0,1]);oracle=ix.oracle({0},q,0,[0,1]);assert got==oracle
        out.append({'theta_num':str(a),'theta_den':str(b),'age':str(q),'source_phase_num_mod_den':str(y),'source_phase_den':str(b),'ages_per_original_label':[str(u) if u is not None else None for u in got]})
    assert out[0]['ages_per_original_label']!=out[1]['ages_per_original_label']
    return out

def shift_invariance():
    rng=Random(6124);num=0
    for p,q in [(3,11),(101,1009),(262204504569236716045286,10**24)]:
        for m,H in [(1,5),(4,10),(10,20)]:
            for rep in range(11):
                base_j=rng.randrange(-1000,1000)
                offset=rng.choice([0,10**30,-10**40,10**80])
                S={base_j-r for r in range(1,H+1)}
                x=rng.randrange(2*q)
                ia=Index(p,q,m,anchor=base_j)
                ra=None
                for t in S:ra=ia.insert(ra,t)
                ib=Index(p,q,m,anchor=base_j+offset)
                rb=None
                for t in S:rb=ib.insert(rb,t+offset)
                assert ia.query(ra,base_j,x)==ib.query(rb,base_j+offset,x)
                num+=1
    return {'large_absolute_time_shift_invariance':num}

def main():
    res={'frozen_science_pin':PIN,'classification':'AUTHOR_PROOF_AND_EXACT_FINITE_TEST','small':small_cases(),'frozen_sparse':frozen_cases(),'order_certificate':safe_order_certificate(262204504569236716045286,10**24,128,225),'irrational_drift_witness':drift_counterexample(),'time_shift':shift_invariance()}
    print(json.dumps(res,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
