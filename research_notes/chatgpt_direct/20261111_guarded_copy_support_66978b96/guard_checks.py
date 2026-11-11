"""Checks equal-command conditional-copy routing, rank memory, and guarded path costs.
Finite evidence and proofs are separate. All-key tests here use explicit selected preparations.
No native BRC execution is counted by this control program.
"""
from itertools import product,combinations
from pathlib import Path
import sys, json, argparse
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'copylife'))
from oracle import Model
from certificates import minimum_mask
from origin_checks import compile_graph,projected

def rankrows(rows):
    piv={};basis=[]
    for j,val in enumerate(rows):
        a=val
        while a:
            i=a.bit_length()-1
            if i not in piv:
                piv[i]=a;basis.append(j);break
            a ^= piv[i]
    return basis

def phys_route(model,rows,n,z,pairs):
    """Literal per-slot assignment, real Boolean dispatch and inherited word lengths."""
    m=len(rows);tmp=2*m;gs=tmp+1
    tab=[0]*model.r
    for j,(u,v) in enumerate(pairs):tab[2*j:2*j+2]=[u,v]
    for i in range(n):tab[gs+i]=3 if z>>i&1 else 0
    fee=0; steps=0
    def move(d,s):
        nonlocal fee,steps
        assert d!=s
        x=tab[s];tab[d]=x;fee+=model.copy_charge(x);steps+=1
    def drop(d):
        nonlocal fee,steps
        x=tab[d];tab[d]=0;fee+=model.q+9;steps+=1;return bool(x)
    for i in range(n):
        reply=drop(gs+i)
        for j,row in enumerate(rows):
            if row>>i&1:
                l=2*j; r=l+1
                move(tmp,l)
                if reply: move(l,r);move(r,tmp)
                else: move(l,tmp);move(tmp,l)
                drop(tmp)
    for j in range(m):assert drop(2*j+1)
    return tuple(tab),fee,steps

def rank_checks():
    matrices=literal_inputs=projections=cost_matches=0; examples=[]
    for m,n in ((1,1),(1,5),(2,3),(3,3),(3,4)):
        slots=max(2*m+1+n,4*m-3);model=Model(slots,())
        pairs=[(4*j+1,4*j+2) for j in range(m)]
        assert max(k for p in pairs for k in p)<=slots+1
        assert all(model.copy_charge(a)==model.copy_charge(b) for a,b in pairs)
        for rows in product(range(1<<n),repeat=m):
            base=rankrows(rows);rho=len(base);states={};costs=set();answers=set()
            expcost=(n+m)*(model.q+9)+sum(row.bit_count()*(model.q+9+3*model.copy_charge(pairs[j][0])) for j,row in enumerate(rows))
            for z in range(1<<n):
                p=tuple((row&z).bit_count()%2 for row in rows)
                t,c,steps=phys_route(model,rows,n,z,pairs)
                pred=tuple(pairs[j][b] for j,b in enumerate(p))
                assert tuple(t[2*j] for j in range(m))==pred and all(t[j]==0 for j in range(slots) if j>=2*m or j%2)
                assert c==expcost
                ans=tuple(k for k in model.keys(0) if k not in t)
                answers.add(ans)
                sig=tuple(p[i] for i in base);states.setdefault(sig,set()).add(ans);costs.add(c)
                literal_inputs+=1;cost_matches+=1
            assert len(costs)==1 and len(answers)==len(states)==2**rho and all(len(s)==1 for s in states.values())
            for k in range(rho+1):
                # Store the first k basis-row bits, then one selected physical bit (low bit)
                # on each other basis row. No pair has overlapping identities.
                restored={}
                for z in range(1<<n):
                    p=tuple((row&z).bit_count()%2 for row in rows)
                    mem=tuple(p[i] for i in base[:k])
                    bits=tuple(pairs[i][p[i]]&1 for i in base[k:]);key=mem+bits
                    if key in restored:assert restored[key]==p
                    restored[key]=p
                assert len(restored)==2**rho
                projections+=1
            if n==4 and rows==(0b1110,0b1011,0b0101):
                examples.append(dict(rows=rows,n=n,m=m,r=slots,rank=rho,physical_histories=2**n,exclusion_classes=len(answers),cost=expcost,basis_rows=base))
            matrices+=1
    return dict(matrix_shapes=[[1,1],[1,5],[2,3],[3,3],[3,4]],matrices=matrices,literal_guard_world_executions=literal_inputs,
                equal_cost_checks=cost_matches,memory_tradeoff_cases=projections,example=examples)

def regret_checks():
    rows=[]
    # Independent two-world finite DP. State S is a subset of possible true
    # survivors. Can ask a separating bit or take any key universally available.
    from functools import cache
    for n in range(1,9):
        m=Model(n+3,());h=1<<(m.b-1);result=[]
        pairs=[(h,1)]
        for z in range(1<<n):
            table,c,steps=phys_route(m,((1<<n)-1,),n,z,pairs)
            assert table[0]==(1 if z.bit_count()%2 else h)
            known=(n+1)*(m.q+9)+n*(m.q+9+3*m.copy_charge(h))
            assert c==known
        # Omit W/D common fees: only incremental weight/paid bits appear below.
        ks=tuple(m.keys(0))
        @cache
        def dp(T,S,actual):
            if not T:return 0
            a=min(m.weight(k)+dp(T-1,S,actual) for k in ks if k not in S)
            if len(S)>1:a=min(a,8+dp(T,(actual,),actual))
            return a
        for T in range(13):
            odd=dp(T,(1,h),1);even=dp(T,(1,h),h)
            assert odd==2*T+min(2*T,8) and even==4*T
            result.append(dict(T=T,odd_optimal_after_forget=odd,even_optimal_after_forget=even))
        rows.append(dict(n=n,r=m.r,h=h,distinct_gate_words=1<<n,raw_prefix_fee=known,odd_DNF_terms=1<<(n-1),T4=result[4],T5=result[5]))
    return rows

def join_examples():
    m=Model(3,());data=[]
    for x in (1,2):
        tab=[x,2,0];orig=['X','Y','Z'];price=0
        def cp(d,s):
            nonlocal price
            k=tab[s];price+=m.copy_charge(k);tab[d]=k;orig[d]=orig[s];return k
        def drop(d):
            nonlocal price
            k=tab[d];tab[d]=0;orig[d]=None;price+=m.q+9;return bool(k)
        k=cp(2,0);cp(0,1 if k==1 else 2);drop(1);drop(2)
        assert tab==[2,0,0]
        data.append(dict(initial_X=x,final=tab,final_origin=orig[0],body_to_join=price))
    assert len({row['body_to_join'] for row in data})==1
    assert not any(row['initial_X']==1 and row['final_origin']=='X' for row in data)
    assert any(row['initial_X']==1 for row in data) and any(row['final_origin']=='X' for row in data)
    # Explicit same-true-world branch enumeration: a W business reply controls its own suffix.
    m=Model(2,());cost={}
    for k in m.keys(1):
        fee=8*m.r+m.fixed[1]+m.weight(k)
        cost[k]=fee+(m.copy_charge(k) if k==6 else 0)
    assert cost=={4:87,5:89,6:129}
    return dict(conditional_conjunction=data,product_of_separate_unions_wrongly_blocks=1,
                endogenous=dict(initial=[0,0],target=1,long_branch_key=6,actual_full_cost_by_key=cost,
                    pointwise_minimum=min(cost.values()),unattainable_short_leaf_unconstrained_minimum=85))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=HERE/'guard_results.json')
    out=ap.parse_args().out
    a=rank_checks();z=dict(status='PASS',scope='Control-level exact finite checks; native executions are reported separately.',linear_routes=a,single_parity=regret_checks(),guarded_joins=join_examples())
    out.write_text(json.dumps(z,indent=2)+'\n')
    print(json.dumps(a))
if __name__=='__main__':main()
