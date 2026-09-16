# RSA-270 continuation: 3-adic torsion multiplier packets and singular-Hensel lifting

Status: `RESEARCH NOTE / EXACT THEOREMS + ORACLE REDUCTION / NOT CANONICAL PROMOTION`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-06T20:08:32+08:00`  
Parent salvage PR: `#1331`  
Source line corrected: external research PR `#1330`  
Verifier: `experiments/rsa270_3adic_torsion_packet_ladder.py`

## 0. Assumptions and status

Let `N=pq`, `p<q` distinct odd primes. The 3-adic statements below use the explicit conditional branch

`H2: p ≡ q ≡ 2 (mod 3)`

so, because the factors are odd, `p ≡ q ≡ 5 (mod 6)`.

No RSA-270 factor is obtained. The new result is a rigorously scoped observable class that is **strictly richer than the previously claimed fixed `S mod 72` channel**, but whose efficient N-only evaluation remains open.

Tool-reuse resolution: this is a task-local composition of existing finite-fiber / precision-refinement / symmetry ideas (`T4`, `T5`, `T7`); no new general-purpose tool family is claimed.

---

## 1. Composite odd multiplier profile: exact divisor-packet decomposition

For odd `k` with `gcd(k,N)=1`, write `b=k/a` for `a|k`. The bivariate profile coefficient decomposes exactly as

`P_(kN)(u) = 2 sum_(a|k) [ W_((a+bN+2)/2)(u) + W_((ap+bq+2)/2)(u) ]`.

The first packet is N-only. The factor-bearing packet is indexed by

`X_a := a p + (k/a) q`.

The following identities are exact.

### 1.1 Trace / reciprocal identities

`sum_(a|k) X_a = sigma_1(k) S`, where `S=p+q`.

For the reciprocal divisor `b=k/a`,

`X_a + X_b = (a+b) S`,

`X_a - X_b = (a-b)(p-q)`,

`X_a X_b = k S^2 + (a-b)^2 N`.

Thus a square multiplier `k=m^2` contains the fixed-point boundary

`X_m = m S`.

### 1.2 Two-boundary Pluecker identity

For divisors `a,c|k`, put `b=k/a`, `d=k/c`, and `Delta=ad-bc`. Then

`(d X_a - b X_c)(a X_c - c X_a) = Delta^2 N`.

If `Delta != 0` and the exact two boundary values are known, then

`p=(d X_a-b X_c)/Delta`,
`q=(a X_c-c X_a)/Delta`.

So two independent exact multiplier boundaries are factor-complete.

### 1.3 No nontrivial exact boundary collisions when `gcd(k,N)=1`

If `X_a=X_c` with `a!=c`, then

`ac p = k q`.

Since `a,c|k`, this forces `q|k`, contradicting `gcd(k,N)=1`. Hence all `X_a` are distinct.

Moreover

`p | (X_a-X_c) <=> p | (b-d)`,
`q | (X_a-X_c) <=> q | (a-c)`.

Therefore if `k < min(p,q)`, every nonzero pairwise boundary difference has gcd 1 with N. A small composite multiplier cannot produce a direct factor merely by taking gcds of exact boundary differences.

### 1.4 Correct narrow closure theorem

Any polynomial expression in the boundary packet that is invariant under factor swap `p<->q` is a symmetric polynomial in `p,q`, hence is a polynomial in `S=p+q` and `N=pq`.

This is a valid **boundary-polynomial closure theorem**. It is intentionally much narrower than #1330's rejected universal claim that all Enterprise/BRC observables close at `S mod 72`.

The next sections exhibit a non-polynomial periodic/torsion packet that escapes that narrow closure.

---

## 2. A new observable class: `3^e` multiplier at `3^e`-torsion

Let

`m_e = 3^e`, `e>=2`,

and let `zeta_e` be a primitive `m_e`-th root of unity.

Set the multiplier `k=m_e`. The hidden factor packet in `P_(m_e N)(zeta_e)` is

`H_e(p,q) = 2 sum_(j=0)^e W_((3^j p + 3^(e-j) q + 2)/2)(zeta_e)`.

The two extreme terms are

`E_e(p,q) = 2 [ W_((p+m_e q+2)/2)(zeta_e) + W_((m_e p+q+2)/2)(zeta_e) ]`.

These extreme terms are not a function of `S mod 2m_e` alone.

### 2.1 Exact cyclotomic form of one W-block

For odd `m` and `t=s-1`,

`W_(t+1)(zeta) = zeta (zeta^t-zeta^(-t)) / (zeta^2-1)`.

For an odd residue `r mod 2m_e`, define

`tau_e(r) := (r+m_e)/2 (mod m_e)`.

Under H2, `r≡5 (mod6)`, hence

`tau_e(r) ≡ 1 (mod3)`.

The extreme packet is therefore a fixed nonzero scalar times

`(zeta^tau(p)-zeta^-tau(p)) + (zeta^tau(q)-zeta^-tau(q))`.

---

## 3. Extreme torsion packet injectivity theorem

**Theorem.** Let `e>=2`, `m=3^e`. On unordered H2 residue pairs modulo `2m`, the map

`{p,q} -> E_e(p,q)`

is injective.

### Proof

Let `n=m/3=3^(e-1)`. Suppose two H2 pairs give the same extreme value. After removing the common nonzero scalar, this gives a sparse integer relation

`R(zeta)=0`

between the eight possible monomials `zeta^(±tau(p))`, `zeta^(±tau(q))`, and the corresponding terms from the second pair.

Reduce exponents modulo `m` so `deg R < m`. Since `zeta` is primitive,

`Phi_(3^e)(x) = 1 + x^n + x^(2n)`

divides `R(x)`. Therefore, in every triple of coefficient positions

`r, r+n, r+2n`,

the three coefficients of `R` must be equal.

But `n` is divisible by 3, so each such triple stays in one residue class modulo 3. Under H2 all positive `tau` exponents are `1 mod3`, all negative `tau` exponents are `2 mod3`. In either mod-3 sector the sparse relation contains at most two positive and two negative monomials. A nonzero multiple of `1+x^n+x^(2n)` would require three equal nonzero coefficients in one sector, which is impossible. Hence `R` is coefficientwise zero.

Looking in the `1 mod3` sector gives equality of the multisets of positive `tau` exponents. Since `tau_e` is injective from odd residues mod `2m` to residues mod `m`, the unordered factor residue pairs are equal. QED.

The verifier exhaustively checks this injection on **all** H2 unordered residue pairs for `e=2,3,4`:

- `m=9`: 3 allowed factor residues, 6 unordered pairs, all 6 signatures distinct;
- `m=27`: 9 residues, 45 unordered pairs, all 45 distinct;
- `m=81`: 27 residues, 378 unordered pairs, all 378 distinct.

This is a genuine new channel relative to a fixed `S mod 72` description: periodic torsion of multiplied profiles can distinguish factor pairs having the same low S residue.

---

## 4. Singular-Hensel lifting structure

At precision

`M_(e-1)=2*3^(e-1)`,

suppose the unordered factor residue pair is already known. Each factor has three lifts modulo

`M_e = 3 M_(e-1) = 2*3^e`.

Writing the lifts as

`p'=p+i M_(e-1)`, `q'=q+j M_(e-1)`, `i,j in F_3`,

the product condition `p'q'≡N (mod M_e)` becomes one nondegenerate linear equation in `(i,j) mod3`, because H2 makes both previous factor residues nonzero modulo 3.

Hence there are exactly three ordered lift solutions; after forgetting factor order there are at most three candidates (sometimes two because of symmetry).

All intermediate terms `j=1..e-1` of `H_e` are already determined by the previous residue pair, because their coefficients contain at least one factor 3 and require no more than the previous precision. Only the two extreme terms carry the new lift branch.

Combining this with the injectivity theorem gives:

**Recursive lifting theorem.** An oracle for the exact coefficient

`C_e(N) := P_(3^e N)(zeta_(3^e))`

selects the unique H2 factor-pair lift modulo `2*3^e` from the 2-3 product-compatible candidates at level e.

Starting from the H2 base pair `{5,5} mod6`, the sequence `C_2,C_3,...` recursively recovers the local factor residues to arbitrary 3-adic precision.

This is an oracle reduction, **not** an efficient N-only algorithm: computing `C_e(N)` from the product side is the unresolved step.

### Validation

The exact decoder was simulated with oracle values generated from known factors.

- Published RSA-260 factor pair: exact recovery through `e=5`, ending at the true unordered residues modulo `2*3^5=486`.
- 10 independently generated H2 semiprimes: exact recovery through `e=5` in every case.
- At each tested level the product equation left only 2 or 3 candidate lifts and the torsion packet selected exactly one.

---

## 5. Compact twisted-trace observables

The full cyclotomic coefficient has dimension growing with `3^e`, so the important question is whether the branch selector can be compressed.

For `K_e=Q(zeta_e)` define the integer functional

`Lambda_(e,r)(Z) := Tr_(K_e/Q)(zeta_e^(-r) Z)`.

For `m=3^e`, `n=m/3`, the Ramanujan sum gives

`Tr(zeta^t) = 2n` if `t≡0 (mod m)`,
`Tr(zeta^t) = -n` if `t≡n or 2n (mod m)`,
`Tr(zeta^t) = 0` otherwise.

Therefore, if a Laurent profile has residue masses `c_j` modulo m,

`Lambda_(e,r) = n [ 2 c_r - c_(r+n) - c_(r+2n) ]`.

So a twisted trace is exactly a **three-way residue imbalance** across one cyclotomic fiber. It is an integer, not a large cyclotomic output.

Because the trace pairing on `K_e` is nondegenerate, any two distinct candidate torsion coefficients are separated by some `Lambda_(e,r)`. With at most three candidate lifts, at most two suitably chosen twisted traces are information-theoretically sufficient to distinguish them. An explicit fixed polylog-time selector for the best `r` values is still open; the verifier also records small explicit separating probe sets through e=5.

This gives a sharply defined computational target:

> Compute one or two adaptively chosen integers `Lambda_(e,r)(C_e(N))` from N without knowing p,q.

If that can be done cheaply at successive e, the 3-adic factor lift follows.

---

## 6. RSA-270: the first unresolved bit is already concrete

For RSA-270,

`N mod54 = 19`, and under H2 the prior corrected lattice gives `S≡16 mod72`.

At level `e=2` (`m=9`), the H2 factor residues modulo 18 compatible with `N≡1 mod18` are exactly

`{5,11}` or `{17,17}`.

For the full profile coefficient

`C_2(N)=P_(9N)(zeta_9)`,

the ordinary field trace is predicted to be

- `Tr(C_2)=36` for factor residues `{5,11} mod18`;
- `Tr(C_2)=0` for factor residues `{17,17} mod18`.

Equivalently, after subtracting the N-only packet, the hidden-packet traces are `0` and `-36`.

For the exact RSA-270 residue `N mod54=19`, these two outcomes imply

- `Tr(C_2)=36 -> S≡52 mod54 -> S≡160 mod216` together with `S≡16 mod72`;
- `Tr(C_2)=0  -> S≡34 mod54 -> S≡88 mod216` together with `S≡16 mod72`.

Thus **one exact integer coefficient trace at order 9 would add a real new bit of RSA-270 information**, lifting the current H2 class from mod72 to one of two classes mod216.

No N-only method for obtaining this trace is presently known.

---

## 7. Exact cubic norm identity: the BRC interpretation of the missing trit

Let

`F(Q,u)=prod_(n>=1) ((1-Q^(2n))^2 (1-u^2 Q^(2n))(1-u^-2 Q^(2n))) /
                    ((1-u Q^(2n-1))^2(1-u^-1 Q^(2n-1))^2)`.

Let `omega` be a primitive cube root of unity. Factorwise use

`prod_(r=0)^2 (1-omega^r z) = 1-z^3`.

This gives the exact formal-product identity

`prod_(r=0)^2 F(Q, omega^r u)
   = A(Q) F(Q^3,u^3)`,

where

`A(Q)=prod_(n>=1) (1-Q^(2n))^6 / (1-Q^(6n))^2`.

Now set `u=zeta_(3^e)`. The three substitutions `u,omega u,omega^2 u` are exactly the degree-3 Galois conjugates over `Q(zeta_(3^(e-1)))`. Hence

`Norm_(K_e/K_(e-1)) F(Q,zeta_(3^e))
   = A(Q) F(Q^3,zeta_(3^(e-1)))`.

This gives a corrected BRC/precision picture:

- every 3-adic cyclotomic level is a cubic extension;
- the norm collapses the three conjugate branches to the lower level;
- the factor lift resides in the missing conjugate/branch choice;
- the product constraint leaves 2-3 candidate lifts, matching the cubic local structure.

This replaces the falsified shallow claim that a 3-adic carry quotient simply “erases exactly one bit per digit”. The natural local unit is a **degree-3 branch/trit**, not a universal one-bit law.

The norm identity does not yet give a fast target-coefficient recurrence: coefficient extraction from a product norm introduces convolution with lower coefficients. That is the next mathematical bottleneck.

---

## 8. What this changes from #1330

The statement

`all tested Enterprise/BRC/discrete observables -> only S mod72; no new channel`

is no longer tenable once multiplied torsion packets are admitted.

The corrected statement is:

1. fixed boundary-polynomial observables close in `(S,N)` (proved narrow closure);
2. fixed low torsion of the original N-profile gives only low residue / hidden-residuosity information;
3. **multiplier-torsion packets `P_(3^eN)(zeta_(3^e))` form a strictly richer hierarchy that is locally factor-complete under H2**;
4. the unresolved wall is now precise: efficient N-only computation of a small twisted-trace coefficient of that hierarchy.

That is a stronger research frontier than the prior “72 is terminal” conclusion.

## 9. Next target

Do not spend the next round enlarging generic modulus tables.

Target the first concrete scalar

`Tr_Q(zeta9)( [Q^((9N-1)/2)] F(Q,zeta9) )`.

For RSA-270 it is provably either `36` or `0` under H2, and the two values lift `S` to `160` or `88 mod216` respectively.

The productive questions are:

1. derive a direct 9-dissection / modular-function expression for this trace coefficient;
2. test whether its coefficient sequence satisfies a usable recurrence, Hecke-type relation, or sparse BRC residue-count formula;
3. prove a no-go if exact evaluation still requires divisor/factor data.

Until one of those succeeds, this is a **new exact hidden channel, not a factorization algorithm**.
