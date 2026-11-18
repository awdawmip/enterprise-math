# S23 mother ↔ AV auxiliary: exact observer bridge, cubic nonfactorization, finite-bank bound

Date: 2026-11-07. Author-side derivation, not independent mathematical admission.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor full-27 auxiliary theorem: PR #1777@ce7762b32d79402781d2391a767b6edd3e13a3ed.

## Frozen mother protocol and exact one-sample positive bridge

The mother S23 model has six statistical sources (AU0,AU1,AV,BU0,BU1,BV), six mixed preparations, four stopped-time outputs, row-stochastic M=M20/20 and eleven causal policy controls in [0,1]^11. M20 row index 2 is (0,0,20,0,0,0): the third preparation is **pure source AV**, without source-mixing error.

For source AV the four-time law, in order T1,T2,T3,T4, is

\[
F_{AV}=(a_A,(1-a_A)b_{AV},(1-a_A)(1-b_{AV})c_{AV},(1-a_A)(1-b_{AV})(1-c_{AV})).
\]

On the lawful face b_AV=0 let a=a_A, c=c_AV, z=(1-a)c and b=(1-a)(1-c). The third prepared law is exactly p3=(a,0,z,b). On a,c in [1/2,7/8] this is the predecessor's conditional AV auxiliary ternary law.

Two parameter-independent deterministic observers of the stopped time are:

C(T1,T2,T3,T4)=(0,0,1,2), giving p3 C=(a,z,b);
B(T1,T2,T3,T4)=(0,0,1,0), giving p3 B=Bernoulli(z), where success means T3.

The T2 assignment is irrelevant on this face. Thus **one auxiliary ternary trial and its binary coarsening factor exactly through one lawful mother stopped-time outcome**. When an expressly NEW experiment consists of three conditionally independent repeated AV preparations with one shared policy (a,c), tensor observers C⊗3 and B⊗3 yield exactly the 27-output ternary target and eight-input binary experiment used by the previous auxiliary δ3 theorem. Product independence is an additional sampling operation, not a law inferred from one mother stop-time observation.

## Theorem 1: single stop-time cannot simulate three independent binary trials by fixed Markov decoding

There exists NO parameter-independent stochastic H from a *single* mother T∈{T1,T2,T3,T4} to three ordered binary words such that p3(a,0,c)H = Bernoulli(z)⊗3 for **all** a,c in [1/2,7/8].

Proof: Fix a=1/2. Each input time mass is affine in c: (1/2,0,c/2,(1-c)/2). Consequently the H-produced probability of the event 111 is affine in c for every fixed H. The demanded event probability is z³=(c/2)³ with a nonzero cubic coefficient. A fixed Markov kernel, including any finite composition of fixed encoders/postprocessors, cannot satisfy the equality throughout the interval. QED.

Four-policy exact quantitative witness: at a=1/2, choose c=(1/2,5/8,3/4,7/8). This yields z=(1/4,5/16,3/8,7/16), with uniform step h=1/16. The third forward difference of z³ is 6h³=3/2048, while any postprocessed event probability from one stop time has vanishing third difference. If TV error of a fixed H at all four policies is at most ε, event-111 errors are bounded by ε. The absolute-coefficient sum of the third difference is 1+3+3+1=8, so

\[
\boxed{\max_{\text{four policies}}TV(p_3H,Bern(z)^{\otimes3})\ge 3/16384}.
\]

Even a finite bank of m fixed postprocessors H_l selected by an arbitrary policy-dependent label cannot provide an **exact** reproduction for every c in [1/2,7/8]: each polynomial equation (c/2)³−P_{H_l}(111)=0 is a nonzero cubic and holds at at most three c values, so finitely many such equations cannot cover the continuum. This remains an exact nonfactorization statement even if label selection is discontinuous.

## Theorem 2: lawful finite-bank mother lower bound from the AV time-3 event

Fix any finite source-state count k, any θ-independent stochastic encoder E, and any bank of m>=1 fixed θ-independent stochastic decoders D_l. The mother S23 protocol selects l after policy selection but before observing the stopping time, with

\[
G(\theta)=\min_{1\le l\le m}\max_{1\le i\le6}TV(p_i(\theta),(MED_l)_i).
\]

Restrict to b_AV=0, a_A=a and c_AV=c in [1/2,7/8] (other controls fixed legally). In the pure AV row, p3(T3)=z=(1-a)c, while q_{3,l}(T3)=(ED_l)_{AV}(T3)=r_l is a constant in [0,1]. TV dominates the error on an event, hence

\[
G(\theta)\ge\min_l |z-r_l|.
\]

The continuous map (a,c)↦(1-a)c takes the rectangle onto the **entire** interval [1/16,7/16], length 3/8. If m intervals of radius ρ centered at r_l cover an interval of length L, the union's total length is <=2mρ; therefore ρ>=L/(2m). Taking the supremum gives the exact source-observer lower bound

\[
\boxed{\sup_{a,c\in[1/2,7/8]} G(\theta(a,c))\ge 3/(16m)}.
\]

For m=10 the bound is 3/160. On the unrestricted legal mother control cube [0,1]^11, choose a_A=b_AV=0 and c_AV=z in [0,1]; the same proof gives sup_θ G(θ)>=1/(2m), or 1/20 for m=10.

The interval-covering bound is sharp for the **one-event scalar readout**, among arbitrary m constants: take r_j=z_min+(2j+1)L/(2m) for j=0,...,m−1. It is not asserted sharp for full four-time TV or the mother six-preparation joint objective. The prior mother lower bound remains stronger numerically; the contribution is an exact observer-sensitive bridge and quantified information-loss mechanism.

## Relation to auxiliary δ3 and BRC/native scope

The previous auxiliary exact δ3=5211/21952 concerns reconstructing the ordered **three-i.i.d.-trial** ternary law from three binary coarsenings under one shared (a,c). Here the one-trial C and B observers are source-faithful, but Theorem 1 shows three fresh draws cannot be created by a fixed Markov postprocessor of **one** stopped time. Mother E is fixed on statistical sources and its finite decoder bank is selected before stop-time observation; that causal operation is distinct from B⊗3 on three observed stopped times. Theorem 2 directly applies to the actual mother protocol without assuming replica sampling.

This is a positive, negative and quantitative factorization analysis on the **frozen statistical S23 model**. The six latent statistical sources are not the P000 native six spatial axes; X6/provenance and independent-time interpretations retain their own bridges. No world-axiom changes or mathematical admission are made here.

## Executed certificate / next problem

VERIFY.py (standard-library exact Fraction) checked the source mixing row, four legal AV policy values, event observer identities, affine third differences, cubic third difference 3/2048, one-H TV lower bound 3/16384, and bank covering 3/160 for m=10. RUN_EVIDENCE.txt is the actual stdout. Continuum claims follow from the displayed algebraic proofs, rather than floating-point or finite grids.

**Next:** specify a lawful three-replica S23 experiment with explicit source/re-preparation sampling, shared θ, label-choice timing and decoder class. Test exact commutation of source encoder E with B⊗3/C⊗3, and derive the correct Blackwell deficiency inequality for that replicated experiment. Maintain a separate statement for the original one-stop mother R_beh(k,m). Review the auxiliary exact-Bernstein theorem independently before canonical acceptance.
