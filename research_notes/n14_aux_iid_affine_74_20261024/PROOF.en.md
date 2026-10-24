# N=14 auxiliary iid sequential decision model — the 74th exact affine interval

**Classification:** author-side exact finite mathematical proof; independently checked by two exact-rational programs which share the inherited deterministic stop table. No independent Research Driver acceptance, native CLAIM, or BRC/X6/Heartbeat transfer is asserted.

## Statement and notation

Fix N=14 and iid symbols 0,1,2 with P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6). For a possibly randomized sequential policy stopping by N, write e_P=P(declare Q), e_Q=Q(declare P), t_P=E_P[T], t_Q=E_Q[T], and

\[
V_{14}(\alpha)=\inf_{e_P,e_Q\leq\alpha}\max(t_P,t_Q).
\]

The inherited 73rd endpoint (author-checked, not independently Driver-admitted) is

\[
\alpha_{73}=\frac{2585970555518493847}{7450150876955541504},\quad
V_{73}=\frac{24569599527714816749}{1862537719238885376},\quad
s_{73}=\frac{11935611272766011}{20889600000000000}.
\]

The last number is the Q-stopping coin at B=(12,0,1). In the inherited deterministic stop table the previous tie A73=(8,6,1) now always declares P. Its complete action definition is preserved in verify_n14_74.py, evolved from the immutable 73rd source commit 44b91386326e39d851697927ca33db98baf86f4e.

**Theorem.** Put
\[
K_{74}=\frac{20412}{5},\qquad
\lambda_P=72+\frac89K_{74}=\frac{18504}{5},\qquad
\lambda_Q=K_{74}=\frac{20412}{5},\qquad
\Gamma=\lambda_P+\lambda_Q=\frac{38916}{5},
\]
and
\[
\eta_{74}=\frac{6015625}{22455364091904}.
\]
For every real number \(0\leq\delta\leq\eta_{74}\),
\[
\boxed{V_{14}(\alpha_{73}+\delta)=V_{73}-\Gamma\delta}.
\]
In particular,
\[
\boxed{\alpha_{74}=\frac{2585972551358493847}{7450150876955541504}},\qquad
\boxed{V_{74}=\frac{24565716022242816749}{1862537719238885376}}.
\]
The Bellman support line is right-sharp: for alpha greater than this endpoint no policy can attain the same support lower bound with equality. This does not assert differentiability or nondifferentiability of the value function.

## Exact dual certificate: complete finite state coverage

The sufficient external-model state is (n,a,b), where n counts observations and a,b count symbols 0 and 1 respectively. The positive likelihoods satisfy Q/P=2^(a+b)/3^a. Under the P reference measure, the Lagrangian t_P+lambda_P*e_P+lambda_Q*e_Q has action values

\[
D_P(n,a,b)=\lambda_Q\frac{2^{a+b}}{3^a},\qquad
D_Q(n,a,b)=\lambda_P,
\]
\[
D_C(n,a,b)=1+\sum_{i=0}^2P_iD(n+1,a+1_{i=0},b+1_{i=1}).
\]

At n=14, continuing is unavailable. The Python verifier calculates D from n=14 down to n=0 and compares every nonselected action against the inherited chosen action. Exactly
\[
\sum_{n=0}^{14}(n+1)(n+2)/2=680
\]
states and 1240 nonselected action gaps are covered. **1238 are strictly positive, none negative; only two vanish:**
\[
A_{74}=(12,5,1):\quad C=P,\qquad
B=(12,0,1):\quad C=Q.
\]
The smallest strictly positive gap is 417599/4976640. The exact root value is
\[
\boxed{D(0,0,0)=\frac{185895261266750005303}{68475651442606080}}
=V_{73}+\Gamma\alpha_{73}.
\]

This exhaustive rational computation certifies all Bellman inequalities because every successor state is at higher n, and all 680 states are visited with exact Fraction arithmetic. Consequently, for every randomized feasible strategy,
\[
\max(t_P,t_Q)\ge t_P\ge D(0,0,0)-\lambda_P e_P-\lambda_Qe_Q
\ge D(0,0,0)-\Gamma\alpha.
\]

## First-hit mass and truncation of ordered histories

The nominal count of ordered length-12 words with A74=(12,5,1) is 12!/(5!1!6!)=5544. Precisely **4158** survive all earlier stopping rules, while 1386 are stopped earlier. The surviving first-hit P and Q masses are
\[
p_A=\frac{1203125}{679477248},\qquad
q_A=\frac{1203125}{2579890176}.
\]
At B exactly 12 first-hit histories survive, with
\[
p_B=\frac{48828125}{725594112},\qquad
q_B=\frac{48828125}{362797056}.
\]

Starting at A74 and continuing (before enabling the early-P coin) yields exactly these five distinct terminal local words:

| Terminal stop / decision | Local words | Conditional P mass | Conditional Q mass |
|---|---:|---:|---:|
| (13,5,1), P | 1 | 5/6 | 5/6 |
| (13,6,1), P | 1 | 1/8 | 1/12 |
| (14,5,2), P | 1 | 5/144 | 5/72 |
| (14,5,3), Q | 1 | 1/576 | 1/144 |
| (14,6,2), P | 1 | 1/192 | 1/144 |

All conditional masses sum to 1 under each hypothesis. Switching on early stopping at A74 truncates five completed stopping suffixes per live first-hit history, i.e. **20,790** ordered completed stopping histories: 8,316 length-13 and 12,474 length-14 terminal histories. These are path counts, not probability weights.

The exact conditional continuation risk vectors, ordered as (P-error, Q-error, remaining P-time, remaining Q-time), are
\[
c_A=(1/576,143/144,25/24,13/12),\qquad
c_B=(63/64,1/144,9/8,13/12).
\]

## Continuous interval: explicit randomized primal certificate

Let u in [0,1] be the probability of early P at A74; otherwise continue using the inherited table. Let s in [0,1] be the probability of early Q at B. The two sites are at the same depth n=12 but at different count states, so an ordered path cannot visit both. Consequently all four risk functions are exactly affine in (u,s), with zero mixed coefficient u*s. An independent backward recursion also verifies every one of these mixed terms at the four deterministic corners.

Define
\[
X=p_Ac_{A,e_P}=\frac{1203125}{391378894848},\qquad
Y=q_A(1-c_{A,e_Q})=\frac{1203125}{371504185344},
\]
\[
E=p_B(1-c_{B,e_P})=\frac{48828125}{46438023168},\qquad
H=q_Bc_{B,e_Q}=\frac{48828125}{52242776064}.
\]
Relative to the former endpoint (u=0,s=s73), the exact changes are
\[
\Delta e_P=-Xu+E(s-s_{73}),\qquad
\Delta e_Q=Yu-H(s-s_{73}).
\]
Their equality forces
\[
s=s_{73}+h_{74}u,\qquad
\boxed{h_{74}=\frac{X+Y}{E+H}=\frac{345807}{108800000}}.
\]
The common error increase is exactly
\[
e_P=e_Q=\alpha_{73}+\eta_{74}u,\qquad
\eta_{74}=Eh_{74}-X=\frac{6015625}{22455364091904}>0.
\]
The coin remains feasible on the whole real interval:
\[
0<s_{73}<s_{74}=\frac{12002006216766011}{20889600000000000}<1.
\]

At u=0 and u=1 the positive t_P-t_Q gaps are respectively
\[
\frac{276634099139617787}{465634429809721344},\qquad
\frac{276114249347617787}{465634429809721344}.
\]
The gaps are affine in u, hence t_P is the worst expected sample count throughout [0,1]. The construction chooses only zero-gap Bellman actions, so
\[
t_P+\lambda_Pe_P+\lambda_Qe_Q=D(0,0,0).
\]
Therefore \(t_P=V_{73}-\Gamma\eta_{74}u\) achieves the universal dual bound for **every real u**, which proves the theorem for all real delta in the closed interval, not merely the seven test values.

## Right-end sharpness

The 1238 strictly positive Bellman gaps force every action of any strategy attaining equality on the same support line to agree with the fixed stop table, except randomized choices at A74 and B. Both tie states have positive first-hit P mass. Since lambda_P and lambda_Q are strictly positive, equality of the error upper-bound step requires *both* e_P=e_Q=alpha. The risk formulas above then force s-s73=h74*u and alpha=alpha73+eta74*u with u in [0,1]. Hence alpha cannot exceed alpha74 in any strategy attaining the same dual bound. This proves the precise support-line sharpness claim.

## Reproduction and scope

The complete two executable Python files are verify_n14_74.py and verify_n14_74_crosscheck.py. The first checks all Bellman states/actions, exact forward risks at endpoints and seven rational interpolation points, then locates only an *exploratory* next crossing. The second shares the inherited stopping table but uses an independent backward risk recurrence, DFS enumeration of surviving ordered histories, local suffix enumeration, and four-corner mixed-coefficient checks. Both use Python's standard-library fractions.Fraction. The full Chinese exposition and original exact output files also appear in the companion reproducibility archive.

The **candidate only** for the next segment, after freezing A74 to P, is
\[
K_{75}^{candidate}=\frac{35653474730376}{9239954171},\qquad
A_{75}^{candidate}=(4,1,3),\qquad C\leftrightarrow Q.
\]
Neither the 75th segment nor independent source/Driver admission has yet been proved. Inherited stop rules are shared by the two local verifiers, and this work makes no claim of native BRC/X6/Heartbeat correspondence, external originality, Lean formalization or P000/worldview changes.
