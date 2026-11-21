#!/usr/bin/env python3
"""R284DS: heap-based labeled envelope and sorted-site batch evaluation.
Exact frozen Port inputs from pinned R284CO, with R284DP/R284DD reference helpers.
"""
from bisect import bisect_right
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
import hashlib, heapq, json, random
from R284CO_spectral_witness_checker import P, FROZEN_SHA, words, arcs, dist
from R284DP_eight_skeleton_fast_pair_generator_checker import q3, residue
from R284DD_attributed_envelope_checker import attributed_envelope

EXPECTED_PAIR_SHA='7c05864095ba5cde368002e67764bc772ca1bfe3fabbcf26af4fb090b7d0996a'

def build_heap_envelope(A):
    events=defaultdict(list)
    segments=0
    for label,(a,w) in enumerate(A):
        assert 0<=a<P and 0<w<P
        for k in (-1,0):
            b=a+w+k*P; e=a+(k+1)*P; mid=(b+e)//2
            for lo,hi,s,c in ((b,mid+1,1,-b),(mid+1,e+1,-1,e)):
                lo=max(0,lo);hi=min(P,hi)
                if lo<hi:
                    key=(s,c,label)
                    events[lo].append((key,1));events[hi].append((key,-1))
                    segments+=1
    events[0];events[P]
    times=sorted(events)
    heaps={1:[],-1:[]}
    buckets={1:{},-1:{}}
    active=Counter()
    profiles=[]
    pushes=pops=0
    for t in times[:-1]:
        for (s,c,label),delta in events[t]:
            key=(s,c,label)
            old=active[key];new=old+delta
            assert new>=0
            if new:active[key]=new
            elif old:del active[key]
            bucket=buckets[s].get(c)
            if old==0 and new>0:
                if bucket is None:
                    bucket={};buckets[s][c]=bucket
                    heapq.heappush(heaps[s],-c);pushes+=1
                bucket[label]=new
            elif old>0 and new==0:
                assert bucket is not None
                del bucket[label]
                if not bucket:del buckets[s][c]
            elif new>0:
                assert bucket is not None
                bucket[label]=new
        row=[]
        for s in (1,-1):
            while heaps[s] and -heaps[s][0] not in buckets[s]:
                heapq.heappop(heaps[s]);pops+=1
            if heaps[s]:
                c=-heaps[s][0]
                row.append((c,tuple(sorted(buckets[s][c]))))
            else:row.append((None,()))
        profiles.append(tuple(row))
    return times,profiles,{'segments':segments,'heap_pushes':pushes,
                          'stale_heap_pops':pops,'slabs':len(profiles)}

def query_profile(x,row,m):
    up,dn=row
    value=max(0,x+up[0] if up[0] is not None else 0,
                 dn[0]-x if dn[0] is not None else 0)
    if value==0:return value,tuple(range(m))
    labels=set()
    if up[0] is not None and x+up[0]==value:labels.update(up[1])
    if dn[0] is not None and dn[0]-x==value:labels.update(dn[1])
    return value,tuple(sorted(labels))

def batch_query(sorted_sites,times,profiles,m):
    """Already sorted points: O(len(sorted_sites)+len(times)+winner_output)."""
    j=0;values=[]
    for x in sorted_sites:
        assert 0<=x<P
        while j+1<len(times)-1 and times[j+1]<=x:j+=1
        values.append(query_profile(x,profiles[j],m))
    return values,j

def regression():
    rnd=random.Random(284312)
    cases=[[(3,5),(3,5)],[(P-4,8),(8,3)],
           [(5,P-10),(5,P-10)],[(P//2-5,7),(P//2+5,9),(0,P-1)]]
    for count in (1,2,4,9):
        for repeat in range(8):
            A=[(rnd.randrange(P),rnd.randrange(1,P)) for _ in range(count)]
            if repeat%3==0:A.append(A[-1])
            cases.append(A)
    checks=0
    for A in cases:
        T,R,_=build_heap_envelope(A)
        T0,R0=attributed_envelope(A)
        assert T==T0 and R==R0
        sites={0,1,P-1,P//2}
        for a,w in A:
            sites.update(v%P for v in (a-1,a,a+1,a+w-1,a+w,a+w+1,
                                       a+w+(P-w)//2,a+w+(P-w)//2+1))
        sites.update(rnd.randrange(P) for _ in range(20))
        sites=sorted(sites)
        out,_=batch_query(sites,T,R,len(A))
        for x,row in zip(sites,out):
            ds=[dist(x,arc) for arc in A]
            max_d=max(ds)
            assert row==(max_d,tuple(k for k,d in enumerate(ds) if d==max_d))
            checks+=1
    return len(cases),checks

def main():
    families,regression_checks=regression()
    A=arcs(); assert len(A)==64
    T,profile,ops=build_heap_envelope(A)
    old_T,old_prof=attributed_envelope(A)
    assert (T,profile)==(old_T,old_prof)
    assert (ops['segments'],len(T),len(profile))==(191,194,193)
    lows=sorted(1056|(x<<9)|(y<<8)|(z<<4)
                for x,y,z in product((0,1),repeat=3))
    pairs=set();sites={};det_count=0
    for low in lows:
        for upper in range(0,16,2):
            root=(upper<<12)|low
            for shift in (0,1,64,65):
                i=root^shift;j=i^4096
                d=q3(i&4095)
                assert d in (59,60)
                x=residue(i);y=(x-d)%P
                assert i not in sites and j not in sites
                sites[i]=x;sites[j]=y;det_count+=1
                pairs.add((i,j))
    assert len(sites)==512 and len(pairs)==256 and det_count==256
    sorted_sites=sorted((x,i) for i,x in sites.items())
    rows,last=batch_query([x for x,i in sorted_sites],T,profile,len(A))
    by_index={i:r for (_,i),r in zip(sorted_sites,rows)}
    for i,j in pairs:
        assert by_index[i][1]==by_index[j][1] and len(by_index[i][1])==1
        assert abs(by_index[i][0]-by_index[j][0]) in (59,60)
    pair_sha=hashlib.sha256(b''.join(i.to_bytes(2,'big')+j.to_bytes(2,'big')
                                 for i,j in sorted(pairs))).hexdigest()
    assert pair_sha==EXPECTED_PAIR_SHA
    # Complete full-population exact audit, not part of construction cost.
    X=words()
    assert FROZEN_SHA=='b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4'
    assert all(X[i]==x for i,x in sites.items())
    sorted_full=sorted((x,i) for i,x in enumerate(X))
    full_rows,final=batch_query([x for x,i in sorted_full],T,profile,len(A))
    assert final==192
    for (x,i),row in zip(sorted_full,full_rows):
        ds=[dist(x,arc) for arc in A]
        mx=max(ds)
        assert row==(mx,tuple(k for k,d in enumerate(ds) if d==mx))
        if i in by_index:assert by_index[i]==row
    cert={'schema':'R284DS_HEAP_BATCH_ATTRIBUTED_ENVELOPE_V1',
          'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
          'frozen_source_commit':'acba2d8667903434aaa2a10720f43637fcc2421b',
          'frozen_source_git_blob_sha1':'b46e0f682b58e47c27094b4bea6fa4e55119a3ee',
          'frozen_codeword_sha256':FROZEN_SHA,'P':P,'arcs':len(A),'codewords':len(X),
          'events':len(T),'heap':ops,
          'preprocessing_profiles_equal_prior_O_m_squared_reference':True,
          'auxiliary_arc_families':families,'auxiliary_sites_checked':regression_checks,
          'all_codeword_values_and_winning_label_sets_equal_64_arc_baseline':True,
          'full_universe_validation_arc_distance_calls':len(X)*len(A),
          'witness_base_determinant_calls':det_count,'witness_modular_partner_translations':len(pairs),
          'witness_sorted_batch_sites':len(sites),'witness_advanced_event_slabs':last,
          'witness_pair_count':len(pairs),'witness_pair_sha256':pair_sha,
          'new_construction_direct_point_arc_calls':0,'review':'NOT_REVIEWED'}
    path=Path(__file__).with_name('R284DS_fast_labeled_sweep_certificate.json')
    path.write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'
',encoding='utf8')
    print(json.dumps(cert,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
