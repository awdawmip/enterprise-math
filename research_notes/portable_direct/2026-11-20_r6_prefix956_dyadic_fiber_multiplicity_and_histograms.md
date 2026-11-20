# PREFIX-956 — Exact dyadic fiber multiplicity and closed witness histograms

Date: 2026-11-20. Author-side independent research continuation after PREFIX-955.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Model: **auxiliary named-XOR observer** `(k*a XOR 2^j)-2^i=t*b`; no native P000/Heartbeat X6 state/rotation/time or BRC evolution is identified.
Status: **complete author proof**, exact small-width exhaustive arithmetic checks; no independent mathematical review/admission.

## 1. Exact source-fiber theorem (unbounded p)

For integer `p>=3`, let `x>=0`, `0<=i,j<p`, and define the **named witness count**
`N_p(x,d)=#{(i,j): (x XOR 2^j)-2^i=x-d}`.
Here `d=x-y`, so when used in the frozen collision model `x=k*a` and `y=t*b`, with positive quotient `t`. This count retains distinct source-bit *names*, not just Boolean collision support.

**Theorem 1.**
1. If `d=0`, `N_p(x,0)=p-popcount(x mod 2^p)`.
2. If `d!=0`, `0<=N_p(x,d)<=2`, uniformly in x, p and any externally selected k,a,b,t.
3. Exact formula: write `z=|d|=2^u q` with odd q>0 and let `M(q)` mean `q=2^r-1` for r>=1. Write `b_j(x)=bit_j(x)`.
   - For `d<0`, `N_p(x,d)=1` exactly when `M(q)`, `u+r<p` and `b_{u+r}(x)=0`; otherwise zero.
   - For `d>0`, **add** the following disjoint types:
      (A) one difference witness if `M(q)`, `u+r<p` and `b_u(x)=0` (named `i=u+r,j=u`);
      (B) if z has exactly one set bit at h, one sum witness if `1<=h<=p` and `b_{h-1}(x)=1` (named `i=j=h-1`);
      (C) if z has exactly two set bits at u<v<p, `b_u(x)+b_v(x)` sum witnesses (named `(i,j)=(u,v),(v,u)` according to their named source bits).
   No other witnesses exist.

**Proof.** Let `s_j=1-2 b_j(x)` be +1 when flipping the j-th bit adds `2^j`, -1 when it subtracts `2^j`. The exact XOR identity reduces the equation to
`d=2^i-s_j 2^j`.
If `s_j=+1` then `d=2^i-2^j`: for d>0, i>j and its 2-adic valuation is j, with odd part `2^(i-j)-1`; for d<0, i<j and its valuation is i with odd part `2^(j-i)-1`. Both have **at most one** possible ordered source pair.
If `s_j=-1`, d is positive and `d=2^i+2^j`: a one-bit power has the unique representation i=j, a two-bit integer has exactly two ordered representations, and any other popcount has none.
A difference candidate can overlap two sum candidates only if `d=3*2^u`. In that case the difference candidate requires `b_u(x)=0`, while the sum candidate with j=u requires `b_u(x)=1`; these are mutually exclusive. Consequently nonzero d supports at most two named witnesses. If d=0, necessarily i=j and `b_j(x)=0`; there are exactly the claimed zero bits. QED.

**Sharp in the strict odd-modulus collision domain.** For `p=4,H=8,Q_4={9,11,13,15},k=1,a=13,b=11,t=1`, take `x=13,d=2`. Both `(i,j)=(0,0)` and `(2,1)` satisfy `(13 XOR 2^j)-2^i=11`. Thus two is attained with odd a,b in the original strict domain.

**Useful special classification.** If `d=3*2^u` and `0<=u<=p-3`, then
`N_p(x,d)=1+b_{u+1}(x)`.
At the top boundary `u=p-2`, the difference witness is out of range and `N_p(x,d)=b_{p-2}(x)+b_{p-1}(x)`.

## 2. New universal closed histograms for every p>=3

Set `H=2^(p-1)`; every named source pair (i,j) produces `1-H<=d<=2H`, and the endpoint values are included. Let `A_r(p)` count the pairs `(x,d)` with `0<=x<2^p`, **nonzero** `1-H<=d<=2H`, and `N_p(x,d)=r`. Then, exactly,

```text
A_2(p) = 2^(p-3) * (p^2 + 3p - 8)
A_1(p) = 2^(p-2) * (3p^2 - 5p + 8)
A_0(p) = 2^(p-3) * (3*2^(p+2) - 7p^2 + 7p - 16)
```

For the actual odd-core auxiliary observer, x is odd. Let `A_r^odd(p)` count the same pairs with x odd. Then

```text
A_2^odd(p) = 2^(p-4) * (p^2 + 5p - 10)
A_1^odd(p) = 2^(p-3) * (3p^2 - 7p + 12)
A_0^odd(p) = 2^(p-4) * (3*2^(p+2) - 7p^2 + 9p - 22).
```

For p=3, `2^(p-4)=1/2`; its polynomial factors are even. All counts are exact integers. These histograms range over **all x residues (or all odd x residues) and offsets**. Fixed k and the restricted a,b in `Q_p` form a different population and are not assigned these histogram counts.

**Counting proof.** For nonzero d, two witnesses arise only from:
- d=2^h, `1<=h<=p-2`: require `bit_h(x)=0, bit_{h-1}(x)=1`; each contributes `2^(p-2)` all-x residues.
- d with two separated (nonadjacent) set bits `0<=u<v<p`, `v>=u+2`: `(p-1)(p-2)/2` offsets, each contributing `2^(p-2)` all-x residues.
- d=3*2^u, `0<=u<=p-3`: exactly `2^(p-1)` all-x residues each, plus the top boundary u=p-2 contributing `2^(p-2)`.
Their sum is `A_2(p)`.
For odd x, repeat the same three classes with bit_0 fixed to 1; the respective two-witness counts are `2^(p-3)(p-1)`, `2^(p-3)[2(p-2)+(p-2)(p-3)/2]`, and `2^(p-3)[2(p-2)+1]`, summing to `A_2^odd(p)`.
Every x and each of p^2 named source pairs determine exactly one offset in the stated interval, so `sum_{x,d} N_p(x,d)=p^2*2^p`; the d=0 fiber has total `p*2^(p-1)`. Restricting x to odd gives corresponding totals `p^2*2^(p-1)` and `(p-1)*2^(p-2)`. Subtract twice the respective two-witness counts to obtain `A_1` and `A_1^odd`; subtract their totals and the d=0 residue populations from `3*2^(2p-1)` and `3*2^(2p-2)` to obtain `A_0` and `A_0^odd`. QED.

At `p=19`, `A_2^odd(19)=14,614,528` over all odd x residues and nonzero feasible offsets. This is a universal dyadic-residue baseline, **not** a count of distinct `Q19` modulus pairs.

## 3. Executed checks and evidence

- Full original-equation enumeration for every `x mod 2^p` and every offset `1-H<=d<=2H`, for p=3,4,5,6,7,8,9: respectively **96, 384, 1536, 6144, 24576, 98304, 393216** exact configurations. Each direct named (i,j) count equals the formula. All six symbolic histogram formula checks (three all-x, three odd-x) agree.
- Nonzero `A_2` sequence: **10,40,128,368,992,2560,6400**; odd-x sequence **7,26,80,224,592,1504,3712**.
- Additional p=19 checks: 16,000 pseudorandom valid odd k,a,b,t configurations; 12,000 constructed **true** XOR witnesses compared to direct two-loop counting; seed 20261120. The random raw k,a,b,t sample is not a uniform sample of collision events.
- All arithmetic is exact integers. The repository checker `PREFIX956_R6_MINIMAL_INDEPENDENT_CHECK.py` reproduces the complete exhaustive p=3,...,9 and histograms. The run-specific richer experiment and JSON log are retained in the matching local reproduction bundle; publication of the compact checker preserves the stated main finite verification.

## 4. Residual/observation significance and frontier

Boolean support erases a genuinely real 1-versus-2 nonzero source-fiber distinction; the proof supplies an exact count and named reconstruction candidates for any fixed `x,d`. The zero-offset fiber `p-popcount` recovers the earlier diagonal phenomenon (PREFIX-952) as a special case. The theorem is **not** a proof that this multiplicity can be collapsed under later branch/time composition: future operations still require retaining the actual named (i,j) histories or proving an observer-specific descent.

Next high-value route: insert the exact O(p) or bitwise source-fiber tester into the nonresonant determinant/CRT candidate path of PREFIX-955; classify its 6,203 offdiagonal Q19 pairs by exact (t,T) witness-fiber multiplicities without scanning every signed source quadruple. Do not re-enumerate the established W21/W23 union as a substitute for this test.

Historical R6 attribution: `EM-DIRECT-58C410`; original SID `MCP-31edc522830749ad8775ca012e02ef30`; Activity `RA-25432C4AAE9BF66A907F5115`. Authenticated shared-task CLAIM, Activity association and independent scientific Review are separate and pending where not supported by their own current receipts. Mother problem `B_fix,odd(32) in {19,20}` remains open.
