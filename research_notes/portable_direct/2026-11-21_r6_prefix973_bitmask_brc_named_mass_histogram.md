# PREFIX-973 — Bit-mask source observer and exact positive named-history weight histogram

Date: 2026-11-21 (Asia/Shanghai). Status: AUTHOR_PROOF / EXACT_INTEGER_VERIFIED / NOT_REVIEWED.
Scope: independent auxiliary adjacent-core integer XOR observer, not a primitive X6 operation. Frozen input pin `f42f2906d77f24085c123f3ccfe9667d41caa96d` unchanged. Predecessors: PREFIX-968, PREFIX-970 and PREFIX-972. Historical EM-DIRECT-58C410 is provenance, not current authenticated identity or CLAIM.

## Model

Let p>=4, H=2^(p-1), Q_p={H+1,H+3,...,2H-1}, k>0 odd, k+2<H, m>0 odd, 1<=t<=2k. A named witness (a,b,t,t+m,i,j,I,J) satisfies a,b in Q_p, a!=b and

```
((k*a) XOR (1<<j)) -(1<<i) = t*b
(((k+2)*a) XOR (1<<J)) -(1<<I) = (t+m)*b.
```

Define c=k*a-t*b, C=(k+2)*a-(t+m)*b. Each signed label (i,j,s) denotes c=2^i-s*2^j, s=1-2*bit_j(k*a); the second has the analogous rule.

## Theorem 973.1 — exact signed source-bit masks

For each numeric residual c in D_p={2^i-s*2^j}, set

```
P_c = sum_{j: exists i with 2^i-2^j=c} 2^j
M_c = sum_{j: exists i with 2^i+2^j=c} 2^j.
```

For fixed (c,j,s) the index i is unique, since 2^i=c+s*2^j. Therefore the exact number of source labels satisfying the original XOR equation at product x is

```
W_p(c,x) = popcount(P_c & ~low_p(x)) + popcount(M_c & low_p(x)),
low_p(x)=x mod 2^p.
```

Proof. When s=+1, toggling bit j increases x by 2^j and requires bit_j(x)=0. When s=-1, toggling reduces x and requires bit_j(x)=1. Each qualifying j selects exactly one i for its sign. Counting selected bits yields the formula. QED.

For c=0, exactly the p diagonal sign-positive slots (i=j,s=+1) occur, giving W_p(0,x)=p-popcount(low_p(x)). The numeric c alone is not a sufficient observer: at p=4, c=0, x=9 yields W=2 while x=15 yields W=0. Equal total W also does not preserve future port-specific j queries.

## Theorem 973.2 — exact named-mass factorization and BRC histogram

For every fixed integer candidate (a,b,t,m) with c and C as above, the original named history multiplicity is

```
w(a,b,t,m) = W_p(c,k*a) * W_p(C,(k+2)*a).
```

Proof. For fixed integer parameters the valid first and second signed source-slot sets form a Cartesian product; the two XOR checks impose no cross-source label relation. Their cardinalities are the two W factors. QED.

The finite histogram H_m(z)=sum_{non-diagonal in-range integer candidates} z^w is an exact positive-integer weighted-branch carrier. Its positive-support size is sum_{w>0}[z^w]H_m; the total number of named histories is H_m'(1); its second raw weight moment is sum w^2[z^w]H_m. This is a typed auxiliary BRC-style observer, not a claim that native X6, signed-phase BRC or a physical transfer has been executed. Future source-label-sensitive operations require the masks or full labels, or a separate quotient-invariance proof.

## Lemma 973.3 — oddness is automatic

Let d=2t-km be odd and nonzero. Under the established source parity direction c≡1-t (mod 2), C≡t (mod 2), and d | [kC-(k+2)c], the inverse moduli

```
b=[kC-(k+2)c]/d,   a=[tC-(t+m)c]/d
```

are both odd integers. The two numerators are odd by parity. The second quotient is integer by the odd-d determinant identity proved in PREFIX-970. Division by odd d preserves oddness. This removes parity as an independent rejection stage after the correct directed filter; strict Q_p bounds and a!=b remain mandatory.

## Exact results (p=19,k=21, gaps 1/3/5)

Each row is the histogram of w after removing diagonal integer candidates. Missing weight columns have zero count.

| m | w=0 | w=1 | w=2 | w=4 | w=7 | w=8 | w=9 | named mass | sum(w^2) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 977 | 311 | 115 | 14 | 0 | 1 | 1 | 614 | 1140 |
| 3 | 1986 | 501 | 285 | 52 | 1 | 0 | 0 | 1286 | 2522 |
| 5 | 12 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 3 |

In-range integer candidate counts before diagonal exclusion: 1420, 2826, 15. The first two each remove one diagonal candidate. Distinct supporting (a,b) pairs: 442,839,3. All 1903 named histories retain the historical canonical hashes:
m=1 `ccbccc30c4171a809f7270ce59f0b72b368839e93ffeeed8df9ba1045720da71`;
m=3 `1360a9ca274b357d0b87058d35ef6ccd059d0c5aef995e4d93b0d1363e1aaae3`;
m=5 `c429ef59749f36ef295b4ac9171fb5171ab3a706beaa270563728d4962649c1b`.

The implementation uses 499 distinct residuals, 722 signed source slots and 58 shared (q, parity) indices. Exact independent raw-XOR checks cover all 357 (p,k,m) cases with p=4..8, every eligible odd k, and m=1,3,5; they compare named masses, supported pairs and every *positive histogram coefficient*. The Q19 positive histogram is independently checked against the original named witness generator from PREFIX-968.

Ten interleaved complete three-gap CPython executions yielded median ~0.021 s for count-only masks and ~0.074 s for complete PREFIX-968 named expansion. They produce different outputs: this is a count-only specialization, not a like-for-like full reconstruction speedup. Numerical claims use exact Python integers, and benchmark seconds are environment-specific.

## Reproduction and continuation

Use `PREFIX973_R6_MASK_MASS_OBSERVER.py` beside `PREFIX968_R6_MODULAR_BUCKET_JOIN.py` in the same directory, run `python PREFIX973_R6_MASK_MASS_OBSERVER.py` and inspect `PREFIX973_R6_EXACT_RESULTS.json`. The named reconstruction method remains the existing PREFIX-968 program. Next: find the minimal mask/port carrier stable under declared downstream BRC bit and branch operations, and test exact histogram propagation without materializing every source label. The mother target `B_fix,odd(32) in {19,20}` remains OPEN.

This note does not assert a native Task CLAIM, Result, independent Review, Activity association or P000/worldview change.
