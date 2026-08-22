# CBRC F1 Non-Sign Recoalescence Carrier — Driver Review

Status: `ACCEPTED_WITH_SCOPE_NARROWING`
Date: `2026-08-22`
Driver-ID: `EM-DVR-CBRC-F0-7C3A21`
Task-ID: `RS-CBRC-F1-NONSIGN-RECOALESCENCE-CARRIER-FORWARD-CLASSIFICATION`
Taskbook source: `e279377a6578ac9adb93c2c21d52b31c569bae20`
Accepted owner branch: `research/cbrc-f1-nonsign-recoalescence-carrier-forward-classification`
Accepted owner head: `417b8ef08ce6e20596c84e8f15e77bc55c124c37`
Researcher-ID: `EM-CBRCF1-8D27A4`

## 0. Driver verdict

`F1_UNIQUE_MINIMAL_NONSIGN_CARRIER` is **accepted only under the declared F1 rank-primary complexity order**.

The accepted hard target is:

`NONSIGN_RECOALESCENCE_MINIMAL_CARRIER_CLASSIFIED = true`.

This acceptance does **not** mean that the returned carrier is an observable wave/amplitude carrier, a phase algebra, a probability model, or a Foundation object.

The correct scope is:

> F1 has classified the least conservative finitely generated additive enrichment that supports a finite elementary transport orbit strictly larger than the F0 sign orbit, while preserving the old signed layer, path typing, composition, and reversal choice independence.

## 1. Accepted mathematical core

### 1.1 F0 rank-one replay

The old signed scalar carrier is `Z e` and its additive automorphisms are exactly `±id`. Therefore the F0 carrier itself cannot support an elementary reversible orbit containing more than the two sign states.

PASS.

### 1.2 Torsion is admissible under the issued F1

The F1 taskbook explicitly required any formally smaller torsion construction to be tested against conservative embedding and refinement consistency and then either admitted or killed.

The return constructs the split extension

`C_min = Z e ⊕ <tau | 3 tau = 0>`

with retraction

`pi(ne + a tau) = ne`.

The transport

`R(e)=e+tau`,
`R(tau)=tau`

satisfies

`pi R = pi`,
`R^3 = id`,

and preserves the embedded signed subgroup and exact additive inverses.

The new torsion relation does not impose a new relation on `e`.

PASS.

### 1.3 Minimality and uniqueness

Under the declared complexity order, first minimizing torsion-free rank and then new generators/relations, finite-kernel size, elementary orbit size, and optional multiplication burden:

- rank `0` is impossible because the old `Z` must embed;
- rank `1` without a new generator is the F0 no-go;
- a same-rank finite kernel of size `2` cannot give an elementary orbit larger than `2`;
- kernel size `3` is attainable with one generator and one relation;
- the two raw shifts `+tau` and `-tau` are conjugate under the unique reversal fixing `e`.

Therefore the least carrier/transport class is unique under this order.

PASS WITH SCOPE NOTE:

There is an infinite same-torsion-free-rank family `Z e ⊕ Z/m` for `m>=3`. Hence the result is **not** “rank-one uniqueness”; it is uniqueness of the least element under the full declared order.

### 1.4 Exact transport relations

For `N=R-id`, the return derives

`N^2=0`,
`3N=0`,
`R^3=id`.

The non-sign information disappears after rationalization, so it must not be silently reinterpreted as a torsion-free quadratic carrier.

PASS.

### 1.5 Sign layer remains independent

The old sign involution `J=-id` is central and is not a power of `R`, because every power of `R` acts trivially on the free quotient while `J` acts by `-1`.

Thus F1 extends rather than replaces F0 sign cancellation.

PASS.

### 1.6 Reversal / choice independence

The unique additive automorphism fixing `e` and sending the raw transport to its inverse is

`S(e)=e`,
`S(tau)=-tau`,

with

`S R S^-1 = R^-1`.

Hence the two raw orientation presentations form one unoriented transport class.

PASS.

### 1.7 Path composition

The local transport extends by composition of powers of the already-derived `R`. Edge transport is sufficient; elementary diamond ratios are presentation/gauge invariant; the existing typed Path-formal provenance remains necessary until recoalescence.

Checker evidence covers composition through depth `4` and all `3^4=81` elementary edge-exponent assignments around one diamond with zero mismatches.

PASS.

### 1.8 Internal multiplication is not intrinsic

Path concatenation needs only an action by additive automorphisms. No multiplication of arbitrary coefficient states is forced.

If one nevertheless imposes an associative bilinear product extending `e*e=e` and requires `R` to be multiplicative, exactly two reversal-paired directed nonunital products survive and no two-sided-unital survivor exists.

PASS AT F1 SCOPE.

### 1.9 Torsion-free counterfactual

If a new torsion-free axiom is added, minimum free rank becomes `2`. For primitive orbit-generated rank-two finite-order integral transport, the surviving characteristic polynomials are

`x^2+x+1`,
`x^2+1`,
`x^2-x+1`,

with orders `3,4,6`.

This is accepted only as a counterfactual control. It is not the primary F1 answer.

## 2. Target-leak / blindness review

The source audit records only the frozen native inputs plus the explicitly authorized F0 boundary. It reports no R063/R064/R065 mathematics, downstream coherent/wave free-research result, or external quantum/wave formalism before freeze.

No prechosen ring, phase group, complex structure, positive form, readout exponent, or physical law was used as a selector.

`TARGET_LEAK_AUDIT_PASS = accepted`.

## 3. Checker / packet integrity

Accepted checker digest:

`d3e570e05b76fc4f6d3269ac5fd58f9f833ce537f9121403b09f9c7fad132080`.

Reported mismatch count:

`0`.

The owner branch is `7` commits ahead of the F1 issue commit and `0` behind it. The branch changes only the required F1 reports/checker/manifest surface; it does not modify current native definitions.

Remote frozen head is:

`417b8ef08ce6e20596c84e8f15e77bc55c124c37`.

The manifest does not independently prove the researcher's local working tree was clean at freeze. This is recorded as a minor delivery-evidence gap, not a mathematical rework trigger; the accepted object is the remote frozen packet at the SHA above.

## 4. Scope narrowing — load-bearing

The following claims are **not accepted** as consequences of F1:

1. `C_min` is not yet an observable coherence/amplitude carrier.
2. The three states in the elementary `R`-orbit are not yet physical intensity/phase levels.
3. No scalar readout distinguishes the torsion sheet in F1.
4. `pi(e)=pi(e+tau)=pi(e-tau)=e`; therefore the accepted F0 forgetting map makes the entire new orbit invisible.
5. No square/Born law, norm, inner product, continuum wave equation, or interference profile has been selected.
6. No Foundation promotion is authorized.
7. The phrase “torsion-free rank = 1” means the rank of the free quotient is one; the accepted carrier itself contains order-three torsion and must not be described as a torsion-free carrier.

Therefore F1 is best interpreted as:

`MINIMAL_HIDDEN_NONSIGN_TRANSPORT_LAYER_CLASSIFIED`.

Whether this layer can become operationally visible at native recoalescence is a separate question.

## 5. Why F2 is required

The next forward question is not “which familiar phase algebra matches the F1 result?”

The next question is:

> Can a non-sign transport class affect the scalar result of the smallest native same-terminal recoalescence while individual path alternatives remain locally indistinguishable in scalar weight, common transport remains unobservable, and all F0 typing/refinement constraints remain intact?

This is an observability question, not a downstream matching question.

F2 must first test the accepted F1 torsion minimum. If it is observationally silent under the required invariances, F2 must classify the least enlargement that is not silent. If it is observable, F2 must classify the full allowed readout family and identify exactly which extra axiom, if any, would be required for uniqueness.

No target readout exponent or known wave formalism may be preloaded.

## 6. Driver disposition

`F1_ACCEPTED_WITH_SCOPE_NARROWING = true`.

`F1_FOUNDATION_PROMOTION = false`.

`F1_DOWNSTREAM_MATCHING_AUTHORIZED = false`.

`F2_OBSERVABILITY_STAGE_AUTHORIZED = true`.

Driver note:

`FIRST CLASSIFY WHETHER THE NONSIGN SHEET IS OBSERVABLE; DO NOT NAME WHAT YOU EXPECT TO SEE.`
