#!/usr/bin/env python3
"""Complete R3 cost-nine minimum, using the three proved branch reductions.

This file exhausts every canonical both-W CRT start. The zero-W lower-bound
calculation and one-W minimum are separate, explicitly named dependencies.
It also verifies full integer witnesses and optionally executes native BRC.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations, permutations, product
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import sys
import time

HERE=Path(__file__).resolve().parent
A3=191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3=398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
P=(7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,1321,14449,29191,65537,6700417)
FIXED43={7:5,17:10,31:8,41:38,71:11,97:34,113:69,127:119,151:147,241:165,
257:68,281:261,337:4,641:488,673:107,1321:475,14449:7695,29191:19665,
65537:4080,6700417:65537,5:3,13:1,19:6,73:37,11:0,61:0,331:0,
37:0,109:0,433:0,38737:38733,181:0,577:0,631:0,23311:0,54001:0,
87211:0,246241:182629,262657:0,279073:0,18837001:0,29247661:0,
487824887233:487823838657}
Z=(29,43,1429,5419)
K=(92737,649657,40388473189,77158673929,118750098349)
B8=(193,1153,6337,22253377,38941695937,278452876033)
D6=(33975937,138991501037953)
C10=(61681,4562284561,168692292721,469775495062434961)
R12=(209924353,4261383649,24929060818265360451708193)
H20=(8369281,394783681,4278255361,46908728641,750016890283777055704738227247474485366338380663681)
F16=(3457,816769,18446744069414584321,1562985901350085709953,1422346738975853644793916289)
J14=(3361,15790321,88959882481)
U35=(211,421,86171,106681,122921,152041,664441,1564921,7416361,47392381,146919792181,1041815865690181)
A_SET={1,2,10,11,12,16,17,22,25,26,30,31,32}
MINIMUM_INDEX=11380571075
GLOBAL_WITNESSES=((5,6),(7,16),(13,12),(17,3),(19,152),(31,89),(41,5),(71,293),(73,128),
(97,117),(113,833),(127,113),(151,41),(241,33),(257,87),(281,233),(337,773),
(641,527),(673,333),(1153,2480),(1321,257),(3457,2912),(14449,473),(29191,593),
(38737,140),(65537,95),(816769,320),(6700417,111),(487824887233,2120))
NATIVE_COMMIT='b1efc6c805661ed7b476e6e730107da6043176ee'
NATIVE_BLOBS={'brc_transport.py':'be1debe367263931bd5e93fd750be3ed54624fe1',
'brc_histogram.py':'9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1',
'brc_rational_holonomy.py':'2591640fe348da9cd7f293a957bea9ae92c82943',
'brc_weighted_recurrent.py':'4e6b3132580e3cd70a20a0d8bd4d28792b961afb'}


def pair(q,b,offset=4,step=6):
    r=pow(2,-(offset+step*b),q)
    return r,(-r)%q


def eight(a):
    retained=any(all(any(a%q in pair(q,b,16,18) for q in qs) for b in bs)
                 for qs,bs in [(B8,(0,4)),(D6,(0,2)),(C10,(0,6,8))])
    phases=[]
    for q in Z:
        bs=[b for b in range(1,6) if a%q in pair(q,b)]
        if len(bs)!=1:return retained
        phases.append(bs[0])
    if len(set(phases))!=4:return retained
    c=next(b for b in range(1,6) if b not in phases)
    via14=all(any(a%q in pair(q,b) for q in J14) for b in [c,c+7])
    points=[v for v in A_SET if v%7==c]
    via35=len(points)==2 and all(any(a%q in pair(q,b) for q in U35) for b in points)
    return retained or via14 or via35


def starts(qs,phases,coordinate):
    modulus=prod(qs)
    weights=[modulus//q*pow(modulus//q,-1,q) for q in qs]
    inverses=[pow(S3,-1,q) for q in qs]
    offset,step=(16,18) if coordinate=='w' else (16,72)
    base=[pow(2,-(offset+step*b),q) for q,b in zip(qs,phases)]
    values=[(((r-A3)*iv%q)*c,((-r-A3)*iv%q)*c)
            for q,r,iv,c in zip(qs,base,inverses,weights)]
    for bits in product((0,1),repeat=len(qs)):
        index=sum(v[b] for v,b in zip(values,bits))%modulus
        yield {'index':index,'index_period':str(modulus),'primes':qs,
               'phases':phases,'coordinate':coordinate,
               'signs':[1 if b==0 else -1 for b in bits],
               'root_residues':[(r if b==0 else -r)%q for q,r,b in zip(qs,base,bits)]}


def enumerate_both():
    summaries=[]
    def family(name,patterns):
        count=phase_count=0;first=None;eligible=None;period_min=None;stream=sha256()
        for qs,bs,coordinate,always_eight in patterns:
            phase_count+=1
            for row in starts(qs,bs,coordinate):
                count+=1
                stream.update((str(row['index'])+'\n').encode())
                period=int(row['index_period'])
                period_min=period if period_min is None else min(period_min,period)
                if first is None or row['index']<first['index']:first=row
                if not always_eight and (eligible is None or row['index']<eligible['index']):eligible=row
        if eligible is not None:
            a=A3+S3*eligible['index']
            assert not eight(a),(name,eligible)
            eligible={**eligible,'root':str(a),'digits':len(str(a)),
                      'complete_eight_predicate':False,'supplementary_minimum':9}
        summaries.append({'family':name,'phase_descriptions':phase_count,'signed_starts':count,
                          'minimum_any':first,'minimum_exact_nine':eligible,
                          'minimum_index_period':str(period_min),'index_stream_sha256':stream.hexdigest()})
    family('five_mod7_rows',((qs,bs,'w',False) for qs in combinations(tuple(sorted(Z+K)),5)
                            for bs in permutations((0,1,2,3,5))))
    family('old_binary',((qs,(0,1),'t',True) for qs in permutations(B8,2)))
    family('binary_refinement',(((q,r,s),(b,1-b,3-b),'t',False)
                                for q in B8 for r,s in permutations(F16,2) for b in (0,1)))
    family('ternary_Q7',((qs,(0,2),'t',set(qs)<=set(D6)) for qs in permutations(D6+R12,2)))
    family('three_mod5_columns',((qs,(0,2,4),'t',False) for qs in permutations(C10+H20,3)))
    assert [r['phase_descriptions'] for r in summaries]==[15120,30,240,20,504]
    assert sum(r['signed_starts'] for r in summaries)==489992
    winner=min((r['minimum_exact_nine'] for r in summaries if r['minimum_exact_nine']),key=lambda r:r['index'])
    assert winner['index']==MINIMUM_INDEX
    return summaries,winner


def prime_trial(q):
    return q>=2 and (q==2 or q%2!=0 and all(q%d for d in range(3,isqrt(q)+1,2)))


def order(q):
    x=1
    for d in range(1,841):
        x=x*2%q
        if x==1:return d
    raise AssertionError(q)


def native_setup(src):
    for file,want in NATIVE_BLOBS.items():
        data=(src/'enterprise_math'/file).read_bytes()
        assert sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==want
    sys.path.insert(0,str(src))
    from enterprise_math.brc_transport import Affine,EffectHistogram,euclidean_digits,recompose
    step=EffectHistogram.from_terms(1,[(1,Affine(((2,),),(1,)),1)])
    twice=step.then(step)
    assert twice.entries==((Fraction(1),Affine(((4,),),(3,)),1),)
    def evaluate(effect,x):
        (point,weight),=effect.evaluate((x,)).items()
        assert weight.entries==((Fraction(1),1),) and point[0].denominator==1
        return int(point[0])
    return step,twice,evaluate,euclidean_digits,recompose


def integer_certificate(a,supplement,dictionary,witness_sets,native,counts):
    assert all(a%q==r for q,r in FIXED43.items())
    assert all(prime_trial(q) for q in dictionary)
    assert a*a-1>max(dictionary)
    orders={q:order(q) for q in dictionary}
    phases={q:next(n for n in range(orders[q]) if a*a*pow(2,n,q)%q==1) for q in dictionary}
    period=lcm(*orders.values());masks=[0]*period
    for bit,q in enumerate(dictionary):
        for n in range(phases[q],period,orders[q]):masks[n]|=1<<bit
    assert all(masks)
    sets=[];terms={}
    for name,witnesses in witness_sets:
        assert len(witnesses)==len(dictionary) and {q for q,n in witnesses}==set(dictionary)
        selected=[]
        for q,n in witnesses:
            f=(a*a<<n)-1;terms[n]=f
            assert f>q and f%q==0
            assert [p for p in dictionary if f%p==0]==[q]
            selected.append({'prime':q,'n':n,'state_hex':hex(f),'cofactor_hex':hex(f//q),
                             'P_free':gcd(f,prod(P))==1})
        checks=[gcd(terms[n],terms[k]) for (_,n),(_,k) in combinations(witnesses,2)]
        assert set(checks)=={1}
        external=[r for r in selected if r['prime'] not in P]
        if name=='P_free':assert len(external)==9 and all(r['P_free'] for r in external)
        counts['witness_entries']+=len(witnesses);counts['gcd_one_checks']+=len(checks)
        sets.append({'name':name,'terms':selected,'maximum_n':max(n for _,n in witnesses),
                     'gcd_one_pairs':len(checks),'all_external_terms_P_free':all(r['P_free'] for r in external)})
    result={'root':str(a),'root_digits':len(str(a)),'supplement':supplement,
            'dictionary':dictionary,'dictionary_size':len(dictionary),'orders':orders,
            'zero_phases':phases,'full_cover_period':period,'uncovered':0,
            'witness_sets':sets,'distinct_retained_integer_terms':len(terms),
            'delta_P':9,'tau':len(dictionary),'native_execution':bool(native)}
    if native:
        step,twice,evaluate,digits,recompose=native
        observed=sorted(set(dictionary)|set(FIXED43));x=previous_even=a*a-1;actual={};stream=sha256()
        for n in range(1,max(terms)+1):
            x=evaluate(step,x);assert x==(a*a<<n)-1;counts['one_step_updates']+=1
            if n%2==0:
                assert evaluate(twice,previous_even)==x;previous_even=x;counts['two_step_evaluations']+=1
            for q in observed:
                quotient,(residue,)=digits(x,(q,));assert (quotient,residue)==divmod(x,q)
                counts['prime_readouts']+=1
                if q in FIXED43:
                    assert residue==(FIXED43[q]**2*pow(2,n,q)-1)%q
                    counts['fixed43_comparisons']+=1
            quotient,rems=digits(x,observed);assert recompose(quotient,rems,observed)==x
            counts['joint_readouts']+=1;counts['joint_recompositions']+=1
            encoded=x.to_bytes((x.bit_length()+7)//8,'big');stream.update(len(encoded).to_bytes(8,'big'));stream.update(encoded)
            if n in terms:actual[n]=x
        assert actual==terms
        result['native']={'observed_prime_count':len(observed),'updates':max(terms),
                          'retained_distinct_terms':len(actual),'integer_stream_sha256':stream.hexdigest(),
                          'last_state_hex':hex(x),'last_state_bits':x.bit_length(),
                          'scope':'Witness intervals only; full covering period is separately checked exactly.'}
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--zero-certificate',type=Path,default=HERE.parent/'zero'/'zero_nine_bounded_minimum_certificate.json')
    parser.add_argument('--one-certificate',type=Path,default=HERE.parent/'one'/'one_w_minimum_certificate.json')
    parser.add_argument('--source-dir',type=Path)
    parser.add_argument('--output',type=Path,default=HERE/'global_minimum_certificate.json')
    args=parser.parse_args();started=time.monotonic()
    families,winner=enumerate_both();a=int(winner['root'])
    zero=json.loads(args.zero_certificate.read_text());one=json.loads(args.one_certificate.read_text())
    assert zero['status']=='PASS' and zero['all_47_geometries_processed']
    assert int(zero['initial_strict_upper_bound_index'])==MINIMUM_INDEX
    assert not zero['exact_nine_found_below_initial_bound'] and zero['distinct_ordinary_root_candidates']==0
    one_a=int(one['global_one_W_minimum']['root'])
    assert one['status'].startswith('PASS_') and one['signed_CRT_starts']==307200 and one_a>a
    assert one['supplementary_minimum']==9 and one['unrestricted_total_minimum']==28
    counts=dict(one_step_updates=0,two_step_evaluations=0,prime_readouts=0,joint_readouts=0,
                joint_recompositions=0,fixed43_comparisons=0,witness_entries=0,gcd_one_checks=0)
    native=native_setup(args.source_dir) if args.source_dir else None
    supplement=[5,13,19,73,38737,487824887233,1153,3457,816769]
    primary=integer_certificate(a,supplement,sorted(set(P)|set(supplement)),[('P_free',GLOBAL_WITNESSES)],native,counts)
    old=one['coverage_and_coprime_certificate']
    short=[(r['assigned_prime'],r['exponent']) for r in old['selected_terms']]
    strong=[(r['assigned_prime'],r['exponent']) for r in old['P_free_refinement_seed']['selected_terms']]
    one_supplement=[5,13,73,29,43,1429,5419,92737,649657]
    comparison=integer_certificate(one_a,one_supplement,old['optimal_reduced_dictionary'],
                                   [('short',short),('P_free',strong)],native,counts)
    result={'schema':'RIESEL_R3_GLOBAL_COST_NINE_MINIMUM_V15','status':'PASS','R3':{'A3':str(A3),'S3':str(S3)},
            'canonical_both_W_families':families,'canonical_signed_starts':489992,
            'global_minimum':winner,'minimum_scope':'All positive a in R3 with delta_P(a)=9.',
            'branch_dependencies':{'zero':{'path':args.zero_certificate.name,'sha256':sha256(args.zero_certificate.read_bytes()).hexdigest(),
                                   'classification':'../zero/proof.md','no_smaller_root':True},
                                  'one':{'path':args.one_certificate.name,'sha256':sha256(args.one_certificate.read_bytes()).hexdigest(),
                                   'classification':'../one/proof.md','minimum':str(one_a)},
                                  'both':{'classification':'../both/proof.md','all_canonical_starts_recomputed':True}},
            'exact_total_certificates':[primary,comparison],'actual_counts':counts,
            'distinct_roots':2,'witness_sets':3,'native_execution':bool(native),
            'native_source_commit':NATIVE_COMMIT,'native_source_blobs':NATIVE_BLOBS,
            'native_semantics':'Full integer at fixed Heartbeat X6 anchor; positive singleton BRC; weight and multiplicity one; exact future readouts and joint recomposition.',
            'independent_project_review':False,'elapsed_seconds':time.monotonic()-started}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','root':str(a),'digits':len(str(a)),'index':MINIMUM_INDEX,
                      'delta':9,'tau':29,'comparison_tau':28,'actual_counts':counts,
                      'native_execution':bool(native),'elapsed_seconds':result['elapsed_seconds']}))


if __name__=='__main__':main()
