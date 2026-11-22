"""Verify v8 fixed-root certificates without any optimization solver.

The unchanged 1..1027 dictionary is an explicit verified v6 dependency.
The default recomputes precisely the new 1028..2055 entries with GMP.
An already completed exact run can be reused with --reuse-new-packets.
All finite-window pairs are then checked using full, unfactored integer gcds.
"""
from __future__ import annotations
import argparse,hashlib,itertools,json,subprocess,sys,tempfile,time
from fractions import Fraction
from math import gcd,lcm,prod
from pathlib import Path

BASE=Path(__file__).resolve().parent
def load(p):return json.loads(p.read_text())
def locate_prior():
    for parent in [BASE,*BASE.parents]:
        for relative in ('research_notes/portable_direct/riesel_budget_20261120/fixed',
                         'riesel_budget_20261120/fixed'):
            p=parent/relative
            if (p/'period_dictionary.json').exists():return p
    raise FileNotFoundError('Pass --prior-dir for the pinned v6 fixed artifacts.')

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--prior-dir',type=Path)
    ap.add_argument('--source-dir',type=Path)
    ap.add_argument('--threads',type=int,default=8)
    ap.add_argument('--reuse-new-packets',type=Path)
    ap.add_argument('--output',type=Path,default=BASE/'verification_results.json')
    args=ap.parse_args();start=time.monotonic()
    prior=args.prior_dir or locate_prior()
    source=load(prior/'input.json');old=load(prior/'period_dictionary.json')
    new=load(BASE/'new_period_dictionary.json');w=load(BASE/'window_certificate.json')
    a,A,S=map(int,(source['a'],source['A'],source['S']))
    assert a==690786768637635218740714348513373826260012289
    assert S==7543152493250337317777998389729624720196910046042166547544586890203606088003198926478506067947700
    assert A==a*a*2**66 and S%2==0
    assert [w[k] for k in ('a','A','S')]==[source[k] for k in ('a','A','S')]
    size=w['window_size'];assert size==2056
    assert [r['q'] for r in old]==list(range(1,1028))
    assert [r['q'] for r in new]==list(range(1028,size))
    packet_start=time.monotonic()
    if args.reuse_new_packets:
        raw=args.reuse_new_packets.read_text()
        backend='Reused actual exact GMP extension output from this research round.'
    else:
        with tempfile.TemporaryDirectory(prefix='riesel_fixed_v8_') as directory:
            binary=Path(directory)/'extend_packets'
            subprocess.run(['g++','-O2','-std=c++17','-fopenmp',str(BASE/'extend_packets.cpp'),
                            '-lgmpxx','-lgmp','-o',str(binary)],check=True)
            raw=subprocess.check_output([str(binary),str(A),str(S),'1028',str(size-1),
                                         str(args.threads)],text=True)
        backend='Exact GMP extension recomputed in this verifier run.'
    actual=sorted(({'q':int(q),'G':g,'E':e} for q,g,e in
                   (line.split() for line in raw.splitlines())),key=lambda r:r['q'])
    assert actual==new
    packet_seconds=time.monotonic()-packet_start
    packets=old+new
    profiles=load(prior/'phase_profiles.json')
    new_profiles=[]
    for row in new:
        q,e=row['q'],int(row['E'])
        if e==1:continue
        r=pow(2,S,e);x=(A-1)%e;phases=[]
        for c in range(q):
            h=gcd(x,e)
            if h>1:phases.append({'phase':c,'gcd':str(h)})
            x=(r*x+r-1)%e
        assert x==(A-1)%e
        if phases:new_profiles.append({'q':q,'E':str(e),'phases':phases})
    profiles=profiles+new_profiles
    assert profiles==load(BASE/'phase_profiles.json')
    t=int(w['offset']);assert t>=0
    construction=w['offset_construction']
    if 'CRT_modulus' in construction:
        two=construction['power_two_modulus']
        coordinates={int(p):v for p,v in construction['odd_coprime_coordinates'].items()}
        assert all(gcd(p,q)==1 for p,q in itertools.combinations(coordinates,2))
        assert t%two==construction['t_mod_power_two']
        assert all(t%p==v for p,v in coordinates.items())
        assert int(construction['CRT_modulus'])==two*prod(coordinates)==lcm(*(r['q'] for r in profiles))
        assert 0<=t<int(construction['CRT_modulus'])
    # Complete all-prime gcd reconstruction, not a search over small primes.
    edges={};pairs=0
    for row in packets:
        d,g=row['q'],int(row['G']);pairs+=size-d
        if g==1:continue
        r=pow(2,S,g);x=(A*pow(2,S*(t+1),g)-1)%g
        for i in range(1,size-d+1):
            h=gcd(x,g)
            if h>1:edges[i,i+d]=h
            x=(r*x+r-1)%g
    assert pairs==size*(size-1)//2==2112540
    encoded=[{'i':i,'j':j,'gcd':str(g)} for (i,j),g in sorted(edges.items())]
    assert encoded==w['exact_nonunit_pair_gcds']
    classes=[];phase_edges=set()
    for row in profiles:
        q=row['q']
        for phase in row['phases']:
            first=(phase['phase']-t)%q or q
            vertices=list(range(first,size+1,q))
            if len(vertices)>1:
                classes.append({'q':q,'phase':phase['phase'],'vertices':vertices,
                                'packet_gcd':phase['gcd']})
                phase_edges.update(itertools.combinations(vertices,2))
    assert phase_edges==set(edges)
    assert classes==w['nontrivial_prime_incidence_classes']
    selected=set(w['independent_set']);blocks=w['joint_gcd_partition']
    assert len(selected)==len(w['independent_set'])==w['pairwise_coprime_lower_bound']
    assert selected<=set(range(1,size+1))
    assert all(not {i,j}<=selected for i,j in edges)
    seen=set();hist={}
    for block in blocks:
        assert block and len(set(block))==len(block) and seen.isdisjoint(block)
        seen.update(block);hist[len(block)]=hist.get(len(block),0)+1
        if len(block)>1:
            assert gcd(*(edges[tuple(sorted((block[0],j)))] for j in block[1:]))>1
    assert seen==set(range(1,size+1))
    assert len(blocks)==w['finite_window_prime_cover_upper_bound']
    if len(selected)==len(blocks):assert w['finite_window_exact_alpha_tau']==len(selected)
    else:assert w['finite_window_exact_alpha_tau'] is None
    assert w['any_full_cover_minimum_primes_outside_old_P']==len(selected)
    assert w['if_old_P_is_retained_minimum_total_primes']==len(selected)+20
    # Entire old-channel relative cycles escape, for every orbit position.
    for row in source['original_twenty_channels']:
        p,o=row['p'],row['order'];q=o//gcd(o,S)
        assert all((A*pow(2,S*i,p)-1)%p for i in range(q))
    # The current offset's projections use the unchanged native BRC semantics.
    if args.source_dir is None:
        args.source_dir=next((p/n for p in [BASE,*BASE.parents] for n in ('vendor_src','src')
                if (p/n/'enterprise_math/brc_transport.py').exists()),None)
    assert args.source_dir is not None,'Pass --source-dir for the pinned native modules.'
    native_blobs={}
    for name,expected in source['project_source_blobs'].items():
        data=(args.source_dir/'enterprise_math'/name).read_bytes()
        blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
        assert blob==expected;native_blobs[name]=blob
    sys.path.insert(0,str(args.source_dir))
    from enterprise_math.brc_transport import Affine,EffectHistogram,euclidean_digits
    steps=0
    for row in profiles:
        e=int(row['E']);r=pow(2,S,e)
        packet=EffectHistogram.from_terms(1,[(1,Affine(((r,),),(r-1,)),1)])
        x=(A*pow(2,S*t,e)-1)%e
        for j in (1,2):
            (point,weight),=packet.evaluate((x,)).items()
            assert weight.entries==((Fraction(1),1),) and point[0].denominator==1
            x=int(euclidean_digits(int(point[0]),(e,))[1][0])
            assert x==(A*pow(2,S*(t+j),e)-1)%e;steps+=1
    result={'status':'PASS','inherited_dictionary_commit':w['inherited_dictionary_commit'],
            'inherited_dictionary_interval':[1,1027],'new_exact_dictionary_interval':[1028,size-1],
            'new_exact_packets_verified':len(new),'packet_backend':backend,
            'packet_verification_seconds':packet_seconds,
            'prime_size_cutoff':None,'unfactored_full_packets_retained':True,
            'active_period_count':len(profiles),'active_phase_count':sum(len(r['phases']) for r in profiles),
            'new_active_period_count':len(new_profiles),
            'exact_pair_checks':pairs,'nonunit_pair_count':len(edges),
            'nontrivial_prime_incidence_classes':len(classes),
            'independent_set_size':len(selected),'joint_partition_size':len(blocks),
            'partition_size_histogram':hist,'finite_window_exact_alpha_tau':w['finite_window_exact_alpha_tau'],
            'any_full_cover_minimum_primes_outside_old_P':len(selected),
            'if_old_P_is_retained_minimum_total_primes':len(selected)+20,
            'native_projected_updates':steps,'native_source_blobs':native_blobs,
            'seconds':round(time.monotonic()-start,6),
            'scope':w['scope'],'review_status':'Author verification, not independent project Review or formal proof checking.'}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)

if __name__=='__main__':main()
