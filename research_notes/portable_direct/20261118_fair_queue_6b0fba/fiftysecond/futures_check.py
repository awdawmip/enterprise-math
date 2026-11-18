"""Exact restricted-future certificates on the pinned positive unit-word patch."""
import argparse
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
from itertools import combinations,product
import json
from math import comb
from pathlib import Path
import sys

PATCH='research_notes/chatgpt_direct/20261007_residual_algebra_patch_7c2e8a/BRC_PATCH.py'
PIN='8b74d37eec97457b71e5873426db6b800a5001039da0f48e813a73b6870da96c'
def load(repo):
    f=repo/PATCH
    assert sha256(f.read_bytes()).hexdigest()==PIN
    spec=importlib.util.spec_from_file_location('bounded_future_patch',f)
    p=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=p
    spec.loader.exec_module(p)
    return p

def source_coeffs(p,w,d):
    z=p.signature(w,d)
    assert all(t.count==t.total and t.dominant==1 for t in z.values())
    return {u:t.count for u,t in z.items()}

def canon(v):return tuple(sorted(v.items()))

def allwords(alphabet,depth):
    for length in range(depth+1):
        yield from product(alphabet,repeat=length)

def division(sig,a,right):
    out={}
    for u,k in sorted(sig.items(),key=lambda item:len(item[0])):
        yes=u and u[-1 if right else 0]==a
        cropped=u[:-1] if right else u[1:]
        val=k-(out.get(cropped,0) if yes else 0)
        assert val>=0
        if val:out[u]=val
    return out

def short_model(p):
    words=list(allwords((1,-2),7))
    result=[]
    for d in (1,2):
        sig={w:source_coeffs(p,w,d) for w in words}
        for w in words:
            if w:
                assert division(sig[w],w[0],False)==sig[w[1:]]
                assert division(sig[w],w[-1],True)==sig[w[:-1]]
        for h in range(4):
            fwd={}
            back={}
            for w in words:
                # Undefined deletions are observed as such. At d>=1 length is retained.
                key=(canon(sig[w]),w[:h],w[-h:] if h else ())
                obs=tuple(canon(sig[w[i:len(w)-j]]) if i+j<=len(w) else None
                          for i in range(h+1) for j in range(h+1-i))
                assert fwd.setdefault(key,obs)==obs
                assert back.setdefault(obs,key)==key
            result.append(dict(d=d,h=h,words=len(words),different_future_classes=len(fwd)))
    return result

def common_family(p,n,d,h):
    words=list(product(range(1,n+1),repeat=h))
    blocks=words[:]
    for _ in range(d):
        blocks=[sum(blocks[i:]+blocks[:i],()) for i in range(len(blocks))]
    fullset={a+tuple(reversed(b)) for a in blocks for b in blocks}
    keys={canon(source_coeffs(p,w,d)) for w in fullset}
    tags={(w[:h],w[-h:]) for w in fullset}
    assert len(keys)==1 and len(tags)==n**(2*h)
    return dict(n=n,d=d,h=h,length=len(next(iter(fullset))),same_signature_classes=len(keys),
                different_end_pairs=len(tags))

def first_heads(p):
    out=[]
    for r in range(1,6):
        width=2**(r+1)-1
        level=[(1,)+(0,)*(width-1)]
        examined=0
        for length in range(1,17):
            new=[]
            for v in level:
                a=list(v);b=list(v)
                for index in range(1,width,2):
                    source=(index-1)//2
                    a[index]+=v[source]
                    b[index+1]+=v[source]
                new.extend((tuple(a),tuple(b)))
            level=new
            examined+=len(level)
            middle=len(level)//2
            seen={v:j for j,v in enumerate(level[:middle])}
            pair=next(((seen[v],k) for k,v in enumerate(level[middle:],middle) if v in seen),None)
            if pair:
                ws=[tuple(int(x)+1 for x in format(k,f'0{length}b')) for k in pair]
                assert ws[0][0]!=ws[1][0] and source_coeffs(p,ws[0],r)==source_coeffs(p,ws[1],r)
                out.append(dict(precision=r,least_length=length,words=[list(w) for w in ws],examined=examined))
                break
    assert [x['least_length'] for x in out]==[2,4,7,12,16]
    return out

def anchored(p,w,pattern,d):
    result={}
    for hits in combinations(range(len(w)),len(pattern)):
        if tuple(w[j] for j in hits)!=pattern:continue
        sig=p.signature(w[hits[-1]+1:],d)
        for u,v in sig.items():
            result[u]=p.add(result.get(u,p.CWM_ZERO),v)
    return {u:v.count for u,v in result.items()}

def anchors(p):
    used=[]
    for w in [(1,2,2,1),(2,1,1,2),(1,-2,2,1,-2),(1,2,1,1,2,2,1)]:
        for pattern in [(1,),(2,),(1,-2),(2,1)]:
            for d in (1,2):
                ans=anchored(p,w,pattern,d)
                allc=source_coeffs(p,w,d+len(pattern))
                assert ans=={u[len(pattern):]:k for u,k in allc.items() if u[:len(pattern)]==pattern}
                used.append(sum(ans.values()))
    rows=[]
    u,v=(1,),(2,)
    for r in range(1,6):
        u,v=u+v,v+u
        assert source_coeffs(p,u,r)==source_coeffs(p,v,r)
        witness=(1,)*r+(2,)
        sig=source_coeffs(p,u,r+1)
        other=source_coeffs(p,v,r+1)
        coef=sig.get(witness,0)-other.get(witness,0)
        assert coef==(-1)**(r-1)*2**((r-1)*(r-2)//2)
        rows.append(dict(r=r,native_word_length=len(u),target_pattern=witness,difference=coef))
    unary=[]
    for m in range(2,8):
        sums=[{},{}]
        for j in range(m+1):
            for u,w in p.signature((1,)*j,m).items():
                for _ in range(comb(m,j)):
                    slot=sums[(m-j)%2]
                    slot[u]=p.add(slot.get(u,p.CWM_ZERO),w)
        for w in allwords((1,),m-1):
            assert sums[0].get(w,p.CWM_ZERO)==sums[1].get(w,p.CWM_ZERO)
        assert sums[0][(1,)*m].count==1 and (1,)*m not in sums[1]
        unary.append(dict(m=m,positive_worlds_per_population=2**(m-1),degree_m_gap=1))
    return dict(direct_anchor_tests=len(used),single_word_sharp=rows,unary_population_sharp=unary)

def mixture(p):
    def pack(ws):
        out={}
        for w in ws:
            for k,v in p.signature(w,2).items():
                out[k]=p.add(out.get(k,p.CWM_ZERO),v)
        return out
    A=[(1,2,2),(2,1,1)]
    B=[(1,1,2),(2,2,1)]
    assert pack(A)==pack(B) and [(w[0],w[-1]) for w in A]==[(w[0],w[-1]) for w in B]
    out=[]
    for ws in (A,B):
        before=pack(ws)
        after=pack([w[1:] for w in ws])
        joint=Counter()
        for w in ws:
            for u,v in p.signature(w[1:],1).items():
                joint[(w[0],)+u]+=v.count
        for u in set(before)|set(after):
            gap=before.get(u,p.CWM_ZERO).count-after.get(u,p.CWM_ZERO).count
            assert gap==joint[u]
        out.append({''.join(map(str,k)):v.count for k,v in after.items() if len(k)==2})
    assert out==[{'11':1,'22':1},{'12':1,'21':1}]
    return dict(initial_words=[A,B],same_end_pair_counts=True,post_drop_degree_two=out)

def hit_example(p):
    w,z=(1,2,2,1),(2,1,1,2)
    a,b=source_coeffs(p,w,2),source_coeffs(p,z,2)
    assert a==b
    l,k=source_coeffs(p,w[1:],1),source_coeffs(p,z[1:],1)
    assert {v:l.get(v,0)-k.get(v,0) for v in set(l)|set(k)}=={():0,(1,):-1,(2,):1}
    s,n=5,2 # H=X2+((-1)*X1), counting leaves and gates
    D=2*n*s*s
    first=[F(0)]+[F((-1)**(r-1),r)*(F(1,2**r)-1) for r in range(1,D)]
    assert first[1]==F(-1,2)
    return dict(source_port_count=12,actual_ports=[1,2],word_degree=2,pure_equal=True,
                hidden_left_drop_degree=1,raw_output_difference='X2-X1',active_variables=n,
                compiled_difference_tree_nodes=s,external_tuple_dimension=D,first_nonzero_entry=[1,0,'-1/2'],
                first_column_sha256=sha256(json.dumps([str(x) for x in first]).encode()).hexdigest())

def main():
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument('--repo',type=Path,required=True)
    p=load(a.parse_args().repo)
    result=dict(patch_sha256=PIN,external_commit='adc7f1241b42e322a6451854ab7e4b4c146bf78a',
                short_future_classes=short_model(p),full_boundary_fibers=[common_family(p,*v) for v in
                ((2,1,1),(2,2,2),(2,3,1),(3,2,1))],hidden_head_thresholds=first_heads(p),
                anchored=anchors(p),positive_populations=mixture(p),hitting_example=hit_example(p))
    result['certificate_contract']={
        'source':'awdawmip/enterprise-math@bed9964bd6a31dc926e67f759dac66bd83797342:'+PATCH,
        'ports':list(p.PORTS),'field':'Q','coefficient_type':'unit indexed selections: (count,total,dominant)=(c,c,1) for c>0',
        'quotient_kernel':'J^(d+1), J generated by separate port variables',
        'original_futures':['left/right concatenation','all bounded coefficient queries','declared endpoint and order readouts'],
        'additional_tests':['true endpoint receipt','hidden endpoint removal with bounded budget','all anchored occurrence suffixes'],
        'formula_limit_in_matrix_example':5,'word_degrees':[1,2],
        'external_hitting_status':'conditional on frozen preprint; not an arbitrary shared circuit or native admission'}
    result['frozen_typed_brc_calls']=dict(p.CALLS)
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__': main()
