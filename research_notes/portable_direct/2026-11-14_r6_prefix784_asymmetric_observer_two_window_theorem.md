# PREFIX-784 — Asymmetric corner budgets and a disconnected sign-loss set

Date: 2026-11-14. Scientific status: AUTHOR_PROVED / EXACT_RATIONAL_REGRESSION / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged).
Historic Researcher-ID: EM-DIRECT-E77192. Historic Activity: RA-66BBE259AEE1AD543D9454A3.
Lineage: PREFIX-781, PREFIX-782, PREFIX-783; external 189-layer BRC–Gamma scalar auxiliary-model observer. Independent science; not a native X6 claim.

## Question

PREFIX-783 proves exact pointwise sign-loss under reflection-paired symmetric private-corner budgets. Allow the observed base and reflected private corner errors to have different, potentially one-sided intervals. Can one still compute the exact parameter values where both strict mixed signs cease to be guaranteed?

Fix m>=1 abstract cells, two for the adjacent diagonal Gamma grid squares. For q>0 put x_i(q)=A_i-q B_i, with rational A_i and positive rational B_i. In the frozen Gamma model the A_i and B_i have their original exact values; this section derives a general algebraic theorem valid for any such inputs.

The base shared scalar-corner error h belongs to H=[h_l,h_u]; its reflection h' belongs to H'=[h'_l,h'_u]. Impose |h-h'|<=delta with delta>=0. For cell i the signed sum of the three other base-corner errors u_i varies independently over the closed interval U_i=[l_i,r_i]; the corresponding reflected private sum v_i independently varies over V_i=[l'_i,r'_i]. These are the full attainable interval sums of independently variable signed corner errors. The private-corner sets of the two diagonal squares are distinct. For general m the setup is an abstract shared-corner star, not a geometric embedding claim.

The normalized observed mixed differences are
\[
 a_i=x_i(q)+h+u_i,\qquad
 a'_i=-\bigl(x_i(q)+h'+v_i\bigr).
\]
Sign loss means all 2m entries are nonnegative or all are nonpositive. Strict two-sign persistence means every admissible observer has at least one positive and one negative entry.

## Theorem 784.1 — exact affine interval elimination

For each of the two sign orientations construct four sets of affine functions of q. All constants below denote constant affine functions.

If all observed differences are required to be nonnegative, define
\[
\begin{aligned}
L_I&=\{h_l\}\cup\{-A_i+qB_i-r_i\}_i,&U_I&=\{h_u\},\\
L_J&=\{h'_l\},&U_J&=\{h'_u\}\cup\{-A_i+qB_i-l'_i\}_i.
\end{aligned}
\]
If all observed differences are required to be nonpositive, define
\[
\begin{aligned}
L_I&=\{h_l\},&U_I&=\{h_u\}\cup\{-A_i+qB_i-l_i\}_i,\\
L_J&=\{h'_l\}\cup\{-A_i+qB_i-r'_i\}_i,&U_J&=\{h'_u\}.
\end{aligned}
\]
For either orientation the *exact* feasibility condition at real q>0 is that every inequality in the following four families holds:
\[
\boxed{\begin{gathered}
l\le u\quad(l\in L_I,\ u\in U_I),\\
l\le u\quad(l\in L_J,\ u\in U_J),\\
l\le u+\delta\quad(l\in L_I,\ u\in U_J),\\
l\le u+\delta\quad(l\in L_J,\ u\in U_I).
\end{gathered}}
\]
Each family is a finite collection of rational affine inequalities in q. Its intersection with q>0 is a single interval, possibly empty or unbounded. Therefore the *exact* positive-q sign-loss set is a union of **at most two intervals**, one for each orientation, with rational finite endpoints. The two intervals may be disjoint. All positive finite endpoints are included.

**Proof.** For the nonnegative orientation, maximizing each independent base private sum over [l_i,r_i] and minimizing each independent reflected private sum over [l'_i,r'_i] leaves the constraints h>=-x_i-r_i and h'<=-x_i-l'_i. Thus permissible shared values are h in I=[max L_I,min U_I], h' in J=[max L_J,min U_J]. For the nonpositive orientation, minimize each base private sum and maximize each reflected sum; this yields exactly the other two intervals. After these independent choices, each orientation is feasible if and only if I and J are nonempty and some h in I, h' in J satisfy |h-h'|<=delta. Two nonempty closed real intervals [L,U],[L',U'] contain such a pair exactly when L<=U'+delta and L'<=U+delta. Expanding the minima/maxima gives the four families. Conversely feasible h,h' and the chosen private endpoints produce an actual observer; independently variable per-corner intervals realize the aggregate endpoints by signed Minkowski addition. Each inequality is of the form (p-p')q<=r'-r+delta_or_zero. Its real solution is a half-line, all half-lines intersect in one closed interval, and q>0 removes q=0 if present. Union the two orientations. QED.

**Algorithm.** Enumerate the four families; each pair of affine entries yields one rational linear inequality. If its q coefficient is positive, update the upper endpoint; if negative, update the lower endpoint; if zero, check the constant inequality. This takes O(m^2) rational comparisons on explicitly given coefficients. No numerical root search or external LP solver is required; this operation bound is not a bit-complexity or native X6 runtime estimate.

## Theorem 784.2 — exact disconnected witness even with zero-containing errors

Choose m=2,
\[
 A_1=1,\quad A_2=8,\quad B_1=1,\quad B_2=2,\quad
 D=A_2B_1-A_1B_2=6>0.
\]
Set h=h'=0 and delta=0. Let
\[
 U_1=[0,1],\quad V_1=[0,3],\qquad
 U_2=[-2,0],\quad V_2=[-6,0].
\]
Every private-error interval contains zero; each can be realized by a single signed corner error with the other two held at zero. The exact positive-q feasibility windows from Theorem 784.1 are:
\[
 \text{all entries }\ge0\iff q\in[1,2],\qquad
 \text{all entries }\le0\iff q\in[3,4].
\]
Hence the sign-loss set equals [1,2] union [3,4], a disconnected set. For all 2<q<3, already the first two base differences have opposite strict signs:
\[
 a_1=1-q+u_1\le2-q<0,\qquad
 a_2=8-2q+u_2\ge6-2q>0.
\]
The normalized strict-sign margin is at least min(q-2,6-2q), equal to 1/2 at q=5/2. This is a sharp counterexample to transferring the single-interval conclusion of PREFIX-781–783 to asymmetrically calibrated observations. Its A/B are an exact algebraic illustration, not a substitution for the frozen Gamma coefficients.

## Reproducible validation and limits

Companion Python standard-library Fraction program: PREFIX784_R6_ASYMMETRIC_CORNER_WINDOWS_CHECK.py. Companion JSON: PREFIX784_R6_ASYMMETRIC_CORNER_WINDOWS_RESULTS.json. The implementation forms the affine endpoint constraints, independently checks pointwise feasibility by interval distance, verifies the disjoint rational witness and exercises 1,536 seeded rational examples with 21,256 orientation probes and 2,647 exact boundary probes. Local outcome: ALL_CHECKS_PASS PREFIX784 ASYMMETRIC_CORNER_WINDOWS. The general theorem follows from the preceding proof; finite tests are regression evidence.

This abstract scalar observer carries provenance-labeled signed private-corner intervals and a shared reflection-pair defect. A single symmetric global radius discards orientation information and can erase the disconnection. There is no new computation of the native BRC recurrence, no native Cell/Link/Port/event-time map, and no increment to original comparator exclusion counts.

**Next question.** Identify the native BRC/X6 observer's actual signed source, incidence and time constraints. If their attainable error set factors into these intervals, substitute actual pinned Gamma A_i,B_i to compute exact q windows. If errors are correlated, construct the joint provenance-preserving feasibility polytope; independent interval outer bounds still yield a sound sufficient two-sign persistence certificate but generally not a necessary one. Do not duplicate a shared event into independently chosen observed corners.

Sources: PREFIX-781, PREFIX-782 and PREFIX-783 exact author research, awdawmip/enterprise-math/research_notes/portable_direct/; global P000/ACTIVE worldview and current research protocol read separately. Author proof; no independent mathematical review/admission claimed.
