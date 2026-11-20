# PREFIX-954 — Exact top-bit cross-moments by parity-run sweep; full named diagonal moment without scanning Q_p

Date: 2026-11-20. Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Scientific predecessor: PREFIX-952 (named-source witness classification) and PREFIX-953 (lower-bit two-core moment), both published in `research_notes/portable_direct/`. Mathematical scope: auxiliary two-port named-XOR observer with integer source-bit labels, **not** a native X6 time-evolution or a BRC physical rotation result. Status: author proof plus finite exact checks; independent scientific review and Source admission pending.

## Problem

Fix width `p>=4`, `H=2^(p-1)`, `N=2^(p-2)`, `Q_p={H+1+2r:0<=r<N}`, and arbitrary odd cores `1<=k,l<H`. For a core `s` and modulus `a` define

```
e_j(s,a)=1[bit_j(s*a)=0],       j=1,...,p-2
L(s,a)=sum_{j=1}^{p-2} e_j(s,a)
T(s,a)=1[bit_{p-1}(s*a)=0]
Z(s,a)=L(s,a)+T(s,a).
```

The low source-bit 0 is always one because `sa` is odd. Preserve source labels: the product `Z(k,a)Z(l,a)` counts ordered **named** zero-bit witness pairs, not merely existence of a collision.

PREFIX-953 computes `U_p(k,l)=sum_{a in Q_p}L(k,a)L(l,a)` by dyadic inverse classes and Euclidean floor sums, but used a complete `N`-row scan for the terms involving `T`. We remove that scan for fixed/small core parameters.

## Theorem 1: exact upper-bit parity-run formula

Let `a(r)=H+1+2r`, `x_s(r)=s(H+1)+2sr`, and

```
R_s = maximal integer half-open intervals [u,v) subset [0,N)
      on which floor(x_s(r)/H) is even.
```

The intervals are determined without enumerating `r`: for each integer `q` between `floor(x_s(0)/H)` and `floor(x_s(N-1)/H)`, set

```
u_q=max(0,ceil((q*H-s*(H+1))/(2*s)))
v_q=min(N,ceil(((q+1)*H-s*(H+1))/(2*s))).
```

Keep `[u_q,v_q)` iff `q` is even and `u_q<v_q`. There are at most `s+1` such parity blocks (and at most `s+1` all-q blocks), since `x_s(N-1)-x_s(0)<sH`.

For `F(n,m,u,v)=sum_{r=0}^{n-1}floor((ur+v)/m)`, put

```
P_j(s,n)= n-F(n,2^j,2*s,s*(H+1))
             +2*F(n,2^(j+1),2*s,s*(H+1)).
```

Then, exactly for every admissible `p,k,l`,

```
A_p(k,l) = sum_{a in Q_p} L(k,a)*T(l,a)
         = sum_{[u,v) in R_l} sum_{j=1}^{p-2}
                                    (P_j(k,v)-P_j(k,u)).      (1)

D_p(k,l) = sum_{a in Q_p} T(k,a)*T(l,a)
         = sum_{I in R_k, J in R_l} |I intersect J|.           (2)
```

Equation (2) is computed by merging sorted interval endpoints in `O(k+l)` integer steps without examining a single full-width row. Equation (1) uses at most `(l+1)(p-2)` prefix-differences, each containing two exact Euclidean floor sums.

**Proof.** `bit_{p-1}(x)=floor(x/H)-2floor(x/(2H))` is zero exactly on even-q intervals. Solving `qH <= x_s(r) < (q+1)H` for the integer index `r` yields the ceiling endpoints. For a lower source bit, `bit_j(y)=floor(y/2^j)-2floor(y/2^(j+1))`; summing from `r=0` to `n-1` shows that `P_j(s,n)` counts precisely the zero bits at `j` in the first `n` entries. Partitioning by `R_l` proves (1). Both high bits are zero exactly on intersections of `R_k` and `R_l`, proving (2). All objects and counts are integers. QED.

## Theorem 2: complete two-core named witness moment

Write `W_p(s,a)` for the number of `(i,j,t)` with `0<=i,j<p`, `t>=1` and `(s*a XOR 2^j)-2^i=t*a`. The exhaustive source classification in PREFIX-952 gives

```
W_p(s,a)=Z(s,a)+2*[a=H+1]*[s>=3].
```

Let `U_p(k,l)` be the exact lower/lower moment from PREFIX-953, where, for `j=1,...,p-2`, `q_j=l*k^(-1) mod 2^(j+1)`, `h_j=2^(j-1)`,

```
C_j=h_j-F(h_j,2^j,2*q_j,q_j)+2*F(h_j,2^(j+1),2*q_j,q_j)
U_p(k,l)=N*(p-2)*(p-3)/4 + sum_j (N/2^j)*C_j.
```

For `a0=H+1`, `z_s=p-popcount((s*a0) mod 2^p)`, the **complete** two-core named-source product is

```
M_p(k,l)=sum_{a in Q_p} W_p(k,a)*W_p(l,a)
        = U_p(k,l)+A_p(k,l)+A_p(l,k)+D_p(k,l)
          +2*[k>=3]*z_l+2*[l>=3]*z_k
          +4*[k>=3]*[l>=3].                                 (3)
```

**Proof.** Expand `(L_k+T_k+2 delta_k)(L_l+T_l+2 delta_l)`, sum the four ordinary products via (1),(2),PREFIX-953, and note that `delta_s` is supported only at `a0`. QED.

When `k,l` are fixed while width grows, the algorithm uses `O((k+l)p^2)` Euclidean arithmetic iterations and `O(k+l)` run endpoints, rather than `N=2^(p-2)` row inspections. This is **unit-cost integer-operation** accounting: multiprecision bit complexity and input/output materialization must be included for an end-to-end benchmark. At large `k,l` near `H`, the sweep offers no general sublinear guarantee.

## Strict Q19 check: cores 21 and 23

```
p=19, H=262144, N=131072, k=21, l=23
R_21 contains 10 top-zero runs; R_23 contains 11.
A_19(21,23)          =   532848
A_19(23,21)          =   530485
D_19(21,23)          =    29848
U_19(21,23)          =  9448558  [PREFIX-953 independently recomputed]
ordinary Z-product   = 10541739
special source pairs =       62
M_19(21,23)          = 10541801
```

This reproduces all three high-bit terms previously obtained only by a full-width scan in PREFIX-953. It independently recovers the 10,541,739 ordinary rank-one named diagonal combinations in PREFIX-948 and the 10,541,801 full named moment in PREFIX-953. This is a witness **multiplicity** count, not an increase in distinct modulus-pair union coverage.

## Validation and reproducibility

1. `PREFIX954_R6_TOP_BIT_SWEEP.py`: exact parity-run sweep and independent row scan for *all* 5,456 ordered odd-core pairs across widths p=4,5,6,7,8, plus 81 selected p=9 pairs. Every high/low and high/high term matched. It also checks each generated interval against the literal top-bit indicator. At Q19, the three terms matched independent direct per-modulus arithmetic.
2. `PREFIX954_R6_INDEPENDENT_FULL_MOMENT.py`: independent direct enumeration of original `(i,j,t)` solutions, for all 5,456 ordered core pairs over p=4..8, matches (3) exactly. All 5,456 symmetry checks `M_p(k,l)=M_p(l,k)` passed.
3. On the observed local Python run for Q19, compressed three-term sweep took 0.00161 s, direct 131072-row bit scan 0.30584 s, and complete (3) took 0.00186 s. These single-run observations are not end-to-end timing, exclude code compilation/startup and should not be used as a universal speedup benchmark.
4. All arithmetic is exact integers; no stochastic or floating-point inference. A local result JSON and SHA-256 package manifest preserve these observations. Source proofs specify arbitrary admissible p,k,l; code tests certify the declared finite ranges.

## Frontier, provenance and open questions

Frozen science remains `f42f2906d77f24085c123f3ccfe9667d41caa96d`, not a rebased main. The operative account rules and P000/ACTIVE worldview were separately read on 2026-11-20, with the X6 native space and separate time preserved. This note is an **auxiliary named-XOR observer** arithmetic result; native BRC/X6 transfer requires an explicit typed state/observer/allowed-future-operations bridge.

Next: combine determinant grouping of PREFIX-948 with CRT/floor sums to count exactly the 6,203 **non-diagonal** pairs in `W_21 intersect W_23` without materializing complete W21/W23. Independently validate the statement for the actual original paired-port legality predicate. Mother question `B_fix,odd(32) in {19,20}` remains open.

Original R6 source lineage: `EM-DIRECT-58C410`, historical `MCP-31edc522830749ad8775ca012e02ef30`, `RA-25432C4AAE9BF66A907F5115`. A historical identity string grants no fresh private session or active shared TASK CLAIM. Activity source association, independent Source audit, mathematical review and project admission remain separate from this scientific publication.
