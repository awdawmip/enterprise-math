#!/usr/bin/env python3
"""EC49DI independent exact signed-X6 weighted observer check (stdlib only).

All calculations are integers. Ranks are certified by nonzero minors modulo two
primes; finite runs audit separately written analytic formulae, not all-h truth.
"""
import argparse
import itertools
import json
import hashlib
from collections import defaultdict

P1, P2 = 1000003,1000033
X = (2,2,5,2,2,2)
Y = tuple(2*t+1 for t in X)
A=(1,2)
B=(2,1)
OPS={
 'a':(-1,-1), 'b':(-2,-2),
 'c':(1,2,-1,-2), 'd':(2,1,-2,-1),
 'e':(3,1,1,-3),
}

def endpoint(word):
    e=[0]*6
    for j in word:
        e[abs(j)-1]+=1 if j>0 else -1
    return tuple(e)

def positive_count(word):
    return sum(j>0 for j in word)

def tags(word):
    return (2 if any(word[i:i+2]==A for i in range(len(word)-1)) else 0) + (1 if any(word[i:i+2]==B for i in range(len(word)-1)) else 0)

def weights(word):
    xx=yy=1
    for j in word:
        if j>0:
            xx*=X[j-1];yy*=Y[j-1]
    return xx,yy

def gate(axis): return (axis,-axis)

def gates(i,j,count_i,count_j): return gate(i)*count_i + gate(j)*count_j

def tail_for_extreme(h, prefix):
    # prefix is a partially built word with endpoint e; append negative-only
    # steps so that the final native X6 displacement is (-2h,0,...,0).
    e=endpoint(prefix)
    target=(-2*h,0,0,0,0,0)
    counts=[e[k]-target[k] for k in range(6)]
    assert min(counts)>=0, (prefix,h,counts)
    return prefix+tuple(-j for j in range(1,7) for _ in range(counts[j-1]))

def extreme_paths(h,m,tag):
    core={0:(),2:(1,2),1:(2,1),3:(1,2,1)}[tag]
    g=m-len(core)
    if g<0:return []
    # Axis 1 is c=2, axis 3 is d=5. Only gate patterns vary.
    out=[]
    for k in range(g+1):
        start=gates(1,3,k,g-k)+core
        w=tail_for_extreme(h,start)
        assert len(w)==2*h+2*m and endpoint(w)==(-2*h,0,0,0,0,0)
        assert positive_count(w)==m and tags(w)==tag
        out.append(w)
    return out

def rank_mod_rows(rows,p):
    basis={}
    for row in rows:
        v=[z%p for z in row]
        for k,b in sorted(basis.items()):
            c=v[k]
            if c:
                for j in range(k,len(v)):v[j]=(v[j]-c*b[j])%p
        for j,c in enumerate(v):
            if c:
                inv=pow(c,-1,p)
                basis[j]=[(q*inv)%p for q in v]
                break
    return len(basis)

def extreme_rank(h,m,p):
    suffix=OPS['e']*h
    accum=0; parts={}; evidence={}
    for tag in (0,2,1,3):
        rows=[]
        for word in extreme_paths(h,m,tag):
            z=word+suffix
            assert endpoint(z)==(0,0,0,0,0,0) and tags(z)==tag
            wx,wy=weights(z)
            rows.append((wx,wy,1))
        r=rank_mod_rows(rows,p)
        parts[str(tag)]=r;accum+=r
        evidence[str(tag)]=[list(row) for row in rows[:3]]
    return accum,parts,evidence

def motifs():
    return [
       (-3,3,-3,3,-3,3),
       (-1,1,-2,2,-1,1),
       (-2,2,-1,1,-2,2),
       (-3,1,2,-2,-1,3),
       (-3,2,1,-1,-2,3),
       (-1,1,2,1,-1,-2),
    ]

def feature(p):
    t=tags(p)
    return tuple(int(t==k) for k in (0,1,2,3)) + (int(t in (0,1) and bool(p) and p[-1]==1), int(t in (0,2) and bool(p) and p[-1]==2))

def tag_bases(h,s,v):
    assert v>=0 and abs(s)+v<=h
    d=h-abs(s)-v
    if s>0 and v>0 and d==0:
        U=(1,)*(2*s);V=(2,)*(2*v);g=(-3,3)
        base=[U+g+V+g+g,U+V+g+g+g,V+U+g+g+g,(1,2)+(1,)*(2*s-1)+(2,)*(2*v-1)+g+g+g]
        assert [tags(w) for w in base]==[0,2,1,3]
        return base
    A1= (1 if s>=0 else -1,)*(2*abs(s)) if s else ()
    base=A1+(-3,3)*d+(2,)*(2*v)
    assert len(base)==2*h and tags(base)==0
    return [base+motif for motif in motifs()]

def returning_suffixes(h,s,v,mode):
    for k in ([h] if mode=='eq' else range(1,h+1)):
        for ops in itertools.product(OPS,repeat=k):
            w=tuple(j for op in ops for j in OPS[op])
            if endpoint(w)==(-2*s,-2*v,0,0,0,0):
                yield ops,w

def predicted_r(h,s,v,mode):
    d=h-abs(s)-v
    if d==0:return 4
    if mode=='le':return 6
    return 5 if d%2 else 6

def independent_columns(h,s,v,mode,p):
    # For every base prefix, three two-gate prepend variants.
    pre=[gate(3)+gate(3),gate(1)+gate(3),gate(1)+gate(1)]
    prefixes=[g+w for w in tag_bases(h,s,v) for g in pre]
    P=len(prefixes);expected=3*predicted_r(h,s,v,mode)
    for w in prefixes:
        assert len(w)==2*h+10 and endpoint(w)==(2*s,2*v,0,0,0,0)
    basis={}; sampled=0
    for ops,suffix in returning_suffixes(h,s,v,mode):
        sampled+=1
        by_tag=[[0]*P for _ in range(12)]
        for i,preword in enumerate(prefixes):
            full=preword+suffix
            assert endpoint(full)==(0,)*6
            t=tags(full);wx,wy=weights(full)
            by_tag[t][i]=1
            by_tag[4+t][i]=wx%p
            by_tag[8+t][i]=wy%p
        for col in by_tag:
            v=col
            for k,b in sorted(basis.items()):
                c=v[k]
                if c:
                    for j in range(k,P):v[j]=(v[j]-c*b[j])%p
            for j,c in enumerate(v):
                if c:
                    inv=pow(c,-1,p)
                    basis[j]=[(q*inv)%p for q in v]
                    break
        if len(basis)==expected:
            return len(basis),sampled,P
    return len(basis),sampled,P

def main():
    a=argparse.ArgumentParser();a.add_argument('--maxh',type=int,default=5)
    args=a.parse_args(); assert 2<=args.maxh<=7
    # Independent determinant check. gate rows k=0,1,2.
    for p in (P1,P2):
        q=[(X[2]**2,Y[2]**2,1),(X[0]*X[2],Y[0]*Y[2],1),(X[0]**2,Y[0]**2,1)]
        det=sum(q[0][i]*(q[1][(i+1)%3]*q[2][(i+2)%3]-q[1][(i+2)%3]*q[2][(i+1)%3]) for i in range(3))
        assert det==-2*1*(X[0]-X[2])**3,det
        assert rank_mod_rows(q,p)==3
    extrema={}
    predicted=[1,2,5,8,11,12]
    for h in range(2,args.maxh+1):
        for m in range(6):
            res=[]
            for p in (P1,P2):
                r,parts,ev=extreme_rank(h,m,p);res.append(r)
                assert r==predicted[m],(h,m,p,r,parts)
            extrema[f'{h}:{m}']=res
    global_checks=[]
    for h in range(2,args.maxh+1):
        for s in range(-h,h+1):
            for v in range(0,h-abs(s)+1):
                for mode in ('eq','le'):
                    per=[]
                    for p in (P1,P2):
                        r,checked,P=independent_columns(h,s,v,mode,p)
                        expect=3*predicted_r(h,s,v,mode)
                        assert r==expect,(h,s,v,mode,p,r,expect,checked)
                        per.append({'mod':p,'rank':r,'words_until_full':checked})
                    global_checks.append({'h':h,'s':s,'v':v,'mode':mode,'ranks':per})
    report={'status':'PASS','weights':{'x':X,'y':Y,'a':2,'b':1},'gate_det':-2*(X[0]-X[2])**3,'extreme_rank_by_m':predicted,'extreme_h_range':f'2..{args.maxh}','extreme_m_range':'0..5','extreme_checks':len(extrema)*2,'all_fiber_checks':len(global_checks)*2,'fibers_and_modes':len(global_checks),'all_fiber_rank_max':max(d['ranks'][0]['rank'] for d in global_checks),'max_suffixes_to_reach_rank':max(z['words_until_full'] for item in global_checks for z in item['ranks']), 'global_results':global_checks}
    print(json.dumps({k:v for k,v in report.items() if k!='global_results'},ensure_ascii=False,indent=2))
    with open('/mnt/data/ec49di_work/EC49DI_EXECUTED.json','w') as f:json.dump(report,f,indent=2)

if __name__=='__main__':main()
