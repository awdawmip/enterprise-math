#!/usr/bin/env python3
"""C300 author-level modular noncancellation certificate, not native BRC.

For each frozen C293 path, build C298 integer polynomial denominator D.
At a modular root of a linear primitive denominator q, compute the
residue of f=A/D as a sum of original 79 rational terms in F_p.
A nonzero residue and nonzero D/q prove q does not divide A in Z[t].
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
import json
from pathlib import Path
import C298_SHARED_DENOMINATOR_EXACT as c298
import C288_ISOLATING_BOXES_EXACT as c288
import C275_STANDALONE_EXACT_REPLAY as src

PRIMES=(2305843009213693951,2147483647,1000000007,1000000009)

def evaluate_polynomial(p,x,prime):
    y=0
    for a in reversed(p):
        y=(y*x+a)%prime
    return y

def prepare_terms(path,tlo,thi,W):
    terms=c298.make_terms(path,tlo,thi,W)
    result=[];groups=Counter();occurs=defaultdict(list);scales=[]
    for j,(c,factors) in enumerate(terms):
        den_scalar=c.denominator
        factor_ids=[]
        nums=[]
        for n,d in factors:
            content,q=c298.primitive_factor(d)
            den_scalar*=content
            factor_ids.append(q)
            nums.append(tuple(n))
        local=Counter(factor_ids)
        for q,m in local.items():
            groups[q]=max(groups[q],m)
            occurs[q].append(j)
        scales.append(den_scalar)
        result.append((c.numerator,den_scalar,tuple(nums),tuple(factor_ids)))
    return groups,occurs,result,scales

def witness(q,group,occs,terms,scales,pr):
    assert len(q)==2
    if q[1]%pr==0:return None
    x=(-q[0]*pow(q[1],-1,pr))%pr
    if any(v%pr==0 for v in scales):return None
    if any(evaluate_polynomial(other,x,pr)==0 for other in group if other!=q):return None
    R=0
    for j in occs:
        num,den,nums,facs=terms[j]
        assert facs.count(q)==1
        val=num%pr
        for n in nums:
            val=val*evaluate_polynomial(n,x,pr)%pr
        for d in facs:
            if d!=q:
                val=val*pow(evaluate_polynomial(d,x,pr),-1,pr)%pr
        val=val*pow(den,-1,pr)%pr
        R=(R+val)%pr
    return {'prime':pr,'root':x,'residue':R}

def one_path(i,path,k,W):
    tlo=F(k,1<<24);thi=F(k+1,1<<24)
    group,occurs,terms,scales=prepare_terms(path,tlo,thi,W)
    linear=sorted(q for q in group if len(q)==2)
    nonlinear=sorted(q for q in group if len(q)!=2)
    assert all(group[q]==1 for q in linear),i
    found=[]; zeros=[]
    for q in linear:
        item=None
        for pr in PRIMES:
            item=witness(q,group,occurs[q],terms,scales,pr)
            if item is not None:break
        if item is None:
            raise AssertionError(f'no modular residue witness at path={i},q={q}')
        if item['residue']==0:zeros.append([list(q),item['prime'],str(item['root']),[int(j) for j in occurs[q]]])
        else:found.append([list(q),item['prime'],str(item['root']),str(item['residue'])])
    return {'index':i,'linear_factor_count':len(linear),'nonlinear_factor_count':len(nonlinear),
            'shared_denominator_degree':sum((len(q)-1)*m for q,m in group.items()),
            'linear_noncancellation_witnesses':found,'modular_zero_candidates':zeros,
            'prime_distribution':dict(sorted(Counter(v[1] for v in found).items()))}

def main():
    raw=json.loads(Path('C293_125_REFINED_BRACKETS.json').read_text())
    paths,_=c288.build_paths()
    W,_=src.floor_fixed_masses()
    out=[]
    for i,(row,path) in enumerate(zip(raw['records'],paths)):
        assert row[0]==i
        ans=one_path(i,path,int(row[1]),W)
        out.append(ans)
        if i%25==0:print('C300_PROGRESS',i,ans['linear_factor_count'],ans['prime_distribution'],flush=True)
    summary={'schema':'EM_C300_LINEAR_NONCANCELLATION_V1', 'paths':len(out),
             'total_linear_witnesses':sum(x['linear_factor_count'] for x in out),
             'factor_count_distribution':dict(sorted(Counter(x['linear_factor_count'] for x in out).items())),
             'status':'AUTHOR_EXACT_MODULAR_NONCANCELLATION_NOT_ADMITTED'}
    Path('C300_LINEAR_POLE_RESIDUE_CERTIFICATES.json').write_text(json.dumps({'summary':summary,'rows':out},sort_keys=True,ensure_ascii=False,separators=(',',':'))+'\n')
    print('C300_LINEAR_POLE_MODULAR_EXACT_PASS',json.dumps(summary,sort_keys=True),flush=True)

if __name__=='__main__':main()

def exact_residue_zero(q,occ_indices,terms):
    assert len(q)==2
    t=F(-q[0],q[1])
    total=F(0)
    for j in occ_indices:
        num,den,nums,facs=terms[j]
        assert facs.count(q)==1
        prod=F(num,den)
        for n in nums:
            prod*=c298.poly_eval(n,t)
        for d in facs:
            if d!=q:
                v=c298.poly_eval(d,t)
                assert v!=0
                prod/=v
        total+=prod
    return total==0,total
