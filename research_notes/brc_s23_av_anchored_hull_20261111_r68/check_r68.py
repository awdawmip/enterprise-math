"""R68 exact anchor-overlap hull cache, bounded LRU and matched-workload tests.
Uses original R67 verified auxiliary rational-circle kernel; no native BRC-physics claim.
Python >=3.10; standard library only. Frozen science pin unchanged.
"""
import sys, json, tracemalloc, time
from pathlib import Path
from fractions import Fraction as F
from random import Random
from collections import Counter, OrderedDict
_base=Path(__file__).resolve().parent
_candidates=(_base/'r67src',_base.parent/'brc_s23_av_certificate_cache_20261111_r67')
_kernel_dir=next((q for q in _candidates if (q/'check_r67.py').is_file()),None)
if _kernel_dir is None:raise ImportError('R67 exact kernel check_r67.py missing; use same branch or bundle')
sys.path.insert(0,str(_kernel_dir))
import check_r67 as r
PIN='43ec6098b1330ae86d0a7863be336c5d97f6ef34'

class HullLRU:
    def __init__(self,cap=None):
        self.cap=cap
        self.data=OrderedDict() # (immutable subtree identity, exact query signature) -> one certified anchor-overlap hull
        self.metrics=Counter()
    def excluded(self,n,a,L,U,j,x,m,z,nxt,stat):
        assert L<=a<=U
        key=(n,(a,j,x,m,z,nxt))
        got=self.data.get(key)
        if got is not None:
            self.data.move_to_end(key)
            if got[0]<=L and U<=got[1]:
                stat['cache_hits']+=1
                stat['saved_events']+=n.count
                self.metrics['hits']+=1
                return True
        v=r.exclusion(n,a,L,U,j,x,z,nxt,stat)
        if v:
            if got is None:
                self.data[key]=(L,U)
                self.metrics['insertions']+=1
            else:
                # Intervals both contain anchor a, so their union is precisely the hull.
                self.data[key]=(min(got[0],L),max(got[1],U))
                self.metrics['hull_extensions']+=int(self.data[key]!=got)
            self.data.move_to_end(key)
            if self.cap is not None:
                while len(self.data)>self.cap:
                    self.data.popitem(last=False)
                    self.metrics['evictions']+=1
        return v

# R62/R64-style exact competitor scan under the same stable original history.
def linear_certify(ev,a,L,U,m,j,x,z,st):
    if not L<=a<=U:return ('INCONCLUSIVE',None)
    h=r.history(a,m);labs=[v for _,v in h]
    if not all(r.avoid(F(0),F(v-w),L,U) for v,w in zip(labs,labs[1:]+labs[:1])):
        return ('INCONCLUSIVE',None)
    nxt=labs[(labs.index(z)+1)%m]
    w=r.oracle(a,ev,m,j,x,z)
    st['source_candidates']+=sum(w is None or t>=w for t,b in ev)
    # Every newer event has fixed membership in the target arc; the nominal winner, if any, stays inside.
    for t,b in ev:
        if w is None or t>=w:
            st['source_boundary_tests']+=2
            if not r.avoid(x,F(t-j-z),L,U) or not r.avoid(x,F(t-j-nxt),L,U):
                return ('INCONCLUSIVE',w)
    return ('CERTIFIED',w)

# Full time, precision and output scopes are identical for all three methods.
def run_cases(cap=64,count=80,seed=68001,checks=5):
    rng=Random(seed)
    old=r.Cache(); hull=HullLRU(cap)
    st0,st1,st2,slin=Counter(),Counter(),Counter(),Counter()
    results=Counter(); total_s=[0.,0.,0.,0.]
    # Bit-length envelope, not a claim of a complete bit-operation ledger.
    widths={'time':0,'theta_den':0,'interval_den':0,'observation_den':0}
    tracemalloc.start()
    peak0=tracemalloc.get_traced_memory()[1]
    for case in range(count):
        den=rng.choice([101,103,107,109,113,127,131])
        a=F(rng.randrange(3,den-3),den)
        m=rng.randrange(2,11);j=rng.randrange(70,170)
        x=F(rng.randrange(2,39),rng.randrange(41,95))
        root=None; population=[];used=set()
        for i in range(rng.randrange(20,48)):
            t=rng.randrange(-80,j); b=i%13
            if (t,b) in used:continue
            used.add((t,b));population.append((t,b))
            root=r.add(root,(r.fr(t*a),t,b),rng.getrandbits(96))
        assert len(population)>10
        versions=[(root,list(population))]
        t=population[0][0];newb=20000+case
        newroot=r.add(root,(r.fr(t*a),t,newb),rng.getrandbits(96))
        versions.append((newroot,population+[(t,newb)]))
        versions.append((r.erase(newroot,(r.fr(t*a),t,newb)),list(population)))
        widths['time']=max(widths['time'],*(abs(t).bit_length() for t,b in population))
        widths['theta_den']=max(widths['theta_den'],a.denominator.bit_length())
        widths['observation_den']=max(widths['observation_den'],x.denominator.bit_length())
        # 4 asymmetric windows, all share anchor, plus deeper nested queries.
        ep=F(1,10**7)
        intervals=[(a-8*ep,a+ep),(a-ep,a+8*ep),(a-4*ep,a+4*ep),
                   (a-8*ep,a+8*ep),(a-ep/16,a+ep/16),(a-ep/64,a+ep/64)]
        for vi,(version,events) in enumerate(versions):
            # revisit stable signature and changed label/observation, same immutable subtree
            z=rng.randrange(m)
            qs=[(z,x)]*len(intervals)
            if vi==2:qs += [( (z+1)%m,x), (z,x+F(1,1000003))]
            for qid,(zz,xx) in enumerate(qs):
                L,U=intervals[qid%len(intervals)]
                widths['interval_den']=max(widths['interval_den'],L.denominator.bit_length(),U.denominator.bit_length())
                xs=[]
                for idx,cache in enumerate((None,old,hull)):
                    beg=time.perf_counter();v=r.certify(version,a,L,U,m,j,xx,zz,(st0,st1,st2)[idx],cache)
                    total_s[idx]+=time.perf_counter()-beg
                    xs.append(v)
                assert xs[0]==xs[1]==xs[2],(case,vi,qid,xs)
                beg=time.perf_counter();lv=linear_certify(events,a,L,U,m,j,xx,zz,slin)
                total_s[3]+=time.perf_counter()-beg
                if lv[0]=='CERTIFIED':assert lv[1]==xs[0][1],(case,vi,qid,lv,xs[0]);results['linear_certified']+=1
                results['matched_queries']+=1
                if xs[0][0]=='CERTIFIED':
                    results['certified']+=1
                    # Oracle at rational endpoints and several inner points, exact arithmetic.
                    for th in [L,(2*L+U)/3,(L+U)/2,(L+2*U)/3,U]:
                        assert r.oracle(th,events,m,j,xx,zz)==xs[0][1],(case,vi,qid,th)
                        results['oracle_checks']+=1
    # Verify branch delete and old snapshot observable in all versions.
    now_peak=tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return {'science_pin':PIN,'model':'auxiliary exact rational circle observer',
      'models':count,'cache_cap':cap, 'counts':dict(results),
      'plain':dict(st0),'legacy':dict(st1),'hull':dict(st2),'linear':dict(slin),'hull_metrics':dict(hull.metrics),
      'entries_legacy':sum(len(v) for v in old.data.values()),'entries_hull':len(hull.data),
      'wall_seconds':dict(zip(('plain','legacy','hull','linear'),map(lambda x:round(x,6),total_s))),
      'tracemalloc_peak_bytes_including_all_methods':now_peak,'data_operand_widths_bits':widths}

def test_merge_and_adversarial():
    # Exact theorem unit-tests independent of full tree: both positive intervals overlap anchor.
    a=F(3,10);A=(a-F(3,100),a+F(1,100));B=(a-F(1,100),a+F(2,100))
    assert max(A[0],B[0])<=min(A[1],B[1])
    H=(min(A[0],B[0]),max(A[1],B[1]))
    for t in [H[0],A[0],a,B[1],H[1]]:assert A[0]<=t<=A[1] or B[0]<=t<=B[1]
    # Disjoint counterexample for naive hull in a circular membership test:
    # m=2, source time t=4, x=j=0, z=0; A0(theta)=[0,theta).
    # Both [1/10,1/5] and [17/50,9/25] exclude t=4,
    # but theta=1/4 is between them and includes t=4 exactly.
    excluded=lambda th: not (F(0)<=r.fr(4*th)<th)
    left=(F(1,10),F(1,5)); right=(F(17,50),F(9,25))
    assert all(excluded(th) for th in [left[0],(left[0]+left[1])/2,left[1],right[0],(right[0]+right[1])/2,right[1]])
    assert not excluded(F(1,4))
    non_anchor_counterexample={'circle_membership': 'fractional(4*theta) in [0,theta), label z=0, m=2, x=j=0',
       'excluded_components': ['[1/10,1/5]','[17/50,9/25]'],
       'intervening_inclusion_theta':'1/4', 'note':'Disjoint certified components require separate entries if outside fixed-anchor regime'}
    return {'overlap_hull':[[str(v) for v in A],[str(v) for v in B]],
            'union_hull':[str(v) for v in H], 'unrestricted_disjoint_hull_warning':non_anchor_counterexample}


def adversarial_workloads():
    rng=Random(68002);a=F(23,101);m=17;j=223;x=F(7,19)
    root=None;ev=[]
    for i in range(80):
        t=i*3-40;b=i%5;ev.append((t,b))
        root=r.add(root,(r.fr(t*a),t,b),rng.getrandbits(96))
    base=Counter(); wide=Counter(); tight=Counter()
    cwide=HullLRU(None);ctight=HullLRU(2)
    # Repeated rounds with 17 different label signatures; tiny cap repeatedly loses prior keys.
    queries=[(z,x) for z in range(17)]*5
    certified=0
    for z,obs in queries:
        L=a-F(1,10**10);U=a+F(1,10**10)
        expected=r.certify(root,a,L,U,m,j,obs,z,base)
        assert expected==r.certify(root,a,L,U,m,j,obs,z,wide,cwide)
        assert expected==r.certify(root,a,L,U,m,j,obs,z,tight,ctight)
        if expected[0]=='CERTIFIED':
            certified+=1
            for th in (L,a,U):assert r.oracle(th,ev,m,j,obs,z)==expected[1]
    # Cache miss cost can dominate if every request uses a fresh signature and no reuse occurs.
    uncache=Counter();single=Counter();c=HullLRU(32)
    elapsed=[0.,0.];statuses=Counter()
    for i in range(400):
        z=i % m;obs=x+F(i+1,1000007)
        L=a-F(1,10**11);U=a+F(1,10**11)
        st=time.perf_counter();one=r.certify(root,a,L,U,m,j,obs,z,uncache);elapsed[0]+=time.perf_counter()-st
        st=time.perf_counter();two=r.certify(root,a,L,U,m,j,obs,z,single,c);elapsed[1]+=time.perf_counter()-st
        assert one==two
        statuses[one[0]]+=1
        if one[0]=='CERTIFIED':assert r.oracle(a,ev,m,j,obs,z)==one[1]
    return {'alternating_labels':{'queries':len(queries),'certified':certified,
      'no_cache_checks':base['subtree_checks'],'unbounded_checks':wide['subtree_checks'],
      'capacity_2_checks':tight['subtree_checks'],'unbounded_hits':wide['cache_hits'],
      'capacity_2_hits':tight['cache_hits'],'capacity_2_evictions':ctight.metrics['evictions']},
      'unique_signatures':{'queries':400,'status_counts':dict(statuses),
      'no_cache_checks':uncache['subtree_checks'],'capacity_32_checks':single['subtree_checks'],
      'cache_hits':single['cache_hits'], 'cache_evictions':c.metrics['evictions'],
      'wall_s':{'uncached':round(elapsed[0],6),'capacity_32':round(elapsed[1],6)}}}

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--cap',default='64');ap.add_argument('--count',type=int,default=80)
    ap.add_argument('--output',default='')
    ar=ap.parse_args();cap=None if ar.cap=='none' else int(ar.cap)
    out={'theorem_units':test_merge_and_adversarial(), 'cases':run_cases(cap=cap,count=ar.count),
         'adversarial':adversarial_workloads()}
    if ar.output:Path(ar.output).write_text(json.dumps(out,indent=2,sort_keys=True))
    c=out['cases'];print(json.dumps({'models':c['models'],'matched_queries':c['counts']['matched_queries'],
      'hull_rectangles':c['hull']['subtree_checks'],'plain_rectangles':c['plain']['subtree_checks'],
      'linear_certified':c['counts']['linear_certified'], 'linear_wall_seconds':c['wall_seconds']['linear'],
      'hull_hits':c['hull'].get('cache_hits',0), 'hull_extensions':c['hull_metrics'].get('hull_extensions',0),
      'entries_hull':c['entries_hull'],'adversarial':out['adversarial']},indent=2))
