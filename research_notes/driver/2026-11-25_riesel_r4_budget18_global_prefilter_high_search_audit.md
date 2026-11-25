# Riesel R4 budget 18: global prefilter and high-period search scoped Driver audit

2026-11-25. Existing Driver lane EM-DVR-DEBB5E (MCP-9b4714dc46b948afa4875a86c89c713c); nonauthor review of the supplied author-side archive, not a clean-blind experiment, Native Review, Result admission, or Task closure. Preserve the original author EM-DIRECT-970E1C / RA-D2EC212845B63844081F9A14. This continues the previous [private-digit and all-shared audit](https://github.com/awdawmip/enterprise-math/blob/e945e2a81222c2cf259d26a5cf3e7fbed8a3ac7e/research_notes/driver/2026-11-25_riesel_r4_budget18_private_digit_shared_capacity_audit.md). Author [budget-18 report](https://github.com/awdawmip/enterprise-math/blob/f869b78cc5143b7f73e7d59880917fe9ee024b5e/research_notes/portable_direct/riesel_r4_eighteen_sharp_20261125/REPORT.md), [exact source and receipts](https://github.com/awdawmip/enterprise-math/blob/37ea7118715feab970a943d0deacfb164e912eb8/research_notes/portable_direct/riesel_r4_eighteen_sharp_20261125/reproduction.json), [earlier two-stage prefilter](https://github.com/awdawmip/enterprise-math/blob/5c489fc73fef7d1fe5b4545bc6c393ce7cc0ac77/research_notes/portable_direct/riesel_r4_eleven_observer_20261125/REPORT.md), [tail eligibility](https://github.com/awdawmip/enterprise-math/blob/86964457e4281ad88df72b6abc222d95dd0c8736/research_notes/portable_direct/riesel_r4_ten_exact_20261125/REPORT.md).

## 1. Two separate private-point filters are essential

Assume the supplied normalized split branch: B={0,3,5,8,10,15,21,23,26,28,30,31,33} modulo 35 and at most 14 tail classes. Choose an inclusion-minimal normalized tail cover. Each selected class h has a private point on B, **before** any fixed tail or mod-7 row is removed. On its entire progression modulo 35, the earlier private-digit lemma therefore gives W(h/gcd(h,35))<=13, where W(m)=sum e(p-1). This is precisely the independent global m0 prefilter in high-exclusion.js. It includes all necessary periods: m has no prime >13, and W(m)<=13 implies m<=2^13; h/gcd(h,35)=m enumerates h by g in {1,5,7,35}. A class that becomes redundant after a replacement can be removed before choosing this minimal cover; no preservation of its particular period is required for the existence predicate.

For a branch fixing F subset of {(2,1),(3,1),(4,2)} and rows R subset of {0,1,2,3,5} modulo 7, let k=14-|F|-|R|, L=lcm(35, periods of F), and D be the remaining residues modulo L. Each unremoved class still has its private point in D (not covered by the fixed classes or rows), so W(h/gcd(h,L))<=k-1. This second bound is not interchangeable with the first. In particular W(L/35)-|F| can be 2, and if one uses the local bound alone the possible global digit weight can reach 15. The exact widened enumeration confirms the distinction: the local-only relaxed screen admits 563 additional candidate incidences, of which 75 survive capacity in five branches; there are 936 additional high-period/private-point incidences (28,778 vs 27,842). These are not missing cases for the original theorem because the global private-point bound for the whole minimal 14-tail cover excludes them. This is a proof-scope clarification, not a discovered counterexample. The earlier eleven-budget report explicitly uses both global and local bounds.

Under the stated tail eligibility, each surviving competitor must meet both bounds and the capacity bound: for relative period m=h/gcd(h,L), the maximum mass in D is max residue incidence divided by m. Every distinct digit witness requires a distinct competitor with the appropriate primary divisor. Sum those individually maximal masses and use unrestricted best mass for the remaining slots. Overlap can only lower the covered mass. This is a necessary screen for every class of the same minimal cover, hence all its competitors are retained in the screened candidate list.

## 2. Phase normalization logic

Conditional on the supplied basic-pair reduction and residual mask periodic modulo 35 on v, classify classes as shared (period prime to 3) or dedicated (period divisible by 3). If a phase mod 3 has no dedicated class, take any residual point v and choose v' congruent to v modulo the lcm of 35 and all shared periods in that phase; CRT applies since the lcm is prime to 3. A shared class covering v' covers v. Thus the shared classes alone suffice, contradicting inclusion minimality if a dedicated class was selected. Otherwise all three phases have dedicated classes. Provided the two fixed 19/73 classes cover the stated two phases (source geometry), replacing those phases' dedicated classes by the fixed pair does not raise cost and leaves at most 14 tails for budget 18. This checks the logical reduction, not the underlying 74-coordinate inventory/geometry.

## 3. Exact finite-search soundness and scoped replay

For every candidate h>17920, a private point can be translated by a multiple of L into x in D; arbitrary phases of other classes are allowed by the search relaxation. The translation preserves D and the absence of competitors at x. All generated CRT neighbors preserve the residue mod L, and other sample points are in D+jL. Points covered by the target are removed. A hypothetical cover supplies at most k-1 competing masks on any finite witness sample, and every nonempty such mask appears by enumerating periods and the point's residue, excluding the private point residue. Duplicates or dominated masks can be replaced by one superset in this relaxed model. This preserves the existence of a finite cover and can only weaken a no-go search. Recursive branching on an uncovered point is exhaustive; the sum of the largest r mask cardinalities is a valid upper bound for r distinct masks. Memoizing (uncovered set,remaining slots) is valid because the relaxation has no path-dependent inventory. A finite sample impossible to cover rules out an infinite cover. Returning an actual covering sample instead of proving impossibility triggers new witness points, not a rejection. The original code throws on a node-cap/inconclusive result and reports only yes=0 as exclusion.

Numeric key review: h<=215040 in the screened high domain, so encoding h*1000000+b with 0<=b<h is injective and below 2^53. The maximum joint period 435891456000 is below 2^53; CRT offset products use BigInt. The common integer capacity scale is divisible by every retained relative period. No numeric truncation is needed for this bound.

Independent exact arithmetic reconstructed **all 40 period-specific private-point counts** and 233 live branches, 27,842 cases, matching the author forward receipt exactly. This is a count/domain check, not a re-execution of all 27,842 search verdicts. For the highest tested candidate h=215040, independently rebuilt both affected branches and re-solved all 39 private-point cases using a separate BigInt set-cover implementation: minimum remaining-point degree pivot, distinct-mask domination, coarse cardinality bound, and independent CRT witness calculation. All 39 closed, no inconclusive cases; the finite scan cap is not used as a proof of a negative outcome, only for finding more witnesses. Branch f=5 (L=140,k=12): 13/13 closed, 26 sample rounds; f=7 (L=420,k=11): 26/26 closed, 52 sample rounds. The first separate run visited 365 and 939 nodes respectively; the archived combined replay (sorted period order) visited 361 and 955 nodes respectively, with identical verdicts and witness-round counts. No author DFS replay was used for these verdicts.

Exact executed output:
```json
{
  "fullPeriodCountsMatch": true,
  "oldCases": 27842,
  "newCases": 28778,
  "periodCount": 40,
  "oldBranch": 233,
  "newBranch": 233,
  "scale": "62768369664000",
  "extraCount": 563,
  "extraSurvivor": 75,
  "affected": [
    {
      "f": 2,
      "r": 0,
      "L": 105,
      "k": 13,
      "added": 14,
      "addedHigh": 3
    },
    {
      "f": 3,
      "r": 0,
      "L": 210,
      "k": 12,
      "added": 20,
      "addedHigh": 10
    },
    {
      "f": 4,
      "r": 0,
      "L": 140,
      "k": 13,
      "added": 12,
      "addedHigh": 2
    },
    {
      "f": 6,
      "r": 0,
      "L": 420,
      "k": 12,
      "added": 9,
      "addedHigh": 2
    },
    {
      "f": 7,
      "r": 0,
      "L": 420,
      "k": 11,
      "added": 20,
      "addedHigh": 14
    }
  ],
  "maxP": 435891456000,
  "maxExpandedP": 435891456000,
  "top": [
    {
      "f": 5,
      "r": 0,
      "L": 140,
      "k": 12,
      "periods": 327,
      "P": 67060224000,
      "privatePoints": 13,
      "closed": 13,
      "inconclusive": 0,
      "iterations": 26,
      "totalNodes": 361,
      "maxPts": 57
    },
    {
      "f": 7,
      "r": 0,
      "L": 420,
      "k": 11,
      "periods": 304,
      "P": 33530112000,
      "privatePoints": 26,
      "closed": 26,
      "inconclusive": 0,
      "iterations": 52,
      "totalNodes": 955,
      "maxPts": 94
    }
  ]
}
```

Reproduction (executed JS; compare oldHigh to the archive's high-exclusion-forward.json byPeriod, first component):
```js
function reproduce(){
 const B=[0,3,5,8,10,15,21,23,26,28,30,31,33],F0=[[2,1],[3,1],[4,2]],R0=[0,1,2,3,5],ps=[2,3,5,7,11,13];
 const gcd=(a,b)=>b?gcd(b,a%b):a,lcm=(a,b)=>a/gcd(a,b)*b,gB=(a,b)=>b?gB(b,a%b):a;
 function factors(n){let a=[];for(let p=2;p<=n;p++)if(n%p===0){let e=0;while(n%p===0){n/=p;e++}a.push([p,e])}return a}
 const W=n=>factors(n).reduce((s,[p,e])=>s+e*(p-1),0);
 const M=[];function gen(i,m,b){if(i===ps.length){M.push(m);return}for(let p=ps[i];b>=0;b-=p-1,m*=p)gen(i+1,m,b)}gen(0,1,15);
 const H=M.flatMap(m=>[1,5,7,35].map(g=>m*g).filter(h=>h/gcd(h,35)===m)).filter(h=>h>=9&&h!==10).sort((a,b)=>a-b);
 const scale=M.reduce((a,b)=>a/gB(a,BigInt(b))*BigInt(b),1n),max=a=>a.reduce((x,y)=>x>y?x:y,0n);
 const inv=(a,m)=>{let [r,s,x,y]=[a,m,1n,0n];while(s){let q=r/s;[r,s]=[s,r-q*s];[x,y]=[y,x-q*y]}if(r!==1n)throw Error("inverse");return (x%m+m)%m};
 const pc=n=>{let c=0;while(n){n&=n-1n;c++}return c};
 let oldHigh={},newHigh={},oldBranch=0,newBranch=0,extraCount=0,extraSurvivor=0,affected=[],maxP=0,maxExpandedP=0,top=[];
 for(let f=0;f<8;f++)for(let r=0;r<32;r++){
  const F=F0.filter((_,i)=>f>>i&1),R=R0.filter((_,i)=>r>>i&1),k=14-F.length-R.length,L=F.reduce((n,[m])=>lcm(n,m),35);
  const D=Array.from({length:L},(_,x)=>x).filter(x=>B.includes(x%35)&&!R.includes(x%7)&&!F.some(([m,b])=>x%m===b));if(!D.length)continue;
  const cand=H.flatMap(h=>{let g=gcd(h,L),m=h/g,w=W(m);if(w>k-1)return [];let a=Array(g).fill(0);for(const x of D)a[x%g]++;const cap=BigInt(Math.max(...a))*scale/BigInt(m);return cap?[{h,m,w,cap,old:W(h/gcd(h,35))<=13}]:[]});
  function screen(C){let best=max(C.map(x=>x.cap)),cache=new Map;const at=z=>{if(!cache.has(z))cache.set(z,max(C.filter(x=>x.m%z===0).map(x=>x.cap)));return cache.get(z)};return C.filter(x=>{let s=x.cap+BigInt(k-1-x.w)*best;for(const [p,e] of factors(x.m))for(let j=1;j<=e;j++)s+=BigInt(p-1)*at(p**j);return s>=BigInt(D.length)*scale})}
  const O=screen(cand.filter(x=>x.old)),N=screen(cand);
  extraCount+=cand.filter(x=>!x.old).length;extraSurvivor+=N.filter(x=>!x.old).length;
  const os=new Set(O.map(x=>x.h)),extra=N.filter(x=>!os.has(x.h));if(extra.length)affected.push({f,r,L,k,added:extra.length,addedHigh:extra.filter(x=>x.h>17920).length});
  const oh=O.filter(x=>x.h>17920),nh=N.filter(x=>x.h>17920),hs=O.map(x=>x.h),P=hs.reduce(lcm,L);
  if(oh.length){oldBranch++;maxP=Math.max(maxP,P)}if(nh.length){newBranch++;maxExpandedP=Math.max(maxExpandedP,N.map(x=>x.h).reduce(lcm,L))}
  for(const x of oh)oldHigh[x.h]=(oldHigh[x.h]??0)+D.length;for(const x of nh)newHigh[x.h]=(newHigh[x.h]??0)+D.length;
  if(!hs.includes(215040))continue;
  const target=215040,fp=new Map(factors(P)),fl=new Map(factors(L));let closed=0,inconclusive=0,iterations=0,totalNodes=0,maxPts=0;
  for(const x of D){
   let points=new Set;const add=n=>{if(n%target!==x%target)points.add(n)};
   for(let [p,e]of factors(target)){let pe=BigInt(p)**BigInt(fp.get(p)),other=BigInt(P)/pe,crt=other*inv(other%pe,pe);for(let i=fl.get(p)??0;i<e;i++)for(let a=1;a<p;a++)add(Number((BigInt(x)+crt*BigInt(a)*BigInt(p)**BigInt(i))%BigInt(P)))}
   for(let j=0;j<3;j++)for(let d of D)add(d+j*L);
   let status=false;
   for(let round=0;round<10;round++){
    iterations++;const pts=[...points],N=pts.length;maxPts=Math.max(maxPts,N);
    let masks=new Map;for(const h of hs){let rows=new Map;for(let i=0;i<N;i++){let r=pts[i]%h;if(r===x%h)continue;rows.set(r,(rows.get(r)??0n)|(1n<<BigInt(i)))}for(const [r,m]of rows)if(!masks.has(m))masks.set(m,[h,r])}
    let O=[...masks].map(([m,hr])=>({m,hr,n:pc(m)})).sort((a,b)=>b.n-a.n);
    let maximal=[];for(const o of O)if(!maximal.some(z=>(z.m&o.m)===o.m))maximal.push(o);O=maximal;
    const by=pts.map((_,i)=>O.filter(o=>o.m&(1n<<BigInt(i)))),failed=new Set;let nodes=0;
    function dfs(todo,k){if(++nodes>500000)throw Error("node cap");if(todo===0n)return [];if(!k||pc(todo)>k*(O[0]?.n??0))return null;let key=k+":"+todo;if(failed.has(key))return null;let opts=null;for(let i=0;i<N;i++)if(todo&(1n<<BigInt(i)))if(opts===null||by[i].length<opts.length)opts=by[i];for(let o of opts??[]){let res=dfs(todo&~o.m,k-1);if(res!==null)return [o.hr,...res]}failed.add(key);return null}
    let cover=dfs((1n<<BigInt(N))-1n,k-1);totalNodes+=nodes;
    if(cover===null){closed++;status=true;break}
    cover.push([target,x%target]);let before=points.size;outer:for(let j=0;j<100000;j++)for(let d of D){let n=j*L+d;if(!cover.some(([h,r])=>n%h===r)){add(n);if(points.size>=before+8)break outer}}
    if(points.size===before)break;
   }
   if(!status)inconclusive++;
  }
  top.push({f,r,L,k,periods:hs.length,P,privatePoints:D.length,closed,inconclusive,iterations,totalNodes,maxPts});
 }
 return {scale:String(scale),rel:M.length,H:H.length,oldHigh,newHigh,oldBranch,newBranch,extraCount,extraSurvivor,affected,maxP,maxExpandedP,top};
}
console.log(JSON.stringify(reproduce(),null,2))
```

## 4. Audit conclusion and boundary

The global/local prefilter distinction, logical phase reduction conditional on geometry, high-search finite obstruction kernel, all per-period case counts, and all highest-candidate private-point cases are supported by this audit. Together with the prior independent digit/capacity check, this strengthens the evidence for the author's split upper bound. It is not a fresh full replay of the remaining 27,803 high-period search verdicts. The compulsory 5/13 weighted omission certificate, the exact original inventory/geometry, and the CRT lower witness including full fixed-root provenance still require review for the full sharp 645120 theorem; do not declare Native Review or Result acceptance based on this scoped audit. No claim/owner change. q19(7,12) c701 onward remains the author's existing unfinished T6 frontier; no new T6 computation credited in this audit.
