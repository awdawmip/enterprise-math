# R762DC — Bounded frame reachability determines exact X6 pair-area BRC repair

Date: 2026-11-17. Task RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142. Researcher EM-X6-3050F6, original SID MCP-4b2d70a97f594366a7c94a0f8b45df38. Independent review NOT_REVIEWED.

## Scientific provenance and protected scope

Frozen taskbook: `awdawmip/enterprise-math@e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md`, blob `218bf9ce05fd2dd79f477ac269fc3590f83f482e`. Frozen P000 V5: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`.

This note consumes R762CH, PR #2575 commit `1c860018c4399e1b7497192ef818e3567390d2e2`, `research_notes/portable_direct/R762CH_PAIR_AREA_FRAME_TRANSPORT_THEOREM.md`: for closed signed-X6 primitive unit-step paths, the fifteen oriented pair-area coordinates are additive under closed-loop concatenation, and transform equivariantly under axis permutations. R762DA/R762DB supply distinct positive BRC probability seed budgets for sparse and adaptive temporal sampling, and are retained at their previously proved scopes.

P000's six native axes, three-force minimum, pairwise PERP_E/120-degree definition and affine Cell torsor remain fixed. Pair-area coordinates label path provenance, not native two-dimensional spatial planes. This work studies a specifically declared **diagnostic passive-reframing candidate** rather than assuming a native TRIADIC_CLOSURE_E event.

## Setup — reachable area observables

Let q>=2 be an integer. Given a closed word H of signed primitive steps ±e_i in Z^6, let C_ij(H) be the R762CH alternating pair-area, reduced modulo q. This gives a typed **history residue** C(H) in (Z/qZ)^15, separate from Cell position.

Start with a three-Port frame on axes (0,1,2). Its pair diagnostic set is E0={01,12,02}. Let S be any fixed collection of permutations of the six axis labels (with optional known axis signs). The observer may perform at most h successive **passive frame relabelings** in S, including none, and at an accessible frame may ask any one of the three rooted pair-area phase guards Q_(e,k)(H)=[C_e(H)+k=0 mod q], k=0,...,q-1. The frame path and any externally specified appended closed loops are known. Query timing and later frame choices may adapt to previous answers. Each permitted frame action and guard remains available for every history.

For each permutation word w of length <=h, write p_w for its composition, and define
`E_h(S)=union_{0<=|w|<=h} p_w(E0)`, an unordered-pair set, `d_h=|E_h(S)|`.

## Theorem A — exact quotient and optimal repair for every finite horizon

For the declared frame/guard language, two histories are observationally equivalent through depth h if and only if their pair-area residues coincide on E_h. On the **single common-coarse-data fibre** of histories constructed below, the exact number of distinguishable classes is

```
K_h(S,q)=q^(d_h),        R_h(S,q)=ceil(log2 K_h)=ceil(d_h log2 q) fixed bits.
```

**Sufficiency.** Every readable area coordinate after any allowed sequence is a known sign times one of the original C_e for e in E_h. A signed reversal changes the phase label but not the required coordinate. All answers are therefore determined by C restricted to E_h. Any adaptive observer follows the same frame/query choices on histories with the same recorded vector, by induction on its transcript. Appending a known closed-loop history contributes a known additive pair-area vector by R762CH, so the retained coordinates still suffice for this named operation.

**Sharp lower bound, with an explicit X6 path witness.** For every e={i,j} in E_h take q independently labeled four-step slots. In each slot place either
`B_ij=(+e_i,-e_i,+e_j,-e_j)` or
`L_ij=(+e_i,+e_j,-e_i,-e_j)`.
Concatenate all slots in a fixed edge order. R762CH gives C(B)=0 and C(L) equal to a unit at edge ij; each is a native signed-step **closed path**. The resulting full history always has Cell return 0, time 4q d_h, and signed-direction histogram `count(+e_i)=count(-e_i)=q*deg_E_h(i)` for all six axes, independent of choices. Choosing t of q L-slots for edge e produces residue t mod q, t=0,...,q-1, and changes no other pair residue. Hence all q^(d_h) vectors occur on exactly the same full coarse Cell/time/signed-step-histogram fibre. If two such vectors differ on e, some frame path of length <=h presents that edge, and the phase guard `k=-C_e mod q` distinguishes the histories. Therefore they are pairwise inequivalent. QED.

This lower bound requires only the declared one-edge query guards; it does not assume every native triadic transition admits them. Additional source, path, or signed-force observables can refine the quotient.

## Theorem B — cyclic six-axis reframing saturates at twelve pairs

Take the single permitted relabeling `c=(0 1 2 3 4 5)` (a six-cycle). After r applications the rooted triangle presents unordered pairs
`{r,r+1}, {r+1,r+2}, {r,r+2}`, indices modulo six. These all have circular separation one or two. The entire cycle's pair orbit contains exactly six separation-one and six separation-two pairs, excluding the three antipodal pairs 03,14,25.

The exact reachable edge counts for h=0,1,2,3,4,5 and h>=6 are

```
d_h = 3, 5, 7, 9, 11, 12, 12, ...
```

Each step r=1,...,4 adds two new edges; r=5 adds the last distance-two edge, then repetition starts. By Theorem A the exact observer repair budget is `q^(d_h)` states. For q=2, the number of fixed residual bits is 3,5,7,9,11,12 and remains twelve at every later relabeling horizon. This is an intermediate, sharp scope between R762CH's one-fixed-frame three-pair and all-frames fifteen-pair extremes.

## Theorem C — a single extra swap forces all fifteen pair directions by depth five

Now allow `S={c,tau}`, where `tau=(0 1)` swaps the first two axis names. Enumerate distinct reached permutations by shortest word length in c and tau, starting at the identity, deduplicating each six-entry array. At exact distance h=0,...,5 the counts of **new** permutations are

```
1, 2, 3, 5, 8, 13.
```

Unioning their presented pair sets with all earlier layers yields the exact sequence

```
d_h = 3, 5, 8, 11, 14, 15  (h=0,...,5), and d_h=15 for h>=5.
```

This is a finite complete integer enumeration certified by the attached executable verifier, not a generic assumption that the two generators represent native V17/V29/V39 transitions. In this candidate, at horizon 2 the extra swap increases the q=2 memory lower bound from 7 to 8 bits, at horizon 4 from 11 to 14, and at horizon 5 from 12 to 15. The exact future-accessible pair **orbit** determines which dormant path residues must be retained.

## Verification

Run `node R762DC_VERIFY.js > R762DC_EVIDENCE.json` (Node.js built-in assert, integer-only). The independent-from-formula author checker evaluates the native four-step words, their signed direction histograms and all 15 pair contributions; checks signed-permutation covariance on identity, six-cycle and swap; BFS enumerates the two-generator permutation frontiers; constructs all q-slot single-edge residue witnesses for q=2..5; and checks that all q^d residue vectors have pairwise distinct phase-guard signatures for (q,d)=(2,12) and (3,8). Evidence: 450 unit-pair checks; 675 covariance checks; 210 constructive witness checks; exact signature sizes 4096 and 6561; all PASS. General validity follows from the proofs, finite checks corroborate examples and implementation. Independent review remains NOT_REVIEWED.

## Native research continuation

Obtain the authenticated and frozen-input-compatible native `TRIADIC_CLOSURE_E` signed Cell/Link/Port event predicate and licensed V17/V29/V39 transports. Determine whether any of their legal suffixes actually realize the diagnostic frame actions and area queries above, and which named branch/source and path-area residues they inspect. Then compute their true reachable observation closure and either certify its exact observer-safe quotient or construct a **legal** separating suffix. Preserve P000, full X6 Cell identity and the direct-user joint-relation observer-preservation contract. No native licence or physical dynamics is claimed by this conditional diagnostic theorem.
