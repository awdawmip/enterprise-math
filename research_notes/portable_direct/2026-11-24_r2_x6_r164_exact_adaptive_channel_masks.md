# X6 R164 — Exact direction-specific channel masks for the static six-pair observer

2026-11-24. AUTHOR ANALYTIC PROOF / EXACT FINITE CROSSCHECK / NOT_REVIEWED. Independent informed continuation, not a formal Task Result or native heartbeat computation. Frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f, R162@3682ce83f1a1638e29f600769ffa6cd6207b4841 and R163@c8a9d155c12ba72410a3f9f3b2a793e1e4657adb. P000 V5, Heartbeat World and joint-observer preservation remain unchanged.

## Proposition (any Port, fixed positive ratio)

Use the unchanged four scalar heights h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z), six absolute labeled gaps and positive pair capacities s_ij=w_i+w_j. A direction score F=max g_ij/s_ij. Write r=C/A, b=B/A, d=D/A. Scale A=1 for comparisons (actual F has the factor 1/A). Let c=g_AC, f=g_BD. For X=B or D, put a=g_AX, e=g_CX. A minimal fixed channel mask that exactly evaluates the direction score for every b,d>0 at fixed r is as follows:
* keep AC iff c>0; keep BD iff f>0;
* keep AX iff a>0 and either (a>e and c=a-e), or ar>e;
* keep CX iff e>0 and either (e>a and c=e-a), or e>ar;
* exceptional case r=1,c=0,a=e>0: retain exactly one of AX,CX, e.g. AX.

The last rule applies separately to X=B and X=D. All strict inequalities are exact; no need to sample parameters. Every retained nonduplicate channel can uniquely attain the full score for some positive weights at that ratio. A retained identical pair is replaceable only by its mate. Hence the mask is minimum among fixed subsets of the six original channels preserving each direction's full score uniformly at fixed r. This is an evaluation theorem, not a deletion of raw joint relations, a minimal end-to-end decision circuit, or a claim about future native evolution.

## Proof

For AX, let t=w_X/A>0. To beat AC and CX it suffices and is necessary (with c=0 interpreted as no AC upper bound) that a>0, c(1+t)<a(1+r), and (a-e)t+ar-e>0. Once these hold, send the remaining free weight Y to a sufficiently large finite value: all three channels incident to Y tend to zero while AX is fixed positive. Thus a unique local win is equivalent to a unique global win.

Since the heights are scalars, c=a+e or c=|a-e| (including zero gaps). If ar>e, at t approaching zero both strict inequalities hold, because c<=a+e<a(1+r). If a<=e and ar<=e the second inequality cannot hold. If a>e and c=a+e with ar<=e the first cannot hold. In the remaining case a>e and c=a-e, define U=a(1+r)/c-1>0. At t=U the first is equality and the left side of the second equals 2ar>0. Taking t slightly below U yields both strict inequalities. This proves AX criterion; swapping A and C and replacing r by 1/r proves CX criterion. For a=e>0, c=0, r=1 the two functions are identical and positive; they dominate all other channels when the other free weight tends to infinity. If a=e and c=2a at r=1, AC strictly dominates both for t>0. AC with c>0 uniquely wins for both B,D sufficiently large. BD with f>0 uniquely wins for both B,D sufficiently small.

For sufficiency without any generic-position assumption, the nonretained nonzero channels in the above cases are pointwise bounded by AC or their mate (as shown by the failed inequalities with their signs); a domination chain terminates in AC or a retained mate, except an identical pair, for which one representative is retained. Zero channels never determine the positive score of a nonzero physical direction. Thus the maximum of the mask equals F. Necessity follows from the explicit unique-win witnesses above and from the identical-pair witness. This proves exact score factorization for the declared static observer, all positive B,D, and any scalar height row, hence any integer Port. The full six raw gaps and sign/physical direction provenance remain stored.

## Port 10 practical consequence at r=22/17

R162 gives ten possible near rows, R163 six optimizer rows. In channel order AB,AC,AD,BC,BD,CD the minimum score masks are:

| direction | retained channels |
|---|---|
| (1,0,0) | AC AD BC BD |
| (1,3,-1) | AB AC BD CD |
| (4,-4,1) | AC BC CD |
| (4,-1,0) | AB AD BD |
| (5,-4,1) | AC BC BD CD |
| (5,-1,0) | AB AC BD CD |
| (6,-4,1) | AD BD |
| (6,-1,0) | AB AC AD |
| (7,-1,0) | AB AC AD BD |
| (9,-5,1) | AC AD BC BD |

Ten-row joint exact evaluation uses 35 instead of 60 row-channel fractions. Identical (channel,numerator) pairs can be reused, leaving 22 distinct fractions, six capacities shared. Six-row optimizer-only uses 20 instead of 36 row-channel fractions, or 15 distinct fractions. These are operation counts, not wall-clock speedups, and not a claim that the distinct fraction count is circuit-minimal. For exact rational weights one can also compare by cross multiplication. At r=1, the row (6,-1,0) reduces to AC alone; (4,-1,0) and (6,-4,1) illustrate the identical-pair degeneracies.

## Actual crosscheck

The following JavaScript was executed in the current research turn. It verifies the mask preserves the full maximum for every one of the 1935 physical Port-10 representatives, ten exact rational ratios, and 25 integer B,D pairs per ratio. Integer products here remain within the exact safe integer range. Output: {"checks":483750,"rows":1935,"ratios":10,"weights_per_ratio":25,"joint":[35,22],"optimizer":[20,15]}. The continuous theorem is proved analytically above; the finite crosscheck is additional evidence, not the proof of continuous coverage.

```javascript
function verify(){
 const J=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]], rows=[];
 function g([x,y,z]){const h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z];return J.map(([i,j])=>Math.abs(h[i]-h[j]))}
 function local(a,e,c,n,d){return a>0&&((a>e&&c===a-e)||a*n>e*d)}
 function mask([a,c,b,e,f,h],n,d){const m=[local(a,e,c,n,d),c>0,local(b,h,c,n,d),local(e,a,c,d,n),f>0,local(h,b,c,d,n)];if(n===d&&c===0){if(a===e&&a>0)m[0]=true;if(b===h&&b>0)m[2]=true}return m}
 for(let x=-10;x<=10;x++)for(let y=-10;y<=10;y++)for(let z=-10;z<=10;z++){const v=[x,y,z];if(!(v.find(t=>t!==0)>0)||Math.max(v.reduce((a,t)=>a+Math.max(t,0),0),v.reduce((a,t)=>a+Math.max(-t,0),0))>10)continue;rows.push([v,g(v)])}
 if(rows.length!==1935)throw Error("population");
 const ratios=[[1,10],[1,3],[1,2],[1,1],[10,9],[22,17],[4,3],[7,5],[2,1],[10,1]], values=[1,2,7,30,1000];let checks=0;
 for(const [n,d] of ratios)for(const [v,a] of rows){const m=mask(a,n,d);if(!m.some(Boolean))throw Error("empty mask");for(const B of values)for(const D of values){const w=[d,B,n,D],s=J.map(([i,j])=>w[i]+w[j]);let k=m.findIndex(Boolean);for(let j=0;j<6;j++)if(m[j]&&a[j]*s[k]>a[k]*s[j])k=j;for(let j=0;j<6;j++)if(a[j]*s[k]>a[k]*s[j])throw Error(JSON.stringify({v,n,d,B,D,j}));checks++}}
 const T=[[1,0,0],[1,3,-1],[4,-4,1],[4,-1,0],[5,-4,1],[5,-1,0],[6,-4,1],[6,-1,0],[7,-1,0],[9,-5,1]],W=T.filter(v=>![[1,3,-1],[4,-4,1],[5,-4,1],[7,-1,0]].some(u=>String(u)===String(v)));
 function totals(V,n,d){let count=0;const uniq=new Set();for(const v of V){const a=g(v);mask(a,n,d).forEach((on,j)=>{if(on){count++;uniq.add(`${j}:${a[j]}`)}})}return [count,uniq.size]}
 const t=totals(T,22,17),w=totals(W,22,17);if(String(t)!=="35,22"||String(w)!=="20,15")throw Error("totals");
 return {checks,rows:rows.length,ratios:ratios.length,weights_per_ratio:25,joint:t,optimizer:w};
}
console.log(verify());
```

## Continuation

The exact original registration receipt r2-20261124-0310-r155-own-session-v1 was read as SUCCEEDED, Researcher EM-DIRECT-AE5AD5, RA-B60559848FD879270DCA6317, execution_authorized=false. Current X6 continuation r2-20261124-1110-x6-cont-read-v1 was observed RUNNING/NATIVE_RUNNER before publication. No CLAIM, formal Result, Review or owner mutation. Next scientific question: use active-channel masks jointly with strict near decision boundaries to test if further comparisons can be skipped without computing each exact row score; or extend adaptive banks for smaller Ports. Independent mathematical review pending.
