# D25/LIFT — All-digit original-parameter diagonal bridge with authentic four-face Ward sources

Date 2026-10-26. Requested Research lane `chatgpt-research-hourly-enterprise-math-20260923`, separate from maintenance `chatgpt-hourly-enterprise-math-20260921`. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** No winning native claim, authorized open, Source checkpoint, original-class CM experiment, WZ cancellation or independent Driver approval is claimed.

## Precise new question and consumed results

The existing six-channel Hasse third-digit computation and the genuine two-parameter Green–Ward master (research_notes/portable_direct/20261026_hourly_d25_bivariate_master_ward_r13.md) give correct finite-order interfaces, but do not yet provide a **direct all-precision, source-preserving expression for the fixed original ordered Clausen cutoff**. The signed 3+2+1 source theorem (20261026_offphase_d25_genuine_signed_ward_diagonal_kernel_source_neutral.md) independently proves that parameter-diagonal observation does not reconstruct every individually labelled Hasse source; that caveat remains binding.

We derive one exact diagonal *scalar* bridge, retaining both orientations of finite shift faces and a separately ordered high–high population. This is a source normalization and mathematical dependency advance, not an assertion of an additional cross-Hasse cancellation.

Let `p=6m+1 >= 7` be prime; `R=Z_(p)`; `L=1-2m`, `N=2m-1`. Define the corrected bivariate-input germ already in the master,

```text
f_r(z) = (-m-z)_r (-2m-2z)_r / ((1-p/2-3z)_r r!), 0<=r<p.
```

The **new exact specialization** is at `theta=-p/6`, which is a *parameter evaluation*, not a change of the fixed geometric rank weight `2^n`. Define the original coefficient `r_r` by `r_0=1` and

```text
r_(k+1)/r_k = (6k+1)(3k+1)/(36(k+1)^2), 0<=k<p-1.
```

### Theorem 1 — exact original-series identification and second-order tail division

For every `0<=r<p`,

```text
f_r(theta) = (1/6)_r(1/3)_r / (r!)^2 = 2^r r_r                 (1)
```

**exactly in the rational field**, rather than only modulo a power of `p`. For every `2m<r<p`, the original high-tail factor has precisely two `p`-factors and

```text
beta_r := f_r(theta)/p^2  belongs to R^×.                     (2)
beta_r mod p =
 (-1)^m m! (2m)! (r-m-1)! (r-2m-1)! / [18 (r!)^2] mod p.    (3)
```

Also `v_p(f_(2m)(theta))=1`. Proof: at `theta=-p/6`, the three Pochhammer parameters are exactly `1/6,1/3,1`. In the numerator products up to `r-1<p`, factors `6k+1` and `3k+1` each have one multiple of `p`, precisely at `k=m` and `k=2m`; for `r<=2m` only the first is present when `r>m`. Every factorial denominator is a `p`-unit. Delete these two factors, evaluate the remaining products modulo `p`, and obtain (3). The difference between denominator 18 for `f` and denominator 36 for original `r` in (1) is an essential factor `2^r`: identifying `f` directly with `r` would be erroneous.

### Theorem 2 — an original-series Green–Ward equation with all genuine finite faces

Use the **original normalized** ordered low–high carrier

```text
V_n^h = sum_(1<=j,ell<=2m; ell-j=n) j^h f_j(theta) beta_(p-ell),
  h=0,1, L<=n<=N; V_(N+1)^h=0.
Z_n = 2 V_n^1 - (p-n)V_n^0.
```

These `V_n^h` are `M_n^h(theta,theta)/p^2` exactly. Define the source `E_n` by the **actual two-ended shift faces**:

```text
n>=0:
 E_n = 2(m+theta)^2 beta_(p-n-1)
     - (6m^2-8m theta+2theta^2) f_(2m-n)(theta) beta_(4m);

n<0:
 E_n = (20m^2-14m theta+2theta^2) f_(-n)(theta) beta_(p-1)
     + (2m theta-2theta^2) f_(2m)(theta) beta_(p-(2m+n+1)).
```

All reflected `beta` indices lie strictly between `2m` and `p`. Then, for **all ranks `L<=n<=N`**, one has the exact rational identity in `R`

```text
(p-n) Z_n - (p-n-1/2) Z_(n+1) = E_n.                         (4)
```

Proof: specialize the exact bivariate master at `t=s=theta=-p/6`, retaining each of the four finite edge terms. At this value `D_z(r)=r^2` and `A_z(r)=(r+1/6)(r+1/3)`. For one pair `ell-j=n`, the unshifted difference is `j^2-(p-ell)^2=(p-n)(2j-(p-n))`. For shifted pair `ell'-j'=n+1`, the numerator difference is `(p-n-1/2)(2j'-(p-n-1))`. Sum over the *actual finite* ordered domain and restore all dropped endpoint cells, yielding exactly the displayed `E_n`. Divide by `p^2` only after (2) proves the numerator/source divisibility. This is a **direct original coefficient** identity and does not require discarding positive ranks or identifying finite faces with infinity.

### Theorem 3 — exact all-digit fixed-geometric-weight source formula for original Q

Use the actual ordered original cutoff

```text
Q_p = sum_(0<=a,b<p; a+b>=p) (6(a+b)+1) r_a r_b.
```

Define the genuine negative-rank *original* adjoint without any division by `p`:

```text
lambda_0=0;
lambda_(n-1) = ((p-n)lambda_n - 2^n)/(p-n+1/2), n=0,-1,...,L+1;
delta=2^L-(p-L)lambda_L.
```

Each displayed denominator is a `p`-unit. Let

```text
U=sum_(n=L..0) 2^n V_n^0; K=sum_(n=L..0) 2^n V_n^1;
H_beta=sum_(2m<a,b<p; a+b>=p) (6(a+b)+1) 2^(-(a+b)) beta_a beta_b.
```

Then the complete **all-digit original** identity is

```text
Q_p/p^2 =
  2^(1-p) [ U + 12 K
          - 6 sum_(n=L..-1) lambda_n E_n
          - 6 delta Z_L ]
  + p^2 H_beta.                                               (5)
```

Proof: low–low terms never meet `a+b>=p`. Each low–high ordered pair is `a=j<=2m`, `b=p-ell>2m`, `1<=ell<=j`, with a symmetric partner, hence the exact low–high contribution to `Q_p/p^2` is
`2^(1-p) sum_(n=L..0) 2^n(6p+1-6n)V_n^0`.
The elementary relation `(6p+1-6n)V_n^0 = V_n^0+12V_n^1-6Z_n` gives its mass/rank form. Sum (4) against `lambda_n` for `n=L..-1`; direct coefficient comparison telescopes to
`sum_(n=L..0)2^n Z_n=sum_(n=L..-1)lambda_n E_n+delta Z_L`.
The high–high ordered sector has *two* factors `p^2 beta`; after division by `p^2`, its contribution is precisely `p^2 H_beta`. These disjoint populations exhaust `Q_p`. Every equality is exact in `R`, and not just a Taylor congruence.

This direct specialization **resums all Hasse degrees at once** for the declared *fixed diagonal scalar observer*. It does **not** invert the diagonal observer on the six separately labelled Hasse sources; the established authentic signed 3+2+1 information-loss counterexample remains valid. The right/positive ranks in (4) are maintained as a separate source port for future couplings, and no infinity or high–high term has been relabelled a finite face.

### Corollary — original-boundary precision and p=733 gauge-specific resonance

The single leftmost cell is `(j,ell)=(2m,1)`, so `Z_L=-4m f_(2m)(theta) beta_(p-1)` and `Z_L in pR`. For the inherited Hasse endpoint `Y_L^(1,2)=-2m u_(1,2m)u_(2,p-1)`, the exact Taylor divisibilities imply

```text
(Z_L/p) mod p = -Y_L^(1,2)/108 mod p.                         (6)
```

Thus an actual first-Hasse endpoint may be nonzero even while the **original normalized** endpoint appears only at one additional `p`-adic digit. This is a genuine representation/precision relation, not disappearance of a source.

At `p=733`, direct original recurrence and four-origin source checks give
`delta mod 733=0`, `(delta/733) mod 733=288`, `(Z_L/733) mod 733=388`; hence the **original-operator** normalized left-face port is

```text
-6*2^(1-733)*delta*Z_L =
  733^2*231 = 124113759 (mod 733^3), nonzero.                (7)
```

For `p=13`, the same original-operator port is `1404=13*108 (mod 13^3)`, already visible at the second digit. These ports depend on the declared original Green–Ward adjoint gauge; the previously calculated Hasse-truncated p=733 face number `733^2*430` belongs to a different adjoint decomposition, so the individual ports must not be equated. The total normalized original scalar is invariant.

The original high–high sector remains `71459437=733^2*133` modulo `733^3`, distinct from both the finite face and the positive-rank source. The complete directly recomputed equality is

```text
Q_733/733^2 = 99531942
 = 28072505 [low-high] + 71459437 [ordered high-high]
   (mod 733^3).
```

These reproduce known scalar results as **checks**, not newly credited discoveries. The genuinely new result is the exact original-series source identity (4)–(5) valid at **all p-adic precisions**, with separate true boundary/sector provenance, and the precision relation (6).

## Executed evidence and bounded claim

Companion `20261026_hourly_d25_original_parameter_diagonal_source_bridge_r15_check.py` uses **two independently generated** coefficient sequences: corrected `f` with denominator 18 and original `r` with denominator 36. It verifies (4) from the independent four explicit endpoints, source-adjoint telescoping, full original ordered `Q`, low–high/high–high decomposition and left-face precision. **Executed PASS:** 10 rankwise exact rational checks across `p=7,13`; **1957** rankwise exact finite-ring genuine-source identities over 23 primes (`7<=p<=211, p≡1 mod6`, plus `733`) modulo `p^3`, with 23 source-adjoint and 23 full ordered-`Q` checks. Tests are author exact arithmetic, not native CM or independent Driver verification.

BRC **COMPOSE_APPLIED**: ordered low–high versus high–high sector, integer rank/direction, Hasse parameter and its exact diagonal evaluation, four finite face origins, observer `2^n`, p-valuation, and precision-relevant residual are retained. Auxiliary indices are not Enterprise native X6 spatial coordinates; P000 and ACTIVE residual-fidelity premises remain unchanged.

## Honest continuation / owner boundary

The immediately previous valid Source checkpoint stays historical and immutable; no new run is authorized. Current service reports `0.6.11` with `research_authority_granted=false`. Last relevant typed native continuation was blocked by `INVALID_ARGUMENT / CONTROL_QUOTA` (original request `researchhourly-20261026-2021-continuation-r13`, receipt `CONTROL_REQUEST_NOT_FOUND`). Historical original Session `MCP-22fdc1ed9a2d44d8bcf5fd6b5cf810dd` and staging remain protected pending legal transition; no reuse of its private capability or fresh CLAIM/OPEN is inferred. Controller support `awdawmip/enterprise-math#1558`.

Next science: use the source-faithful all-digit *original* operator (4)–(5) together with the established signed 3+2+1 anti-diagonal genuine Hasse equations, the independently oriented positive-rank port and high–high population. Determine whether the actual cross-source `k-1,k-2` constraints annihilate the remaining port in a declared observer class; otherwise derive a labelled exact nonzero residue/counterexample. Mother D25/LIFT/JT2 remains **OPEN**: original-class `H0/B0`, `[X]U mod p²`, Frobenius `eta`, `kappa` and `Delta_p-R_p`, native CM experiment and independent review are still absent. Do not infer theorem admission or native checkpoint from this portable evidence.
