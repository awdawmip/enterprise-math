# X6 R109 — A sharp twelve-direction theorem on a four-weight BRC cone

2026-11-22 · \`AUTHOR_PROOF / EXACT_INTEGER_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED\`.

Scientific input is the **conditional auxiliary four-positive-weight, six-pair BRC observer** of R104–R108, with the frozen P000 premise unchanged at \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`. This is a three-dimensional integer-difference observer *within* the fixed X6 research program, not an assertion of native Cell/Link/heartbeat dynamics.

## Exact definitions

For \`a=(x,y,z)∈Z^3\setminus{0}\`, identify \`a\` and \`-a\` and set
\[
q(a)=\max\{\sum_i\max(a_i,0),\ \sum_i\max(-a_i,0)\}.
\]
Its exact integer moments are
\[
u=x+3y+6z,\quad v=3x+12y+30z,\quad h=7x+39y+126z.
\]
For positive \`w=(A,B,C,D)\`, retain all six pair observers:
\[
F_w(a)=\max\left\{\frac{|u|}{A+B},\frac{|v|}{A+C},\frac{|h|}{A+D},
\frac{|v-u|}{B+C},\frac{|h-u|}{B+D},\frac{|h-v|}{C+D}\right\}.
\]
For an integer Port budget \`p≥11\`, let \`\eta_p(w)\` be the minimum of \`F_w\` among nonzero \`a\` with \`q(a)≤p\`. Let \`N_p(w)\` comprise *unoriented* feasible differences satisfying \`F_w(a)<3\eta_p(w)/2\`.

## Theorem — sharp 12 bound on a full cone

Assume all four weights are positive and
\[
\boxed{B\le A,\qquad B\le D,\qquad A\le C,\qquad B+D\le8(A+B).}\tag{H}
\]
For **every integer** \`p≥27\`,
\[
\boxed{|N_p(A,B,C,D)|\le12.}
\]
The bound is **sharp within the cone**: the weights \`(9,1,58,41)\` attain 12 for every \`p≥38\`. The region (H) is homogeneous and has nonempty four-dimensional interior, and has arbitrarily large \`C\` at fixed \`A,B,D\`.

### Infinite-lattice proof

Reuse two actual feasible differences:
\[
s=(10,-5,1),\ q(s)=11,\ (u,v,h)(s)=(1,0,1);
\qquad t=(24,-14,3),\ q(t)=27,\ (u,v,h)(t)=(0,-6,0).
\]
The weight ordering in (H) makes
\[
F_w(s)=\frac1{A+B},\quad
F_w(t)=\frac6{B+C}.
\]
Therefore for every \`p≥27\`,
\[
\eta_p(w)\le\frac1{A+B},\qquad\eta_p(w)\le\frac6{B+C}.\tag{1}
\]
For any \`a∈N_p(w)\`, applying the relevant three *retained pair* coordinates and (1) yields the **strict integer bounds**
\[
|u|<\tfrac32,\quad |v-u|<9,\quad
|h-u|<\tfrac32\frac{B+D}{A+B}\le12.\tag{2}
\]
Consequently \`|u|≤1\`, \`|v-u|≤8\` and \`|h-u|≤11\`.

Now suppose \`a\` belongs to the mod-3 sign orbit \`L=\{\pm(0,1,2)\}\` in the original \`(x,y,z)\` coordinates. Orient it so \`x≡0,y≡1,z≡2 (mod 3)\`. Since \`u≡x (mod 3)\`, the first bound in (2) forces \`u=0\`. Then \`x=-3y-6z\` and
\[
v=3y+12z=3(y+4z)\equiv0\pmod9.
\]
Because \`|v|=|v-u|<9\`, necessarily \`v=0\`. The two equations \`u=v=0\` imply
\[
(x,y,z)=(6z,-4z,z),\qquad h=12z.
\]
The final bound \`|h-u|<12\` forces \`z=0\`, contradicting \`a≠0\`. Thus **no near-optimal direction lies in the single sign-orbit \`L\`**.

R104 proves, by the exact \`(a-b)/3\` argument and Port subadditivity, that distinct members of \`N_p(w)\` occupy distinct nonzero mod-3 sign-orbits. There are 13 such orbits, one of which \`L\` is now excluded. Hence \`|N_p(w)|≤12\`. This uses the entire infinite integer lattice, all real weights satisfying (H), and every \`p≥27\`. QED.

**Why this advances R104–R108:** R104 had an all-weight bound of 13 and a 12-direction example; R106 proved a small four-dimensional robustness box; R108 classified one positive \`C\`-ray. This theorem proves an exact 12 bound on the much larger four-weight cone (H), by excluding a specific residue orbit with only three retained observer inequalities. It does **not** settle the global 12-versus-13 question outside (H).

## Sharpness: exact self-contained witness

Take \`w_*=(9,1,58,41)\`. It satisfies (H): \`1≤9\`, \`1≤41\`, \`9≤58\`, and \`42≤80\`. For any \`p≥11\`, the vector \`s\` has score \`1/10\`. Conversely any nonzero integer difference has score at least \`1/10\`:

* If \`u≠0\`, the \`A+B=10\` pair immediately gives \`F≥1/10\`.
* If \`u=0,h≠0\`, the exact integrality relation \`h-u≡0 (mod 6)\` gives \`F≥6/42=1/7>1/10\`.
* If \`u=h=0,v≠0\`, \`v≡0 (mod 3)\` and \`h-u-6v≡0 (mod 12)\` imply \`v∈6Z\`, hence \`F≥6/59>1/10\`.

Invertibility of the moment matrix rules out \`u=v=h=0\` for nonzero \`a\`. Thus \`\eta_p(w_*)=1/10\` for every integer \`p≥11\`.

At this weight, \`F<3/20\` is equivalent to the six exact integer moment bounds
\[
|u|\le1,\quad |v|\le10,\quad |h|\le7,\quad
|v-u|\le8,\quad |h-u|\le6,\quad |h-v|\le14.\tag{3}
\]
The integer moment inverse and integrality conditions are
\[
x=(h+19u-8v)/2,\quad
y=(-h-14u+7v)/3,\quad z=(h+11u-6v)/12,
\]
\[
v\equiv0\ (3),\qquad h-u\equiv0\ (6),\qquad h-u-6v\equiv0\ (12).
\]
Enumerating (3) and those three congruences gives exactly 24 nonzero oriented vectors, or twelve unoriented directions, all with \`q≤38\`. The twelve (ordered by minimum Port) are:

| direction \`(x,y,z)\` | \`q\` | exact \`F_{w_*}\` |
|---|---:|---:|
| \`(1,0,0)\` | 1 | \`1/7\` |
| \`(5,-4,1)\` | 6 | \`1/7\` |
| \`(9,-5,1)\` | 10 | \`1/7\` |
| \`(10,-5,1)\` | 11 | \`1/10\` |
| \`(14,-9,2)\` | 16 | \`1/10\` |
| \`(15,-9,2)\` | 17 | \`1/7\` |
| \`(19,-10,2)\` | 21 | \`1/7\` |
| \`(23,-14,3)\` | 26 | \`1/7\` |
| \`(24,-14,3)\` | 27 | \`6/59\` |
| \`(25,-14,3)\` | 28 | \`1/7\` |
| \`(29,-18,4)\` | 33 | \`1/7\` |
| \`(34,-19,4)\` | 38 | \`7/59\` |

Every displayed value is strictly less than \`3/20\`. No additional integer vector, regardless of Port, can satisfy the six bound box. Hence **exactly twelve** exist for every \`p≥38\`, and the cone-wide upper bound is attained.

## Evidence and verification

Companion reproducible checker: \`research_notes/portable_direct/x6_r109_twelve_cone_verify.py\`. It performs exact rational scoring (\`fractions.Fraction\`), enumerates the complete congruence-bounded moment box, verifies the 24 oriented/12 unoriented counts and 12 distinct nonzero mod-3 orbits, checks each listed direction against the threshold and Port budget, and independently scans the complete original integer-difference set \`q≤38\`. The generated result certificate is \`x6_r109_twelve_cone_results.json\`. On the author-side run, all assertions passed.

The all-weight cone upper bound is the analytic proof above; the executable finite check verifies the sharpness witness. Neither is a claim of independently reviewed mathematical admission. No P000 modification, official native X6 CLAIM/PROGRESS or native physics computation was performed.

## Next exact question

On the complementary region \`B>A\` **or** \`B>D\` **or** \`A>C\` **or** \`B+D>8(A+B)\`, decide whether 13 mod-3 sign-orbits can all contain strict \`3/2\`-near representatives. An exact first discrimination is to determine whether a different pair of feasible short vectors and three retained observer inequalities excludes *another* sign-orbit on subregions; only then consider a certificate of global 12 or an exact 13-point witness. Preserve all six pair interactions when changing or compressing the observer, and keep the P000 native mapping question separate.

Source references: R104 \`research_notes/portable_direct/2026-11-22_x6_r104_thirteen_class_robust_gap_and_finite_box.md\`; R106 \`research_notes/portable_direct/2026-11-22_r2_x6_r106_robust_twelve_chamber.md\`; R108 \`research_notes/portable_direct/2026-11-22_r2_x6_r108_full_C_positive_ray_port_near_atlas.md\`.
