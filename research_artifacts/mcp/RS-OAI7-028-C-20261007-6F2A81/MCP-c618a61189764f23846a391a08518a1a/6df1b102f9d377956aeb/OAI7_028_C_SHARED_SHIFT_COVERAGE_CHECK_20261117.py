#!/usr/bin/env python3
from math import ceil, log, sqrt
p, beta, tau = 101, .5, 3/8
m = ceil(p ** (1-beta))
A = tuple(range(m,p))
assert p >= 2*m and m >= p ** (1-beta)
P_before, P_after = [0.0]*p, [0.0]*p
for x in A:
    P_before[x] += 1/len(A)
    P_after[x] += 1/(2*len(A))
    P_after[(x+m)%p] += 1/(2*len(A))
assert sum(v < tau/p for v in P_before) == m
assert sum(v < tau/p for v in P_after) == 0
assert abs(sum(P_before)-1)<1e-12 and abs(sum(P_after)-1)<1e-12
assert abs(min(P_after)-1/180)<1e-12
assert abs(max(P_after)-1/90)<1e-12
Ap = {(x+m)%p for x in A}
assert m in A and m not in Ap and 0 in Ap and 0 not in A
print({"p":p,"m":m,"epsilon":log(p/(p-m))/log(p),
       "shift_entropy_nats":log(2),"min_after":min(P_after),
       "coverage_threshold":tau/p,"absent_joint_pair":(m,0)})
