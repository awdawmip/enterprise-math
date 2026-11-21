"""Exact v7 verification, reusing the pinned v6 all-prime G/E dictionary.

No optimization solver or prime-factorization cutoff is used. The large G/E
extraction was independently performed in v6 and is an explicit dependency.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib,itertools,json
from math import gcd,lcm,prod
from pathlib import Path
import subprocess,sys,tempfile,time

BASE=Path(__file__).resolve().parent

def locate_prior():
    for parent in [BASE,*BASE.parents]:
        for relative in ('research_notes/portable_direct/riesel_budget_20261120/fixed',
                         'riesel_budget_20261120/fixed'):
            path=parent/relative
            if (path/'period_dictionary.json').exists():return path
    raise FileNotFoundError('Pass --prior-dir for the v6 fixed artifact directory.')

def load(path):return json.loads(path.read_text())

def graph(A,S,t,packets):
    edges={};pairs=0
    for row in packets:
        d,g=row['q'],int(row['G']);pairs+=1028-d
        if g==1:continue
        r=pow(2,S,g);x=(A*pow(2,S*(t+1),g)-1)%g
        for i in range(1,1028-d+1):
            h=gcd(x,g)
            if h>1:edges[i,i+d]=h
            x=(r*x+r-1)%g
    return edges,pairs

def encode_edges(edges):
    return [{'i':i,'j':j,'gcd':str(g)} for (i,j),g in sorted(edges.items())]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--prior-dir',type=Path)
    ap.add_argument('--source-dir',type=Path)
    ap.add_argument('--output',type=Path,default=BASE/'verification_results.json')
    args=ap.parse_args();start=time.monotonic()
    prior=args.prior_dir or locate_prior()
    source=load(prior/'input.json');packets=load(prior/'period_dictionary.json')
    profiles=load(prior/'phase_profiles.json');structure=load(prior/'period_structure.json')
    w=load(BASE/'window_certificate.json');bound=load(BASE/'bound_certificate.json')
    a,A,S=map(int,(source['a'],source['A'],source['S']))
    assert A==a*a*2**66 and S%2==0
    assert [r['q'] for r in packets]==list(range(1,1028))
    assert [w[k] for k in ('a','A','S')]==[source[k] for k in ('a','A','S')]
    t=int(w['offset']);assert t>=0 and t%4==w['t_mod_4']
    coordinates={int(p):r for p,r in w['odd_prime_coordinates'].items()}
    assert sorted(coordinates)==structure['odd_prime_CRT_moduli']
    assert all(t%p==r for p,r in coordinates.items())
    assert int(w['CRT_modulus'])==4*prod(coordinates)==lcm(*(r['q'] for r in profiles))
    assert 0<=t<int(w['CRT_modulus'])
    edges,pairs=graph(A,S,t,packets)
    assert pairs==527878 and encode_edges(edges)==w['exact_nonunit_pair_gcds']
    groups=[];phase_edges=set()
    for row in profiles:
        q=row['q'];e=int(row['E']);r=pow(2,S,e);x=(A-1)%e;phases=[]
        for c in range(q):
            h=gcd(x,e)
            if h>1:phases.append({'phase':c,'gcd':str(h)})
            x=(r*x+r-1)%e
        assert phases==row['phases'] and x==(A-1)%e
        for phase in phases:
            first=(phase['phase']-t)%q or q
            vs=list(range(first,1029,q))
            if len(vs)>1:
                groups.append({'q':q,'phase':phase['phase'],'vertices':vs,'packet_gcd':phase['gcd']})
                phase_edges.update(itertools.combinations(vs,2))
    assert phase_edges==set(edges) and groups==w['nontrivial_prime_incidence_classes']
    independent=set(w['independent_set']);blocks=w['joint_gcd_partition']
    assert len(independent)==len(w['independent_set'])==len(blocks)==970
    assert all(not {i,j}<=independent for i,j in edges)
    seen=set();hist={}
    for b in blocks:
        assert b and len(set(b))==len(b) and set(b).isdisjoint(seen)
        seen.update(b);hist[len(b)]=hist.get(len(b),0)+1
        assert len(independent&set(b))==1
        if len(b)>1:
            assert gcd(*(edges[tuple(sorted((b[0],j)))] for j in b[1:]))>1
    assert seen==set(range(1,1029))
    assert w['maximum_pairwise_coprime_size']==w['minimum_prime_cover_size']==970
    assert w['any_full_cover_minimum_primes_outside_old_P']==970
    assert w['if_old_P_is_retained_minimum_total_primes']==990
    # Exact all-future old-channel escape, independent of the chosen offset.
    for row in source['original_twenty_channels']:
        p,o=row['p'],row['order'];q=o//gcd(o,S)
        assert all((A*pow(2,S*i,p)-1)%p for i in range(q))
    # Every clique from each family intersects an entire other family at most once.
    qs=bound['relative_periods'];cs=bound['phases']
    assert qs==[257,271,277] and cs==[[0,88],[4,11,116],[78,97,243]]
    for q,c in zip(qs,cs):
        assert [x['phase'] for x in next(r for r in profiles if r['q']==q)['phases']]==c
        assert 1028//q>=3 and (1028+q-1)//q<=4
    for i,j in itertools.permutations(range(3),2):
        differences={(u-v)%qs[j] for u in cs[j] for v in cs[j]}
        assert all((m*qs[i])%qs[j] not in differences for m in (-3,-2,-1,1,2,3))
    # This proves one private vertex per clique for every coordinate tuple.
    with tempfile.TemporaryDirectory(prefix='riesel_v7_bound_') as directory:
        binary=Path(directory)/'three_period_bound'
        subprocess.run(['g++','-O3','-std=c++17',str(BASE/'three_period_bound.cpp'),'-o',str(binary)],check=True)
        actual=json.loads(subprocess.check_output([str(binary)],text=True))
    for key,value in actual.items():assert bound[key]==value
    assert actual['coordinate_tuples']==257*271*277==19292219
    assert sum(actual['union_size_histogram'].values())==actual['coordinate_tuples']
    assert actual['minimum_union_size']==25
    assert actual['alpha_maximum_for_three_period_subgraph']==1028-25+8==1011
    # Reproduce the exact minimizing eight-class witness independently in Python.
    clique_rows=[]
    for q,c,shift in zip(qs,cs,actual['minimizing_coordinates']):
        for phase in c:
            first=(phase-shift)%q or q
            clique_rows.append(set(range(first,1029,q)))
    assert len(set.union(*clique_rows))==25
    for i,c in enumerate(clique_rows):assert c-set.union(*(d for j,d in enumerate(clique_rows) if j!=i))
    # Native projected recurrence for the new offset, at the existing source pins.
    if args.source_dir is None:
        args.source_dir=next((p/name for p in [BASE,*BASE.parents]
             for name in ('vendor_src','src') if (p/name/'enterprise_math/brc_transport.py').exists()),None)
    assert args.source_dir is not None,'Pass --source-dir for the pinned native modules.'
    verified_blobs={}
    for name,expected in source['project_source_blobs'].items():
        raw=(args.source_dir/'enterprise_math'/name).read_bytes()
        actual_blob=hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest()
        assert actual_blob==expected;verified_blobs[name]=actual_blob
    sys.path.insert(0,str(args.source_dir))
    from enterprise_math.brc_transport import Affine,EffectHistogram,euclidean_digits
    steps=0
    for row in profiles:
        modulus=int(row['E']);r=pow(2,S,modulus)
        effect=EffectHistogram.from_terms(1,[(1,Affine(((r,),),(r-1,)),1)])
        x=(A*pow(2,S*t,modulus)-1)%modulus
        for j in (1,2):
            (point,weight),=effect.evaluate((x,)).items()
            assert weight.entries==((Fraction(1),1),) and point[0].denominator==1
            x=int(euclidean_digits(int(point[0]),(modulus,))[1][0])
            assert x==(A*pow(2,S*(t+j),modulus)-1)%modulus;steps+=1
    result={'status':'PASS','dictionary_dependency_commit':w['inherited_science_commit'],
            'dictionary_policy':'Reused unchanged v6 exact all-prime G/E extraction; no prime-size cutoff; raw packet gcd retained.',
            'exact_pair_checks':pairs,'nonunit_pair_count':len(edges),
            'nontrivial_prime_incidence_classes':len(groups),
            'independent_set_size':len(independent),'joint_partition_size':len(blocks),
            'partition_size_histogram':hist,'native_projected_updates':steps,
            'native_source_blobs':verified_blobs,'all_translation_bound':actual,
            'seconds':round(time.monotonic()-start,6),
            'review_status':'Author verification; not independent project Review or formal proof checking.'}
    args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))

if __name__=='__main__':main()
