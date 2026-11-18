# PREFIX-897 — Maximal first-port fiber capacity and 1,377,112 new exact collision exclusions

Date: 2026-11-18 (Asia/Shanghai). Lane: 进取数论研究6. Researcher-ID: EM-DIRECT-E370C2; original SID: MCP-4b417026c0f54b45970c6f223e1833f6. Frozen science pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged). Predecessors: PREFIX-895/896.
Status: AUTHOR_PROVED / TWO_EXACT_FINITE_CHECKS / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Model and precise statement

Let `p>=1`, `N=2^p`, `T=(p+1)N`. Legal *named* directed trajectories are `Z_x=(x,x)` and `F^i_x=(x,x XOR 2^i)`, for `0<=x<N,0<=i<p`. The two-port observation `Phi_(q1,q2)(u,v)=(u mod q1, v mod q2)` has independent positive integer moduli `q1,q2`. Names, directions, source indices and multiplicities are retained.

**Theorem 897-A (maximal-fiber capacity).** If
```
(p+1)*ceil(N/q1)>q2
```
or the same inequality with `q1,q2` interchanged, then two distinct named legal trajectories share the same two-port observation.

**Proof.** Of the `q1` possible first-port residues, the residue zero class `x=0,q1,2*q1,...<N` contains exactly `ceil(N/q1)` distinct starts. Each start generates `p+1` distinct named legal trajectories. All have the identical first-port residue zero and their second-port residue is one of `q2` values. If the displayed strict inequality holds, pigeonhole gives a collision within that class. For the reversed condition, the involution `(x,y,i)->(y,x,i)` preserves all legal named transitions and exchanges the two observer ports. Thus the symmetric condition also gives a collision. QED.

For `T=(p+1)N`, PREFIX-896 already excludes `P={(q1,q2):q1*q2<T}` by global capacity. Define the genuinely new one-sided fiber family
```
X = {(q1,q2) in Q^2 : q1*q2 >= T and q2 < (p+1)*ceil(N/q1)}.
```
The first inequality excludes all already capacity-positive pairs; the second gives an explicit particular-fiber collision proof. Let `Y=X union transpose(X)`, exploiting legal time reversal.

## Theorem 897-B: complete strict-19-bit exact new census

For `p=32,N=4294967296,T=141733920768`, let `Q={262145,262147,...,524287}`, `|Q|=131072`. The code computes each row of `X` without scanning `Q^2`:

```
L(q)=max(262145,ceil(T/q)),
H(q)=min(524287,33*ceil(N/q)-1),
X_q={odd q2 in [L(q),H(q)]}.
```

The complete exact integer results are:
- `|X| = 1,016,538`.
- `|X intersect transpose(X)|=629,230`.
- `|Y|=2*1,016,538-629,230=1,403,846`.
- `|Y intersect (Q\U)^2|=1,393,078`, where `U` is the exact 552-port set from PREFIX-895 (16 original certified rows, 24 axis ports, 512 full two-strip rows).
- Among these, exactly `1,377,112` additionally satisfy `lcm(q1,q2)>=N`.

By PREFIX-896, `P`, the special row/column set `H_U={(q1,q2):q1 in U or q2 in U}`, and the `lcm<N` zero/zero family `Z` have exact union cardinality `7,566,243,102`. The last set of `1,377,112` fiber-positive pairs lies outside `P union H_U union Z` by construction. Consequently the *new, exactly deduplicated four-family certificate* proves collisions on
```
7,566,243,102 + 1,377,112 = 7,567,620,214
```
different ordered modulus pairs of `Q^2`, leaving `17,179,869,184-7,567,620,214=9,612,248,970` not yet excluded by this specified four-family union.

## Evidence and reproducibility

Run `python3 PREFIX897_R6_FIBER_CAPACITY_CHECK.py` (Python standard library, exact integers). Method A scans each capacity-negative narrow row once and weighs transpose-asymmetric pairs by two. Independently, Method B explicitly constructs set `X` using the same closed-form row bounds, forms `Y=X union transpose(X)`, and counts membership in the old sets by direct predicates. All five exact counts agree and match the asserted result. The set-of-pairs method is logically independent of the weighted symmetric accounting, although both use the same necessary exact row range.

The proof is valid for all positive integer `p,q1,q2`. The numerical result is exhaustive solely for the declared strict-19-bit odd-pair domain. The observation is a finite named-source BRC auxiliary: no native X6 spatial reduction, physical time reversal, accepted theorem, or Result/Review status is inferred.

## Next frontier

The next low-overlap unresolved family satisfies `q1*q2>=T`, both ports outside `U`, `lcm(q1,q2)>=N`, and fails both fiber conditions. Test the PREFIX-891 zero-flip endpoint and PREFIX-895 FF carry witness on such inputs, looking for a uniform constructive no-go or an actual injective pair. The mother problem `B_fix,odd(32) in {19,20}` remains open.
