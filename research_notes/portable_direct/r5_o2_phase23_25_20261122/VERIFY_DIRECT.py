"""Independent fixed-threshold evaluator using original load inequalities and event masks.
No tie-cone coefficient recurrence or rational generating function is used.
"""
import numpy as np
from REPRODUCE import S, mul, roll, homogeneous, factor, vectors

def direct(d,m):
    u=homogeneous(d,[216,217,218],m-1)
    j=homogeneous(d,[219,220,221],m-1)
    u_cumulative=np.cumsum(u,axis=0)
    joint={(jj,r):mul(j[jj],u_cumulative[r]) for jj in range(m) for r in range(m)}
    result=np.zeros(d,dtype=np.int64)
    for mask in range(1,8):
        f=[idx for idx in range(3) if mask & (1<<idx)]
        relevant_x=bool(mask & (1|2))
        relevant_y=bool(mask & (1|4))
        relevant_j=bool(mask & (2|4))
        p=np.zeros(d,dtype=np.int64)
        for x in (range(m) if relevant_x else [0]):
            for y in (range(m) if relevant_y else [0]):
                for jj in (range(m) if relevant_j else [0]):
                    load=[x+y,x+jj,y+jj]
                    cap=max(load[i] for i in f)
                    if cap>=m:continue
                    p+=roll(joint[(jj,m-1-cap)],214*x+215*y)
        union=set.union(*(S[i] for i in f))
        cc=factor(d,union)
        result+=(1 if len(f)%2 else -1)*mul(cc,p)
    return result

if __name__=='__main__':
    checks={23:[1,2,3,23,42,46],25:[1,2,3,25,46,50]}
    for d,ms in checks.items():
        r=vectors(d,46 if d==23 else 50)
        for m in ms:
            actual=direct(d,m)
            target=r[m-1]
            assert np.array_equal(actual,target),(d,m)
            print('DIRECT_MATCH',d,m,'full_vector_zero',not np.any(actual))
