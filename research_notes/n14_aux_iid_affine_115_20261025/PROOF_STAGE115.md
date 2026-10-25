# Stage115: sharp exact real-affine optimum after Stage114 saturation

**Status:** AUTHOR_EXACT_FINITE_PROOF; two author implementations passed; not a native Result, Driver review, Working Truth, or P000/X6/Heartbeat theorem. External finite iid model only. Frozen source reads: GLOBAL_KNOWLEDGE_V1 `main@900a0332bcdcec62b3ba32fa4f3c26ecba3e3e0d`, Enterprise Math `main@bb10c4dbe1badc4adad436d075f2fd93f732e89c` (before this publication). Native control returns CONTROL_QUOTA; session_start returns STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Owner and formal CLAIM are not verified.

## Theorem

Let at most 14 ternary observations have iid distributions
[
P=(1/8,1/24,5/6),quad Q=(1/12,1/12,5/6).
]
All randomized full-ordered-history stopping/decision policies are allowed. Write (e_P=P(	ext{decide }Q)), (e_Q=Q(	ext{decide }P)), (t_P=E_P	au), (t_Q=E_Q	au), and (V_{14}(alpha)=min_{e_P,e_Qlealpha}max(t_P,t_Q)). Stage114's verified author endpoint is
[
alpha_{114}=rac{900372060659842701793}{2592933255351443128320},
quad V_{114}=rac{132764620121352969281069}{10371733021405772513280}.
]
Define
[
K=rac{2533113}{2734},quad L=rac{1181272}{1367},quad
S=K+L=rac{4895657}{2734},quad
eta=rac{2712640625}{390765645398016}.
]
**For every real (0ledeltaleeta):**
[
oxed{V_{14}(alpha_{114}+delta)=V_{114}-Sdelta}.
]
The endpoint is exactly
[
oxed{alpha_{115}=rac{900390060440962701793}{2592933255351443128320}},
qquad
oxed{V_{115}=rac{132635694365041929281069}{10371733021405772513280}}.
]
This **same** supporting affine line cannot be attained for any (alpha>alpha_{115}); no claim about the next face is implicit.

## Complete dual Bellman bound

At count state (s=(n,a,b)), (R(s)=Q(s)/P(s)=2^{a+b}/3^a). For (n<14), in conditional P-units,
[
H(s)=min{K R(s),L,1+	frac18 H(n+1,a+1,b)+	frac1{24}H(n+1,a,b+1)+	frac56 H(n+1,a,b)};
]
omit continuation at (n=14). Exact rational evaluation of all (sum_{n=0}^{14}inom{n+2}{2}=680) states yields exactly 1,238 **strict positive** non-minimizer action gaps, minimum (11023/7086528), no negative gap, and exactly two tied states:

* (D=(9,1,2)): Qstop versus continue;
* (E=(12,4,1)): Pstop versus continue.

All other states have a unique minimizing action. The exact root dual is
[
H(0,0,0)=23760619012724853347605/37442486208817004544
=V_{114}+Salpha_{114}.
]
The same Bellman induction operates over the **entire ordered-prefix tree**: an arbitrary history-dependent competitor may choose different actions at histories with the same counts, but the iid conditional laws and likelihood ratio depend only on the counts. Thus, without restricting the policy class,
[
H(0,0,0)le t_P+L e_P+K e_Qlemax(t_P,t_Q)+Salpha.
]
Both multipliers are positive.

## Exact positive-rational ordered-history carrier and primal construction

At (D), stop and declare Q with probability (w), otherwise continue; at (E), stop and declare P with probability (v), otherwise continue. Everywhere else use the unique minimizing action. Stage114's old A=(10,3,0) now chooses Pstop strictly.

The two true ordered cones are disjoint: D's symbol-1 count is 2, E's is 1, so D cannot precede E; E occurs later and cannot precede D. Preserve each literal ordered history with its positive integer/rational mass through the finite horizon. The exact **first-hit** carriers are:

| state | literal histories | P mass | Q mass |
|---|---:|---:|---:|
| D | 172 | 671875/53747712 | 671875/20155392 |
| E | 3048 | 9921875/1146617856 | 9921875/2902376448 |

Conditional continuation at D gives ((e_P,e_Q,t_P,t_Q)=(97421/98304,641/248832,51509/36864,25831/20736)); at E it gives ((1/576,143/144,25/24,13/12)). The root moment (M=(e_P,e_Q,t_P,t_Q)) is **exactly affine** in (w,v), with mixed (wv) coefficient zero. The exact derivative vectors are

[
partial_w M=left(
593265625/5283615080448,;
-430671875/5015306502144,;
-34607609375/1981355655168,;
-17355203125/417942208512ight),
]

[
partial_v M=left(
-9921875/660451885056,;
9921875/417942208512,;
-248046875/27518828544,;
-128984375/34828517376ight).
]

The Stage114 endpoint is attained at ((w,v)=(170386233161181/1042086080000000,0)). Solving the **actual two** error equations (e_P=e_Q) gives
[
w(v)=rac{170386233161181}{1042086080000000}
+rac{637032}{3256519}v,quad 0le vle1.
]
Both probabilities are feasible for all real (vin[0,1]), ending at
[
(w_{115},v_{115})=(374236473161181/1042086080000000,1).
]
Hence E saturates first while D remains mixed. The two errors are both (alpha_{114}+eta v), and (t_P=V_{114}-Seta v). The difference (t_P-t_Q) is affine and **strictly positive at both ends**:
[
444777657503394885715/691448868093718167552>0,qquad
444360026883234885715/691448868093718167552>0.
]
The constructed policies therefore meet the dual lower bound for **every real** parameter value, proving the theorem.

## Sharpness against any full-history randomized policy

The finite randomized policy set is compact. Equality in the dual line beyond (alpha_{115}) would force (i) both positive-multiplier errors to equal (alpha), and (ii) every positive-mass action to be a Bellman minimizer. All actions are forced except randomization at D and E. The per-state constant likelihood ratio and identical iid suffix law justify **only for the four declared observers** replacing arbitrary history-specific tie probabilities by their first-hit-P-mass weighted averages (w,v); both P and Q masses are preserved because Q/P is constant on a fixed count state. Disjointness of their cones rules out mixed products. The equality (e_P=e_Q) forces the displayed (w(v)) and (alpha=alpha_{114}+eta v). Since (vle1), equality requires (alphalealpha_{115}), contradiction. The endpoint is sharp.

## Reproducibility, observer scope, next

The author ran exact-Python-`Fraction` Bellman/root-moment/positive-first-hit checks (680 states, 1,238 strict gaps, two ties, exact endpoint) and a **separately written literal ordered-prefix integer DFS** using denominators (24^{14}) and (12^{14}), all four deterministic parameter corners, both first-hit counts, both mass pairs, all derivative entries and zero mixed term. Both PASS. The attached companion source files are portable reproduction code; they have not been executed on GitHub itself. Ordered histories are compressed only after exact sufficiency for (e_P,e_Q,t_P,t_Q) and iid extensions up to N=14; BRC reuse = REUSE_APPLIED to positive rational, label-preserving carriers. This proves no native X6 transfer, phase cancellation, physical result or infinite-horizon theorem.

**Stage116:** E's Pstop probability is 1, D's Qstop probability is still interior. Sweep the adjacent dual face keeping D tied and E strict Pstop; identify the next closing Bellman gap, rebuild feasible equal-error randomization with a new tie, or prove a precise obstruction. Formal native authority and independent Driver review remain pending.
