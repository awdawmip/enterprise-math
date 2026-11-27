# X6 R286 — reusable signed circuit dictionary and factorized mixed slack

2026-11-28. Independent informed TASK_RESEARCH, author proof and computation, NOT_REVIEWED. Native read r2-20261128-0405-x6-read SUCCEEDED at 2026-11-27T20:05:49.810241Z, Source ba14c781840cd555f6f3011948df0beb4d02f41f, NO_CANONICAL_PUBLICATION_DIRECTORY; owner projection and own researcher binding unconfirmed. No CLAIM or shared control mutation; Activity association pending. Global entries verified immutable main@4d6afb4a5ffc6adc20d31ee6898f6707b1e4ac2f. P000 V5, global V4 matching canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview, joint/residual fidelity retained. Auxiliary coefficient algebra of frozen BRC observer, not native arithmetic.

## Exact scope and previous frontier
R285@7403583b0ed8aeffeb5d70744b93660c12c7cc9d:research_notes/portable_direct/2026-11-28_r2_x6_r285_mixed_intercept_positive_circuits.md; R284@b1dcb5bc4869113730d936e03be15ebc926a2ba1f (mixed solver). Frozen R247 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md; reuse its data literal, two support splits, primitive ray normalization, 51 endpoints and 98 directed germs. R285 strict-sixth frontier [5350,0], 422650/667787 checked, 2954 necessary-condition survivors; unchanged this round. R285 capacity prerequisites and R283 frozen pins retained. K6 remains 1–2.

## Theorem: sign-independent circuit compilation and factorized slack
For fixed rational intercept normals u_i in R^3 write each nonzero u_i=k_i v_g, where v_g are distinct primitive projective normals (one representative per unoriented ray). A mixed row u_i*x+b_i(y) >=_i 0 may be sign-switched and labeled strict or weak (equalities use two weak rows). After any switch divide by |k_i|; retain oriented direction epsilon_i v_g, normalized slack b_i(y)/|k_i|, strict flag and original row identity.

Compile the unsigned minimal linear dependence supports of distinct v_g once. In dimension three these have size 3 or 4: distinct projective normals are pairwise independent; a triple is a circuit iff determinant zero; a quadruple iff all four 3-minors are nonzero. Obtain its unique primitive signed coefficient vector w by 2x2 minors on a nonzero coordinate projection for triples and alternating 3x3 minors for quadruples. Each circuit has two compatible positive orientations, epsilon_g=sign(w_g) or its simultaneous negative, with coefficients |w_g|. Other minimal positive circuits are singleton zero normals and opposite-oriented pairs from the same projective class (normalized weights 1,1). Indeed a minimal positive relation of size >2 cannot contain parallel rows: opposite ones already give a positive pair; same-oriented ones can be merged into one positive coefficient, contradicting minimal support. On distinct classes a support-minimal positive relation has one-dimensional restricted kernel (R285), hence is a compiled circuit. Conversely each active oriented circuit is minimal.

For fixed y define m_(g,epsilon)(y) as the minimum normalized slack among rows of that oriented normal; mark it strict iff at least one minimizing row is strict. Empty groups inactive. For each active circuit test sum |w_g| m_(g,epsilon)(y) >=0, strict iff any selected minimum is strict. Opposite pairs use weights 1. Zero normals tested individually. This factorization is equivalent to all R285 circuit inequalities including boundaries: the Cartesian product of row choices has minimum weighted sum equal to sum of minima by positivity. If positive, all choices pass; if negative, a minimizing tuple fails; if zero, a tuple fails iff some minimizing row can be chosen strict. Non-minimizing choices have strictly positive total slack. Thus by R285 the check is necessary and sufficient for existence of intercept coefficients at the specified y. For arbitrary y this is an identity of functions; a global linear-region solver still needs piecewise minima or expanded rows. Original rows with identities, scales and flags retained for future intercept-dependent constraints and provenance. No native observation coordinates removed. Dictionary construction O(G^4) fixed-dimensional determinant tests; point evaluation O(N + number of active group subsets up to four), or O(N + total circuit count) when scanning compiled circuit list, constant-size rational arithmetic (bit costs separate). No global runtime claim.

## Actual frozen-row experiment
All 51 endpoint and 98 directed derivative coefficient rows generated as in R285, without same-pencil zero simplification, so this is a universal raw-row dictionary. Counts are projective unsigned circuits; each has two sign orientations. Raw choices are Cartesian products of group sizes, not actual feasible X6 masks. Exact BigInt arithmetic.
```json
{"endpoints":51,"germs":98,"rawRows":149,"zeroNormals":3,"projectiveNormals":44,"parallelDistinctRowPairs":406,"triples":242,"quadruples":126612,"rawTripleChoices":"14968","rawQuadrupleChoices":"12664241","groupSizes":[16,12,11,8,8,8,7,5,4,4,4,4,4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1],"stats":{"arbitrary":160,"realizableSubsets":40,"probes":600,"feasible":211,"infeasible":389,"fullWitnessWords":8,"fullRows":532,"zeroEndpointWords":8}}
```
Fixed integer slope comparisons against independently implemented original-real mixed Fourier–Motzkin elimination of three intercept variables: 160 arbitrary sampled row systems and 40 sampled subsets of true endpoint/germ words from Q=D(D-alpha*t-beta*B). Eight full true words checked at their known witness slopes using dictionary only. No full-region FM equivalence experiment, BRC capacity classification, or strict-prefix progress. The earlier larger verification attempt timed out without publication; no counts from it credited.

## Reproducer
Parse the JSON array in the frozen R247 text between 'const data=' and '; experiment(data)'; run experiment(data).
```javascript
function experiment(data){
 const abs=x=>x<0n?-x:x,gcd=(a,b)=>b?gcd(b,a%b):abs(a),sign=x=>x>0n?1:x<0n?-1:0,dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],det=(a,b,c)=>dot(cross(a,b),c),prim=a=>{let d=a.reduce(gcd,0n);return d?a.map(x=>x/d):a};
 let P=[],ids=new Map(),G=[];function id(p){p=prim(p);let k=p.join();if(!ids.has(k)){ids.set(k,P.length);P.push(p)}return ids.get(k)}
 for(let o of data){let parts=o.normal.join()==="51,2,-1"?[[["1","9","69"],["3","17","187"]],[["2","5","112"],["1","0","51"]]]:o.normal.join()==="17,-1,0"?[[["0","0","1"],["1","17","391"]],[["1","17","69"],["1","17","22"]]]:[o.endpoints];for(let [a,b] of parts){a=a.map(BigInt);b=b.map(BigInt);if(dot(a,o.normal.map(BigInt))||dot(b,o.normal.map(BigInt)))throw Error("incidence");let i=id(a),j=id(b);G.push([i,j],[j,i])}}
 if(P.length!==51||G.length!==98)throw Error("shape");
 const ep=([t,B,D])=>[t*t,t*B,B*B,t*D,B*D,D*D],pol=([t,B,D],[T,U,V])=>[2n*t*T,t*U+B*T,2n*B*U,t*V+D*T,B*V+D*U,2n*D*V];
 const rows=P.map(ep).concat(G.map(([i,j])=>pol(P[i],P[j])));
 const V=[],sizes=[],index=new Map(),meta=rows.map(r=>{let u=r.slice(0,3),d=u.reduce(gcd,0n);if(!d)return [-1,0,0n];let s=sign(u.find(Boolean)),v=u.map(x=>x/(BigInt(s)*d)),k=v.join();if(!index.has(k)){index.set(k,V.length);V.push(v);sizes.push(0)}let i=index.get(k);sizes[i]++;return [i,s,d]});
 const dict=new Map(),count=[0,0,0,0,0],weighted=[0n,0n,0n,0n,0n];
 function circuit(I){let a=I.map(i=>V[i]);if(a.length===3){if(det(...a))return null;let c=cross(a[0],a[1]),z=c.findIndex(Boolean);return prim([cross(a[1],a[2])[z],cross(a[2],a[0])[z],c[z]])}let [p,q,r,s]=a;let w=[det(q,r,s),-det(p,r,s),det(p,q,s),-det(p,q,r)];return w.every(Boolean)?prim(w):null}
 function subsets(I,f){for(let i=0;i<I.length;i++)for(let j=i+1;j<I.length;j++)for(let k=j+1;k<I.length;k++){if(f([I[i],I[j],I[k]])===false)return false;for(let l=k+1;l<I.length;l++)if(f([I[i],I[j],I[k],I[l]])===false)return false}return true}
 subsets(V.map((_,i)=>i),I=>{let w=circuit(I);if(!w)return;if(w.some(x=>!x)||[0,1,2].some(j=>I.reduce((s,i,k)=>s+w[k]*V[i][j],0n)!==0n))throw Error("dependency");dict.set(I.join(),w);count[I.length]++;weighted[I.length]+=I.reduce((s,i)=>s*BigInt(sizes[i]),1n)});
 function factor(R,e,f){let A=V.map(()=>[null,null]);for(let [id,s,strict] of R){let [g,o,d]=meta[id],r=rows[id],c=BigInt(s)*(r[3]*e+r[4]*f+r[5]);if(g<0){if(c<0n||c===0n&&strict)return false;continue}let j=s*o>0?0:1,b=A[g][j];if(!b||c*b[1]<b[0]*d||c*b[1]===b[0]*d&&strict&&!b[2])A[g][j]=[c,d,strict]}
  function check(a,w){let x=0n,y=1n,s=false;for(let i=0;i<a.length;i++){let [c,d,t]=a[i];x=x*d+y*c*abs(w[i]);y*=d;s=s||t}return x>0n||x===0n&&!s}
  let I=[];for(let i=0;i<A.length;i++){let a=A[i];if(a[0]||a[1])I.push(i);if(a[0]&&a[1]&&!check(a,[1n,1n]))return false}
  return subsets(I,J=>{let w=dict.get(J.join());if(!w)return true;for(let o of [1,-1]){let a=J.map((i,k)=>A[i][sign(w[k])*o>0?0:1]);if(a.every(Boolean)&&!check(a,w))return false}return true})
 }
 function fm(R,e,f){let L=R.map(([i,s,t])=>{let a=rows[i].map(x=>x*BigInt(s));return [...a.slice(0,3),a[3]*e+a[4]*f+a[5],t]});
 function reduce(L){let M=new Map();for(let a of L){let t=a.at(-1);a=a.slice(0,-1);let d=a.reduce(gcd,0n);if(d)a=a.map(x=>x/d);if(a.slice(0,-1).every(x=>!x)){if(a.at(-1)<0n||a.at(-1)===0n&&t)return null;continue}let k=a.join();M.set(k,[...a,t||M.get(k)?.at(-1)||false])}return [...M.values()]}
 L=reduce(L);if(!L)return false;for(let d=3;d;d--){let P=L.filter(a=>a[0]>0n),M=L.filter(a=>a[0]<0n),Z=L.filter(a=>!a[0]).map(a=>a.slice(1));for(let p of P)for(let m of M){let a=[];for(let j=1;j<=d;j++)a.push(p[0]*m[j]-m[0]*p[j]);Z.push([...a,p.at(-1)||m.at(-1)])}L=reduce(Z);if(!L)return false}return true}
 let state=28620261128n;function rnd(n){state=(1664525n*state+1013904223n)&0xffffffffn;return Number((state>>8n)%BigInt(n))}
 let st={arbitrary:0,realizableSubsets:0,probes:0,feasible:0,infeasible:0,fullWitnessWords:0,fullRows:0,zeroEndpointWords:0};
 function verify(R,e,f){let a=factor(R,e,f),b=fm(R,e,f);if(a!==b)throw Error("FM mismatch");st.probes++;st[a?"feasible":"infeasible"]++}
 function randomProbe(R){verify(R,BigInt(rnd(41)-20),BigInt(rnd(41)-20))}
 for(let k=0;k<160;k++){let R=[];for(let j=0,m=5+rnd(6);j<m;j++){let i=rnd(rows.length),s=rnd(3)-1;if(!s)R.push([i,1,false],[i,-1,false]);else R.push([i,s,!!rnd(2)])}for(let j=0;j<3;j++)randomProbe(R);st.arbitrary++}
 for(let k=0;k<40;k++){let e=BigInt(-rnd(90)),f=BigInt(-rnd(30)),q=[0n,0n,0n,e,f,1n],S=P.map(p=>sign(dot(ep(p),q))),R=[];
 for(let i=0;i<P.length;i++){if(S[i])R.push([i,S[i],true]);else R.push([i,1,false],[i,-1,false])}
 for(let i=0;i<G.length;i++){let [a,b]=G[i];if(S[a])continue;let h=sign(dot(rows[51+i],q)),s=h||S[b];if(s)R.push([51+i,s,S[b]!==s]);else R.push([51+i,1,false],[51+i,-1,false])}
 if(k<8){if(!factor(R,e,f))throw Error("full witness");st.fullWitnessWords++;st.fullRows+=R.length;if(S.includes(0))st.zeroEndpointWords++}
 let T=Array.from({length:8+rnd(3)},()=>R[rnd(R.length)]);verify(T,e,f);randomProbe(T);randomProbe(T);st.realizableSubsets++}
 return {endpoints:P.length,germs:G.length,rawRows:rows.length,zeroNormals:meta.filter(m=>m[0]<0).length,projectiveNormals:V.length,parallelDistinctRowPairs:sizes.reduce((s,n)=>s+n*(n-1)/2,0),triples:count[3],quadruples:count[4],rawTripleChoices:String(weighted[3]),rawQuadrupleChoices:String(weighted[4]),groupSizes:sizes.slice().sort((a,b)=>b-a),stats:st}
}
```

## Next
Use dictionary for actual mixed words, taking advantage of same-pencil zero simplification where appropriate; compare full projected regions with R284 before claiming global classifier integration. Strict sixth resumes at [5350,0] using R282/R285, then remaining singleton directions. Independent review and Activity association pending.
