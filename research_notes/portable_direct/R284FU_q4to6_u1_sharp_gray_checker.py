#!/usr/bin/env python3
"""R284FU finite sharp capacity for q=4,5,6 and u=1.

Calls the sibling R284FT exact all-histogram flow-prefix verifier, with
its omission budget/cuts recomputed per q. No sampled or floating tests.
"""
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path

source=Path(__file__).with_name('R284FT_q3u1_22bit_flow_checker.py')
spec=spec_from_file_location('r284ft_exact',source)
m=module_from_spec(spec)
spec.loader.exec_module(m)

EXPECTED={
  4:((593775,10493,7,1,0),(736281,23954,69,10,0)),
  5:((1344904,24052,7,1,0),(1623160,49708,66,10,0)),
  6:((2760681,49836,7,1,0),(3262623,95253,66,10,0)),
}

def main():
    for q, rows in EXPECTED.items():
        m.Q=q;m.U=1;m.CUTS={ij:m.cut_patterns(*ij) for ij in m.PAIRS}
        for step, expected in enumerate(rows):
            n=4*q+8+step
            count, distance, stable, edge0, edge1=m.check(n)
            got=(count,distance,stable,len(edge0),len(edge1))
            assert got==expected,(q,n,got,expected)
            assert not edge1,(q,n,edge1)
            print(f'q={q},u=1,n={n}: total={count},distance={distance},'+
                  f'stable={stable},edge0={len(edge0)},edge1={len(edge1)}')
        x=(0,0,2*q+5,0,0,2*q+5,0)
        assert all(m.edge_has_safe_count_path(x,e) for e in range(4))
        print(f'With R284FP lower bound and R284FE upper construction: n_min({q},1)={4*q+10}')

if __name__=='__main__':main()
