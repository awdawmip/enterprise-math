"""Certify a complete minimax binary search on the original c=512 catalogue."""
import json
from grid import critical_bins as C

def verify(c):
    C.prepare(c+1)
    C.terminal.cache_clear()
    readings=[]
    second_lo,second_hi=None,None
    for v in range(2,c+1):
        for w in range(2,v+1):
            middle=C.block(v,w,3,C.terminal(w))
            lo,hi=C.full_width(c,v,middle)
            readings.append((lo,hi,v,w))
            bl,bh=C.full_width(c+1,v,middle)
            second_lo=bl if second_lo is None else min(second_lo,bl)
            second_hi=bh if second_hi is None else max(second_hi,bh)
    readings.sort()
    # Twice the dyadic numerator of the threshold, strictly between the two
    # bracketed values; comparisons use only an integer-precision observation.
    cuts=[]
    for previous,current in zip(readings,readings[1:]):
        assert previous[1]<current[0]
        cuts.append(previous[1]+current[0])
    first_span=max(row[1] for row in readings)-min(row[0] for row in readings)
    assert max(first_span,second_hi-second_lo)<C.UNIT
    n=len(readings)
    counts={}
    def visit(start,stop,depth):
        if stop-start==1:
            counts[depth]=counts.get(depth,0)+1
            return
        mid=(start+stop)//2
        threshold=cuts[mid-1]
        assert 2*readings[mid-1][1] < threshold < 2*readings[mid][0]
        # All lower ranks give floor(g-threshold)<0, all higher ranks >=0.
        # The physical shift is {-threshold} and the integer origin is known.
        visit(start,mid,depth+1)
        visit(mid,stop,depth+1)
    visit(0,n,0)
    assert sum(counts.values())==n and max(counts)==(n-1).bit_length()
    return dict(c=c,templates=n,readings_per_endpoint_fit_in_one_unit=True,
                first_exact_values_ordered=True,distinct_cut_count=len(cuts),
                worst_case_reads=max(counts),leaf_depths=counts,
                upper_width_first_in_millionths=-(-10**6*first_span//C.UNIT),
                upper_width_second_in_millionths=-(-10**6*(second_hi-second_lo)//C.UNIT))
if __name__=='__main__':
    print(json.dumps(verify(512),indent=2))
