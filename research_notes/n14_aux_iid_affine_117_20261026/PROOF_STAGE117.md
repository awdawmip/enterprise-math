# Stage117: exact optimal affine segment for the N=14 auxiliary iid test

Status: AUTHOR_EXACT_FINITE_PROOF. This is NOT a P000, X6, Heartbeat, or native physical theorem. Independent Driver review and native Owner/CLAIM/Result remain unverified. Local Researcher-ID: EM-DIRECT-5A72C1 (not service-issued).

## Statement and finite model

For all randomized stopping/deciding rules on full ordered histories of at most 14 iid ternary draws, use

\[
P=(1/8,1/24,5/6),\qquad Q=(1/12,1/12,5/6).
\]

Define error probabilities \(e_P=P(\mathrm{decide}\ Q)\), \(e_Q=Q(\mathrm{decide}\ P)\), and expected sample sizes \(t_P=E_P(\tau)\), \(t_Q=E_Q(\tau)\). Let

\[
V_{14}(\alpha)=\inf_{\text{all admissible ordered-history randomized policies};\,e_P,e_Q\leq\alpha}\max\{t_P,t_Q\}.
\]

The prior author-level Stage116 endpoint is

\[
\alpha_{116}=\frac{900390062503198401793}{2592933255351443128320},\qquad
V_{116}=\frac{132635679890866772493569}{10371733021405772513280}.
\]

Define the exact rational dual parameters and interval size by

\[
K=\frac{7703713039590}{8727240137},\quad
L=\frac{7249159245096}{8727240137},\quad
S=K+L=\frac{2136124612098}{1246748591},\quad
\eta=\frac{8727240137}{228653726221467648}.
\]

**Theorem.** For **every real** \(0\leq\delta\leq\eta\),

\[
\boxed{V_{14}(\alpha_{116}+\delta)=V_{116}-S\delta.}
\]

The exact right endpoint and value are

\[
\boxed{\alpha_{117}=\frac{900390161470101555373}{2592933255351443128320}},\qquad
\boxed{V_{117}=\frac{132635001628579939136609}{10371733021405772513280}}.
\]

For every \(\alpha>\alpha_{117}\) the same affine Bellman support is **strictly** below the optimum.

## 1. Finite Bellman global lower bound

At count state \(s=(n,a,b)\), where \(a\) is the number of symbol-0 observations and \(b\) the number of symbol-1 observations, the likelihood ratio is

\[
R(s)=\frac{Q(s)}{P(s)}=\frac{2^{a+b}}{3^a}.
\]

In conditional P units define

\[
H(s)=\min\Big\{K R(s),\,L,\,
1+\tfrac18H(n+1,a+1,b)+\tfrac1{24}H(n+1,a,b+1)+\tfrac56H(n+1,a,b)\Big\};
\]

at depth 14 omit continuation. Direct exact Fraction backward recursion covers

\[
\sum_{n=0}^{14}\binom{n+2}{2}=680
\]

different count states. Among all nonselected actions, exactly 1238 action gaps are strictly positive and none negative. The smallest positive action gap is

\[
\frac{273655643173420723}{6671206249789390848}.
\]

Exactly TWO states have ties:

\[
X=(7,5,1):\quad \mathrm{decide\ P}\sim\mathrm{continue},
\qquad
D=(9,1,2):\quad \mathrm{decide\ Q}\sim\mathrm{continue}.
\]

In particular terminal \(T=(14,7,4)\) now uniquely decides P. The root value is

\[
H(0,0,0)=\frac{145276732397197889380399249433}{239041381470853493302493184}
=V_{116}+(K+L)\alpha_{116}.
\]

For an arbitrary full ordered-history randomized policy, at every prefix the conditional iid suffix distribution and the declared four future observers factor through counts. Bellman induction on the *actual ordered prefix tree* (not an identification of histories as native states) proves

\[
H(0,0,0)\leq t_P+L e_P+K e_Q.
\]

Since \(K,L>0\), \(e_P,e_Q\leq\alpha\) and \(t_P\leq\max(t_P,t_Q)\), this implies the globally valid dual inequality

\[
V_{14}(\alpha)\geq H(0,0,0)-(K+L)\alpha.
\]

## 2. First dual wall after Stage116

Use the Stage116 dual point \(K_0=37550061/41440\), \(L_0=3296576/3885\). At that point the ties are \(D=(9,1,2)\) Q-stop versus continuation, and \(T=(14,7,4)\) P-stop versus Q-stop. Choose at D the Q-stop representative, at T the P-stop representative, and elsewhere the unique minimizer. Each chosen policy's continuation value is affine in \(K,L\).

Keeping D tied and moving toward smaller \(K+L\) produces the exact ray

\[
K(x)=K_0-x,\qquad L(x)=L_0-\frac{164096}{214569}x.
\]

Every nonselected action gap is an explicit affine rational form along this ray. D remains tied and the old alternative Q-stop at T has strictly *increasing* gap. The UNIQUE first positive zero among previously positive gaps is

\[
x_*=\frac{172786349905893}{7380751658720},
\]

attained at \(X=(7,5,1)\) for alternative P-stop. Evaluating \(K(x_*),L(x_*)\) gives the displayed K,L. Recomputing the entire 680-state Bellman recurrence there (rather than relying only on the candidate ray sweep) establishes all the minimizer and gap claims of section 1.

## 3. Labeled positive-rational histories and primal attainment

Using first-hit *ordered* histories (not merely sorted count paths), the two tied states have the following exact arrivals under the unique-policy skeleton with each tied state continued when counting first arrivals:

\[
\begin{array}{c|r|c|c}
\text{State}&\text{Ordered prefixes}&P\text{-mass}&Q\text{-mass}\\ \hline
X=(7,5,1)&28&35/1179648&35/4478976\\
D=(9,1,2)&172&671875/53747712&671875/20155392
\end{array}
\]

Their history cones are disjoint: after reaching X at depth 7 with five zeros, a path cannot reach D at depth 9 with only one zero; D cannot precede X by depth. This is the explicit positive-rational labeled-history BRC-style carrier retaining branch identity and the four error/time observers. It is NOT signed phase/amplitude cancellation or a transfer to native X6.

Let \(w\) denote probability of immediately deciding Q at D, and \(y\) probability of immediately deciding P at X. Elsewhere use the unique minimizing action. For \(M=(e_P,e_Q,t_P,t_Q)\), cone disjointness yields EXACT affinity

\[
M(w,y)=M(0,0)+w\,d_wM+y\,d_yM,
\]

with no cross term. Direct rational recursion and an independently written literal ordered-history integer DFS give

\[
d_wM=
\left(
\frac{593265625}{5283615080448},
-\frac{430671875}{5015306502144},
-\frac{34607609375}{1981355655168},
-\frac{17355203125}{417942208512}
\right),
\]

\[
d_yM=
\left(
-\frac{816010405}{5410421842378752},
\frac{3257975}{17832200896512},
-\frac{8114835365}{225434243432448},
-\frac{151243295}{13374150672384}
\right).
\]

Stage116's endpoint uses \(y=0\) and

\[
w_0=\frac{374319733261181}{1042086080000000}.
\]

Solving \(e_P=e_Q\) as an exact rational linear equation gives

\[
\boxed{w(y)=w_0+\frac{12528414549}{7443472000000}\,y,\qquad 0\leq y\leq1.}
\]

The whole interval is feasible:

\[
0<w_0<w(1)=\frac{376073711298041}{1042086080000000}<1.
\]

Exact arithmetic at the two endpoints, together with affinity, proves for ALL real \(y\in[0,1]\),

\[
e_P=e_Q=\alpha_{116}+\eta y,\qquad
t_P=V_{116}-(K+L)\eta y,\qquad
t_P>t_Q.
\]

The last strict inequality holds at both endpoints, hence everywhere between. These policies use only Bellman minimizers, satisfy both error constraints and attain the global dual inequality. This establishes the theorem for the full continuous real interval, not a grid.

## 4. Sharpness at the right endpoint

The set of finite-horizon randomized stopping/decision policies on the finite ternary history tree is compact, so the optimum is attained. Suppose \(\alpha>\alpha_{117}\) attained the same support line. Because \(K,L>0\), equality would force \(e_P=e_Q=\alpha\), \(t_P=\max(t_P,t_Q)=V_{14}(\alpha)\), and all positive-mass action choices to be Bellman minimizers.

The only tie states are X and D. On their first-hit fibers, the likelihood ratio and the conditional iid suffix response for these four observers are constant within each count state; any history-specific mixing may therefore be P-mass-averaged into effective parameters \(w,y\in[0,1]\) while preserving all four moments. Disjoint cones ensure there is no interaction term. Error equality forces precisely the family \(w(y)\) above; therefore

\[
\alpha=\alpha_{116}+\eta y\leq\alpha_{117},
\]

contradiction. Thus the support line is strictly below the true optimum for every larger alpha.

## 5. Executed evidence, provenance and scientific limits

The actually executed author-side primary program em_stage117_compute.py used standard-library exact fractions for the ray sweep, the full 680-state Bellman recurrence, first-hit rational mass, two mixture derivatives and the Stage118 candidate. An *independently implemented* direct ordered-history DFS accumulated integer mass numerators before rational reconstruction; all four deterministic corners passed with respective prefix visits 862459, 852463, 854719, 844723. Both local programs ran, and the raw outputs and their SHA-256 hashes are specified in EXECUTION_EVIDENCE_STAGE117.md. Portable GitHub Python source is separately preserved and was NOT executed remotely merely because it was uploaded. No independent Research Driver review has occurred.

Frozen account input: GLOBAL_KNOWLEDGE_V1 main 1fe18ba120c1f8f901246acb659589849b7e9147. Frozen Enterprise Math input: main c7fa172ab920563207bd5d782a78ec1cd79515df. BRC interface reused: definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json, exact positive-rational branch observer only (REUSE_APPLIED). Native task list returned CONTROL_QUOTA, native own-session creation returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. The registered local research activity is provenance only, not native Owner/CLAIM/Result authority.

## 6. Next exact candidate, not yet a theorem

After saturation \(y=1\), X uniquely decides P and D still mixes. Moving further on the D-tie ray yields the next candidate wall

\[
K_{118}=\frac{254421}{296},\quad L_{118}=\frac{90232}{111},
\]

at \(G=(13,6,4)\), Q-stop versus continuation. Its full optimal affine segment is OPEN; see NEXT_TASK_PACKET_118.md.
