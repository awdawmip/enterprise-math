#!/usr/bin/env python3
"""PREFIX-875 exact 3:1 lattice collision certificate (Python 3, no dependencies).
For every eligible odd pair q2=3*q1-2**i, verify a legal no-change/
single-toggle collision and exact overlap with PREFIX-874's D_B.
"""
B=19
P=32
Q=(1<<B)-1
N=1<<P
D={1<<i for i in range(1,B)}
D|={(1<<i)+(1<<j) for i in range(2,B) for j in range(1,i)}
D|={(1<<i)-(1<<j) for i in range(2,B+1) for j in range(1,i)}
assert len(D)==307
count=0
new=0
overlap=0
rows=[]
for i in range(1,B+2):
    z=1<<i
    low=max(1,(z+3)//3)  # ceil((2**i+1)/3)
    high=min(Q,(Q+z)//3)
    n=0
    nnew=0
    for q1 in range(low+(low%2==0),high+1,2):
        q2=3*q1-z
        assert 1<=q2<=Q and q2%2==1
        if q1==q2:
            assert i==1 and q1==1
            continue
        a=3*q1
        u=0 if a&z else z
        A=(u,u)
        C=(u+a,u+q2)
        assert 0<=A[0]<N and 0<=A[1]<N
        assert 0<=C[0]<N and 0<=C[1]<N
        assert C[0]^C[1]==z
        assert A[0]%q1==C[0]%q1 and A[1]%q2==C[1]%q2
        n+=1
        if abs(q1-q2) not in D:
            nnew+=1
    rows.append(dict(i=i,non_diagonal=n,new_beyond_874=nnew))
    count+=n
    new+=nnew
    overlap+=n-nnew
assert (count,overlap,new)==(1747629,1138,1746491)
print({"status":"ALL_EXACT_ASSERTIONS_PASSED",
       "p":P,"B":B,"family_pairs":count,
       "overlap_with_PREFIX874":overlap,
       "additional_pairs":new,
       "union_lower_bound":136052720+new,
       "rows":rows})
