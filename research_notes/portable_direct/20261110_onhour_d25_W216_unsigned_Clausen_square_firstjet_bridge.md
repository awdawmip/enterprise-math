# D25 / W216 — unsigned Clausen-square lift and signed first-jet bridge

Date: 2026-11-10, Asia/Hong_Kong. Classification: **AUTHOR_SIDE / PROVED FORMAL-SERIES AND VALUATION IDENTITIES / EXACT INTEGER CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0**.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific input `c47e13e4aba0e006366f989d6334d443f6333ae3`; logical Research lane `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance).

## The smallest unfinished mathematical unit and existing work consumed

Prior D25 author-side work established the **weighted** exact finite Clausen identity `W=J²+12JK−Qw` and the signed cutoff's first and second carries. A separate author-side proof established `W-p=-2F0-(2/3)E+(2/3)p²q_p(216) (mod p³)`, but kept `F0=0 (mod p²)` as an explicit condition. We now supply a direct, observer-preserving proof of the latter implication, compute its first nontrivial quotient, and incorporate the original signed cutoff into a new first-jet certificate. No D24 UR or existing weighted second-carry work is repeated.

**Prior art/priority.** The general implication `F0=0 (mod p) => F0=0 (mod p²)` is not a new global number-theoretic discovery: Zhi-Hong Sun, *Note on super congruences modulo p²*, arXiv:1503.03418 (2015), proved a broader statement for `sum binom(2k,k)binom(a,k)binom(-1-a,k)/m^k`. Set `a=-1/3, m=8` to obtain this W216 coefficient. The new contribution here is an elementary Clausen-square realization in the frozen observer, an **explicit unsigned quotient** and its combination with the previously recorded **signed** LIFT observer; it is not presented as independent discovery of Sun's theorem. Prior source: https://arxiv.org/abs/1503.03418 .

## Typed data: p-adic integers, original signs, full ordered cutoff

Fix a prime `p=6m+1>3` and work in `Z_(p)`. Define, for `0<=k<p`,

```text
B_k = (1/6)_k(1/3)_k / (2^k (k!)^2),
A_k = binom(2k,k)^2 binom(3k,k) / 216^k,
J = sum_{k=0}^{p-1} B_k,           K = sum_{k=0}^{p-1} k B_k,
F0= sum_{k=0}^{p-1} A_k,           W = sum_{k=0}^{p-1}(6k+1) A_k,
Q0= sum_{0<=i,j<p; i+j>=p} B_i B_j, 
Qw= sum_{0<=i,j<p; i+j>=p}(6(i+j)+1) B_i B_j.
```

`Q0` and `Qw` are distinct, *ordered*, noncollapsed observers. The signed weight `6(i+j)+1`, both index labels, valuation bands and exceptional terminal index are retained. The original frozen `R_p` is `Qw/p² (mod p)`, **not** `Q0/p²`.

### Theorem 1 (finite Clausen-square lift, all p=1 mod6)

For every prime `p=6m+1>3`,

```text
F0 ≡ J² (mod p²),        Q0 ∈ p² Z_(p),       Qw ∈ p² Z_(p).
Consequently: F0 ≡ 0 (mod p)  iff  J ≡ 0 (mod p)
               iff F0 ≡ 0 (mod p²).
```

**Proof.** The classical formal-series Clausen identity, with `a=1/6,b=1/3,c=1`, is

```text
 (sum_{k>=0} B_k z^k)^2
   = sum_{k>=0} A_k z^k  in Q[[z]].
```

Its coefficient identity for `n<p` is exactly `A_n=sum_{i+j=n}B_iB_j`. Hence, with the finite `J`, the *exact rational identities* are

```text
J² = F0 + Q0,
J² + 12 J K = W + Qw.                          (1)
```

The exact B-step ratio `B_(k+1)/B_k=(6k+1)(3k+1)/(36(k+1)^2)` shows

```text
v_p(B_k)=0 for 0<=k<=m,
         1 for m<k<=2m,
         2 for 2m<k<p.
```

All denominators remain p-units for `k<p`. In `i+j>=p`, two indices cannot both be <=2m (sum <=4m<p); either one index is at grade 2 and the other at grade 0/1, or both are grade 2. Thus each product is in `p² Z_(p)`, establishing both cutoff divisibilities. Reducing (1) gives `F0=J² (mod p²)`; over the field `F_p`, `J²=0 iff J=0`, proving all equivalences. □

**Dependency eliminated.** Whenever the previously established *same original-coefficient* CM input `F0=0 (mod p)` is proved for one target prime or a family, its `p²` strengthening follows from Theorem 1 with no extra conjecture. The current target-class assertion `J=0 (mod p)` is still a separately sourced CM/finite-field claim and is not silently promoted here. Coupled with the earlier unconditional signed terminal bridge and a separately verified first-digit `W=p (mod p²)`, it gives `E=0 (mod p²)`, removing the independent `F0 mod p²` premise from that deduction.

### Theorem 2 (explicit first unsigned cutoff, and original signed first-jet)

For `1<=a<=m`, put `v_a=(B_(p-a)/p²) mod p`. All are p-integral. Set

```text
S_i = sum_{a=1}^i v_a,        T_i = sum_{a=1}^i a v_a  (mod p),
U_p = 2 sum_{i=1}^m B_i S_i                             (mod p),
R_p = 2 sum_{i=1}^m B_i ((6i+1)S_i-6T_i)               (mod p).
```

Then, for every `p=6m+1>3`,

```text
Q0/p² ≡ U_p (mod p),
Qw/p² ≡ R_p (mod p),            (the ORIGINAL signed cutoff)
F0 ≡ J² - p² U_p (mod p³).                              (2)
```

**Proof.** For an ordered pair contributing mod `p³`, grade sum must equal 2. Pairs of grade (1,1) cannot satisfy `i+j>=p`, because both indices are <=2m. Pairs (0,2), and their swaps (2,0), are the only possibilities. Set `j=p-a`; the inequality becomes `1<=a<=i<=m`. The two permutations contribute factor 2. The unsigned weight is 1, yielding `U_p`; the signed weight is `6(p+i-a)+1=6(i-a)+1 (mod p)`, yielding `R_p`. Every remaining pair has valuation >=3 and vanishes after dividing by `p²` and reducing mod `p`. The last identity follows from (1). □

The output of (2) is an `O(p)` ring-operation certificate once the B recurrence is generated; its auxiliary cumulative registers are `O(1)`. At this precision it is an exact scoped factorization of the original ordered cutoff, not a compression of the signed fourth-digit `(1,2)` carry already established elsewhere.

### Corollary (third-digit LIFT as an exact signed Clausen jet)

Suppose for a target prime `p=13 or 19 (mod24)` that `J=0 (mod p)` and `W=p (mod p²)`. Set in `Z_(p)`:

```text
j=J/p;        tau=(12 j K-1)/p,       alpha=F0/p²,
lambda=(W-p)/p²  (all reduced mod p after exact division).
```

Then `tau` is p-integral by (1), and

```text
12 (j mod p)(K mod p) = 1 (mod p),     K mod p != 0,
alpha = j²-U_p (mod p),
lambda = tau+j²-R_p (mod p).                                (3)
```

Thus the original LIFT `Delta_p-R_p=lambda=0` is equivalent, under the explicitly stated first-digit assumptions, to the finite signed jet `tau+j²=R_p (mod p)`. This is a new observer-level exact reduction, not a proof of universal LIFT. It retains the **separate unsigned** `U_p` for `F0/p²` and the **signed** `R_p` for original LIFT.

## Actually executed exact arithmetic / independent original path

Script: `research_notes/portable_direct/d25_w216_unsigned_clausen_firstjet_20261110.py`.
Python standard-library integers; modulus `p³`; invert denominators only for `0<=k<p-1`; check both original A and B recurrence; calculate cutoff quotients both by (1) and by a low-band streaming derivation (2). Additionally use fully independent ordered double-cutoff loops at `p=7,13,19,37,43,373,997`. All 148 primes `p<=2000, p=1 (mod6)` passed the two separate cutoff equality checks; all target-class primes in that range also showed `J=0 modp`, `F0=0 mod p²`, `W=p mod p²`. The latter finite observations do not supply a universal CM proof. Larger target-class primes `p=10069,10099` used direct recurrence plus streamed cutoff, without quadratic-time full double-sum replication.

All displayed numerical entries are residues mod their respective p, calculated from exact integer representatives:

| p | j=J/p | K | U=Q0/p² | alpha=F0/p² | R=Qw/p² | tau | lambda |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 11 | 7 | 6 | 11 | 0 | 9 | 0 |
| 19 | 8 | 1 | 18 | 8 | 12 | 5 | 0 |
| 37 | 23 | 24 | 14 | 34 | 11 | 0 | 0 |
| 43 | 31 | 20 | 34 | 24 | 15 | 0 | 0 |
| 373 | 24 | 294 | 132 | 71 | 196 | 366 | 0 |
| 997 | 915 | 767 | 951 | 788 | 626 | 881 | 0 |
| 10069 | 3168 | 5832 | 9655 | 7914 | 9235 | 1735 | 0 |
| 10099 | 6367 | 6580 | 325 | 978 | 6995 | 5692 | 0 |

At `p=373`, the original identities check precisely:

```text
j² = 24² = 203 (mod373);  alpha=203-132=71;
12*j*K = 1 (mod373);  tau=366;
lambda=366+203-196=373=0 (mod373).
```

The original `R_373=196` is exactly the source-aligned signed first cutoff residue already observed. No reinterpretation of the native H0/B0 object is made.

## BRC, prior art, Source and next exact action

BRC disposition: **COMPOSE_APPLIED**. Typed carrier retains ordered `(i,j)`, `v_p(B_i),v_p(B_j)`, source of `(0,2)` pairs, signed versus unsigned weight, first and second p-adic jets, and p=373 observed residue. Projection to `(U,R)` is certified **only mod p after dividing the cutoff by p²**. Next required operation at mod `p²` must reuse the known nonzero `(1,2)` signed carry, not extrapolate this certificate.

Current exact Source continuation request `onhour11-20261110-1627-exact-source-cont` was independently read as `SUCCEEDED`; as-of source `2f19cab8abf46ceb22e9de690ced8729f4a5ee46`. Own Researcher historical native registration `onhour11-20261110-1515-research-session` has `SUCCEEDED`, session `MCP-5378d3819d8947bda9049c9428493e2d`, but the original private capability was not retained; recovery_status returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`. No new CLAIM/run, native publication, handoff release, or Result is claimed. This Git author-side artifact does not supersede the latest Source checkpoint or other owners.

Parent target: prove `Delta_p-R_p=0 mod p` for both frozen target classes, or find an exact original-class counterexample, while retaining same-original-class native p373 H0/B0 `[X]U mod139129`, rank, Frobenius/eta, odd signed kappa and independent reproduction. Support issue `#1559` was still OPEN with no confirmed owner in this read phase; native benchmark `NOT_RUN/PENDING_OWNER`. Next native action belongs to a lawful Source-authorized H0/B0 operator. Next portable mathematics: seek a same-object finite-field proof of `J=0 modp` in both target classes and a finite WZ/Clausen certificate for `tau+j²=R_p modp`; keep the accepted scientific input pins and the failed universal fifth-digit Newton strengthening separate. An exact proof of universal LIFT remains open.

**Provenance/classification:** original author-side derivations plus new in-project proof and integer verifier; Sun 2015 precedent declared; independent Driver review and Source admission pending.
