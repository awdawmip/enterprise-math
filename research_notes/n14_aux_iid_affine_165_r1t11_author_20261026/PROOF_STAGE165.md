# Stage165 exact affine optimum on a full real interval (R1 author proof)

**Scientific status:** AUTHOR_EXACT_COMPUTATION_ASSISTED for an **external** ternary-iid horizon-14 sequential test. This is neither an independently checked Research Driver Result nor a native P000 X6 theorem.

## Fixed sources and mathematical object

GLOBAL_KNOWLEDGE_V1 canonical main **1f73bff7ce37e663922e3c8dd29411441b0e37a7**, Enterprise Math source main **92a0535e556693c942614dc9d92e6561ca594348**. Read fixed 00_BOOTSTRAP, OPERATING_MANUAL, TASK bootstrap, P000_STARTUP (canonical blob **770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc**, original checked), ACTIVE worldview, native X6 and observer-preservation contracts, mathematical/BRC rules and the current PORTABLE_RESEARCH_PROTOCOL. Predecessor Stage164 author proof: commit **611e4903c3a9babc1237b74f0ed3d99df3f33ab0**.

Alphabet {0,1,2}, independent observations, P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6). All randomized, history-dependent ordered-path stopping/decision policies with stopping time τ≤14 are admissible. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P τ and tQ=E_Q τ. Set V14(α)=inf_{eP,eQ≤α}max(tP,tQ).

## Author exact theorem

For **every real** δ in

$$0\le\delta\le\frac{248469455}{93707153704539389952}$$

the value function is

$$\boxed{V_{14}(\alpha_{164}+\delta)=V_{164}-\frac{80880101855}{149081673}\delta}$$

with

$$\alpha_{164}=\frac{62947091618416625195}{180720939287325966336},\quad V_{164}=\frac{2138584004831606037541}{180720939287325966336}.$$

The new right endpoint is

$$\boxed{\alpha_{165}=\frac{881259282664541428015}{2530093150022563528704},\quad V_{165}=\frac{4277168009143268563157}{361441878574651932672}}.$$

The same affine supporting line lies **strictly below** V14(α) for α>α165.

## Exact Bellman dual lower bound for all full ordered-history policies

For s=(n,a,b), where a,b count symbols 0,1, the prefix likelihood ratio Q/P equals ℓ(s)=2^(a+b)/3^a. Define K=13623672285/49693891, L=40009085000/149081673. For n<14 let

$$H(s)=\min\{K\ell(s),\ L,\ 1+\sum_{i=0}^2P_i H(s+e_i)\};$$

omit continuation when n=14. Exact rational evaluation over **680 states** gives

$$H(0)=\frac{819944053177461253554178891}{4083385870731431154548736}.$$

The **only** ties are R=(10,0,1), Q/continue, and G=(10,7,3), P/continue. There are **1238 strictly positive nonminimal action gaps**, minimum 8257109179793/821825520500736, with no negative gap. Bellman induction for every randomized **ordered-history** policy gives

$$H(0)\le t_P+K e_Q+L e_P\le\max(t_P,t_Q)+(K+L)\alpha.$$

Here K+L=80880101855/149081673. Count compression was used only to evaluate conditional iid suffix laws, not to restrict the admissible full-history policy or to assert a native X6 quotient.

## Ordered first-hit primal witness

Keep every ordered first-hit history and its separate exact positive P and Q mass. Literal unmerged integer-weight DFS finds R: **10** histories, P mass 9765625/120932352, Q mass 9765625/60466176; G: **30** histories, P mass 5/4831838208, Q mass 5/10319560704. They lie at the same depth, with incompatible symbol counts, so their ordered first-hit cones are disjoint.

At R let r be the immediate-Q probability; at G let g be the immediate-P probability. Everywhere else select the unique Bellman-minimal action. The measured four-vector M=(eP,eQ,tP,tQ) obeys

$$M(r,g)=M_{00}+r\,d_R+g\,d_G\quad(0\le r,g\le1).$$

Indeed, **two different author algorithms** agree exactly: backward Fraction count-suffix recursion and literal forward unmerged integer-weight ordered DFS at all four coin corners; P- and Q-terminal total mass equals exactly 1; M11−M10−M01+M00=(0,0,0,0). Full rational four-vectors are in certificate165.json.

The equality eP=eQ holds precisely on

$$\boxed{r(g)=\frac{257914391728953}{844544000000000}+\frac{30168519}{11823616000000000}g}.$$

For every real g∈[0,1] both coins remain admissible, r(g) strictly interior. The g=0 endpoint agrees **exactly** with the published α164,V164. At g=1 the values are α165,V165 above. The time differences tP−tQ at the two endpoints are respectively

$$\frac{25049209729437132035}{60240313095775322112}>0,\quad \frac{350688935928809353165}{843364383340854509568}>0.$$

Exact substitution at both endpoints yields tP+K eQ+L eP=H(0). Because each observer is affine in g, error balance, positive time dominance and exact dual attainment hold for **all real** intermediate g. Therefore the constructed primal policies attain the universal dual lower bound throughout the stated interval.

## Strict right sharpness

The finite full-history randomized policy simplex is compact and the optimum is attained. Suppose equality with the *same* supporting line held at any α>α165. Since K,L>0, both error bounds would be tight (eP=eQ=α), tP would be the maximal time and Bellman equality must hold on each positively visited prefix. Positive action gaps exclude all actions except the unique chosen ones and the two ties R/G. At identical count states, ordered histories have identical iid suffix distributions and common Q/P ratio, so history-specific tie coins collapse to one P-mass-weighted effective coin **for these four declared observers only**. R/G first-hit cones do not intersect, hence every equality policy has the affine M(r,g) representation above. Its error-balance locus has 0≤g≤1 and thus α≤α165, contradiction. The line is strictly suboptimal to the right.

## Actual evidence, next question and admission boundary

Locally **executed** verify165.py: 680 Bellman states, 1238 positive action gaps, four exact corner coincidences and zero mixed coefficient. Ordered DFS visited 409696, 408976, 409456, 408736 nodes for corners 00,01,10,11. Computation certificate and stdout are in the local evidence bundle. The GitHub PORTABLE_VERIFY_STAGE165.py is a **source adaptation** of the already published Stage164 portable verifier; its remote storage is **not** an execution claim or byte-for-byte identity with locally executed verify165.py.

A separate symbolic affine-dual tangent scan plus a fresh independent Fraction Bellman evaluation identifies **Stage166 dual-only** at K=310447538892/1139969309, L=912521643352/3419907927; new tie W=(7,4,1) P/C with R still Q/C, all 1238 other gaps positive. **Stage166 primal interval not proved**. See NEXT_TASK_PACKET_166.md.

GitHub connected user awdawmip is push-authorized; however native control-tasks read returned CONTROL_QUOTA, native session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). **Native active owner, CLAIM, Result and independent Driver admission are UNKNOWN**. Ordinary author-note publication is not native control acceptance. No P000 six-axis native Cell embedding or physics correspondence has been established.