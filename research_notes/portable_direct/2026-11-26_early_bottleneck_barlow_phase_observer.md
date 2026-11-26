# 2026-11-26 early bottleneck revisit — P022 exact shell-total phase observer

Status: NONCANONICAL DIRECT RESEARCH / author derivation and finite independent integer regression / novelty relative to full legacy owner branch not yet established / NOT A TASK PUBLICATION, RESULT, REVIEW OR FOUNDATION PROMOTION.
Progress-Event-ID: em-revisit-20261126-barlow-phase-01
Control: own registration request revisit-20261126-0801-own-session (native receipt RUNNING at last observation); no task claim or execution authority. P022 historical task lookup revisit-20261126-0801-p022 RUNNING. Historical P000 task lookup revisit-20261126-0801-p000 FAILED: CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION. Do not replay or infer an alias. No existing owner was displaced.

## Frozen scientific inputs and old negative evidence

P022 original: docs/OPEN_PROBLEMS.en.md, PR #50, ideal carrier integer geometry (not physical native space). Source pin 364c81984ca8ea31c18126a03ad308ef8fb02a76. #288 monotone Barlow interface witness polynomial, #292 target-layer observer compression, #267/#296 canonical periodic growth (merge 0d6b751e0d16ba0049369e912e1730e3383f0f58), src/enterprise_math/p022_barlow_growth.py blob 4185cafdb3e4ad4f55c58ff111747013e710af43; same-pin p022_barlow_stacking.py and p022_barlow_precision.py. #296 explicitly warns that the universal eventual C-finite annihilator may not be minimal and equal (L,|D|) does not fix the finite sequence/phase. This negative remains true. #298 coordination cardinality is a different observer. The old P022 Franel taskbooks at TP2-D78DBA0243911E0363FA / TP2-DE338F269CA11E9BC01B and owner pin 603ef1c72245612359f8b59cab7a492de21a9166 concern additional arithmetic defect/reentry questions; this note does not close them or prove that the complete historical branch lacks the present result. Existing task inventory 2026-11-04 records a structural fork for RS-P022-OBSERVATION-HISTORY. Current owner/novelty review still outstanding; searches alone do not establish absence.

New tool: canonical main-backed WBRC T33,T35,T37, definitions/ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md at source pin above. Use positive rational first-moment transfer with length marker, retain distinct forward/backward and plus/minus channels; do not treat aggregate as a labeled phase state. Phase here means root-relative index in a stacking word, not complex phase, native physical time, or a six-axis physical claim. Coordinate data are ideal Barlow integer coordinates (q,r,k) with monotone interfaces, not a P000 proof.

## Author lemma 1: exact finite observer and inverse

Let s be a declared periodic binary word of length L, 1 representing +, 0 representing -. Let K be its number of 1, D=2K-L. For positive distance q from layer zero let a_q count 1 along forward raw interfaces; b_q count 1 along the reverse raw word. Actual downward traversal negates signs, which only swaps the terms below. Define f_0=2, f_q=2^a_q+2^(q-a_q)+2^b_q+2^(q-b_q) for q>=1, h_0=4, h_q=f_q for q>=1.

Canonical per-layer geodesic total at radius n: if |k|=n, 3^n; otherwise binom(n,q)[3*2^(n-q+c)*(1+2^d)-6] where q=|k|, c=min(plus,minus), d=|plus-minus|. Since 2^c(1+2^d)=2^plus+2^minus, summing yields, n>=1,
B(f)_n=sum_{q=0}^n binom(n,q) 2^(n-q) f_q,
T_n=2*3^n+3*B(f)_n-3*f_n-12*2^n+18, T_0=1.
The -6 contribution is -6*(2*2^n-3); the q=0 term has one layer, not two. Coefficient of f_(n-1) is 6n; all other f terms are earlier. Thus all shell totals T_n are equivalent to f, and T_1..T_N recover f_0..f_(N-1) by exact triangular inversion.

For r=0..L-1 put U_r=2^a_r+2^b_r and V_r=2^(r-a_r)+2^(r-b_r), using a_0=b_0=0; A=2^K,C=2^(L-K). Then h_(mL+r)=A^m U_r+C^m V_r, including h_0. Actual BRC realization: disjoint four directed L-cycles with each edge weight 2 for the selected bit and 1 otherwise, reading forward or reverse word; start at phase zero in each cycle, sum path mass over endpoints at depth q. WBRC T33 first moment is exactly h_q; use T35 length-marked transfer / T37 formal mass specialization (no complex cancellation or lossy native coordinate compression). The four-cycle representation and scalar projection are applied here algebraically; repository BRC implementation itself was not invoked. Integer regression independently implements the pinned layer formula.

H(z)=U(z)/(1-A z^L)+V(z)/(1-C z^L) with U(z)=sum U_r z^r, V analogously, F(z)=H(z)-2. Therefore
G_T(z)=2/(1-3z)+3/(1-2z)*F(z/(1-2z))-3*F(z)-12/(1-2z)+18/(1-z)-7.
The last -7 corrects the constant 8 to T_0=1. Reducing numerator and denominator by polynomial gcd yields the minimal eventual recurrence denominator (ordinary rational formal series), including cancellations with universal factors. This is an exact derivation, not an independently reviewed theorem.

For fixed L,K, if D != 0, two samples h_r and h_(L+r) recover U_r,V_r by a 2x2 invertible linear system; D=0 recovers U_r+V_r. Thus equality T_1..T_(2L) is sufficient for all-radius equality; for D=0 the bound is L. These are sufficient bounds, not sharpness claims.

## Author lemma 2: complete nonzero-drift fiber in declared-L word space

For fixed K with D !=0, exact shell equality iff unordered pairs {a_r,b_r} agree at every r=0..L, because U_r is the sum of exactly two powers of two and uniquely determines their unordered exponents (two equal exponents are the single-bit case); V_r is then determined. Here b_r=K-a_(L-r). Define meeting set M={r: a_r=b_r} containing 0,L, symmetric under r->L-r. Nontrivial excursions are adjacent meeting intervals (i,j) with j-i>1. Two trajectories are strictly ordered between meetings. Any alternate compatible pair of 0/1 increment paths has to choose one ordering throughout each excursion: switching without a meeting would require a gap to jump from positive to negative in one unit step, impossible. At meetings swapping is free. Reverse consistency b'_r=K-a'_(L-r) forces the excursion choices to be the same on reflection-paired intervals; it also suffices. Therefore if e is the number of reflection orbits of nontrivial excursions, there are exactly 2^e labeled binary words in the fiber for fixed declared L and K. This counts all words, not only those of least period L. If e>0 reversal pairs distinct words, leaving 2^(e-1) reversal classes; if e=0 the only word is a palindrome. Global sign may be quotiented only with the corresponding K<->L-K change. No cyclic root shift was silently identified. This is a new author-level exact finite fiber characterization in this note; project-wide priority and independent verification pending.

## Executed finite checks (independent JS integer implementations)

All 510 nonempty binary words of lengths 1..8, n=0..2L+3: 9212 exact BigInt direct layer-sum versus triangular-transform comparisons, zero mismatches. All binary words of lengths 1..12 with 2K!=L grouped by K and unordered prefix pairs: 3076 total classes tested; each size equals 2^e. Counts per L: 2,2,6,6,20,26,70,90,252,362,924,1316. Additional enumeration of primitive words up to length 12 modulo reversal/global sign found first nontrivial all-depth twin at L=6,D=0: 001101 / 001110, h_q for q=1..11: 6,9,12,18,24,32,48,72,96,144,192. These are distinct even modulo reversal/sign; both least period 6. For L=7, K=3: 0100101 / 0110001, meetings {0,2,5,7}, excursions (0,2),(2,5),(5,7), reflection orbit count 2. Four labeled words / two reversal classes in this fiber. Their h_q q=1..13: 6,8,12,18,24,36,48,72,96,144,240,320,480. First T_0..T_8 for L=6 example: 1,12,84,402,1596,5892,20892,72504,248724; L=7 example: 1,12,84,384,1524,5652,20172,70656,244692. Equality at all n follows from lemma 1, not finite extrapolation.

Reproduction pseudocode (uses exact integer arithmetic):
for L in 1..8:
 for s in binary_words(L):
  for n in 0..2*L+3:
   a(q)=sum(s[j mod L] for j in 0..q-1)
   b(q)=sum(s[L-1-j mod L] for j in 0..q-1)
   f(q)=2 if q==0 else 2^a(q)+2^(q-a(q))+2^b(q)+2^(q-b(q))
   direct=1 if n==0 else sum over k=-n..n of pinned layer formula
   assert direct == (1 if n==0 else 2*3^n+3*sum_{q=0}^n binom(n,q)*2^(n-q)*f(q)-3*f(n)-12*2^n+18)
for L in 1..12:
 group all words with 2*K!=L by (K,tuple(sorted(a(r),b(r)) for r=0..L))
 for group:
  M=[r:a(r)==b(r)]
  excursions=[(i,j) consecutive in M if j-i>1]
  e=len(set(min((i,j),(L-j,L-i)) for (i,j) in excursions))
  assert len(group)==2^e

## Proposed new, bounded next problem — not yet formally published

Classify the zero-drift phase twins using folded prefix counts and the explicit finite observation horizon; derive sharp recovery horizon per (L,K) and exact least-period refinement, then compute and certify minimal recurrence denominators from G_T. Do not re-prove old growth rate or the nonzero-drift fiber lemma without an independent verification reason. First check current native task/owner, full legacy P022 observation branch and recent records; if exact scope already covered, consume existing result instead. Initial acceptance: prove or falsify that U_r+V_r uniquely determines unordered folded counts {min(a_r,r-a_r),min(b_r,r-b_r)} for each r (no assertion yet), then solve consistency across r and reflection; include exact all-depth equivalence and a smallest witness for any failed conjecture. Validate against all declared words <=12, distinguish primitive from declared period and labeled vs sign/reversal. For minimal recurrence, reduced denominator must have exact gcd certificate and reproduce pinned sequence; sharp observation horizon requires lower-bound witnesses or a proof of impossibility. Cost: four L-cycles, O(L) vertices/edges, coefficients O(L) bits and O(L^2) bit storage for explicit prefix table, L-step linear word scans plus integer bit cost; naive finite full-word grouping O(L^2*2^L) bit operations up to sorting/hash overhead, <=8190 words over L<=12. Shell regression direct formulas O(N^2) summands per word up to n=N, integer operands O(N) bits, binomial/power arithmetic and comparisons charged. Construct rational series via polynomial substitutions of degree O(L), exact polynomial gcd cost charged separately (not a claimed speedup for bit complexity). If folding uniqueness fails, retain smallest exact collision rather than discard phase residual; if no new scope, do not publish. No physical/native world extrapolation.

## Other old lines triaged

P000 Gen16 bare K4_ADJ universal lift rejected; Gen17 exact C2xS4 graph of sign and zero-section subgroups intersect in A4 despite individual surjectivity; Gen18 full generator-fiber transparency accepted, chosen lift-pair insufficient, flat pure gauge not sufficient for equivariance, nonflat equivariant example. Historical frozen inputs ba1396656ac3f8d935d653c58b6080803f1bdbaf, research_returns/P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17_RETURN_20260830.md, research_returns/P000_LOCAL_TO_GLOBAL_BACKGROUND_EQUIVARIANCE_V18_RETURN_20260831.md, driver_reviews/P000_LOCAL_TO_GLOBAL_BACKGROUND_EQUIVARIANCE_V18_DRIVER_REVIEW_20260831.md. Do not resurrect universal claims. Historical Gen19 moduli question not presumed current; native lookup NO_CURRENT_IMMUTABLE_PUBLICATION. Potential joint lift-fiber weighted observer only if current moduli frontier and missing output are verified; no task proposed. P022 graph-distance/domain API already resolved (legacy task inventory), no replay. P017/P018/P021/P022/P023/P024 remain scoped active according to current problem index, not individually exhaustively reviewed. Recent RH/X6/Riesel directions are already actively developed; no duplicate publication.

Publication barrier: current ordinary-chat MCP exposes task_prepare for existing immutable publication, and review-linked Driver followup_materialize, not arbitrary new independent task publication. The canonical task-record CLI requires actual current prepare/audit/publish and atomic exact taskbook+V2 record, not a fabricated JSON PASS. Current own registration and current P022 read pending, global exact dedup incomplete. This research note is durable evidence only; zero new tasks, no READY/NEEDS_DISPATCH assertion, no GitHub Actions invoked, no global index mutation.
