#!/usr/bin/env python3
"""Exhaustive 31-mask pole-order enumeration for frozen R5, stdlib only."""
import json
S=[
  set(range(214,219)),
  {214,*range(216,222)},
  set(range(215,222)),
  set(range(223,291)),
  set(range(296,313)),
]
def compute(d):
    multiples={p for p in range(214,315) if p%d==0}
    by_order={}
    for mask in range(1,32):
        union=set().union(*(S[i] for i in range(5) if mask&(1<<i)))
        order=len(multiples-union)
        by_order.setdefault(order,[]).append(mask)
    highest=max(by_order)
    return {"order":d,"multiples":sorted(multiples),
            "maximum_pole_order":highest,
            "leading_masks":by_order[highest],
            "next_masks":by_order.get(highest-1,[]),
            "masks_by_order":{str(k):v for k,v in sorted(by_order.items())}}
if __name__=="__main__":
    result={str(d):compute(d) for d in (11,13,16,17)}
    assert result["11"]["leading_masks"]==[1]
    assert result["13"]["leading_masks"]==[1]
    assert result["16"]["leading_masks"]==list(range(1,8))
    assert result["17"]["leading_masks"]==[1]
    assert result["11"]["next_masks"]==list(range(2,8))
    assert result["13"]["next_masks"]==list(range(2,8))
    assert result["16"]["next_masks"]==list(range(16,24))
    assert result["17"]["next_masks"]==[2,3,4,5,6,7,16,17]
    print(json.dumps({"status":"PASS","scope":"exact frozen R5 mask denominator orders",
                      "results":result,"review":"NOT_REVIEWED"},indent=2))
