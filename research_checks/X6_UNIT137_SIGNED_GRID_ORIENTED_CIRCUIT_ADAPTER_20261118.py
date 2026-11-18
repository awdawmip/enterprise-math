#!/usr/bin/env python3
"""Independent finite X6 signed 2-generator chart / circuit-chain adapter audit.

Runs only the new finite chart adapter; does not execute or alter the frozen
oriented-matroid experiment or the R063 512-case benchmark.
"""
from __future__ import annotations
import itertools
import json
import math
import hashlib


def check(cond: bool, msg: str) -> None:
    if not cond:
        raise ValueError(msg)


def words(a: int, b: int):
    for xs in itertools.combinations(range(a+b), a):
        s=['j']*(a+b)
        for x in xs: s[x]='i'
        yield ''.join(s)


def path_chain(w: str):
    x=y=0; c={}
    for letter in w:
        e=('H',x,y) if letter=='i' else ('V',x,y)
        c[e]=c.get(e,0)+1
        if letter=='i':x+=1
        else:y+=1
    return c


def face_boundary(x: int,y: int):
    return {('H',x,y):1,('V',x+1,y):1,('H',x,y+1):-1,('V',x,y):-1}


def area_under(w: str, a: int, b: int):
    x=y=0; faces=set()
    for letter in w:
        if letter=='i':
            for yy in range(y):faces.add((x,yy))
            x+=1
        else:y+=1
    check(x==a and y==b,'bad word end')
    return faces


def diff(p,q):
    keys=set(p)|set(q)
    return {e:p.get(e,0)-q.get(e,0) for e in keys if p.get(e,0)!=q.get(e,0)}


def boundary_face_chain(c):
    out={}
    for (x,y),v in c.items():
        for e,coeff in face_boundary(x,y).items():out[e]=out.get(e,0)+v*coeff
    return {e:v for e,v in out.items() if v}


def coordinate_path(anchor,axis_i,axis_j,eps_i,eps_j,w):
    z=list(anchor)
    for letter in w:
        axis=axis_i if letter=='i' else axis_j
        sgn=eps_i if letter=='i' else eps_j
        z[axis]+=sgn
    return tuple(z)


def run():
    anchors=[(0,0,0,0,0,0), (5,-3,2,7,0,-11),(-4,1,-2,0,9,6)]
    shape_count=0; words_count=0; unique_pair_checks=0
    chart_families=0; realized_paths=0; signed_endpoint_tests=0; shape_max=0
    elementary_face_counts=0; full_support_embeds=0
    witness={}
    for a in range(1,5):
      for b in range(1,5):
        shape_count+=1
        ws=list(words(a,b)); B=math.comb(a+b,a)
        check(len(ws)==B,'BRC mismatch')
        words_count+=len(ws)
        shape_max=max(shape_max,B)
        P={w:path_chain(w) for w in ws}
        A={w:area_under(w,a,b) for w in ws}
        elementary_face_counts+=a*b
        for p,q in itertools.combinations(ws,2):
            coeff={face:int(face in A[q])-int(face in A[p]) for face in A[p]|A[q]}
            coeff={face:v for face,v in coeff.items() if v}
            check(set(coeff.values())<={-1,1},'area coefficient outside +-1')
            check(diff(P[p],P[q])==boundary_face_chain(coeff),'path circuit expansion failed')
            unique_pair_checks+=1
            if (a,b)==(2,2) and not witness:
                witness={'a':a,'b':b,'p':p,'q':q,'area_coefficients':[(list(f),v) for f,v in sorted(coeff.items())], 'chain_difference':[([k[0],k[1],k[2]],v) for k,v in sorted(diff(P[p],P[q]).items())]}
        for ai,aj in itertools.combinations(range(6),2):
          for ei,ej in itertools.product([-1,1],repeat=2):
            chart_families+=1
            for anchor in anchors:
              signed_endpoint_tests+=1
              target=list(anchor);target[ai]+=ei*a;target[aj]+=ej*b
              L=sum(abs(target[k]-anchor[k]) for k in range(6))
              check(L==a+b,'native shortest length wrong')
              check(math.factorial(L)//(math.factorial(a)*math.factorial(b))==B,'native BRC wrong')
              for w in ws:
                 check(coordinate_path(anchor,ai,aj,ei,ej,w)==tuple(target),'signed path endpoint mismatch')
                 realized_paths+=1
              # Omitted coordinates remain anchored; there is no native 2-plane inference.
              check(all(target[k]==anchor[k] for k in range(6) if k not in [ai,aj]),'omitted coordinate changed')
              full_support_embeds+=1
    check(chart_families==16*15*4,'wrong chart family census')
    result={'schema':'X6_UNIT137_SIGNED_GRID_CIRCUIT_ADAPTER_EXACT_FINITE_V1',
     'scope':'a,b in 1..4; distinct X6 axis pairs, 4 sign choices, 3 six-component anchors; no original script rerun',
     'shapes':shape_count,'total_positive_chart_words':words_count,'unordered_pair_circuit_checks':unique_pair_checks,
     'total_unit_faces_over_shapes':elementary_face_counts,'max_chart_BRC':shape_max,
     'axis_sign_chart_families':chart_families,'anchored_chart_cases':signed_endpoint_tests,
     'direct_signed_path_endpoints_checked':realized_paths,'unspecified_coordinate_checks':full_support_embeds,
     'failures':0,'bounded_witness':witness,
     'universal_statement_status':'separate elementary proof required; finite checks alone not a universal proof',
     'typed_barrier':'graph cycles/path provenance in fixed signed two-generator X6 chart, not primitive 2D plane or 3-force balance'}
    return result


if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,separators=(',',':')))
