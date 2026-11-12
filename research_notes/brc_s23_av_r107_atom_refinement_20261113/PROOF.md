# R107 — Exact historical atom refinement, shared-addition leases, and an explicit-output lower bound

Date: 2026-11-13 (Asia/Shanghai). Parent R106 immutable scientific frontier: `4f76a79dd7878573dd618728a6986d6d8d396865`. Frozen scientific input pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Model

This is the finite rational directed-circle auxiliary source model of R104–R106, not a claim about unbridged native X6 dynamics. Each source has complete integer identity (u=(t,branch)), descending lexicographic rank. Fix (sigma=(j,x,a,b)), (j,a,binmathbb Z), (xinmathbb Q), (kge1), and rational (I=[L,U]), (L<U). At real (	heta), (M_u(	heta)) means that ({x+(t-j)	heta}) is in the directed half-open circular arc from ({a	heta}) to ({b	heta}); coinciding endpoints mean the empty arc. (operatorname{Top}_k(F,	heta)) is the descending ordered list of up to (k) eligible identities.

For finite source set (V), let (K(V)) be (L,U) together with all integer-crossing points in (I) of the six rational affine forms (a	heta), (b	heta), ((t-j)	heta+x), ((t-j-a)	heta+x), ((t-j-b)	heta+x), ((a-b)	heta), for each ((t,branch)in V). Each open gap between adjacent points has constant membership for every identity in (V); singleton cutpoints are checked separately. Rational midpoints provide exact witnesses for gaps.

## R107.1 — Hereditary refinement theorem

Given finite old (F,G), set (V=Fcup G), (C=Fcap G), (Delta=F	riangle G). Suppose an exact old certificate uses a sorted cut list (Tsupseteq K(V)), with for each (uinDelta) and old atom (J) either OUT or the complete guard incidence fiber

[
S_{m old}(u,J)={vin C:v>u, M_v(	heta)}.
]

For arbitrary finite edited versions (F',G'), put (V'=F'cup G'), (C'=F'cap G'), (Delta'=F'	riangle G'), and

[
T'=Tcup K(V'setminus V).
]

Then (T') is a valid exact atom cut list for (V'). If (r=|T'setminus T|), the total number of singleton-and-gap atoms increases by exactly (2r).

Every new atom (J') lies in a unique old atom (P(J')). For a retained discrepancy (uinDeltacapDelta'), old OUT remains OUT; otherwise the exact new incidence fiber is

[
S_{m new}(u,J')=
  (S_{m old}(u,P(J'))cap C')
  cup
  {vin C'setminus C:v>u, M_v(	heta_{J'})}.
]

For (uinDelta'setminusDelta), evaluate eligibility and higher eligible common identities in (C') directly at the rational atom representative (	heta_{J'}). Then

[
orall	hetain I,quad
operatorname{Top}_k(F',	heta)=operatorname{Top}_k(G',	heta)
]

if and only if **every active discrepancy fiber on every new atom has size at least (k)**. A smaller fiber supplies an exact rational mismatch witness.

**Proof.** Sources in (V'cap V) were covered by (T); sources in (V'setminus V) contribute all new critical points through the union. Every membership is therefore constant on each new open gap. The source identity of a retained discrepancy is unchanged, so its OUT/IN predicate is inherited from its containing old atom. The higher common identities surviving from (C) are exactly the old guard fiber intersected with (C'); all additional common identities belong to (C'setminus C) and are tested separately. The newly discrepant rows are evaluated from (C'). The R104 pointwise rank-shield equivalence proves the asserted iff, and the atom representative proves the witness. Inserting an interior cutpoint splits one old gap into open gap, point, open gap, increasing the count by two. QED.

**Representation scope.** The supplied implementation holds immutable historical versions and reuses unchanged guard-fiber objects. It copies the new row arrays, with up to (O(|Delta'|,|T'|)) row entries. It does not claim a logarithmic-time balanced-DAG update; complete rational bit-operation and historical-memory costs remain part of the next performance comparison.

## R107.2 — Zero-refinement equality lease

For finite (F,G,H), every (	heta), and (kge1),

[
operatorname{Top}_k(F,	heta)=operatorname{Top}_k(G,	heta)
Longrightarrow
operatorname{Top}_k(Fcup H,	heta)=operatorname{Top}_k(Gcup H,	heta).
]

Consequently, a complete interval equality certificate remains sound after arbitrary **common additions** to both versions, without calculating any new phase cutpoint or guard fiber. (H) may contain an identity previously discrepant in one version.

**Proof.** For any finite (S,H), (operatorname{Top}_k(Scup H,	heta)=operatorname{Top}_k(operatorname{Top}_k(S,	heta)cup H,	heta)): each eligible (S)-identity discarded from (operatorname{Top}_k(S)) is dominated by (k) eligible (S)-identities, which remain available after adding (H). Equal initial lists thus produce equal updated lists. Apply independently to every real (	hetain I). QED.

An immutable *equality lease* may refer to the old full certificate and the new versions. Such a lease certifies equality but is not a refreshed exact guard incidence table. Before a later edit uses depleted guard counts to claim inequality, materialize or validate the newly relevant identities and phase cuts. A formerly unequal pair can become equal under common addition, so equality preservation is an implication rather than a two-way characterization.

## R107.3 — Exponential binary-input gap for explicit atoms

Set (sigma=(0,1/4,0,1)), (I=[1/4,3/4]), (k=1). Begin with empty (F=G). For any integer (Tge4), insert (u_T=(T,0)) into (F) alone. Its eligibility has (Omega(T)) distinct transition points within (I), although (T) is encoded in (Theta(log T)) bits.

**Proof.** Each integer (n) for which (	heta_n=(n-1/4)/Tin(1/4,3/4)) gives source phase ({1/4+T	heta_n}=0), while the arc is ([0,	heta_n)); hence the source is IN. For (arepsilon=1/(64T)), immediately to the left its phase equals (63/64>	heta_n-arepsilon) (OUT); immediately to the right it equals (1/64<	heta_n+arepsilon) (IN). There are (Omega(T)) such distinct transitions. Any explicitly enumerated constant-Top-1 atom representation must resolve them. A direct point membership query can instead evaluate the symbolic phase without enumerating every transition. QED.

This identifies a concrete regime favoring equality leases or demand-driven symbolic queries over eager global atom expansion.

## Exact validation

The independently executable Python `check_r107.py` uses `fractions.Fraction` exclusively for the mathematics. It constructs 34 seeded initial histories and performs 374 historical branching edits: 10 positive equality leases and 364 exact refinement updates. It checks complete source memberships and guard fibers against direct scans at 28,952 rational atom representatives, verifies boundary singleton (	heta=3/4), immutable branches, and lower-bound tests at (T=N+1) for (N=7,31,127,255).

Terminal output: `R107_PASS 374 10 364 28952 4`. Full counters in `verification_r107.json`. These tests check the implementation on finite instances; the universal claims are proved above.

## Frontier

Independent author-side R107 result. Formal Source task/owner, Researcher Activity, shared CLAIM, Result and independent review require their separate actual receipts. Scientific input remains the exact frozen pin above.

R108: build persistent balanced interval-DAG nodes with demand-driven splits and retain equality leases; measure exact phase generation, rational bit lengths, cache updates, old-version memory and witness restoration against R103 net overlay and complete materialization. Compare the (Omega(T)) adversarial family under sparse and dense point-query workloads.
