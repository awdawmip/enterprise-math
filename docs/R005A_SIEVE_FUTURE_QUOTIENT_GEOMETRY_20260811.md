# R005-A — Sieve Future-Quotient Geometry Checkpoint

Status: `PROVED STRUCTURAL CHECKPOINT / EXECUTABLE CHECKED / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-11`  
Task: `RS-R005-PRIME-ALGORITHM-LAB`  
Researcher-ID: `R005A-7C2`

This continues the existing R005-A owner generation. It does **not** open a new task, does not reopen the first-round taxonomy, and does not change Prime Toolkit theorem status.

Prime fixtures in executable Python work are consumed through `enterprise_math.prime_toolkit.bounded_prime_enumeration`; the returned `PrimeToolResult` must remain exact and carry `CLASSICAL_BASELINE`. No internal prime helper is reimplemented here.

## 0. Closure obtained in this checkpoint

The second-round sieve state problem now separates into four layers:

1. exact activation preperiod and state cardinality — already closed in the v3 packet;
2. exact relation-resolved full-horizon law — closed here for prime-prefix sieves;
3. Boolean steady observation depth — reduced here to local separator geometry with a Jacobsthal branch-and-bound;
4. compiler/state sufficiency boundary — prime-coordinate support determines global mismatch mass but does **not** determine local future depth.

The strongest resource consequence is asymptotic: for prime-prefix sieves, erasing prime attribution saves a vanishing fraction of minimal states while forcing a diverging relative observation-depth penalty.

## 1. Boolean separator normal form

Fix a finite nonempty prime set `P`,

\[
Q=\prod_{p\in P}p,
\qquad
A=\{x\in\mathbb Z/Q\mathbb Z:(x,Q)=1\}.
\]

Use the steady Boolean wheel word

\[
w(x)=1[(x,Q)>1].
\]

For a nonzero shift `d mod Q`, define the separator/mismatch set

\[
M_d
=\{x:w(x)\ne w(x+d)\}
=A\triangle(A-d).
\]

Let `G_Q(S)` be the maximum cyclic gap between consecutive elements of a nonempty subset `S` of `Z/QZ`.

### T-R005A-BS1 — exact local-separation representation

For the shift `d`, the first distinguishing offset in the worst starting phase satisfies

\[
\boxed{\rho_d+1=G_Q(M_d)}.
\]

Therefore the Boolean wheel phase-separation radius is

\[
\boxed{
\rho(P)=\max_{d\not\equiv0\pmod Q}\bigl(G_Q(M_d)-1\bigr).
}
\]

Equivalently, `rho(P)+1` is the shortest cyclic-window length for which all `Q` wheel phases are distinct. This equivalence is generic periodic-word/automata mathematics; the arithmetic problem is the exact structure of `M_d`.

## 2. Aggregate separator mass is CRT-support data

For each prime coordinate, simultaneous coprimality of `x` and `x+d` leaves

- `p-1` residues if `p|d`;
- `p-2` residues if `p∤d`.

CRT therefore gives

\[
I_Q(d)
:=|A\cap(A-d)|
=
\prod_{\substack{p\mid Q\\p\mid d}}(p-1)
\prod_{\substack{p\mid Q\\p\nmid d}}(p-2).
\]

Hence

\[
\boxed{
|M_d|=2\bigl(\varphi(Q)-I_Q(d)\bigr).
}
\]

If

\[
J(d)=\{p\in P:p\nmid d\},
\]

then

\[
|M_d|
=2\varphi(Q)
\left[
1-\prod_{q\in J(d)}\frac{q-2}{q-1}
\right].
\]

Thus `J(d)` is sufficient for **global Hamming mismatch mass**.

The sparsest nonzero separator is obtained by changing only the largest prime coordinate `r=max(P)`:

\[
\boxed{
\min_{d\ne0}|M_d|=\frac{2\varphi(Q)}{r-1}.
}
\]

This is elementary CRT arithmetic and is not claimed as new classical number theory.

## 3. T-R005A-BS2 — support is not future-sufficient

The quotient

\[
d\longmapsto J(d)
\]

is **not** sufficient for `rho_d`.

The smallest clean counterexample already occurs for

\[
P=\{2,3,5\},\qquad Q=30.
\]

Take

\[
d_1=6,\qquad d_2=12.
\]

Both satisfy

\[
J(d_1)=J(d_2)=\{5\},
\qquad
|M_{d_1}|=|M_{d_2}|=4.
\]

But the exact separator sets are

\[
M_6=\{5,19,25,29\},
\]

with cyclic gaps `14,6,4,6`, while

\[
M_{12}=\{5,13,23,25\},
\]

has gaps `8,10,2,10`.

Therefore

\[
\boxed{
G_{30}(M_6)=14\ne10=G_{30}(M_{12}).
}
\]

So a state/compiler representation that retains only **which prime CRT coordinates changed** can preserve aggregate separator cardinality while losing exact finite-horizon continuation depth.

This is a direct negative test for any support-only compiler proposal. It does not promote or modify Draft #333; #333 remains registry-status WIP.

## 4. Jacobsthal bridge

Define `j(m)` here as the maximum cyclic gap between residues coprime to `m`.

For any `q in J(d)`, consider

\[
S_{d,q}
=
\{x\pmod Q:q\mid x,\ (x+d,Q)=1\}.
\]

Then

\[
S_{d,q}\subseteq M_d.
\]

Writing `x=qt`, the conditions on `t mod Q/q` are a CRT translate of ordinary coprimality to `Q/q`. Consequently

\[
G_Q(S_{d,q})=q\,j(Q/q).
\]

Adding separator points can only shorten gaps, hence:

### T-R005A-BS3 — Jacobsthal separator bound

\[
\boxed{
\rho_d+1
=G_Q(M_d)
\le
\min_{q\nmid d}q\,j(Q/q).
}
\]

Therefore

\[
\boxed{
\rho(P)+1
\le
\max_{q\in P}q\,j(Q/q).
}
\]

The ordinary Jacobsthal function is classical. The contribution here is the exact bridge from it to the Enterprise Boolean phase-separation statistic.

### Exact branch-and-bound consequence

Suppose a candidate separator gap `G0` is already known. If

\[
q\,j(Q/q)\le G_0,
\]

then any shift with `q∤d` cannot improve the candidate. Every improving shift must therefore be divisible by all such `q`.

This turns Jacobsthal data into an exact search-space reduction, not a heuristic.

## 5. Exact `19#` certificate

For the prime prefix through 19,

\[
Q=19\#=9,699,690.
\]

The exact Jacobsthal products are

| q | `j(Q/q)` | `q*j(Q/q)` |
|---:|---:|---:|
| 2 | 17 | 34 |
| 3 | 18 | 54 |
| 5 | 22 | 110 |
| 7 | 22 | 154 |
| 11 | 24 | 264 |
| 13 | 26 | 338 |
| 17 | 26 | 442 |
| 19 | 26 | 494 |

A candidate gap 366 therefore forces every improving shift to be divisible by

\[
2\cdot3\cdot5\cdot7\cdot11\cdot13=30030.
\]

Only the residual `17 x 19 = 323` CRT shift classes remain.

`experiments/r005a_boolean_rho19_certificate.cpp` exhaustively checks these classes and certifies

\[
\boxed{\rho(\{p:p\le19\})=365.}
\]

One maximizing shift is

\[
d=4,564,560,
\qquad
(d,Q)=570,570=Q/17,
\]

with separator gap 366 and `207,360` mismatch positions.

The sparsest largest-prime-only family (`J={19}`) has only `184,320` mismatches, yet its best gap is only 342. Thus separator density is not monotone with local observation depth.

Even inside one fixed support class `J={17}`, different unit multiples have different local radii. For example the fixed-support family has gap 272 at one phase and 366 at another. `gcd(d,Q)` and support determine the Hamming mass, not the local gap geometry.

## 6. Exact relation-resolved actual horizon

Let `P_q={p:p<=q}` be a prime prefix, `Q_q=q#`, and let the actual relation observation be

\[
R_q(n)=\{p\le q:p\mid n,\ n\ge p^2\}.
\]

The exact preperiod is already known:

\[
\mu_q=q^2-q+1.
\]

Let `H_R^act(q)` be the maximum first distinguishing offset over distinct states in the exact one-sided lasso quotient.

### T-R005A-RH1

\[
\boxed{
H_R^{act}(2)=3,
\qquad
H_R^{act}(3)=4,
}
\]

and for every prime `q>=5`,

\[
\boxed{
H_R^{act}(q)=\max(12,q-1).
}
\]

### Proof skeleton

The `q=5` machine is an exact finite base case with horizon 12; states 7 and 13 agree through offset 11 and first differ at offset 12 when the second tail reaches the active 5-strike at 25.

For the inductive step let `r<q` be the previous prime and `B=r#`.

If two states are already distinct in the prior relation quotient, they separate within `H_R^act(r)`.

Otherwise both are at or beyond the prior preperiod and differ by a multiple of `B`.

For `q>=7`,

\[
\mu_r+B\ge q^2.
\]

At `q=7` this is `21+30>=49`. For later prime prefixes, primorial growth together with the classical Bertrand bound makes `B>q^2`.

Hence if the earlier state is still before `mu_q`, the later prior-equivalent state is already beyond `q^2`. Its next q-multiple occurs within at most `q-1` steps, while the earlier state cannot yet carry the active q-label. If both are already q-steady, distinct q-residues separate within at most `q-2`; equal q-residues would make the two canonical cycle states identical.

Therefore

\[
H_R^{act}(q)\le\max(H_R^{act}(r),q-1).
\]

Two independent lower bounds are sharp:

- the fixed `(7,13)` base collision preserves the lower bound 12 for every larger prime prefix;
- choose `x` with `mu_r<=x<mu_q` and `x=1 mod q`, and compare `x` with `x+Q_q`. Prior labels agree forever, while the q-label first separates exactly at offset `q-1`.

The interval `[mu_r,mu_q)` has length `(q-r)(q+r-1)>=q` for `q>=5`, so such an `x` exists.

The executable finite pressure test verifies the exact formula through the prefix ending at 13; the proof supplies the all-prefix induction.

## 7. Boolean actual horizon: exact decomposition, not yet a closed formula

For prime prefixes the Boolean actual preperiod is

\[
\mu_U=q+1.
\]

Let `tau(q)` be the maximum first-difference offset over state pairs with at least one transient state. Then exactly

\[
\boxed{
H_U^{act}(q)=\max(\rho(P_q),\tau(q)).
}
\]

This is a decomposition, not a claimed closed formula for `tau`.

Exact local pressure values are:

| max prime q | `tau(q)` | `rho(P_q)` | full `H_U^act` |
|---:|---:|---:|---:|
| 2 | 3 | 1 | 3 |
| 3 | 4 | 3 | 4 |
| 5 | 15 | 13 | 15 |
| 7 | 23 | 37 | 37 |
| 11 | 63 | 65 | 65 |
| 13 | 91 | 137 | 137 |
| 17 | 91 | 237 | 237 |
| 19 | 173 | 365 | 365 |

Thus steady Boolean geometry already dominates the full actual machine from q=7 through every checked prefix. No theorem is claimed that this remains true for all q.

## 8. T-R005A-PARETO1 — asymptotic attribution-erasure inversion

For prime prefixes, the exact minimal unbounded state counts are

\[
N_R(q)=Q_q+q^2-q+1,
\]

\[
N_U(q)=Q_q+q+1.
\]

Therefore erasing strike attribution saves exactly

\[
\boxed{N_R(q)-N_U(q)=q(q-2).}
\]

Since `Q_q=q#` grows exponentially on the q-scale,

\[
\boxed{
\frac{N_R-N_U}{N_R}\to0.
}
\]

So the relative state-space saving vanishes.

For observation depth, the sparsest separator has

\[
|M_d|=\frac{2\varphi(Q_q)}{q-1}.
\]

A set of `m` points on a cycle of length `Q` has maximum gap at least `Q/m`, hence

\[
\boxed{
\rho(P_q)+1
\ge
\left\lceil
\frac{Q_q(q-1)}{2\varphi(Q_q)}
\right\rceil.
}
\]

The full Boolean actual horizon is at least its steady submachine radius, while

\[
H_R^{act}(q)=\max(12,q-1)\sim q.
\]

By the classical Mertens product theorem,

\[
\frac{Q_q}{\varphi(Q_q)}
\sim e^\gamma\log q.
\]

Therefore

\[
\boxed{
\frac{H_U^{act}(q)}{H_R^{act}(q)}
=\Omega(\log q).
}
\]

So attribution erasure has an asymptotically inverted resource profile:

\[
\boxed{
\text{vanishing relative state saving}
\quad\text{but}\quad
\text{diverging relative observation-depth cost}.
}
\]

This is the strongest Enterprise specialization in the checkpoint.

A transported classical upper bound is also available. Iwaniec's Jacobsthal result gives, for a modulus with `k` distinct prime factors,

\[
j(n)=O((k\log k)^2).
\]

Combined with T-R005A-BS3,

\[
\rho(P_q)
=O\!\left(q(k\log k)^2\right),
\]

and the generic finite-preperiod overhead does not change that order for the full Boolean actual lasso. With `q=p_k~k log k`, this is `O(q^3)`.

This upper bound is prior-art transport, not a new number-theory estimate.

## 9. Concrete `19#` Pareto point

At q=19:

\[
Q=9,699,690,
\]

\[
N_R=9,700,033,
\qquad
N_U=9,699,710.
\]

Only 323 states are removed — about `0.00333%` of the relation-resolved state count.

But

\[
H_R^{act}=18,
\qquad
H_U^{act}=365,
\]

so the exact checked observation-depth ratio is

\[
\frac{365}{18}\approx20.28.
\]

The coarser Boolean language is therefore almost identical in minimal state cardinality but far deeper to identify from finite observation.

## 10. Prior-art attack and status

Relevant classical/adjacent literature:

- Henryk Iwaniec, *On the problem of Jacobsthal*, Demonstratio Mathematica 11(1), 1978, 225–232, DOI `10.1515/dema-1978-0121` — asymptotic Jacobsthal upper bound.
- Mario Ziller, *On differences between consecutive numbers coprime to primorials*, arXiv:`2007.01808` — primorial unit-gap/Jacobsthal structure and restricted coverings.
- Mario Ziller and John F. Morack, *A short note on the computation of the generalised Jacobsthal function for paired progressions*, arXiv:`1706.03668` — paired progressions; adjacent but not the same as the symmetric-difference local separator statistic here.
- generic periodic-word / unary-automata / autocorrelation theory already owns the ultimately-periodic quotient and cyclic-shift language. R005-A does not claim these mother theorems.

Current classification:

- separator cardinality formula — `CLASSICAL CRT SPECIALIZATION`;
- Jacobsthal bridge / branch-and-bound — `ENTERPRISE SPECIALIZATION / PROVED WIP`;
- `Q=30` support-insufficiency counterexample — `EXACT NEGATIVE BOUNDARY / EXECUTABLE CHECKED`;
- exact `rho(19#)=365` — `EXECUTABLE CHECKED / PRIME-SPECIFIC EXACT VALUE`;
- relation actual horizon law — `PROVED STRUCTURAL CHECKPOINT / LEAN PENDING`;
- asymptotic attribution-erasure inversion — `ENTERPRISE SPECIALIZATION / PROVED FROM CLASSICAL INPUTS / NOVELTY UNVERIFIED`.

No result here upgrades #333, #191/#170, or any Prime Toolkit registry status.

## 11. Next frontier inside the same task

The next mathematically justified target is **not** another taxonomy pass and not another sieve implementation.

It is one of:

1. determine whether `rho(P_q)` admits a sharper arithmetic upper/lower law than the Jacobsthal sandwich;
2. determine whether `H_U^act(q)=rho(P_q)` eventually always holds, or construct a later transient-dominant counterexample;
3. formalize T-R005A-RH1 and the separator/Jacobsthal bridge after owner-local Lean is available;
4. use the `Q=30` counterexample as a falsification test against any future support-only prime compiler state.

No generic compiler mother theorem is reopened.
