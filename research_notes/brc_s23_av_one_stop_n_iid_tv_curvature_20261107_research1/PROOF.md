# Single S23 stopped time versus n independent binary stops: exact TV-curvature certificates

Date: 2026-11-07. Scientific source fixed at `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Status: author-side analytical proof, exact rational check executed, independent review pending.

## Precise statement and legal observer

The frozen six-source eleven-control S23 mother source has third preparation equal to pure AV. On its lawful face `b_AV=0`, fix `a_A=1/2` and let `c_AV=c∈[1/2,7/8]`. The stopped-time distribution on (T1,T2,T3,T4) is
`p_z=(1/2,0,z,1/2-z)`, where `z=c/2∈[1/4,7/16]`. The deterministic binary observer is `B(T)=1_{T=T3}`; its law is Bernoulli(z). A NEW n-replica experiment consists of n conditionally independent applications of this preparation at the same fixed policy. Its target is `Q_z^(n)=Bernoulli(z)^⊗n` on the complete ordered set `{0,1}^n`.

For any parameter-independent stochastic kernel `H_n:{T1,T2,T3,T4}→{0,1}^n`, define `ε_n(H_n)=sup_{z∈[1/4,7/16]} TV(p_z H_n,Q_z^(n))`. This is a single-stopped-time simulation question, distinct from n fresh observed stopped times and distinct from the original one-stop mother finite-decoder-bank objective. A postprocessing device can output correlated n-word symbols.

**Theorem.** Put `z0=1/4`, `z1=11/32`, `z2=7/16`; for `n≥1` let

```
Δ_(n,r)=z0^r(1-z0)^(n-r) - 2 z1^r(1-z1)^(n-r) + z2^r(1-z2)^(n-r),
C_n = (1/8) Σ_(r=0)^n binom(n,r) |Δ_(n,r)|.
```

All `C_n` are exact rational numbers. For every stochastic `H_n`, `ε_n(H_n)≥C_n`. Moreover `C_(n+1)≥C_n`, `C_1=0`, and `lim_(n→∞) C_n=1/2`. In particular `ε_2≥9/1024` and

`ε_3≥27/2048 = 0.01318359375`.

The last bound strengthens the previous four-point/event-111 certificate `3/16384` by a factor of 72 in exactly the same one-stop-to-three-fresh-binary-trials model.

## Proof: affine source fiber and exact finite witness

Since `p_z=(1/2,0,z,1/2-z)`, the fixed-kernel output `L_z=p_z H_n` is affine in z. Thus `L_(z0)-2L_(z1)+L_(z2)=0` because `z1=(z0+z2)/2`.

On the target alphabet define the zero-mass signed measure `ν_n=Q_(z0)^(n)-2 Q_(z1)^(n)+Q_(z2)^(n)`. For any signed zero-mass measure v, let `||v||_TV=(1/2)Σ_w |v(w)|`. Then

```
||ν_n||_TV = || (Q0-L0)-2(Q1-L1)+(Q2-L2) ||_TV
          ≤ ||Q0-L0||_TV + 2||Q1-L1||_TV + ||Q2-L2||_TV
          ≤ 4 ε_n(H_n).
```

Every n-bit word with r ones has the same weight `Δ_(n,r)` in ν; there are `binom(n,r)` such words. Hence `||ν_n||_TV/4=C_n`, proving the universal bound.

At n=3 the four values of `Δ_(3,r)`, r=0,1,2,3, are respectively

`(567,-279,-9,297)/16384`.

Including the binomial multiplicities (1,3,3,1) gives `Σ_w|ν_3(w)|=(567+837+27+297)/16384=1728/16384=27/256`. Dividing by 8 yields the claimed exact `C_3=27/2048`. At n=2, `Δ_(2,r)=(9,-9,9)/512` and `C_2=9/1024`.

## Proof: monotonicity and asymptotic certificate

The marginal of each product law `Q_z^(n+1)` on its first n output bits is `Q_z^(n)`. Marginalizing the signed combination ν_(n+1) therefore yields ν_n. Total variation of a signed measure cannot increase under a stochastic marginal map, so `||ν_n||_TV≤||ν_(n+1)||_TV`; consequently C_n is nondecreasing.

Put `h=z1-z0=z2-z1=3/32`. For each n take the count event `E_n={w: |(#ones(w))/n-z1|<h/2}`. The Bernoulli weak law of large numbers implies `Q_(z1)^(n)(E_n)→1`, while `Q_(z0)^(n)(E_n)→0` and `Q_(z2)^(n)(E_n)→0`. Thus `ν_n(E_n)→-2`. Because ν_n has total mass 0, `||ν_n||_TV≥|ν_n(E_n)|`; also `||ν_n||_TV≤2` by the triangle inequality and normalization of each Q. Therefore `||ν_n||_TV→2`, i.e. `C_n→1/2`. QED.

## Executed exact verification and interpretation

`VERIFY.py` uses only `fractions.Fraction` and integer binomial coefficients. It verifies the precise 3-word signed coefficients, exact C2/C3, zero mass, a finite regression of monotonicity, and evaluates the exact rational lower formula at n=10,100,500,1000. Actual stdout is in `RUN_EVIDENCE.txt`. The all-n theorem and the limit follow from the displayed exact algebra and probability-law argument, not the finite regression.

At n=1000 the exact-rational certificate computed by the verifier is `C_1000≈0.498789320819`. This is a bound for producing one 1000-bit target word from a *single* S23 AV stopped time; it is not the prior six-hypothesis bound on reconstructing the ternary AV law from 1000 separately observed binary outputs.

BRC observer audit: preserve the full ordered n-bit word and its multiplicities in the TV sum; the count histogram is a sufficient quotient only for this exchangeable-law TV calculation, with exact multiplicity correction. Six statistical source labels here are not P000 native X6 spatial axes. No result or review admission is implied by this author-side calculation.

**Next unresolved unit:** Specify a three-replica lawful S23 sampling/channel protocol (shared policy, fresh conditional stop times, fixed source encoder per trial versus shared batch encoding, and label-selection timing) and identify which Blackwell/deficiency comparison maps commute. Keep the original one-stop `R_beh(k,10)` as a separate mother objective.
