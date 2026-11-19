"""Independent exhaustive check of a declared subset of C++ universe.

No candidate-by-current-state minimum-cost merging. Keep each original y
separate and track its current state and total resource or dead marker.
"""
import json
from collections import deque
from pathlib import Path

HERE=Path(__file__).resolve().parent

def decode_map(code):
    return tuple((code//(3**z))%3 for z in range(3))

def decide_direct(maps, costs, labels, S, x, B):
    ylist=[y for y in range(3) if S >> y & 1 and y!=x]
    rest=tuple((y,0) if not ((labels >> x & 1) and not(labels >> y & 1)) else None for y in ylist)
    if all(z is None for z in rest):
        return False
    initial=(x,0,rest)
    todo=deque([initial]);seen={initial}
    while todo:
        u,sx,ypaths=todo.popleft()
        for a in range(2):
            nx=sx+costs[a][u]
            if nx>B:
                continue
            v=maps[a][u]
            updated=[]
            for item in ypaths:
                if item is None:
                    updated.append(None)
                    continue
                yy,cy=item
                nc=cy+costs[a][yy]
                ny=maps[a][yy]
                if nc>B or ((labels>>v&1) and not(labels>>ny&1)):
                    updated.append(None)
                else:
                    updated.append((ny,nc))
            if all(z is None for z in updated):
                return False
            node=(v,nx,tuple(updated))
            if node not in seen:
                seen.add(node);todo.append(node)
    return True

def main():
    counts=[0]*4;total=0
    for m0 in range(4):
        for m1 in range(4):
            maps=(decode_map(m0),decode_map(m1))
            for labels in range(8):
                for cbits in range(64):
                    costs=tuple(tuple((cbits>>(a*3+z))&1 for z in range(3)) for a in range(2))
                    for S in range(1,8):
                        if S.bit_count()<2:continue
                        for x in range(3):
                            if not(S>>x&1):continue
                            total+=1
                            for B in range(4):
                                counts[B]+=decide_direct(maps,costs,labels,S,x,B)
    expected=json.loads((HERE/'RESULT_BUDGET_PREFIX.json').read_text())['subset_m0_m1_0_3']
    assert (total,counts)==(expected['cases'],expected['safe']), (total,counts,expected)
    # A human-readable binary-cost counterexample with a non-monotone budget sequence.
    maps=((0,0,0),(0,2,0))
    costs=((0,0,0),(0,1,1))
    res=[decide_direct(maps,costs,0,6,2,B) for B in range(4)]
    assert res == [True,False,True,True],res
    assert [decide_direct(maps,costs,7,6,2,B) for B in range(4)] == res
    print('PASS_R5_BUDGETED_INDEPENDENT',total,*counts,'witness',res)
if __name__=='__main__':main()
