# Stage491-B — Relative-end SET: exact reachable-neighborhood repair and a two-step counterexample

Status: AUTHOR-SIDE MATHEMATICAL PROOF + EXACT FINITE EXECUTION; UNREVIEWED / NOT ADMITTED.
Parent: Stage490-B in draft PR #1736, commit 98a89255c6413980ed06cd1ba8838c329d5d59c4.
Frozen scientific pins (unchanged): global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; enterprise-math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.
Current normative context separately refreshed, global main 0b7e5cf45d2297a00c7d6198bc5519f77f378876, EM main 731eb24885993ab70e9b64c855048293409f85b5.

## Theorem 491.1 — bounded append-first moving edit

Let D be twelve distinct signed native X6 unit directions. Two ordered histories have the same fixed P and initial Q length n. Their observations at each step are (lengths, signed six-component displacements, all 144 ordered edge counts, K=overlap-position equality count). Their legal public base actions are finite POP and APPEND(z), with identical labeled traces and parameters. Let ~0 mean exact equality under ALL legal no-SET base traces.

Extend the action grammar by at most one Q_SET_FROM_END(d,z), setting the direction at one-based index j=|Q|-d. Before this SET, Q may perform t public APPENDs for any t in 0,...,b but no Q POP; after SET, any remaining legal base POP/APPEND may be interleaved. An unedited trace may perform all legal base operations. Assume d>=2, b<=d-1, and J={n+t-d:0<=t<=b} lies in the ORIGINAL interior 2,...,n-1 and strictly after every P length permitted by its fixed base budget. All initial Q lengths and fixed P words agree.

Then the enlarged complete future equivalence is precisely

  (P,Q1) ~move (P,Q2)
   iff (P,Q1) ~0 (P,Q2)
   and tau_j(Q1)=tau_j(Q2) for every j in J,

where tau_j(Q)=(Q[j-1],Q[j],Q[j+1]) in one-based coordinates. In other words, the repair is the UNION of the original one-step neighborhoods of every dynamically reachable edit site, rather than the triple at the initial site alone.

Proof (necessity): The no-edit sublanguage gives ~0. For each t, issue t identical public APPENDs then SET at j=n+t-d. Because j<=n-1, the site and both neighbors are original, unaffected by the append prefix. Compare the resulting signed displacements for all twelve replacement symbols: v(z)-v(center) identifies the old center (the twelve v(center) are pairwise distinct). Choose a replacement z different from the old center and the four possible neighboring letters (at most five excluded, twelve available). In the ordered-edge change, the two z-incidence terms [left,z]+[z,right] identify left and right separately. Hence the two original triples agree.

Proof (sufficiency): Delete SET from a selected enlarged trace to obtain an identical legal base reference trace. By ~0, reference observers agree at every time. Prior to SET, public append-only actions leave its original neighborhood unchanged. The signed displacement correction is v(z)-v(center); its ordered-edge correction is -[left,center]-[center,right]+[left,z]+[z,right], determined by the corresponding tau_j. Later POP/APPEND operations can erase the edited site, replace a trailing neighbor by a known appended direction, or leave the site intact: all corrections relative to the matching base trace remain functions of tau_j and public actions. By the lower bound on j, edits do not modify K against P at any step. Thus all enlarged observations agree.

This is a sufficiency/exactness statement for a specified bounded grammar, not an assertion of minimal independent coordinate count in every fiber. POP before an edit, repeated edits, and index-shifting interior INSERT/DELETE are next cases.

## Strict minimal-length trace against the old fixed-site repair

Take T=P=ABGABA, W=GH, Q=T W A H A, D=A..L with G=-E1 and I=-E3, H1=AAAABA, H2=AAABAA (u=6). Both Q have length 16 and the same complete initial observer, same full no-SET future observer for Q POP<=1 and APPEND<=1, and identical triples at fixed sites j=10 and j=11 (the Stage490 sites). Their initial moving offset d=5 targets j=11 with triple AAA in both.

Immediately editing at end-5 (j=11) by I yields equal observations. One public Q_APPEND(C) shifts the moving target to j=12 while preserving the observer. The next Q_SET_FROM_END(5,I) distinguishes: H1 has tau_12=AAA, H2 has tau_12=AAB. Edge corrections are respectively -2[AA]+[AI]+[IA] and -[AA]-[AB]+[AI]+[IB]. Their difference is -[AA]+[AB]+[IA]-[IB], a nonzero 144-coordinate vector. This is the shortest distinguishing trace in the declared Q grammar: no base-only trace and no initial immediate moving SET distinguishes these histories.

## Exact BRC support/population experiments

With H over {A,B,G,H}^6 (4096 distinct raw histories), T,W fixed and both P and Q base POP/APPEND budgets <=1: initial ordered-edge fibers = 1202, complete base-equivalence keys (edge multiset, H[-1]) = 1973; base plus fixed sites 10,11 = 3904 classes. Moving d=5 without preappend = 3904 classes; with up to one preappend = 4096 classes.

For H over {A,B,G,H}^7 (16384 raw histories), the moving key has 15952 classes, including 432 non-singleton classes. A nontrivial same-class example is H1=AAAAABA, H2=BAAAAAA. An exact oracle checked 10368 post-SET observer comparisons for all 12 replacement symbols, both public preappend schedules (0 or 1 of C), on these non-singleton classes. A complete paired Q-trace simulation (one APPEND, one POP, one moving SET; all twelve symbols; POP-before-SET forbids subsequent SET) visited 481 reachable paired states for this representative pair; all observers agreed. P is common and has at most 1 POP/APPEND, hence P length <=7 and cannot overlap the edited Q indices here.

Carrier discipline: population is the full raw word set, Boolean support is separate from integer class population, and direction order and all 144 edge types are retained before the justified quotient. The statistics are exact integer counts on the declared finite model; no empirical claim about physical dynamics or canonical P000 theorem admission is made.

## New INSERT/DELETE locality identity

For an interior boundary a|b, inserting signed direction z changes the edge vector by -[ab]+[az]+[zb] and adds v(z) to displacement. For a single interior deletion of letter c from a c b, the edge change is -[ac]-[cb]+[ab] and displacement changes by -v(c). An insertion before old original position j transports that original position to j+1; deletion transports surviving later positions back by one. These exact identities motivate a trace-dependent address-transport automaton rather than a static triple list when interior indices shift.

## Validation and next unit

Portable standard-library executable REPRO_STAGE491B_PORTABLE.py and its actual executed stdout are stored alongside this proof. Full independent author-run script and JSON evidence are preserved as local task artifacts. No native Source CLAIM/Result or independent Driver admission is implied. Native Site status on this turn: BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false; authenticated Owner remains unconfirmed.

Stage492-B: permit one Q POP BEFORE the moving SET, or one interior INSERT/DELETE before SET; compute reachable original-neighborhood vs public replacement provenance and look for the smallest failure of a naive fixed-J signature. Separately seek sparse Euler-BRC ranking without enumerating the full active-edge state space.
