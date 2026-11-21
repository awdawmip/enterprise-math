#!/usr/bin/env python3
"""Exact reduced-site certificate for all 64 finite Port covering thresholds.
Requires the frozen R284CL_finite_codeword_support_checker.py in this folder.
"""
import bisect
import hashlib
import json
import sys
from R284CL_finite_codeword_support_checker import (
    P, D, Z, SELECT, FROZEN_SHA, arc_data, generate_codewords, distance_point_arc
)

def d4(q, a, w):
    """Four times the circle distance at y=q/4; q is integer."""
    delta=(q-4*a)%(4*P)
    return 0 if delta<=4*w else min(delta-4*w,4*P-delta)

def breakpoints(arcs):
    return [sorted({0,4*a%(4*P),4*(a+w)%(4*P),
                    (4*a+2*(w+P))%(4*P),4*P}) for a,w in arcs]

def all_breaks(arcs):
    # q=4y; all isolated pair equalities have 2q=8y integer.
    br=breakpoints(arcs)
    kinks=set().union(*map(set,br))
    roots=set(); pair_hits=0; flat_ties=0
    for i in range(len(arcs)):
        for j in range(i+1,len(arcs)):
            for l,r in zip((seg:=sorted(set(br[i]+br[j]))),seg[1:]):
                il,ir=d4(l,*arcs[i]),d4(r,*arcs[i])
                jl,jr=d4(l,*arcs[j]),d4(r,*arcs[j])
                si,sj=(ir-il)//(r-l),(jr-jl)//(r-l)
                assert ir-il==si*(r-l) and si in (-1,0,1)
                assert jr-jl==sj*(r-l) and sj in (-1,0,1)
                slope_diff=si-sj; value_diff=il-jl
                if slope_diff==0:
                    if value_diff==0: flat_ties+=1
                    continue
                assert (2*value_diff)%slope_diff==0
                root8=2*l-(2*value_diff)//slope_diff
                if 2*l<=root8<=2*r:
                    roots.add(root8); pair_hits+=1
    critical=sorted(set(2*q for q in kinks)|roots)
    assert critical[0]==0 and critical[-1]==8*P
    stats={'individual_arc_kinks':len(kinks)-2,'pairwise_arc_pairs':len(arcs)*(len(arcs)-1)//2,
           'pair_crossing_segment_hits':pair_hits,'distinct_pair_crossings':len(roots),
           'flat_tie_segments':flat_ties,'distinct_critical_sites_including_cut_endpoints':len(critical)}
    return critical,stats

def candidates(critical, sorted_words):
    out=set()
    for b in critical:
        index=bisect.bisect_left(sorted_words,(b+7)//8)
        if index<len(sorted_words):out.add(sorted_words[index])
        if index:out.add(sorted_words[index-1])
        if index==0:out.add(sorted_words[-1])
        if index==len(sorted_words):out.add(sorted_words[0])
    return sorted(out)

def spectrum(values,arcs):
    radius=[-1]*len(arcs); witnesses=[None]*len(arcs)
    for idx,x in enumerate(values):
        ds=sorted(distance_point_arc(x,a,w) for a,w in arcs)
        for k,d in enumerate(ds):
            if d>radius[k]:radius[k]=d;witnesses[k]=idx
    return radius,witnesses

def sha_lines(values):
    return hashlib.sha256(('\n'.join(str(x) for x in values)+'\n').encode('ascii')).hexdigest()

def main(outfile):
    arcs=arc_data()
    assert len(arcs)==64 and all(0<w<P//2 for _,w in arcs)
    raw=generate_codewords()
    original=[t[0] for t in raw]
    ordered=sorted(original)
    assert len(original)==65536 and len(set(original))==len(original)
    critical,stats=all_breaks(arcs)
    small=candidates(critical,ordered)
    U,reduced_witness=spectrum(small,arcs)
    baseline,baseline_witness=spectrum(original,arcs)
    assert U==baseline and U[0]==0 and U[53]==7642302204
    idxmap={x:i for i,x in enumerate(original)}
    cert={
      'schema':'R284CM_CRITICAL_SITE_SPECTRUM_V1',
      'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
      'inputs':{'p':P,'D':D,'Z':Z,'SELECT':SELECT,'codeword_sha256':FROZEN_SHA,
                'codewords':len(original),'arcs':len(arcs)},
      'critical_sites':stats,
      'finite_reduction':{'candidate_codewords':len(small),
            'reduced_distance_evaluations':len(small)*len(arcs),
            'baseline_distance_evaluations':len(original)*len(arcs),
            'critical_8y_newline_sha256':sha_lines(critical),
            'candidate_codewords_newline_sha256':sha_lines(small)},
      'spectrum_U_1_to_U_64':U,
      'critical_site_witnesses':[{'k':k+1,'radius':U[k],
            'matrix_index':idxmap[small[reduced_witness[k]]],
            'port':small[reduced_witness[k]]} for k in range(64)],
      'baseline_witness_indices':baseline_witness,
      'verification':{'exhaustive_65536_x_64_baseline_equal':True,
                      'integer_exact':True,'independent_review':'NOT_REVIEWED',
                      'cost_scope':'arc-distance evaluation count, not end-to-end runtime'}
    }
    with open(outfile,'w',encoding='utf-8') as f:
        json.dump(cert,f,ensure_ascii=False,indent=2)
        f.write('\n')
    print(json.dumps({'breakpoints':len(critical),'candidate_codewords':len(small),
        'reduced_distances':len(small)*64,'baseline_distances':65536*64,
        'spectrum_equal':U==baseline,'U54':U[53],'output':outfile},indent=2))

if __name__=='__main__':
    main(sys.argv[1] if len(sys.argv)>1 else 'R284CM_critical_site_port_spectrum_certificate.json')
