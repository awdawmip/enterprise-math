#!/usr/bin/env python3
"""R728 exact higher-order BRC source-ID port-edge admission law, m=1..8."""
from math import factorial
from R728_X6_pair_port_conflict_verify import source_id_recursion, PORT

def run():
    base = source_id_recursion(PORT)
    admitted = source_id_recursion(tuple(PORT) + ((0,1,2),))
    expected = [1,4,36,576,14400,518400,25401600,1625702400]
    for m,want in enumerate(expected,1):
        a = (m,m,m,0,0,0)
        pre = base(a)
        post = admitted(a)
        assert pre == 0
        falling = lambda k: factorial(m)//factorial(m-k)
        transfer = sum((falling(k)**3//factorial(k)) *
                       base((m-k,m-k,m-k,0,0,0)) for k in range(m+1))
        assert post == transfer == want == factorial(m)**2
        if m >= 2:
            assert base((m-1,m-1,m-1,0,0,0)) == 0
        print("m",m,"new_source_partitions",post)
    print("R728_PORT_EDGE_FACTORIAL_SQUARE_EXACT_PASS")

if __name__ == "__main__":
    run()
