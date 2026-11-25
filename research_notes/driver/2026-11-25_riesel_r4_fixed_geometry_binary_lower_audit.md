# Riesel R4 fixed geometry and binary lower bound: scoped Driver audit

2026-11-25; existing Driver EM-DVR-DEBB5E, nonauthor audit of supplied author science (EM-DIRECT-970E1C / RA-D2EC212845B63844081F9A14). No Native Review, Result admission or Task closure. Source [budget18 archive](https://github.com/awdawmip/enterprise-math/blob/37ea7118715feab970a943d0deacfb164e912eb8/research_notes/portable_direct/riesel_r4_eighteen_sharp_20261125/reproduction.json) and [all-budget CRT lower construction](https://github.com/awdawmip/enterprise-math/blob/2ae5de00bf7e8f1e2571ef5666e95f82a25dc429/research_notes/portable_direct/riesel_r4_twelve_observer_lower_20261125/REPORT.md). This verifies geometry directly from archived A4, S4 and fixed prime inventory, rather than trusting the geometry receipt. Primality of all 74 historically fixed coordinates is inherited as the fixed prime inventory premise, not re-proved here.

## Geometry crosscheck

A4 is 3 modulo 6, and S4 is exactly six times the product of 74 distinct pairwise-coprime coordinates. Of these 27 are nonzero, exactly the 20 old primes P and seven fixed extra primes 5,13,19,73,38737,246241,487824887233. Direct modular doubling on the original exponents over 6720 verifies all 1152 old holes, all even and exactly the supplied 36 u=n/2 residues modulo 105. Direct doubling over 20160 verifies the mask after 5 and 13: n=8+12v, (v-2)/3 mod35 (division by 3 modulo35) lies in B. On that residual progression 19 covers v=0 mod3 and 73 covers v=1 mod3, both exactly. The normalized holes after both are precisely the 208 points n=32+36w with w mod35 in B. Each claimed full period is verified by modular exponentiation. Fixed tail periods 2,3,4 and phases 1,1,2 are verified independently over 420 w points each.

The four free anchors 1009,21169,4278255361,394783681 are prime by trial division and the expected 14:0,14:10,20:0,20:8 phases verified. With the other six anchors in the source, the old dictionary and the ten anchors leave exactly 12 holes modulo 60480, namely n=3488 mod5040. All 10 private witnesses hit the corresponding own anchor and none of P, any other anchor, 246241, or the relaxed potential high-order class n=3488 mod560. The whole combined period 60480 is verified. Thus these witnesses force all ten anchors in the lower construction when other potential competitors are suppressed.

## Lower construction argument

For budget b>=11 put t=b-11, w=96+140z. Use one prime of exact raw order 560*2^j for each j=1,...,t with phase z=2^(j-1) mod 2^j, one target prime of order 5040*2^t for the final z=0 mod2^t leaf, and two repair primes of orders 1120*2^t and 3360*2^t for the two halves of that final leaf. These orders are distinct: the first series has no factor 3, the first repair is the next strictly higher power of 2 in that series, the second repair has one factor 3, and the target has two factors 3. Exact effective periods on n=32+36w are respectively 140*2^j, 140*2^t, 280*2^t, 280*2^t by gcd with 36. All raw orders are multiples of 560 and the chosen exponent n0 is 3488 mod560; hence no such class invades any anchor witness. Standard Bang-Zsigmondy for 2^d-1 supplies a prime of each such order (all d>6). Checked against all 74 fixed coordinates and four free anchors: for every such possible order dividing a coordinate minus one, exact modular order testing gives zero clashes (11 divisibility-passing tests). The remaining factors of S4 are 2,3 and cannot be these primes. Thus CRT can assign distinct new coordinates preserving the fixed root class. A4 is odd and divisible by 3, not a multiple of 6: prime 3 is inactive; prime 2 never covers a positive exponent and its possible isolated hit at n=0 cannot improve a periodic cover of all positive exponents.

The private-point lemma on the full old-hole progression modulo 6720 bounds every raw order in an inclusion-minimal complement cover of at most b classes by 6720*2^(b-1). Indeed W(d/gcd(d,6720))<=b-1 implies d/gcd(d,6720)<=2^(b-1). This applies to any candidate complement cover, not only the designed dictionary. The finite set of other nonfixed primes of orders at most this bound can be set to residue zero by CRT. The extra fixed 246241 covers only w=1 mod3, equivalently z=2 mod3, and cannot replace an entire dyadic leaf or half-leaf; each has infinitely many points outside z=2 mod3.

In the open root the target covers the final leaf and the nonzero leaves are disjoint; at least ten anchors, t nonzero leaves and one final class are necessary. In the closed root the target is inactive and both repair classes are necessary; exact costs are b and b+1. Choose the CRT roots sufficiently large for strict proper divisors. For any observer modulus not divisible by the target prime, all shared CRT requirements can be extended to an identical residue modulo that modulus, because only the target prime differs. Then root observers and all future-term observers agree, proving lower bound 5040*2^(b-11), in particular 645120 at b=18. This audit supports the lower argument under the fixed prime inventory and standard primitive divisor theorem, separate from the finite upper search and weighted basic-pair omission certificate. It does not claim the upper theorem or a native admission.

## Exact executed output

```json
{
  "fixedCount": 74,
  "unique": 74,
  "allDivideStep": true,
  "stepEqualsSixProduct": true,
  "Amod6": "3",
  "pairwiseCoprime": true,
  "PCount": 20,
  "activeCount": 27,
  "activeExtra": [
    "5",
    "13",
    "19",
    "73",
    "38737",
    "246241",
    "487824887233"
  ],
  "oldPeriodVerified": true,
  "normPeriodVerified": true,
  "holes": 1152,
  "odd": 0,
  "mismatch": 0,
  "pairMismatch": 0,
  "phaseMismatch": 0,
  "normHoles": 208,
  "normMismatch": 0,
  "tail": [
    {
      "q": "38737",
      "h": 2,
      "r": 1,
      "orderVerified": true,
      "errors": 0
    },
    {
      "q": "246241",
      "h": 3,
      "r": 1,
      "orderVerified": true,
      "errors": 0
    },
    {
      "q": "487824887233",
      "h": 4,
      "r": 2,
      "orderVerified": true,
      "errors": 0
    }
  ],
  "actualFree": [
    {
      "q": "1009",
      "h": 14,
      "prime": true,
      "periodOK": true,
      "phaseErrors": 0
    },
    {
      "q": "21169",
      "h": 14,
      "prime": true,
      "periodOK": true,
      "phaseErrors": 0
    },
    {
      "q": "4278255361",
      "h": 20,
      "prime": true,
      "periodOK": true,
      "phaseErrors": 0
    },
    {
      "q": "394783681",
      "h": 20,
      "prime": true,
      "periodOK": true,
      "phaseErrors": 0
    }
  ],
  "anchorHoles": 12,
  "anchorMismatch": 0,
  "privateTests": [
    {
      "n": 6,
      "own": true,
      "old": false,
      "other": false,
      "repair": false,
      "potential": false
    },
    {
      "n": 12,
      "own": true,
      "old": false,
      "other": false,
      "repair": false,
      "potential": false
    },
    {
      "n": 152,
      "own": true,
      "old": false,
      "other": false,
      "repair": false,
      "potential": false
    },
    {
      "n": 20,
      "own": true,
      "old": false,
      "other": false,
      "repair": false,
      "potential": false
    },
    {
      "n": 140,
      "own": true,
      "old": false,
      "other": false,
      "repair": false,
      "potential": false
    },
    {
      "n": 968,
      "own": true,
      "old": false,
      "other": false,
      "repair": false,
      "potential": false
    },
    {
      "n": 2048,
      "own": true,
      "old": false,
      "other": false,
      "repair": false,
      "potential": false
    },
    {
      "n": 9968,
      "own": true,
      "old": false,
      "other": false,
      "repair": false,
      "potential": false
    },
    {
      "n": 4352,
      "own": true,
      "old": false,
      "other": false,
      "repair": false,
      "potential": false
    },
    {
      "n": 320,
      "own": true,
      "old": false,
      "other": false,
      "repair": false,
      "potential": false
    }
  ],
  "orderPeriodErrors": 0,
  "tested": 11,
  "fixedOrderClashes": []
}
```

Reproduction (extract basic-pair-weighted.js as a UTF-8 string from the pinned archive; independent checker parses literal data, does not execute the original script):
```js
function checkGeometry(src){
 const fixed=JSON.parse(src.match(/const fixedPrimes = (\[[^\n]+\])\.map\(BigInt\);/)[1]).map(BigInt);
 const P=JSON.parse(src.match(/const P=(\[[^\n]+\])\.map\(BigInt\);/)[1]).map(BigInt);
 const [,As,Ss]=src.match(/const A4=(\d+)n,S4=(\d+)n;/),A=BigInt(As),S=BigInt(Ss);
 const B=[0,3,5,8,10,15,21,23,26,28,30,31,33],H=[0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100];
 const pow=(a,e,q)=>{a=BigInt(a);let v=1n;for(e=BigInt(e);e;e>>=1n,a=a*a%q)if(e&1n)v=v*a%q;return v};
 const mask=(classes,N)=>{let covered=new Uint8Array(N);for(let [q,a] of classes){let v=a*a%q;for(let n=0;n<N;n++,v=2n*v%q)if(v===1n)covered[n]=1}return covered};
 const get=q=>A%q,orig=P.map(q=>[q,get(q)]),active=fixed.filter(q=>get(q)!==0n),extra=active.filter(q=>!P.includes(q)),gcd=(a,b)=>b?gcd(b,a%b):a;
 let old=mask(orig,6720),holes=0,odd=0,mismatch=0;for(let n=0;n<old.length;n++){if(!old[n]){holes++;odd+=n%2}let expected=n%2===0&&H.includes((n/2)%105);if(expected!==!old[n])mismatch++}
 const basic=[5n,13n,19n,73n].map(q=>[q,get(q)]),norm=mask([...orig,...basic],20160);let normHoles=0,normMismatch=0;
 for(let n=0;n<norm.length;n++){if(!norm[n])normHoles++;let expected=n>=32&&(n-32)%36===0&&B.includes(((n-32)/36)%35);if(expected!==!norm[n])normMismatch++}
 const pair=mask([...orig,...basic.slice(0,2)],20160);let pairMismatch=0,phaseMismatch=0;
 for(let n=0;n<20160;n++){let v=(n-8)/12;let expected=Number.isInteger(v)&&v>=0&&B.includes((((v-2)*12)%35+35)%35);
 if(expected!==!pair[n])pairMismatch++;
 if(Number.isInteger(v)&&v>=0)for(let [i,r] of [[2,0],[3,1]]){let [q,a]=basic[i];if((a*a%q*pow(2,n,q)%q===1n)!==(v%3===r))phaseMismatch++}
 }
 const tail=[[38737n,2,1],[246241n,3,1],[487824887233n,4,2]].map(([q,h,r])=>({q:String(q),h,r,orderVerified:pow(2,36*h,q)===1n,errors:Array.from({length:420},(_,w)=>w).filter(w=>(get(q)**2n*pow(2,32+36*w,q)%q===1n)!==(w%h===r)).length}));
 const anchorQs=[5n,13n,19n,73n,38737n,487824887233n,1009n,21169n,4278255361n,394783681n];
 const freeW=[0,10,0,8],anchors=anchorQs.map((q,i)=>[q,i<6?get(q):pow((q+1n)/2n,16+18*freeW[i-6],q)]);
 const expectedOrders=[14,14,20,20];const actualFree=anchors.slice(6).map(([q,a],i)=>({q:String(q),h:expectedOrders[i],prime:(()=>{for(let k=2n;k*k<=q;k++)if(q%k===0n)return false;return true})(),periodOK:pow(2,36*expectedOrders[i],q)===1n,phaseErrors:Array.from({length:280},(_,w)=>w).filter(w=>(a*a%q*pow(2,32+36*w,q)%q===1n)!==(w%expectedOrders[i]===freeW[i])).length}));
 const all=mask([...orig,...anchors],60480);let anchorHoles=0,anchorMismatch=0;
 for(let n=0;n<all.length;n++){if(!all[n])anchorHoles++;if((n%5040===3488)!==!all[n])anchorMismatch++}
 const witnesses=[6,12,152,20,140,968,2048,9968,4352,320],competitor=246241n;
 const hits=([q,a],n)=>a*a%q*pow(2,n,q)%q===1n;
 let privateTests=witnesses.map((n,i)=>({n,own:hits(anchors[i],n),old:orig.some(x=>hits(x,n)),other:anchors.some((x,j)=>j!==i&&hits(x,n)),repair:hits([competitor,get(competitor)],n),potential:n%560===3488%560}));
 let orderPeriodErrors=0;for(const [q,a] of [...orig,...anchors])if(a!==0n&&pow(2,60480,q)!==1n)orderPeriodErrors++;
 let fixedOrderClashes=[],tested=0;
 for(const q of [...fixed,...anchorQs.slice(6)]){for(let t=0;;t++){const s=1n<<BigInt(t);const ds=[560n*s,5040n*s,1120n*s,3360n*s];if(ds[0]>q-1n)break;for(const d of ds){if((q-1n)%d)continue;tested++;if(pow(2,d,q)!==1n)continue;let ok=true;for(const p of [2n,3n,5n,7n])if(d%p===0n&&pow(2,d/p,q)===1n)ok=false;if(ok)fixedOrderClashes.push([String(q),String(d)])}}}
 const prod=fixed.reduce((a,b)=>a*b,1n);
 return {fixedCount:fixed.length,unique:new Set(fixed.map(String)).size,allDivideStep:fixed.every(q=>S%q===0n),stepEqualsSixProduct:S===6n*prod,Amod6:String(A%6n),pairwiseCoprime:fixed.every((q,i)=>fixed.slice(i+1).every(p=>gcd(q,p)===1n)),PCount:P.length,activeCount:active.length,activeExtra:extra.map(String),oldPeriodVerified:orig.every(([q])=>pow(2,6720,q)===1n),normPeriodVerified:[...orig,...basic].every(([q])=>pow(2,20160,q)===1n),holes,odd,mismatch,pairMismatch,phaseMismatch,normHoles,normMismatch,tail,actualFree,anchorHoles,anchorMismatch,privateTests,orderPeriodErrors,tested,fixedOrderClashes};
}
console.log(JSON.stringify(checkGeometry(src),null,2));
```
