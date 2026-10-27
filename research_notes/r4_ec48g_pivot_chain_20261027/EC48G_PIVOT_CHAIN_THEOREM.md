# EC48G — Pivot-chain lemma for seedless BRC memory compression

Date: 2026-10-27 (Asia/Shanghai). Status: AUTHOR-SIDE MATHEMATICAL PROOF + EXACT FINITE VERIFICATION, not a native Result, independent Driver decision, Foundation theorem, or native-X6 dynamical claim.

## Exact frozen sources / authority
- GLOBAL_KNOWLEDGE_V1 canonical main@bb0c0f4538fbc3ea90fc4118ecc8ce88f09f17bc: canonical bootstrap, manual, P000 V4, ACTIVE worldview, code/math/BRC policies and EM project router. P000 is a locked project premise, not a claim proved here.
- Enterprise Math canonical control main@fdbc7b890b4c4f132ab13005ba6db46e6a6fd9e0: AGENTS.md, docs/PORTABLE_RESEARCH_PROTOCOL.md, docs/RESEARCH_ACTIVITY_PROTOCOL.md.
- Scientific parent EC48F: immutable 795f9beabbd4fb10c973b3bd2976acaf76064aa4, research_notes/r4_ec48f_collision_signature_bank_20261027/EC48F_COLLISION_SIGNATURE_BANK_THEOREM.md.
- Actual actor: GitHub login awdawmip, local Researcher-ID EM-R004-EC48G-20261027-R11 and activity RA-EMR4-20261027-0918-EC48G-R11. The local ID is not a native claim. Native control query failed CONTROL_QUOTA and native session start failed STATIC_READONLY_SCOPE_DENIED (operation_sent=false). No active owner confirmation or formal CLAIM.

## Positive-weight auxiliary source model
H and Y are finite history and future-label sets. The separately normalized joint source laws p(h,y), q(h,y) are strictly positive. The stage-1 observer sees history h and privately encodes one of K memory labels with conditional distribution pi(m|h). The stage-2 observer sees y and declares hypothesis P with probability u(m,y). No persistent public/shared random seed is present. Effective decisions are w(h,y)=sum_m pi(m|h)u(m,y). Define alpha=sum_(h,y) p(h,y)w(h,y), beta=sum_(h,y) q(h,y)w(h,y), and S_K={(alpha,beta)}. Full-history Z=sum_(h,y)[0,(p(h,y),q(h,y))] is a two-dimensional positive-generator zonotope. Set K_hull=min{K:conv(S_K)=Z}, K_seed=min{K:S_K=Z}.

For critical ratio r=p(h,y)/q(h,y)>0, H_r denotes histories with at least one tied cell. A history outside H_r has forced binary decision word c_r(h)_y=1[p(h,y)>r q(h,y)]; C_r is the set of distinct such words. Each tied history has endpoint words a_r(h)_y=1[p(h,y)>=r q(h,y)] and b_r(h)_y=1[p(h,y)>r q(h,y)], so b<=a coordinatewise. It is called C-absorbed if BOTH a and b belong to C_r. D_r is the set of DISTINCT nonabsorbed ordered pairs (b,a). Let Q_r=sum_(p=rq) q(h,y). EC48A/EC48F establish the exact generic-threshold sign-profile characterization of K_hull and the one-transition face construction when |D_r|<=1.

## Theorem EC48G.1 (two-transition pivot face)
Fix r with C=C_r nonempty. Assume there exists c in C such that D_r consists exactly of two transition signatures:
  I: (b,a)=(x,c), x not in C;
  O: (b,a)=(c,y), y not in C.
All other tied histories are C-absorbed by definition. Then the entire full-history exposed face of alpha-r beta at its maximum is attainable using at most |C|+1 memory states without a persistent seed. Moreover K_hull>=|C|+1, hence this face is fully attainable with K_hull states. This improves the general EC48F simultaneous-bank bound B_r=|C|+|D_r|=|C|+2 by one state.

### Proof, explicit encoder and decoder
Partition tied histories into A (C-absorbed), I (their signature is (x,c)), and O (signature (c,y)). Let Q_A,Q_I,Q_O be the summed q-mass of tied cells of each class; Q_r=Q_A+Q_I+Q_O. Keep one deterministic decoder row for every word in C throughout. Add only one extra, movable, decoder row. Every non-tied history encodes to its forced word in C. We construct a three-piece continuous sweep of the TOTAL tied q-mass.

Piece A, t in [0,1]: the extra decoder is x. Every I history uses it and every O history uses c. An absorbed history with endpoints b,a in C privately encodes to a with probability t, to b with probability 1-t. Tied q-mass is t Q_A and covers [0,Q_A]. All strict non-tie bits are forced correctly.

Piece I, t in [0,1]: all absorbed histories use their a endpoint in C; O histories stay at c. The extra decoder is v_I(t)=(1-t)x+t c, and every I history uses it. On a non-tied coordinate of an I history x=c, hence this interpolation preserves its strictly forced decision. On every tied coordinate of I, x=0,c=1, hence its probability is t. Total tied q-mass is Q_A+t Q_I, covering [Q_A,Q_A+Q_I].

Piece O, t in [0,1]: absorbed histories stay at their a endpoint, I histories use c, and the extra decoder is v_O(t)=(1-t)c+t y for every O history. On each strict O coordinate c=y; on each tied O coordinate c=0,y=1. Thus tied q-mass is Q_A+Q_I+t Q_O, covering [Q_A+Q_I,Q_r].

All three pieces use exactly |C|+1 available rows (possibly fewer), all private encoders and decoder probabilities lie in [0,1], and non-tied forced decisions remain optimal. Therefore each point has alpha-r beta=V_r=sum max(p-rq,0). Since all tied generators (p,q) are parallel with slope r, the tied q-mass alone parametrizes the entire exposed face, and the three pieces jointly fill [0,Q_r]. The parameter t indexes alternative actual strategies; no public or persistent seed is stored.

Finally, at a generic threshold immediately above r, all non-tied words C remain unchanged and each I history has strict word x not in C. Thus K_hull>=|C|+1 from EC48A's signature theorem. QED.

### Corollary EC48G.2 (a new global sufficient condition)
Suppose at every critical ratio r either (i) |D_r|<=1 or (ii) the two-transition pivot condition in Theorem EC48G.1 holds. Then K_seed=K_hull. Strict-threshold vertices require at most K_hull states by the generic-sign-profile theorem. EC48F covers class (i) edges and the pivot lemma covers class (ii). Complementary decoder decisions give the opposite edges of the full-history zonotope. S_K is radially star-shaped about (0,0): scale every u(m,y) by t in [0,1]. Because the finite positive-generator 2D zonotope has no other exposed boundary face types, obtaining the entire boundary and radial contraction yields S_K=Z. Equality of convex hulls already supplies K_seed>=K_hull.

This is a new *sufficient* condition only. Cases with |D_r|=2 but no pivot, and all larger collision patterns, remain open. There is no assertion of general equality for arbitrary positive source laws.

## Explicit rational two-transition witness
Take H={0,1,2}, Y={0,1}, with positive raw matrices:
P_raw=[[1,3],[1,2],[2,3]], total 12;
Q_raw=[[1,1],[1,1],[1,1]], total 6.
Normalize p=P_raw/12, q=Q_raw/6. The critical likelihood ratios are 1/2, 1, 3/2. Across the four generic intervals, the numbers of distinct binary history signatures are [1,2,2,1]. Hence K_hull=2.

At r=1, history 0 has strict word c=(0,1); history 1 has transition (x,c)=((0,0),(0,1)); history 2 has transition (c,y)=((0,1),(1,1)). Therefore C={(0,1)}, D_1 consists of TWO distinct unabsorbed signatures, and EC48F's B_1=3 static bank would exceed K_hull, whereas our moving bank uses K=2.

First face segment: decoder rows (0,1),(0,t); assign (0,t) only to history 1 and (0,1) to histories 0 and 2. Exactly alpha=(3+t)/6, beta=(2+t)/6.
Second segment: decoder rows (0,1),(t,1); assign (t,1) only to history 2 and (0,1) to histories 0 and 1. Exactly alpha=(4+t)/6, beta=(3+t)/6.
For 0<=t<=1, both have alpha-beta=1/6 and together cover beta in [1/3,2/3]. At r=1/2 and 3/2, each critical face has only ONE nonabsorbed transition signature, so EC48F covers those. Thus K_seed=K_hull=2<|H|=3.

## Verification and coverage
Local Python 3 standard-library Fraction program EC48G_VERIFY.py independently enumerated 3^9=19,683 ternary sign matrices for H=3,Y=3, using q0(h,y)=1+((5h+7y) mod 4), P_raw=q0(2+sign), Q_raw=2 q0; all weights strictly positive and separately normalized. Of those templates, exactly 108 have the specified pivot and state-capacity condition. For each, 15 exact phase-and-interpolation settings were checked for strict forced bits, maximal support, tied q-mass, and bank size. All passed. Independent JavaScript integer verifier EC48G_VERIFY.js also enumerated the 19,683 templates, found the same 108, and checked 1,620 exact phase/t configurations with PASS. The explicit 3x2 positive rational witness was verified by Python Fraction at its critical and generic thresholds.

Exhaustiveness applies only to the declared finite sign-template family, not to arbitrary real or rational source probabilities. The universal pivot theorem is a direct algebraic proof, not an inference from sampling. There is no Lean/formal-checker result and no independent Driver audit.

## BRC/ontology boundary
Research reuse: EC48A sign-profile and EC48F tied signature bank are REUSE_APPLIED; exact finite algebraic test is EXTEND_EXISTING_TOOL. Carrier is strictly positive joint BRC-style source branch mass with explicit history provenance, a two-stage observation order, and subsequent terminal decision. The signed expression p-rq is a support functional, NOT signed BRC amplitude. This auxiliary source/decision theorem is NOT native X6 Cell dynamics, BRC-Shor rotation, or a 2D native plane. P000's six-dimensional discrete X6 Cell substrate and separate time typing remain in force; no native embedding/readout preservation certificate has been supplied.

## Next EC48H
Classify the remaining two-unabsorbed-transition critical faces with no shared pivot in C: both transitions originate outside C, both terminate outside C, or their transition centers differ. Start with three histories, 2-3 later labels and K_hull=2. Decide whether a K_hull-state continuous encoder/decoder reconfiguration exists, or output a strictly positive rational law, exact r and an uncovered rational interval certified by the EC48C encoder compatibility graph. The actual tied q-masses matter: sign patterns alone do not determine the missing-interval obstruction.
