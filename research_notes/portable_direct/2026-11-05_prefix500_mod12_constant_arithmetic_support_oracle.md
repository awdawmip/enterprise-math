# PREFIX-500 — Modulus-12 elimination: constant-arithmetic exact BRC/KMP first-source support

Date: 2026-11-05 Asia/Shanghai. Researcher-ID: EM-DIRECT-8B0128. Native Activity: RA-F9B518C846D8B912D6658ED6.
Mode: author-side independent continuation, no formal CLAIM. Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Scientific inputs remain frozen at awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Current normative controls were fetched separately from canonical main.
Predecessor: research_notes/portable_direct/2026-11-05_prefix499_constant_suffix_linear_support_oracle.md.

## Selected local problem and observer

Within native X6 Heartbeat World, the sixth spatial axis has zero occupancy in the selected path family. For the other five axes a,b,c,d,e, words use signed alphabet {a,A,b,B,c,C,d,D,e,E}. Retain the exact observation (n,y,V,W,q,t), with five signed displacements y_i, per-axis cancellation p_i=min(u_i,v_i), V=p_b+2p_d+p_e, W=p_c+p_e, longest terminal KMP prefix q of g in {aab,aba}, and absorbing first-source tag t in {N,B,C}. Permitted future operation: append a native direction; the observer is not the full underlying native history. BRC application is the exact integer cancellation carrier and joint observer-preservation mapping, not a claim about physical dynamics or an independent five-dimensional native world.

PREFIX-499 obtained the exact support set C_g(n,y,V,W) by checking at most 125 three-color suffix words, with a loop over e=p_e in an interval of O(n) possible integers. We remove this last length-dependent loop.

## Theorem: a constant-arithmetic exact support oracle

For each fixed gate g in {aab,aba}, the support set C_g(n,y,V,W) can be computed exactly using O(1) integer arithmetic operations and O(1) auxiliary words, uniformly for every nonnegative path length n and all integer observation inputs. For valid inputs all intermediate integers have O(log(n+1)) bits. In particular, the proof supplies a direct bounded-arithmetic algorithm with no n-dependent precomputed table, no generic integer-programming solver, and no enumeration of cancellation points.

### Step 1. Reuse the exact word/occupancy reduction

Reject invalid n or nonintegral/negative m=(n-sum_i |y_i|)/2. Set d=p_d, e=p_e, so

p_a=m-V-W+d+e,
p_b=V-2d-e,
p_c=W-e.

The five-color Parikh counts for colors (a,b,B,c,x), where x represents A/d/D/e/E, are

k_a=p_a+max(y_a,0);
k_b=p_b+max(y_b,0);
k_B=p_b+max(-y_b,0);
k_c=2p_c+|y_c|;
k_x=p_a+max(-y_a,0)+2(d+e)+|y_d|+|y_e|.

For every suffix v of length min(3,n), impose k>=Parikh(v) componentwise. The suffix fixes q. For tag B, either the prefix contains a B-source (k_b+k_B-v_b-v_B >=1), or it contains no B/C source and the suffix's first source is B. The analogous disjunction holds for tag C. Tag N requires no prefix B/C source and no source in v. Each resulting conjunctive feasibility branch is a list of integer inequalities

a*d+b*e+c >= 0.

The *only nonzero coefficients of d* in this explicit construction have absolute values in {1,2,3,4}. They arise from p_a(+1), p_b(-2), k_x(+3), and the prefix B-source count 2p_b+|y_b|(-4); equality is represented by two opposite inequalities. Thus every nonzero |a| divides M=lcm(1,2,3,4)=12.

### Step 2. Exact residue elimination

For each residue r=0,...,11 write e=12t+r, t>=0. An inequality a*d+b*e+c>=0 converts to:

* if a>0: d >= (-12b/a)t + ceil((-br-c)/a);
* if a<0, h=-a>0: d <= (12b/h)t + floor((br+c)/h);
* if a=0: (12b)t+(br+c)>=0.

All displayed slopes are integers because |a| divides 12. Hence every lower and upper d-bound is an affine integer-valued function of t. There is an integer d satisfying all bounds exactly if and only if every lower bound is at most every upper bound. Together with the a=0 inequalities and t>=0, these are finitely many one-variable integral affine inequalities of the form A*t+C>=0.

For A>0 impose t>=ceil(-C/A), for A<0 impose t<=floor(C/(-A)), and for A=0 check C>=0. Intersect the resulting integer interval. If it contains t, take the least such t, set e=12t+r and d to the maximum lower bound; this explicitly reconstructs a witness. Empty intervals are infeasible. Loop over twelve residues and the constant number of suffix/tag/branch cases, union the successful (q,t) outputs. This proves both directions of the oracle's result and covers n=0,1,2 (suffix is then the whole word).

Because the gate length, alphabet, source-tag set, number of inequalities, and modulus 12 are fixed constants, the entire query uses O(1) arithmetic operations. In ordinary bit-cost accounting, operations are on O(log(n+1))-bit numbers for valid observations; additions, comparisons and division by fixed coefficients yield O(log(n+1)) bit complexity under standard elementary arithmetic. This is a stronger *specific-model* bound than the prior O(n) arithmetic scan, with exactly the same output and observer scope.

## Exact execution and validation scope

The published JavaScript certificate runs the exact residue-12 elimination kernel and compares it with independent rectangular brute-force enumeration for 945 bounded inequality systems (0<=d,e<=8, one additional row a*d+b*e+c>=0, a in {-4,-3,-2,-1,0,1,2,3,4} with |a| dividing 12, b in [-3,3], c in [-7,7]); each feasible result also reconstructs an integer witness. Output: ALL_CHECKS_PASS.

An independent Python implementation performs the full five-color suffix/first-source oracle with the same modulus-12 elimination and compares its supports against the independent ten-native-letter KMP and BRC append recurrence for *all* base fibers of n=0..4, separately for aab and aba. Counts of base/joint fibers by length: n=0 (1/1), n=1 (10/10), n=2 (55/68), n=3 (220/323 aab; 220/324 aba), n=4 (712/1218 aab; 712/1219 aba). It also checks 144 longer exact positive witnesses from n in {8,16,32,64,128,256}. The local full Python code and its original run log are retained in the accompanying research evidence package. Finite checks validate implementations; the all-n theorem follows from the symbolic integer elimination.

## Complexity, continuation and open problem

Per-fiber support and its cardinality k_g(x) now require constant arithmetic work. PREFIX-496 dense rank R(s)=sum_{base fiber r'<r(s)} k_g(r') + ord_{C_g(x)}(q,t) still needs the *weighted prefix sum* over base fibers. The sum is not computed by the present membership oracle alone.

Next PREFIX-501: derive an exact dimension-fixed weighted prefix-count representation for k_g over lexicographic y,W,V intervals. One candidate is finite Presburger partition plus a fixed-dimensional lattice-point counting structure; investigate concrete integer-sum formulas and their preprocessing, bit complexity, rank/unrank and native append cost. Preserve the frozen scientific pin and test against PREFIX-496 exact n<=9 joint counts. In particular determine whether a practical representation can avoid the O(N^8) explicit joint support table without shifting the cost to an equally large prefix index.

Sources: project PREFIX-496, PREFIX-497, PREFIX-498, PREFIX-499 at their committed Git objects; native P000/ACTIVE Heartbeat World and observer-preservation records; current docs/PORTABLE_RESEARCH_PROTOCOL.md; global math/code policies. Mathematical proof in this note is self-contained relative to PREFIX-499's proved suffix/occupancy bijections.