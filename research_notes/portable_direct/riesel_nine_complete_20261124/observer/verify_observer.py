#!/usr/bin/env python3
"""The complete 59-coordinate ninth-budget observer on R3.

Standard-library, exact integer arithmetic. The set-cover oracle operates on
the full common period and does not implement the branch predicates themselves.
All-prime sufficiency is the classification theorem cited in proof.md.
"""
from __future__ import annotations
from functools import lru_cache
from itertools import combinations
from math import gcd,isqrt,lcm,prod
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
A3=191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3=398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
HOLES=(1,2,10,11,12,16,17,22,25,26,30,31,32)
FIXED_TAIL=(19,73,38737,246241,487824887233)
PERIOD=5040
POSITIONS=tuple(v for v in range(PERIOD) if v%35 in HOLES)
FULL=(1<<len(POSITIONS))-1

def factors(n):
    out=[];p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:out.append(n)
    return out

def exact_order(q):
    x=1
    for d in range(1,841):
        x=x*2%q
        if x==1:return d
    raise AssertionError(('unlisted order',q))

def load_inventory():
    obj=json.loads((HERE/'prime_inventory.json').read_text());done=set()
    def check(q):
        if q in done:return
        row=obj['certificates'][str(q)]
        if row['kind']=='trial':assert q>=2 and all(q%d for d in range(2,isqrt(q)+1))
        else:
            assert row['kind']=='lucas_n_minus_one'
            fs={int(p):e for p,e in row.get('factorization',row.get('factors')).items()}
            assert prod(p**e for p,e in fs.items())==q-1
            for p in fs:check(p)
            a=row['witness'];assert pow(a,q-1,q)==1
            assert all(gcd(pow(a,(q-1)//p,q)-1,q)==1 for p in fs)
        done.add(q)
    for q in obj['roots']:check(q)
    free=tuple(obj['free59']);assert len(free)==len(set(free))==59
    assert all(gcd(q,S3)==1 for q in free)
    order={q:exact_order(q) for q in obj['roots']}
    assert max(order[q] for q in free)==840
    assert all(12*PERIOD%d==0 for d in order.values())
    fixed={int(q):r for q,r in obj['fixed43'].items()}
    assert S3==6*prod(fixed) and all(A3%q==r for q,r in fixed.items())
    assert max(free)<A3*A3-1
    return obj,free,order,fixed,len(done)

def crt(pairs):
    a,m=0,1
    for r,q in pairs:
        assert gcd(m,q)==1
        a += m*((r-a)*pow(m,-1,q)%q);m*=q
    assert 0<=a<m
    return a,m

def root_v(q,b):return pow(2,-(4+6*b),q)
def root_w(q,b):return pow(2,-(16+18*b),q)

def configuration(q,g):
    chosen={};slots=[]
    def v(p,b):
        assert p not in chosen
        chosen[p]=root_v(p,b);slots.append({'prime':p,'coordinate':'v','phase':b})
    def w(p,b):
        assert p not in chosen
        chosen[p]=root_w(p,b);slots.append({'prime':p,'coordinate':'w','phase':b})
    def t(p,b):
        assert p not in chosen
        chosen[p]=root_w(p,4*b);slots.append({'prime':p,'coordinate':'t','phase':b})
    Z,K=g['Z7'],g['K21'];F=g['F16'];H=g['H20']
    if q in Z:
        family='five_mod7_rows_target_Z';w(q,0)
        for p,b in zip(K[:4],(1,2,3,5)):w(p,b)
    elif q in K:
        family='five_mod7_rows_target_K'
        for p,b in zip(Z,(0,1,2,3)):w(p,b)
        w(q,5)
    elif q in g['B8']:
        family='binary_refinement_target_B';t(q,1);t(3457,0);t(816769,2)
    elif q in F:
        family='binary_refinement_target_F';t(1153,1);t(q,0)
        t(next(p for p in F if p!=q),2)
    elif q in g['D6']+g['R12']:
        family='ternary_Q7';t(q,0)
        t(next(p for p in g['R12'] if p!=q),2)
    elif q in g['C10']+H:
        family='mod5_three_columns';t(q,0)
        for p,b in zip([p for p in H if p!=q][:2],(2,4)):t(p,b)
    elif q in g['J14']+g['L28']:
        family='zero_W_IV'
        for p,b in zip(Z,(2,3,4,5)):v(p,b)
        if q in g['J14']:
            v(q,1);v(g['L28'][0],8);v(g['L28'][1],22)
        else:
            v(3361,1);v(q,8);v(next(p for p in g['L28'] if p!=q),22)
    elif q in g['U35']:
        family='zero_W_V'
        for p,b in zip(Z,(1,3,4,5)):v(p,b)
        v(q,2)
        for p,b in zip([p for p in g['U35'] if p!=q][:2],(16,30)):v(p,b)
    elif q in g['V70']:
        family='zero_W_VI'
        for p,b in zip(Z,(2,3,4,5)):v(p,b)
        v(3361,1);v(61681,2);v(q,36)
    else:raise AssertionError(q)
    assert q in chosen and len(chosen)<=7
    return family,chosen,slots

@lru_cache(None)
def phase_mask(q,residue,d):
    f=d//gcd(d,12)
    if residue==0:return None,0
    value=residue*residue*pow(2,8,q)%q
    step=pow(2,12,q);hits=[]
    for b in range(f):
        if value==1:hits.append(b)
        value=value*step%q
    assert len(hits)<=1
    if not hits:return None,0
    b=hits[0]
    bits=sum(1<<i for i,v in enumerate(POSITIONS) if v%f==b)
    return b,bits

def cover_oracle(a,free,order):
    rows=[]
    for q in FIXED_TAIL+free:
        b,mask=phase_mask(q,a%q,order[q])
        if mask:rows.append((q,mask,order[q]//gcd(order[q],12),b))
    tested=[];minimum=None;witness=None
    for k in range(8):
        count=0
        for chosen in combinations(rows,k):
            count+=1;union=0
            for _,mask,_,_ in chosen:union|=mask
            if union==FULL:
                minimum=k;witness=[q for q,_,_,_ in chosen];break
        tested.append({'classes':k,'subsets_examined':count,'found':minimum is not None})
        if minimum is not None:break
    return {'minimum_classes_through_seven':minimum,'supplementary_cost_when_found':None if minimum is None else 2+minimum,
            'cover_primes_beyond_5_13':witness,'search_by_budget':tested,
            'active_channels':[{'prime':q,'v_period':f,'v_phase':b,'covered_positions':mask.bit_count()} for q,mask,f,b in rows]}

def prefix_check(old):
    primes=tuple(old)+(5,13)
    values={q:(A3*A3-1)%q for q in primes};missing=[]
    for n in range(12*PERIOD):
        if all(values.values()):missing.append(n)
        for q in primes:values[q]=(2*values[q]+1)%q
    want=[8+12*v for v in POSITIONS]
    assert missing==want and len(missing)==1872
    return {'n_period':12*PERIOD,'v_period':PERIOD,'hole_count':len(missing),'scalar_prime_residue_updates':len(primes)*12*PERIOD,'exact_holes':'n=8+12v, v mod35 in HOLES','native_BRC_execution':False}

@lru_cache(None)
def phi2(d):
    value=(1<<d)-1
    for e in range(1,d):
        if d%e==0:
            f=phi2(e);assert value%f==0;value//=f
    return value

def finite_840_pair(data,free,order,M):
    target=127681
    family,chosen,slots=configuration(target,data['groups'])
    assert family=='zero_W_VI' and order[target]==840
    cyclo=[]
    for d,b in [(560,36),(1680,106)]:
        value=phi2(d)
        assert value>1 and pow(2,d,value)==1
        tests={r:gcd(value,pow(2,d//r,value)-1) for r in factors(d)}
        assert set(tests.values())=={1}
        assert gcd(value,S3*M)==1 and value<A3*A3-1
        cyclo.append({'order':d,'cyclotomic_modulus':str(value),'v_phase':b,'v_period':140,'root_residue':str(root_v(value,b)),'proper_order_gcd_tests':tests,'modulus_claimed_prime':False,'chosen_ordinary_prime':'least prime divisor of this cyclotomic modulus'})
    assert gcd(int(cyclo[0]['cyclotomic_modulus']),int(cyclo[1]['cyclotomic_modulus']))==1
    roots=[]
    for on in (True,False):
        residues={q:chosen.get(q,0) for q in free}
        if not on:residues[target]=0
        pairs=[(A3,S3)]+[(residues[q],q) for q in free]
        pairs += [(int(r['root_residue']),int(r['cyclotomic_modulus'])) for r in cyclo]
        a,modulus=crt(pairs)
        assert a>0 and all(a%m==r for r,m in pairs)
        oracle=cover_oracle(a,free,order)
        assert oracle['minimum_classes_through_seven']==(7 if on else None)
        roots.append({'on':on,'root':str(a),'R3_index':str((a-A3)//S3),'oracle':oracle,'exact_supplementary_cost':9 if on else 10})
    common=0
    for q in chosen:
        if q==target:continue
        common |= phase_mask(q,chosen[q],order[q])[1]
    for r in cyclo:
        b=r['v_phase'];common |= sum(1<<i for i,v in enumerate(POSITIONS) if v%140==b)
    assert common==FULL
    a,b=map(lambda r:int(r['root']),roots)
    common_named=sorted(set(map(int,data['fixed43'])) | (set(free)-{target}))
    assert len(common_named)==101 and target not in common_named
    assert all(a%p==b%p for p in common_named)
    common_modulus=S3*(M//target)*prod(int(r['cyclotomic_modulus']) for r in cyclo)
    assert (a-b)%common_modulus==0 and a%target!=b%target
    return {'target_prime':target,'target_order':840,'family':family,'selected_slots':slots,
            'cyclotomic_support':cyclo,'ordinary_primes_used_from_each_cyclotomic_modulus':1,'common_cover_prime_count':10,
            'common_cover':'5,13; Z four rows; 3361; 61681; least prime divisor of Phi560(2); least prime divisor of Phi1680(2)',
            'common_modulus':str(common_modulus),'common_named_prime_coordinates':101,'common_named_prime_list':common_named,'common_additional_distinct_prime_divisors_at_least':2,
            'same_prime_future_trajectories_at_least':103,'roots':roots}

def main():
    data,free,order,fixed,nodes=load_inventory()
    prefix=prefix_check(data['old_dictionary'])
    M=prod(free);pairs=[]
    for q in free:
        family,chosen,slots=configuration(q,data['groups'])
        residues={p:chosen.get(p,0) for p in free};roots=[]
        for on in (True,False):
            rr=dict(residues)
            if not on:rr[q]=0
            a,modulus=crt([(A3,S3)]+[(rr[p],p) for p in free])
            assert modulus==S3*M and a>0
            assert all(a%p==r for p,r in rr.items()) and a%S3==A3
            oracle=cover_oracle(a,free,order)
            assert oracle['minimum_classes_through_seven']==(7 if on else None),(q,family,on,oracle)
            roots.append({'on':on,'root':str(a),'R3_index':str((a-A3)//S3),'target_residue':a%q,'oracle':oracle,
                          'cost_statement':'delta_P=9' if on else 'delta_P>9 by the complete ninth-budget prime universe; finiteness not asserted here'})
        aon,aoff=map(lambda r:int(r['root']),roots)
        assert (aon-aoff)%(S3*(M//q))==0 and aon%q!=aoff%q
        pairs.append({'target_prime':q,'target_order':order[q],'family':family,'selected_slots':slots,
                      'common_named_prime_coordinates':101,'roots':roots})
    finite=finite_840_pair(data,free,order,M)
    result={'schema':'RIESEL_R3_COMPLETE_NINE_OBSERVER_V15','status':'PASS',
            'scope':'The complete <=9 predicate on the full fixed43 R3 fiber; root residues and complete future trajectories',
            'R3':{'A3':str(A3),'S3':str(S3)},'free_prime_support':free,'free_coordinate_count':59,
            'observer_modulus':str(M),'observer_modulus_decimal_digits':len(str(M)),'observer_modulus_binary_bits':M.bit_length(),
            'maximum_prime_order':840,'exact_observer_condition':'M9 divides N',
            'ordinary_minimal_true_pairs':pairs,'all_on_roots_exact_cost_nine':True,'all_off_roots_have_cost_greater_than_nine':True,
            'off_finiteness_general_claimed':False,'finite_exact_nine_ten_pair_at_order840':finite,
            'exact_period_set_cover_check':prefix,'certified_prime_nodes':nodes,
            'all_prime_completeness_inputs':['v13 complete <=8 classification','v14 basic-pair forcing and one-W nine classification','v15 full Q0-retaining root predicate','v15 complete irredundant zero-W nine classification'],
            'set_cover_oracle_independent_of_explicit_branch_predicates':True,'native_BRC_execution_claimed':False,'independent_project_review_claimed':False}
    (HERE/'nine_observer_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','necessary_coordinates':59,'ordinary_pairs':len(pairs),'minimum_maximum_prime_order':840,'v_period':PERIOD,'n_period':12*PERIOD,'residual_bits':len(POSITIONS),'finite840_pair_costs':[9,10],'prime_nodes':nodes,'output':str(HERE/'nine_observer_certificate.json')}))

if __name__=='__main__':main()
