# R247 — Exact finite-horizon affine-effect trace equivalence for deterministic positive BRC

**Status:** author-side mathematical derivation + exact finite verification. NOT a native X6 heartbeat theorem; NOT a Source-native Python import; no formal Researcher CLAIM, Driver review, Result admission or Foundation promotion. A control word's length is not a heartbeat duration. Four control bits are non-spatial labels.

## Frozen inputs and declared observer

Account rules: GLOBAL_KNOWLEDGE_V1 \`main@dae2d3974fa237fbf09aea29233e8a9b21a9d42d\`; P000 \`ACTIVE_LOCKED\`, original Git blob \`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc\` (verified by the P000 startup projection). Source baseline: Enterprise Math \`main@4e126797f473f213c9dd63058d265c8c8fc56b94\`. Reused \`src/enterprise_math/brc_control_port.py\` blob \`44def6b8ac787e798d3cc2c6be16f873f91b9db8\` and \`src/enterprise_math/brc_transport.py\` blob \`be1debe367263931bd5e93fd750be3ed54624fe1\`.

R246 author-side frontier: \`research_notes/R246_SINGULAR_EFFECT_TRACE_OBSTRUCTION_20261024.md\` at \`6a6f0ed8d36eadd0b7cded16064a927bc89ac25a\`. Its delayed singular example has shortest witness length 3; the masked example has 9 trace-equivalence classes but 10 strong row-congruence classes. Here we settle a **different question**: the existence of an exact finite bound for **all** deterministic rational-affine effect traces despite singular maps.

Finite nonspatial control states \`S\`, finite operation alphabet \`Σ\`, rational affine maps \`E_g(s)(x)=A_g(s)x+b_g(s)\` on \`Q^d\` for each state \`s\` and operation \`g\`. Each operation uses exactly one positive, weight-1, multiplicity-1 path from \`s\` to \`f_g(s)\` (the deterministic special case of Source \`ControlPacket.deterministic\`). Serial composition uses later effects on the **left**. Observer: \`π:S→C\` together with the **entire exact affine composite map** \`F_w(s)\`. States are trace equivalent iff, for every word \`w\`, final \`π\` labels and the two entire maps agree.

This observation is weaker than \`refine_control_partition\`'s **independently restartable** strong compositional quotient; no claim of equivalence between those two notions is made.

## Theorem R247.1 — finite exact decision for arbitrary singular/invertible affine effects

For a pair \`(s,t)\`, let

\[
P=\{(f_w(s),f_w(t)) : w\in\Sigma^*\},\quad r=|P|,\quad D=r\{2d(d+1)+1\}.
\]

**Claim:** If the pair is distinguishable under the declared final-control/full-affine observer, then some word of length at most \`D−1\` distinguishes it. An exact rational basis algorithm decides **all-future** equality using at most \`D\` independent vectors, no matter whether some \`A_g(s)\` is singular. The upper bound is not asserted optimal, and excludes arbitrary multibranch histograms/infinite-state or provenance-sensitive observers.

### Complete proof

(1) First BFS the finite ordered-pair transition graph \`P\`. If \`π(u)≠π(v)\` for a reachable pair \`(u,v)\`, the first witness has length at most \`r−1\`, since a shortest witness path cannot repeat an ordered pair. Henceforth assume these two labels match for every reachable pair.

(2) Define a rational vector space as a direct sum over \`p=(u,v)∈P\`. Each block has coordinates \`(M_u,h_u,M_v,h_v,c)\`, where \`M_u,M_v\` are rational \`d×d\` matrices, \`h_u,h_v\` are \`d\`-vectors, and \`c\` is a scalar. The vector-space dimension is exactly \`D\`. For operation \`g\`, the linear successor sends the block at \`p\` to the block at \`p'=(f_g(u),f_g(v))\` by

\[
(M_u,h_u,M_v,h_v,c)\mapsto
(A_g(u)M_u,\ A_g(u)h_u+b_g(u)c,\
 A_g(v)M_v,\ A_g(v)h_v+b_g(v)c,\ c).
\]

Contributions landing in the same block add. This is a **linear** map \`T_g\` on the direct sum: the extra scalar \`c\` makes affine offsets linear as well.

(3) Initially \`v_0\` has \`(I_d,0,I_d,0,1)\` in block \`(s,t)\` and zeros elsewhere. Induction on word length shows that \`T_wv_0\` is supported at exactly one ordered pair and stores the two complete affine composite maps. Define a linear difference observer

\[
L(v)=\sum_{p\in P}\left(\operatorname{vec}(M_u-M_v),\ h_u-h_v\right).
\]

For each actual word, \`L(T_wv_0)=0\` is **equivalent** to equality of its two entire affine effects. Rational signed differences appear only in *proof bookkeeping*, **not** as negative BRC path masses or cancellation.

(4) Let \`W_k=span_{\mathbb Q}\{T_wv_0:|w|\le k\}\`. Then
\[
W_{k+1}=W_k+\sum_{g\in\Sigma}T_gW_k.
\]
If \`W_{k+1}=W_k\`, it is invariant under every \`T_g\` and hence contains every future word vector. Otherwise \`dim W_{k+1}>dim W_k\`. Since \`dim W_0=1\` and the ambient dimension is \`D\`, a stable space must be reached by \`k=D−1\`: either an earlier equality stabilizes, or \`W_{D−1}=V\`. Thus \`L\` vanishes on *all* word vectors exactly when it vanishes on \`W_{D−1}\`; if not, a word of length at most \`D−1\` witnesses the difference. This also proves the finite exact basis-successor algorithm and its termination. QED.

**Scope caveat:** The proof depends crucially on finite deterministic control, rational affine maps and complete affine-effect readout; a generic \`EffectHistogram\` with branching is not represented simply by two affine composites.

## R246 specialization and exact test

The 16 states are \`s=8x+4a+2c+r\` with \`x,a,c,r∈{0,1}\`; \`π(s)=(x,a⊕c,r)\`, and
\[
G_3(x,a,c,r)=(x\oplus a\oplus c,a,c,r),\qquad G_2(x,a,c,r)=(x\oplus r,a,c,r).
\]
The initial ordered pair \`(2,4)\` reaches **only two** pairs: \`P={(2,4),(10,12)}\`, so \`r=2\`.

On the six original space coordinates, use \`N(z)=(0,z_2,\ldots,z_6)\`, \`C(z)=(z_1+1,z_2,\ldots,z_6)\`, and \`R(z)=(-z_1,z_2,\ldots,z_6)\` together with identity \`I\`. Both operations on control sources \`2,4\` have \`N\`; \`G3\` on sources \`10,12\` has \`I,R\`. \`G2\` on \`10,12\` has \`C,C\` in the delayed model and \`I,I\` in the masked model. All other edges have identity effects. Every path weight and multiplicity remains **positive 1**.

For the full six-axis affine type \`d=6\`, theorem R247.1 gives \`D=170\`, hence a complete bound **169**. Since the differing effects act only on axis 1 and identically on the other five axes, a faithful one-axis affine lift reduces the test to \`D=2×(2×1×2+1)=10\`, hence the sharper complete bound **9**.

Two independent exact implementations—Python \`fractions.Fraction\` and C++17 \`boost::rational<cpp_int>\`—computed:

- **Delayed model:** shortest distinguishing word \`G3,G2,G3\` (string \`323\`). Full effect on the first path is \`C∘N\`, constant coordinate \`+1\`; on the second it is \`R∘C∘N\`, constant coordinate \`−1\`. All words of length at most 2 agree. Before the witness the basis rank is **4**.
- **Masked model:** complete all-future equivalence, with an exactly successor-invariant **3-dimensional** reachable subspace in the 10-dimensional representation; \`L\` annihilates that entire subspace. Exhaustive word tests through length 10 corroborate but are not the all-future proof.
- Other checks: shared-singular families remain equal and a purposely asymmetric edge effect yields the correct one-step witness.

This proves that **singularity invalidates the particular two-step bound, not general finite decidability** in the declared typed deterministic rational-affine BRC class.

## Verification / honest limits

Execution in this run: standalone exact Python PASS; independent C++17 compilation and exact PASS; immutable local ZIP reopened, all included files hashed; independent Python/C++ cold-start replay PASS. A full external native Python import was attempted and returned \`ModuleNotFoundError: No module named 'enterprise_math'\`, so do **not** represent the above as a passed Source-native API integration test. The Source \`Affine\` value type accepting singular \`N\` is distinct from proving that \`N\` is a **legal Heartbeat-X6 physical state transition**.

Prior art: the finite-dimensional linear-span method is standard in weighted/probabilistic automata equivalence; e.g., W.-G. Tzeng, *A Polynomial-Time Algorithm for the Equivalence of Probabilistic Automata*, SIAM J. Computing 21(2), 1992, DOI \`10.1137/0221017\`. No claim of discovering linear reachability generally is made. The present reusable increment is the exact typed affine-effect BRC specialization, the explicit \`D\` bound, and the complete singular R246 model certificate.

## Source status and next unit

Author-side research activity: \`research_activity_records/RA-EMR247-20261024-0732-N4.json\` (source main entry, local session key explicitly **not** a platform-attested session). Authenticated GitHub user \`awdawmip\`. This note is a durable **author branch** artifact only, not a canonical theorem/Result. Owner / formal CLAIM await native dispatch and receipts.

Next R248: directly execute \`ControlPacket.deterministic\`, \`.then\`, \`Affine\`, \`EffectHistogram\` and \`refine_control_partition\` at an exact Source revision; audit Heartbeat-X6 legal space-update rules for singular \`N\`; explore whether any finite-dimensional span observer survives genuine positive multibranch effect histograms. R193 provenance embedding and original native enumeration completeness remain independent pending obligations. Do not edit P000 or the protected worldview.
