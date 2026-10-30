# BRC N=4: certified five-symbol minimax error bounds

**Author-side research, 2026-10-31. UNREVIEWED / NOT_ADMITTED.** Direct continuation of the precise six-state theorem in PR #1757, commit 8b4aaf08c00d736aa2989242f66f035175aef514. This proves a positive rational lower bound and a universal constructive upper bound; the sharp stochastic minimax value remains open.

## Frozen finite BRC experiment and game

The original 16 strictly positive leaves (S,J,K), with S in {AU,AV,BU,BV}, J,K binary, each K fair conditional on (S,J), have the following mass numerators **per individual K leaf** with denominator 240:

| S | Q,J=0 | Q,J=1 | P,J=0 | P,J=1 |
|---|---:|---:|---:|---:|
| AU | 10 | 10 | 9 | 11 |
| AV | 20 | 20 | 5 | 5 |
| BU | 15 | 15 | 3 | 27 |
| BV | 15 | 15 | 30 | 30 |

The eight *prepared* inputs are x=(S,b), b in {P,Q}. The external preparation label b is neither a native X6 axis nor a freely available decoder input. Conditional on x, J has success probabilities p_AU,Q=1/2, p_AU,P=11/20; p_AV,b=1/2; p_BU,Q=1/2, p_BU,P=9/10; p_BV,b=1/2.

A single stochastic encoder E(c|x) of at most five codes acts **before** J and before the lawful policy H is chosen. Each H has its own stochastic decoder D_H(o|c), without access to x,J,K. Only the *marginal public terminal record* O=(T,Decision,Z_BU) is evaluated: when S=BU, Z=J XOR Bernoulli(ε), with 0≤ε≤1/2, and elsewhere Z is a distinct absent symbol. This declared BU sensor is emitted after encoding; it is not assumed to be part of P000 or a stage-two observation. Same-realized-path reconstruction is not required.

For the policy class F = all lawful S23 or all lawful S2, define

\[
R_5(F;\varepsilon)=\inf_{E:\,|C|\le 5}\;\sup_{H\in F}\;\inf_{D_H}\;\max_{x} TV\bigl(L_H(\cdot|x),(ED_H)(\cdot|x)\bigr).
\]

A policy-aware decoder is permitted; E is fixed across **all** future H. Randomized stopping/decisions are included. Lawful stage-four decisions read K only after continuation and cannot rewrite K.

**Theorem:** For every real ε in [0,1/2] and F equal to either all S23 or all S2,

\[
\boxed{\frac{2}{143}\le R_5(F;\varepsilon)\le\frac1{40}}.
\]

The upper constant is the *actual worst loss of a particular five-code encoder*, not a claim that the optimal minimax value is 1/40. The lower constant is sharp for the **unstructured entrywise rank-five relaxation of the six-policy witness**; it is not established sharp for stochastic encoders.

## Proof: quantitative robust-rank obstruction

Reuse six policies that are legal in S23 and S2. All continue from stage two and stop at stage three. Four policies H_AU,H_AV,H_BU,H_BV decide P precisely when observed S equals the subscript; H_AU1,H_BU1 decide P precisely at contemporaneous (AU,J=1) and (BU,J=1). These decisions are constant on the original six likelihood-ratio classes (AU0, AU1, AV, BU0, BU1, BV); no unobserved K is consulted. The six prepared rows AU_Q,AU_P,AV_Q,BU_Q,BU_P,BV_Q and six policy columns above give the exact Decision=P response matrix

\[
A=\begin{pmatrix}
1&0&0&0&1/2&0\\
1&0&0&0&11/20&0\\
0&1&0&0&0&0\\
0&0&1&0&0&1/2\\
0&0&1&0&0&9/10\\
0&0&0&1&0&0
\end{pmatrix},
\quad\det A=\frac1{50}.
\]

For any five-code E and six policy decoders, their corresponding event probabilities form B=E_6 V, with E_6 a six-by-five matrix and V five-by-six. Thus rank(B)≤5. If all full-record total-variation losses are at most δ then |A_ij−B_ij|≤δ, because Decision=P is a legitimate public event. Choose a nonzero left-null vector w with w^T B=0. It follows that

\[
\|w^TA\|_\infty=\|w^T(A-B)\|_\infty\le\delta\|w\|_1.
\]

An exact inverse, checked independently by rational Gauss–Jordan elimination, is

\[
A^{-1}=\begin{pmatrix}
11&-10&0&0&0&0\\
0&0&1&0&0&0\\
0&0&0&9/4&-5/4&0\\
0&0&0&0&0&1\\
-20&20&0&0&0&0\\
0&0&0&-5/2&5/2&0
\end{pmatrix}.
\]

Set y=A^Tw. The six components of w=A^{-T}y are

\[
11y_1-20y_5,\quad -10y_1+20y_5,\quad y_2,\quad
\frac94y_3-\frac52y_6,\quad-\frac54y_3+\frac52y_6,\quad y_4.
\]

Therefore, by the triangle inequality,

\[
\|w\|_1\le(61+\tfrac{17}{2}+2)\|y\|_\infty
=\tfrac{143}{2}\|A^Tw\|_\infty.
\]

The coefficient is attained at y=(-1,-1,-1,-1,1,1), for which w=(-31,30,-1,-19/4,15/4,-1) and ||w||_1=143/2. Since w is nonzero and A invertible, combining the two inequalities yields δ≥2/143.

The sensor error ε never appears in these six lawful Decision=P event probabilities. Thus the lower bound is uniform across all ε, including an expressly suppressed sensor, and holds for all S2 since S23 is a subclass.

To expose the exact proof boundary, write u_i=sign(w_i)/(143/2) and B*=A−u y^T. Then w^T B*=0 and the maximum entrywise error is 2/143. **This shows optimality only for unstructured rank deficiency.** There is no assertion that B* factors as a common stochastic E and six stochastic decoders; their positivity/normalization may force a stronger lower bound.

## Proof: explicit universal five-code reconstruction

Encode (AU,Q) and (AU,P) as one common code AU*. Keep the four other codes AV,BU_Q,BU_P,BV, mapping their applicable prepared inputs deterministically. Given AU* the decoder samples J as Bernoulli(21/40); for each other code it samples J from the *exact* conditional prepared-input law (AV/BV fair; BU_Q 1/2; BU_P 9/10). It samples independent fair K when the lawful policy reaches stage four, runs the announced lawful S2/S23 stopping and decision policy, and emits the BU sensor conditional on the sampled J with declared noise ε. It never uses a hidden b or actual J/K.

At the AU states,

\[
TV(Bern(21/40),Bern(1/2)) =
TV(Bern(21/40),Bern(11/20)) = 1/40.
\]

Every other prepared state is simulated exactly. Each policy's full public terminal record is a common Markov kernel of the newly sampled J and supplemental randomness, so total variation cannot increase under this readout. Hence error ≤1/40 for every stochastic/adaptive lawful policy, for all real ε. The lawful policy H_AU1 reads J at stage three and makes the public Decision=P event distinguish the AU inputs: the constructed decoder incurs error exactly 1/40 there. This is sharp **for this encoder alone**.

**BRC/structural interpretation:** merging the AU preparation contrast erases an explicitly typed, future-observer-relevant conditional Bernoulli residual. Its exact 1/40 propagation bound is a *statistical approximation residual*; it is not a new spatial dimension, energy, force or evidence that P000 Heartbeat dynamics is physically true.

## Verified arithmetic and research boundary

The executed standard-library Python Fraction verifier checks both normalized strictly positive 16-leaf laws, all conditional J probabilities, determinant 1/50 and full inverse, exact operator norm 143/2 over 64 dual sign vectors, the unrestricted rank-deficiency witness, and **2048** exact S23 stage-three public-record comparisons (64 decision rules × eight inputs × ε∈{0,1/8,1/4,1/2}); all pass, constructed maximum TV=1/40. The analytic proof above, not this finite enumeration, covers all lawful policies and the continuous noise interval.

The previous six-symbol exact-sufficiency result is **reused** not newly claimed. This output neither proves the sharp five-symbol stochastic minimax constant nor admits a theorem through the native Source. No independent reviewer, native CLAIM, Result or formal checker has been invoked. P000 original V5, its X6/independent-time semantics, and ACTIVE joint-relation conservation/worldview remain unchanged. The physical transition / source-preparation / observer-commutation bridge is unresolved.

**Next:** Solve the constrained stochastic encoder–decoder optimization even for just the six lawful policies. Improve the 2/143 rank-relaxed lower bound with positivity/TV constraints, or produce a five-code counterexample with loss <1/40 and full statewise certificate. See NEXT_TASK.md.
