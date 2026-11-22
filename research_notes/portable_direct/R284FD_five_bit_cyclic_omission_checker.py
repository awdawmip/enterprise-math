"""Exhaustive sharp n=6 certificate for four-generation q=1, u=0 cyclic omission tags.
Public scientific calculation, Python 3 standard library only.
"""
from itertools import permutations


def terminal_successors(state, old, new):
    """Every terminal state after trying every changed address and omitting <=1."""
    changed = old ^ new
    base = (state & ~changed) | (new & changed)
    out = {base}
    bits = changed
    while bits:
        bit = bits & -bits
        bits -= bit
        out.add((base & ~bit) | (state & bit))
    return out


def reachable_stable_sets(codes):
    """Least cyclic fixed point, initialized at exact generation-0 word."""
    stable = [set() for _ in range(4)]
    stable[0].add(codes[0])
    changed = True
    while changed:
        changed = False
        for i in range(4):
            j = (i+1) % 4
            for state in tuple(stable[i]):
                for next_state in terminal_successors(state, codes[i], codes[j]):
                    if next_state not in stable[j]:
                        stable[j].add(next_state)
                        changed = True
    return stable


def overlap_count(sets):
    return sum(len(sets[i] & sets[j]) for i in range(4)
               for j in range(i+1, 4))


def main():
    n=5
    count=0
    no_overlap=0
    minimum=None
    minimizers=0
    witness=None
    # XOR translation normalizes generation zero to the all-zero word.
    # The other three codes are distinct nonzero n-bit words.
    for a,b,c in permutations(range(1,1<<n),3):
        codes=(0,a,b,c)
        states=reachable_stable_sets(codes)
        conflicts=overlap_count(states)
        count+=1
        if not conflicts:
            no_overlap+=1
        if minimum is None or conflicts < minimum:
            minimum=conflicts
            minimizers=1
            witness=(codes,tuple(map(len,states)))
        elif conflicts == minimum:
            minimizers+=1
    assert count == 31*30*29 == 26970
    assert no_overlap == 0
    assert minimum == 4 and minimizers == 20
    # The earlier n=6 Gray construction is a matching upper bound.
    codes6=(0b000000,0b000111,0b111111,0b111000)
    sets6=reachable_stable_sets(codes6)
    assert tuple(map(len,sets6)) == (16,16,16,16)
    assert overlap_count(sets6) == 0
    assert len(set.union(*sets6)) == 64
    print({'model':'4-generation cyclic; <=1 failed changed bit per edge; no cleanup; u=0',
           'five_bit_code_cycles_checked':count,
           'five_bit_disjoint_terminal_families':no_overlap,
           'least_pairwise_endpoint_intersection_sum':minimum,
           'minimizer_count':minimizers,
           'one_minimizer':witness,
           'six_bit_gray_codes':codes6,
           'six_bit_reachable_terminal_sizes':tuple(map(len,sets6)),
           'six_bit_terminal_union_size':len(set.union(*sets6)),
           'conclusion':'n_min=6, subject to exact model'})


if __name__=='__main__':
    main()
