#!/usr/bin/env python3
"""Unit145: source-exact dual_edges guard from scripts/check_p000_first_shell_polyhedron_classification.py.
Exposes opt-mode guard loss without running original program or altering frozen inputs.
"""
import json
import hashlib
import sys

def dual_edges(Fc,E):
    D=set()
    for e in E:
        inc=[k for k,f in enumerate(Fc) if set(e)<=f]
        assert len(inc)==2
        D.add(tuple(sorted(inc)))
    return sorted(D)

def require(p, message):
    if not p:
        raise RuntimeError(message)

cases = {
    'valid_two_facets': ([{0,1,2},{0,1,3}],[(0,1)]),
    'boundary_one_facet': ([{0,1,2}],[(0,1)]),
    'nonmanifold_three_facets': ([{0,1,2},{0,1,3},{0,1,4}],[(0,1)]),
    'missing_zero_facets': ([{2,3,4}],[(0,1)]),
}
observed = {}
for name,(facets,edges) in cases.items():
    expected_count={'valid_two_facets':2,'boundary_one_facet':1,'nonmanifold_three_facets':3,'missing_zero_facets':0}[name]
    actual_count=sum(set((0,1))<=f for f in facets)
    require(actual_count==expected_count,'bad setup')
    try:
        result=dual_edges(facets,edges)
        observed[name]={'kind':'returned','dual_edges':[list(x) for x in result]}
    except AssertionError:
        observed[name]={'kind':'assert_rejected'}
if __debug__:
    require(observed['valid_two_facets']=={'kind':'returned','dual_edges':[[0,1]]},'valid graph fail')
    for name in cases:
        if name != 'valid_two_facets':
            require(observed[name]['kind']=='assert_rejected',f'{name} erroneously accepted')
else:
    require(observed['valid_two_facets']=={'kind':'returned','dual_edges':[[0,1]]},'valid graph fail opt')
    require(observed['boundary_one_facet']=={'kind':'returned','dual_edges':[[0]]},'one-facet mismatch')
    require(observed['nonmanifold_three_facets']=={'kind':'returned','dual_edges':[[0,1,2]]},'three-facet mismatch')
    require(observed['missing_zero_facets']=={'kind':'returned','dual_edges':[[]]},'zero-facet mismatch')
mode='normal' if __debug__ else 'optimized'
out={'unit':145,'source_function':'scripts/check_p000_first_shell_polyhedron_classification.py::dual_edges', 'mode':mode,'cases':observed,'source_guard':'assert len(inc)==2','native_p000_modified':False,'original_historical_program_run':False}
canonical=json.dumps(out,sort_keys=True,separators=(',',':'),ensure_ascii=False)
print(json.dumps({'sha256':hashlib.sha256(canonical.encode('utf-8')).hexdigest(),'result':out},sort_keys=True,ensure_ascii=False))
