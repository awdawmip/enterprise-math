# PREFIX-870 — Exact odd-source port widths 33–55 and the p=32 shared-GCD barrier

Date: 2026-11-17. Predecessors: PREFIX-869 and PREFIX-861. Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged).
Status: author-proved/exact-integer-checked, independent review and native mathematical admission pending.
Scope: auxiliary **named binary BRC** two-port integer observer, not yet mapped to original X6 Cell/Link/Port events.

## Model
For p named binary sources let `0<=u<2^p` be the state. A legal ordered transition is either `(u,u)` or `(u,u xor 2^i)`, with one named bit index `0<=i<p`. The observer gives `(u mod q1,v mod q2)` for **fixed odd** q1,q2>=3. Full recovery means identifying old state, new state, changed name and direction. Define `B_fix,odd(p)` as the smallest possible maximum bit length of the two moduli, for injectivity on all `2^p(p+1)` transitions.

## Theorem 870-A (twelve exact new optima)
For every odd p in `{33,35,37,39,41,43,45,47,49,51,53,55}` the global optimum among all fixed odd two-modulus observers is exactly
[
B_{m fix,odd}(p)=min{Bge1:(2^B-1)^2ge2^p(p+1)}.
]
The corresponding bit widths are 20,21,22,23,24,25,26,27,28,29,30,31.

**Lower bound.** Injectivity maps `2^p(p+1)` distinct legal ordered transitions into at most `q1*q2 <=(2^B-1)^2` different output pairs. This establishes the lower bound for arbitrary odd q1,q2.

**CRT construction and upper bound.** Let `g` be odd and let `h(g)` be the least positive d with `2^d=+1 or -1 (mod g)`. If `h(g)>=p`, the signed-increment set `D={0} union {+/-2^i : 0<=i<p}` is injective modulo g: a signed-power collision would imply an earlier ±1 power, contrary to h(g)>=p, and no power of 2 is zero mod odd g. Choose **consecutive odd** a,b=a+2 with `g*a*b>=2^p`; they are coprime. Set `q1=g*a,q2=g*b`. The common residue `(r2-r1) mod g` uniquely determines delta=v-u and the named source; then
[
vequiv r_1+deltapmod {q_1},qquad vequiv r_2pmod {q_2}.
]
The generalized CRT fixes v modulo `lcm(q1,q2)=g*a*b>=2^p`, hence its unique representative in the state domain. Finally `u=v-delta`. Each exact odd-p witness in the table attains the lower bound above.

## Explicit verified witnesses
All rows have `q1=g*a,q2=g*(a+2)`, `gcd(a,a+2)=1`, `h(g)>=p`, and `g*a*(a+2)>=2^p`. `L` is the strict finite-alphabet lower bound; `B` is the witness peak bit width. Odd p: B=L is the global optimum. Even p: L<=optimum<=L+1.

| p | L | B | g | h(g) | q1 | q2 |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 19 | 20 | 67 | 33 | 536469 | 536603 |
| 33 | 20 | 20 | 67 | 33 | 758641 | 758775 |
| 34 | 20 | 21 | 71 | 35 | 1104405 | 1104547 |
| 35 | 21 | 21 | 71 | 35 | 1561929 | 1562071 |
| 36 | 21 | 22 | 79 | 39 | 2329947 | 2330105 |
| 37 | 22 | 22 | 79 | 39 | 3295169 | 3295327 |
| 38 | 22 | 23 | 79 | 39 | 4659973 | 4660131 |
| 39 | 23 | 23 | 79 | 39 | 6590259 | 6590417 |
| 40 | 23 | 24 | 83 | 41 | 9553051 | 9553217 |
| 41 | 24 | 24 | 83 | 41 | 13509993 | 13510159 |
| 42 | 24 | 25 | 101 | 50 | 21076175 | 21076377 |
| 43 | 25 | 25 | 101 | 50 | 29806211 | 29806413 |
| 44 | 25 | 26 | 101 | 50 | 42152249 | 42152451 |
| 45 | 26 | 26 | 101 | 50 | 59612321 | 59612523 |
| 46 | 26 | 27 | 101 | 50 | 84304397 | 84304599 |
| 47 | 27 | 27 | 101 | 50 | 119224541 | 119224743 |
| 48 | 27 | 28 | 101 | 50 | 168608895 | 168609097 |
| 49 | 28 | 28 | 101 | 50 | 238448981 | 238449183 |
| 50 | 28 | 29 | 101 | 50 | 337217891 | 337218093 |
| 51 | 29 | 29 | 103 | 51 | 481596791 | 481596997 |
| 52 | 29 | 30 | 107 | 53 | 694179513 | 694179727 |
| 53 | 30 | 30 | 107 | 53 | 981718045 | 981718259 |
| 54 | 30 | 31 | 121 | 55 | 1476394931 | 1476395173 |
| 55 | 31 | 31 | 121 | 55 | 2087937885 | 2087938127 |

## Theorem 870-B (p=32 decoder-class optimum)
For any two-port decoder which **first identifies delta solely from the common residue modulo `g=gcd(q1,q2)`**, all `2p+1` signed delta possibilities must be distinguished, forcing `g>=2p+1`. Injectivity of the no-change transitions also forces `lcm(q1,q2)>=2^p`. Thus
[
(2^B-1)^2ge q_1q_2=goperatorname{lcm}(q_1,q_2)ge(2p+1)2^p.
]
For p=32 and B=19 this fails exactly:
[
(2^{19}-1)^2=274876858369 < 65,2^{32}=279172874240.
]
The row `p=32` gives `(q1,q2)=(536469,536603)`, `g=67`, `h(g)=33`, peak width 20. Hence **the common-residue-first CRT decoder has exact optimum 20 bits at p=32**. For arbitrary fixed odd moduli, the present bound is `19<=B_fix,odd(32)<=20`. If a 19-bit observer exists, it must exploit nontrivial cross-port coupling rather than decoding delta from the shared residue; the no-op lcm bound also forces `gcd(q1,q2)<=63`.

## Verification scope and source provenance
The companion Python script recomputes all 24 integer witnesses p=32..55; checks actual signed-delta injectivity modulo g; checks CRT and strict alphabet inequalities; and enumerates all 192 transitions at p=5 for a small independent decoder sanity case. The certificate was additionally recomputed with an independent JavaScript BigInt implementation and matched all 24 `(p,L,B,g,q1,q2)` rows. No floating-point computations, classical π/trigonometry, or native physics evolution were performed. These are exact arithmetic certificates for the explicitly defined auxiliary BRC observer, **not an original X6 simulation**.

Open next problem: determine whether a fixed odd two-port 19-bit observer exists for p=32, by examining non-CRT coupled residue fibers; generalize the sharp odd-p interval using half-order supply. Preserve original P000 six-space-one-time ontology, named-source provenance and frozen scientific input; no protected shared-task CLAIM or official acceptance is asserted.
