#!/usr/bin/env python3
"""Exact checker for the native 3/5/7 orbit decomposition of the 105 gate."""

from __future__ import annotations


def K4_orbit(x: int, y: int, q: int) -> frozenset[tuple[int,int]]:
    return frozenset(((sx*x)%q,(sy*y)%q) for sx in (1,-1) for sy in (1,-1))


def fminus(m: int) -> int:
    return 6*m*m-2*m+1


def fzero(m: int) -> int:
    return 6*m*m+1


def fplus(m: int) -> int:
    return 6*m*m+2*m+1


def lane(m: int, q: int) -> str:
    hits=[]
    for name,f in (("-",fminus),("0",fzero),("+",fplus)):
        if f(m)%q==0:
            hits.append(name)
    assert len(hits)==1,(m,q,hits)
    return hits[0]


def hyperbola(q: int) -> set[tuple[int,int]]:
    return {(x,y) for x in range(q) for y in range(q) if (3*(y*y-x*x)+1)%q==0}


def main() -> None:
    # Root partitions.
    expected={
        3:{"-":{2},"0":set(),"+":{1}},
        5:{"-":{1},"0":{2,3},"+":{4}},
        7:{"-":{2,3},"0":{1,6},"+":{4,5}},
    }
    for q,parts in expected.items():
        got={name:{m for m in range(1,q) if f(m)%q==0} for name,f in (("-",fminus),("0",fzero),("+",fplus))}
        assert got==parts,(q,got)
        assert set().union(*got.values())==set(range(1,q))

    # q=5 one regular orbit and 1:2:1 lane weights.
    H5=hyperbola(5)
    O5={K4_orbit(x,y,5) for x,y in H5}
    assert len(H5)==4 and len(O5)==1
    o5=next(iter(O5))
    assert len(o5)==4
    ms5={(y-x)%5 for x,y in o5}
    assert ms5=={1,2,3,4}
    counts5={s:sum(lane(m,5)==s for m in ms5) for s in ("-","0","+")}
    assert counts5=={"-":1,"0":2,"+":1}

    # q=7 one ramified size2 + one regular size4.
    H7=hyperbola(7)
    O7={K4_orbit(x,y,7) for x,y in H7}
    sizes=sorted(len(o) for o in O7)
    assert len(H7)==6 and sizes==[2,4]
    ram=next(o for o in O7 if len(o)==2)
    reg=next(o for o in O7 if len(o)==4)
    assert all(x==0 for x,y in ram)
    ms_ram={(y-x)%7 for x,y in ram}
    ms_reg={(y-x)%7 for x,y in reg}
    assert ms_ram=={3,4}
    assert ms_reg=={1,2,5,6}
    c_ram={s:sum(lane(m,7)==s for m in ms_ram) for s in ("-","0","+")}
    c_reg={s:sum(lane(m,7)==s for m in ms_reg) for s in ("-","0","+")}
    assert c_ram=={"-":1,"0":0,"+":1}
    assert c_reg=={"-":1,"0":2,"+":1}
    total={s:c_ram[s]+c_reg[s] for s in c_ram}
    assert total=={"-":2,"0":2,"+":2}

    # q=3 is degenerate because B=3=0 mod3; transverse pattern remains 1:0:1.
    assert 3%3==0
    assert {s:len(expected[3][s]) for s in ("-","0","+")}=={"-":1,"0":0,"+":1}

    print("MOD3_DEGENERATE_OUTER_PAIR_101=PASS")
    print("MOD5_REGULAR_K4_121=PASS")
    print("MOD7_REGULAR_PLUS_RAMIFIED_121_PLUS_101_EQUALS_222=PASS")
    print("NATIVE_105_GATE_ORBIT_DECOMPOSITION=PASS")


if __name__ == "__main__":
    main()
