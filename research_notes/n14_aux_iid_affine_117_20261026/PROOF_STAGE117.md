# Stage117 — exact affine optimum after terminal T saturates

Status: **AUTHOR_EXACT_FINITE_PROOF / DRIVER_UNREVIEWED / NO_NATIVE_CLAIM**. This is an external auxiliary iid sequential-testing experiment, **not** a P000, X6, Heartbeat, or native BRC physical theorem. Researcher-ID `EM-DIRECT-5A72C1` is locally allocated provenance, not a service-issued Owner/CLAIM.

## Frozen model and theorem

On every full ordered history of at most 14 iid ternary draws, use
[
 P=(1/8,1/24,5/6),qquad Q=(1/12,1/12,5/6).
]
Write `eP=P(decide Q)`, `eQ=Q(decide P)`, `tP=E_P(tau)`, `tQ=E_Q(tau)`. Define
[
 V_{14}(alpha)=inf_{	ext{all ordered-history randomized stopping/decisions}:eP,eQleqalpha}max(tP,tQ).
]
Use the Stage116 author-level endpoint
[
 alpha_{116}=rac{900390062503198401793}{2592933255351443128320},quad
 V_{116}=rac{132635679890866772493569}{10371733021405772513280}.
]
Set
[
 K=rac{7703713039590}{8727240137},quad
 L=rac{7249159245096}{8727240137},quad
 S=K+L=rac{2136124612098}{1246748591},quad
 eta=rac{8727240137}{228653726221467648}.
]
**Theorem.** For EVERY REAL (0leqdeltaleqeta),
[
 oxed{V_{14}(alpha_{116}+delta)=V_{116}-Sdelta.}
]
In particular
[
 oxed{alpha_{117}=rac{900390161470101555373}{2592933255351443128320}},quad
 oxed{V_{117}=rac{132635001628579939136609}{10371733021405772513280}}.
]
The same Bellman support line is **strictly unattainable** at every (alpha>alpha_{117}).

## Dual certificate over all ordered histories

At count state (s=(n,a,b)), with (nleq14), the likelihood ratio is (R(s)=Q(s)/P(s)=2^{a+b}/3^a). In conditional P units define
[
 H(s)=minleft{K R(s), L, 1+	frac18H(n+1,a+1,b)+	frac1{24}H(n+1,a,b+1)+	frac56H(n+1,a,b)ight}
]
with the continuation term omitted at (n=14). All operations are rational. The exact recurrence exhausts (sum_{n=0}^{14}inom{n+2}{2}=680) states. Of all nonminimizing actions, exactly 1238 have strictly positive gaps, zero have negative gaps, and the minimum strict gap is
[
 rac{273655643173420723}{6671206249789390848}>0.
]
There are exactly TWO ties:
[
 X=(7,5,1): 	ext{decide P / continue},qquad
 D=(9,1,2): 	ext{decide Q / continue}.
]
The previously tied terminal state (T=(14,7,4)) now uniquely decides P. Direct computation gives
[
 H(0,0,0)=rac{145276732397197889380399249433}{239041381470853493302493184}
 =V_{116}+Salpha_{116}.
]
Induction on the *uncompressed, ordered prefix tree* gives, for any history-dependent randomized policy,
[
 H(0,0,0)leq t_P+L e_P+K e_Q.
]
The count recursion is valid because the conditional iid suffix and four declared observers agree on count fibers, NOT because different ordered histories are identical native states. Since (K,L>0) and (t_Pleqmax(t_P,t_Q)), the universal lower bound is (V_{14}(alpha)geq H(0,0,0)-Salpha).

### First dual wall after Stage116

At Stage116 take (K_0=37550061/41440, L_0=3296576/3885). Use the nonmixing selector Q at D and P at T and all otherwise unique minimizers. Keeping D exactly tied determines
[
 K(x)=K_0-x,quad L(x)=L_0-rac{164096}{214569}x.
]
Every nonselected action gap is affine on this fixed-policy ray. The old terminal tie T moves strictly to P (the Q-minus-P gap increases), and D remains tied. Exhaustively comparing all formerly positive gaps gives the UNIQUE smallest positive zero
[
 x_*=rac{172786349905893}{7380751658720}
]
at (X=(7,5,1)), alternative action **P**. Independently recomputing the exact 680-state Bellman recurrence at ((K(x_*),L(x_*))) yields precisely the two ties and 1238 positive gaps above. The ray sweep only locates a candidate; this independent endpoint Bellman minimization is the global dual certificate.

## Positive-rational labeled path carriers

Keep the actual first-hit ordered histories. Choosing continuation at the two tie states to obtain first-hit masses:
[
 egin{array}{c|c|c|c}
 	ext{state}&	ext{number of ordered prefixes}&P	ext{-mass}&Q	ext{-mass}\
 X&(28)&35/1179648&35/4478976\
 D&(172)&671875/53747712&671875/20155392
 end{array}
]
The two cones are disjoint: X has 5 zeros already at depth 7, while D has only 1 zero at depth 9, so X cannot precede D; D cannot precede X by depth. A branch is represented by its ordered prefix and two positive rational masses; this is a typed finite BRC-style carrier with the four moment observers. It contains no signed amplitudes or phase cancellation. Source interface reused: `definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json`, explicit positive rational branch population (REUSE_APPLIED); this finite use is not a general identification with native dynamics.

At D decide Q with probability (w) and otherwise continue; at X decide P with probability (y) and otherwise continue. The other states use their unique Bellman minimizers; in particular T always decides P. As the two cones do not meet, the root moment vector (M=(e_P,e_Q,t_P,t_Q)) is exactly affine (M(w,y)=M(0,0)+w,d_w M+y,d_y M), without a (wy) term. Exact derivatives (two independent computation schemes) are
[
 d_wM=left(rac{593265625}{5283615080448},-rac{430671875}{5015306502144},-rac{34607609375}{1981355655168},-rac{17355203125}{417942208512}ight),
]
[
 d_yM=left(-rac{816010405}{5410421842378752},rac{3257975}{17832200896512},-rac{8114835365}{225434243432448},-rac{151243295}{13374150672384}ight).
]
The Stage116 endpoint is (y=0) and (w_0=374319733261181/1042086080000000). Solving (e_P=e_Q) gives the legal **continuous** family
[
 oxed{w(y)=w_0+rac{12528414549}{7443472000000},y,quad 0leq yleq1.}
]
Here (0<w_0<w(1)=376073711298041/1042086080000000<1). Direct exact evaluation at both endpoints proves
[
 e_P=e_Q=alpha_{116}+eta y,quad
 t_P=V_{116}-Seta y,quad
 t_P>t_Q.
]
The last strict inequality holds at both endpoints and thus on the full interval by affinity. All policies use only Bellman minimizers and attain the dual lower bound, proving the theorem for **every real** point, not merely a numerical grid.

## Sharp right endpoint

This is a finite-horizon compact randomized policy space, so each optimum is attained. Equality in the Bellman support lower bound for (alpha>alpha_{117}) would force (e_P=e_Q=alpha), (t_P=V_{14}(alpha)), and only minimizing actions on every positive-mass prefix. The only possible mixtures are at X and D. Since on every first-hit fiber the likelihood ratio and conditional suffix response for these four observers depend only on counts, arbitrary history-specific mixtures average to some (w,yin[0,1]). Cone disjointness makes the four moments affine in these averages. Error equality forces the displayed (w(y)), hence (alpha=alpha_{116}+eta yleqalpha_{117}); contradiction. Therefore the support is **strictly** below the optimum to the right.

## Actual validation and limits

Author-side local `em_stage117_compute.py` executed the rational fixed-action ray, all 680 Bellman minima and gaps, first-hit rational masses, complete moment family and the sharpness algebra. A separately implemented ordered-prefix INTEGER-numerator DFS (`em_stage117_independent.py`) recomputed every corner ((w,y)in{0,1}^2), visiting 862459, 852463, 854719 and 844723 prefixes, and matched both derivative vectors, first-hit masses and all endpoint assertions. Both returned PASS; no floating arithmetic used. A transport/persistence receipt is not a scientific independent review.

Original frozen inputs: GLOBAL_KNOWLEDGE_V1 main `1fe18ba120c1f8f901246acb659589849b7e9147`; Enterprise Math main `c7fa172ab920563207bd5d782a78ec1cd79515df`. Native `em_control_tasks` returned CONTROL_QUOTA; session creation returned STATIC_READONLY_SCOPE_DENIED and `operation_sent=false`. Hence Owner/CLAIM/Result and independent Driver authority remain unverified. This result neither changes P000 nor establishes infinite-horizon, native X6, or physical correspondence.

## Next: Stage118

Starting from (y=1) (X now uniquely P) while D still mixes, the next fixed-policy dual wall candidate is (K_{118}=254421/296, L_{118}=90232/111) at ((13,6,4)), where Q-stop and continue tie. Recompute its first-hit labeled histories, interacting cones, active error constraints, and sharp endpoint. Candidate only, not a Stage118 interval theorem.
