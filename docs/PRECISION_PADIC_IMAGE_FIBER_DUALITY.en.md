# p-adic Precision Duality: Hidden FIBER Spectrum and IMAGE Solvability Height

Status: `RESEARCH BRIDGE / NONCANONICAL`

Prime-power observation precision exposes a useful duality between the two ends of the affine exact sequence.

## 1. FIBER side: kernel-growth spectrum

For integer observation map O with hidden free rank h and nonzero Smith factors d_i, write

`a_i=v_p(d_i)`

and

`kappa_e=log_p |ker(O mod p^e)|`.

Then

`kappa_e=e*h + sum_i min(e,a_i)`.

The discrete slope is

`s_e=kappa_e-kappa_(e-1)=h + #{i:a_i>=e}`,

so

`s_e-s_(e+1)=#{i:a_i=e}`.

The complete infinite precision-growth curve reconstructs the free hidden rank and every positive p-primary Smith-depth multiplicity.

But a finite ladder through exponent E cannot distinguish a genuine free hidden direction from finite p^K torsion with K>=E.  The two models can have identical kernel-growth curves throughout the observed precision range.

## 2. IMAGE side: target p-divisibility height

For affine target equation

`A x=b`,

define

`eta_p(b)=sup {e>=0 : A x == b (mod p^e) is solvable}`.

This is the p-divisibility height of the target class `[b]` in `coker A`.

- exact reachable target: `eta_p=infinity` for every p;
- finite p-primary image obstruction: finite eta_p;
- prime-to-p finite torsion can have `eta_p=infinity` for that prime even though the target is not exactly reachable;
- a free cokernel component has finite eta_p for every fixed p.

The finite solvability ladder is a true-prefix/false-suffix sequence.  If no failure is seen through exponent E, the observation only proves

`eta_p>=E`.

It does not prove `eta_p=infinity`.

## 3. Sharp IMAGE finite-depth mimic

Fix prime p and depth K.  Use the same scalar map

`A=p^(K+1)`

with targets

`b_good=p^(K+1)`,

`b_bad=p^(K+1)+p^K`.

The first target is exactly reachable; the second is not.  Yet the two equation data are identical modulo every `p^e` with `e<=K`, so their modular solution sets are identical throughout that finite precision ladder.  They separate at exponent K+1.

## 4. Dual finite-precision no-go

The two sides now have parallel impossibility statements.

### FIBER no-go

A finite p-adic observation ladder cannot certify that a persistent hidden direction is genuinely free rather than finite torsion deeper than the tested precision.

### IMAGE no-go

A finite p-adic solvability ladder cannot certify that a persistently solvable target is exactly reachable rather than blocked by a deeper image obstruction.

The stronger finite-modulus versions also hold: any finite modular experiment family has one lcm precision ceiling, and exact integer lifts beyond that ceiling can disagree in free/torsion structure or exact target reachability while matching every declared modular test.

## 5. What makes a finite experiment decisive?

Finite modular/p-adic evidence becomes decisive only after adding some independent bound or stronger language.

Examples of sufficient extra information include:

- a proven upper bound on every relevant Smith valuation / torsion depth;
- a proven upper bound on target-class p-divisibility depth;
- exact integer access;
- a new modulus/refinement known to exceed the remaining obstruction depth.

If a valid p-primary depth bound K is known, precision level `p^(K+1)` is enough to rule out every deeper finite mimic on that axis.

Without such a bound, “no failure observed yet” is a lower bound on required precision, not evidence of infinity or exactness.

## 6. Precision-world interpretation

This is an integer identifiability statement, not a metaphysical claim that hidden variables or obstructions are physically real.

It says only:

> **At finite observation precision, an exact world property and a deeper finite approximation can be operationally identical.  Claims of exact reachability or genuinely unbounded hidden structure require either stronger precision or an independent depth bound.**

Smith normal form, p-adic valuation, cokernel divisibility and congruence are standard prior mathematics.  The project value is the dual IMAGE/FIBER precision architecture.