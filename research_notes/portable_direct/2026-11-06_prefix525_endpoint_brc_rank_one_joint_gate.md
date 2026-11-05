# PREFIX-525 — Exact endpoint–visit reconstruction of signed X6 BRC and a rank-one aAc gate transfer

Date: 2026-11-06 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Task: RS-X6-NATIVE-ROTATION-DYNAMICS. Researcher-ID: EM-X6-8FB3D3. Activity: RA-D3661FAD9EA47C295651391F.
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Inputs: frozen four-STAR symbolic phase graph (PREFIX-518/523/524), PREFIX-515 BRC signed-pair formula, PREFIX-522 aAc local gate, current P000/ACTIVE Heartbeat World and portable research rules. This is a symbolic signed-X6 path statement.

## 1. Population and declared observers

The four STARs have native axes A={1,3,6}, B={1,4,5}, C={2,3,5}, D={2,4,6}. A directed phase is s=(STAR,p,c), with c signed current direction and p signed preceding direction. There are 48 states, each with three legal next phases. For every directed edge s->t there are two independently labeled native two-step paths:
INNER=(-c(s),c(t)), OUTER=(c(t),-c(s)).
Every length-d path has d phase edges, a 2d-long signed native word, d provenance bits and an initial phase. The population has exactly 48*6^d labeled histories.

Fix any one of 24 K4/S4 chart frames h. The signed gate aAc reads positive h-L1 as a, negative h-L1 as A, both h-L3 signs as c, and every other axis as filler. Let H_h count occurrences of aAc. PREFIX-522 proves that a hit ends at macro i>=2 iff phase s_i equals one target phase T_h and the two most recent branches are INNER. Phase T_h has exactly three incoming predecessors and no self-loop.

The intended quotient retains the joint histogram (H_h,p_1,...,p_6) and endpoint phase labels for path concatenation and exact BRC readout. Ordered intermediate Cell history and branch provenance remain separately available if those are the desired outputs.

## 2. Theorem A: six-axis BRC is an endpoint-corrected visit count

For signed direction c and native axis a=1,...,6 define sigma_a(c)=sgn(c) if |c|=a, otherwise 0. For a phase chain s_0,...,s_d define
K_a = sum_(i=1)^d (1_(|c(s_(i-1))|=a) + 1_(|c(s_i)|=a)).

For every d>=0 and every branch choice, **exactly**
y_a = sigma_a(c(s_d))-sigma_a(c(s_0));
p_a = (K_a - |y_a|)/2.
Here y_a is the net signed-X6 primitive displacement on axis a, and p_a=min(N_a^+,N_a^-) is the native BRC opposite-sign pair count. Also sum_a K_a=2d, K_a>=|y_a|, and K_a and |y_a| have equal parity. If s_d=s_0, then y=0 and p_a=K_a/2.

Proof. Both ordered edge realizations contain the same two signed directions {-c(s_(i-1)),c(s_i)}. Their signed displacement telescopes:
sum_(i=1)^d(-e_(c(s_(i-1)))+e_(c(s_i)))=e_(c(s_d))-e_(c(s_0)), where e_(-a)=-e_a.
Their unsigned axis-a occurrence total is K_a. Thus N_a^++N_a^-=K_a and N_a^+-N_a^-=y_a, giving p_a=(K_a-|y_a|)/2. Parity, nonnegativity, d=0, and the return case follow immediately. QED.

The reduction from separate signed occurrence counts to (K,s_0,s_d) is exact for this declared BRC/output scope. The original INNER/OUTER labels must still be retained for intermediate Cell queries and historical source recovery.

## 3. Theorem B: a 48-phase second-order transfer with rank-one gate correction

Introduce six commuting formal visit variables x_1,...,x_6. Define a 48x48 matrix W(x) with destination rows, source columns, and
W_(t,s)= product_(a=1)^6 x_a^[1_(|c(s)|=a)+1_(|c(t)|=a)] when s->t, and 0 otherwise.
For fixed initial phase s_0, let f_d(x,z)_t be the sum of x^K z^H over all labeled paths ending at t. Let e be the unit vector of the gate target T_h.

For ALL d>=2:
**f_0=e_(s_0), f_1=2W f_0, f_d=2W f_(d-1)+(z-1)e e^T W^2 f_(d-2).**

Proof. Every incoming weighted phase history extends through each allowed phase edge in two labeled branch orders. This gives the default 2W f_(d-1). The one exceptional weight occurs when the last branch is INNER, the preceding branch was INNER and destination equals T_h: replace weight 1 by z, an extra z-1. Since T_h has no self-loop, its immediate predecessor s differs from T_h; choosing INNER at the previous edge ending at s could not itself close the gate. The eligible histories are precisely the one-branch-inner extensions of arbitrary histories two steps earlier, summed by (W^2 f_(d-2))_(T_h). Hence the difference is (z-1)e e^T W^2 f_(d-2). This partition is bijective for every length, every frame h and all formal weights. QED.

Summing in the length variable t gives the exact formal resolvent
**sum_(d>=0) f_d t^d = (I-2tW-(z-1)t^2 e e^T W^2)^(-1)e_(s_0).**
Its matrix has constant term I and so has a unique formal-series inverse. The gate-dependent correction has rank at most one in the 48 phase indices. This replaces the explicitly saved previous-branch bit of the older 96-state first-order transfer by one time lag and a rank-one update. It does not assert a strictly smaller minimal first-order state count.

For any final t and multidegree K, [x^K z^j] f_d(t) counts exactly the histories with final phase t, visit vector K, and H=j. Theorem A supplies p_a=(K_a-|sigma_a(c(t))-sigma_a(c(s_0))|)/2; after this endpoint correction, summing s_0 and t gives the full (H,p_1,...,p_6) histogram. This keeps the required BRC min-readout AFTER path composition, as demanded by PREFIX-523.

## 4. Theorem C: exact weighted renewal identity and PREFIX-524 specialization

Let M=I-2tW and q=(z-1)t^2. Since e e^T W^2 is rank one, the formal Sherman–Morrison identity yields
1^T(M-q e e^T W^2)^(-1)e_(s_0)
=1^T M^(-1)e_(s_0)
 + q (1^T M^(-1)e)(e^T W^2 M^(-1)e_(s_0)) / [1-q e^T W^2 M^(-1)e].
All inverses are formal series, not numerical matrix approximations. This is the exact six-axis BRC-visit-weighted renewal kernel for aAc.

At x_a=1 the phase graph has exactly three incoming and outgoing neighbors per phase. Summing over all 48 initial phases gives the base term 48/(1-6t), the first hit numerator 9t^2(z-1)/(1-6t)^2, and
t^2 e^T W^2(I-2tW)^(-1)e = sum_(m>=2) 2^(2m-2) a_m t^(2m) = R(t),
where a_m is PREFIX-520's exact 2m-step phase-return count. Therefore the joint-weighted formula SPECIALIZES EXACTLY to PREFIX-524:
P(t,z)=48/(1-6t)+9t^2(z-1)/[(1-6t)^2(1-(z-1)R(t))].
This is a direct all-length algebraic consistency result.

## 5. Explicit information-loss witness for endpoint/gate-only compression

At d=3 the following distinct INNER-only paths have the SAME start (A,+6,-3), SAME end (A,-6,+3), SAME H=0, but different BRC axis-1 pair count.

Path 1: (A,+6,-3)->(A,-3,+1)->(A,+1,-6)->(A,-6,+3).
Primitive word (+3,+1,-1,-6,+6,+3), so p_1=1.

Path 2: (A,+6,-3)->(C,-3,+2)->(D,+2,-6)->(A,-6,+3).
Primitive word (+3,+2,-2,-6,+6,+3), so p_1=0.

Their visit counts K_1 are 2 and 0 respectively. Hence H and endpoints alone cannot recover p_1; the visit-coordinate repair distinguishes these two fibers exactly.

## 6. Reproducible exact certificates and finite scope

The full author-executed Python integer certificate checks all 288 labeled two-step phase edges and all six axes (1,728 exact local checks), compares the independent 96-state and the 48-vector second-order polynomial transfers on six axes to depth 6 (59,660 coefficient positions), and directly reads literal primitive words for all 74,640 labeled paths of depths 0..4 (48*sum_(d=0)^4 6^d). The separately author-executed JavaScript integer certificate checks the same local laws, 37,254 coefficient positions to depth 5, and all 74,640 primitive words through depth 4. Both return ALL_CHECKS_PASS.

At d=6, the exact joint (H,p_1) counts are:
(H,p)=(0,0):568320; (0,1):1374672; (0,2):238356; (1,1):43056; (1,2):14904; (2,2):180.
The H marginal is (2181348,57960,180), matching PREFIX-524. Each certificate uses exact integers; the theorem for arbitrary finite d follows from the proofs above. Author checked, pending independent mathematics review.

## 7. Next open unit

Use the six-axis weighted rank-one resolvent to extract an exact lower-degree rational denominator for the joint single-axis (H,p_h-L1) distribution, accounting for endpoint signed differences. Compare minimal transfer polynomials by exact elimination, and keep coefficient-growth/bit-complexity accounting separate from algebraic state compression. The parent hard target remains native arbitrary-triad C6 generators, generated group and physical X6 rotation-selection dynamics; the present result concerns the explicitly defined symbolic four-STAR path model.

BRC reuse: exact signed-pair observer formula from PREFIX-515; preserved branch/source provenance as in PREFIX-518/523; all future gate and concatenation operations in this note covered by the proved transfer, not all possible Cell-history observers.
