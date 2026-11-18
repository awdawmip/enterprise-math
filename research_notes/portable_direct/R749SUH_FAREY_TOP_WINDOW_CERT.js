'use strict';
// R749SUH: bounded exhaustive regression for the proved high-tail rigidity theorem.
// Run with: node R749SUH_FAREY_TOP_WINDOW_CERT.js
function allMatrices(M) {
  const out = [];
  for (let a = 1; a <= M; a++) for (let d = 1; d <= M; d++) {
    const p = a*d - 1;
    if (p <= 0) continue;
    for (let u = 1; u <= M; u++) {
      if (p % u !== 0) continue;
      const v = p/u;
      if (v < 1 || v > M) continue;
      out.push({a,d,u,v,tau:Math.max(u,v)*a*d});
    }
  }
  return out;
}
function canonical(M, z) {
  const x=M-z.a, y=M-z.d, b=M-Math.max(z.u,z.v), w=M-Math.min(z.u,z.v);
  return x===y && x===b+1 && w===b+2;
}
function F(M,j) {return (M-j+1)*(M-j)*(M-j);}
function certifiedJ(M) {
  let j=0;
  while (j+1<=M-2 && (3*(j+1)-1)**2<4*(M+1)) j++;
  return j;
}
let matrices=0, noncanon=0, windows=0, squareCases=[];
let sample={};
for (let M=6;M<=96;M++) {
  const arr=allMatrices(M), j0=certifiedJ(M);
  const groups=new Map();
  let bestNoncanon=0;
  for (const z of arr) {
    matrices++;
    groups.set(z.tau, (groups.get(z.tau)||0)+1);
    if (canonical(M,z)) continue;
    noncanon++;
    bestNoncanon=Math.max(bestNoncanon,z.tau);
    const x=M-z.a,y=M-z.d,b=M-Math.max(z.u,z.v),S=x+y+b;
    if(S*S<4*(M+1)) throw Error('minimum noncanonical defect violated '+JSON.stringify({M,z,S}));
    if(27*z.tau>(3*M-S)**3) throw Error('product AM-GM violation '+JSON.stringify({M,z,S}));
  }
  const largest=[...groups.keys()].sort((a,b)=>b-a);
  for(let j=1;j<=j0;j++) {
    windows++;
    if (largest[j-1]!==F(M,j) || groups.get(F(M,j))!==2 || bestNoncanon>=F(M,j))
      throw Error('first-j rigidity violated '+JSON.stringify({M,j,j0,bestNoncanon,top:largest.slice(0,j0)}));
  }
  if([6,15,20,24,32,64,80,96].includes(M)) sample[M]={certified_j:j0,actual_canonical_before_intrusion:largest.findIndex(t=>groups.get(t)!==2 || t!==F(M,largest.indexOf(t)+1)),best_noncanonical_threshold:bestNoncanon};
}
for(let t=4;t<=40;t++) {
  const M=t*t-1,a=M-t,d=a,u=M,v=t*(t-2);
  const witness=M*a*d, upper=(M-2*t/3)**3;
  if(a*d-u*v!==1 || !Number.isInteger(witness) || !(witness<=upper) || 2*witness<=M**3)
    throw Error('square-minus-one family fails t='+t);
  squareCases.push({t,M,witness});
}
const result={status:'PASS',model:'positive integer labeled two-Port unimodular threshold; not native X6 event',tested_M_range:[6,96],tested_matrix_instances:matrices,tested_noncanonical:noncanon,top_j_certificates:windows,tested_square_minus_one_t_range:[4,40],samples:sample,square_family_samples:squareCases.filter(x=>[4,5,6,10,20,40].includes(x.t)),exact_arithmetic:'JS Number integers safe over finite exhaustive domain; no numerical tolerance',limitations:'finite verification complements infinite parameter proof in paper'};
console.log(JSON.stringify(result,null,2));
