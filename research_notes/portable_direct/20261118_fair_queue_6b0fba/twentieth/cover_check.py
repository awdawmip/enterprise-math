"""Exact finite opposition checks for the fixed Lassak lens. Python 3.10+, stdlib."""
import argparse
import hashlib
import json
import subprocess
import sys
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from pathlib import Path

NAME='RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE'
RR='RR-68BA014D54542DA7221C'
RR_SHA='41750ec8c0593f9bcc67593ce39ecd9a330e68b4d2071008d5d5ed4acdc8511c'
UNIVERSE=(1<<32)-1
COORDS=(1,2,4,8,16)


def replay(repo):
    rr=(repo/'research_result_records'/NAME/(RR+'.json')).read_bytes()
    assert hashlib.sha256(rr).hexdigest()==RR_SHA
    record=json.loads(rr);pins=[]
    for item in record['output_manifest']:
        path=repo/item['path'];b=path.read_bytes()
        sha=hashlib.sha256(b).hexdigest()
        git=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
        assert 'sha256:'+sha==item['sha256'] and 'sha1:'+git==item['git_blob_sha1']
        pins.append({'path':item['path'],'sha256':sha,'git_blob':git})
    script=next(repo/i['path'] for i in pins if i['path'].endswith('.py'))
    result=subprocess.run([sys.executable,str(script)],check=True,capture_output=True,text=True).stdout.strip()
    assert result==record['checker_summary']
    return {'result':RR,'record_sha256':RR_SHA,'all_frozen_files':pins,'original_stdout':result}


def mask(items):
    return sum(1<<i for i in set(items))


def elements(bits):
    return [i for i in range(32) if (bits>>i)&1]


def union(blocks):
    out=0
    for b in blocks:out|=b
    return out


def shapes():
    balls=[];faces=set();tetra=set()
    for x in range(32):
        balls.append(mask([x]+[x^a for a in COORDS]))
        for a,b in combinations(COORDS,2):
            faces.add(mask((x,x^a,x^b,x^a^b)))
        for a,b,c in combinations(COORDS,3):
            tetra.add(mask((x,x^a^b,x^a^c,x^b^c)))
    all_shapes=balls+sorted(faces)+sorted(tetra)
    assert len(set(all_shapes))==192 and len(faces)==len(tetra)==80
    for s in all_shapes:
        assert max((i^j).bit_count() for i,j in combinations(elements(s),2))<=2
        assert all(any((i^j).bit_count()>2 for j in elements(s)) for i in elements(UNIVERSE^s))
    return balls,all_shapes


def ball_bounds(balls,alls):
    hist={};uncovered=[];worst=0
    for k in (4,5,6):
        counts=Counter()
        for rest in combinations(range(1,32),k-1):
            u=balls[0]|union(balls[i] for i in rest)
            counts[u.bit_count()]+=1
            if k==4 and u.bit_count()==24:
                rem=UNIVERSE^u
                best=max((s&rem).bit_count() for s in alls)
                assert best==2
                uncovered.append([0,*rest]);worst=max(best,worst)
        hist[k]=dict(sorted(counts.items()))
    assert [max(h) for h in hist.values()]==[24,26,30] and len(uncovered)==15
    six=(3,5,14,22,24,25)
    assert (UNIVERSE^union(balls[c] for c in six))==mask((0,31))
    seven=(0,7,25,10,22,23,12)
    assert union(balls[c] for c in seven)==UNIVERSE
    return {'zero_ball_fixed_histograms':hist,'four_disjoint_configurations':uncovered,
            'max_extra_points_in_a_shape_after_four_disjoint_balls':worst,
            'six_ball_centres_missing_0_and_31':six,'seven_cover_centres':seven}


def holes(alls):
    # The analytical 30-point ceiling implies every maximal enlargement still avoids both target holes.
    out={}
    for h in range(1,6):
        target=UNIVERSE^mask((0,(1<<h)-1))
        allowed=[s for s in alls if not(s&~target)]
        by=[[s for s in allowed if (s>>i)&1] for i in range(32)]
        @lru_cache(None)
        def solve(rem,k):
            if not rem:return ()
            if k==0 or rem.bit_count()>6*k:return None
            need=max(1,rem.bit_count()-6*(k-1))
            move=min(([s for s in by[i] if (s&rem).bit_count()>=need]
                     for i in elements(rem)),key=len)
            for s in sorted(move,key=lambda m:-(m&rem).bit_count()):
                rest=solve(rem&~s,k-1)
                if rest is not None:return (s,*rest)
            return None
        best=solve(target,6)
        if best is not None:assert union(best)==target and len(best)<=6
        assert (best is not None)==(h==5)
        out[h]={'possible':best is not None,'memo_states':solve.cache_info().currsize,
                'allowed_maximal_anticodes':len(allowed),'witness':None if best is None else [elements(s) for s in best]}
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo',type=Path,required=True)
    args=ap.parse_args()
    original=replay(args.repo);balls,alls=shapes()
    bounds=ball_bounds(balls,alls)
    bins={}
    for u,parts,threshold in [(F(0),1,6),(F(1,8),1,6),(F(1,4),2,5),
            (F(9,32),2,5),(F(5,16),4,4),(F(1,3),4,4),(F(5,12),8,3)]:
        assert all((F(4,5)*u*h>=1)==(h>=threshold) for h in range(1,6))
        assert ((F(7,12)+u)>=1)==(u==F(5,12))
        bins[str(u)]={'strict_cover_parts_with_pole':parts,'first_incompatible_hamming_distance':threshold}
    data={'original':original,'shape_counts':{'balls':32,'coordinate_squares':80,'parity_tetrahedra':80},
          'six_block_certificate':bounds,'all_two_hole_orbits':holes(alls),'radial_tests':bins}
    print(json.dumps(data,indent=1,sort_keys=True))


if __name__=='__main__':
    main()
