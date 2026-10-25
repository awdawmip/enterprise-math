# Stage143 — dual candidate only; next primal problem

External finite iid N=14: P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Error controls eP=P(decide Q), eQ=Q(decide P), objective V14(alpha)=min max(tP,tQ), arbitrary randomized literal ordered histories. This is not a native P000/X6 model.

Stage142 author-proved full-real interval ends at
~~~
alpha142=12238552734313788965/35205614928358539264
V142=24070360310471940161/1955867496019918848
K142=395290882339224/875825669873
L142=54591710813272/125117952839
B=(11,0,1): Q/continue tied, interior Q-stop w=50180601034414837/81438720000000000
J=(4,3,0): P/continue tied, P-stop saturated at 1
~~~
Independent Research Driver review pending; no native CLAIM/Result.

Continue along the B tie-preserving dual ray dK=-43/1536, dL=-7/288. The J tie breaks strictly in favor of P. Exact scan of all **834** positive directional action-gap closures gives first at

~~~
lambda143=36775812459682145214747988992/39950391891606071321645969
K143=19411949464309662/45614547809953
L143=18882041753802888/45614547809953
Hroot143=42222189293875024646776690163383/138821594513174762290616991744
new tie C=(3,3,0): continue/P; old tie B=(11,0,1): Q/continue
~~~

A full exact 680-state Bellman recomputation at this candidate finds precisely these 2 ties, 1,238 positive other action gaps and zero negative gaps; minimum strict gap 1685757022745149/59116453961699088. **Dual candidate, no Stage143 primal theorem yet.**

Next independent unit: first-hit literal word inventories and exact P/Q masses for B,C; four exact M=(eP,eQ,tP,tQ) corners by Fraction Bellman plus separately structured positive integer-weight ordered-prefix DFS; solve eP=eQ and test coin feasibility, tP>=tQ, alpha growth, left match with Stage142 and right sharpness. The prior J state remains fixed P-stop, though C=(3,3,0) may now be its ancestor (do not mistakenly treat C and J as disjoint). B,C cannot share a path since C contains 3 symbol-0 outcomes and B contains zero.

Inputs pinned GLOBAL_KNOWLEDGE_V1 main@596508231dcc5d8cf66c6b991a311dd5d89c2ba0 and Enterprise Math main@c5902704247dcbecf47b24981935c623db607653. Native tasks control returned CONTROL_QUOTA and service session_start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. No live owner or native Researcher identity/CLAIM/Result verified. Ordinary author notes are mathematical evidence, not research-state-machine admission.
