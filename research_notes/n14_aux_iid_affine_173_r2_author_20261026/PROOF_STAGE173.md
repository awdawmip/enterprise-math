# Stage173: exact full-real minimax interval, with terminal-randomization saturation

Status: AUTHOR_EXACT / EXTERNAL_N14_TERNARY_IID / NO_NATIVE_CLAIM / NOT_ADMITTED.

## Exact source and model

GLOBAL_KNOWLEDGE_V1 frozen main: 32303b81b21f488a745aa9af6a05aaef150cf33d. Enterprise Math frozen main: b03d306acf9763f8db33e09d9fd434f35e4640fd. P000 startup projection canonical blob matched the P000_REALITY_FOUNDATION.json blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. ACTIVE worldview and current portable research/ordinary control policies were read. Predecessor Stage172 complete external author packet: immutable commit bd3287d76bf71a967c69a1f1a4fca6275b805f05, specifically its proof, actual verifier, certificate and dual173 candidate.

Fix P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), IID ternary words of at most N=14 observed symbols. Allowed sequential randomized decisions may depend on FULL ORDERED HISTORY. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau); minimize V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha. Compactness of the finite policy space guarantees attainment.

## Theorem: strictly shorter interval than a whole coin sweep

At K173=L173=451080/1909, let S173=902160/1909 and Bellman root H173=9224707194483683711431/52288007441574002688.

Previous endpoint:
alpha172=220608887064170557255/632523287505640882176,
V172=1047792388565411809841/90360469643662983168.

New saturation z*=406062589150005409/409600000000000000, width
Delta173=750324145848852691/13493830133453672153088, and new endpoint
alpha173=611493515114730101/1752976676930715648,
V173=1267557322258081771/109561042308169728.

For ALL REAL 0<=delta<=Delta173,
  V14(alpha172+delta)=V172-(902160/1909)*delta.

For alpha>alpha173 in the value-function domain, the same affine support line H173-(902160/1909)*alpha is STRICTLY below V14(alpha). This is sharpness of the particular support line, not a claim the value function terminates.

## Exact dual proof for all history-dependent policies

For each ordered prefix with count state s=(n,a,b), where a/b count letters 0/1, likelihood ratio Q(prefix)/P(prefix)=ell(s)=2^(a+b)/3^a. Its P-weighted Bellman terminal action costs are K*ell(s) for deciding P, L for deciding Q, or 1+sum_i P_i h(child_i(s)) for continuing if n<14. The exact rational suffix recursion covers sum_{n=0}^{14} C(n+2,2)=680 states, with H173 above, 1238 strictly positive gaps (minimum 8039/309258), and exactly two ties: R=(10,0,1) Q/continue; Z=(14,0,0) P/Q. Every other action is strictly inferior.

Induction at EACH ORDERED PREFIX proves H173<=tP+K*eQ+L*eP for every full-history strategy; count grouping is just an algebraic computational speedup. Thus all feasible policies satisfy
  max(tP,tQ)>=tP>=H173-(K+L)*alpha.

## Exact primal witness, including the nontrivial feasibility boundary

At R choose verdict Q with probability r, otherwise continue; at Z choose verdict Q with probability z, otherwise P. Else choose the unique Bellman minimizer. R's paths have one letter 1, while Z has no letters 0 or 1, so their first-hit cones are disjoint. First-hit R: 10 labeled histories, P-mass 9765625/120932352 and Q-mass 9765625/60466176. First-hit Z: one history, P=Q=6103515625/78364164096.

A Fraction suffix recursion and a separate unmerged labeled-history integer-numerator DFS returned identical (eP,eQ,tP,tQ) at every deterministic corner (r,z)∈{0,1}²; branch numerator/denominators were P:(3,1,20)/24 and Q:(1,1,10)/12. Both terminal measures have mass one. DFS node counts by corner (00,01,10,11) are 286156,286156,285916,285916: 1,144,144 total. The mixed term M11-M10-M01+M00=(0,0,0,0).

Consequently M(r,z)=M00+r*dR+z*dZ exactly, with four-observable increments
  dR=(4521484375/1486016741376,
      -3232421875/1253826625536,
      -61181640625/557256278016,
      -20751953125/104485552128);
  dZ=(6103515625/78364164096,
      -6103515625/78364164096,0,0).

Solving eP=eQ gives the UNIQUE affine relation
  r(z)=420842109150005409/14779520000000000-(640000/23093)*z.

Legal coins are NOT the naive whole [0,1] z-range. The exact feasible balance segment is z*<=z<=1: r(1)=11242109150005409/14779520000000000>0, r(z*)=1. In contrast, r(0)>1 is an exact obstruction to a full z sweep. Along z descending from 1 to z*, the common error strictly increases from alpha172 to alpha173 with positive width Delta173. The P-expected stop time decreases from V172 to V173. The differences tP-tQ are positive at both endpoints:
  at z=1: 234844840446617153803/632523287505640882176;
  at z=z*: 43007218367498219/109561042308169728.
All observables are affine in z; thus both error balance and tP>=tQ hold for every real intermediate z. At both endpoints, and hence throughout, exact dual equality tP+K*eQ+L*eP=H173 holds. That proves universal primal-dual equality over the entire stated real alpha interval.

## Right support sharpness

If for alpha>alpha173 equality V14(alpha)=H173-S173*alpha held, compactness yields an optimizer. Equality of all steps forces tP>=tQ, eP=eQ=alpha (K,L>0), and only Bellman-winning actions at every reached prefix. There are precisely two ties, at R and Z. Within each tied count-state fiber the Q/P prefix likelihood ratio is constant, and subsequent strict actions are unique; averaging the history-specific tie probabilities against P-prefix mass therefore preserves all four observables. R and Z first-hit cones are disjoint, allowing reduction to effective r,z∈[0,1]. Error equality then forces precisely r(z) above, and its feasible z range forces alpha<=alpha173. Contradiction.

## Boundary and reproducibility

The local executed full verifier and Stage174 scanner appear in the downloadable accompanying portable author package. The GitHub reference checker is self-contained and recomputes the essential exact certificate; remote Git blob readback is storage proof, not remote execution. Stage174 has a dual-only candidate; no primal theorem or independent review has been asserted. BRC reuse consists of labeled path/branch provenance, distinct positive P/Q masses and honest residual observer scope; not native typed physical BRC–Shor computation. No P000 X6 embedding, native three-dimensional slice, native dynamics theorem, Lean formalization, Driver acceptance, or original task CLAIM follows from this result.
