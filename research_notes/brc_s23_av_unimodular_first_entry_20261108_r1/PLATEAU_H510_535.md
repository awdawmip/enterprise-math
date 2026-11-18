# S23/AV: exact 26-horizon plateau N(h)=2,455,069 for h=510..535

Date: 2026-11-08 (Asia/Shanghai). Status: AUTHOR_SIDE_ANALYTIC_LOWER_BOUND + FINITE_EXACT_UPPER_CERTIFICATE; independent mathematical review pending.
Frozen scientific pin: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Dependencies: PROOF.md (unimodular base-gap first-entry theorem), FULL_SATURATION.md (the h=510 complete upper-certificate method) in this research note directory. No change of the two-point S23/AV auxiliary observation model.

## Theorem: exact constant N over 26 consecutive future horizons

For every integer h=510,511,...,535, the first prefix length whose attainable two-point likelihood ratios hit EVERY open threshold cell of T_h is

  N(h)=2,455,069.

This strengthens the previously exact h=510 result to an entire 26-horizon plateau and gives a concrete minimum-complete-memory phenomenon under the declared future likelihood-sign observer. In particular, for h=535, the old strict lower bound 20,001 is improved to the exact value 2,455,069.

## Proof: one uniform analytic lower bound

Let r=ln7/ln(10/7), eps=79r-431 and d=2074774-380295r, with 0<d<eps certified by exact integer powers in PROOF.md. The integer lattice basis (v,k)=(79,431),(380295,2074774) has determinant one. PROOF.md proves the prefix cell J0=(10^431/7^510,1), equivalently the reflected log-coordinate gap (0,eps), has first-entry length n*=2455069.

For every h=510,...,535 the endpoints (0,0) and (79,431) remain neighboring points of the reflected threshold set {r*v-k : v,k>=0,v+k<=h}. This is independently checked in the executable upper-certificate proof below. Thus the *same cell* remains open and requires n>=n* for complete coverage:

  N(h)>=2455069.

## Proof: exact complete upper certificate for all h=510..535

Let t=h-510 (0<=t<=25) and write t_(v,k)=r*v-k in the reflected threshold coordinate. Any ordered pair of endpoints

  t_(v0,k0) and t_(v0+79,k0+431),   v0,k0>=0, v0+k0<=t,

differs by eps>0. The verifier proves EVERY such pair is adjacent in T_h's reflected ordering. There are exactly (t+1)(t+2)/2 of these designated small-gap cells, including base gap at v0=k0=0.

Each designated cell has an explicitly constructive prefix witness with

  (k,ell)=(2074774-k0,380295-v0).

Both counts are nonnegative for 0<=t<=25. Its reflected prefix coordinate is

  E=k-r*ell = d+(r*v0-k0),

which lies strictly between the designated endpoints because 0<d<eps. Its total non-label-3 length is n*-(v0+k0)<=n*. The verifier also certifies the two strict inequalities against its rational log bounds for EVERY designated gap.

For all OTHER open threshold cells, the verifier explicitly finds a prefix with k+ell<=4000, simultaneously at each h in this finite interval. It uses the rigorous exact rational enclosure

  545569623581288298975349314 / 10^26
       < r <
  545569623581288298975349315 / 10^26,

proved solely by Fraction-based finite atanh series and rigorous tails (see FULL_SATURATION.md). Sorting of all M_h=(h+1)(h+2)/2 threshold points is certified by strict adjacent integer inequalities. Candidate witness selection may use the lower rational key for speed, but its actual membership in a cell is accepted ONLY after the adverse-endpoint integer inequalities

  (k+k_left)*Q > hi*(ell+v_left)
  (k+k_right)*Q < lo*(ell+v_right)

hold (omit the irrelevant comparison at an outer cell). Here lo/Q<r<hi/Q and Q=10^26. The complete set of M_h+1 threshold cells, including the two outer cells, is independently enumerated for each h.

Every execution from h=510 through h=535 passed the complete all-cell coverage check: the only unmarked cells of the short-prefix search were precisely the explicitly covered designated small-gap cells. The final horizon h=535 has 143,917 threshold points (M_535=(536*537)/2=143,916, so M_h+1=143,917 open cells); 351 designated cells and 143,566 other cells were covered. At h=510, there are 1 designated and 130,816 other cells. Full stdout lists all 26 h and counts.

Thus every open cell at each h<=535 has a witness of length <=n*=2455069. Label 3 has likelihood ratio 1 and permits padding to the same length. Together with the analytic lower bound, N(h)=n* for all 26 horizons. QED.

## Verification and scope

Actual code: VERIFY_H510_535_PLATEAU.py. Actual full log: RUN_H510_535_PLATEAU.txt. The program runs Python 3 standard-library big integers and Fraction only; no approximate floating-point evidence. It checks all threshold orderings, all special gap adjacencies and explicit witnesses, then the existence of integer-certified witnesses for EVERY other cell. The universal large-n exclusion is the already stated analytic unimodular theorem, while h is finite (510..535) and exhaustively enumerated.

This is an author-side mathematical proof for the two-point S23/AV likelihood-sign future observer. It is not the full-lawful minimax TV deficiency delta_n, nor a full six-source, ten-label S23 mother-model bridge, nor a native Heartbeat X6 physical experiment. Current P000, source firewall and scientific pin remain unchanged. Native authenticated Owner/CLAIM/Research-Activity and independent review remain unresolved.

Next: identify the first horizon h>535 with N(h)>2455069, or extend the plateau via the same exhaustive certificate; derive a general exact upper-bounding theorem that replaces finite horizon scans. Keep full-lawful delta4 and lawful original mother-model mapping as independent next research tracks.