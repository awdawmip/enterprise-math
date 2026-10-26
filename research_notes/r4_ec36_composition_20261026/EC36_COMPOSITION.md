# R4-EC36 — Exact source-label error propagation under repeated BRC observer compression

Status: AUTHOR_SIDE_PROOF_AND_EXACT_CHECKS; not an independently admitted theorem or native X6 heartbeat computation. Date: 2026-10-26. 
Research mode: source-backed auxiliary BRC research, with current canonical owner/CLAIM **unverified** (native control query \`CONTROL_QUOTA\`).
Global canonical knowledge read: \`awdawmip/chatgpt-global-knowledge@f43f0160e56ef99ea5daa8bbfe8c44516e7661b9\` / GLOBAL_KNOWLEDGE_V1. Enterprise Math control read: \`awdawmip/enterprise-math@51e594f6642b88f8ab6d852f575fff4911d3e081\`.
The ACTIVE P000/worldview is respected; its \`fixed_heartbeat_program=null\`. Neither extra historical state nor operation depth is asserted to be an additional spatial/time axis.

## 1. Exact inherited source model

Reuse EC33's positive ordered-microscopic-source transition \`transitions_v\` from
\`0f84db42704c6e107adb9fd99d5e64cb77589e9d:research_notes/r4_ec33_label_fibre_20261026/EC33_verify.py\`.
Write remaining capacity \`a=H-q\`, with H>=1. At capacity a>0, the observed labels R and B each have precisely one positive microscopic source edge and decrease a by one. At a=0, only R is possible, via two distinct microscopic source branches, and capacity remains zero. Every state has two source alternatives. Normalizing the length-n source counts by 2^n gives fair independent R/B at positive-capacity steps and deterministic R at zero-capacity steps. The observer sees R/B, not individual saturated R0/R1 branch IDs.

Given a fixed deterministic post-transition capacity map Q:{0,...,H}->{0,...,H}, let T(a)=max(a-1,0) and define
a_t=T^t(a_0), while b_0=a_0 and b_(t+1)=Q(T(b_t)).
For any n>=0 put I={0<=t<n:a_t>0} and J={0<=t<n:b_t>0}. Both paths have exactly 2^n microscopic sources in total. Their normalized label-word measures P_I and P_J are uniform on the words whose letters at every index outside the respective mask are R; a free index accepts R or B equally.

## 2. All-horizon exact composition theorem

**Theorem EC36.1.** For arbitrary finite free-index sets I,J in {0,...,n-1}, define p=|I\J| and q=|J\I|. Then

  TV(P_I,P_J) = 1 - 2^(-max(p,q)).

For the corresponding *unnormalized* source-word counts C_I(w)=2^n P_I(w) and C_J(w)=2^n P_J(w),

  sum_(w in {R,B}^n) |C_I(w)-C_J(w)| = 2^(n+1) TV(P_I,P_J).

**Proof.** P_I has support size 2^|I| and has mass 2^(-|I|) at every supported word. Similarly P_J has support size 2^|J|. The intersection of their supports has exactly 2^|I∩J| words; at each intersection word the smaller of the two probabilities is 2^(-max(|I|,|J|)). Therefore the overlap mass is 2^(|I∩J|-max(|I|,|J|))=2^(-max(|I\J|,|J\I|)). By the finite-space identity TV=1-sum_w min(P_I(w),P_J(w)), the formula follows. Multiplying both measures by the same 2^n gives the exact L1 count identity. QED.

**Corollary EC36.2 (necessary and sufficient compositional error budget).** For 0<=epsilon<1 and fixed length n, define d_(epsilon,n)=max{0<=d<=n:1-2^(-d)<=epsilon}. Repeated post-transition compression obeys TV_n<=epsilon if and only if both p<=d_(epsilon,n) and q<=d_(epsilon,n). In particular epsilon<1/2 demands I=J; for all finite n, exact preservation is equivalent to agreement of the indicator of positive capacity at *every* future output step. This is a path-level certificate. Importantly, the exponent is max(p,q), **not** |I△J|: with I={0}, J={1}, TV=1/2.

## 3. Exact no-go for repeatedly reusing a one-step exact quotient

**Theorem EC36.3.** A capacity map Q can preserve the full one-step R/B distribution **at every state** while its repeated use causes whole-future-word TV to converge to one.

**Witness.** Set H=2, a_0=2 and Q(0)=0, Q(1)=2, Q(2)=2. At every a, the one-step label law at a and Q(a) is identical: if a=0 it is certain R; if a=1 or 2 it is fair R/B. But the original capacities are (2,1,0,0,...), while the compressed capacities are (2,2,2,2,...). Thus the first two steps are free in the original process, every step is free in the compressed process, and Theorem EC36.1 yields exactly

  TV_n = 0 (n<=2), and TV_n=1-2^(-(n-2)) (n>2).

In particular TV_3=1/2, TV_4=3/4, TV_8=63/64 and lim_(n→infinity) TV_n=1. The reason is failure of successor quotient compatibility at a=1:
Q(T(1))=Q(0)=0, whereas Q(T(Q(1)))=Q(T(2))=Q(1)=2.
One-step equality does not certify commuting future updates. EC35's *budget-decreasing* state (h,min(a,h)) is a distinct correct finite-horizon quotient; this no-go does not contradict it. QED.

## 4. Verification and scope

Full local exact Python verifier: \`EC36_verify.py\` in local evidence archive \`EM_R4_EC36_COMPOSITION_20261026.zip\` (available in the conversation). It enumerated **all** Q maps for H=1,2,3 (4,27,256 maps), all initial capacities 0..H and lengths 0..8; 10,017 exact state/depth/map cases, 1,137,486 word-level checks, 10,017 exact TV and 10,017 exact L1 checks; a ZIP extraction reproduced its JSON report byte-for-byte. The scoped GitHub JavaScript verifier in this directory independently checks the exact source law/closed masks and TV identity across an exhaustive finite range (see its generated report). All arithmetic is integer/rational or exact powers of two; no π, trigonometry, matrix exponential, floating-point physical propagator, or phase approximation. Finite checks do not establish the infinite theorem; the support-count proof above does.

The statement concerns **EC33's auxiliary positive BRC R/B-label observer**. It does not prove preservation of full microscopic R0/R1 IDs, arbitrary terminal ports, source-labelled native X6 dynamics, physical heartbeats, or signed/complex amplitudes. In particular, native X6's true update, admissible three-dimensional slice and third-coordinate semantics, time readout, source-fibre map and native Owner/CLAIM are unverified. Status: \`NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION\`. Independent Driver review/formal mathematical admission is pending.

## 5. Next discriminating problem

Extend the compositional source-count certificate from deterministic Q with label-independent state paths to **label-dependent and stochastic post-transition compression**, preserving microbranch provenance and typed observations; derive a sharp path-space coupling bound from the actual conditional BRC source kernels. Separately obtain an authorized X6 labelled transition and prove the native-to-BRC fibre map before applying any auxiliary error theorem to native dynamics.