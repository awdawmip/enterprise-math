# PREFIX-865 — Forced coupled decoding at p=17 with eleven-bit full-transition observations

Date: 2026-11-17. Scope: auxiliary fixed odd two-read complete named-source transition observer.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Predecessor: PREFIX-864 (exact widths for p=10..16,18). Status: AUTHOR_PROVED, exact arithmetic, NOT_INDEPENDENTLY_REVIEWED, NOT_ADMITTED.

## Model

Let the state space be `u in [0,2^p)`, with a legal ordered transition `u -> v` either unchanged or a flip of precisely one of the p named binary sources. A fixed observer reads `(u mod q1, v mod q2)` with each `qj` an odd positive integer >=3. Injectivity is required on the COMPLETE ordered legal transition. Peak width <= B means `qj <= 2^B-1`.

## Theorem 865-A: universal no-op least-common-multiple obstruction

For ANY injective observer of the above type (without a shared-factor decoding assumption),
`lcm(q1,q2) >= 2^p`.

Proof. Every `u -> u` is a legal no-op. Their transcripts are `(u mod q1, u mod q2)`. If `lcm(q1,q2) < 2^p`, the two distinct valid no-op transitions `0 -> 0` and `lcm(q1,q2) -> lcm(q1,q2)` have identical transcripts, a contradiction. QED.

Writing `g=gcd(q1,q2)`, since `lcm(q1,q2)=q1*q2/g`, the necessary condition at peak width B is

`g <= floor((2^B-1)^2 / 2^p)`.

This inequality applies to every fixed pair of moduli, not merely the common-GCD CRT subclass.

## Theorem 865-B: p=17, B=11 forces a non-difference-only decoder

Set `p=17` and `B=11`. Then `2^p=131072` and `q1,q2<=2047`. The universal no-op obstruction gives

`g <= floor(2047^2/131072) = floor(4190209/131072) = 31`.

But the set of named one-flip differences is
`E_17={0} union {+/-2^i: 0<=i<17}`,
having 35 DISTINCT integers. Modulo any `g<=31`, at least two of the 35 differences share a residue. Thus `delta=v-u` CANNOT be universally recovered from `(v mod q2)-(u mod q1) modulo gcd(q1,q2)` alone at B=11.

Consequently every hypothetical valid eleven-bit scheme at p=17 must use the two full ordered residues jointly in a way not reducible to a shared-GCD difference label followed by CRT. This structural requirement is proved whether or not a full observer at eleven bits exists.

In particular, every common-GCD CRT construction of PREFIX-861/863/864 needs `g>=2p+1=35` to label all 35 differences separately. The universal upper bound `g<=31` excludes that construction family at eleven bits.

## General arithmetic lower bound for the difference-only CRT subclass

If a decoder is required to identify each member of `E_p` from its residue modulo `g=gcd(q1,q2)` alone and then use CRT to restore the complete transition, then necessarily

`g>=2p+1`, `lcm(q1,q2)>=2^p`, and
`(2^B-1)^2 >= (2p+1) * 2^p`.

Thus within this exact subclass,

`B >= ceil(log2(1+sqrt((2p+1)*2^p)))`.

For p=17 this lower bound is 12. For p=18 the previously verified witness `(q1,q2)=(2405,4033)` has `g=37`, and `lcm=262145=2^18+1`, meeting the information-count lower B=12 for the COMPLETE transition problem.

## Exact arithmetic and reproducibility

All integer comparisons use exact values:
`2047^2=4190209`, `31*131072=4063232`, `32*131072=4194304`; hence `floor(4190209/131072)=31`.
The model and observations are those of PREFIX-864; no new empirical program, random search or native X6 event reclassification is involved.

## Open scientific frontier

The unrestricted `p=17, B=11` fixed-odd observer existence problem remains unresolved. The next discriminating action is to exploit `gcd(q1,q2)<=31` plus the exact old-fiber difference criterion of PREFIX-864 to classify genuinely coupled residue pairs without enumerating complete transition tables naively. A verified pair proves `B_fix,odd(17)=11`; complete exclusion at B=11 establishes 12, for which a constructive witness already exists.

Sources: PREFIX-864 paper at `b8b6e11f65662d769d9efd491a9a64123545d516`, PREFIX-861 at `727d6ca2dee6f707e3dd3cabba600d2c21b12bc8`, and current P000 V5/ACTIVE Heartbeat World. Neither P000 nor protected shared task authority is changed.
