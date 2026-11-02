# PREFIX-439 — Exact S6 X6 history Port: missing-bit obstruction and effect-coupled BRC repair

2026-11-02 Asia/Shanghai. AUTHOR-SIDE PROOF AND EXACT CHECKS; UNREVIEWED / NOT_ADMITTED. Research mother objective: the typed X6 BRC Port and path-history problem from PREFIX-438/437. Frozen scientific input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d; applicable current normative source base: enterprise-math main@bdba5cfa529f565d303c869e19f254ae3712f446; account rule snapshot: chatgpt-global-knowledge main@f3fb0738848db1c43c2af6040c3a1f442ef7e812.

## Exact auxiliary source model

Fix a chosen X6 Cell and six signed native axis steps. No independent native plane or complete three-dimensional slice is claimed. A signed word has displacement x in Z^6, primitive step count n (not a physical heartbeat interval), parity p=x mod 2, phase sign t in F2 and negative-step parities r_j=(number of negative e_j steps mod 2). Each primitive letter has phase 0. Define c(p,q)=sum_{i<j}p_i q_j mod 2. The auxiliary typed BRC branch composition is

  (x,n,t,r) *(y,m,u,s) = (x+y,n+m,t+u+c(p,y mod 2),r+s).

Phases/history use F2 addition; exact affine translation and positive BRC multiplicities are separate typed data. Alternatives add positive multiplicities by branch. This is a mathematical extension of the fixed signed-X6 source alphabet, not a claim of a native physical phase mechanism.

Observers: full terminal (t,r_1,...,r_6), any S6-relabeling of the individual r_1 observation, exact branch affine translations, and subsequent signed steps or axis relabelings. A standalone controller has no external displacement/duration oracle; an effect-coupled controller explicitly retains both per branch.

## Theorem A — S6 phase gauge and exact obstruction to standalone 64-state equivariance

For pi in S6 mapping old axis i to new axis pi(i), set

  F_pi(p) = sum_{i<j,pi(i)>pi(j)}p_i p_j mod 2.

Then P_pi(x,n,t,r)=(pi(x),n,t+F_pi(p),pi(r)) defines an S6 action by automorphisms of the auxiliary typed BRC product. In particular P_sigma P_pi=P_{sigma∘pi} and P_pi(a*b)=P_pi(a)*P_pi(b).

Proof: comparing pair order gives

  c(pi(p),pi(q))+c(p,q)=F_pi(p+q)+F_pi(p)+F_pi(q).

Both F_{sigma∘pi}(p) and F_pi(p)+F_sigma(pi(p)) have the same polarization and vanish on 0 and each basis vector. The difference is a linear form vanishing on a basis, hence zero. This proves the group law and composition preservation, including signed generators. The law is phase covariance, not naive phase invariance.

The PREFIX-437 controller keeping only p_1,...,p_5,t (64 labels) has no **standalone** S6 action: the empty word and +e_6 both have identical six retained bits, yet exchange of axes 1 and 6 gives different retained p_1. These words have different endpoints/durations: this is an obstruction to the control quotient alone, not to the combined exact-effect carrier or the earlier fixed-frame 64-state theorem.

## Theorem B — exact effect/duration recovery and 2048-state typed control repair

For any word, let N_- denote its total negative-step count. Then

  n=sum_j x_j + 2N_-,

so n-sum_j x_j is even/nonnegative and

  r_6 = ((n-sum_j x_j)/2 mod 2)+sum_{j=1}^5r_j (mod 2).

Also p_6=x_6 mod 2, relative to the chosen starting Cell. Thus for each legal branch the joint record (exact affine translation x, common packet duration n, 11-bit control C=(p_1,...,p_5,t,r_1,...,r_5)) recovers the complete (p,t,r), and supports exact S6 relabeling by first recovering the omitted bits. The finite control alphabet has 2^11=2048 values. This is **sufficiency**, not a global lower-bound/minimality claim for arbitrary effect-dependent control APIs.

For signed update (j,sg), with all additions modulo 2:

  p_i'=p_i+[i=j] (i<=5);
  t'=t+sum_{i<j}p_i;
  r_i'=r_i+[i=j and sg=-1] (i<=5).

Its exact six-axis effect is x -> x+sg*e_j. For a whole branch b=(y,m,u,s), the source-indexed target is

  p'=p+(y mod 2), t'=t+u+c(p,y mod 2), r'=r+s.

The cocycle relation c(p,y)+c(p+y,z)=c(y,z)+c(p,y+z) proves exact serial composition; alternatives sum the positive branch counts. This is the declared law of ControlPacket.from_edges / then with source-target blocks and exact Affine translation. The full upstream class is source-inspected, **not imported or executed**; the independent algebraic kernel has been executed with exact finite checks. EffectHistogram alone drops a phase/history label unless the control target retains it. r_6 must be derived per effect atom together with its packet duration, never from an averaged moment or a merged effect of different translations.

Scope: signed unit **translations** with unit primitive-step duration, chosen source-relative chart, fixed-duration alternatives and exact affine-effect atoms. General affine maps, physical heartbeat dynamics, physical Port actuators and variable-duration alternatives are unverified.

## Theorem C — 8192 standalone-state minimum in declared fully symmetric observer language

Consider deterministic finite controllers that must output (t,r_1,...,r_6) and support all signed steps and all S6 relabelings, **without** a position/time oracle. Exactly 2^13=8192 observable control states are required and sufficient.

Proof of sufficiency: retain six p bits, one t bit and six r bits. Theorem A gives the updates and S6 action.

Proof of reachability: positive signed steps set any p. A return loop (+e_j,-e_j) toggles r_j and leaves p,t unchanged. A plaquette (+e_1,+e_2,-e_1,-e_2) toggles t, and its toggles of r_1,r_2 are independently corrected by return loops. Every (p,t,r) is reachable.

Proof of separation: states with different t or r differ at horizon 0. If only p differs, permute a differing coordinate to position 1. If transformed phases differ, observe immediately; otherwise append +e_2, whose phase update includes the differing p_1. Hence no distinct pair is future-observer-equivalent for this declared language. Theorem does not apply if relabeling is absent from the permitted future language.

## Same-effect 64-way exact fiber

At exact x=0 and n=12, N_-=6, hence r has even parity. There are 32 such r vectors. For each choose six signed return pairs across the axes whose per-axis pair counts have the required parities, and arrange at least two axes with nonzero pair counts (for r=0 use 4 pairs on axis 1 and 2 on axis 2). The serial pair order yields t=0. Reordering one pair from each of two different axes into (+e_i,+e_j,-e_i,-e_j) preserves x,n,r and flips t to 1. Thus 64 distinct (t,r) observables occur at the **same** displacement and duration. At least six bits of observer-distinguishing information are necessary even with that full effect and duration, if phase and the orbit of r_1 are in the observation language. This does not establish global optimality of the 2048-state fixed-control implementation.

An additional equal-duration, equal-endpoint obstruction to keeping r_1 alone: (+e_2,-e_2) and (+e_3,-e_3) have identical endpoint, length, phase and r_1, but exchanging axes 1 and 2 makes their r_1 observations different.

## Evidence, exact scope and next scientific step

Source: original signed_brc.py Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176 under experiments/x6_signed_native_spatial_v16_20260905; upstream typed BRC API from src/enterprise_math/brc_control_port.py and src/enterprise_math/brc_transport.py at the above current source base. Executed the actual original signed_brc path/return count methods plus a proven auxiliary typed positive-multiplicity phase/history BRC extension. No pi/trig, Taylor, high-precision or ordinary non-BRC physics reference computation.

Actual full local certificate: 1728 generator associativity triples; 552960 S6/signed-step covariance squares; all signed words of lengths 0..4 and a bounded length-5 sample; 294912 complete 2048-state two-step source-indexed BRC target laws; all 64 fixed-effect witness states; two exact obstruction witnesses; and another 552960 coupled S6 representative transforms. All passed. A separate standalone repository reproducer runs the essential named families and was independently executed. Finite checks cover exactly their stated domains; universal conclusions above use the written proofs.

This is an author-side mathematical artifact, not a native result/admission. GitHub login=awdawmip with repository push rights; native current owner listing returned CONTROL_QUOTA and Site gateway had research_authority_granted=false, so no authenticated Task CLAIM, independent review, or native Result exists.

Next PREFIX-440: from verified GitHub blobs, **import and execute the unmodified upstream** ControlPacket/EffectHistogram/MomentState dependency chain. Test source-indexed 2048-state from_edges/then/alternatives/evaluate/moment_action on the same 64-way fiber and determine whether a per-affine-effect terminal Port can recover r_6 after genuine EffectHistogram coalescence. If not, specify the smallest typed extension and an exact failing witness rather than reporting a native implementation as complete.