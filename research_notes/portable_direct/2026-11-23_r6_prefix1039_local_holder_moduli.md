# PREFIX-1039 — Local optimized half-Hölder bounds enlarge both certified positive spectral neighborhoods

Date: 2026-11-23 (Asia/Shanghai). Parent: PREFIX-1038. Status: AUTHOR_EXACT_CONDITIONAL_PROOF / EXACT_FRACTION_CHECKED / NOT_INDEPENDENTLY_REVIEWED.

## Scope, immutable inputs and operator typing

Frozen P000 V5 scientific input: \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json\`; Stage46 signed BRC \`W=J12-6I12\`, incoming \`-e1\`, blocked bidirectional Link \`{0,e1}\`, exactly one negative outgoing step. Full native X6 Cell–terminal-port–grade, branch multiplicity, sign and provenance remain retained. This is a theorem **conditional on the inherited auxiliary six-phase scalar spectral integral**, not a native-state reduction or new native BRC computation. It neither executes a new classical comparison with the native model nor attributes a residual. Native attribution remains \`NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION\`.

Verified parents (preserve their exact scope):
- PREFIX-1037 \`928461a6f8c675b9a7bd38586cf47db9d25835e9:research_notes/portable_direct/2026-11-23_r6_prefix1037_certified_critical_density_positivity.md\`; certified inherited \`g(4)>6371/60\`, \`g(16)>919/90\`.
- PREFIX-1038 \`bc77bccbe4befbd9cb69d834e9bbdead032d66bd:research_notes/portable_direct/2026-11-23_r6_prefix1038_explicit_critical_positive_neighborhoods.md\`; earlier \`10^-9\` and \`10^-11\` radii.

Write \`r=√y\`, \`H=y²(36-y)²\`, \`P=y(y-36)(17y-91)\`, \`A=2H'-P\`, \`B=H/r\`, \`C=12(11+y)\`, \`D=r(y-6)\`, \`E=2y\`. The inherited *auxiliary* formula is
\[
g(y)=\int_0^\infty K(t;y)\,dt,\qquad
K(t;y)=\frac{J_0(t)^6}{5}
\left[A\,tJ_0(rt)-B\,t^2J_1(rt)+C\left(DJ_1(rt)-\frac{E}{t}J_2(rt)\right)\right].
\]
We use the same Bessel inequalities and derivative recurrences from PREFIX-1037/1038 without rerunning spectral integrals or changing their native attribution.

## New theorem

For \`x,y∈[7/2,9/2]\`, \`δ=|x-y|≤1\`,
\[
\boxed{|g(x)-g(y)| < 172000\sqrt{\delta}.}
\]
For \`x,y∈[31/2,33/2]\`, \`δ=|x-y|≤1\`,
\[
\boxed{|g(x)-g(y)| < 336000\sqrt{\delta}.}
\]

Combining with the unchanged certified endpoint signs gives the explicit **closed positive neighborhoods**:
\[
\boxed{|y-4|\le10^{-7}\ \Longrightarrow\ g(y)>50,}
\qquad
\boxed{|y-16|\le5\cdot10^{-10}\ \Longrightarrow\ g(y)>5/2.}
\]
The certified radii are respectively 100 and 50 times those in PREFIX-1038.

## Proof: exact coefficient envelopes

Fix a local band \`[a,b]\` and *rational* bounds \`r_-≤√a≤√y≤√b≤r_+\`. Put
\[
v=\max_{y=a,b}|36-2y|,\quad
w=\max_{y=a,b}|17y-91|,\quad
z=\max_{y=a,b}|y-6|,\quad R=(2r_-)^{-1}.
\]
The following are upper bounds for \`|H|,|H'|,|H''|,|P|,|P'|,|A|,|A'|,|B|,|B'|,|C|,|C'|,|D|,|D'|,|E|,|E'|\`, respectively (all positive and in the written order):
\[
\begin{aligned}
\mathcal H&=b^2(36-a)^2,&
\mathcal H_1&=2b(36-a)v,&
\mathcal H_2&=2v^2+4b(36-a),\\
\mathcal P&=b(36-a)w,&
\mathcal P_1&=vw+17b(36-a),\\
\mathcal A&=2\mathcal H_1+\mathcal P,&
\mathcal A_1&=2\mathcal H_2+\mathcal P_1,\\
\mathcal B&=\mathcal H/r_-,&
\mathcal B_1&=\mathcal H_1/r_-+\mathcal H/(2r_-^3),\\
\mathcal C&=12(11+b),&\mathcal C_1&=12,\\
\mathcal D&=r_+ z,&\mathcal D_1&=r_+ +Rz,\\
\mathcal E&=2b,&\mathcal E_1&=2.
\end{aligned}
\]
They follow from product differentiation, \`H''=2(36-2y)^2-4y(36-y)\`, \`P'=(2y-36)(17y-91)+17y(y-36)\`, \`r'=1/(2r)\`; all use triangle inequalities. The bound on \`H''\` is an absolute bound, not an equality.

For \`0≤t≤1\`, use \`|J_\nu^{(j)}|≤1\`, \`|J_2(rt)/t|≤r_+\`, and \`|\partial_y (J_2(rt)/t)|≤R\`. Thus
\[
|\partial_y K|\le S:=\frac15\left[\mathcal A_1+\mathcal A R+\mathcal B_1+\mathcal B R+
\mathcal C_1(\mathcal D+\mathcal E r_+)+
\mathcal C(\mathcal D_1+\mathcal D R+\mathcal E_1 r_++\mathcal E R)\right].
\]
For \`t≥1\`, the already verified bounds \`|J_0(t)|^6≤2t^{-3}\`, \`|J_0(rt)|≤(11/10)t^{-1/2}\`, \`|J_1(rt)|≤2t^{-1/2}\`, \`|J_2(rt)|≤6t^{-1/2}\` and \`|J'_0(rt)|≤2t^{-1/2}\`, \`|J'_1(rt)|≤4t^{-1/2}\`, \`|J'_2(rt)|≤14t^{-1/2}\` yield
\[
|K(t;y)|\le M t^{-3/2},\quad
|\partial_yK(t;y)|\le L t^{-1/2},
\]
with
\[
M=\frac25\left[\frac{11}{10}\mathcal A+2\mathcal B+\mathcal C(2\mathcal D+6\mathcal E)\right]
\]
and
\[
L=\frac25\left[\frac{11}{10}\mathcal A_1+2\mathcal A R+2\mathcal B_1+4\mathcal B R+
\mathcal C_1(2\mathcal D+6\mathcal E)+
\mathcal C(2\mathcal D_1+4\mathcal D R+6\mathcal E_1+14\mathcal E R)\right].
\]
The derivative is integrated only over finite \`[0,T]\`. The improper tails are bounded absolutely; no global differentiability under the improper integral is invoked.

For \`0<δ≤1\`, choose \`T=q/δ\` with \`q≥1\`. The fundamental theorem of calculus on the finite part and the two tails give
\[
|g(x)-g(y)|\le \delta S+2L\delta(\sqrt{T}-1)+4M/\sqrt{T}
\le(S+2L\sqrt q+4M/\sqrt q)\sqrt\delta.
\]

Two rational bands suffice. Each entry is obtained by exact Fraction arithmetic:
| band | \`[a,b]\` | \`[r_-,r_+]\` | \`S\` | \`M\` | \`L\` | \`q\` |
|---|---|---|---|---|---|---|
| near 4 | \`[7/2,9/2]\` | \`[3/2,9/4]\` | \`31329/5\` | \`1030149/40\` | \`585099/20\` | 2 |
| near 16 | \`[31/2,33/2]\` | \`[15/4,17/4]\` | \`13241447/1875\` | \`18701001/200\` | \`266744147/7500\` | 5 |

By rational squares \`4/3<√2<3/2\` and \`20/9<√5<9/4\`, the two modulus coefficients are bounded above by
\[
S_4+3L_4+3M_4=\frac{6851673}{40}<172000;
\]
\[
S_{16}+\frac92L_{16}+\frac95M_{16}
=\frac{2515632017}{7500}<336000.
\]
Finally \`√(10^-7)<1/3100\` since \`3100²<10^7\`, so
\[
g(y)>\frac{6371}{60}-\frac{172000}{3100}>50 \quad (|y-4|\le10^{-7}).
\]
Also \`√(5·10^-10)<9/(4·10^5)\`, since \`√5<9/4\`, so
\[
g(y)>\frac{919}{90}-\frac{336000\cdot9}{4\cdot10^5}>\frac52
\quad (|y-16|\le5\cdot10^{-10}).
\]
All claims are strictly proved by rational inequalities under the inherited auxiliary integral. QED.

## Recalculation, control and next research

The exact verifier \`PREFIX1039_R6_LOCAL_HOLDER_CHECK.py\` recomputes every rational coefficient above from the stated bands and checks endpoint subtractions using Python stdlib \`fractions.Fraction\`. It does not evaluate \`π\`, trigonometric/Bessel samples, native BRC propagation or a new non-BRC classical reference. A prior full native X6–BRC observer correspondence is not claimed.

This is one reusable conditional derived-scalar sharpening; preserve PREFIX-1037/1038 as distinct immutable previous frontiers. Next investigate a certified cover of the remaining spectral gaps \`(0,4)\`, \`(4,16)\`, \`(16,36)\`, and audit the auxiliary integral's precise observer correspondence. A rigorous counterexample would equally settle a local sign question. Independent Review, Activity semantic association, formal Result and mother target \`B_fix,odd(32)∈{19,20}\` remain open. Historical EM-DIRECT-FBEA5D attribution is preserved as prior source only; current logical-session authentication is not inferred from a public SID.
