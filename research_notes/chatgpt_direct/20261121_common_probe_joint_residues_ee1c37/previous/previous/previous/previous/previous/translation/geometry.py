"""Export original menu-derived line prices and the action on the five translation quotients."""
from pathlib import Path
from itertools import combinations
import sys


def export(path):
    from translation import DIRECTIONS, POINTS, shift, maps, observations, class_cost
    bad,obs=observations()
    with path.open('w') as f:
        lin,_,_=maps()
        for g in lin: print(*g,file=f)
        for d in DIRECTIONS:
            lines=sorted({tuple(sorted(shift(i,d,t)for t in range(5)))for i in range(125)})
            lookup={p:i for i,line in enumerate(lines)for p in line}
            print(*d,file=f)
            print(*(lookup[p] for p in range(125)),file=f)
            for row in lines:
                print(*row,file=f)
            for row in lines:
                print(*(shift(j,POINTS[row[0]],1)for j in range(125)),file=f)
            for row in lines:
                for other in lines:
                    selected=row if row==other else row+other
                    invalid=any(bad[i][j]>>k&1 for i,j,k in combinations(selected,3))
                    print(-1 if invalid else class_cost(selected,obs),end=' ',file=f)
                print(file=f)
if __name__=='__main__':export(Path(sys.argv[1]))
