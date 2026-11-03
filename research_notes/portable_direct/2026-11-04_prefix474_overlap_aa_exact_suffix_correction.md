# PREFIX-474 — Exact suffix-fiber correction for the self-overlapping aa gate in X6 BRC

**2026-11-04. Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.** This is author-side portable research, not a native formal Result, Review, or Foundation promotion.

## 1. Starting model, prior results and scope

Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Continue PREFIX-471 (universal base state count for words of equal gate length), PREFIX-472 (dictionary-free base ranking), and PREFIX-473 (nonconsecutive aba suffix ranking); their proof and admission statuses remain as originally recorded. The setting is the P000-native X6 signed six-axis affine cell torsor with time/order carried in a typed path, not a lower-dimensional world.

Use special x=+E1 and ten ordinary signed directions a=+E2, A=−E2, b=+E3, B=−E3, c=+E4, C=−E4, d=+E5, D=−E5, e=+E6, E=−E6. Every ordinary direction is legal. The special x is legal initially or after a terminal word aa. The length-two pattern aa has a nontrivial one-letter self-overlap. The KMP state q∈{0,1,2} is the length of the longest suffix matching a prefix of aa (so q2 means the last two directions are aa).

A length-n word has the exact positive BRC base observation f=(s,y1,...,y5,Av,Cv), with s=#x, yi=ci+−ci−, pi=min(ci+,ci−), Av=p2+2p4+p5 and Cv=p3+p5. Let S_n be the set of f reachable by legal words of length n, B_n=|S_n|, S_(n,q) the base observations admitting legal representatives in state q, and F_n=sum_q |S_(n,q)|. Negative-index sets are empty and B_m=0 for m<0. A tagged state (f,q) is not the ordered word: path multiplicity, provenance and positive weight remain separate typed observers. The finite-horizon quotient discussed here preserves the Boolean continuation language and resulting base observation only.

## 2. Lemma: reversible padding, including mixed positive/negative letters

Let v be any fixed word over the ordinary letters. On each axis i write hi+ and hi− for its plus/minus counts and yi for the old signed displacement. The old positive/negative counts are pi+max(yi,0), pi+max(−yi,0), hence appending v changes pi by exactly

Δi(yi;v)=min(max(yi,0)+hi+, max(−yi,0)+hi−).

Thus the map Tv changes yi by hi+−hi−, Av by Σ ai Δi with (ai)=(0,1,0,2,1), and Cv by Σ ci Δi with (ci)=(0,0,1,0,1). It leaves the special count s unchanged. Invert Tv by subtracting the known signed displacement shift, recomputing each Δi from the recovered old yi, and subtracting its valuation increments. Therefore Tv is injective even though the individual pi are not retained.

For any gate word w consisting of k≥1 ordinary letters, including repeated letters, proper self-overlaps and both signs of an axis, its **full-word suffix support** obeys the exact all-n identity

S_(n,k) = Tw(S_(n−k))  (n≥k).

Indeed, every legal word ending w remains legal when this ordinary suffix is deleted. Conversely, appending ordinary w to any legal word is always legal and leaves KMP in the full-match state k. This lemma gives a universal, dictionary-free rankable full-match block. The analogous equality for a *proper* prefix may fail because its appendage can complete a longer KMP match.

## 3. Theorem: exact three suffix supports for aa at every n

Define a finite exceptional set E0(n) of base observations by

E0(0)=∅;
E0(1)={f(a)};
E0(2)={f(aa), f(xa)};
E0(n)={f(a^n)} for all n≥3.

Then for every nonnegative n,

S_(n,0)=S_n ∖ E0(n);

S_(n,1)=Ta(S_(n−1) ∖ E0(n−1)) for n≥1, and empty for n=0;

S_(n,2)=Taa(S_(n−2)) for n≥2, and empty for n<2.

The missing proper-prefix supports are uniformly bounded (at most two base observations per length), even though the failure of naive padding persists to arbitrarily large n.

**Proof, q0.** If a legal word contains an ordinary letter c different from a, remove one c and place it last. The immediate aa predecessor of each previously admissible x is preserved when a non-a ordinary letter is moved. The resulting word remains legal and ends in q0. Consequently, a base observation without a q0 representative must have representatives consisting only of a and x. Such legal words with s≥1 occurrences of x have at least 2(s−1) letters a. With s=0, the nonempty word a^n ends in nonzero q. With s=1, zero letters a gives q0 word x, exactly one letter a gives only xa (which ends q1), and at least two letters a permits the q0 word a^t x. With s≥2 and any legal t≥2(s−1), the word x(aa x)^(s−2) a^(t−2(s−1)+2) x is legal and ends q0. The empty word is q0. Finally f(a^n) and f(xa) at their listed lengths determine the indicated pure-letter occupancies uniquely, because the exact identity n=s+Σ|yi|+2Σpi leaves no hidden canceling pair or extra letter. This proves precisely E0(n).

**Proof, q1.** Under aa, q1 means that the final direction is a and the previous direction (if present) is not a. Removing this last a gives a legal q0 word of length n−1; appending a to any legal q0 word gives exactly q1. Reversible padding Ta therefore transfers its whole base support, including its exact exceptional holes.

**Proof, q2.** The full-word suffix lemma with w=aa gives S_(n,2)=Taa(S_(n−2)).

**Minimal counterexample.** At n=2, f(aa) lies in Ta(S_1) but not in S_(2,1): the sole corresponding word aa has q2. For every n≥2, f(a^n) is similarly absent from q1. Thus the proper-prefix image equality used in an unrestricted extrapolation from aba is false even for the shortest possible self-overlapping gate. The exact exception repair above is sufficient for this aa gate.

## 4. Corollary: rational series and exact finite future classes

Let u_n=|E0(n)|, giving u0=0, u1=1, u2=2 and u_n=1 for n≥3. With the preceding proven base series for any gate word of length 2,

G(z)=Σ_(n≥0) B_n z^n
=(1+2z²)(1+z)²(1+z−z³) / ((1−z)^8(1−z³)),

the complete tagged-state count for **every** n≥0 is

F_n=B_n+B_(n−1)+B_(n−2)−u_n−u_(n−1),

F(z)=(1+z+z²)G(z)−(1+z)U(z),
U(z)=z+2z²+z³/(1−z).

Let N(n,H) denote minimal classes when allowed future words have length at most H and the observer includes legality and final base f. H=0 collapses all q states: N(n,0)=B_n. At H=1 the suffixes q0 and q1 have the same admissible one-step continuations, while q2 allows x. For n≥2, the q0∪q1 base support is exactly S_n ∖ {f(a^n)}, and the q2 support contains f(a^n). Consequently

N(n,1)=B_n+B_(n−2)−1 for n≥2;
N(n,1)=B_n for n=0 or 1.

Its generating series is (1+z²)G(z)−z²/(1−z). At H≥2, q2 permits x immediately, q1 permits ax but q0 does not, so all three suffix states have distinct admissible futures: N(n,H)=F_n for H≥2. The q distinction is considered only within a fixed base-observer fiber; the distinct future words give the corresponding explicit distinguishability witnesses.

**Dense codec.** Let R_m be PREFIX-472's exact dictionary-free base rank for k=2 and R_m^−1 its inverse. For the q0 block, use R_n with at most two sorted ranks of E0(n) skipped. For q1, invert Ta and reuse the q0 rank on length n−1. For q2, invert Taa and use R_(n−2) without holes. Concatenate the three blocks with their exact sizes. For H=1, use the entire base rank excluding f(a^n) (n≥2) for the combined q0/q1 block and append the q2 block. For H=0, use R_n directly. These are concrete bijections with integer range [0,N(n,H)−1], hence require the optimal fixed-width ceil(log2(N(n,H))) bits (0 for a singleton). At most two holes per block preserve the prior O(log(n+1)) arbitrary-precision **integer-operation count**, including no complete state dictionary. No bit-complexity improvement for full input conversion, provenance recovery or general BRC operations is implied.

In particular at n=8 the aa gate gives B8=33797, N(8,1)=40665, F8=56527, whereas the ab gate of PREFIX-467 gives B8=33797, N(8,1)=40666, F8=56526. Equal gate length determines base-state count under the reused hypotheses; it does not determine all suffix-history counts.

## 5. Executed certificate and verification range

The attached Python 3 standard-library source and original output log are the actual locally executed materials:

- prefix474_overlap_aa_certificate.py — exact Counter dynamic programming over all reachable f,q, keeping integer path multiplicities and positive masses. For n=0..4 it separately enumerates complete admissible ordered words and recomputes f, q, multiplicities and weights from symbol counts, independent of the incremental BRC transition. For n=0..8 it verifies E0 holes, q0/q1/q2 supports, B_n coefficients, F_n, H=1 classes and both weighted and unweighted path-series coefficients.
- PREFIX474_EXACT_EXECUTION.log — produced directly by the executed source, concluding ALL_CHECKS_PASS.

At n=8, q0=33796, q1=15862, q2=6869, F=56527, 110650630 legal ordered paths and exact positive total mass 10938069583787562. The finite validation covers n≤8 (independent full-word enumeration n≤4). Universal results are supported by the preceding written proofs and the imported exact base-series theorem, with no independent admission assertion. The positive weight assigns x and negative ordinary steps weight 1, while the positive E2..E6 steps have weights 6,12,18,24,36. It is positive BRC arithmetic, not signed/phase cancellation.

BRC interface resolution: COMPOSE_APPLIED — PREFIX-471 base series, PREFIX-472 base ranking and the exact valuation/update observer with source-sensitive KMP residual. The extra q is historical state, not a new native spatial coordinate. P000/ACTIVE and scientific pin were preserved.

## 6. Authority, provenance and next question

At this research pass, connected GitHub authentication was awdawmip with repository admin/push permission. Native task inventory read returned CONTROL_QUOTA. Native session creation returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false; active native Owner and own Researcher-ID/CLAIM remain unverified. This author-side source deposit does not modify the formal state machine or grant review authority.

**PREFIX-475:** for arbitrary ordinary gate word w, classify the deficiency T_(w[:j])(S_(n−j)) ∖ S_(n,j) as a semilinear family, and test whether its size is bounded independently of n. Search for a growing counterexample using repeated mixed-sign patterns; if found, determine its exact fiber count and codec correction. Independently derive suffix-conditioned ordered-path multiplicity generating series via a weighted KMP transfer matrix, preserving order and mass.
