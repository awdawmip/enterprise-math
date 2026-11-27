# R834 — Dependency-cover quotient and cost regrading for exact joint-moment FPTAS

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_RATIONAL_CHECKED / NOT_REVIEWED.
Independent portable TASK_RESEARCH, EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91, own session metadata recovered by r3-20261127-r834-own-read, execution_authorized=false, no run. Owner query r3-20261127-r834-running-read was RUNNING during derivation; no shared claim or Result writes. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint-observer 3923890d77a02d84b772f789e6912dd14f220d14; ACTIVE worldview and current global entries main@54fab8643647b08ad70a92da127a2699b358cd75 read. Current portable, BRC-only, residual and research method rules read. R833 predecessor 4b4f175b5aacdbedd4d6b735b0392ad26c70efd1:research_notes/portable_direct/R833_PARTIAL_OVERLAP_UNION_FOOTPRINT_CERTIFICATE.md; R832 proof d7b2f813b12780c30120efc98f0577cec21db0dc:research_notes/portable_direct/R832_OVERLAP_BUNDLE_CONTEXTUAL_PRODUCT_CERTIFICATE.md; R825 enumeration 6ee4743d62741ab9898036d556175202ab6c76d8:research_notes/portable_direct/R825_ADAPTIVE_PREFIX_ENTROPY_PAYMENT.md.
Auxiliary independent-group fixed-charge joint-moment model only. No new native Heartbeat computation, classical physical reference comparison or native residual attribution. All original signed BRC information, road matrices, branch IDs, provenance, time order and common depth are retained; only the analytic/algorithmic dependency coordinate is changed.

## 1. Dependency-cover theorem
Use R833 hypotheses: independent physical groups B, original labeled factors f, I_f measurable on true footprint F_f, signed rational alpha_f, exact joint moments with |E prod_{f in S} I_f|<=prod_{f in S} lambda_f, polynomial-time polynomial-bit exact oracle. P_U(t)=E prod_{f in U}(1+alpha_f I_f t^{c_f}), positive integer c_f. Partition labels into bundles H, true union V_H. Let G be their dependency graph: distinct H,K adjacent iff V_H intersects V_K.
Choose a finite explicit family of nonempty auxiliary sets A of bundle IDs, called anchors. Every bundle belongs to at least one anchor, and every edge of G has both endpoints together in some anchor. Added edges are permitted. The sets need not be actual physical groups, and no new probability independence is assumed. Write A_H={A:H in A}, D(A)=union of original labels in H in A. Put R>1, u_f=|alpha_f| lambda_f R^c_f, w_H(U)=prod_{f in H intersect U}(1+u_f)-1, w_H=w_H(all). Zero envelopes can be excluded from this observer. For nonnegative d_AH define Q_A=prod_{H in A}(1+d_AH), T_{A|H}=prod_{K in A minus {H}}(1+d_AK). Then the following suffice:
    Q_A<2,
    w_H prod_{D in A_H minus {A}} T_{D|H}/(2-T_{D|H}) <= d_AH.      (1)
For every U and |t|<=R:
    P_U != 0,
    |P_U/P_{U minus D(A)}-1| <= Q_A(U)-1,
    Q_A(U)=prod_{H in A}(1+d_AH w_H(U)/w_H).                       (2)
For S subset U intersect D(A), V=U minus S:
    |P_U/P_V-1| <= [Q_A(U)-Q_A(V)]/[2-Q_A(V)].                    (3)
The log branch with log P(0)=0 satisfies
    |log P(t)| <= sum_A (Q_A-1)/(2-Q_A),
    E_k <= R^(-k)/(R-1) sum_A (Q_A-1)/(2-Q_A).                    (4)

Proof: G_H(U,t)=prod_{f in H intersect U}(1+alpha_f I_f t^c_f)-1 exactly. A selected bundle support C has weight W_U(C)=E prod_{H in C}G_H bounded in modulus by prod_{H in C}w_H(U), by the original joint envelope. If two sets of bundles have no edge between them in the anchor intersection graph, they have disjoint true union footprints, hence their random variables are independent. Thus the expectation factors across anchor-connected components; the exact polymer expansion on the anchor graph follows. Extra anchor edges only change the grouping of components. In particular, deletion of anchor A gives the R832 identity P_U=P_{U minus D(A)}+sum_C W_U(C)P_{U minus N[C]}, with C connected and touching A; N[C] is the closed neighborhood in the anchor graph. No assumption of measurability on invented independent variables is needed.

Induct on |U| as R832: use the deterministic FIFO alternating tree rooted at A, discover each selected bundle once, attach all its other anchors, repeat anchors as leaves. The set of selected bundle IDs can be reconstructed from the tree, giving an injection. Deleting distinct anchors of C in first-occurrence order after root A gives U minus N[C]; each nonroot anchor D reached through H has H absent, so the inductive inverse ratio is <=1/(2-T_{D|H}). Repeated occurrences can be paid again since the bound >=1. The sum over all alternating trees of bounded height has child-subset majorant T_{D|H} by (1); at the root each selected H contributes <=d_AH w_H(U)/w_H. Nonnegative sums increase with height and are bounded by Q_A(U). Removing empty tree proves (2), closes nonvanishing because Q_A(U)<2 and every nonempty surviving support is incident to an anchor. For (3), expand P_U-P_V over the same root-deletion identity. Complement ratios agree since S subset D(A) subset N[C] for each root-touching C. Changed bundle weights are only at the root: the absolute difference is at most prod_{H in C}w_H(U)-prod_{H in C}w_H(V). Every selected root-incident bundle is discovered at the root. Its descendants are unchanged. The nonnegative difference of root weight products times the same descendant bounds sums to Q_A(U)-Q_A(V); divide by |P_V/P_{U minus D(A)}|>=2-Q_A(V). Telescoping anchor deletions and using the log series gives (4) by Cauchy. This is R832/R833 with their only graph-factorization premise verified on the new anchor cover. It holds for arbitrary original subsets, and preserves all exact moments.

## 2. Certificate-preserving quotient, constructive cover selection
The original union-incidence family is A_B={H:B in V_H}. Discard empty sets. If A_D is contained in A_B for another retained anchor B, drop D, with its own payments, from the analytic cover. Every edge and vertex represented by D remains represented by B. The remaining Q and T are unchanged, each remaining inequality (1) loses only a factor >=1, so any old witness remains a witness at the same R. The bound sum in (4) weakly decreases, strictly if a dropped anchor had Q>1. In particular, equal incidence rows are represented just once, and inclusion-maximal rows suffice. For m bundles and g physical rows, Boolean incidence storage and pairwise containment tests give O(g^2 m) elementary Boolean checks; duplicate hashing can accelerate. No minimum clique-cover solver is required. Any explicitly verified alternative cover, e.g. graph edges as two-ID anchors with singleton anchors for isolated vertices, may be tried without changing the exact observer. Construct graph by expanding each physical incidence row into its pairs, polynomial in explicit input; test vertex and edge coverage by the same method. Optimal cover size, payment tradeoff and global search complexity are open. Retain true rows and their original data for the moment oracle and for any native or future observation. Even arbitrary true group deletion remains within (3) whenever the true deletion labels lie in a common retained anchor; this is automatic for the inclusion quotient (take a containing maximal row). An arbitrary synthetic cover need not have such a row; (3) is then only a per-anchor statement.

## 3. Exact cost regrading
Use a separate vertex/edge-covering anchor family for the ORIGINAL factor dependency graph (not necessarily the bundle cover). Let a_f be the positive number of anchors incident to f. Choose integer L_f>=0 satisfying original-label Kraft on each such anchor, and set new interpolation degrees c'_f=a_f+L_f. Define P'_U(t) with c'_f instead of c_f. P'_U(1)=P_U(1) exactly for every U, with original coefficients alpha, signs and full joint moments. It is a change of interpolation, not an identity at general t. Apply (1)-(4) with u_f=|alpha_f|lambda_f R^{c'_f}.
R825 FIFO enumeration works on this original-label anchor graph: start from a root anchor, emit 1 plus prefix codeword of each newly discovered label, enqueue unseen anchors, then 0. Bits <=1+sum_{f in C}(a_f+L_f); a support can be decoded, checked and deduplicated. Nonempty support touches an anchor; original dependency edges are covered, hence any disconnected support on the anchor graph has vanishing log Mobius difference. All coefficients are evaluated using the actual original moment oracle on label subsets, not approximate products. Thus connected-support Mobius extraction takes g' 2^{O(k)} poly(N,k) with g' number of original-label anchors, N full original input length. For fixed R>1, Q_A<=2-eta for fixed eta>0, supplied polynomial-bit certificate, polynomial-bit moment oracle and explicit incidences, (4) gives k=O(log((g'+g_a+1)/epsilon)), g_a analytic anchors. Exact rational verification uses polynomially bounded exponents for explicit constructions (or polynomial-bit powers if supplied); eligible labels with c'<=k suffice for enumeration. Real coefficients, P'(0)=1 and zero-freeness imply P'(1)>0; with positive baseline and R825 recovery this is a deterministic FPTAS. No production timing claim.

## 4. Strict separation from EVERY R833 partition on original physical groups
Let G0 be a simple 4-regular square torus on side l>=10, n=l^2, connected and unbounded treewidth. One factor per graph vertex. Each graph edge e has h>=512 independent physical groups with that same pair of incident factors; no other groups. Each factor has true arity 4h, each group degree two. Original incidence graph contains a subdivision of G0. All factor IDs and groups distinct. Each physical group has independent Bernoulli bit of probability p=1-1/(100h); I_f is the product of its true bits. The exact joint moment of a support is p to the number of incident distinct physical groups, with polynomial bit length (explicit input). Choose all signed alpha_f with |alpha_f|=243/32768. lambda_f=1 is valid. More strongly any valid envelope satisfies lambda_f>=E I_f=p^{4h}>=24/25 (Bernoulli inequality), so at ANY R>=1 and nonnegative degrees the activity of each original factor is >=v=729/102400.

Consider any partition of original factors into R833 bundles, still paying at every original physical group in their union footprints. All w_H>=v, all d_BH>=w_H because other ratios>=1. If partition has more than one bundle, connectedness gives an edge e with endpoint factors in different bundles H,K. Their h shared physical groups each have T_{D|H}>=1+v. For each such group B, R833 requires
    d_BH >= v ((1+v)/(1-v))^{h-1} > 1
since the last inequality already holds at h=512 (exact check below). This contradicts Q_B<2. If the partition has just one bundle, w_H>=(1+v)^n-1>1 at n>=100, another contradiction. Therefore **no R833 partition and no nonnegative payments, even optimized valid moment envelopes and degrees, certify ANY R>=1 on these original groups**. The assertion concerns the R833 physical-incidence certificate, not other representations or algorithms.

Our quotient retains one anchor per graph edge, with its two factors; singleton bundles suffice. Original-label anchor arity four, L=1, c'=5, R=4/3. With lambda=1,
    u_f=|alpha_f| R^5=1/32,
    d_Af=1/16, Q_A=(17/16)^2=289/256,
    w_f prod T/(2-T)=(1/32)(17/15)^3=4913/108000<1/16.
All local witnesses pass uniformly, hence deterministic FPTAS for the auxiliary family with arbitrary signs. The full physical moment p^{union size} is retained, so even when h grows there is no physical independence assumption replacing the correlations. Analytic anchor count 2n versus original 2nh; original c=4h+1 with L=1 becomes 5, while target P(1) is identical. At h=512, 512-fold reduction in analytic row count and original cost 2049 -> 5. For n=10000, error_log=1/100, exact cutoff from (4) at 20000 anchors is k=48. Old physical-incidence witness fails already at R=1, so no finite comparable old certified cutoff. This is a structural algorithmic separation, not a native Port realization. The fixed alpha is independent of h and n.

## 5. Executed exact checks
Six physical incidence fixtures, including duplicate rows, strict artificial overgraph, synthetic clique not present in physical rows, mixed bundles, and isolated label. Three rational Bernoulli/sign configurations each. For each, all original label subsets at three Gaussian-rational unit directions multiplied by R, with original degrees and u=1/128; original joint probabilities and P_U computed exactly. Test cover, local certificates, nonvanishing, full and every partial anchor deletion. Also check separation and family parameters by exact rationals, and minimal cutoff by integer powers. No native computation or physical reference; model-internal combinatorial evidence. Actual result: {"stats":{"fixtures":18,"cover":43,"local":40,"full":1944,"partial":5643,"nonzero":936,"family":10,"cutoff":2},"total":8618,"k":48,"cross_ratio_lower_approx":9.771624880857063,"one_bundle_lower_approx":1.0327548003320013}. General statements use the analytic proof. No production performance or formal review claimed.

```javascript
function replay(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a};
 const q=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<=0n)throw Error("denom");let g=gcd(a,b);return [a/g,b/g]};
 const add=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]),div=(a,b)=>{if(b[0]<=0n)throw Error("div");return q(a[0]*b[1],a[1]*b[0])},le=(a,b)=>a[0]*b[1]<=b[0]*a[1],lt=(a,b)=>!le(b,a);
 const pow=(a,n)=>{let p=q(1);while(n){if(n%2)p=mul(p,a);n=Math.floor(n/2);if(n)a=mul(a,a)}return p},one=q(1),two=q(2),zero=q(0),prod=xs=>xs.reduce(mul,one);
 const z=(a,b=zero)=>[a,b],za=(a,b)=>z(add(a[0],b[0]),add(a[1],b[1])),zs=(a,b)=>z(sub(a[0],b[0]),sub(a[1],b[1])),zm=(a,b)=>z(sub(mul(a[0],b[0]),mul(a[1],b[1])),add(mul(a[0],b[1]),mul(a[1],b[0]))),scale=(a,b)=>z(mul(a[0],b),mul(a[1],b)),norm=a=>add(mul(a[0],a[0]),mul(a[1],a[1])),zp=(a,n)=>{let p=z(one);while(n--)p=zm(p,a);return p};
 const mask=ls=>ls.reduce((m,i)=>m|(1<<i),0),pop=m=>{let n=0;while(m){m&=m-1;n++}return n},subset=(m)=>{let a=[];for(let s=m;;s=(s-1)&m){a.push(s);if(!s)return a}},assert=(ok,msg)=>{if(!ok)throw Error(msg)};
 const fixtures=[
 {physical:[[0,1],[1,2],[0,2]],bundles:[[0],[1],[2]],anchors:[[0,1,2]]},
 {physical:[[0,1],[0,1],[0,1],[1,2],[1,2],[2,3],[2,3],[0]],bundles:[[0],[1],[2],[3]],anchors:[[0,1],[1,2],[2,3]]},
 {physical:[[0,1],[0,1],[0,1],[1,2],[1,2],[2,3],[2,3],[0]],bundles:[[0],[1],[2],[3]],anchors:[[0,1,2],[2,3]]},
 {physical:[[0,1],[1,2],[2,3],[3,0]],bundles:[[0,2],[1],[3]],anchors:[[0,1],[0,2]]},
 {physical:[[0,1],[1,2],[2,0],[2,3],[3,4],[4,2]],bundles:[[0],[1],[2],[3],[4]],anchors:[[0,1,2],[2,3,4]]},
 {physical:[[0,1],[1,2],[2,0],[3]],bundles:[[0],[1],[2],[3]],anchors:[[0,1,2],[3]]}
 ];
 let stats={fixtures:0,cover:0,local:0,full:0,partial:0,nonzero:0,family:0,cutoff:0};
 for(const a of fixtures){
  let bm=a.bundles.map(mask),pm=a.physical.map(mask),am=a.anchors.map(mask),n=a.bundles.flat().length,all=(1<<n)-1;
  for(let i=0;i<bm.length;i++){assert(am.some(m=>m&(1<<i)),"vertex cover");stats.cover++;for(let j=0;j<i;j++){if(pm.some(m=>(m&bm[i])&&(m&bm[j]))){assert(am.some(m=>(m&(1<<i))&&(m&(1<<j))),"edge cover");stats.cover++;}}}
  let d=q(1,16),u=q(1,128),w=bm.map(m=>sub(pow(add(one,u),pop(m)),one));
  let Q=am.map(m=>pow(add(one,d),pop(m))),T=(A,H)=>pow(add(one,d),pop(am[A])-1);
  for(let A=0;A<am.length;A++){assert(lt(Q[A],two),"Q");stats.local++;for(let H=0;H<bm.length;H++)if(am[A]&(1<<H)){let b=w[H];for(let D=0;D<am.length;D++)if(D!==A&&(am[D]&(1<<H))){let t=T(D,H);b=mul(b,div(t,sub(two,t)))}assert(le(b,d),"local");stats.local++;}}
  const db=am.map(m=>bm.reduce((x,b,i)=>x|((m&(1<<i))?b:0),0));
  const qctx=(A,U)=>prod(bm.flatMap((b,i)=>am[A]&(1<<i)?[add(one,mul(d,div(sub(pow(add(one,u),pop(b&U)),one),w[i])))]:[]));
  for(let v=0;v<3;v++){
    stats.fixtures++;
    let probs=pm.map((_,i)=>q(2+(i+v)%4,7)),c=Array.from({length:n},(_,f)=>pm.filter(m=>m&(1<<f)).length+1);
    let moments=Array.from({length:all+1},(_,S)=>prod(pm.flatMap((m,i)=>m&S?[probs[i]]:[])));
    for(const p of [z(one),z(zero,one),z(q(3,5),q(4,5))]){
      const activity=c.map((k,f)=>scale(zp(p,k),((f+v)%3===0)?neg(u):u));
      const weights=Array.from({length:all+1},(_,S)=>scale(activity.reduce((a,x,f)=>S&(1<<f)?zm(a,x):a,z(one)),moments[S]));
      const P=Array.from({length:all+1},(_,U)=>subset(U).reduce((a,S)=>za(a,weights[S]),z(zero)));
      for(let U=0;U<=all;U++){
        assert(lt(zero,norm(P[U])),"nonzero");stats.nonzero++;
        for(let A=0;A<am.length;A++){
          let V0=U&~db[A],Qu=qctx(A,U),b=sub(Qu,one);
          assert(le(norm(zs(P[U],P[V0])),mul(mul(b,b),norm(P[V0]))),"full");stats.full++;
          for(const S of subset(U&db[A])){
            let V=U&~S,Qv=qctx(A,V),b=div(sub(Qu,Qv),sub(two,Qv));
            assert(le(norm(zs(P[U],P[V])),mul(mul(b,b),norm(P[V]))),"partial");stats.partial++;
          }
        }
      }
    }
  }
 }
 const R=q(4,3),alpha=q(243,32768),v=q(729,102400),d=q(1,16);
 assert(le(v,mul(alpha,q(24,25))),"v");stats.family++;
 assert(lt(one,mul(v,pow(div(add(one,v),sub(one,v)),511))),"all cross partitions");stats.family++;
 assert(lt(two,pow(add(one,v),100)),"single bundle");stats.family++;
 assert(le(mul(alpha,pow(R,5)),q(1,32))&&le(q(1,32),mul(alpha,pow(R,5))),"activity");stats.family++;
 assert(le(mul(q(1,32),pow(q(17,15),3)),d),"new certificate");stats.family++;
 assert(lt(pow(add(one,d),2),two),"new Q");stats.family++;
 for(let h of [512,513,1024,2048]){assert(le(q(24,25),pow(sub(one,q(1,100*h)),4*h)),"Bernoulli lower");stats.family++}
 let k=0,err=mul(q(20000),mul(q(33,223),q(3)));while(!le(err,q(1,100))){err=mul(err,q(3,4));k++}assert(le(err,q(1,100)),"cutoff");stats.cutoff++;assert(lt(q(1,100),mul(err,R)),"minimal cutoff");stats.cutoff++;
 return {stats,total:Object.entries(stats).filter(([k])=>k!=="fixtures").reduce((s,[_,v])=>s+v,0),k,cross_ratio_lower_approx:Number(v[0])/Number(v[1])*Math.pow(1+2*Number(v[0])/Number(v[1]),511),one_bundle_lower_approx:Math.pow(1+Number(v[0])/Number(v[1]),100)-1};
}
console.log(JSON.stringify(replay()));
```

## 6. Continuation
Investigate a certified cover/partition co-optimization that changes both the graph of bundles and original-label interpolation degrees, with local monotone payment updates and a nontrivial approximation guarantee. In particular consider high-degree physical rows where maximal-row quotient cannot reduce repeated pairwise dependencies but synthetic clique covers can; account for tradeoff between anchor degree, arity and new Kraft lengths. Native Port realizability and unrestricted complete Port FPTAS remain open. Preserve R833 and earlier exact results, do not re-run their mathematics merely for bookkeeping.
