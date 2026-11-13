# EC48R — H5 positive BRC observation trees with two nontrivial intermediate widths

Scientific predecessor: EC48Q in research_notes/r4_ec48q_h5_k1_width_20261028 (this PR); EC48P PR #1581 at a569913b3cc267ab571db7f552e63878eb3c6895; EC48O PR #1578 at 20eb4f35105908f403d631608657d7973bd604ee. All are author-side/unreviewed pending independent review and native admission.

## Frozen EC48Q result, do not reprove as the sole contribution

In a finite strictly positive two-source horizon-5 stopping observer, stage 1 and stage 2 each have exactly one common observable history, stage 3 has l global histories and stage 4 has arbitrary finite conditional signals, terminal at stage 5. Registered controller updates BEFORE each stage action using old register, current signal, time and joint-prefix likelihood ratio; source-independent private randomness, no shared public seed or hidden history read. For O=(Paccept,Qaccept,E_PT,E_QT), preserving the entire RAW set for every tree requires and is guaranteed by max(l,2) memory states. l>=2 positive rational witnesses have exact support gap c/(2*l*ceil(log2 l)) for every real 0<c<=1/32; the 14-leaf l=3 instance at c=1/32 has V_F=7/192, V_2=13/384, gap 1/384. There is also a three-leaf l=1 counterexample to one-state sufficiency. Proof and reproducible exact verifier are in this PR.

## New question

Allow stage-2 width k>=2 and stage-3 *global* history width l>=k, with two genuinely branching intermediate levels. Is max(k,l,2) states always enough to preserve every RAW 4-vector, or can history/register dependence from successive decisions require more? Clarify that l is a count of global (h,j) histories, *not* per-branch fanout, current signal alphabet size or LR fiber count. If negative, build a strictly positive rational separator and complete deterministic controller normal form; if positive, build a full policy-by-policy joint P/Q fiber factorization preserving four coordinates, including update timing and surviving histories.

Begin with k=2,l=4, H5: seek stage-4 LR collisions between histories with different continuation and terminal information patterns, including independent changes at stage 2 and 3. Explore whether multiple successive overwrite-to-stop/continue operations remain safe, rather than treating support-value equality as RAW equality.

## Acceptance and provenance

Preserve exact positive P/Q mass normalization, source-independent randomization and current joint likelihood ratios; provide explicit full observer and registered control rules. Either a complete analytical theorem with precise limitations, or rational infeasibility certificate plus executed verifier, or a source-backed negative result. Do not conflate k,l definitions. Retain EC48Q/EC48P/EC48O source pins, classify any inherited lemma as unreviewed, record reproducible code/exact outputs and the next discriminating problem. Project native P000 and ACTIVE six-axis X6 ontology remain fixed; no X6 lifting without a typed joint-relation and future-operation preserving map. Canonical Source/Owner/CLAIM and Driver mathematical acceptance require separate current authority checks.
