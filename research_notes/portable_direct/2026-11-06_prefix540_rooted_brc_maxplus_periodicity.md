# PREFIX-540 — Exact rooted BRC max-plus periodicity

Date: 2026-11-06. Line: RS-X6-NATIVE-ROTATION-DYNAMICS.
Frozen scientific source: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessor: PREFIX-539 at 8dc4ebaccfaeb633550f27322e9754a2697091d9.
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Research route: independent author-side scientific material, not an authenticated CLAIM.

## The exact question and observation

Use the frozen four-STAR native X6 directed model with 48 phases, 144 legal directed phase edges and two labeled INNER/OUTER choices for every macro step. For a fixed root phase s, define p1(w) by the first-axis BRC cancellation number of a length-d labeled path w. Determine M_s(d), the maximal possible p1(w), for every d>=0 and every root. The observer is the maximum BRC exponent with all gate multiplicities aggregated; no Cell or ordered microstep state is being compressed for future operations by this theorem.

Write a phase s=(a,p,c). Define sigma(s)=sign(c) when |c|=1 and 0 otherwise. For sigma(s)=0, let I(s)=1 if any legal immediate phase successor j has |c_j|=1, and I(s)=0 otherwise.

## Theorem: exact fixed-root maxima at all depths

For all roots s and integers d>=0:

(A) If sigma(s)=0, write d=3k+b, b in {0,1,2}. Then

    M_s(d) = k + I(s)*[b=2].

There are 24 roots with I(s)=1 ("FAST") and 16 roots with I(s)=0 ("DELAYED").

(B) If sigma(s)=+1 or -1, write d=6k+b, b in {0,1,2,3,4,5}. Then

    M_s(d) = 2k + [b in {4,5}].

There are exactly 8 such roots ("SIGNED").

The displayed maxima are attained by actual labeled native paths. This refines the uniform earlier bound p1 <= floor((d+1)/3), root by root.

## Proof (exact finite max-plus reduction)

Let epsilon(i) be 1 if |c_i|=1 and 0 otherwise. The PREFIX-539 cocycle is

    tau_r(i,j) = (epsilon(i)+epsilon(j)-|sigma(j)-r|+|sigma(i)-r|)/2,

where r=sigma(s). The frozen legal graph has no two successive first-axis phases. Consequently, tau_r is an integer in {0,1} on each of the 144 directed edges for all three r. For any path i0,...,id, summing tau telescopes:

    sum tau_r = (sum_{k=0}^{d-1}(epsilon(ik)+epsilon(ik+1))
                 - |sigma(id)-sigma(i0)|)/2 = p1.

Thus the sum exactly reproduces the BRC cancellation number, with its actual native path retained upstream.

Define T_r on 48-vectors by

    (T_r v)(i) = max_{j in NEXT(i)} (tau_r(i,j) + v(j)),

and V_r(0)=0_48; V_r(d)=T_r^d(0_48). Then M_s(d)=V_{sigma(s)}(d)(s).

Finite integer evaluation of all 48 coordinates using the explicit STAR transition table proves the three identities

    T_0^3(0_48)  = 1_48,
    T_+1^6(0_48) = 2_48,
    T_-1^6(0_48) = 2_48.

The attached executable certificate independently constructs the 48 phases and 144 edges and asserts these equalities coordinatewise.

For every scalar integer c, T_r(v+c*1_48)=T_r(v)+c*1_48. Therefore these finite identities imply for ALL d>=0

    V_0(d+3)=V_0(d)+1_48,
    V_+/-1(d+6)=V_+/-1(d)+2_48.

The base values for sigma(s)=0 at d=0,1,2 are (0,0,I(s)).
For each sigma(s)=+/-1 root, d=0,1,2,3,4,5 has base values
(0,0,0,0,1,1). These base values are also checked by the finite certificate. Reducing d modulo 3 or 6 gives (A) and (B). Every maximum over a finite nonempty set of legal path choices has a maximizing path. QED.

The finite graph is reconstructed from the exact STAR triples
(1,3,6),(1,4,5),(2,3,5),(2,4,6). A phase is (star,previous,current). A transition continues in the same STAR excluding immediate backtracking, or changes to the other STAR containing |current|, preserving current while selecting a legal next axis. Both labeled microsteps exist on each directed transition.

## Consequence: root-specific joint-histogram support

The previous joint support satisfies 0<=h<=H(d)=floor((d+2)/4) and h<=p1. Combining these with the theorem gives for a rooted BRC/gate polynomial:

    0<=h<=H(d),  h<=p1<=M_s(d).

The number of candidate coefficient positions per root is

    C_s(d)=sum_{h=0}^{H(d)} max(0,M_s(d)-h+1).

For all 48 roots at depth 20: old uniform support 1584 slots; new rooted support 1440 slots, saving 144 (9.09%). At depth 23: 2016 vs 1848 slots, saving 168 (8.33%). At depth 24: 2016 vs 2016, no saving. These are candidate coefficient positions, not a claim that every position is occupied.

## Evidence, scope and continuation

The exact Python certificate (adjacent file) constructs the graph and verifies all 48-coordinate period identities, every base case, and 48 root classifications (24 FAST, 16 DELAYED, 8 SIGNED). An independent raw endpoint dynamic program propagates actual labeled-path multiplicities by the pair (terminal phase, first-axis visit total K), recomputes p1 from the endpoint formula, and agrees with all 48 formulas at lengths 0..36 (1776 complete root-depth maxima). Additional max-plus checks cover lengths 0..240. Execution status: ALL_CHECKS_PASS, Python exact integers.

The all-depth theorem rests on the finite max-plus identities plus a mathematical induction, not on extrapolating a finite experiment. The optimization applies only to the declared BRC/gate histogram observer. Other operations on Cell identities, time, ordered branch provenance and joint relations continue to use their native typed carriers.

Next: integrate per-root exact support into an allocation-aware symbolic histogram, compare repeated time/memory runs against the PREFIX-539 49-coordinate sparse lift, and establish which further native Cell/provenance observers admit an exact factorization.
