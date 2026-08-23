# Driver Review — Prime Fusion Phase/Fusion Extension Targeted Independent Verification

Status: `DRIVER_ACCEPTED_WITH_SCOPE_NARROWING / TARGETED_VERIFICATION_COMPLETE`
Date: `2026-08-23`
Driver-ID: `EM-DVR-R63A21 / CONTROL_PLANE`
Task: `RS-PRIME-FUSION-PHASE-EXTENSION-TARGETED-INDEPENDENT-VERIFICATION`
Taskbook source: `94f6222675abb38acf8ccfe15c9bc6df83b1f9da`
Owner branch: `research/prime-fusion-phase-extension-targeted-verification`
Frozen return: `research_returns/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_RETURN_20260823.md`
Return blob at review: `501816d4455582cbf5a9601ff9899ed74bb2892f`
Evidence manifest blob at review: `0693ebf4bf1d58513d939f0a4548c0ec61f7b0c3`
Checker evidence blob at review: `f2570534c99a92e75ca55b9ba24286854bc48fff`
Live source main immediately before this review: `3a84d32e3516a0771ba1f07502898d21293900e8`

## 1. Verdict

The targeted statement-exposed independent verification is accepted.

Formal Driver classification:

`PHASE_EXTENSION_VERIFIED_WITH_SCOPE_NARROWING = ACCEPTED`.

The hard target

`PRIME_FUSION_PHASE_EXTENSION_T3_T6_T10_T11_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED`

is achieved.

Evidence strength:

- statement-exposed independent proof checking, not blind discovery;
- source proofs/checker/narrative remained withheld before return freeze;
- independently authored exact-integer checker returned `PASS`;
- one theorem-critical scope repair was found in V10;
- no material counterexample to the corrected phase/fusion extension was found.

## 2. Identity / execution provenance

The return and manifest use runtime Researcher-ID:

`EM-PFVEXT-B47C27`.

This differs from the previously prepared manual relay ID `EM-PFEXT-94F622`.

The manifest shows that the actual execution read the taskbook/router packet directly and did not read the manual dispatch envelope. Under the active taskbook identity policy `AUTO_RESOLVE_OR_ALLOCATE`, taskbook-direct execution may resolve/allocate its own runtime identity. Therefore this is recorded as an alternate legitimate execution identity, not as mathematical-evidence contamination.

The mathematical firewall is accepted as intact at the stated strength.

## 3. V3 — accepted exactly with convention

Accepted theorem:

`Z[X]/((X^2+1)(X^2+X+1)) ~= Z[i] x Z[omega]`

with `omega=[X]` satisfying

`omega^2+omega+1=0`.

The integral Bezout identity

`(X+1)(X^2+1)-X(X^2+X+1)=1`

establishes comaximality over `Z[X]`.

The discriminant is exactly

`Disc(F)=12`.

For `xi=(i,omega)`, component norms of `a+b xi` are

`a^2+b^2`

and

`a^2-ab+b^2`.

The only wording convention that must remain explicit is that `omega` is the primitive cube root satisfying `X^2+X+1`, not a sixth-root sign convention.

Driver classification:

`T3 = INDEPENDENTLY_VERIFIED_EXACTLY_WITH_CONVENTION`.

## 4. V6 — accepted and strengthened

The verifier independently proved that the unit hypothesis is redundant:

for any modular root `F(r)=0`, the root is automatically a unit.

With

`T=r+r^{-1}`

and

`e=-T`,

the Laurent identity gives

`T^2+T=0`, hence

`e^2=e`.

For arbitrary `H>=2`, every root of `F mod H` therefore induces a full prime-power factor split

`A=gcd(e,H)`,

`B=gcd(e-1,H)`,

with

`gcd(A,B)=1`, `AB=H`.

For the pointed primitive cell this specializes exactly to

`A=N`, `B=C`.

Driver classification:

`T6 = INDEPENDENTLY_VERIFIED_AND_STRENGTHENED`.

## 5. V10 — accepted only after scope narrowing

The local order statements are accepted:

`ord_p(r)=4`, `ord_q(r)=3`, hence `ord_H(r)=12`

under the stated dual-prime hypotheses.

The crucial scope correction is:

The set

`{r,r^5,r^7,r^11}`

is exactly the **channel-oriented mixed locus**

`M_{p,q}={x mod pq : f(x)=0 mod p and g(x)=0 mod q}`,

and forms the free `U(12)=(Z/12Z)^x` orbit of the pointed phase.

It is not, in general, the complete root set of

`F(X)=(X^2+1)(X^2+X+1)`

modulo `pq`.

Explicit exact counterexample to the overbroad full-root reading:

`(a,b)=(2,3)`, `(p,q,H,r)=(13,7,91,60)`.

Here the oriented mixed locus has four roots

`{18,44,60,86}`

but the full fused polynomial has eight roots

`{9,16,18,44,60,74,81,86}`.

The four extra roots arise from other local factor choices.

The shared-coefficient coordinate-swap pair is still exactly

`{r,r^11}={r,r^{-1}}`,

while `{r^5,r^7}` is the other inversion pair inside the oriented mixed locus.

Therefore the package may retain the phase-coset theorem only after explicitly defining/fixing the channel-oriented mixed locus. If the current T10 wording can reasonably be read as claiming all roots of `F mod H`, it must be repaired before package acceptance.

Driver classification:

`T10 = INDEPENDENTLY_VERIFIED_WITH_MANDATORY_SCOPE_NARROWING`.

## 6. V11 — accepted exactly under dual-prime hypotheses and strengthened beyond them

For every oriented mixed root satisfying

`x^2=-1 mod A`

and

`x^2+x+1=0 mod B`,

one has directly

`x^6=-1 mod A`,

`x^6=+1 mod B`.

Thus V11 does not require the full V10 orbit theorem.

For coprime channels the exact general gcd formulas are

`gcd(AB,x^6+1)=A*gcd(B,2)`,

`gcd(AB,x^6-1)=B*gcd(A,2)`.

Under the original dual-prime hypotheses `p,q>3`, both channels are odd and the source formulas are exact:

`p=gcd(H,x^6+1)`,

`q=gcd(H,x^6-1)`.

Driver classification:

`T11 = INDEPENDENTLY_VERIFIED_EXACTLY_AT_SOURCE_SCOPE / STRENGTHENED_COMPOSITE_PARITY_FORM_AVAILABLE`.

## 7. Dependency correction

The independent verification materially improves the package dependency graph.

Accepted dependency facts:

- T6 does not logically require the product-ring interpretation T3; the polynomial/Laurent identity suffices.
- T10 does not logically require T3; local root orders plus CRT suffice.
- T11 does not require T10 orbit completeness and does not require primality for the local sixth-power law.
- V6 idempotent and V11 sixth-power readout satisfy, on the oriented locus,
  `x^6=2e-1 mod H`.
- for odd `H`, the V6 and V11 channel-split readouts are equivalent because `2` is invertible.

Therefore the late phase/fusion layer should not be documented as one strictly linear proof chain.

## 8. Executable evidence

Independent checker:

`experiments/prime_fusion_phase_extension_targeted_verification_checker.py`.

Recorded SHA-256:

`f1dc858eaf76f1ee215562e242172b1d6a88095238c08c8182395bceb45a9d70`.

Evidence JSON:

`research_output/evidence/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_CHECK_20260823.json`.

Recorded result:

`final_status=PASS`.

Audited ranges include:

- exact symbolic Bezout/resultant/discriminant/Laurent identities;
- every root of `F mod H` for `2<=H<=400`;
- 3,931 ordered primitive cells with `1<=a,b<=80`;
- 318 ordered dual-prime cells;
- 3,610 ordered composite cells satisfying retained order-12 hypotheses;
- exhaustive full-root enumeration for 21 unordered cells with `H<=5000`;
- explicit V10 extra-root and V11 parity controls.

Finite checks are audit evidence; theorem acceptance rests on the written exact proofs.

## 9. Package-level evidence state after this return

Relative to the previous Driver comparison, the four previously source-only/missed claims are now classified:

- T3: exact independent verification;
- T6: exact independent verification, strengthened;
- T10: independent verification only after mandatory scope narrowing;
- T11: exact independent verification at source dual-prime scope, strengthened beyond it.

This closes the previously missing phase/fusion cluster.

However, the previous blind comparison had only substantial partial convergence for T4/T7/T8. This targeted task did not explicitly re-run those three source statements as standalone verification targets.

Therefore the correct package-level statement is:

`PHASE_EXTENSION_TARGETED_GAP = CLOSED_WITH_T10_SCOPE_REPAIR`.

but not yet automatically:

`ALL_15_THEOREMS_INDEPENDENTLY_VERIFIED_AT_EXACT_SOURCE_STATEMENT_STRENGTH`.

A future Driver may either:

1. perform one final narrow compositional/exact verification of T4/T7/T8; or
2. retain the current evidence-typed matrix and treat T4/T7/T8 as partially independently reconstructed but mathematically supported by the package proof/review.

No automatic successor is created by this review.

## 10. PR #597 disposition

PR #597 remains Draft / not canonical.

Before any package-level acceptance, T10 wording should explicitly define the channel-oriented mixed locus or otherwise exclude the overbroad interpretation that all `F mod pq` roots are the four powers.

The V6/V11 strengthening may be incorporated as optional theorem notes, but is not required to preserve the original source-scope conclusions.

No source theorem package mutation is performed by this Driver review.
