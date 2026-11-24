# EC49FZF — Conditional deficit dual: three new exact inventories
2026-11-25. Frozen BRC16943 auxiliary Boolean observer, same literal support family and labeled columns as FZE (01d2f0ab95c179c6997d4c93e3055c9e932f83bf:research_notes/portable_direct/EC49FZE_SMALL_HOLE_TERMINAL_CAPACITY.md) and FZC (725a6c9d6695346a9a6dd762efa6587af10fd7dc:research_notes/portable_direct/EC49FZC_FINITE_EXCEPTION_INVENTORY_ENVELOPE.md). State (U,H), U in F, H subset of m labeled columns, |H|<=h<m; query W(r,j)=1[r in U]1[j not in H]. This is the existing auxiliary observer, not native X6 residual attribution. Parent-dependent; author-proved, not independently reviewed.

## New results
M_28=55, M_52=101, M_76=147. Corresponding Q values 94, 173, 252 (c=39,72,105). The 82 FZB exceptional h now contain 35 exact values, 41 intervals of width one and 6 of width two. This round adds three exact values without a new full decision tree: upper bounds are witnessed by FZC/FZE transport. Lower bounds are new. At the candidate lower endpoints for h=10,11,14,16,17,19,24,25,27,29,30,32, the only possible deficient support is 673, as verified by the finite certificate pool; no adaptive feasibility asserted. At h=9,12,20,22, the candidates are 101,394,673. 

## Conditional deficit dual theorem
Keep the parent zero-prefix lemma: for a winning strategy of depth m+c_h, after d=h+c_h-1 distinct zero probes (padding a terminal transcript if needed, in the permitted d<=10m range), every support U has b_U>=h except at most one with b_U=h-1. Here b_U counts DISTINCT physical columns whose observation mask intersects U. If no support is deficient, the following lower bound holds for every choice f in nonempty F. Otherwise choose the same actual deficient f throughout all inequalities.
For each certificate (A,q,w) with A>0, q>=0 and nonnegative integral w, suppose sum_{U intersect S}w_U<=A+q|S| for every nonempty mask S. With W=sum w_U, sum_U w_U b_U>=hW-w_f; summing physical-column contributions gives <=Am+qd. Hence every winning strategy has a single f such that for every certificate in a finite pool D,
m>=ceil((hW-w_f-qd)/A).
Thus M_h >= min_{f in F} max_{D} ceil((hW-w_f-qd)/A).
This retains the shared deficit identity across certificates. The old FZC bound uses max_D min_f, equivalently each certificate subtracts its own max weight; the new bound dominates it by the elementary minimax inequality, and is strictly stronger here. No support, label or future observer is deleted: each f is separately checked as a necessary feasibility condition. The no-deficit case satisfies all conditional inequalities and therefore cannot evade a complete exclusion. The method applies to any finite nonempty support family under the parent prefix lemma, not to arbitrary unrelated observers without that lemma.
For a proposed m, define D_h(m)={f: all certificates satisfy hW-w_f-qd<=Am}. If this set is empty, m is impossible. If it is nonempty, this says only which deficient supports are allowed, not that any is achievable. In a no-deficit history every f must pass; thus any proper subset also rules out no-deficit.
For h=28,52,76, candidate m=54,100,146 respectively is excluded for all 50 f; the FZC/FZE constructive uppers are 55,101,147. Monotonic extension in m (recover original columns and query a known positive row for every added column) rules out smaller m as well, or directly use the parent lower envelope. 

## Evidence
Local Python/SciPy HiGHS LP discovery maximized hW-w_f-qd with A=1 at 17 candidate pairs (h,m): (9,17),(10,16),(11,19),(12,24),(14,25),(16,28),(17,32),(19,34),(20,39),(22,41),(24,43),(25,47),(27,49),(28,54),(29,52),(30,56),(32,58). Rational reconstruction, then exact integer inequalities were checked. Discovery objective for a fixed f uses coefficients -h for each w except 1-h for w_f, d for q, nonnegative variables; constraints for every s are C(s)w-popcount(s)q<=1. Four additional distinct certificates E (alongside the prior D) suffice. Independently executed exact JavaScript replay of all 10*1023 mask inequalities, all 22*50 block support inequalities and 180 recurrence steps h=4..183; ordinary integers are within exact JS range. No optimizer infeasibility is used. Actual replay result:
{"oldWidths":{"0":32,"1":44,"2":6},"widths":{"0":35,"1":41,"2":6},"changes":[[28,54,55,55],[52,100,101,101],[76,146,147,147]]}
All exception rows [h,lo,up]: [[4,9,9],[5,9,9],[6,11,11],[7,11,11],[8,13,13],[9,17,18],[10,16,17],[11,19,20],[12,24,25],[13,22,22],[14,25,27],[16,28,29],[17,32,33],[18,31,31],[19,34,35],[20,39,40],[21,37,37],[22,41,42],[24,43,44],[25,47,49],[27,49,51],[28,55,55],[29,52,53],[30,56,57],[32,58,59],[33,63,64],[35,65,66],[36,70,70],[38,71,73],[39,77,77],[40,73,75],[41,78,79],[43,80,81],[44,85,85],[46,87,88],[47,92,92],[49,93,94],[51,95,97],[52,101,101],[54,102,103],[55,107,108],[57,109,109],[58,115,115],[60,116,116],[62,117,118],[63,123,123],[65,124,125],[66,130,130],[68,131,132],[71,138,139],[73,139,140],[74,145,146],[76,147,147],[77,153,153],[79,153,154],[82,161,161],[84,162,163],[85,168,168],[87,169,170],[90,176,177],[93,183,184],[95,184,185],[96,191,191],[98,191,192],[101,199,199],[104,206,206],[106,207,208],[109,214,215],[112,221,222],[115,229,229],[117,229,230],[120,237,237],[123,244,244],[128,252,253],[131,259,260],[134,267,267],[139,275,275],[142,282,282],[150,297,298],[153,305,305],[161,320,320],[172,343,343]]
Remaining rows [h,lo,up,possible f at lo]: [[9,17,18,[101,394,673]],[10,16,17,[673]],[11,19,20,[673]],[12,24,25,[101,394,673]],[14,25,27,[673]],[16,28,29,[673]],[17,32,33,[673]],[19,34,35,[673]],[20,39,40,[101,394,673]],[22,41,42,[101,394,673]],[24,43,44,[673]],[25,47,49,[673]],[27,49,51,[673]],[29,52,53,[673]],[30,56,57,[673]],[32,58,59,[673]],[33,63,64,[101,394,673]],[35,65,66,[101,394,673]],[38,71,73,[673]],[40,73,75,[673]],[41,78,79,[673]],[43,80,81,[673]],[46,87,88,[101,394,673]],[49,93,94,[673]],[51,95,97,[673]],[54,102,103,[673]],[55,107,108,[394]],[62,117,118,[673]],[65,124,125,[673]],[68,131,132,[101,394,673]],[71,138,139,[394]],[73,139,140,[673]],[74,145,146,[394]],[79,153,154,[394]],[84,162,163,[101,394,673]],[87,169,170,[101,394,673]],[90,176,177,[394]],[93,183,184,[394]],[95,184,185,[394]],[98,191,192,[394]],[106,207,208,[101,394,673]],[109,214,215,[394]],[112,221,222,[394]],[117,229,230,[394]],[128,252,253,[394]],[131,259,260,[394]],[150,297,298,[394]]]
Additional exploratory terminal-capacity LPs at these same 17 pairs did not exceed capacity; no exclusions attributed to those LPs. Next: use the single-support conditional reductions, especially h=10,11,14, to derive integer mask constraints and check positive branches; seek upper constructions where lower endpoints remain feasible.

## Standalone reproduction (Python 3, literal inputs, exact arithmetic; equivalent to executed JS replay)
```python
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
D=[[3,30,[[86,6],[91,1],[101,13],[243,1],[281,3],[299,1],[346,1],[394,14],[412,2],[460,2],[602,9],[673,14],[788,10]]],[27,64,[[23,6],[86,14],[101,19],[157,2],[243,9],[281,3],[299,12],[394,21],[412,6],[460,15],[602,22],[646,7],[673,22],[697,6],[788,22],[833,12]]],[1,3,[[86,1],[101,1],[299,1],[394,1],[460,1],[602,1],[673,2],[788,1]]],[5,36,[[23,1],[86,6],[101,16],[243,2],[281,3],[299,2],[346,2],[394,16],[412,3],[460,3],[602,12],[673,17],[788,12]]],[3,22,[[86,5],[101,9],[243,1],[281,2],[299,2],[346,1],[394,9],[412,2],[460,2],[602,7],[673,11],[788,7]]],[3,38,[[86,7],[91,2],[101,17],[243,1],[281,4],[346,1],[394,19],[412,2],[460,2],[602,11],[673,17],[788,13]]]]
E=[[1,19,[[86,4],[91,1],[101,8],[281,2],[346,1],[394,9],[412,1],[460,1],[602,5],[673,9],[788,6]]],[5,36,[[23,1],[86,6],[101,16],[211,2],[281,3],[299,2],[346,2],[394,16],[412,3],[460,3],[602,12],[673,17],[788,12]]],[3,38,[[86,7],[91,2],[101,17],[211,1],[281,4],[346,1],[394,19],[412,2],[460,2],[602,11],[673,17],[788,13]]],[3,22,[[86,5],[101,9],[211,1],[281,2],[299,2],[346,1],[394,9],[412,2],[460,2],[602,7],[673,11],[788,7]]]]
P=[[],[[7,1]],[[1,1],[2,1],[256,1],[516,1]],[[3,1],[5,1],[6,1],[520,1]],[[1,1],[3,1],[6,1],[144,1],[256,1],[516,1]],[[1,1],[2,1],[3,1],[4,2],[9,1],[144,1],[256,1],[512,1]],[[1,1],[3,1],[4,1],[6,1],[17,1],[144,1],[192,1],[256,1],[768,1]],[[1,1],[3,2],[4,1],[6,1],[17,1],[64,1],[128,1],[144,1],[256,2],[512,1]],[[1,3],[2,2],[3,1],[4,3],[8,1],[144,1],[192,1],[256,2],[512,2]],[[1,1],[3,2],[4,2],[8,1],[12,1],[17,1],[64,1],[128,1],[144,1],[256,1],[257,1],[512,1],[514,1]],[[1,2],[2,2],[3,2],[4,4],[9,2],[144,2],[256,2],[512,2]],[[1,3],[2,2],[3,3],[4,4],[8,1],[16,1],[64,1],[128,2],[256,3],[512,3]],[[1,2],[2,1],[3,3],[4,3],[6,1],[17,1],[40,1],[64,1],[128,1],[144,2],[256,3],[512,2]],[[1,4],[2,2],[3,2],[4,4],[8,1],[144,2],[192,2],[256,3],[320,1],[512,3]],[[1,2],[3,4],[4,2],[6,2],[48,2],[64,2],[128,2],[144,2],[256,4],[512,2]],[[1,3],[2,3],[3,3],[4,6],[9,3],[144,3],[256,3],[512,3]],[[1,4],[2,2],[3,4],[4,5],[8,2],[16,1],[64,1],[128,1],[132,1],[144,1],[192,1],[256,4],[512,4]],[[1,3],[2,1],[3,5],[4,5],[6,1],[8,1],[9,1],[48,1],[64,1],[128,1],[144,3],[256,4],[512,3]],[[1,3],[2,2],[3,5],[4,6],[8,2],[17,1],[64,1],[128,2],[144,2],[256,3],[257,1],[320,1],[512,4]],[[1,5],[2,3],[3,5],[4,7],[8,2],[16,1],[64,1],[128,2],[144,1],[192,1],[256,5],[512,5]],[[1,4],[2,4],[3,4],[4,8],[9,4],[144,4],[256,4],[512,4]],[[1,5],[2,3],[3,5],[4,7],[8,1],[9,1],[12,1],[16,1],[64,1],[128,2],[144,2],[192,1],[256,5],[512,5]],[[1,6],[2,4],[3,6],[4,8],[8,2],[16,2],[64,2],[128,4],[256,6],[512,6]]]
def cd(a,b): return -((-a)//b)
def C(h): return cd(15*h+6,11)
def bound(h,f,cert):
    A,q,w=cert
    return cd(h*sum(n for u,n in w)-dict(w).get(f,0)-q*(h+C(h)-1),A)
for A,q,w in D+E:
    assert A>0 and q>=0 and all(u in F and n>=0 for u,n in w)
    assert len(dict(w))==len(w)
    for s in range(1,1024):
        assert sum(n for u,n in w if s&u)<=A+q*s.bit_count()
B=[0]
for k,p in enumerate(P[1:],1):
    assert sum(n*s.bit_count() for s,n in p)==cd(26*k,11)
    assert all(sum(n for s,n in p if s&u)>=k for u in F)
    B.append(sum(n for s,n in p))
hi={}; changes=[]; oldWidths={}; widths={}; remaining=[]; rows=[]
base={4:9,5:9,6:11,7:11,8:13}
for h in range(4,184):
    c=C(h);d=h+c-1;t=11*c-15*h-6;z=(h-4-8*t)//11;m0=28*h-19*c+10
    assert (h-4-8*t)%11==0
    eq=z>=max(1,t-1)
    choices=[m0] if eq else [base[h]] if h in base else []
    for k in range(1,min(22,h-4)+1):
        if c-C(h-k)==cd(26*k,11)-k: choices.append(hi[h-k]+B[k])
    up=hi[h]=min(choices)
    if eq: continue
    old=max(h+1,m0+1,base.get(h,0),*[min(bound(h,f,x) for f in F) for x in D])
    cond=min(max(bound(h,f,x) for x in D+E) for f in F)
    lo=max(old,cond)
    assert lo<=up
    oldWidths[up-old]=oldWidths.get(up-old,0)+1
    widths[up-lo]=widths.get(up-lo,0)+1
    if lo>old:changes.append([h,old,lo,up])
    if lo<up:remaining.append([h,lo,up,[f for f in F if all(bound(h,f,x)<=lo for x in D+E)]])
    rows.append([h,lo,up])
assert changes==[[28,54,55,55],[52,100,101,101],[76,146,147,147]]
assert oldWidths=={0:32,1:44,2:6} and widths=={0:35,1:41,2:6}
print(changes,widths)
print(rows)
print(remaining)
```

## Control and continuation
Original session registration r4-20261124-0240-ec49fyh-own-session-v1 read SUCCEEDED, historical Researcher EM-DIRECT-23537B / TASK_RESEARCH, RA-2D7B4AD1AA5CD3F5D9EF1C76. Current r4-20261125-0230-ec49as-read-v1 read SUCCEEDED, pinned Source 61d8371ddbf9bc6e987e8187773d12c815e38b01, NO_CANONICAL_PUBLICATION_DIRECTORY, native owner projection not evaluated; no formal shared task or CLAIM inferred. Current private writer binding not established; preserve independent non-overwriting portable evidence and pending Activity association. AUTHOR_PROVED / EXACT_FINITE_INTEGER_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.
