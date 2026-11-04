# PREFIX-486 — Exact three-source BRC fibers, rational generating functions, and horizon compression density

Date: 2026-11-04 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_REACHABILITY_AND_SMALL_EXHAUSTIVE_CHECKED / UNREVIEWED / NOT_ADMITTED. This is an author-side portable mathematical result, not an authenticated Researcher CLAIM/Result.

## Authority, provenance and representation

Continues the exact FRONTIER PREFIX-485 at `awdawmip/enterprise-math@7bbdb1f12465559d967245362fcf94b379be5274`; maintain the prior task scientific pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Current behavioral rules were separately read on 2026-11-04 from global canonical `main@8af13ca22c76796fb2b39b73b091714c778f301c`, and Enterprise Math applicable control at `main@8440d7986faa0068274659d70bb911e9be806ec5`. Protected P000, ACTIVE Heartbeat X6, joint observer preservation, and research method remain assumed; nothing here changes their ontology.

Within the fixed six-native-axis X6, use the restricted ordered-path model of PREFIX-485. There are ten ordinary signed steps `a/A,b/B,c/C,d/D,e/E`, always legal, and a special `x` allowed only as the first step or immediately after KMP gate word `w`, resetting KMP to 0. Fix `w=aab` or `w=aba`. Ordinary positive/negative counts `u_i,v_i` give `y_i=u_i-v_i`, `p_i=min(u_i,v_i)`, `S=sum p_i`, `V=p_b+2p_d+p_e`, `W=p_c+p_e`. Retain `(n,s,y_a,...,y_e,V,W,q)` as the base BRC-KMP fiber, with `s=#x`, `q` terminal KMP state. `S=(n-s-sum|y_i|)/2` is determined. This is an explicitly typed projected observer and does not discard full provenance for other queries.

Source state `t=N,B,C` means no occurrence of b/B/c/C, first such occurrence is b/B, or first is c/C. Source output F=1 precisely in state B. Let `T_w(n;s,q)` count base fibers simultaneously supporting N,B,C. Let `T_w(n)=sum_{s,q}T_w(n;s,q)`. Let `H_0,H_1` count minimum source-observation states at horizons zero and at least one, after summing across all base fibers.

## Theorem 1 — exact binomial classification (ALL n>=0)

For `w=aab`, the only possible triple-fiber suffix states are q=0,1,2; for `w=aba`, they are q=0,1. For both words `s in {0,1}`, and the **exact** count is

```
T_w(n;s,q) = binom(n+1-s-q,5)
```

for each permitted (s,q), with binom(t,5)=0 for t<5, and zero in all other (s,q).

### Proof: necessity

A triple fiber contains an N path, which uses no b/B/c/C. Thus y_b=y_c=0 and p_b=p_c=0 in its N realization; since either gate w includes b, an N path may use x at most once and, if present, only first. Its terminal KMP state is 0,1,2 for aab (q2 means suffix aa), or 0,1 for aba (q2 would require suffix ab, impossible for N).

Fix this N realization with p=(p_a,0,0,p_d,p_e), and consider a C realization with the same base observation. A C history has at least one c or C; since y_c=0, it contains c and C so p'_c=h>=1. Equality of W gives p'_e=p_e-h>=0, hence p_e>=1. Equality of V gives p'_b=h-2t>=0 where t=p'_d-p_d, hence t<=floor(h/2). Equality of S gives p'_a=p_a+t-h<=p_a-1, hence p_a>=1. With the same y_a, the number of positive a steps in C is `u'_a=p'_a+max(y_a,0)<=u_a-1`, where `u_a` is the N count. State q=1 requires at least one terminal positive a; aab q=2 requires at least two. Thus `u_a>=q+1` for permitted q. For q=0 this just follows from p_a>=1. These are necessary constraints.

### Proof: sufficiency

Conversely take any N ordinary signed count vector with `u_a,v_a,u_e,v_e>=1` and `u_a>=q+1`, arbitrary nonnegative u_d,v_d, and no b/c steps, plus s=0 or one initial x. Its KMP terminal q can be realized: place an available E at the end for q0; place E before final a for q1; or E before final aa for aab q2. For q1, using E as preceding symbol prevents an unwanted longer suffix.

Construct **both** B and C histories with identical base observation by the cancellation-count substitution
```
(p_a,0,0,p_d,p_e) -> (p_a-1,1,1,p_d,p_e-1).
```
It preserves S,V,W, all signed displacements, length and s. Put b/B and c/C early, with b first for B or c first for C; the source label then locks in. For q0 end with a non-prefix uppercase B/C; for q1 end in uppercase B/C followed by a, and for aab q2 end in uppercase B/C followed by aa. Since the modified positive a count is `u_a-1>=q`, every required suffix is available. Prefix letters can be reordered arbitrarily, ordinary steps are legal, and the optional x is put first in all three realizations. Hence precisely the stated N configurations yield three-source fibers. There is no `{N,C}`-only fiber: the construction always supplies B.

Finally, on N histories the base observer uniquely reconstructs all five p counts (p_b=p_c=0, p_e=W, p_d=(V-W)/2, p_a=S-p_d-p_e) and all signed counts; different N count vectors give different base fibers. Remove one a/A pair and one e/E pair from N counts. The remaining six nonnegative coordinates
```
(u_a-1,v_a-1,u_d,v_d,u_e-1,v_e-1)
```
sum to `n-s-4`, with the first coordinate at least q. Thus there are exactly `binom(n-s-4-q+5,5)=binom(n+1-s-q,5)` distinct fibers (stars and bars). QED.

## Corollary 2 — exact rational generating functions and difference

For all n, including boundary cases,
```
sum_{n>=0} T_aab(n) z^n = z^4 (1+z)(1+z+z^2)/(1-z)^6,
sum_{n>=0} T_aba(n) z^n = z^4 (1+z)^2/(1-z)^6,
sum_{n>=0} (T_aab(n)-T_aba(n)) z^n = z^6(1+z)/(1-z)^6.
```
In particular `T_aab(8)=286`, `T_aba(8)=259`, with exact structural difference `27=binom(7,5)+binom(6,5)`; at n=9 they are `637` and `560`, difference `77=binom(8,5)+binom(7,5)`. The extra aab fibers all have terminal suffix state q2=aa; aba q2=ab cannot coexist with source N. This settles the previous unexplained 286-versus-259 observation exactly for every length.

## Corollary 3 — exact horizon-zero saving and asymptotics

At H=0, N and C are output-indistinguishable; at H>=1 the ordinary suffix b distinguishes them, and B is distinguished already by the empty suffix. Every fiber with N and C also has B (proof above), so **H1(n)-H0(n)=T_w(n)** for every n, not merely in finite experiments. The savings have exact polynomial growth
```
T_aab(n) = n^5/20 + O(n^4),    T_aba(n) = n^5/30 + O(n^4).
```
Using the inherited, author-proved PREFIX-477 base-history asymptotic `F_w(n)=n^8/3360+O_w(n^7)`, the corresponding savings as a fraction of base fibers obey
```
T_aab(n)/F_aab(n) = 168/n^3 + O(n^-4),
T_aba(n)/F_aba(n) = 112/n^3 + O(n^-4).
```
The last density conclusion inherits PREFIX-477's proof status; the present binomial/generating-function theorem has its independent direct proof above. The source state must still be retained for H>=1, and this theorem does not cover other provenance outputs or physical time/phase evolution.

## Executed exact evidence

The companion standalone JavaScript certificate performs (1) set-valued BRC-KMP-source reachability DP with independent explicit closed-form binomial comparison for both gates at all n=0..9, (2) per-(s,q) triple-fiber counting, (3) H0/H1 equivalence and exclusion of {N,C}-only fibers, and (4) independent exhaustive ordered-path enumeration n=0..4 with complete base-fiber source-mask comparison. The certificate logs all checked layers, checks PREFIX-485 n8 values and prints `ALL_CHECKS_PASS` on success. The finite test is independent confirmation, not the basis of the unbounded proof.

## External methods, open work, and authority

The counting proof uses a direct six-variable stars-and-bars bijection. A general extension to other gate/source automata may use the semilinear image of finite automata (Anthony Widjaja To, 2010, https://arxiv.org/abs/1002.1464) and rational/Presburger counting (Kevin Woods, 2015, https://doi.org/10.1017/jsl.2015.4); those references are not treated as proofs of this special formula.

Remaining PREFIX-487: find exact one-type and two-type generating functions (beyond the triple case), determine a finite automaton-to-Presburger algorithm for generic source automata, and test alternative information-sensitive source outputs under explicit future operations. Native task owner/CLAIM, review, and mathematical admission remain separate from this author-side published proof.
