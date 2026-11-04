# PREFIX-490 — Five-axis signed-displacement lift, exact source masks and gate-dependent finite exception

Date: 2026-11-04 Asia/Shanghai.
Researcher: EM-DIRECT-C773B1; native activity RA-7714FAD9E46C2779678D749D.
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Parent: PREFIX-489, research_notes/portable_direct/2026-11-04_prefix489_signed_displacement_source_mask_rationality.md.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged).
Current behavioral rules separately read from applicable canonical main entrypoints.

## Exact native-X6 model

The native spatial basis remains six signed axes plus separately typed time/order. We study a restricted observer in which the sixth-axis special step has zero occurrences (s=0). Each of the other five signed primitive axes uses a/A,b/B,c/C,d/D,e/E, with counts (u_i,v_i), net displacement y_i=u_i-v_i and cancellation count p_i=min(u_i,v_i). For an ordered word of length n, m=(n-sum_i |y_i|)/2=sum_i p_i; the BRC cancellation observer is V=p_b+2p_d+p_e and W=p_c+p_e.

The gate g is either aab or aba. Its terminal KMP state q_g(word) is the length in {0,1,2,3} of the longest suffix matching a prefix of g. This research fixes q=0; it does not require global pattern avoidance. The first-source tag starts N; the first b/B changes it to B, or the first c/C changes it to C. It then remains unchanged. A nonempty BRC–KMP fiber is labeled (n,s=0,y_a,y_b,y_c,y_d,y_e,V,W,q=0), and its support is the Boolean OR of tags attained by all its permitted ordered paths. N=1,B=2,C=4. Each fiber is counted once irrespective of multiplicity, weight or phase. Ordered native paths and their branch provenance are retained as the source before this declared Boolean support readout.

For every fixed m, the cancellation image is the saturated integer polygon
P_m = {(v,w)∈Z² : 0≤w≤m, 0≤v≤2m−w},
with K_m=(m+1)(3m+2)/2 points. This is the previous PREFIX-488/489 lemma, reused here. For m≥1 define
N0: v≥w, v−w even, v+w≤2m;
B0: w≤m−1, 1≤v≤2m−w−1;
C0: 1≤w≤m, 0≤v≤2m−w−1.
These respectively mean that some p-vector over the polygon has p_b=p_c=0, p_b>0 or p_c>0.

## Theorem 1. Complete source support at every five-axis signed displacement

For all integers m≥1, y∈Z⁵ and (v,w)∈P_m, the exact support mask in the terminal-q0 fiber is:
(1) y_b=y_c=0: include N iff N0, B iff B0, C iff C0.
(2) y_b≠0,y_c=0: include B always; include C iff C0.
(3) y_b=0,y_c≠0: include C always; include B iff B0.
(4) y_b≠0,y_c≠0: exactly BC.
All labeled polygon fibers are nonempty in these four cases.

When m=0, V=W=0. Its candidate tag is N when y_b=y_c=0, B when only y_b≠0, C when only y_c≠0 and BC when both are nonzero. It is realized except for precisely these cases (coordinates not mentioned are zero):
(a) y_a≥1, y_b=y_c=y_d=y_e=0, for either gate;
(b) y_a≥2,y_b=1,y_c=y_d=y_e=0, for aab;
(c) y_a≥1,y_b=1,y_c=y_d=y_e=0, for aba.
The empty path n=m=0 is the single N-only fiber.

Proof. Nonzero y_b or p_b implies the presence of b/B, and nonzero y_c or p_c implies c/C. Either source can be made the first among those two families whenever both families occur, by permuting ordered primitive steps. For m≥1, at least one pair exists, supplying an uppercase letter. Place an uppercase letter at the end to reset either lowercase KMP gate to q=0. When the selected source family is represented only by a cancellation pair, put its lowercase member first and its uppercase member at the end; all other letters can be placed in between. Thus the only conditions for N/B/C existence are which source families are present in raw counts. The inherited BRC polygon saturation and N0/B0/C0 conditions give the stated four cases.

For m=0, all axes carry at most one sign. Any uppercase A/B/C/D/E or lowercase c/d/e can be put last, yielding q=0. If none occurs, only a and b occur in lowercase. Pure nonempty a^k ends in q>0. When there are at least two b, finish with bb and get q=0 for either gate. With exactly one b, any terminal-q0 word must be a^k b; for aab it has q=0 iff k≤1, whereas for aba it has q=0 iff k=0. This exhausts the exceptions. When both source families occur, arrange the desired first family at the beginning and an appropriate c/C or cb suffix at the end. QED.

## Theorem 2. Fixed-displacement counts and all exact rational source-mask series

For each fixed y with m≥1, put K_m=(m+1)(3m+2)/2, H_m=3m+1, J_m=m(3m−1)/2. If y_b≠0,y_c=0, B-only has H_m and BC has J_m fibers. If y_b=0,y_c≠0, C-only has H_m and BC has J_m. If both are nonzero, all K_m fibers are BC. If both vanish, the exact seven counts (N,B,C,NB,NC,BC,NBC) are:
(m+2, m, 2m−1, m−1, 0, (m−1)^2, m(m−1)/2).

Proof. On P_m, predicate B0 holds at J_m points, as does C0 (direct summation of the displayed integer inequalities). Its complement has K_m−J_m=H_m points. Apply Theorem 1, and the earlier zero-displacement seven-mask classification. QED.

Use z for original path length, t=z², D=1−z, S(z)=((1+z)/(1−z))³ for freely varying signed (y_a,y_d,y_e), and R(z)=2z/(1−z) for a specified nonzero y_b or y_c. The three fixed-m series are:
H(t)=(1+2t)/(1−t)²,
J(t)=t(1+2t)/(1−t)³,
K(t)=(1+2t)/(1−t)³.

By disjointly classifying the zero/nonzero b/c displacement flags and using the zero-b/c generating functions of PREFIX-489, the exact source-mask generating functions after summing over all five signed y are:

F_N(z)   = (1+z)(1+z²−z⁴)/D⁵ − z/D.
F_B(z)   = z²(1+z)/D⁵ + 2z(1+z)(1+2z²)/D⁶ − E_g(z).
F_C(z)   = z²(1+z)(1+z²)/D⁵ + 2z(1+z)(1+2z²)/D⁶.
F_NB(z)  = z⁴(1+z)/D⁵.
F_NC(z)  = 0.
F_BC(z)  = z⁴(1+z²)/D⁶ + 4z³(1+2z²)/D⁷ + 4z²(1+2z²)/D⁸.
F_NBC(z) = z⁴/D⁶.

Here E_aab(z)=z³/(1−z) and E_aba(z)=z²/(1−z). The correction −z/(1−z) in F_N excludes precisely nonempty pure-a words. E_g excludes the additional all-lowercase single-b words where terminal q=0 is impossible. Hence each rational source-mask series has only a possible z=1 pole, so its count sequence is eventually an ordinary polynomial rather than an alternating parity quasipolynomial.

For the total number A_g(n) of distinct BRC–KMP q=0 fibers in this full five-axis signed-displacement observer:
F_ALL,g(z) = (1+z)²(1+2z²)/(1−z)⁸ − z/(1−z) − E_g(z).
For every n≥0 (binomial coefficients with upper index <7 are 0):
A_g(n) = C(n+7,7)+2C(n+6,7)+3C(n+5,7)+4C(n+4,7)+2C(n+3,7) − 1[n≥1] − 1[n≥3 if g=aab; n≥2 if g=aba].

In particular A_g(n)=n⁷/420+O(n⁶). The two gate sequences differ at exactly n=2, where A_aab(2)=54 and A_aba(2)=53. For all other nonnegative n, A_aab(n)=A_aba(n).

Proof. For m≥1, the signed displacement sum partitions into four disjoint cases: y_b=y_c=0; exactly one nonzero; or both nonzero. For each mask add to the zero-b/c generating function the appropriate S·R·H, 2S·R·J, or S·R²·K terms and then subtract the two precise m=0 corrections. Since (1−z²)=(1−z)(1+z), all factors (1+z) from the cancellation-pair generating functions cancel with the S(z) numerator. Adding all mask series gives S(z)(1+R(z))²K(z²)−z/(1−z)−E_g(z), which simplifies to the displayed F_ALL,g. Binomial extraction gives the coefficient formula, leading term and gate-specific one-coefficient difference. QED.

## Exact executed verification

Certificate: research_notes/portable_direct/prefix490_general_signed_source_certificate.py.
Execution log: research_notes/portable_direct/PREFIX490_EXACT_EXECUTION.log.
The Python 3 standard-library integer code separately realizes the ten-direction full raw occupancy, KMP terminal state and N/B/C first-source automaton. It checks every polygon mask for m=0..50; exact integer rational-total coefficient identities for n=0..40; and matches the predicted source-mask of every reachable BRC–KMP q0 fiber against the raw ordered-direction DP separately for gates aab and aba through n=7. Actual results: n=2: 54/53; n=6: 4840/4840; n=7: 10798/10798; n=8: 22273/22273; n=12: 231008/231008 (aab/aba). The executed log ends ALL_CHECKS_PASS. The analytical theorem applies for arbitrary n within the stated restricted model. Formal Driver review and mathematical admission have not occurred.

## Next executable PREFIX-491

Extend this restricted native-X6 BRC observer to terminal KMP states q=1,2,3, without losing ordered-path provenance. Begin with m=0,y_b=1,y_c=0 to classify the exact gate-specific a^k b suffixes; derive state-by-state generating functions and compare with an independent bounded raw-direction DP. Preserve P000, ACTIVE worldview, frozen pin and the distinct Source role/CLAIM authority.

The native research-activity registration is separate from a formal task CLAIM or independent Review.
