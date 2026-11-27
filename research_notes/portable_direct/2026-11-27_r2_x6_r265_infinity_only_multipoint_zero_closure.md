# X6 R265 — infinity pencil as the only multipoint zero pencil excluded

2026-11-27, independent informed TASK_RESEARCH, author proof and BigInt calculation, NOT_REVIEWED. Same frozen BRC auxiliary weight problem, P000 V5, joint-relation and residual-fidelity constraints as R264. Source control observation r2-20261127-1308-x6-read at ed90fe9e5400d61cd1e2ab0e8b46a52bac13fc66, NO_CANONICAL_PUBLICATION_DIRECTORY. Own researcher identity unconfirmed, no CLAIM or shared Task/Result/Review mutation, Activity association pending.

## Inputs and theorem

R264@3c6fcee204ed134a241ec8de3f2d7ccb571732e0:research_notes/portable_direct/2026-11-27_r2_x6_r264_singleton_pencil_all_zero_words_closure.md; its frozen R247@7e54892a45579bdc497c27e061399339d1fb3512 and R261@b091d79f5b7b493918b181750b2494c3688799a2; R262@cdd1ec936c0b5c10261a9c61e25620c15f43f999 excludes exactly one finite zero on t=0. Inherit necessary-wall and linear-suffix monotone capacity premises; Port 10, 1935 integer directions, 47 labels, 51 endpoint rays, 98 directed germs, 2225 linear partitions. Let Q=a t^2+b B^2+c D^2+d tB+e tD+f BD be full rank, with Q(p24)=c=0. If t=0 has a finite zero, and all finite anchors on the other five multipoint pencils are nonzero, Q cannot be the sole quadratic root of a correct depth-six tree, regardless of all singleton-pencil zeros. No claim here for two or more multipoint pencils with zeros.

Proof: on t=0 a finite zero z requires f!=0 (else the line divides Q); normalize f=1 by scaling and branch exchange, then b=-D_z/B_z. There is at most one finite zero on this pencil. Its entire sign word is determined by the anchor position. Modify R264 to emit exactly one finite zero on group 0, keep the other five multipoint pencils strict, and permit arbitrary singleton zeros. All true Q are represented; apply the open/singleton circuit constraints and monotone capacity cuts of R264. All 12 sectors complete; 59 sector states (47 oriented distinct partial masks) survive, all having z=p18. Eight have no other finite zero and are already excluded by R262. For each of the remaining 39 states, choose its first additional zero p0=(t0,B0,D0), t0!=0, and eliminate a from Q(p0)=0. For any x=(t,B,D),
 
t0^2 Q(x) = d (t0^2 tB-t^2 t0 B0) + e (t0^2 tD-t^2 t0 D0)
            + t0^2 (b B^2+BD) - t^2 (b B0^2+B0D0).
 
The scaled observation is affine in the two free real coefficient parameters d,e. For every finite endpoint impose its exact strict sign, or equality if zero. Q(p24)=0 automatically. The germ at p24 retains its prior assigned branch; for residual recovery we may omit the slope-sector interval and its coupling to this germ, a safe relaxation that does not remove any true Q. The remaining unassigned germs are precisely those starting at the known finite zeros. For p->q from such a zero, the first jet is 2 p^T A q (Q=x^T A x), represented by the scaled row Q(p+q)-Q(p)-Q(q). The second jet when the first is zero equals Q(q). If both p and q are zeros, a zero first jet would make the line through them a factor, incompatible with full rank, so this branch need not be included. Otherwise allow exact first-jet >0, <0, or =0, and in the equality case assign the known sign of Q(q). This preserves all genuine high-order residuals.

For feasibility of each affine constraint family, use exact Fourier–Motzkin elimination: rows A d+B e+C >=0 or >0; for A_p>0>A_m, the combined row is (A_p B_m-A_m B_p)e+(A_p C_m-A_m C_p) >=0 (strict if either parent strict). Keep all A=0 rows. Existence of d given e is exactly the condition that all lower bounds are compatible with all upper bounds, including strict endpoints. Thus feasibility reduces to intersection of rational one-variable half-lines with open/closed endpoints. Equality is two weak inequalities. Search the finite three-way first-jet decisions using this test; at each terminal mask call the inherited suffix capacity test. All 119 complete masks fail capacity, even after dropping the sector constraint. No unknown arithmetic cases or omitted true sign words. This proves the theorem.

Corollary with R264: if a successful common-zero full-rank sole quadratic root exists, at least one finite zero lies on one of the five finite multipoint pencils B=17t, B=0, B=4t, 2B=5t, B=9t. There are 35 such anchors, and at least one further finite zero on a distinct pencil (R262/R263/R264). The remaining common-zero family lies in a union of 3-dimensional coefficient kernels. The case c!=0 and K6 in {1,2} remain open.

## Exact executed evidence

First complete partial run: 30,048,442 suffix checks, 12 sectors, 59 final sector states and 47 unique masks (all z=18). Prefix unique counts [4,80,1319,2966,2985,1288,1483,1640,1818,1116,789,614,337,273,130,81,47].
Second run re-executed same prefix and residual completion; 30,174,079 total suffix checks, 125,637 residual-stage checks; 47 oriented distinct masks, 8 exactly-one-finite-zero masks covered by R262, 39 other partial masks completed; 3390 exact 2-variable feasibility calls, 2124 failed tests, 119 complete masks, all 119 capacity failures, 0 survivors. No CUT. All counters exact; common prefix repeated across the two runs and not counted twice as independent work. A prior runner construction had a JavaScript SyntaxError before execution and was fixed; no scientific output attributed to that attempt.

Per completed state (finite zero IDs / missing germs / complete masks):
18,22,31,41 /20/1
18,22,35,41 /20/1
18,22,41 /18/1
18,22,41 /18/1
18,7,30,32 /17/1
18,7,30 /16/1
18,7,30 /16/3
18,7,32 /16/3
18,7 /15/3
18,7,32 /16/1
18,7 /15/1
18,30,32 /14/1
18,30 /13/3
18,32 /13/5
18,7,32 /16/5
18,31,41 /17/1
18,33,41 /17/1
18,33,41 /17/1
18,41 /15/1
18,41 /15/13
18,41 /15/13
18,31 /14/1
18,7,31 /17/3
18,31 /14/3
18,27,31 /16/1
18,27 /14/1
18,27 /14/3
18,7,27 /17/1
18,27 /14/1
18,7 /15/11
18,27 /14/5
18,7,27 /17/1
18,27 /14/1
18,27 /14/5
18,7,27 /17/5
18,7 /15/9
18,27 /14/5
18,22 /15/1
18,22 /15/1
All final survivor counts zero.

## Reproduction

Extract first JS fenced blocks from pinned R247 as src, R261 as patch, and R264 as runner. Execute following wrapper exactly. Its partial-stage output is reproduced before residual completion; all affine coefficients, rational comparisons and bit masks use BigInt.

```javascript
runner=runner.replace('let result=new Function(src)();','return new Function(src)();');
runner=runner.replace('if(k>=6)emit([0]);if(!s){emit(Array(n).fill(1));','if(k>=6)emit([0]);if(k===0){if(s)for(let j=0;j<n;j++)emit(ids.map((_,i)=>i===j?0:i<j?-s:s));return out}if(!s){emit(Array(n).fill(1));');
const residual=`
const partialChecks=checks, distinct=[...new Map(final.map(h=>[h.a+","+h.b+","+h.zs.join(),h])).values()];
let lpCalls=0,lpReject=0,capReject=0,fullVisits=0,single=0,finalFull=[],byAnchor={},status=[];
function feasible(H){
 lpCalls++;let plus=[],minus=[],flat=[];
 for(let h of H){if(h[0]>0n)plus.push(h);else if(h[0]<0n)minus.push(h);else flat.push([h[1],h[2],h[3]])}
 let lo=null,hi=null,ls=false,hs=false;
 function add1(b,c,strict){
  if(!b)return c>0n||!strict&&c===0n;
  let q=b>0n?[-c,b]:[c,-b];
  if(b>0n){let z=lo?cmp(q,lo):1;if(z>0){lo=q;ls=strict}else if(!z)ls=ls||strict}
  else{let z=hi?cmp(q,hi):-1;if(z<0){hi=q;hs=strict}else if(!z)hs=hs||strict}
  if(!lo||!hi)return true;let z=cmp(lo,hi);return z<0||!z&&!ls&&!hs;
 }
 for(let [b,c,t] of flat)if(!add1(b,c,t))return false;
 for(let p of plus)for(let m of minus){
  if(!add1(p[0]*m[1]-m[0]*p[1],p[0]*m[2]-m[0]*p[2],p[3]||m[3]))return false;
 }
 return true;
}
const negrow=h=>h.map(x=>-x), eqrows=h=>[[...h,false],[...negrow(h),false]], add3=(x,y)=>x.map((v,i)=>v+y[i]);
for(let st of distinct){
 let a=BigInt("0x"+st.a),b=BigInt("0x"+st.b),zs=st.zs, z=zs[0];
 let rec=byAnchor[z]??={partial:0,single:0,lpInfeasible:0,completed:0,full:0,survive:0};rec.partial++;
 if(zs.length===1){single++;rec.single++;continue}
 if(st.f!=="1")throw Error("normalization");
 let [t0,B0,D0]=P[zs[1]],bb=-P[z][2]/P[z][1],scale0=t0*t0;
 if(!t0||P[z][1]!==1n)throw Error("anchor geometry");
 function row([t,B,D]){return [scale0*t*B-t*t*t0*B0,scale0*t*D-t*t*t0*D0,scale0*(bb*B*B+B*D)-t*t*(bb*B0*B0+B0*D0)]}
 let rows=P.map(row),signs=P.map((_,i)=>i===24||zs.includes(i)?0:a&E[i]?1:b&E[i]?-1:99),H=[];
 if(signs.includes(99))throw Error("missing anchor");
 for(let i=0;i<P.length;i++){let h=rows[i],v=signs[i];if(v)H.push([...(v>0?h:negrow(h)),true]);else H.push(...eqrows(h))}
 if(!feasible(H)){lpReject++;rec.lpInfeasible++;continue}
 let missing=G.filter(g=>!(g[2]&(a|b))).map(([p,q,bit])=>({p,q,bit,h:sub(sub(row(add3(P[p],P[q])),rows[p]),rows[q]),s:signs[q]}));
 if(missing.some(g=>!zs.includes(g.p)))throw Error("missing germ not zero");
 let visitsBefore=fullVisits, survivorsBefore=finalFull.length;
 function dfs(j,x,y,H){
  if(j===missing.length){fullVisits++;if(!can(x,5)||!can(y,5)){capReject++;return}finalFull.push({z,zs,a:x.toString(16),b:y.toString(16)});return}
  let {h,s,bit}=missing[j];
  for(let sg0 of [-1,1]){
   let next=H.concat([[...(sg0>0?h:negrow(h)),true]]);
   if(!feasible(next)){lpReject++;continue}
   dfs(j+1,sg0>0?x|bit:x,sg0<0?y|bit:y,next)
  }
  if(s){let next=H.concat(eqrows(h));if(feasible(next))dfs(j+1,s>0?x|bit:x,s<0?y|bit:y,next);else lpReject++}
 }
 dfs(0,a,b,H);rec.completed++;rec.full+=fullVisits-visitsBefore;rec.survive+=finalFull.length-survivorsBefore;
 status.push({zs,missing:missing.length,full:fullVisits-visitsBefore,survive:finalFull.length-survivorsBefore});
}
`;
const old="return {groups,checks,completed,unique:unique.map(s=>s.size),totals,final};";
const rep=residual+"return {groups,checks,partialChecks,completed,unique:unique.map(s=>s.size),totals,partial:final.length,distinct:distinct.length,lpCalls,lpReject,capReject,fullVisits,single,byAnchor,status,finalFull};";
runner=runner.replace("src=src.replace(",`patch=patch.replace(${JSON.stringify(old)},${JSON.stringify(rep)});\nsrc=src.replace(`);
const result=new Function("src","patch",runner)(src,patch);
```

## Continuation

Generalize the residual LP kernel to any three noncollinear zero anchors: choose a nonzero polar coordinate for normalization, solve the three anchor equations, and represent the other two affine parameters by integer rows. Preserve equality endpoints and exact first/second jets. Test the remaining five single-multipoint families with arbitrary singleton zeros; then combinations of multipoint zero pencils. Do not redo the closed singleton-only or infinity-only-multipoint families. Alternatively generalize partial-word search by selecting any first finite multipoint zero and then permitting more zeros, retaining exact circuits and shared slope intervals. Independent review pending.
