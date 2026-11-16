"""Smallest spacing in each named slab, as an exact dyadic bracket."""
import json
from itertools import combinations_with_replacement
from check_rounding import read_two


def spacing(c, lower):
    values = sorted((read_two(c,v,w),(v,w))
                    for w,v in combinations_with_replacement(range(lower,2*lower+1),2))
    diff, idx = min((values[i][0] - values[i-1][0], i) for i in range(1,len(values)))
    bits = diff.denominator.bit_length()-diff.numerator.bit_length()
    if diff*(1 << bits) >= 1:
        bits -= 1
    assert diff*(1 << (bits+1)) >= 1 > diff*(1 << bits)
    return dict(stock=c, slab_min=lower, smaller_g_landing=values[idx-1][1],
                larger_g_landing=values[idx][1], gap_floor_power=-(bits+1),
                gap_ceiling_power=-bits, necessary_all_offset_bits=bits+1)


if __name__=='__main__':
    print(json.dumps([spacing(c,t) for c,t in ((4096,4),(4096,8),(8192,8))],indent=2))
