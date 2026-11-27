# X6 R260 — four-pencil intercept coupling and the null common-point chart

2026-11-27, independent informed TASK_RESEARCH, author proof and exact calculation, NOT_REVIEWED. P000 V5, ACTIVE worldview and joint relation preservation retained. All coordinates are auxiliary BRC weight coordinates, not native spatial axes. Native read r2-20261127-0905-x6-read SUCCEEDED, Source ab7a6bdace3f6216a6464122924a4414cc2842f9, observed 2026-11-27T01:05:33.298753Z, NO_CANONICAL_PUBLICATION_DIRECTORY (directory observation only; owner and own research identity not established). No CLAIM, Result, Review or shared task mutation. Activity association pending.

## Frozen inputs and objective
R259@24984832757373bd2c06c71496ce05f6c5ae4e89:research_notes/portable_direct/2026-11-27_r2_x6_r259_root_three_pencil_interval_coupling.md left the common zero c=0 unaddressed, and proposed intercept coupling. R258@b0960b0e767177f2b6bb7437275bf19aa662f7f0 closed internal positions at author level (not recomputed here). Frozen R247@7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md supplies exact 51 endpoints, 98 directed germs, 47 labels, 2225 linear masks, and G. Port 10, weights (17t,B,22t,D), 1935 directions, six-pair joint BRC, strict 3/2. Capacity exclusions inherit necessary-wall and linear suffix completeness. This unit addresses partial root masks, not global root closure.

## Four-pencil exact joint feasibility theorem (general c)
Q=a t^2+b B^2+c D^2+d tB+e tD+f BD. On t=0 write y=D/B, q_inf(y)=c y^2+f y+b. On B=kt write y=D/t, q_k(y)=c y^2+(e+k f)y+(a+k d+k^2 b). Fix c (normalize to 1 for c!=0 after branch exchange, or 0 for common zero), and fix slopes e,f. For each line, with strict finite point signs relative to actual chosen branch orientation, define J_k=(l_k,u_k), l_k=max over positives of -c y^2-L_k y, u_k=min over negatives of -c y^2-L_k y, allowing infinite bounds. Here L_inf=f, L_k=e+k f. For any h>k>0,
K_k=(1-k/h) K_0+(k/h)K_h+k(k-h)K_inf.
This follows by substituting K_inf=b, K_0=a, K_h=a+h d+h^2 b. The first three intercepts are independent since h!=0. For fixed slopes, the simultaneous strict sign words on four lines t=0,B=0,B=ht,B=kt are realizable iff each J is nonempty and
J_k intersects (1-k/h)J_0+(k/h)J_h+k(k-h)J_inf.
Proof: image of independent open intervals under this linear map is exactly the open interval with endpoints obtained by taking lower bounds for positive coefficients and upper bounds for negative coefficients, and vice versa; every interior value has a preimage by convexity and the endpoint infimum/supremum. Select compatible intercepts and recover a,b,d from K_0,K_inf,K_h. Thus cross conditions are l_k<combined upper, combined lower<u_k. Replacing maxima/minima by their constituent affine inequalities yields a finite strict linear feasibility test in the two slopes e,f; no relaxation of the four finite strict words. For general c!=0 this theorem is proved, not yet computed. It supplements R259's slope-only condition. Example in abstract auxiliary data: y=0 on infinity,0,1,2 with b<0, K0>0,K2>0,K1<0. All separate slope constraints vacuous, yet K1=(K0+K2)/2-b>0, impossible. For exact zero constraints, replace a point's strict inequality by equality K=-c y^2-L y, so J may be singleton or open interval or empty; interval image/intersection with correct endpoint inclusion remains exact for point signs. Directed germs at zero endpoints must still be evaluated by full lexicographic jets, not by their zero point values.

## c=0 chart and full-rank restrictions
The common endpoint p24=(0,0,1) has Q=0 exactly when c=0. Full rank implies (e,f)!=(0,0) (otherwise A has zero third row). On each pencil line finite values are affine in y, so sign sequence is monotone according to slope sign, at most one zero for nonzero slope. Zero slope gives nonzero constant for full rank: a zero constant would make Q vanish identically along a projective line and factor. At p24 there is exactly one germ in frozen bank, pointing to p1=(1,17,391). Along this germ first coefficient is e+17f; if zero, second coefficient is K17. Consequently its sign is assigned exactly even though p24 is a zero endpoint. Other finite zero endpoints are left unassigned in the weak-mask experiment (their full jets remain outstanding); all nonzero finite endpoints assign every outgoing germ by continuity. Partial masks are subsets of full masks, so can(S,5) monotonicity justifies exclusions. The weak experiment covers all full-rank c=0 forms on three lines, including finite zeros. No claim that surviving masks are necessarily full rank or realizable globally.

### Exact three-pencil weak experiment
Ordered finite endpoints:
t=0: 18,2,0,36; B=17t: 26,19,34,20,25,28,39,1,37; B=0: 10,15,11,45,49,9,38,42,40,44,47,50.
There are six projective slope sign sectors (three event rays and three intervals, modulo sign); integer reps e,f in [-18,18] cover all (boundaries e=0,e=-17f,f=0). Final stage per sector: [s_inf,s17,s0; input from first two lines, patterns on last line, direct fail, recursive fail, surviving].
[1,-1,-1;171,25,188,492,3595]
[1,1,-1;171,25,192,316,3767]
[1,0,-1;18,25,40,88,322]
[1,1,0;171,2,60,24,258]
[0,1,1;38,25,74,180,696]
[1,1,1;171,25,196,368,3711]
625499 exact capacity checks; 10119 distinct surviving partial masks up to branch exchange, of which 1278 have all selected finite endpoints nonzero. No cutoff. Sector counts can duplicate masks across sectors. This is a necessary filter, not a global c=0 exclusion.

### Exact four-pencil strict finite experiment (p24 still zero)
Add B=4t, finite ordered endpoints 48,21,29,23,46. 30 finite endpoints plus p24. Set h=17,k=4, hence K4=(13/17)K0+(4/17)K17-52 Kinf. Since c=0, in each fixed slope sign sector, the finite endpoint giving each bound is selected just by its y order. Thus cross conditions are at most two strict homogeneous linear inequalities in e,f. Normalize f=1 if nonzero (overall branch exchange makes f>0), or e=1 if f=0. Slope sign events e/f=-17,-4,0 and f=0 partition all possibilities; exact rational interval intersection determines feasibility, including event equalities. The selected finite point signs and p24 germ are fully coupled; zero finite points are excluded from this strict experiment, not from the previous weak experiment.

Final stage per sector: [s_inf,s17,s0,s4; input, patterns, direct, recursive, algebra, remaining]
[1,-1,-1,-1;500,6,629,706,839,826]
[1,0,-1,-1;86,6,94,124,129,169]
[1,1,-1,-1;517,6,687,591,698,1126]
[1,1,-1,0;517,2,300,175,170,389]
[1,1,-1,1;517,6,737,697,949,719]
[1,1,0,1;71,6,89,104,96,137]
[1,1,1,1;513,6,661,593,832,992]
[0,1,1,1;181,6,240,257,241,348]
6245994 capacity checks; final 15344 sector-word visits, 3437 direct fail, 3247 recursive fail, 3954 intercept infeasible, 4706 sector-word survivors, 2789 distinct surviving masks up to branch exchange. No cutoff. Counts refer to sector-word combinations, not disjoint coefficient cells or globally realizable forms. The two experiments share prefix work; check counts reported separately, not a novel-work sum.

Concrete rejected frozen partial word (first algorithm example): slopes (+,-,-,-); t=0 all positive; B=17t and B=0 all negative; B=4t positive at 48,21,29,23 and negative at 46. In particular p18 gives b>0, p10 gives a<0, p26 at y=9 and slope L17<0 gives K17<-9 L17. Then K4< -(36/17)L17 (since a<0,b>0). But p48 at y=109/2 gives K4>-(109/2)L4; write e/f=s<-17 and f>0. Necessary inequality would require -(109/2)(s+4)<-(36/17)(s+17), which fails for every s<-17 (left positive, right positive but strictly smaller). This proves that the displayed word is impossible despite passing separate line and capacity tests. No numerical tolerances.

## Reproduction
Read the first JavaScript block of the pinned R247 note as src. Replace the exact line 'return {points:P.length,germs:G.length,linearPartitions:Q.length,result:rank4("two_anchor_kernel",[])};' inside experiment with either patch below and replace final experiment(data) with return experiment(data); execute Function(src)(). Both patches actually executed on the frozen source, with outputs as reported. The existing linear bank and capacity recursion are reused, not reconstructed from summaries.

### Weak three-pencil patch
```javascript

ceiling=15000000;
let E=P.map((p,i)=>G.filter(g=>g[0]===i).reduce((a,g)=>a|g[2],0n));
let groups=[[1n,0n,0n],[17n,-1n,0n],[0n,1n,0n]].map(h=>P.map((p,i)=>i).filter(i=>i!==24&&!dot(h,P[i])).sort((i,j)=>sg(P[i][2]*(P[j][0]+P[j][1])-P[j][2]*(P[i][0]+P[i][1]))));
let signs=new Map();for(let e=-18;e<=18;e++)for(let f=-18;f<=18;f++){if(!e&&!f)continue;let s=[Math.sign(f),Math.sign(e+17*f),Math.sign(e)];signs.set(s.join(),s)}
function patterns(ids,s,k){let out=[],n=ids.length;
function emit(v){let a=0n,b=0n;for(let i=0;i<n;i++){if(v[i]>0)a|=E[ids[i]];if(v[i]<0)b|=E[ids[i]]}
if(k===1){let h=s||v[0];if(h>0)a|=E[24];else b|=E[24]}
out.push([a,b]);}
if(!s){emit(Array(n).fill(1));emit(Array(n).fill(-1));}
else {for(let j=0;j<=n;j++)emit(ids.map((_,i)=>i<j?-s:s));for(let j=0;j<n;j++)emit(ids.map((_,i)=>i<j?-s:i===j?0:s));}
return out}
let hist=[],surv=new Map();
for(let s of signs.values()){
 if(s.find(Boolean)<0)continue;
 let states=[[0n,0n]],stages=[];
 for(let k=0;k<3;k++){let pats=patterns(groups[k],s[k],k),out=[],direct=0,recursive=0;
 for(let [a,b] of states)for(let [p,q] of pats){let A=a|p,B=b|q;if(count(A)>31||count(B)>31){direct++;continue}if(!can(A,5)||!can(B,5)){recursive++;continue}out.push([A,B])}
 stages.push({input:states.length,patterns:pats.length,direct,recursive,surv:out.length});states=out;}
 for(let [a,b] of states){let [p,q]=canon(a,b);surv.set(p+","+q,[p,q])}
 hist.push({s,stages});
}
return {groups,hist,checks,unique:surv.size,zeroFree: [...surv.values()].filter(([a,b])=>((a|b)&groups.flat().reduce((s,i)=>s|E[i],0n))===groups.flat().reduce((s,i)=>s|E[i],0n)).length};

```
### Strict four-pencil patch
```javascript

ceiling=15000000;
let E=P.map((p,i)=>G.filter(g=>g[0]===i).reduce((a,g)=>a|g[2],0n));
let groups=[[1n,0n,0n],[17n,-1n,0n],[0n,1n,0n],[4n,-1n,0n]].map(h=>P.map((p,i)=>i).filter(i=>i!==24&&!dot(h,P[i])).sort((i,j)=>sg(P[i][2]*(P[j][0]+P[j][1])-P[j][2]*(P[i][0]+P[i][1]))));
const K=[null,17n,0n,4n];
const reps=[[-18n,1n],[-17n,1n],[-10n,1n],[-4n,1n],[-2n,1n],[0n,1n],[1n,1n],[1n,0n]];
function patterns(ids,s,k){let out=[],n=ids.length;
function emit(v){let a=0n,b=0n;for(let i=0;i<n;i++){if(v[i]>0)a|=E[ids[i]];if(v[i]<0)b|=E[ids[i]]}
if(k===1){let h=s||v[0];if(h>0)a|=E[24];else b|=E[24]}
out.push([a,b]);}
if(!s){emit(Array(n).fill(1));emit(Array(n).fill(-1));}
else for(let j=0;j<=n;j++)emit(ids.map((_,i)=>i<j?-s:s));
return out}
const cmp=(a,b)=>sg(a[0]*b[1]-b[0]*a[1]);
const plus=(a,b)=>[a[0]*b[2]+b[0]*a[2],a[1]*b[2]+b[1]*a[2],a[2]*b[2]];
const times=(a,n,d=1n)=>[a[0]*n,a[1]*n,a[2]*d];
function bounds(a,b,k,s){
 let ids=groups[k],pos=ids.filter(i=>a&E[i]),neg=ids.filter(i=>b&E[i]);
 let l=pos.length?pos[s<0?pos.length-1:0]:null,u=neg.length?neg[s<0?0:neg.length-1]:null;
 function row(i){if(i===null)return null;let [t,B,D]=P[i];return k===0?[0n,-D,B]:[-D,-K[k]*D,t]}
 return [row(l),row(u)]
}
function algebra(a,b,s,e,f){
 let [I,H,Z,J]=groups.map((_,k)=>bounds(a,b,k,s[k]));
 function sum(x,y,z){return x&&y&&z?plus(plus(times(x,-52n),times(y,4n,17n)),times(z,13n,17n)):null}
 let l=sum(I[1],H[0],Z[0]),u=sum(I[0],H[1],Z[1]),ineq=[];
 if(l&&J[1])ineq.push(plus(J[1],times(l,-1n)));
 if(u&&J[0])ineq.push(plus(u,times(J[0],-1n)));
 if(!f)return ineq.every(v=>v[0]>0n);
 let lo=null,hi=null,eq=null;
 for(let k=1;k<4;k++){let v=-K[k];if(s[k]===0)eq=[v,1n];else if(s[k]>0){if(!lo||cmp(lo,[v,1n])<0)lo=[v,1n]}else if(!hi||cmp(hi,[v,1n])>0)hi=[v,1n]}
 for(let [x,y] of ineq){if(!x){if(y<=0n)return false;continue}let r=x>0n?[-y,x]:[y,-x];if(x>0n){if(!lo||cmp(lo,r)<0)lo=r}else if(!hi||cmp(hi,r)>0)hi=r}
 return eq?(!lo||cmp(eq,lo)>0)&&(!hi||cmp(eq,hi)<0):!lo||!hi||cmp(lo,hi)<0;
}
let hist=[],surv=new Map(),badExample=null;
for(let [e,f] of reps){let s=K.map(k=>sg(k===null?f:e+k*f)),states=[[0n,0n]],stages=[];
 for(let k=0;k<4;k++){let pats=patterns(groups[k],s[k],k),out=[],direct=0,recursive=0,alg=0;
 for(let [a,b] of states)for(let [p,q] of pats){let A=a|p,B=b|q;if(count(A)>31||count(B)>31){direct++;continue}if(!can(A,5)||!can(B,5)){recursive++;continue}if(k===3&&!algebra(A,B,s,e,f)){alg++;if(!badExample)badExample={s,positive:groups.map(g=>g.filter(i=>E[i]&A)),negative:groups.map(g=>g.filter(i=>E[i]&B))};continue}out.push([A,B])}
 stages.push({input:states.length,patterns:pats.length,direct,recursive,alg,surv:out.length});states=out;}
 for(let [a,b] of states){let [p,q]=canon(a,b);surv.set(p+","+q,[p,q])}
 hist.push({s,stages});
}
return {groups,hist,checks,unique:surv.size,badExample};

```

## Remaining and next
General c!=0 four-pencil theorem ready for actual application to R259 survivors (linear 2-variable feasibility after eliminating intercepts). In c=0 extend strict four-pencil survivors to more directions B=kt, maintaining the one shared quadratic intercept polynomial and affine slope. Handle finite zero point strata with exact equalities and full jets. K6 remains 1–2; root full-rank indefinite remains open. No independent review or Activity association yet.
