# BRC N=4 — exact deterministic-code rate–distortion staircase and source-preserving stochastic barrier

**Status:** author-side analytic proof + executed finite exact-integer cross-check; **UNREVIEWED / NOT_ADMITTED**. Date: 2026-10-31. Directly continues PR #1757 @ `1b87b83880f4e5ce6060194b6f58b16e8e86338e`, which left the unrestricted *randomized* five-code minimax game open between `2/143` and `1/40`.

## 1. Exact experimental scope and quantifiers

Use the original strictly positive BRC N=4 experiment with 16 leaves `(S,J,K)`, `S∈{AU,AV,BU,BV}`, `J,K∈{0,1}`. Each individual K leaf has P/Q mass `n/240` with `(n_{J=0},n_{J=1})`:

| S | Q | P |
|---|---|---|
| AU | (10,10) | (9,11) |
| AV | (20,20) | (5,5) |
| BU | (15,15) | (3,27) |
| BV | (15,15) | (30,30) |

The encoder input is the **prepared** pair `x=(S,b)` with `b∈{P,Q}`; it is given **before** the latent J, the fair K and the lawful policy H. The decoder does not receive b or x. AV_P/AV_Q have identical conditional future laws, as do BV_P/BV_Q. The six distinct prepared conditional laws are therefore
`X_6=(AU_Q,AU_P,AV,BU_Q,BU_P,BV)`.
Within S, J has Bernoulli success rates
`AU:(1/2,11/20)`, `BU:(1/2,9/10)`, `AV=BV:1/2`; K is fair conditional on (S,J).

The public output is the actually emitted `O=(T,Decision,Z_BU)`, with BU-only sensor `Z=J XOR Bernoulli(epsilon)`, `0<=epsilon<=1/2`, and distinct absent-sensor symbol for other S. Allow all legal S23 or all legal S2 causal stopping/terminal-decision policies H. A policy-specific **stochastic** decoder `D_H(o|c)` is permitted. For a **deterministic** common encoder `f:X_6->[K]`, define
\[
 R_K^{\rm det}(\mathcal F;\epsilon)
 =\inf_f\sup_{H\in\mathcal F}\inf_{D_H}
   \max_{x\in X_6}{\rm TV}\!\left(L_H(\cdot|x),
       D_H(\cdot|f(x))\right).
\]
All infima are finite-dimensional; adding the duplicate AV/BV b-labels does not alter the game. Nothing here requires recovery of the realized J,K path.

## 2. Theorem: exact deterministic-code curve

For every real `0<=epsilon<=1/2` and for **either** `F=all lawful S23` or `F=all lawful S2`,
\[
\boxed{
 R_3^{\rm det}=\frac12,\qquad
 R_4^{\rm det}=\frac15,\qquad
 R_5^{\rm det}=\frac1{40},\qquad
 R_K^{\rm det}=0\ (K\ge6).
}
\]
The values are exact, including the endpoints of the sensor-noise interval. Randomness is allowed in the decoder; only the encoder is deterministic.

### 2.1 Six lawful separating strategies and pair distances

The following six policies lie in S23 (hence S2): continue from stage two, stop at stage three, then declare Decision=P iff (a) `S=AU`, (b) `S=AV`, (c) `S=BU`, (d) `S=BV`, (e) `(S,J)=(AU,1)`, or (f) `(S,J)=(BU,1)`, respectively. All are constant on the original declared likelihood-ratio classes and never inspect unobserved K.

For any two of the six prepared inputs set
\[
 d(x,y)=\sup_{H\in\mathcal F}{\rm TV}(L_H(\cdot|x),L_H(\cdot|y)).
\]
Then **exactly**:
\[
d(AU_Q,AU_P)=1/20,\quad d(BU_Q,BU_P)=2/5,
\quad d(x,y)=1 \text{ whenever }S(x)\ne S(y).
\]
For the first two equalities, conditional on the fixed S, every legal observation is a common kernel of J and fresh randomness; data processing bounds TV by `|p_x-p_y|`. Strategies (e) and (f) attain it because the Decision bit reveals J on the specified S. The additional BU sensor does not affect the equality. For distinct S, strategy (a)–(d) chosen for S(x) makes the public Decision bit deterministically different, attaining TV=1. No larger TV exists.

### 2.2 Deterministic collision lower bound

If `f(x)=f(y)=c`, every decoder `D_H(.|c)` is the same distribution for these two inputs. The total-variation triangle inequality gives
\[
 \max\{\mathrm{TV}(L_H(x),D_H(c)),
       \mathrm{TV}(L_H(y),D_H(c))\}
 \ge \tfrac12\mathrm{TV}(L_H(x),L_H(y)).
\]
After maximizing over H, the error is at least `d(x,y)/2`. Thus any cross-S collision costs at least `1/2`; a BU_P/BU_Q collision costs at least `1/5`; an AU_P/AU_Q collision costs at least `1/40`.

With three codes, four S classes force a cross-S collision, so `R_3>=1/2`. With four codes, either a cross-S collision occurs or each of four S classes uses exactly one code, forcing BU_Q and BU_P together, so `R_4>=1/5`. With five codes, either a cross-S collision occurs, or at most one of AU and BU can have two different codes; AU or BU must collide, so `R_5>=1/40`. Six codes have the trivial lower bound zero. These are lower bounds for **every** legitimate policy-aware stochastic decoder, independent of epsilon.

### 2.3 Explicit upper constructions, all lawful policies

Each code decoder may output an arbitrary mixture of the *correct conditional public laws* `L_H(\cdot|x)` for the announced H, independently of the actual hidden b,J,K. Such a stochastic mixture is a lawful reconstruction (not same-path recovery). For the AU pair, choose the midpoint of its two conditional laws; this has max error `d(AU_Q,AU_P)/2=1/40` under every H. Similarly the BU midpoint has max error `1/5`. For AV and BV, their two b-inputs already induce identical conditional laws.

The four explicit partitions, with a code assigned to each brace, are
\[
\begin{array}{c|l|c}
K & \text{codes (groups of prepared rows)} & \text{maximal TV}\\
3 & \{AU_Q,AU_P\},\{BU_Q,BU_P\},\{AV,BV\} & 1/2\\
4 & \{AU_Q,AU_P\},\{BU_Q,BU_P\},\{AV\},\{BV\} & 1/5\\
5 & \{AU_Q,AU_P\},\{BU_Q\},\{BU_P\},\{AV\},\{BV\} & 1/40\\
6 & \{AU_Q\},\{AU_P\},\{BU_Q\},\{BU_P\},\{AV\},\{BV\} & 0 .
\end{array}
\]
The AV/BV midpoint error is at most `1/2` for any legal H, since TV is at most one. Therefore the displayed maxima bound all finite causal and randomized lawful S2/S23 policies, for the entire continuous epsilon interval. The six separating policies attain each positive displayed maximum, proving equality.

## 3. Stronger limitation: even stochastic encoders with source-homogeneous codes cannot beat 1/40

Call a stochastic encoder `E(c|x)` **source-homogeneous** if each code c has a fixed source class `g(c)∈{AU,AV,BU,BV}` and
\[
 E(c|x)>0\ \Longrightarrow\ g(c)=S(x).
\]
This is a constraint on the *encoder's supports*, not an extra S input handed to the decoder. It permits random encoders within each source class.

**Theorem.** Over the source-homogeneous stochastic encoders, the exact infimum of the same minimax game is `1/5` with four codes, `1/40` with five codes, and `0` with six or more codes, for both lawful policy classes and every real epsilon. At most three codes are infeasible under source homogeneity.

**Proof.** All four S classes occur, so each needs at least one positive-mass code, and these code sets are disjoint. Four codes imply exactly one code for each S; BU_P/BU_Q therefore have identical encoded laws, and the BU separating policy forces error `>=1/5`. With five codes at most one S can possess two or more codes; hence either AU has exactly one code (forcing `>=1/40`) or BU has exactly one code (forcing `>=1/5`). The explicit *deterministic* constructions above achieve `1/5`, `1/40`, and zero, and they satisfy source homogeneity. QED.

**Consequence for the open game.** Any **strict** improvement below `1/40` with five codes must use an encoder that (i) is genuinely stochastic and (ii) has at least one code used with positive probability by prepared inputs from *different* S classes. Optimizing only deterministic encoders, or only source-homogeneous randomized encoders, cannot solve the unrestricted stochastic problem. This necessary condition does **not** prove that such an improvement exists.

## 4. Executed exact verification and scope

`VERIFY.js` reconstructs the original P/Q 16 positive K-leaves, computes all six legal third-stage policies with BU sensor outcomes using integer probability scale 160 for `epsilon∈{0,1/8,1/4,1/2}`, checks each pairwise separating distance, enumerates all **203** set partitions of six prepared rows, obtains their exact pair-collision lower bounds at K=3,4,5,6, and verifies the concrete code-group midpoint decoders' worst errors. It uses integer-only arithmetic: TV of scale-160 distributions is L1/320; all reported code errors use denominator 640. The recorded invocation actually executed and passed.

Finite checks establish these rational inputs and examples only. The continuous epsilon claims and the upper bounds over **all** lawful stochastic/adaptive S2/S23 policies are justified by the analytic kernel/TV arguments above. We do not claim a proof of the unrestricted stochastic optimum, independent review, Lean verification, Source task admission or native Heartbeat dynamics.

## 5. BRC and P000 interpretation

The six prepared conditional rows are branch/provenance-preserving sufficient hypotheses in a declared **external finite BRC probability experiment**. Their split/merge costs quantify conditional predictive information under a specified future observation language. Deterministic state compression has the exact staircase shown; nonlinear cross-source stochastic sharing is the open obstruction.

P000 V5 remains an internal six-native-axis, discrete-Cell, independent-time axiom system. Nothing in this finite statistical proof supplies its native transition kernel, source-preparation mechanism, physical sensor or Heartbeat calibration. No claim is made about a seventh spatial dimension or about empirical physics. Protected worldview is unchanged.

**Next:** constrain the remaining genuinely randomized **cross-S** five-code encoder space with the full BU public sensor and find either a certified improvement below `1/40` or a positivity-aware universal lower bound (see NEXT_TASK.md).
