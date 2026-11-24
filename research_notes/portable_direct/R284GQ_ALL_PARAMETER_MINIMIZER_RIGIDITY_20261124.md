# R284GQ — Complete minimizer histogram classification and compulsory crossing block

2026-11-24. Informed portable continuation of the frozen auxiliary four-phase binary fixed-tag model, author analytic proof plus exact SMT, NOT_REVIEWED. P000 / ACTIVE worldview unchanged; auxiliary residual-incidence computation, no native physical attribution. Original own registration r1-20261124-0256-r284gd-session-v1 SUCCEEDED, session MCP-8cd6c4fa26b9459d923ff73ba0082220 recovered by metadata read, Researcher EM-DIRECT-0C386E, RA-B82240E8488EF5A1DA5186C4. Owner router r1-20261124-1400-owner-read SUCCEEDED (read snapshot Source 4567d55f522ff9e565f6d5bf4cac825d6b39e5cf, observed 2026-11-24T06:04:06Z); it recommended a different task, not a claim. This continues the existing independent R284 problem; no shared task mutation.

Frozen sources:
- GL @5f74ba8a545788cc3fdb080f9953bbe5a0926531:research_notes/portable_direct/R284GL_ASYMMETRIC_THREE_PATTERN_SHARP_CAPACITY_20261124.md (exact prefix distances, lower-bound cases).
- GM @a06ff527a1494a6a61b6964f9a753bcb35ab7433:research_notes/portable_direct/R284GM_GLOBAL_LOW_OMISSION_SHARP_CAPACITY_AND_RIGIDITY_20261124.md (low-omission classification, source groups).
- GP @4b5d6d5a9a0fc6d775273ad557b66cd06fb10567:research_notes/portable_direct/R284GP_CLOSED_CROSSING_AND_ALL_PARAMETER_SHARP_CAPACITY_20261124.md (capacity theorem, exact two-edge necessary relaxation).
- GP SMT @46993baa50424690e4bba39b3a625f9ebdd09455:research_notes/portable_direct/R284GP_all_parameter_lower_bound.smt2, SHA256 6ed06e40130b3c8e84c2750abb2412fbc0c5d85ac666266eacf5316040f6baed. Local transcription matched this digest exactly.
- GP addendum @c2545b7a1352b09de065f6614abced6f56280ca2:research_notes/portable_direct/R284GP_ADDENDUM_RELAXATION_BOUNDARIES_20261124.md.

## Result

For all integers q>=0,u>=1, every width-F minimizer has x1=x2=x4=x7=0, with F=min(4q+8u+2,max(5q+5u+2,6q+4u+2)). Write (A,B,C)=(x3,x5,x6), H=2q+u+1,J=q+3u,r=2u+1. Exact histogram list (ordered normalized modes, not counting physical-coordinate permutations):
- 0<=q<u: (H,J,H),(H-1,J+1,H),(H,J+1,H-1), including q=0 newly proved here.
- q=u: only (H,J,H).
- u<q<2u: (2q+d,2q+2(r-d),2q+d) for every integer u+1<=d<=q+1.
- q=2u: same family for u+1<=d<=2u+1, plus (2q+4u+1,0,2q+4u+1).
- q>2u: only (2q+4u+1,0,2q+4u+1).

The respective counts are 3,1,q-u+1,u+2,1. Rigidity for q>u in the full seven-mode space is SMT-backed; the three-mode classification and q=0 case have human proofs. GM supplies 1<=q<=u. No enumeration is used as unbounded proof.

## 1. Zero-omission rigidity, human proof

Let S=x1+x2+x4+x7. At q=0 the four adjacent distances are at least 4u+1 and two opposite distances at least 2u+1. Sum of all six nominal distances is 4n-S. For n=5u+2 the total of the six nonnegative integer excesses over those thresholds is 2-S, hence S<=2. Group the excesses into edge pairs (01,23),(12,30),(02,13). Their nominal distance sums are S+2(A+B), S+2(C+B), S+2(A+C); all three threshold sums are even. Each paired excess has parity S. S=1 would require at least three total excess, contradiction. If S=2 all excesses vanish, giving A=C=u,B=3u. Each of the six singleton pair sums must then be one, namely x1+x7,x2+x4,x1+x2,x4+x7,x2+x7,x1+x4. All four singleton counts would be 1/2, impossible. Therefore S=0.

Now A+B,C+B>=4u+1 and A+C>=2u+1 at n=5u+2 imply A,C<=u+1 and A+C>=2u+1. The three listed histograms are exactly the possibilities. For sufficiency at each edge, GL with q=0 gives D2=[A-a]+ + b+C and D3=max(0,C,a,B-b+a+C). Set b0=r-C, first write b0 of B, then all A, then the remaining B. A+C>=r, B>=2(r-C) (for C=u, B=3u+1; for C=u+1, B>=3u), so both distances stay >=r on each segment; at the last endpoint A+C>=r. Rotation exchanges A,C. Adjacent and opposite conditions hold, so GE full-cycle criterion applies.

## 2. Equality cases of the GL three-mode lower bound for q>u

Put m=min(A,C), L=max(A,C)=2q+e, d=m-2q. Opposite separation implies e>=u+1. If B<q, GE forces m>=2q+4u+1, hence n>=4q+8u+2+B. Equality with F is possible only q>=2u, B=0, m=L=2q+4u+1, the Gray construction.

If m<q and B>=q, GL case 3 gives strict n>6q+4u+2: its three subcases yield n>=6q+6u+3+m, n>=6q+4u+2+m+e, or n>=7q+4u+3+m. Thus no equality. In the remaining case B,m>=q, GE gives m+B>=3q+4u+1 and n>=5q+4u+1+e. If d>=r then e>=r and n>=5q+6u+2. For q>u this is strictly above F except q=2u; equality there forces e=d=r and B=4u, as listed. If e>q+1, GL gives n>=6q+4u+3>F. Otherwise d<=2u, e<=q+1. The GL mandatory crossing from a=e-1 to e forces B>=2q+4u+2-2d and n>=6q+4u+2+e-d. Equality with F requires q<=2u, e=d, B=2q+4u+2-2d. Opposite separation gives d>=u+1; GE gives d<=q+1. This exhausts all cases.

Sufficiency for the family: put A=C=2q+d, B=2q+2(r-d), b0=q+r-d. Adjacent GE follows from A+B=4q+2r-d>=3q+4u+1, and opposite distance 2d>=r. GL simplifies exactly to D2=[d-a]+ + [b-q]+ + d and D3=max(0,d,[a-q]+-q,B-b+[a-q]+-q+d). First increase b from 0 to b0, then increase a from 0 to A, then finish b to B. D2 on the first segment is >=2d, at b0 is >=r for every a; D3 at (0,b0) equals r or greater, increases with a, and at (A,B) is >=2d. Rotated edges have the same counts. This proves safe existence, including d=r at q=2u.

## 3. Compulsory ordered block (not merely an example schedule)

For the above symmetric family with d<r, all safe paths on any edge must cross every step a=k to k+1 for d-1<=k<=q. At the after-prefix a=k+1>=d, D2>=r forces b>=q+r-d. At the before-prefix a=k<=q, D3=max(0,d,B-b-q+d) forces b<=B-q+d-r=q+r-d. Hence b is exactly b0 at all these crossings. Monotonicity of attempted counts means the q-d+2 changing nonalternating attempts from a=d-1 to q+1 are consecutive in the mode word, with exactly b0 alternating attempts already made. Coordinate identities inside a mode are not fixed. The d=r endpoint has no such necessity because the unchanged residual distance already reaches r. This is an exact order rigidity statement for every safe path on this family, retaining historical residual source groups.

## 4. Full seven-mode exclusion of singletons at equality (exact unbounded SMT)

Every safe histogram satisfies GP's four GE, two opposite, and first two consecutive crossing conditions. Retain all of those necessary assertions and q>u, u>=1, nonnegative integer x_i; replace the sub-F assertion by n=F in its two branches, and assert S>0. No extra endpoint assumption is needed in the relaxation because any safe protocol satisfies all necessary tests. Actual run with libz3 4.13.3.0, Z3_eval_smtlib2_string, exact unbounded QF_LIA returned unsat in 0.268 s. Hence at width F no singleton/triple mode occurs. This rules out mixed minimizers without assuming those modes are redundant in other contexts.

Saved exact query dd769b53fd3d5d08078df7dab3b36dbfad41451c:research_notes/portable_direct/R284GQ_minimizer_singleton_exclusion.smt2, SHA256 ae2315008f136c14a5faf604ae64b1fd4ac11e3d25d0d37d1888c5e9f52f1e1f, Git blob c5fc1b0d66b966b83f39893a49db8362a10b4239 (local git hash-object matches immutable remote blob). Reproduce with z3 -smt2 FILE. Adding the last two rotated crossings also returned unsat (0.470 s), but is unnecessary. The strengthened real relaxation obtained from the saved two-edge file by literal replacements Int->Real, QF_LIA->QF_LRA, (> q u)->(>= q (+ u 1)), (> (+ x1 x2 x4 x7) 0)->(>= (+ x1 x2 x4 x7) 1), (> lo hi)->(>= (- lo hi) 1) also returned unsat (0.253 s); SHA256 d5caa8851f1d007c0309f0783354338fb5cab9d2ff7f8fb21146194a203e7407. All strengthened comparisons are valid for original integer candidates. These are solver-backed exclusions, not an independently checked Farkas proof.

Additional executed finite checks: exact JS integer arithmetic evaluated the four GE, two opposite and all four GP closed crossing predicates, with GP2's necessary opposite-cut partition pruning, at n=F for u=1..4,q=u+1..2u+2 (18 parameter pairs). All candidate lists matched section 2, zero mixed candidates. For q=0,u=1..6, tested every S<=2 allocation with n=F using the same predicates and obtained exactly the three section-1 histograms at each u. These corroborate but are not needed for the analytic case analysis or SMT exclusion. Existing GP raw proof attachment SHA256 was independently recomputed as 25eaf7f7d9d7ac026d01357425b443a3c1d304b53ac7674dbcfca15a9983ef1c, matching GP; this is byte integrity, not proof replay.

## Next

The complete width and histogram classification is now author-verified under the frozen lemmas, with general lower bound and singleton exclusion SMT-backed. Remaining useful work: convert both tightened rational systems to independently checkable affine-disjunction/Farkas certificates, and count safe mode words (or characterize optimal schedule robustness) beyond the compulsory crossing block. Do not repeat the finite capacity scans. No project acceptance or independent Review is claimed.
