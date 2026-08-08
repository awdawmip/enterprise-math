# Legendre Pressure Test — Supplement 06

Status: `ACTIVE RESEARCH NOTE`  
Scope: basin-level support incidence, unique large-modulus hits, and exact aggregation of the four-support large tail.  
Discipline: **this note does not prove Legendre's conjecture.**

## 1. Why move from states to supports

The previous supplements progressively simplified a single composite state's large Möbius tail. That is useful, but it cannot by itself defeat the sieve parity obstruction: for every composite state the complete Möbius divisor sum is already zero.

A successful next step must use information shared by **different states in the same square basin**. The common datum is the same root/anchor \(k\).

The interval

\[
I_k=\{k^2+1,\ldots,k^2+2k\}
\]

has exactly \(2k\) states. Therefore any modulus larger than \(2k\) can hit the entire basin at most once. This converts a large divisor from a repeated local sieve event into a basin-level support incidence.

## 2. L023 — Unique large-support hit and centered square carry

Status: `PROVED`

Let

\[
G>2k
\]

be an integer modulus. Center the basin at

\[
M=k(k+1).
\]

Then

\[
I_k=M+\{1-k,\ldots,k\}.
\]

Because two distinct multiples of \(G\) differ by at least \(G>2k\), at most one multiple of \(G\) can lie in \(I_k\).

Write

\[
a=M\bmod G,
\qquad 0\le a<G.
\]

A multiple of \(G\) occurs in the centered window exactly when the representative of \(-a\) lies in \([1-k,k]\). Since \(G>2k\), the two possible boundary cases are disjoint. Thus the exact hit indicator is

\[
\boxed{
\eta_G(k)
=
\mathbf 1_{a<k}
+
\mathbf 1_{a\ge G-k}
\in\{0,1\}.
}
\]

If \(a<k\), the unique offset is

\[
s=-a.
\]

If \(a\ge G-k\), the unique offset is

\[
s=G-a.
\]

The unique state, when it exists, is

\[
\boxed{n_G(k)=k(k+1)+s.}
\]

This is the large-modulus form of the centered square-carry criterion: the entire basin hit is decided by one residue of the common anchor.

### Half-scale cofactor

If the hit exists, write

\[
n_G(k)=G h_G(k).
\]

Since \(G>2k\), L016 applies directly and gives

\[
\boxed{
h_G(k)\le\left\lfloor\frac{k+1}{2}\right\rfloor.}
\]

So every large support hit comes with a uniquely determined half-scale cofactor.

## 3. L024 — Exact transverse support equals a smooth-cofactor condition

Status: `PROVED`

Let \(P\) be a finite set of transverse primes:

\[
p\le k,
\qquad
p\nmid k(k+1)
\quad(p\in P),
\]

and let

\[
G_P=\prod_{p\in P}p>2k.
\]

Suppose the unique hit of \(G_P\) exists:

\[
n=G_P h.
\]

Then \(h\le\lfloor(k+1)/2\rfloor\le k\).

We claim that the full transverse small-prime support of \(n\) is **exactly** \(P\) if and only if every prime factor of \(h\) belongs to \(P\).

### Forward direction

Assume \(P\) is the full transverse support. If a prime \(q\mid h\), then

\[
q\le h\le k.
\]

Also \(q\mid n\). The state is anchor-surviving because every prime in its full support is transverse, so \(q\nmid k(k+1)\). Therefore \(q\) is itself a transverse small prime divisor of \(n\), and fullness of \(P\) forces

\[
q\in P.
\]

### Reverse direction

Conversely, if every prime factor of \(h\) lies in \(P\), then every prime divisor of \(n=G_Ph\) is already in \(P\). Since all primes in \(P\) are transverse and each divides \(G_P\), the full transverse support is exactly \(P\).

Hence

\[
\boxed{
\operatorname{Supp}_{\mathrm{tr}}(n)=P
\iff
\operatorname{PrimeSupp}(h)\subseteq P.
}
\]

The multiplicities inside \(h\) are unrestricted. The cofactor is `P`-smooth, not necessarily square-free.

This is a useful self-consistency condition: a proposed support set either closes under its half-scale cofactor or automatically grows to a larger support.

## 4. L025 — Exact four-support basin aggregation

Status: `PROVED`

Let \(\mathcal P_{\mathrm{tr}}(k)\) be the set of transverse primes at most \(k\), and let

\[
\mathfrak S_4(k)
=
\left\{
P\subseteq\mathcal P_{\mathrm{tr}}(k):
|P|=4,
G_P=\prod_{p\in P}p>2k
\right\}.
\]

For each \(P\in\mathfrak S_4(k)\), define:

1. the binary common-anchor hit \(\eta_{G_P}(k)\) from L023;
2. when \(\eta=1\), the unique half-scale cofactor \(h_P\);
3. the exact-support indicator
   \[
   \sigma_P(k)
   =
   \mathbf 1_{\operatorname{PrimeSupp}(h_P)\subseteq P};
   \]
4. the four-support graph tail from L022,
   \[
   \tau_P(k)
   =
   C_P(U_P)-I_P(U_P),
   \]
   where
   \[
   U_P
   =
   \left\lfloor\frac{G_P-1}{2k}\right\rfloor
   \le
   \left\lfloor\frac{k+1}{2}\right\rfloor.
   \]

Then the total contribution of **all basin states whose full transverse support has exactly four primes** to the large region \(b>2k\) is

\[
\boxed{
\mathcal L_4(k)
=
\sum_{P\in\mathfrak S_4(k)}
\eta_{G_P}(k)\,
\sigma_P(k)\,
\tau_P(k).
}
\]

### Proof

If a basin state has exact four-prime transverse support \(P\) and contributes to the large region, then \(G_P>2k\). Since the basin has length \(2k\), this support product identifies at most one state. L023 gives exactly that unique state; L024 says exactly when the hit has no additional transverse support; L022 gives its complete four-support large tail.

Conversely, every \(P\) with \(\eta=1\) and \(\sigma=1\) constructs one and only one basin state with exact support \(P\). Distinct support sets cannot represent the same exact-support state.

Therefore the support sum is a bijective reindexing of the exact four-support state sum.

## 5. Why this is different from another statewise Möbius rewrite

The new formula uses one common \(k\) in three independent places:

\[
\boxed{
\text{common anchor residue}
\quad+\quad
\text{half-scale cofactor}
\quad+\quad
\text{half-scale graph balance}.
}
\]

The basin states themselves no longer need to be scanned.

The binary hit

\[
\eta_{G_P}(k)
\]

is determined directly from

\[
k(k+1)\bmod G_P,
\]

and the exact-support closure is determined from a cofactor at most half the root scale.

This is the first P017 formula that is naturally indexed by **support sets across the whole basin**, rather than by divisors inside one already chosen state.

## 6. Known negative example inside the aggregate language

For \(k=58\), take

\[
P=\{3,5,7,11\},
\qquad
G_P=1155.
\]

The centered anchor is

\[
M=58\cdot59=3422,
\]

so

\[
M\bmod1155=1112\ge1155-58.
\]

Therefore \(\eta=1\) and the unique offset is

\[
s=1155-1112=43.
\]

Hence

\[
n=3422+43=3465,
\qquad
h=3465/1155=3.
\]

The cofactor is `P`-smooth, so \(\sigma=1\). L022 gives

\[
\tau_P=-2.
\]

Thus this support contributes \(-2\) to \(\mathcal L_4(58)\).

The important point is not the sign itself but that the negative state is now recovered from the **common support carry** without searching the interval.

## 7. Next target: aggregate compensation

The termwise route is now exhausted enough to be clear: individual support contributions can be negative.

The next mathematically meaningful question is whether the support-indexed negative mass has a basin-level compensation mechanism. Candidate structures are now explicit:

1. **carry collisions:** different support products \(G_P\) may hit the same or neighboring centered offsets only under strong modular compatibility;
2. **smooth-cofactor closure:** negative support hits are discarded whenever their half-scale cofactor introduces a fifth transverse prime;
3. **graph compensation:** each surviving four-support hit carries both isolated-vertex negative rank and cycle positive rank;
4. **small-region linkage:** every half-scale cofactor is itself a small divisor of the hit state, providing a direct bridge back to the \(b\le k\) transverse-discrepancy region.

The priority is to search for an injection or inequality after summing over support sets, not to assert statewise positivity again.

## 8. Executable validation

`src/enterprise_math/basin_aggregate.py` and `tests/test_basin_aggregate.py` check:

- the exact centered-residue hit criterion for moduli larger than \(2k\);
- the unique state and half-scale cofactor;
- the smooth-cofactor exact-support criterion;
- rejection of anchor-contaminated support sets;
- rejection of a four-prime subset when the unique cofactor introduces a fifth transverse prime;
- reconstruction of the known \((58,3465)\) negative state from its support set;
- equality of the aggregate total with the sum of its explicit support contributions.

Finite computation validates the implementation. L023–L025 follow from the proofs above and the previously established square-basin identities.
