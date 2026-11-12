# R749SMG — When a noisy public choice feeds back into the next source query

Date: 2026-11-13 (Asia/Shanghai). Continuation of R749SMD–R749SMF; author-side mathematical result.
Scientific input pin (unchanged): `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.
Predecessor: `2026-11-13_R749SMF_PUBLIC_CHANNEL_RANK_PHASES.md` at commit `ed18c3fa836fa94900c7c71e508fa097456ee69a`.
Scope: a finite conditional source-observer model on three historical signs. No native V29/V39 Cell/Link/Port permission follows from this construction.

## 1. Feedback-before-query experiment

Hidden historical source: `z=(x,y,t) ∈ {−1,+1}³`; publicly observed ordered bits `(a,b,c) ∈ {−1,+1}³`. Let `epsilon_A,epsilon_B,epsilon_C∈[0,1]` be independent bit-flip probabilities, and `alpha_i=1−2 epsilon_i`.

First sample an internal `A_0` with `P(A_0=a_0|x)=(2+a_0 x)/4`; transmit it through BSC(`epsilon_A`) to obtain the **public** `A=a`. The controller now uses this *observed* value to choose the second named source port `z_a=y` when `a=+1` or `z_a=t` when `a=−1`. Sample an internal `B_0` with `P(B_0=b_0|z_a)=(2+b_0 z_a)/4` and transmit it through BSC(`epsilon_B`) to obtain public B. Independently sample `C_0` with `P(C_0=c_0|yt)=(2+c_0 yt)/4` and transmit through BSC(`epsilon_C`). The public A-noise is **before** the B-selector; B/C-noise is after the associated internal choices.

The resulting exact 8×8 column-stochastic likelihood kernel is

[
N^mathrm{fb}_{abc,xyz}=rac{(2+alpha_A ax)(2+alpha_B b z_a)(2+alpha_C c yt)}{64}.
]

The prior ranges over all strictly positive probability measures on the eight historical states. The query asks for the full distribution of the observed three-bit word. As in R749SMF, the minimal number of independent affine source moments for arbitrary interior priors is `rank(N)-1`.

## 2. Theorem: all exact parameter strata

Define `I_i=1[alpha_i != 0]`. For all real noise parameters in `[0,1]^3`:

[
operatorname{rank}N^mathrm{fb}=
egin{cases}
2^{1+I_B+I_C},& alpha_A
e0,\
3,&alpha_A=0, alpha_B
e0, alpha_C=0,\
2^{I_B+I_C},&alpha_A=0	ext{ in every other case}.
end{cases}
]

Consequently the minimal affine source coordinates are respectively this rank minus one. The possible ranks are **1,2,3,4,8**. Particularly, when `epsilon_A=epsilon_C=1/2` and `epsilon_B≠1/2`, exactly **two** independent source moments are needed: `E[Y]` and `E[T]`; one moment is not sufficient.

**Proof.** Put `f_a(x)=1+a alpha_A x/2`. Up to a strictly positive row factor, for each fixed public A=a, the row span over varying B,C is `f_a·U_a`, where `U_a` is spanned by a subset of `{1,z_a,yt,z_a yt}`: retain `z_a` iff `alpha_B≠0`, and `yt` iff `alpha_C≠0`. Since `z_+=y,z_-=t` and `z_a yt` is the other historical sign, when both B,C are informative `U_+=U_-=span{1,y,t,yt}`. If `alpha_A≠0`, `f_+` and `f_-` are a basis for `span{1,x}`. If B and C are informative their two four-dimensional blocks therefore have direct-sum dimension eight. With only C informative the spans `f_a span{1,yt}` also sum directly, giving four; with only B informative the four functions `f_+,f_+y,f_-,f_-t` are independent by coefficients of `1,y,t`, giving four. With neither informative, `f_+,f_-` span two dimensions. If `alpha_A=0`, `f_+=f_-=1`. The two B-only blocks have union `span{1,y,t}` of dimension three. Both B and C informative produce `span{1,y,t,yt}` of dimension four; C-only produces `span{1,yt}` of dimension two; neither produces constants. Each case gives the formula. The linear map from the open prior simplex to all word probabilities has affine rank `rank(N)-1`, since the constant row belongs to the span and arbitrary small signed zero-sum perturbations remain feasible inside an interior prior. QED.

## 3. Determinant: unchanged off the singular locus

For every noise triple,

[
|det N^mathrm{fb}|=rac1{4096}prod_{i=A,B,C}|alpha_i|^4.
]

**Proof.** Order observations by their public A. For each A=a the 4×4 conditional (B,C) channel on the four (Y,T) sources is, up to column permutation, `B_{alpha_B/2} ⊗ B_{alpha_C/2}` where the two-sign channel `B_r` has eigenvalues 1 and r. Its determinant magnitude is `(|alpha_B alpha_C|/4)^2`. The first public A-channel acting independently over four (Y,T) states is `B_{alpha_A/2} ⊗ I_4`, with determinant magnitude `(|alpha_A|/2)^4`. Multiplying both four-state conditional blocks and the first channel yields the stated determinant. The factorization holds at singular endpoints by continuity. QED.

Thus feedback leaves the full-rank determinant law of R749SMF unchanged, but changes the singular strata: when A and C carry no source signal while B does, the no-feedback/postprocessing construction has rank 2 whereas the feedback construction has rank 3. The publicly observed A still declares **which named source port the controller queried**.

## 4. An exact positive-prior separation witness

Take two strictly positive histories:

[
mu_Y(x,y,t)=rac{1+y/2}{8},qquad
mu_T(x,y,t)=rac{1+t/2}{8}.
]

Every atom lies in `[1/16,3/16]`. At `epsilon_A=epsilon_C=1/2` and arbitrary `epsilon_B∈[0,1]`, the old R749SMF arrangement (public A-noise applied **after** the internal A has already selected the B-query) gives **identical** public word distributions for these two priors. In the new feedback experiment,

[
mathrm{TV}(N^mathrm{fb}mu_Y,N^mathrm{fb}mu_T)=rac{|alpha_B|}{8}.
]

**Proof.** A is an independent fair public choice. Given A=+, the B mean is `alpha_B E[Y]/2`; given A=− it is `alpha_B E[T]/2`. Under `mu_Y`, these prior means are respectively 1/2 and 0; under `mu_T` they are 0 and 1/2. C is an independent fair public bit. Each A/B pair contributes absolute difference `|alpha_B|/16` to the full A/B marginal, summing to `4|alpha_B|/16`; division by two gives the TV formula. Under postprocessing, internal A is fair for these X-independent priors, independent of observed A, and B averages Y and T symmetrically; both priors have `E[Y]+E[T]=1/2`, hence the same distribution. QED.

This is an exact provenance/branch preservation effect: injecting the same amount of public output noise before rather than after a branch selector changes which named source relationships future observations can distinguish.

## 5. Exact checking and next problem

The companion standard-library Python program checks all 125 triples `epsilon_i∈{0,1/4,1/2,3/4,1}` with exact `Fraction` arithmetic: column normalization, nonnegativity, ranks, determinants, and the four contrast cases with `epsilon_A=epsilon_C=1/2`, `epsilon_B≠1/2`. It additionally checks 40 positional marginals. The executed result is `PASS`; rank counts over the 125 triples are `{1:1,2:8,3:4,4:48,8:64}`. These finite checks test the implementation; Sections 2–4 establish the stated all-real-parameter algebraic claims.

Next: classify a controller that feeds both A and B through a finite memory register, and test the observable-subspace closure and minimal Walsh carrier for arbitrary future feedback operations. Separately, locate a real V29/V39-admitted triadic event before transferring this conditional source result to native Cell/Link/Port/BRC dynamics. Research preservation is not a shared-task CLAIM or independent review.
