# R808 — Charged activation envelope, normalization reversal, and two-pattern extremizers

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable informed research; no shared CLAIM or Result. R807 immutable source fc069513b1b5b6f758cb6e92e661cd9a91920c71:research_notes/portable_direct/R807_SHARP_ACTIVATION_ENVELOPE_AND_CACTUS_CUT_OPTIMIZATION.md (blob 87b59917e247023e94e6bc7a672701845eb0cc19); R806 at 27475d1940a1a3405969be768bb13f0cdb35a1f9. Frozen P000 V5 and joint observer read by exact blobs dc84bdae6595b5e237a2ad50d8b21916adb2e447 and 3923890d77a02d84b772f789e6912dd14f220d14, respectively, same foundation pin a72226e2430ffa4786321ac86e7f0c599d5f0389. ACTIVE worldview and current portable/method rules read. Canonical global entry snapshot 2610b96276675252bdc29ccaf7199d17d384417a with both entry blobs verified. Own session metadata r3-20261126-0919-own-metadata confirmed own RESEARCHER, no RUN, execution_authorized=false. Owner read r3-20261126-0919-running-read pending at derivation; no owner reassignment.

## 1. Exact scope
Finite simple road kernel G=(V,E), positive rational eta_e<=1, arbitrary nonnegative W on a finite allowed set of activation patterns A (including all-active for results explicitly requiring it). Physical induced-vertex activation patterns are a special case. Z_T(A)=sum over F subset A, boundary F=T, of prod eta_e; Z=Z_empty. Q_T=sum W(A)Z_T(A), Q'_T=sum W(A)Z_T(A intersect J), q_T=Q_T/Q_empty, q'_T=Q'_T/Q'_empty. J is retained anti-channel edge set; original W is unchanged. Q_empty and Q'_empty positive for nonzero W. All signs at empty sites may be extended by independent uniform signs. These are auxiliary combination observers, not native signed BRC dynamics. Retain complete matrices, branch provenance, time order and common depth.

## 2. Exact relative charged loss and simultaneous zero-loss test
For every allowed A with Z_T(A)>0 define l(A)=1-Z_T(A intersect J)/Z_T(A). Then (Q_T-Q'_T)/Q_T is a convex average of l(A) weighted by W(A)Z_T(A). Its sharp uniform maximum is max l(A), attained by a single activation pattern. If arbitrary edge-subset activation is permitted, and a feasible T-join F meets C=E minus J, choose A=F **only if F is inclusion-minimal as a T-join**; otherwise the conclusion of complete loss need not follow (cycles can be optional). More precisely, the uniform relative loss is 1 iff there exists an allowed A with Z_T(A)>0 and Z_T(A intersect J)=0. With arbitrary edge subsets this is equivalent to some inclusion-minimal T-join meeting C: take a minimal T-join in A for necessity; for sufficiency a minimal T-join is a forest, hence unique within itself. For T empty the sole minimal join is empty and loss never reaches 1. For a vertex-induced activation family the pattern criterion remains exact, but the arbitrary-edge construction is not automatically permitted.

If all-active is allowed, exact zero loss for every W holds iff C misses the union of all T-joins. For feasible T this union equals all nonbridges plus precisely the bridges with odd T parity on one side. Proof: all T-joins form F0 xor cycle space by R805. Each nonbridge lies in a cycle, so toggling that cycle toggles its membership; bridge membership is fixed by boundary parity. For infeasible T both observations vanish. A family of feasible charges shares a zero-loss cut exactly when it avoids the union of these supports. This strengthens the observer-specific preservation test without declaring physical roads redundant.

## 3. Normalized observer: sharp negative-drift bound
For a fixed activation A let r=Z(A)/Z(A intersect J), x=Z_T(A)/Z(A), y=Z_T(A intersect J)/Z(A intersect J). Let p(A)=W(A)Z(A intersect J)/Q'_empty. Thus q_T=E_p[r x]/E_p[r], q'_T=E_p[y]. By R807, 1<=r<=K=Z(E)/Z(J). Also 0<=y<=x<=1. Proof of x>=y for general T: in R807's random-cluster representation the sign-character expectation conditional on a cluster configuration is 1 iff every cluster contains an even number of T vertices, else 0. This event is increasing under edge addition (merging even clusters preserves the property); use the exact monotone coupling of R807. This is a genuine extension of the two-point argument to any T.

Let p*(A)=r p(A)/E_p[r]. Then q_T-q'_T=E_p*[x-y]+(E_p*[y]-E_p[y]). For any function in [0,1] the latter difference has magnitude at most TV(p*,p). If R=E_p[r] and K>1, TV=E_p|r-R|/(2R). The convex chord bound for |r-R| on [1,K] gives TV <= (R-1)(K-R)/((K-1)R). Maximizing over R gives R=sqrt(K), and
 q'_T-q_T <= (sqrt(K)-1)/(sqrt(K)+1).
 For d=max_A(x-y), q_T-q'_T <= min(1,d+(sqrt(K)-1)/(sqrt(K)+1)).
K=1 gives TV=0 directly. The negative drift bound is sharp over arbitrary W and allowed model instances: take a disjoint cycle gadget with scalar ratio K and a retained pair with eta=1; allow a pattern activating just the gadget (y=x=0) and a pattern activating just the pair (y=x=1). Set retained-law high-r mass 1/(1+sqrt K), so R=sqrt K and equality holds. The construction realizes every K in [1,infinity) with finitely many disjoint cycles and weights in (0,1] (each cycle factor ranges over (1,2], with K=1 separately); for rational K, rational edge weights can realize the factorization. This is a sharp function of K over the stated arbitrary-weight model class, not necessarily sharp for a given physical W.

Exact counterexample already at eta=1/2: disjoint triangle and separate retained edge st; cut one triangle edge. Use two vertex-induced activation patterns, one activating just the triangle, the other just st, equal W. Then q'_st=1/4 but q_st=4/17, so compression INCREASES the normalized two-point correlation by 1/68, while both unnormalized charged numerators are identical. K=9/8. Thus fixed-activation correlation monotonicity cannot simply be transferred through changing normalization. This directly resolves the sign ambiguity left by R807.

## 4. Exact uniform normalized envelope has two-pattern witnesses
Write u=r x. For any allowed finite pattern family, the extremal values of D=q_T-q'_T over arbitrary nonzero W are attained with at most two patterns. Proof: the map W -> p is onto the probability simplex, since Z(A intersect J)>0. Fix R=E_p r. The feasible p satisfy sum p=1 and sum p r=R. On this compact polytope D=E_p[u]/R-E_p[y] is linear. Each vertex has at most two positive coordinates: three positive coordinates admit a nonzero signed perturbation with both sum and r-weighted sum zero, small in both directions, contradicting extremality. A global extremizer exists by continuity (R>=1), and its fixed-R slice has such a vertex. This applies to both extrema, hence to absolute error.

Explicit pair calculation: for patterns b,a use p(a)=t in [0,1]. Let delta r=r_a-r_b, delta u=u_a-u_b, delta y=y_a-y_b. D(t)=(u_b+t delta u)/(r_b+t delta r)-(y_b+t delta y). Its derivative is (delta u r_b-u_b delta r)/(r_b+t delta r)^2-delta y. Check endpoints and any interior root of this equation. If delta r=0 the function is affine; if delta y=0 the derivative is constant in sign; identically constant cases need endpoints only. Otherwise a root requires the ratio (delta u r_b-u_b delta r)/delta y positive and the positive square root to lie between the endpoint r's. Thus an exact algebraic envelope can be computed in O(P^2) pair candidates given P explicit pattern rows; rational inputs require at most quadratic algebraic comparisons (or certified interval refinement with exact equality handling). Pattern enumeration and obtaining Z_T are separate potentially exponential costs.

The same proof applies to any fixed bounded sign-distribution test event, replacing x,y with the full and retained conditional event probabilities; monotonicity is not needed for the two-pattern theorem. Maximizing over the finite sign-event space shows the worst-case total variation between full and retained sign distributions also has a two-pattern witness (does not give a polynomial algorithm in the number of observed signs). This is a resource-reduction theorem for worst-case certification, not a representation of every actual W by two patterns.

## 5. Reproducible exact calculation
The following verifier was actually executed. Covers all labeled simple graphs on 2–4 vertices, all cuts and all charges, deterministic eta=(1+(g+3i) mod 4)/4, all vertex-induced activation masks. For each cut-charge pair compare monotonicity, zero loss on full activation, a deterministic three-pattern retained-law mixture and the fixed-R extrema among its two-pattern interpolants. Check negative-drift bound by rational squaring. All arithmetic BigInt fractions. The counterexample is checked separately. It does not exhaust arbitrary W, nor implement the quadratic algebraic pair optimizer; these claims use the proof above. Results: {"graphs":74,"cutChargeCases":11892,"monotonicityChecks":188400,"zeroLossChecks":11892,"mixtureChecks":11892,"twoPatternHullChecks":11892,"negativeBoundChecks":13,"counterexampleChecks":1}.

```javascript
function verify(){
 const f=(n,d=1n)=>[BigInt(n),BigInt(d)],add=(a,b)=>[a[0]*b[1]+b[0]*a[1],a[1]*b[1]],neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>[a[0]*b[0],a[1]*b[1]],div=(a,b)=>{let x=a[0]*b[1],y=a[1]*b[0];return y<0n?[-x,-y]:[x,y]},cmp=(a,b)=>a[0]*b[1]-b[0]*a[1],sq=a=>mul(a,a),one=f(1),zero=f(0);
 let stats={graphs:0,cutChargeCases:0,monotonicityChecks:0,zeroLossChecks:0,mixtureChecks:0,twoPatternHullChecks:0,negativeBoundChecks:0,counterexampleChecks:0};
 function ck(x){if(!x)throw Error(JSON.stringify(stats))}
 for(let n=2;n<=4;n++){
 let base=[];for(let u=0;u<n;u++)for(let v=u+1;v<n;v++)base.push([u,v]);
 for(let g=0;g<1<<base.length;g++){
 const E=base.filter((_,i)=>g>>i&1),m=E.length,N=1<<m,full=N-1,L=1<<n;
 const Z=Array.from({length:L},()=>Array(N).fill(0n));let support=Array(L).fill(0);
 for(let F=0;F<N;F++){let b=0,w=1n;for(let i=0;i<m;i++)if(F>>i&1){b^=(1<<E[i][0])^(1<<E[i][1]);w*=BigInt(1+(g+3*i)%4)}else w*=4n;Z[b][F]=w;support[b]|=F}
 for(let T=0;T<L;T++)for(let i=0;i<m;i++)for(let A=0;A<N;A++)if(A>>i&1)Z[T][A]+=Z[T][A^(1<<i)];
 const act=Array.from({length:L},(_,v)=>E.reduce((a,[s,t],i)=>a|(((v>>s&1)&&(v>>t&1))?1<<i:0),0));
 for(let J=0;J<N;J++)for(let T=0;T<L;T++){
 stats.cutChargeCases++;ck((Z[T][full]===Z[T][J])===((support[T]&~J)===0));stats.zeroLossChecks++;
 let K=f(Z[0][full],Z[0][J]);
 let rows=act.map(A=>({r:f(Z[0][A],Z[0][A&J]),u:f(Z[T][A],Z[0][A&J]),y:f(Z[T][A&J],Z[0][A&J])}));
 for(let z of rows){ck(cmp(z.u,mul(z.r,z.y))>=0n&&cmp(z.r,K)<=0n);stats.monotonicityChecks++}
 let ids=[(g+J+T)%L,(3*g+2*J+T+1)%L,(5*g+J+3*T+2)%L],r=zero,u=zero,y=zero;
 for(let i of ids){r=add(r,div(rows[i].r,f(3)));u=add(u,div(rows[i].u,f(3)));y=add(y,div(rows[i].y,f(3)))}
 let d=sub(div(u,r),y);stats.mixtureChecks++;
 if(cmp(d,zero)<0n){let h=neg(d);ck(cmp(h,one)<0n&&cmp(sq(div(add(one,h),sub(one,h))),K)<=0n);stats.negativeBoundChecks++}
 let lo=null,hi=null;
 for(let i of ids)for(let j of ids){let a=rows[i],b=rows[j];if(cmp(a.r,b.r)>0n||cmp(a.r,r)>0n||cmp(b.r,r)<0n)continue;
 let v;if(cmp(a.r,b.r)===0n){v=sub(div(a.u,r),a.y)}else{let t=div(sub(r,a.r),sub(b.r,a.r));v=sub(div(add(mul(sub(one,t),a.u),mul(t,b.u)),r),add(mul(sub(one,t),a.y),mul(t,b.y)))}
 if(lo===null||cmp(v,lo)<0n)lo=v;if(hi===null||cmp(v,hi)>0n)hi=v}
 ck(lo!==null&&cmp(d,lo)>=0n&&cmp(d,hi)<=0n);stats.twoPatternHullChecks++;
 }
 stats.graphs++;
 }
 }
 // triangle (eta=1/2) plus separate pair (eta=1/2); cut one triangle edge.
 let R=f(9,8),q=f(1,4),actual=div(f(1,2),add(one,R));
 ck(cmp(sub(q,actual),f(1,68))===0n);stats.counterexampleChecks++;
 return stats;
}
console.log(JSON.stringify(verify()));
```

## 6. Next
Use the two-pattern theorem to develop computable sparse activation extremal certificates for actual Port weight constraints, and cactus/series-parallel joint-charge resource optimization. Investigate if a sharper conditional d bound can combine R806 paths with R807 scalar K. General tilted-cluster FPRAS remains open. No native physical inference or formal admission claimed.
