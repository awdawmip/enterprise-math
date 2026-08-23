# Prime Fusion — Phase/Fusion Extension Targeted Verification Packet

Status: `TARGETED STATEMENT PACKET / SOURCE PROOFS WITHHELD / NOT A THEOREM VERDICT`
Date: `2026-08-23`
Scope: one native sector, primitive positive interior cells

## 0. Evidence boundary

This packet exposes four exact target statements for independent proof checking. It does **not** expose the source derivations, source checker, or source research narrative.

The verification is therefore statement-exposed independent verification, not blind discovery.

The verifier may use the already independently reconstructed core facts listed below, elementary algebra/number theory, and a newly authored exact-integer checker. The verifier must actively search for counterexamples and may weaken or reject any target statement.

## 1. Core prerequisites already independently reconstructed

For positive integers `a,b`, define

`N=a^2+b^2`,

`C=a^2-ab+b^2`.

For primitive cells `gcd(a,b)=1`, the channels are coprime:

`gcd(N,C)=1`.

Put

`H=NC`.

Use the sign convention

`r == -a*b^{-1} (mod H)`.

Then `b` is invertible modulo `H`, and the independently reconstructed channel-recovery identities are

`N=gcd(H,r^2+1)`,

`C=gcd(H,r^2+r+1)`.

For dual-prime cells with `N=p>3` and `C=q>3`, the independently reconstructed congruence lock is

`(p mod 8, q mod 12) in {(1,1),(5,7)}`.

These facts may be used as premises. Do not re-prove the entire core route unless needed to audit a dependency.

## 2. Target V3 — product fusion algebra and discriminant

Let

`f=X^2+1`,

`g=X^2+X+1`,

`F=fg`.

Verify or refute the following statement at exact ring-theoretic strength:

1. `f` and `g` are comaximal in `Z[X]`;
2. therefore
   `R=Z[X]/(F) ~= Z[i] x Z[omega]`,
   where `omega` is a primitive cube root of unity satisfying `omega^2+omega+1=0`;
3. `Disc(F)=12`;
4. for `xi=(i,omega)`, the two component norms of `a+b*xi` are exactly `N` and `C`.

If any item requires a convention or qualification, state it precisely.

## 3. Target V6 — reciprocal-trace idempotent collapse

Assume `r` is a unit modulo `H` and

`F(r)==0 (mod H)`.

Let

`T=r+r^{-1} (mod H)`

and

`e=-(r+r^{-1}) (mod H)`.

Verify or refute:

1. the Laurent identity
   `F(r)/r^2 = T^2+T`
   in the appropriate algebraic sense;
2. hence `e^2=e (mod H)`;
3. for a primitive cell with the pointed residue above,
   `N=gcd(e,H)` and `C=gcd(e-1,H)`.

Check all unit hypotheses and small/degenerate cases explicitly.

## 4. Target V10 — four mixed phases and the order-12 orbit

Assume a dual-prime cell with

`p=N>3`, `q=C>3`, `H=pq`,

and pointed residue `r=-a*b^{-1} mod H`.

Verify or refute the following:

1. `ord_p(r)=4` and `ord_q(r)=3`, hence `ord_H(r)=12`;
2. the simultaneous mixed roots of `F(X)==0 mod H` form exactly
   `{r,r^5,r^7,r^11}``;
3. these four roots are the orbit under
   `(Z/12Z)^x={1,5,7,11}`;
4. the shared-coefficient coordinate-swap pair is exactly
   `{r,r^11}={r,r^{-1}}`;
5. the other pair `{r^5,r^7}` consists of algebraically valid mixed roots but is not the same shared-coefficient swap pair;
6. consequently the shared-coefficient phase is a coset bit in
   `(Z/12Z)^x/{+/-1} ~= C2`.

The word “exactly” in items 2 and 4 must be justified, not inferred from examples.

## 5. Target V11 — sixth-power phase-blind channel readout

Under the hypotheses of V10, verify or refute:

`r^6==-1 (mod p)`,

`r^6==+1 (mod q)`.

Then determine whether all four mixed phases have the same sixth power modulo `H`, and whether the exact channel recovery formulas

`p=gcd(H,r^6+1)`,

`q=gcd(H,r^6-1)`

hold without hidden qualifications.

Classify precisely what information the sixth-power readout retains and what phase information it loses.

## 6. Dependency audit

Do not treat V3, V6, V10 and V11 as independent slogans. Determine the actual implication/dependency graph.

At minimum answer:

- Does V6 logically require the product-ring interpretation V3, or only the polynomial identity for `F`?
- Does V10 require V3, or can it be proved directly from CRT and local root orders?
- Does V11 require the full V10 orbit theorem, or only the local orders 4 and 3?
- Which claims survive for primitive composite channels rather than dual-prime channels?

Preserve any stronger theorem discovered during this dependency audit.

## 7. Counterexample and scope pressure

Test at least:

- the primitive cell `(1,1)` and other small degeneracies;
- primitive cells with composite `N` or `C`;
- dual-prime cells with the smallest allowed primes;
- coordinate swap;
- arbitrary unit roots of `F mod H` that do not arise from one shared coefficient pair;
- squarefree versus nonsquarefree `H` where relevant.

A counterexample to an overbroad wording is a successful verification outcome if the exact corrected statement is identified.

## 8. Executable evidence

Write an independently authored exact-integer checker for the statements actually retained. It should enumerate nontrivial primitive and dual-prime ranges, enumerate all roots of `F mod H` on manageable examples, and test the phase/orbit/channel-recovery claims.

Finite computation is audit evidence only; proofs or exact counterexamples remain primary.

## 9. Required return

Freeze a return containing:

1. exact source/read list;
2. V3/V6/V10/V11 verdict table;
3. independent proofs or counterexamples;
4. corrected theorem statements where needed;
5. dependency graph;
6. checker path, ranges and actual result;
7. any stronger independent theorem;
8. final classification chosen from:
   - `PHASE_EXTENSION_FULLY_VERIFIED`,
   - `PHASE_EXTENSION_VERIFIED_WITH_SCOPE_NARROWING`,
   - `PHASE_EXTENSION_PARTIALLY_VERIFIED`,
   - `PHASE_EXTENSION_MATERIAL_COUNTEREXAMPLE`.

Do not use source proofs or source checker as evidence before the return is frozen.
