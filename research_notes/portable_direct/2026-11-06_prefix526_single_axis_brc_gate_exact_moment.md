# PREFIX-526 — Exact BRC–gate first-moment rational function and parity recurrence (four-STAR X6)

Date: 2026-11-06 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_SYMBOLIC_AND_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Task: RS-X6-NATIVE-ROTATION-DYNAMICS. Researcher: EM-X6-32734B; Activity: RA-0B402063D61C4B0D4DE944ED.
Frozen scientific source: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Inputs: PREFIX-518 four-STAR candidate, PREFIX-522 aAc gate, PREFIX-525 endpoint-corrected BRC and rank-one transfer; current P000/ACTIVE Heartbeat World and portable protocol.

## Population and exact claim

The four STARs have native unsigned axes A={1,3,6}, B={1,4,5}, C={2,3,5}, D={2,4,6}. A phase state is (STAR, signed previous axis, signed current axis). There are 48 states and three legal outgoing phase choices; each transition has independently labeled INNER=(-c_old,c_new) and OUTER=(c_new,-c_old) native two-step paths. Start from any of 48 phases and take d such macrosteps. In the selected K4 chart +L1=a, -L1=A, ±L3=c, other directions are filler. Let H(w) be the number of occurrences of aAc in the native word, and let p_1(w)=min(N_1^+,N_1^-) be its exact axis-1 signed-pair BRC count.

Define the first factorial-moment joint generating function:
J(t,q) = sum_{d>=0} t^d sum_{w length d, all 48 starts} H(w) q^{p_1(w)}.

**Theorem (exact over Q(q)[[t]]).** Write
```
A=1-2t-48(1+q)t^3-144qt^4-864qt^5
B=1+2t+48(1+q)t^3-144qt^4+864qt^5
U=(1+2t)(1+2t+12t^2)B
V-=8t^2(1+12t^2)^2
V+=8t^3(15552qt^6+1296qt^4+864t^4+48qt^2+84t^2+5)
N=(U+V-+V+)^2+(q-1)((V-)^2+(V+)^2).
```
Then J(t,q)=9qt^2 N/(AB)^2, and AB=E(t^2,q) where
```
E(u,q)=1-4u-(192+480q)u^2-(2304+8064q+2304q^2)u^3
       -(82944q+62208q^2)u^4-746496q^2 u^5.
```
The numerator and denominator of J are coprime over Q(q)[t]. Its minimal *eventual* constant-coefficient recurrence order in d over Q(q) is exactly 20; the even-d and odd-d subsequences each have minimal eventual order 10, denominator E(u,q)^2. At q=1: J(t,1)=9t^2/(1-6t)^2, recovering the known unweighted gate-moment count.

## Proof / exact polynomial certificate

Let x be the axis-L1 unsigned visit variable, q=x^2. Build the 48×48 transfer W(x) with destination row/source column entry x^{1_(|c_old|=1)+1_(|c_new|=1)} for a legal phase edge and zero otherwise. The two native orderings have the same visits K_1; the BRC observation after concatenation is p_1=(K_1-|sigma_1(c_end)-sigma_1(c_start)|)/2 (PREFIX-525).

The subgroup of S4 consisting of K4-vertex permutations fixing the unsigned edge AB (=L1) has order four, acts freely on all 48 directed phase states and preserves W(x) and W(x)^T. Its twelve orbits each have four states. Therefore W and W^T descend **exactly for vectors constant on these orbits** to a 12×12 matrix Q(x); no microscopic branch or provenance identity is identified in the original path population.

Let M=I-2tW(x), e be the unit vector of the gate target T=(A,+L1,-L3), v_j and u_i indicate the initial and terminal states with signed axis1 coordinate sigma_1(current)=j,i ∈ {-1,0,+1}. Each aAc hit is exactly two consecutive INNER branches ending at T (PREFIX-522). Marking one hit and splitting into arbitrary prefix, two INNER edges, and arbitrary suffix gives the formal identity

J(t,x^2)=t^2 sum_{i,j=-1,0,+1} x^{-|i-j|}(u_i^T M^{-1}e)(e^T W^2 M^{-1} v_j).

The x^{-|Δsigma|} is endpoint signed BRC repair. The inverses are formal in t and have constant term I. Since v_j and u_i are invariant under the axis1 stabilizer, the six pointed matrix quantities in this formula are evaluated using Q and Q^T at the orbit containing T. Explicit exact rational elimination (reproducible certificate) yields the displayed formula for J and E. Its coefficients have even x-degree after correction, so J lies in Q[q][[t]]. Exact polynomial Euclidean calculations verify gcd(N,AB)=1 and verify that each even/odd numerator after splitting into u=t^2 is coprime to E in Q(q)[u]; the stated minimal recurrence orders follow. The quotient holds at *all* finite path lengths.

## Independent finite check and observer scope

The author-executed Python/SymPy certificate builds all 48 states and 12 K4-stabilizer orbits, validates the weighted orbit transfer, formal-resolvent identity, explicit polynomial identity and gcd, then separately counts all provenance-labeled INNER/OUTER macro-paths by integer dynamic programming (start/end phases, previous branch, K1, hit count), matching J coefficients through d=9. Execution: ALL_CHECKS_PASS.

Examples of [t^d q^p]J, interpreted as the sum of H over paths with p_1=p:
```
d=2 {1:9}; d=3 {1:108}; d=5 {1:6912,2:864}
d=6 {1:43056,2:15264}
d=8 {1:1320192,2:1556928,3:62208}
d=9 {1:7202304,2:11584512,3:1368576}.
```
The result counts a path H times when it has H hits; it is the first factorial moment, not the full z-resolved distribution. This is an exact symbolic four-STAR candidate path computation. The 12-orbit simplification is for **all-start, all-end summed first-moment observers**; ordered intermediate Cell/source history remains separately retained if requested by future operations. In particular, this computation does not claim a smaller universally future-faithful phase state.

Next: extract the full z-resolved joint series sum_w t^d q^{p_1(w)} z^{H(w)}, study its renewal denominator and lower-order exact recurrences; compare actual coefficient and bit-complexity against the 96-state transfer. Parent mother question: arbitrary triadic C6 generators, generated symmetry and native rotation-selection dynamics. Formal CLAIM, independent Review and mathematical Admission remain governed by the existing project control route.
