"""Exact advice/coordinate-query trade-off after a branch join; original BRC replay."""
import argparse,json
from functools import cache
from itertools import combinations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT))
from copylife.kernel_checks import Physical,core

def optimum(vals,coords,k):
    """All partitions into <=2^k cells, all one-coordinate binary decision trees.
    A state bitset indexes worlds (not markers)."""
    N=len(vals); masks=[sum(1<<i for i,v in enumerate(vals) if (v>>j)&1) for j in range(coords)]
    @cache
    def depth(U):
        if U.bit_count()<2:return 0
        return min(1+max(depth(U&M),depth(U&~M)) for M in masks if U&M and U&~M)
    full=(1<<N)-1
    @cache
    def cost(U,L):
        if U.bit_count()<=L:return 0
        if L==1:return depth(U)
        head=U&-U;ans=depth(U);p=(U-1)&U
        while p:
            if p&head:ans=min(ans,max(depth(p),cost(U^p,L-1)))
            p=(p-1)&U
        return ans
    return cost(full,min(N,1<<k))

def words(kind,b):
    m=(1<<b)-1
    if kind=='star':return tuple(0 if a==0 else 1<<(a-1) for a in range(1<<b))
    return tuple(sum((((a&j).bit_count()&1)<<(j-1)) for j in range(1,m+1)) for a in range(1<<b))

def join_code(h,b,s):
    return h>>(b-s) # only this cross-join state is transmitted

def decode(kind,b,s,summary,probe):
    first=summary<<(b-s);stop=(summary+1)<<(b-s)
    if kind=='linear':
        h=first
        for bit in range(b-s):h|=probe((1<<bit)-1)<<bit
        return words(kind,b)[h]
    options=list(range(first,stop))
    for h in [a for a in options if a][:(len(options) if 0 in options else len(options)-1)]:
        if probe(h-1):return 1<<(h-1)
        options.remove(h)
    assert len(options)==1
    return words(kind,b)[options[0]]

def physically(C,kind,b,s,h_input):
    m=(1<<b)-1
    # h_input and exact source table are harness preparation only.
    src=lambda j:b+j
    temp=b+m; waste=temp+1
    init=[(h_input>>i)&1 for i in range(b)]+list(range(1,m+1))+[0,0]
    P=Physical(C,init);h=0
    for i in range(b):
        P.drop(i);h |= int(bool(P.C.observe_result(P.J)))<<i
    z=words(kind,b)[h]
    for j in range(m):
        a=src(j); expect=j+1
        assert P.copy(temp,a)==expect # validates public marker values on this certified family
        P.drop(a)
        assert P.copy(waste,temp)==expect
        # Two equal-price non-self addressed writes of the same full identity.
        assert P.copy(a if (z>>j)&1 else waste,temp)==expect
        P.drop(temp);P.drop(waste)
    advice=join_code(h,b,s); prefix=P.cost
    del h,z
    def query(j):
        key=j+1; bit=(key&-key).bit_length()-1
        return P.probe(src(j),bit)
    before=P.probes
    result=decode(kind,b,s,advice,query)
    n=P.probes-before
    recovered=tuple((j+1) if (result>>j)&1 else 0 for j in range(m))
    assert tuple(P.codes()[b:b+m])==recovered # verification harness only
    # Definite service: try public key j+1 preferentially, otherwise use common fallback.
    # Required choices arise from the decoded support alone. Full physical audit is independent.
    selected=[]
    for j in range(m):
        k=m+1 if (result>>j)&1 else j+1
        P.round(0,0,k)
        assert P.events[-1]['key']==k
        selected.append(k)
        P.drop(0)
    assert P.probes-before==n
    return dict(guard_word=h_input,summary=advice,join_commands=prefix,recovery_reads=n,total=P.cost,chosen=selected)

def run():
    b=3;m=7;r=12; C=core.prior.Compiler(slots=r);ret={}
    for kind in ('linear','star'):
        vals=words(kind,b); cases=[]
        for s in range(b+1):
            opt=optimum(vals,m,s)
            form=b-s if kind=='linear' else (1<<(b-s))-1
            assert opt==form
            traces=[physically(C,kind,b,s,h) for h in range(1<<b)]
            assert len({a['join_commands'] for a in traces})==1 and max(a['recovery_reads'] for a in traces)==opt
            if kind=='star':
                size=1<<(b-s)
                assert 2*sum(a['recovery_reads'] for a in traces)==(1<<s)*(size-1)*(size+2)
            else:assert all(a['recovery_reads']==b-s for a in traces)
            cases.append(dict(remembered_bits=s,computed_minimax=opt,formula=form,traces=traces))
        for h in range(1<<b):
            t=cases[-1]['traces'][h]['total']
            assert all(c['traces'][h]['total']==t+8*c['traces'][h]['recovery_reads'] for c in cases)
        ret[kind]=dict(support_words=vals,cases=cases)
    return dict(status='PASS',scope='64 original BRC executions and exhaustive partition/query optimization for each eight-world support family, fixed 12-slot construction; worst additional reads, not overall minimax command cost',physical_cases=64,inventory=dict(members=getattr(C,'members',None),candidate_relations=len(C.H)),families=ret)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=Path(__file__).with_name('memory_results.json'));args=ap.parse_args()
    a=run();args.out.write_text(json.dumps(a,indent=2,sort_keys=True)+'\n');print('PASS',a['physical_cases'])
