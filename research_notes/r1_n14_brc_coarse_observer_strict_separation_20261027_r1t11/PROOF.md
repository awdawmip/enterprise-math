# R1/N14 — Coarse terminal observer: full-state SL is not necessary

Status: AUTHOR HAND PROOF + STRICTLY POSITIVE DISTINCT-TWO-LAW EXACT COUNTEREXAMPLE. The finite checker is witness-level; independent Research Driver review, Lean formalization, native Task/CLAIM/Result admission and P000 native-transfer are pending.

## Sources and authority

Frozen GLOBAL_KNOWLEDGE_V1 main@98ccaeb8d933ae4aa84a6e54ec27ec4dcdafe15a: bootstrap, operating manual, Enterprise Math task router, P000 startup projection whose canonical blob matched 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview, mathematics, code, BRC and activity procedures. Frozen Enterprise Math research input main@cc7c18fbf446962eda333bfbe450844613b08aa6: AGENTS.md, original native X6/time and joint-observer contracts, portable research protocol, persistence protocol, and predecessor research_notes/r1_n14_brc_two_law_strong_lumpability_iff_20261026_r1/PROOF.md and NEXT_TASK.md.

Actor is authenticated GitHub awdawmip (push-enabled). Live native tasks read returned CONTROL_QUOTA and native session start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. No active canonical owner or formal claim could be verified; this is a nonclaiming local-author contribution. Activity record RA-R1T11-20261027-COARSE01 is a local author record, NOT service Researcher authority.

The predecessor treats universal preservation of FULL (T,x(H_T),D) under two laws. Here the required output is strictly coarser (T,o(x(H_T)),D). The full-state theorem is neither modified nor promoted.

## 1. General observer-safe lifting lemma

Let H_{<=N} be a finite positive two-law prefix tree, with P and Q strictly positive, and a law-independent history policy assigning stop-A, stop-B and continuation probabilities at each visited prefix (continuation forbidden at depth N). Let x be a deterministic symbol-updatable time-respecting state, z=r(x) be a further quotient, and o=phi(z) the terminal observer.

**Lemma.** Suppose for EVERY full-history policy there is ONE law-independent z-policy preserving the complete joint law (T,z(H_T),D) simultaneously under P and Q. Then for EVERY history policy there is ONE law-independent x-policy preserving (T,o(x(H_T)),D) simultaneously under both laws.

**Proof.** Given the matching z-policy pi_z, set pi_x(action|x)=pi_z(action|r(x)). Because z=r(x) at each reachable ordered history, both policies have exactly the same probability of every action at that history. They therefore induce the same law of (T,z,D) under each P and Q. Apply the deterministic terminal readout phi. The resulting (T,o,D) laws coincide. QED.

This is a sufficient criterion only. It does NOT claim that every observer-safe x admits such an intermediate z, nor that LR remains necessary when o is coarser.

## 2. Exact strictly-positive P!=Q example

Take binary alphabet {0,1} and N=4. First-bit probabilities are P(0)=1/2, P(1)=1/2 and Q(0)=1/3, Q(1)=2/3. Subsequent conditional laws are shared by P and Q. After any prefix of length 1 or 2, the next bit is fair. At a length-3 prefix h, the conditional probability of next 0 is

    c(001)=3/4, c(010)=1/4, c(other h of length 3)=1/2.

All 31 ordered prefixes have strictly positive rational mass under each law, and the two laws differ. Let

    x(h)=(length(h), first(h), count_0(h)),
    z(h)=(length(h), first(h)),
    o(x(h))=first(h),    first(empty)=*.

Both x and z update deterministically by reading the next symbol; z=r(x). At t>=1, the complete conditional suffix distribution given first bit f is identical under P and Q. Hence for every nonempty prefix h:

    Q(h)/P(h)=2/3 if first(h)=0, 4/3 if first(h)=1,

and the root ratio is 1. LR is constant on each z-fiber, as well as on each x-fiber. In z, after the first symbol the next state is deterministically (t+1,f), so z satisfies two-law strong lumpability. At the root there is a single representative and lawful first-bit transitions.

### Direct proof of universal coarse preservation

Fix an ARBITRARY randomized full-history policy, used identically under both laws. Let S_L(t,f) be its mass surviving just before the decision at depth t with first symbol f under law L; A_L^d(t,f) be its mass stopping with decision d at that time and first symbol. The survival factor due to the policy depends on history but not on L. Since Q(h)=r_f P(h) on all prefixes in this first-symbol class,

    S_Q(t,f)=r_f S_P(t,f),  A_Q^d(t,f)=r_f A_P^d(t,f).

Therefore a_d(t,f)=A_P^d(t,f)/S_P(t,f)=A_Q^d(t,f)/S_Q(t,f) wherever survivor mass is nonzero. Define a single z-policy using these stop hazards and residual continuation probability. If the survivor mass is zero, the state is unreachable under both positive laws and its action can be defined arbitrarily. At the root use the original root action.

Induct in t: immediately after the root the survivor masses match for each first bit under each law. At all later times the z state f does not change, and survivor mass at (t+1,f) equals survivor mass at (t,f) less the two stop-decision masses. If masses match before a z action, the common hazards match the original stop masses and thus the next survivor masses. Hence all A_L^d(t,f) match under both L, for every time and decision. This proves exact equality of (T,first(H_T),D) for ALL full-history policies. By the lifting lemma this is also an x-adapted policy. The proof uses no exhaustive policy enumeration.

### Nonetheless refined x fails strong lumpability

Histories 001 and 010 have identical x=(3,0,2), but from 001 the probability of next x-state (4,0,3) is 3/4, while from 010 it is 1/4; these values hold under P AND Q. Thus SL fails for x, despite universal preservation of the declared coarser observer.

The gap is genuine rather than merely definitional. Consider the full-history policy that continues everyone through t=3, then continues ONLY prefix 001; everyone else stops with decision B at t=3. At t=4 it chooses A exactly when the last symbol is 0, otherwise B.

At t=3, 001 and 010 each have P-mass 1/8 and Q-mass 1/12. Any x-policy matching the FULL terminal joint law (T,x,D) must continue everyone before t=3 (the original had no earlier terminal events), must stop at all other t=3 x-states, and must continue with probability precisely 1/2 at x=(3,0,2). Otherwise its observed t=3 B-mass in that x-state differs. So its ENTIRE t=4 arrival mass into child x=(4,0,3) is forced to be

    P: (P(0010)+P(0100))/2=(3/32+1/32)/2=1/16.
    Q: (Q(0010)+Q(0100))/2=(1/16+1/48)/2=1/24.

The original t=4 decision-A mass in that x-child equals P(0010)=3/32 and Q(0010)=1/16. No x-policy can decide A more often than its total arrival mass, leaving exact positive gaps

    P: 3/32 - 1/16 = 1/32.
    Q: 1/16 - 1/24 = 1/48.

This proves full-x universal preservation FAILS although coarse-observer universal preservation HOLDS. Under the successful z-policy for this witness, at (t=3,first=0) stop B with 3/4 and continue 1/4; at (t=4,first=0) decide A with 3/4 and B with 1/4. The coarse event (t=4,first=0,D=A) then has exactly P-mass 3/32 and Q-mass 1/16.

## 3. Computation, BRC scope, open question

Local Python standard-library Fraction checker enumerated 31 prefixes of length <=4, proved positive normalized P/Q masses for this finite example, checked every z-fiber LR, both unequal transitions inside x=(3,0,2), the full-x forced discrepancies, and the entire (T,first,D) joint law under P and Q for both an isolating deterministic history policy and a non-symmetric randomized history policy. All assertions passed. See VERIFY.py and RESULT.json; **two sample policies are evidence for the witness, not the proof of the universal quantifier** (which is the above induction).

BRC branch population is the full ordered-prefix tree with strictly positive rational P/Q weights, and allowed actions are continue/stop/decide. We keep ordered branch identity until proving sufficiency for the precise future operator and observer; 001 vs 010 remains a meaningful residual for the richer x readout. This is NOT a signed/complex BRC cancellation result.

This is an external finite probabilistic auxiliary model. It supplies NO typed bridge to native Heartbeat X6 Cell incidence, six-dimensional spatial coordinates, separately typed time, the three-dimensional native slice, any P000 dynamical rule, or physics. No mathematical acceptance, independent Driver review or Lean checking is implied by GitHub publication.

**Next mathematical unit:** an exact characterization of universal two-law (T,o(x_T),D) preservation when o is coarser than x and no intermediate strongly-lumpable z is assumed. In particular determine whether LR constancy on x-fibers remains necessary, accounting for compensation among different x-states sharing an observer class. Retain universal quantifier order, common policy under both laws, and the declared terminal readout.
