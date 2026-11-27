# R831 - Contextual deletion resource frontier

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_RATIONAL_CHECKED / NOT_REVIEWED.
Independent portable TASK_RESEARCH, EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91. Own recovery r3-20261127-r831-own-read verified session metadata, no own run, execution_authorized=false. Owner read r3-20261127-r831-running-read was RUNNING during proof. No shared claim or Result mutation. Current control Source 669363d00332e93d315a488eb9e23dccff4389ff. Global entries verified at main 75444da7e12456cdfb649df5c493d79ab792c16c; ACTIVE worldview and current method/portable/BRC-only/residual constraints read. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 dc84bdae6595b5e237a2ad50d8b21916adb2e447; joint observer 3923890d77a02d84b772f789e6912dd14f220d14 read. Frozen Heartbeat companion 404; current companion read for terminology only, no science repin.
Predecessors: e64e6c6af3b699961962e436aed19de8ab3e3d7e:research_notes/portable_direct/R830_PARENT_EXCLUSION_ENTROPY_FRONTIER.md; 91fde1508398af7b109503e1155fc9f727853f50:research_notes/portable_direct/R828_GROUP_DELETION_BRANCHING_MAJORANT_FPTAS.md sections 1-2; 6ee4743d62741ab9898036d556175202ab6c76d8:research_notes/portable_direct/R825_ADAPTIVE_PREFIX_ENTROPY_PAYMENT.md section 1. Auxiliary combinatorial theorem, not native BRC dynamics, new classical physical comparison or native residual attribution. Preserve all signed coefficients, joint observations, road matrices, ordered branch identities and common depth.

## 1. Stronger contextual deletion theorem
Use R830's independent groups, factor footprints F_f (s_f>=2), signed rational alpha_f, joint moment envelope |E prod I_f|<=prod lambda_f and factorization over disjoint group supports; exact polynomial-time polynomial-bit moment oracles and positive baseline. Let b_f=|alpha_f|lambda_f, a_f=2^s_f b_f, M=max_B sum_{f incident B} sqrt(a_f). Zero activities vanish only for this observer. Fix beta>0 and promise M<=sqrt(beta); p_f=sqrt(a_f/beta), sum p_f<=1 at every group, L_f=ceil(log2(1/p_f)), c_f=s_f+L_f. Define P_U(t)=E prod_{f in U}(1+alpha_f I_f t^c_f). For 1<R<2 and 0<rho<1 let A=(1+rho)/(1-rho).
Theorem: if
    R A <= 2,    beta R^3/4 <= rho,                              (1)
then every P_U is nonzero on |t|<=R, and every deletion has the context-sensitive bound
    |P_U/P_{U minus F(B)} - 1| <= rho sum_{f in U incident B} p_f. (2)
This replaces R828's fixed denominator (1-rho)^(-1) and R830's parent exclusion only in the numerator by parent exclusion in both. In particular the full log bound and tail are |log P|<=g rho/(1-rho), E_k<=g rho/[(1-rho)(R-1)] R^(-k).

## 2. Proof: group deletion in breadth-first order
As in R828, exact connected polymer decomposition gives P_U=P_{U minus F(B)}+sum_C w(C)P_{U minus N[C]} with C connected subset U touching B, |w(C)|<=prod u_f, u_f=b_f R^c_f. Induct simultaneously on |U|, with empty polynomial 1. If B has incident factors in U, U minus F(B) is smaller. Choose the deterministic R828 queue injection for C: on processing the first occurrence of a group discover all as-yet-undiscovered incident factors of C; each discovered factor f has as children all its other groups; repeated group occurrences are leaves, each factor label occurs once. Process group nodes in queue order. For each distinct nonroot group D, use its first occurrence, whose parent factor f was discovered at an earlier processed group E. Delete all factors incident to each distinct group in this order starting with root B. When deleting D, f is already absent because E was deleted. The current subset V is smaller than U and its p-mass at D is at most 1-p_f. By inductive (2), the reciprocal deletion ratio has modulus <=1/[1-rho(1-p_f)]. This is the crucial bound, valid even with parallel factors, repeated groups and cycles. Deleting all groups of C gives exactly U minus N[C]. Paying repeated group occurrences again with their respective >=1 factors can only increase the product.

Consequently the deviation in (2) is bounded by a nonnegative alternating-tree sum minus its empty term. Each factor occurrence pays u_f, each nonroot group occurrence with parent f pays 1/[1-rho(1-p_f)]. Parent f is never a child of its own group occurrence. Root children are restricted to the actual set U intersect F(B). For descendants we may enlarge the allowed children to all incident labels except parent. The injection is one tree per C, and the set of factor labels recovers C. For a finite-height subtree majorant use Y_{D|f}=1+rho(1-p_f), initialized with 1. Put
    x_h=u_h [(1+rho(1-p_h))/(1-rho(1-p_h))]^(s_h-1).
If for any subset H of incident factors with mass m=sum p_h<=1 we have prod_{h in H}(1+x_h)<=1+rho m, then each oriented subtree excluding f is <=Y_{D|f}, and the root with actual incident subset has bound 1+rho sum_{U intersect F(B)}p_f. Monotone limit of the finite-height sums proves (2). Since rho<1, the induction also proves nonvanishing (choose any root incident to a factor); a group with no incident factor has exact ratio 1. Telescoping the analytic logarithms of the deletion ratios, all equal to 1 at t=0, gives the stated log bound and Cauchy tail.

## 3. Scalar inequality for the contextual witness
Let eta=log2 R, r=2-eta, A(p)=[1+rho(1-p)]/[1-rho(1-p)], K=beta R^3/4. Since A(p)<=A, R A<=2 and s>=2, R^L<=R p^(-eta),
    x_f <= K p_f^r A(p_f).
Write F(p)=p^r A(p). Direct differentiation gives
    p F'(p)/F(p)=r-2rho p/[1-rho^2(1-p)^2] >= r-2rho,
because p<=1-rho^2(1-p)^2 for 0<p<=1. The elementary inequality -ln z>=2(1-z)/(1+z) for 0<z<=1 follows by differentiation. Apply it at z=R/2 and use rho<=(2-R)/(2+R), ln 2<4/5 (e.g. integral of 1/x on [1,2] bounded above by its secant trapezoid 3/4). It gives r-1>=2rho/ln 2 >= (5/2)rho. Therefore pF'/F>=1+rho/2>0, F(p)<=F(1)=1. For y=K F(p)<=rho, the inequality
    (1+y)ln(1+y) <= y(1+y/2)
holds: differentiate y(2+y)/(2(1+y))-ln(1+y), whose derivative is y^2/[2(1+y)^2]>=0. Thus for h(p)=ln(1+K F(p)), p h'(p)>=y(1+rho/2)/(1+y)>=h(p). So h(p)/p is increasing and h(p)<=p ln(1+K)<=p ln(1+rho). Sum over H and use convexity of m -> (1+rho)^m on [0,1] to obtain prod(1+x_h)<=(1+rho)^m<=1+rho m. This proves the induction's scalar condition.

## 4. Frontier and sharpness of this explicit witness
Optimizing rho in (1) gives rho=(2-R)/(2+R) and
    beta <= 4(2-R)/[R^3(2+R)].
For every fixed M<sqrt(4/3) there exist fixed rational beta,R,rho satisfying the promise and strict positive radius margin. In particular M<=23/20=1.15, R=1001/1000 works. Compare R830 beta_old=8(2-R)/[R^2(2+R)^2]; ratio new/old=(2+R)/(2R)>1 for 1<R<2. Limit beta=4/3 versus 8/9. This is a sharp boundary of this specific uniform contextual witness: if R A>2, take a fixed sufficiently small rational p so R A(p)>2 and a lone factor with arbitrarily large arity; x_f then grows beyond the root budget rho p. If beta R^3/4>rho, take two pair factors sharing their two groups, with p=1-e and e. As e decreases to zero through positive rationals, L_strong=1 and x_strong tends to beta R^3/4, exceeding even the full root budget rho. These are auxiliary constant-indicator instances; rational activity approximations preserve strict violations when needed. They do not bound actual zero-free radii or other algorithms. At M=3/4, R=6/5 and rho=1/4, the new tail has minimum sufficient degree 79 for g=10000, epsilon_log=0.01, compared to R830's 127 at R=9/8, rho=7/25. At M=1.15 the old universal certificate is impossible and the new one works; the replay also checks failure of the actual R830 root contribution for the near-concentrated p=0.99 pair and success of the corresponding contextual singleton root bound.

## 5. Algorithm and evidence
The R825 Kraft queue and exact connected-support Mobius extraction are unchanged: enumerate g*2^O(k) poly(N,k) connected supports of cost <=k, compute all necessary original pinned joint moments and exact truncated formal log coefficients, not the envelope. Polynomial-bit code lengths use least integer L>=0 with 2^(2L)a_f>=beta, so irrational p values need not be evaluated for promised inputs. Rational p witnesses can also be checked explicitly. For fixed R>1 and rho<1, k=O(log((g+1)/epsilon)), exact rational arithmetic and certified scalar recovery yield deterministic FPTAS under the original R825 oracle/input hypotheses; baseline zero is handled exactly. Real P(1)>0 follows from P(0)=1, real coefficients and nonvanishing on [0,1]. No native Port realizability or runtime benchmark claimed.
Executed exact BigInt rational checks: {"stats":{"parameters":4,"arity":27600,"subset_products":4088,"ratios":2160,"cutoffs":4,"separation":2},"old":127,"current":79,"total":33858}. The parameter, arity and product checks cover the four explicit tuples, all rational n/d with 1<=n<=d<=24, arities 2..24, and all ordered positive resource lists of at most four entries with common denominator <=10 and mass<=1 (including empty lists). The Gaussian-rational tests evaluate every subset and group deletion on five specified incidence shapes, three probability/weight fixtures, three complex points; within groups ports share a hard-correlated bit. These verify the stronger actual subset-mass ratio, not only the sufficient scalar inequality. Analytic proof covers the full disk and general input.
```javascript
function verify(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a};
 const F=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);const g=gcd(n,d);return [n/g,d/g]};
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>add(a,[-b[0],b[1]]),mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]),pow=(a,k)=>F(a[0]**BigInt(k),a[1]**BigInt(k)),le=(a,b)=>a[0]*b[1]<=b[0]*a[1];
 const one=F(1),two=F(2),zero=F(0),stats={parameters:0,arity:0,subset_products:0,ratios:0,cutoffs:0,separation:0};
 const ck=(v,k)=>{if(!v)throw Error(k);stats[k]++};
 function len(p){let l=0;while(p[0]*(1n<<BigInt(l))<p[1])l++;return l}
 function term(beta,R,rho,p,s){let r=mul(rho,sub(one,p)),A=div(add(one,r),sub(one,r));return mul(mul(mul(beta,pow(p,2)),pow(div(R,two),s)),mul(pow(R,len(p)),pow(A,s-1)))}
 const params=[[9,16,6,5],[529,400,1001,1000],[1,1,21,20],[1,8,3,2]];
 for(const [bn,bd,rn,rd] of params){
  const beta=F(bn,bd),R=F(rn,rd),rho=div(sub(two,R),add(two,R));
  ck(le(mul(beta,pow(R,3)),mul(F(4),rho)),"parameters");
  for(let d=1;d<=24;d++)for(let n=1;n<=d;n++){let p=F(n,d),t=term(beta,R,rho,p,2);for(let s=2;s<=24;s++)ck(le(term(beta,R,rho,p,s),t),"arity")}
  for(let d=1;d<=10;d++){
   const ts=Array.from({length:d+1},(_,n)=>n?add(one,term(beta,R,rho,F(n,d),2)):one);
   function walk(rem,count,prod){ck(le(prod,add(one,mul(rho,F(d-rem,d)))),"subset_products");if(count===4)return;for(let n=1;n<=rem;n++)walk(rem-n,count+1,mul(prod,ts[n]))}
   walk(d,0,one);
  }
 }
 const G=(x,y=zero)=>[x,y],ga=(a,b)=>G(add(a[0],b[0]),add(a[1],b[1])),gm=(a,b)=>G(sub(mul(a[0],b[0]),mul(a[1],b[1])),add(mul(a[0],b[1]),mul(a[1],b[0]))),gn=a=>add(pow(a[0],2),pow(a[1],2)),gp=(a,n)=>{let z=G(one);while(n--)z=gm(z,a);return z},gs=(a,b)=>G(sub(a[0],b[0]),sub(a[1],b[1]));
 const shapes=[[[0,1],[0,1]],[[0,1],[1,2],[2,0]],[[0,1,2],[0,1,3],[0,2,3],[1,2,3]],[[0,1],[0,1,2,3],[1,3],[2,3]],[[0,1],[0,2],[0,3],[0,4]]];
 for(const fs of shapes)for(let trial=0;trial<3;trial++){
  const g=1+Math.max(...fs.flat()),m=fs.length,adj=Array.from({length:g},(_,v)=>fs.map((f,i)=>f.includes(v)?i:-1).filter(i=>i>=0)),w=fs.map((_,i)=>1+(i*3+trial*5)%7),D=Math.max(...adj.map(a=>a.reduce((z,i)=>z+w[i],0))),p=w.map(x=>F(x,D)),beta=F(529,400),R=F(1001,1000),rho=div(sub(two,R),add(two,R)),prob=Array.from({length:g},(_,i)=>F(1+(i+trial)%4,4));
  const alpha=fs.map((f,i)=>mul(F(i%2?1:-1,2**f.length),mul(beta,pow(p[i],2))));
  for(const t of [G(R),G(zero,R),G(mul(R,F(3,5)),mul(R,F(4,5)))]){
   const ts=fs.map((f,i)=>gm(G(alpha[i]),gp(t,f.length+len(p[i])))),P=[];
   for(let mask=0;mask<(1<<m);mask++){
    let z=G(zero);for(let S=mask;;S=(S-1)&mask){let v=G(one),groups=new Set();for(let i=0;i<m;i++)if(S>>i&1){v=gm(v,ts[i]);fs[i].forEach(b=>groups.add(b))}for(const b of groups)v=gm(v,G(prob[b]));z=ga(z,v);if(S===0)break}P.push(z)
   }
   for(let U=0;U<(1<<m);U++)for(const A of adj){let V=U,mass=zero;for(const i of A)if(U>>i&1){V&=~(1<<i);mass=add(mass,p[i])}let r=mul(rho,mass);ck(gn(P[V])[0]>0n&&le(gn(gs(P[U],P[V])),mul(pow(r,2),gn(P[V]))),"ratios")}
  }
 }
 function cutoff(R,rho){const C=div(mul(F(10000),rho),mul(sub(one,rho),sub(R,one))),eps=F(1,100);let k=0;while(!le(C,mul(eps,pow(R,k))))k++;ck(le(C,mul(eps,pow(R,k))),"cutoffs");ck(k===0||!le(C,mul(eps,pow(R,k-1))),"cutoffs");return k}
 const old=cutoff(F(9,8),F(7,25)),current=cutoff(F(6,5),F(1,4));
 const b=F(529,400),R=F(1001,1000),rho=div(sub(two,R),add(two,R)),p=F(99,100);
 const oldTerm=mul(mul(mul(b,pow(p,2)),pow(div(R,two),2)),mul(pow(R,len(p)),div(add(one,mul(rho,sub(one,p))),sub(one,rho))));
 ck(!le(oldTerm,rho),"separation");ck(le(add(one,term(b,R,rho,p,2)),add(one,mul(rho,p))),"separation");
 return {stats,old,current,total:Object.values(stats).reduce((a,b)=>a+b,0)}
}
console.log(verify());
```

## 6. Next
Generalize contextual deletion from one already absent parent to all already absent factors, possibly using factor-specific directed deletion radii or exact local remaining-mass budgets to reduce repeated overlap. Study nonuniform certificates and original R812 road realizability / weak-bias parity moment bounds. The full general Port FPTAS and native attribution remain open. Do not repeat the now-classified uniform contextual witness optimization.
