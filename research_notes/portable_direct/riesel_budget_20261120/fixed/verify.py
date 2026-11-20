"""Verify the fixed-root v6 results without using an optimization solver.

Default: independently recompute every G_q,E_q for 1 <= q <= 1027 in GMP,
enumerating ALL proper divisors in the saturation step.  Then verify all pairs
of two 1028-term windows, the packing/partition certificates, the joint-gcd gap,
the CRT factorization, and the pinned native one-register BRC projections.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import itertools
import json
from math import gcd,isqrt,lcm,prod
from pathlib import Path
import subprocess
import sys
import tempfile
import time

BASE=Path(__file__).resolve().parent

def read(name):return json.loads((BASE/name).read_text())
def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def prime_divisors(n):
    out=[];p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:out.append(n)
    return out

def recompute_profiles(A,S,packets):
    out=[]
    for row in packets:
        q,e=row['q'],int(row['E'])
        if e==1:continue
        r=pow(2,S,e);x=(A-1)%e;phases=[]
        for c in range(q):
            common=gcd(x,e)
            if common>1:phases.append({'phase':c,'gcd':str(common)})
            x=(r*x+r-1)%e
        assert x==(A-1)%e
        out.append({'q':q,'E':str(e),'phases':phases})
    return out

def window_graph(A,S,t,packets,profiles):
    size=1028;edges={};pairs=0
    for row in packets:
        d,g=row['q'],int(row['G']);pairs+=size-d
        if g==1:continue
        r=pow(2,S,g);x=(A*pow(2,S*(t+1),g)-1)%g
        for i in range(1,size-d+1):
            common=gcd(x,g)
            if common>1:edges[i,i+d]=common
            x=(r*x+r-1)%g
        assert x==(A*pow(2,S*(t+size-d+1),g)-1)%g
    phase_edges=set()
    for row in profiles:
        q=row['q']
        for phase in row['phases']:
            first=(phase['phase']-t)%q or q
            vertices=list(range(first,size+1,q))
            phase_edges.update(itertools.combinations(vertices,2))
    assert set(edges)==phase_edges
    assert pairs==1028*1027//2
    return edges,pairs

def encoded_edges(edges):
    return [{'i':i,'j':j,'gcd':str(g)} for (i,j),g in sorted(edges.items())]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source-dir',type=Path)
    ap.add_argument('--threads',type=int,default=4)
    ap.add_argument('--reuse-recomputed-packets',type=Path,
                    help='Compare an already independently recomputed full GMP table; default recomputes from scratch.')
    ap.add_argument('--output',type=Path,default=BASE/'verification_results.json')
    args=ap.parse_args();start=time.monotonic()
    source=read('input.json');a,A,S=map(int,(source['a'],source['A'],source['S']))
    assert a==690786768637635218740714348513373826260012289
    assert S==7543152493250337317777998389729624720196910046042166547544586890203606088003198926478506067947700
    assert A==a*a*2**66 and S%2==0 and source['n_initial']==66
    packets=read('period_dictionary.json')
    assert [r['q'] for r in packets]==list(range(1,1028))
    packet_start=time.monotonic()
    if args.reuse_recomputed_packets:
        raw=args.reuse_recomputed_packets.read_text()
        backend='comparison_to_supplied_independent_GMP_full_recomputation'
    else:
        with tempfile.TemporaryDirectory(prefix='riesel_fixed_v6_') as td:
            binary=Path(td)/'verify_packets'
            subprocess.run(['g++','-O2','-std=c++17','-fopenmp',
                            str(BASE/'verify_packets.cpp'),'-lgmpxx','-lgmp','-o',str(binary)],check=True)
            raw=subprocess.check_output([str(binary),str(A),str(S),'1','1027',str(args.threads)],text=True)
        backend='independent_GMP_full_recomputation_in_this_run'
    recomputed=[{'q':int(q),'G':g,'E':e} for q,g,e in
                (line.split() for line in raw.splitlines())]
    assert recomputed==packets
    packet_seconds=time.monotonic()-packet_start
    print('All 1027 exact all-prime packets matched',flush=True)
    profiles=recompute_profiles(A,S,packets)
    assert profiles==read('phase_profiles.json')
    structure=read('period_structure.json')
    active=[r['q'] for r in profiles]
    assert active==structure['active_periods'] and len(active)==108
    assert sum(map(lambda r:len(r['phases']),profiles))==197
    assert min(active)==257
    composites=[q for q in active if not prime(q)]
    assert composites==structure['composite_active_periods']==[604,698,778,842,866,878,898]
    assert structure['composite_phase_rows']==[r for r in profiles if r['q'] in composites]
    bases=structure['odd_prime_CRT_moduli']
    assert len(bases)==103 and len(set(bases))==len(bases)
    assert all(p%2 and prime(p) for p in bases)
    assert set(bases)==(set(active)-set(composites))|{151,389}
    modulus=4*prod(bases)
    assert modulus==int(structure['common_graph_translation_period'])==lcm(*active)
    assert all(q in bases or (q==4*151) or (q%2==0 and q//2 in bases) for q in active)
    w=read('window_certificate.json');t=int(w['offset'])
    assert t==36336993984980188772089880815813258699155881359803388560850767447862968334159792609944272211396
    edges,pairs=window_graph(A,S,t,packets,profiles)
    assert encoded_edges(edges)==w['exact_nonunit_pair_gcds']
    independent=set(w['independent_set'])
    assert len(independent)==len(w['independent_set'])==892
    assert independent<=set(range(1,1029))
    assert all(not {i,j}<=independent for i,j in edges)
    blocks=w['joint_gcd_partition'];seen=set();nontrivial_blocks=0
    assert len(blocks)==892
    for block in blocks:
        assert block and len(set(block))==len(block)
        assert set(block).isdisjoint(seen);seen.update(block)
        assert len(independent&set(block))==1
        if len(block)>1:
            common=0
            for j in block[1:]:
                pair=tuple(sorted((block[0],j)))
                assert pair in edges;common=gcd(common,edges[pair])
            assert common>1;nontrivial_blocks+=1
    assert seen==set(range(1,1029))
    assert w['maximum_pairwise_coprime_size']==w['minimum_prime_cover_size']==892
    assert w['any_full_cover_minimum_primes_outside_old_P']==892
    assert w['if_old_P_is_retained_minimum_total_primes']==912
    print('1028-window packing and joint-gcd partition both have size 892',flush=True)
    joint=read('joint_certificate.json');tj=int(joint['offset'])
    assert tj==17887629
    assert all(tj%int(q)==r for q,r in joint['offset_congruences'].items())
    jedges,jpairs=window_graph(A,S,tj,packets,profiles)
    selected=set(joint['selected_vertices']);isolates=set(joint['isolated_vertices'])
    triangle=set(joint['triangle_vertices'])
    assert len(selected)==882 and len(isolates)==879 and triangle=={1,272,555}
    assert not isolates&triangle and selected==isolates|triangle
    induced={(i,j):g for (i,j),g in jedges.items() if {i,j}<=selected}
    assert encoded_edges(induced)==joint['exact_nonunit_pair_gcds']
    assert induced=={(1,272):1627,(1,555):1109,(272,555):1242937}
    assert gcd(*induced.values())==1
    assert all(prime(p) for p in induced.values())
    assert joint['two_triangle_cover_primes']==[1627,1109]
    assert len(joint['maximum_independent_set'])==880
    assert set(joint['maximum_independent_set'])==isolates|{1}
    assert joint['maximum_pairwise_coprime_size']==880
    assert joint['minimum_prime_cover_size']==881
    print('882-term induced set: 879 isolates and a non-joint triangle, alpha=880 tau=881',flush=True)
    old=[]
    for row in source['original_twenty_channels']:
        p,o=row['p'],row['order'];assert prime(p)
        assert pow(2,o,p)==1 and all(pow(2,o//r,p)!=1 for r in prime_divisors(o))
        q=o//gcd(o,S)
        assert all((A*pow(2,S*i,p)-1)%p for i in range(q))
        old.append(p)
    assert len(set(old))==20
    if args.source_dir is None:
        args.source_dir=next((p/name for p in [BASE,*BASE.parents]
                             for name in ('src','vendor_src')
                             if (p/name/'enterprise_math/brc_transport.py').exists()),None)
    assert args.source_dir is not None,'Pass --source-dir for the pinned native src or vendor_src.'
    verified_blobs={}
    for name,expected in source['project_source_blobs'].items():
        data=(args.source_dir/'enterprise_math'/name).read_bytes()
        blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
        assert blob==expected, f'Native source pin mismatch: {name}; pass --source-dir for the fixed source snapshot.'
        verified_blobs[name]=blob
    sys.path.insert(0,str(args.source_dir))
    from enterprise_math.brc_transport import Affine,EffectHistogram,euclidean_digits
    def native(packet,x):
        (point,weight),=packet.evaluate((x,)).items()
        assert weight.entries==((Fraction(1),1),) and point[0].denominator==1
        return int(point[0])
    step=EffectHistogram.from_terms(1,[(1,Affine(((4,),),(3,)),1)])
    state=a*a-1
    for _ in range(33):state=native(step,state)
    assert state+1==A
    projections=0
    for g in sorted({int(r['G']) for r in packets if r['G']!='1'}):
        r=pow(2,S,g)
        packet=EffectHistogram.from_terms(1,[(1,Affine(((r,),),(r-1,)),1)])
        for offset in (t,tj):
            x=(A*pow(2,S*offset,g)-1)%g
            observed=euclidean_digits(native(packet,x),(g,))[1][0]
            assert observed==(A*pow(2,S*(offset+1),g)-1)%g
            projections+=1
    result={'schema':'RIESEL_FIXED_OLD_ROOT_V6_FULL_VERIFICATION',
            'researcher_id':'EM-DIRECT-970E1C','activity_id':'RA-D2EC212845B63844081F9A14',
            'all_assertions_passed':True,'packet_backend':backend,
            'exact_packet_range':[1,1027],'exact_packets_verified':1027,
            'independent_algorithm':'A^q from scratch; saturate all proper divisors, in contrast to discovery maximal proper divisors.',
            'packet_recomputation_seconds':packet_seconds,
            'active_period_count':108,'active_phase_count':197,
            'composite_active_periods':composites,'CRT_local_odd_prime_coordinates':103,
            'complete_pair_count_two_ambient_windows':pairs+jpairs,
            'main_window_exact_nonunit_pair_count':len(edges),
            'main_window_maximum_pairwise_coprime_size':892,
            'main_window_minimum_prime_cover_size':892,
            'main_window_non_singleton_partition_blocks':nontrivial_blocks,
            'joint_example_vertex_count':882,'joint_example_exact_nonunit_pair_count':3,
            'joint_example_maximum_pairwise_coprime_size':880,
            'joint_example_minimum_prime_cover_size':881,
            'old_twenty_entire_relative_cycles_verified':old,
            'all_terms_composite':'(a*2^(33+S*i/2)-1)*(a*2^(33+S*i/2)+1)',
            'project_source_commit':source['project_source_commit'],
            'project_source_blobs':verified_blobs,'native_projected_updates_verified':projections,
            'native_BRC':'Unchanged single internal integer register, x -> 4x+3; no added physical axis or time interpretation.',
            'any_full_cover_minimum_primes_outside_old_P':892,
            'if_old_P_is_retained_minimum_total_primes':912,
            'scope':'Exact claims for two specified finite sets only. Full fixed-root finite-cover existence and the optimum over all 1028-window translations remain undetermined.',
            'verification_status':'AUTHOR_EXACT_RECOMPUTATION_NOT_INDEPENDENT_PROJECT_REVIEW',
            'elapsed_seconds':time.monotonic()-start}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['all_assertions_passed','main_window_minimum_prime_cover_size',
         'joint_example_minimum_prime_cover_size','native_projected_updates_verified','elapsed_seconds']}),flush=True)

if __name__=='__main__':main()
