# X6 R284 — exact mixed affine lift reference check

2026-11-28. Independent informed TASK_RESEARCH, author computation, NOT_REVIEWED. Companion to R283@d0fb62e0871f9ca48c692291d0caeca77d3e0055:research_notes/portable_direct/2026-11-28_r2_x6_r283_sixth_prefix_4700_and_mixed_slack.md. Same foundation and native-topic receipt; no new shared authority. This is auxiliary coefficient algebra, not new native BRC arithmetic or an X6 mixed-word classification.

## Algorithm and evidence

Implement R283's lift with exact BigInt rational pairs [c0,c1,d], d>0, representing (c0+c1*delta)/d, ordered lexicographically by cross-products. For row A e+B f+C >= s*delta, s=1 strict or 0 weak, flat rows give weak cuts. Positive/negative rows form the two max hulls; opposite pair cut uses b=A_p B_m-A_m B_p, c=A_p C_m-A_m C_p, t=A_m s_p-A_p s_m, requiring b f+c+t delta >=0. Closed lifted intervals allow singleton bounds. Compare simultaneous hull sweep with both full lifted FM and independent direct-real FM (strict flag propagated by OR for opposite-sign rows; tied bounds strict if any active row is strict). The real projection endpoints recover the standard parts and strictness of finite lifted bounds: lower delta coefficient positive iff open, upper negative iff open. This follows because each original cut has s>=0, each projected strictness weight is nonnegative with positive iff a parent strict, and max/min retains a strict active cut at tied endpoints. Thus the original real projection is reconstructed with endpoints and openness, though its richer lifted representation is retained for updates. No numerical epsilon.

Exhaustive multiset domain: all triples from the 54 rows with A,B,C in {-1,0,1}, s in {0,1}, with repetition, sorted indices. Additional 5000 deterministic pseudo-random cases of 4–12 rows and 21 translated point-tie adversarial systems. All comparison assertions actually executed. The synthetic test is a regression check of the general proof, not an independent review or a frozen X6 endpoint/germ experiment. Pair counts include early rejection, not total runtime costs.

Actual output:
```json
{"cases":32741,"feasible":19551,"infeasible":13190,"singleton":202,"realBoundChecks":17427,"rawPairs":35779,"sweepPairs":25282,"pointTieCases":21}
```

## Exact reproducer (JavaScript, BigInt)

Run the following as the body of a JS function, returning stats.

```javascript

const cmp=(a,b)=>{let c=a[0]*b[2]-b[0]*a[2];if(!c)c=a[1]*b[2]-b[1]*a[2];return c<0n?-1:c>0n?1:0};
const rc=(a,b)=>a[0]*b[1]<b[0]*a[1]?-1:a[0]*b[1]>b[0]*a[1]?1:0;
function hull(rows){
 let L=rows.map(r=>({r,m:-r[1],c:-r[2],t:r[3],d:r[0]<0n?-r[0]:r[0]}));
 const order=(a,b)=>rc([a.m,a.d],[b.m,b.d])||-cmp([a.c,a.t,a.d],[b.c,b.t,b.d]);
 L.sort(order);let H=[];
 for(let l of L){if(H.length&&rc([H[H.length-1].m,H[H.length-1].d],[l.m,l.d])===0)continue;let at=null;
  while(H.length){let a=H[H.length-1];at=[a.c*l.d-l.c*a.d,a.t*l.d-l.t*a.d,l.m*a.d-a.m*l.d];if(at[2]<=0n)throw Error("slope");if(!a.at||cmp(at,a.at)>0)break;H.pop()}
  H.push({...l,at:H.length?at:null})
 }return H
}
function solve(rows,sweep=true){
 let lo=null,hi=null,p=rows.filter(r=>r[0]>0n),m=rows.filter(r=>r[0]<0n),pairs=0;
 function cut(b,c,t){if(!b)return cmp([c,t,1n],[0n,0n,1n])>=0;
 let q=b>0n?[-c,-t,b]:[c,t,-b];if(b>0n){if(!lo||cmp(q,lo)>0)lo=q}else if(!hi||cmp(q,hi)<0)hi=q;return !lo||!hi||cmp(lo,hi)<=0}
 function pair(p,m){pairs++;return cut(p[0]*m[1]-m[0]*p[1],p[0]*m[2]-m[0]*p[2],m[0]*p[3]-p[0]*m[3])}
 for(let r of rows)if(!r[0]&&!cut(r[1],r[2],-r[3]))return {ok:false,pairs};
 if(!sweep){for(let a of p)for(let b of m)if(!pair(a,b))return {ok:false,pairs}}
 else{let P=hull(p),M=hull(m),i=0,j=0;
 while(i<P.length&&j<M.length){if(!pair(P[i].r,M[j].r))return {ok:false,pairs};let a=P[i+1]?.at,b=M[j+1]?.at;if(!a&&!b)break;
 if(!b||a&&cmp(a,b)<0)i++;else if(!a||cmp(a,b)>0)j++;else{i++;j++}}
 if(pairs>Math.max(0,P.length+M.length-1))throw Error("sweep bound");
 }return {ok:true,lo,hi,pairs}
}
// Independent original-real mixed FM, bounds [numerator,denominator,strictFlag].
function real(rows){let lo=null,hi=null;
 function cut(b,c,s){if(!b)return c>0n||c===0n&&!s;let q=b>0n?[-c,b,s]:[c,-b,s];let old=b>0n?lo:hi;let k=old?rc(q,old):0;
 if(!old||(b>0n?k>0:k<0)||(k===0&&s&&!old[2])){if(b>0n)lo=q;else hi=q}
 return !lo||!hi||rc(lo,hi)<0||rc(lo,hi)===0&&!lo[2]&&!hi[2]}
 for(let r of rows)if(!r[0]&&!cut(r[1],r[2],r[3]===1n))return {ok:false};
 for(let p of rows)if(p[0]>0n)for(let m of rows)if(m[0]<0n)if(!cut(p[0]*m[1]-m[0]*p[1],p[0]*m[2]-m[0]*p[2],p[3]===1n||m[3]===1n))return {ok:false};
 return {ok:true,lo,hi}
}
const same=(a,b)=>!a||!b?a===b:cmp(a,b)===0;
let stats={cases:0,feasible:0,infeasible:0,singleton:0,realBoundChecks:0,rawPairs:0,sweepPairs:0,pointTieCases:0};
function verify(rows){let a=solve(rows),b=solve(rows,false),c=real(rows);stats.cases++;stats.rawPairs+=b.pairs;stats.sweepPairs+=a.pairs;
 if(a.ok!==b.ok||a.ok!==c.ok||a.ok&&(!same(a.lo,b.lo)||!same(a.hi,b.hi)))throw Error("comparison mismatch "+JSON.stringify(rows.map(r=>r.map(String))));
 if(a.ok){stats.feasible++;if(a.lo&&a.hi&&cmp(a.lo,a.hi)===0)stats.singleton++;
 for(let key of ["lo","hi"]){let x=a[key],y=c[key];if(!x||!y){if(x!==y)throw Error("unbounded mismatch");continue}
 if(rc([x[0],x[2]],y)!==0||(x[1]!==0n)!==y[2]||(key==="lo"?x[1]<0n:x[1]>0n))throw Error("real endpoint mismatch");
 stats.realBoundChecks++}
 }else stats.infeasible++;
}
let bank=[];for(let a=-1n;a<=1n;a++)for(let b=-1n;b<=1n;b++)for(let c=-1n;c<=1n;c++)for(let s=0n;s<=1n;s++)bank.push([a,b,c,s]);
for(let i=0;i<bank.length;i++)for(let j=i;j<bank.length;j++)for(let k=j;k<bank.length;k++)verify([bank[i],bank[j],bank[k]]);
let state=230283n;function rnd(n){state=(1664525n*state+1013904223n)&0xffffffffn;return state%BigInt(n)}
for(let k=0;k<5000;k++){let n=4+Number(rnd(9)),r=[];for(let j=0;j<n;j++)r.push([rnd(9)-4n,rnd(9)-4n,rnd(13)-6n,rnd(2)]);verify(r)}
for(let t=-10n;t<=10n;t++){let r=[[1n,-1n,t,0n],[1n,1n,-t,0n],[1n,0n,0n,1n],[-1n,0n,0n,0n]];verify(r);if(solve(r).ok)throw Error("point tie failure");stats.pointTieCases++}
return stats;

```

## Next
Strict X6 frontier unchanged from R283: [5200,0], 410800/667787 classified, 2800 necessary-condition survivors. Finish remaining strict prefixes. For mixed X6, generate intercept/germ constraints from R275 and exact mixed elimination before the lifted two-slope solver. The tests above do not assert the mixed X6 classifier is integrated. Independent review and Activity association pending.
