# S23/AV follow-up: exact full horizon-510 saturation N(510)=2,455,069

Date: 2026-11-08 Asia/Shanghai. Status: AUTHOR_SIDE_EXACT_THEOREM (analytic one-gap lower bound + complete finite upper certificate); independent mathematical review pending.
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Precursor: PROOF.md in this directory at commit 983218d0cf889cd50d0d5fd4a48eba5c81c38555.

## Theorem (exact saturation, not only a lower bound)

For the two-point S23/AV finite-future likelihood-sign observer defined in PROOF.md, with T_h={10^i/7^s:0<=i<=s<=h} and N(h) the minimum padded prefix length hitting **every** open threshold cell,

  N(510)=2,455,069.

The one missing cell at prefix length 2,783 is J_0=(10^431/7^510,1). Its exact first-entry prefix has joint counts (k,ell)=(2,074,774,380,295), length 2,455,069. Every other open threshold cell of T_510 already has a prefix of length <=2,783.

This stronger statement closes the previous open equality question for h=510, while retaining the infinite family of exact first-entry bounds and 379,864 consecutive non-tail horizons proved in PROOF.md.

## Proof: lower bound

The earlier determinant-one lattice proof establishes that J_0 cannot be entered before n=2,455,069 and has a witness precisely at n=2,455,069. Thus N(510)>=2,455,069.

## Proof: certified finite complete covering of every other cell

Use r=ln7/ln(10/7)>0, and represent threshold ratios in the reflected log coordinate t_(v,k)=r*v-k for integers v,k>=0, v+k<=510. There are M=(511*512)/2=130,816 **distinct** thresholds; distinctness follows from the multiplicative independence of 7 and 10 and is independently certified by the strict sorting inequalities.

A prefix of k copies of label 1 and ell copies of label 4 has log-coordinate E=k-r*ell. It enters the threshold cell with endpoints t_left<t_right precisely when t_left<E<t_right. The two outer open cells are handled with their one-sided inequalities. Label 3 permits padding.

The companion source VERIFY_N510_FULL_SATURATION.py constructs a *rigorously enclosed* value of r, using only rational arithmetic:

  5.45569623581288298975349314 < r < 5.45569623581288298975349315.

The interval is certified from the absolutely convergent atanh expansion
  2*atanh(z)=2*SUM_(j>=0) z^(2j+1)/(2j+1)
and a finite remainder bound 2*z^(2N+1)/((2N+1)*(1-z^2)), with z=1/3, 1/9, 1/15 and N=45. In particular,
  ln7 = 3 ln2 - 2 atanh(1/15),
  ln(10/7)=2 atanh(1/9)+2 atanh(1/15).
All bounds are implemented with Python Fraction; no floating-point logarithm is used.

For each of the 130,815 adjacent sorted pairs, the verifier checks the *strict exact ordering* by the appropriate rational enclosure endpoint. The sorted consecutive thresholds t_(0,0)=0 and t_(79,431)=79r-431 identify the exceptional cell J_0 at index 20,440 in the reflected-coordinate ordering.

For every OTHER cell (including both outer cells), the verifier searches prefix counts with k+ell<=2,783. Each offered candidate uses the rational lower-bound key only to locate a possible cell; **before marking it**, the actual strict inequalities are certified at the adverse rational enclosure endpoints:

  E > (r*v_left-k_left) follows from
  (k+k_left)*Q > hi*(ell+v_left),

  E < (r*v_right-k_right) follows from
  (k+k_right)*Q < lo*(ell+v_right),

where Q=10^26 and lo/Q<r<hi/Q. The relevant one-sided test is used for an outer cell. These exact integer inequalities establish every witness in its intended interval despite the irrational r.

The program finds certified witnesses for **all 130,816 other open cells** at total prefix lengths <=2,783, with ell<=147; only the known J_0 interval remains unmarked. This finite domain is complete: the 130,816 threshold points and 130,817 open cells are all enumerated and the program checks the marked-cell count and unique missing index. It need not exhaustively enumerate all prefix sequences, because one rigorously verified witness per cell proves the desired upper bound.

Thus by padding each of these witnesses with label 3 to n=2,455,069 and using the exactly minimal J_0 witness, every open cell is occupied by a prefix of that length. Hence N(510)<=2,455,069. With the earlier lower bound, equality follows. QED.

An additional sharp observation: the extreme **right** reflected cell t>510r requires k-r*ell>510r, hence k>510r>2782 and thus k+ell>=2783. Therefore 2,783 is the least length that can fill every non-J_0 cell simultaneously; it is not an arbitrary overestimate.

## Execution evidence and scope

Exact local execution produced:
- a certified rational interval for r with Q=10^26;
- 130,815 pairwise strict integer ordering checks;
- identified exception index 20,440;
- 130,816/130,816 nonexception cells supplied with certified strict integer witnesses, ell<=147;
- final assertion PASS_N510_EXACT_EQUALITY: N(510)=2455069.

Full executable source: VERIFY_N510_FULL_SATURATION.py; actual stdout: RUN_N510_FULL_SATURATION.txt. The finite certificate uses deterministic standard-library Python Fraction and integer arithmetic; large-n exclusion rests on the analytic determinant-one theorem in PROOF.md.

This is precisely the two-point S23/AV **auxiliary** future likelihood-sign observer, not the full-lawful TV deficiency delta_n or the original six-source/ten-label mother model. All P000, frozen science, and provenance scopes are preserved. Native Source role CLAIM/Research-Activity remain unconfirmed due to backend STATUS_DATABASE_UNAVAILABLE; independent reviewer acceptance is pending.

Next: determine exact N(h) for further scaled h (e.g. h=511,535); develop a general all-cell covering theorem, exploiting rational logarithm enclosures and determinant-one near-resonance pairs. Continue full-lawful delta4 and mother-model source/time bridge as independent research questions.