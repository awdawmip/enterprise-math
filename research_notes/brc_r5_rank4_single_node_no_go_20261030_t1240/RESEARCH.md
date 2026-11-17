# R5 — Exact rank-four no-go for every single-node P-error lift (14/14)

**Date:** 2026-10-30 Asia/Shanghai. **Status:** AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Auxiliary finite two-law stopping model; no native X6/Heartbeat dynamics or empirical physical interpretation is asserted.

## Frozen source and method
Verified canonical GLOBAL_KNOWLEDGE_V1 main at \`9b4248a268b843a2e15a925f9a650496c9a8d2be\` (bootstrap/manual/ACTIVE worldview/math/BRC policies). Verified Enterprise Math main at \`222f698b2c1c29cf9c64640940935e36e5656c6a\` (AGENTS, P000, native X6/time, joint-observer contract, portable research protocol and current control). Scientific predecessor: Draft PR #1663 commit \`dce83250d3bafb0c03a0a784ecb1e5f2eb039a3a\`, \`research_notes/brc_r5_real_image_degree_20261030_t1140/RESEARCH.md\` and verifier. Reuse the baseline equal-Q-residual rank-three actual-image equality at its *author-side* evidentiary status.

BRC use: **REUSE_APPLIED**. Carry 14 source-labelled positive P/Q path masses separately until the declared four-stop-observer map; a likelihood-ratio collision does not erase source provenance. The observer polytope lives in abstract \(\mathbb R^4\), not a new native spatial plane or an X6 coordinate replacement. P000/ACTIVE worldview remain unchanged.

## Model and theorem
Use unit-\(1/360\) masses at time 1: A=(120,240), B=(240,120); at time 2: A0=(60,180), A1=(60,60), B0=(180,60), B1=(60,60); at time 3: A00=(30,108), A01=(30,72), A10=(30,45), A11=(30,15), B00=(90,36), B01=(90,24), B10=(20,40), B11=(40,20). Each tuple is (P,Q) mass. The parent/child mapping is explicit in \`VERIFY.js\`. Stop/continue is optional at times 1–3 and mandatory at time 4. FULL has 14 real local stop variables; seedless LR has 12 variables keyed by \((t,L=P/Q)\), sharing only A1/B1 at time 2 and A11/B11 at time 3.

For terminal probabilities, let \(\eta=1/1000\), \(L=P(h)/Q(h)\), and
\[
p_0(t,h)=1/5+t/20+(t+1)/(100L),\qquad
q(t,h)=2/5-t/30+(t+2)L/200+\eta\,1_{\{t=3,h\in\{A11,B11\}\}}.
\]
For *one* selected history \(j\), set \(p_j(t,h)=p_0(t,h)+\delta\,1_{\{h=j\}}\), leaving mandatory t4 unperturbed. "Admissible" means all terminal error rates stay strictly between zero and one; both \(\delta=\pm1/1000\) pass the exact checker for every \(j\).

For a deterministic policy write \(z_h=1\) if it reaches and stops at \(h\), else 0. Define integer observers
\[
r=\sum_{h=A11,B11} q_h z_h,\quad
x=\sum_{t\le3}(4-t)p_hz_h,\quad
y=\sum_{t\le3}(4-t)q_hz_h,\quad
s_j=p_j^{mass}z_j
\]
where \(p_h,q_h\) are the integer path masses (and \(p_j^{mass}\) is **not** an error rate). For real policies take expectations. Direct P/Q change of measure gives
\[
T_P=4-x/360,\quad T_Q=4-y/360,\quad
e_P=21/100+T_P/20+T_Q/100+\delta s_j/360,
\]
\[
e_Q=41/100+T_P/200-T_Q/30+\eta r/360.
\]
For every \(\delta\ne0,\eta\ne0\), these four original observations and \((r,x,y,s_j)\) are connected by an **invertible affine map**, so rank and convex-hull equality/separation are invariant under this change of coordinates.

**Theorem:** For each of all 14 nodes \(j\), and **every nonzero admissible real** \(\delta\), the seedless LR four-observer convex hull has affine rank **four** but is **strictly contained** in the FULL convex hull. Thus all 14 *single-coordinate* P-error lifts of the equal-Q-residual baseline fail the mother target (same four-observer convex hull but different actual real image). The theorem does **not** rule out simultaneous perturbations at two or more nodes or new merger topologies.

## Proof with exact certificates
The following vectors \(w=(w_r,w_x,w_y,w_s)\) expose strict gaps between the exact maximum of \(w\cdot(r,x,y,s_j)\) over **all** 4096 deterministic LR masks and the maximum over **all** 16384 deterministic FULL masks. Each row also has a nonzero 4×4 determinant from five explicit LR mask observations; exact mask indices and signed determinants are embedded in the complete executable \`VERIFY.js\`.

| Node | separating w | max LR | max FULL | positive gap | nonzero LR determinant |
|---|---|---:|---:|---:|---:|
| A | (144,-28,70,-115) | 31920 | 32280 | 360 | -907200000 |
| B | (20,21,-14,-14) | 7560 | 7680 | 120 | 362880000 |
| A0 | (72,-14,35,115) | 22860 | 23040 | 180 | 816480000 |
| A1 | (7,4,-15,44) | 0 | 1320 | 1320 | 816480000 |
| B0 | (60,63,-42,56) | 32760 | 33120 | 360 | 2449440000 |
| B1 | (7,4,-15,44) | 0 | 1320 | 1320 | 816480000 |
| A00 | (72,-14,35,412) | 22860 | 23040 | 180 | 408240000 |
| A01 | (72,-14,35,412) | 22860 | 23040 | 180 | 408240000 |
| A10 | (-6,-32,70,591) | 43440 | 45840 | 2400 | 408240000 |
| A11 | (-527,-18,5,651) | 0 | 11160 | 11160 | 233280000 |
| B00 | (20,21,-14,70) | 10920 | 11040 | 120 | -1224720000 |
| B01 | (20,21,-14,70) | 10920 | 11040 | 120 | -1224720000 |
| B10 | (-68,45,-22,665) | 27240 | 29640 | 2400 | -272160000 |
| B11 | (-5,-2,1,7) | 120 | 240 | 120 | -233280000 |

A policy trajectory visits each time-LR key at most once. Thus the expected observer is **multiaffine** in its own class's independent local stop probabilities. Product-weight interpolation over the behavioral hypercube expresses each real-policy observer as a convex combination of class-specific deterministic-corner observers. Every LR support bound in the table therefore holds for **all real seedless LR policies and their convex hull**. The exact FULL maximizing mask in each row strictly violates the bound. The displayed nonzero affine determinants establish full rank four. Invertibility for any \(\delta\ne0\) carries these gaps back to the original observables, with no perturbation-size sampling. QED.

**Direct four-observer example.** For node A1 and \(\delta=\eta=1/1000\), FULL mask 8 has \((r,x,y,s)=(0,120,120,60)\), giving
\[
O^*=(2581/6000,\ 551/1800,\ 11/3,\ 11/3).
\]
Every real LR policy and its convex hull satisfies
\[
\boxed{132000e_P+21000e_Q-6717T_P-575T_Q\le36462}.
\]
The FULL witness produces **36473**, a strict integer gap **11**.

## Verification and exact scope
\`VERIFY.js\` is an actually executed standalone JavaScript verifier (no packages), using exact integer dot products, 24-term **BigInt** determinants and exhaustive 14×(4096+16384) = **286720** deterministic observation evaluations. It checks both likelihood-ratio collisions, mass conservation, exact support maxima, winning masks, all 14 rank certificates, and strict probability legality for \(\delta=\pm1/1000\) with \(\eta=1/1000\). Save stdout in \`EXACT_OUTPUT.txt\`; final marker \`PASS_EXACT_R5_ALL_14_SINGLE_NODE_RANK4_NO_GO\`. An independent Python standard-library Fraction/integer verifier was also executed locally and agreed on all 14 support/determinant pairs (not used as the submitted executable).

The real-strategy result follows from **proved multiaffine interpolation**, not finite sampling. The 14 normals were discovered using a numerical hull search, but only the exactly verified integer certificates enter the proof. Independent Driver review, Lean formalization, literature novelty and Source admission are not asserted. This auxiliary model is not claimed as a native X6 dynamical theorem.

## Next scientific unit
Single-node coordinate lifts are exhausted; pursue two-or-more-node P-error vectors or a non-lumpable multi-merger model. Screen the *entire signed four-dimensional hull* with exact LR Carathéodory mixtures (at most five vertices for every FULL deterministic vector) or a rational Farkas separating witness. Only upon strict all-signed hull equality seek genuine **real image nonmembership**. Do not infer nonmembership merely from a failed sufficient topology criterion. Preserve Source owner/CLAIM/Result/Driver boundaries.
