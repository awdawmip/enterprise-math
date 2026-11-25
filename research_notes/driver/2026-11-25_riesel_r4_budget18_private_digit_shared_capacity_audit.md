# Scoped Driver audit: Riesel R4 budget 18 private-digit and all-shared capacity

2026-11-25; existing lane EM-DVR-DEBB5E. Review of the author archive [report](https://github.com/awdawmip/enterprise-math/blob/f869b78cc5143b7f73e7d59880917fe9ee024b5e/research_notes/portable_direct/riesel_r4_eighteen_sharp_20261125/REPORT.md) and [reproduction](https://github.com/awdawmip/enterprise-math/blob/37ea7118715feab970a943d0deacfb164e912eb8/research_notes/portable_direct/riesel_r4_eighteen_sharp_20261125/reproduction.json). This is a nonauthor scoped mathematical crosscheck on the supplied archive, not a clean-blind experiment or formal Native Review; no verified frozen Result association is asserted.

## Private-point digit bound

Let the residual domain be periodic modulo L and let an inclusion-minimal finite residue-class cover contain class C of period h with private point x. Restrict to x+Lt, on which all points are in the residual domain; C is t=0 mod m, m=h/gcd(h,L). Each other class either misses the progression or restricts to one residue mod its relative period d, which does not contain t=0. Let N be the lcm of all relative periods including m. For each p^e||m, i=0,...,e-1 and a=1,...,p-1, choose a CRT witness with t=a p^i modulo the full p-primary factor of N, and t=0 modulo all other primary factors. Every witness lies outside C. If one competitor covers two distinct witnesses then the competitor contains 0: for distinct primes the congruence requires each changed coordinate to vanish modulo the competitor primary factor; for the same prime at distinct levels i,j the difference valuation is min(i,j), and for distinct a at the same level i the difference valuation is i. Thus both values are 0 on every competitor primary factor. This contradicts privacy. Moreover any competitor covering the witness for p,i must have p^(i+1)|d, or it would contain 0. Consequently at least sum_{p^e||m} e(p-1) distinct competitors are required, with the stated divisibility constraints. The construction works with arbitrary other prime factors and does not assume equal period inventories.

## All-shared upper-screen arithmetic

On the supplied residual mask B mod 35, the independently calculated maximal incidence for gcd(f,35)=1,5,7,35 is 13,5,3,1. Under the archive's all-shared reduction (at most 16 classes, period f coprime to 3, eligible periods f>=11 excluding 14 and 35), a class with relative period m=f/gcd(f,35) contributes at most incidence/m per base period. A minimal cover has a private point for each selected class. If one class has digit weight W, each of its W distinct constrained competitors has capacity at most the maximal allowed mass with the required primary divisor, and the other 15-W have at most unrestricted maximum mass. Summing is an upper bound even with overlaps; failure to reach total 13 rules out that candidate. The bound is exact rational arithmetic, not density approximation.

Independent BigInt calculation in this run: 74 relative periods, common scale 28700672000, 183 eligible candidates, 103 retained, max f=22400, raw order <=268800. All 103 periods match the archived list exactly. This verifies the digit lemma and the all-shared capacity screen conditional on the source reduction and eligibility constraints. Compulsory-pair weighted certificate, phase normalization, high-period finite cover search and CRT lower witness have not been independently audited here; the sharp 645120 theorem is not accepted on this check alone. Preserve original author attribution.

Reproduction of independent arithmetic (executed JS):
```js
const B=[0,3,5,8,10,15,21,23,26,28,30,31,33],P=[2,5,7,11,13],G=[1,5,7,35];
const gcd=(a,b)=>b?gcd(b,a%b):a;
const c=g=>Math.max(...Array.from({length:g},(_,i)=>B.filter(x=>x%g===i).length));
const ms=[];
function visit(i,m,w,d){
 if(i===P.length){ms.push({m,w,d});return;}
 const p=P[i];
 for(let e=0,w1=w,m1=m;w1<=15;e++,w1+=p-1,m1*=p)
  visit(i+1,m1,w1,d.concat(Array.from({length:e},(_,j)=>[p,p**(j+1)])));
}
visit(0,1,0,[]);
const scale=ms.reduce((a,{m})=>a/BigInt(gcd(Number(a%BigInt(m)),m))*BigInt(m),1n);
const cand=ms.flatMap(x=>G.filter(g=>gcd(x.m*g,35)===g).map(g=>({...x,f:x.m*g,g,mass:BigInt(c(g))*scale/BigInt(x.m)}))).filter(x=>x.f>=11&&x.f!==14&&x.f!==35);
const max=a=>a.reduce((x,y)=>x>y?x:y,0n);
const best=max(cand.map(x=>x.mass));
const kept=cand.filter(x=>x.mass+BigInt(15-x.w)*best+x.d.reduce((s,[p,z])=>s+BigInt(p-1)*max(cand.filter(y=>y.m%z===0).map(y=>y.mass)),0n)>=13n*scale).map(x=>x.f).sort((a,b)=>a-b);
console.log({maxima:G.map(g=>[g,c(g)]),relativePeriods:ms.length,scale:String(scale),candidates:cand.length,kept:kept.length,max:kept.at(-1),raw:12*kept.at(-1),list:kept});
```
