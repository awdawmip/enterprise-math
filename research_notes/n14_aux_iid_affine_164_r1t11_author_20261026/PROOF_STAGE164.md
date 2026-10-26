# Stage164: full-real optimal affine interval and strict right sharpness (R1 author)

**Scientific status:** Exact rational computation-assisted AUTHOR proof in the **external** ternary iid sequential testing model (horizon 14). Not an independently reviewed Research Driver Result, a canonical native CLAIM, or a theorem about P000 X6.

## Frozen sources, model and declared observers

GLOBAL_KNOWLEDGE_V1 at main@ad6b20175a75b09038ffaa5e43ec737463299e1e; EM source at main@658da84476e2ed11d5b243f35246ca0c4aefdb7c; both established by current remote branch read. At that same immutable global pin: 00_BOOTSTRAP.md, OPERATING_MANUAL.md, project Task researcher bootstrap, P000_STARTUP.json (original P000 Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc checked), ACTIVE worldview and mathematics/BRC policies. Current EM docs/PORTABLE_RESEARCH_PROTOCOL.md and Stage163 proof/Stage164 dual candidate were read at the EM pin. Stage163 is consumed, not re-proved.

Ordered observations are iid on alphabet {0,1,2}:
[
P=(1/8,1/24,5/6),qquad Q=(1/12,1/12,5/6).
]
For arbitrary full-ordered-history randomized stopping and decision rules with stopping time τ≤14, let
[
e_P=P(	ext{decide Q}),quad e_Q=Q(	ext{decide P}),quad
t_P=E_P τ,quad t_Q=E_Q τ.
]
Set (V_{14}(alpha)=inf_{e_P,e_Qlealpha}max(t_P,t_Q)). This is external to P000; no embedding or observer-preserving map to the six-native-axis Cell model is claimed.

## Exact theorem

For EVERY real number
[
0le deltale
oxed{rac{17071484375}{17158292304297984}},
]
the value function satisfies
[
oxed{
V_{14}(alpha_{163}+delta)
=V_{163}-rac{1249192}{2175}delta
}
]
where
[
alpha_{163}=rac{440628382682516376365}{1265046575011281764352},qquad
V_{163}=rac{2138687275177334037541}{180720939287325966336}.
]
The new right endpoint and value are
[
oxed{alpha_{164}=rac{62947091618416625195}{180720939287325966336}},qquad
oxed{V_{164}=rac{2138584004831606037541}{180720939287325966336}}.
]
For every (alpha>alpha_{164}) within the nontrivial error-bound domain, this Stage164 supporting affine line lies **strictly below** (V_{14}(alpha)).

## Bellman dual certificate (all ordered policies)

Use state (s=(n,a,b)), where (a,b) count symbols 0,1, and (nle14). Under an ordered prefix the likelihood ratio is (Q(prefix)/P(prefix)=ell(s)=2^{a+b}/3^a). Put
[
K=rac{211248}{725},qquad L=rac{615448}{2175},qquad K+L=rac{1249192}{2175}.
]
At nonterminal (s), define
[
H(s)=min{Kell(s),L,1+sum_{i=0}^{2}P_iH(s+e_i)};
]
at (n=14) omit the continuation. Exact Fraction evaluation of ALL 680 states returns
[
H(0)=rac{5049070838648186965277}{23829526702026915840}.
]
There are precisely two action ties, (R=(10,0,1)) (Q/continue), (S=(13,5,2)) (P/continue); all 1238 other nonminimal action gaps are strictly positive, smallest (141134197/6494515200), with no negative gap. Bellman induction gives for every full-history randomized policy
[
H(0)le t_P+K e_Q+L e_Ple max(t_P,t_Q)+(K+L)alpha.
]
Thus (H(0)-(K+L)alpha) is a universal lower bound, independent of any count-state restriction on the admissible policy.

## BRC-retained ordered prefixes and primal attainment

Retain ordered branch labels, full first-hit prefix, decision, stopping depth and exact positive rational masses under both P and Q. A count quotient is used only for the declared suffix-conditional four observers (M=(e_P,e_Q,t_P,t_Q)), because equal-count histories have identical iid suffix laws and equal Q/P ratios. This is NOT native X6 quotient authorization.

At the tie R let (r) denote immediate Q probability, at tie S let (s) denote immediate P probability. Elsewhere use the uniquely Bellman-optimal action. Literal unmerged ordered-path integer DFS and independent count-suffix rational recursion agree at all four corners ((r,s)in{0,1}^2); both P and Q terminal masses are exactly 1 at each corner. First-hit information:

| Tie | Ordered first-hit histories | P mass | Q mass |
|---|---:|---:|---:|
| R=(10,0,1) | 10 | 9765625/120932352 | 9765625/60466176 |
| S=(13,5,2) | 12056 | 23546875/110075314176 | 23546875/208971104256 |

R cannot reach S: after depth 10 its first-symbol count is 0 and only three observations remain, yet S requires first-symbol count 5. S is deeper than R. Therefore the real ordered first-hit cones do not overlap. For every (r,sin[0,1]) the four-observer vector is **exactly affine**:
[
M(r,s)=M_{00}+r,d_R+s,d_S,qquad M_{11}-M_{10}-M_{01}+M_{00}=(0,0,0,0).
]
Exact observer vectors, in order ((e_P,e_Q,t_P,t_Q)):
[
M_{00}=left(
rac{608967817797479015}{1752976676930715648},
rac{28012606842025}{80244904034304},
rac{2600402594943262961}{219122084616339456},
rac{17057348411101}{1486016741376}
ight),
]
[
d_R=left(
rac{4521484375}{1486016741376},
-rac{3232421875}{1253826625536},
-rac{61181640625}{557256278016},
-rac{20751953125}{104485552128}
ight),
]
[
d_S=left(
-rac{23546875}{2641807540224},
rac{23546875}{2507653251072},
-rac{23546875}{110075314176},
-rac{23546875}{208971104256}
ight).
]
Exact equality (e_P=e_Q) is equivalent to
[
oxed{r(s)=
rac{1786149721302671}{5911808000000000}
+rac{751993}{230930000}s},quad 0le sle1.
]
Both tie probabilities lie strictly between 0 and 1 for the entire segment except that (s=1) saturates the new tie. Along this segment (alpha(s)=alpha_{163}+s(alpha_{164}-alpha_{163})) exactly. In particular, the left endpoint matches the published Stage163 value with exact zero difference. At the two ends the exact time gaps are, respectively,
[
t_P-t_Q=rac{525795582839779772735}{1265046575011281764352}>0,quad
rac{25049209729437132035}{60240313095775322112}>0.
]
Direct exact substitution gives (t_P+K e_Q+L e_P=H(0)) at each end. All four quantities are affine in s, hence both positive time gap and dual equality persist for EVERY real s∈[0,1]. Since (t_Pge t_Q), this attains the Bellman bound and proves the claimed whole interval.

## Strict right sharpness

The space of full ordered-history randomized finite-horizon behavioral policies is compact (finite products of action simplices); the value minimum is attained. Equality with the above line at any α>α164 would, since K,L>0, force (e_P=e_Q=alpha), (t_P=max(t_P,t_Q)), and equality at every positively visited Bellman state. All positive gaps exclude nonoptimal actions. Only R and S may randomize. At the same count state, ordered histories share the same likelihood ratio and suffix distributions, so arbitrary history-dependent tie coins have a single mass-weighted effective coin for the four observers. Since the tie prefix cones are disjoint, every equality policy has exactly M(r,s) above, with (0le r,sle1). Equality of errors forces r(s); monotonicity of α(s) implies (alphalealpha_{164}), contradiction. Strict support loss to the right follows.

## Actual checks, caveats and next

Locally executed independent author program verify_stage164.py (Fraction Bellman/count suffix and literal ordered DFS): 680 states, 1238 strictly positive gaps, 0 negative, four corners exactly identical, mixed term exactly zero, ordered DFS node counts 445864/409696/445624/409456 (corners 00/01/10/11), total mass 1 under P,Q. All exact endpoint identities and inherited Stage163 matching PASS. Independently executed tangent dual scan: Stage165 candidate K=13623672285/49693891, L=40009085000/149081673, new tie (10,7,3) P/continue, old R Q/continue; 680 states, 1238 positive nonminimal gaps. Stage165 primal is UNPROVED.

The GitHub PORTABLE_VERIFY_STAGE164.py is a source adaptation of the previously published Stage163 portable verifier. The independently executed program and stdout evidence are in the local R1T11 evidence bundle; a GitHub upload is not a remote execution test and byte equality between those two programs is not claimed. Verification is AUTHOR exact computation-assisted, not native Research Driver independent review. Current native dispatch read failed CONTROL_QUOTA, session_start failed STATIC_READONLY_SCOPE_DENIED with operation_sent=false: no owner/CLAIM/Result acceptance claimed. Native X6/P000 correspondence remains open.