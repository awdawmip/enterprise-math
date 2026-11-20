# D25/LIFT: finite Cauchy binomial first-jet and signed overflow-tail certificate (author-only)

2026-10-27. **AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**.
Portable evidence only; NOT a Source task result, CLAIM, authorized OPEN, original H0/B0 run, or independent review.
Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; TP2-B6F4FC938FF94941C1B7. Preserve frozen source `c47e13e4aba0e006366f989d6334d443f6333ae3` and taskbook blob `53a3ef039325534e3715add837f0eee332289984`.

## Theorem: an exact first-order observer transport

Reuse the **inherited** finite Cauchy identity from this PR, not a new authorship claim:
`c[k]=(3k)!(2k)!/(216^k (k!)^5)`, `u[j]=binom(2j,j)/8^j`,
`W[p]=sum_{k<p}(6k+1)c[k]`, `S[p]=sum_{j+k<p}(3(j+k)-1)u[j]c[k]`.
All sums have their **finite** source-label and cutoff as shown.

For EVERY prime p>=5, put m=(p-1)/2, a=floor((p-1)/3), chi=(2/p) in {+1,-1}. Work in Z_(p) or F_p as indicated, with theta=z*d/dz. Define
- `P(z)=(1-z/2)^m`, `C(z)=sum_{k<p}c[k]z^k`;
- `C0(z)=sum_{k=0}^a (c[k] mod p) z^k` in F_p[z];
- `L(z)=sum_{r=1}^{p-1}z^r/(r*2^r)` in F_p[z];
- `B(z)=P(z) C0(z) L(z)` in F_p[z];
- `T[p] = (1/2)sum_{n>=p} (3n-1)*[z^n]B(z) mod p`, an actual finite signed HIGH-DEGREE Cauchy tail.

Then

```text
S[p] = (chi/2)*W[p] - p*((3chi/2)*C(1)+T[p])   (mod p^2).       (1)
2*S[p] = chi*W[p]                                (mod p).         (2)
```

**Proof (exact coefficient and valuation accounting).** The formal-power-series identity
`sum_{j>=0}u[j]z^j=(1-z/2)^(-1/2)=P(z)*(1-z/2)^(-p/2)`
implies, coefficientwise in degrees <p,
`sum_{j<p}u[j]z^j = P(z)+(p/2)*P(z)*L(z) (mod p^2,z^p)`.
The `p`-division is legal in Z_(p): j<=m follows by comparing
`(1/2)_j=(-m+p/2)_j` to `(-m)_j`; m<j<p has
`v_p(binom(2j,j))=1`. Thus the finite binomial first jet
`D(z)=(sum_{j<p}u[j]z^j-P(z))/p` satisfies
`D=(1/2)P*L (mod p,z^p)`. The logarithmic expansion is formal and
uses only inverse indices r<p.

For 0<=k<p, `v_p(c[k])=floor(3k/p)+floor(2k/p)`, so `v_p(c[k])>=2`
for k>m. Every coefficient of P*C of degree >=p must use such k;
dropping it is justified modulo p^2, NOT modulo p^3.
Applying the signed observer (3theta-1) to the degree-<p product:
`S[p] = (3theta-1)(P*C)|_{z=1} + p Q[p] (mod p^2)`,
where `Q[p]=(1/2)*[(3theta-1)(B mod z^p)]_{z=1} mod p`.
Because P(1)=2^(-m), P'(1)=-m*2^(-m),
`(3theta-1)(P*C)(1)=rho*(W[p]-3p*C(1))` EXACTLY,
where `rho=2^(-m-1)`.

Let `q=(2^(p-1)-1)/p` (Fermat quotient). Finite-binomial expansion
at z=1 gives `L(1)=q mod p`, while
`L'(1)=sum_{r=1}^{p-1}2^(-r)=0 mod p`.
Euler's criterion and `(2^m)^2=1+pq` yield
`rho=chi/2 - p*chi*q/4 (mod p^2)`.
The product rule yields the **full**, untruncated jet observer
`(1/2)(3theta-1)(P*C0*L)|_{z=1}=chi*q*W[p]/4 (mod p)`.
Subtracting exactly the high-degree signed tail T[p] gives
`Q[p]=chi*q*W[p]/4-T[p] (mod p)`.
The two Fermat-quotient terms cancel in S[p], leaving exactly (1).
No p-adic conjecture, sampling or asymptotic argument is used. QED.

## Remaining exact target-class obstruction

For p=13 or 19 (mod 24), chi=-1. If the separately sourced original
first-digit result `W[p]=p (mod p^2)` is valid for that prime, (1)
says `S[p]=W[p] (mod p^2)` **if and only if**

```text
(3/2)*C(1) - T[p] = 3/2    (mod p).                            (3)
```

The split `C(1)=0`, `T[p]=-3/2` (mod p) is SUFFICIENT, not necessary.
Neither this split nor (3) has been proved for every target prime here.
(3) is a narrower exact finite-field research obligation; it is not
a proof of Sun's conjecture or the third-digit LIFT.

## Actual author checks and provenance boundaries

Executed standard-library **exact integer** checker:
`d25_cauchy_first_order_binomial_jet_checker_20261027.py`.
237 primes 5<=p<1500, of which 60 p=13 or 19 mod24: (1) and the
binomial low/high factorial-harmonic jet all PASS.
Independent signed tail route PASS for 78 primes (all primes <=400
plus 997 and 1213). For the 23 target primes in that tail run the
two sufficient split residues held; all 60 target primes displayed
S-W=0 (mod p^2). Finite evidence, NOT universal proof. Examples:
(p,C(1) mod p,T mod p) = (13,0,5),(19,0,8),(373,0,185),(7,4,6).
The independent local program SHA256 is
`e35c60530ed3a33251f69b06368b3596254c01b3759c20c3cb6d0e7a80738dde`;
author-check JSON SHA256 is
`fde79164397848da94ce25a6a271dd55e2a330ad3823addf3ab08a4b0e839ca3`.
The complete local proof SHA256 is
`a910e3fdeaded186dce1a874c3f50d03557ed3fb8a2c064edd3d6bb055090205`.
These hashes label author inputs, not trusted Source receipt/signatures.

BRC/Enterprise-coordinate typing: source carrier is signed indexed
pairs (j,k), observer precision p^2, allowed operation finite Cauchy
convolution and first binomial jet. The lawful compression erases no
relevant sign or high-degree contribution: T[p] is explicitly retained.
This is external hypergeometric auxiliary mathematics, not an
established map to P000's X6/three-dimensional slice.

Literature: Roman Le Lan, *Series for 1/pi arising from Cauchy product*
(arXiv:2604.03327, 2026-04), supports the INHERITED analytic Cauchy
representation, not this new finite first-jet lemma or a proved Sun
mod-p² conjecture. https://arxiv.org/abs/2604.03327

## Recovery and next action

Exact Source continuation read returned CONTROL_QUOTA; earlier
control-result lookup CONTROL_REQUEST_NOT_FOUND and own checkpoint
list ACCESS_DENIED. Sites: static_machine_readonly /
write_relay_enabled=false. No current winning CLAIM, authorized OPEN,
Source checkpoint, independent Result review or predecessor completed
research was established. If an eventual Source seed is
CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS, complete its
input-artifact readback and set frontier_notes.completed_units=[].
This author-only note stays staged/unreviewed, not predecessor completed.

Original H0/B0 same-class p=373 benchmark is PENDING_OWNER /
NATIVE_NOT_EXECUTED at #1559. Original UR V2 bundle still lacks
simultaneous independent proof of 94687 bytes and SHA256
4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76.
Do not reprove UR; do not transport this auxiliary certificate as
native H0/B0 evidence. Next scientific unit is an all-target proof
or exact counterexample to (3), or authentic original-class transfer.
Next native action is exact own-session continuation/receipt
reconciliation under real current authority, then only the lawful
writer/provenance/checkpoint route. No new scheduler/Actions.
