#!/usr/bin/env python3
"""Exact all-order geometry and certified prime inventory for R3 Q0 nine-covers.

Python standard library only. This checks finite reductions whose universal
bounds are proved in proof.md; it does not claim a new native BRC execution.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
B=(0,3,5,8,10,15,21,23,26,28,30,31,33)
B2=(0,4,5,13,14,15,19,20,25,28,29,33,34)
B4=(0,2,7,10,14,17,20,24,25,27,30,32,34)
A3=191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3=398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
Q0={5,13,19,73}
A,R,U=38737,246241,487824887233

def ratio(x):return {'numerator':x.numerator,'denominator':x.denominator}

@lru_cache(None)
def phi2(d):
    n=(1<<d)-1
    for e in range(1,d):
        if d%e==0:
            f=phi2(e);assert n%f==0;n//=f
    return n

def exact_order(q):
    x=1
    for d in range(1,721):
        x=2*x%q
        if x==1:return d
    raise AssertionError(('unknown order',q))

def verify_inventory():
    data=json.loads((HERE/'prime_inventory.json').read_text());done=set()
    def check(q):
        if q in done:return
        row=data['certificates'][str(q)]
        if row['kind']=='trial':
            assert q>=2 and all(q%d for d in range(2,isqrt(q)+1))
        else:
            assert row['kind']=='lucas_n_minus_one'
            fs={int(p):e for p,e in row['factorization'].items()}
            assert prod(p**e for p,e in fs.items())==q-1
            for p in fs:check(p)
            a=row['witness'];assert pow(a,q-1,q)==1
            assert all(gcd(pow(a,(q-1)//p,q)-1,q)==1 for p in fs)
        done.add(q)
    for q in data['roots']:check(q)
    cycles={row['order']:row for row in data['complete_cyclotomic_factorizations']}
    for d,row in cycles.items():
        fs={int(q):e for q,e in row['factors'].items()}
        assert prod(q**e for q,e in fs.items())==int(row['value'])==phi2(d)
        assert set(fs)<=done
    orders={q:exact_order(q) for q in data['roots']}
    assert max(data['roots']) < A3*A3-1
    fixed={int(q):r for q,r in data['fixed43'].items()}
    old=set(data['old_dictionary'])
    assert S3==6*prod(fixed) and all(A3%q==r for q,r in fixed.items())
    def inventory(base,h):
        ds=[h*g for g in range(1,base+1) if base%g==0 and gcd(h,base//g)==1]
        assert set(ds)<=set(cycles)
        qs=set(q for d in ds for q in map(int,cycles[d]['factors']))
        return sorted(q for q in qs if orders[q]//gcd(orders[q],base)==h and q not in old|Q0 and (q not in fixed or fixed[q]!=0) and q!=3)
    g=data['groups']
    expected36={1:[],2:[A],3:[R],4:[U],5:[],6:g['D6'],7:g['Z7']+g['G7'],8:g['B8'],10:g['C10']}
    expected144={2:g['B8'],3:[R]+g['D6']+g['R12'],4:g['F16'],5:g['C10']+g['H20']}
    checked=[]
    for base,exp in [(36,expected36),(144,expected144)]:
        for h,want in exp.items():
            got=inventory(base,h)
            # The selected fixed A and U have effective t-period one, not
            # among the queried t-periods. They are removed by restriction.
            assert got==sorted(want),(base,h,got,want)
            checked.append({'base_exponent':base,'effective_period':h,'available_primes':got})
    free=set().union(*(set(v) for v in g.values()))
    assert all(gcd(q,S3)==1 for q in free)
    for q in free:
        h=orders[q]//gcd(orders[q],36)
        categories=[{pow(2,-(16+18*b),q),(-pow(2,-(16+18*b),q))%q} for b in range(h)]
        assert all(len(x)==2 for x in categories)
        assert len(set().union(*categories))==2*h
    return data,orders,{'certified_root_primes':len(data['roots']),'verified_prime_nodes':len(done),'complete_cyclotomic_values':len(cycles),'available_inventories':checked}

def universal_mass(D,L,excluded):
    """All h>=6 outside exclusions, grouped by gcd(h,L), with exact maxima."""
    table=[]
    for g in range(1,L+1):
        if L%g:continue
        h=g
        while h<6 or h in excluded or gcd(h,L)!=g:h+=g
        K=max(Counter(x%g for x in D).values())
        mass=F(K*g,len(D)*h)
        table.append({'gcd':g,'least_period':h,'K':K,'relative_mass':ratio(mass)})
    maximum=max(F(r['relative_mass']['numerator'],r['relative_mass']['denominator']) for r in table)
    return maximum,table

def no_A_check():
    occupied=sorted({x%7 for x in B});rows=[]
    for m in range(1,5):
        for killed in combinations(occupied,m):
            D=[x for x in B if x%7 not in killed];r=len(D)
            c5=max(Counter(x%5 for x in D).values());c7=max(Counter(x%7 for x in D).values())
            E=max(F(r,6),F(c5,2),F(c7,2),F(1))
            for selected,p in [((),F(0)),((R,),F(1,3)),((U,),F(1,4)),((R,U),F(1,2))]:
                slots=5-len(selected)-m
                if slots<0:continue
                bound=p*r+slots*E;assert bound<r
                rows.append({'deleted_mod7_rows':killed,'fixed_tails':selected,'remaining_points':r,'generic_slots':slots,'generic_mass_bound':ratio(E),'union_bound':ratio(bound),'positive_gap':ratio(F(r)-bound)})
    assert 5*F(5,2)<13
    cases=[]
    for name,L,predicate,want in [('R_only',105,lambda x:x%3!=1,F(1,4)),('U_only',140,lambda x:x%4!=2,F(10,39)),('R_and_U',420,lambda x:x%3!=1 and x%4!=2,F(1,3))]:
        D=[x for x in range(L) if x%35 in B and predicate(x)]
        maximum,table=universal_mass(D,L,{7});assert maximum==want
        exclusion=10 if name=='U_only' else 6
        other,other_table=universal_mass(D,L,{7,exclusion})
        if name=='R_only':assert other<F(1,4)
        if name=='U_only':
            assert other==F(2,9) and 3*maximum+other==F(116,117)<1
            # A period-ten channel covers only one of the six required
            # (parity, occupied mod5 column) pairs.
            support={(x%2,x%5) for x in D};assert len(support)==6
        if name=='R_and_U':assert other==F(10,39)<F(1,3)
        cases.append({'name':name,'period':L,'residual_count':len(D),'maximum':ratio(maximum),'all_order_table':table,'exceptional_period':exclusion,'outside_exception_maximum':ratio(other),'outside_exception_table':other_table})
    return {'positive_row_deletion_cases':len(rows),'row_deletion_bounds':rows,'no_fixed_tail_gap':ratio(F(13)-5*F(5,2)),'zero_mod7_row_cases':cases,'only_possible_no_A_structure':'five distinct occupied modulo-seven rows'}

def minimal_geometries(residues,budget,min_period):
    limit=2**(budget-1)
    periods=tuple(e for e in range(min_period,35*limit+1) if e//gcd(e,35)<=limit)
    L=lcm(35,*periods)
    FULL=sum(1<<x for x in range(L) if x%35 in residues)
    rows=[]
    for e in periods:
        for b in range(e):
            bits=sum(1<<x for x in range(b,L,e))&FULL
            if bits:rows.append((e,b,bits))
    solutions=set();states=Counter()
    def visit(rem,chosen,left):
        states[len(chosen)]+=1
        if not rem:
            key=tuple(sorted(chosen))
            for j in key:
                private=rows[j][2]
                for t in key:
                    if j!=t:private&=~rows[t][2]
                if not private:return
            solutions.add(key);return
        if not left:return
        threshold=(rem.bit_count()+left-1)//left
        for j,(_,_,bits) in enumerate(rows):
            if j in chosen:continue
            if (rem&bits).bit_count()<threshold:continue
            visit(rem&~bits,chosen+(j,),left-1)
    visit(FULL,(),budget)
    covers=sorted(tuple((rows[j][0],rows[j][1]) for j in sol) for sol in solutions)
    return {'budget':budget,'private_point_interval_bound':limit,'candidate_periods':periods,'common_period':L,'candidate_nonempty_classes':len(rows),'visited_nodes_by_depth':dict(states),'minimal_geometries':covers}

def main():
    data,orders,inventory=verify_inventory();g=data['groups']
    noA=no_A_check()
    four=minimal_geometries(B2,4,3)
    expected4={tuple((3,b) for b in range(3)),tuple((4,b) for b in range(4)),tuple((5,b) for b in (0,3,4))}
    for c in range(3):expected4.add(tuple(sorted([(3,b) for b in range(3) if b!=c]+[(6,c),(6,c+3)])))
    for c in (0,3,4):expected4.add(tuple(sorted([(5,b) for b in (0,3,4) if b!=c]+[(10,c),(10,c+5)])))
    assert set(four['minimal_geometries'])==expected4 and len(expected4)==9
    three=minimal_geometries(B4,3,2)
    expected3={((2,0),(2,1)),((3,0),(3,1),(3,2)),((5,0),(5,2),(5,4))}
    for b in range(2):expected3.add(tuple(sorted([(2,b),(4,1-b),(4,3-b)])))
    assert set(three['minimal_geometries'])==expected3 and len(expected3)==5
    families=[
        {'name':'G7_five_rows','fixed_tails':[],'groups':['Z7+G7'],'w_phases':[0,1,2,3,5],'w_periods':[7]*5,'phase_count':9*8*7*6*5,'signed_count':9*8*7*6*5*32},
        {'name':'old_binary','fixed_tails':[A,U],'groups':['B8','B8'],'t_phases':[0,1],'t_periods':[2,2],'phase_count':6*5,'signed_count':6*5*4},
        {'name':'binary_refinement','fixed_tails':[A,U],'groups':['B8','F16','F16'],'t_phases_rule':'b mod2; 1-b and 3-b mod4, b=0 or1','phase_count':6*5*4*2,'signed_count':6*5*4*2*8},
        {'name':'ternary_Q7','fixed_tails':[A,R,U],'groups':['D6+R12','D6+R12'],'t_phases':[0,2],'t_periods':[3,3],'phase_count':5*4,'signed_count':5*4*4},
        {'name':'mod5_three_columns','fixed_tails':[A,U],'groups':['C10+H20']*3,'t_phases':[0,2,4],'t_periods':[5,5,5],'phase_count':9*8*7,'signed_count':9*8*7*8}]
    assert sum(r['phase_count'] for r in families)==15914
    assert sum(r['signed_count'] for r in families)==489992
    result={'schema':'RIESEL_R3_Q0_NINE_COVER_V15','status':'PASS','integer_trajectory':'F_n(a)=a^2*2^n-1; fixed-X6 positive singleton BRC x -> 2x+1','scope':'Existence of a supplemental cover of at most nine primes containing Q0 on the full R3 fiber; canonical root predicates, not all nine-prime dictionaries','R3':{'A3':str(A3),'S3':str(S3)},'inventory':inventory,'exact_orders':{str(q):d for q,d in orders.items()},'no_A':noA,'A_without_U_four_class_geometry':four,'A_with_U_three_class_geometry':three,'canonical_root_families':families,'canonical_phase_count':15914,'canonical_signed_CRT_count':489992,'maximum_free_prime_order':max(orders[q] for qs in g.values() for q in qs),'exact_cost_nine_rule':'canonical budget-nine predicate AND NOT the complete v13 budget-eight predicate','native_BRC_execution_claimed':False,'independent_project_review_claimed':False}
    assert result['maximum_free_prime_order']==720
    (HERE/'both_tail_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','no_A_positive_cases':noA['positive_row_deletion_cases'],'four_class_minimal_geometries':len(expected4),'three_class_minimal_geometries':len(expected3),'prime_nodes':inventory['verified_prime_nodes'],'canonical_phase_count':15914,'canonical_signed_count':489992,'maximum_free_prime_order':720,'output':str(HERE/'both_tail_certificate.json')}))

if __name__=='__main__':main()
