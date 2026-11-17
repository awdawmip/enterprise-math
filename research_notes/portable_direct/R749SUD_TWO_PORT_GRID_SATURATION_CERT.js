#!/usr/bin/env node
"use strict";
// R749SUD exact integer reproduction. No third-party packages.
// Arithmetic exact for the declared finite regression inputs (all intermediates < 2^53).
// General theorems and arbitrary-size integer inputs are proved in the companion paper.
// For unbounded K,M beyond Number.MAX_SAFE_INTEGER, port to BigInt.
function fastCount(K,M) {
  if (!Number.isInteger(K)||!Number.isInteger(M)||K<=M||M<1) throw Error("domain K>M>=1");
  let total=(2*M+1)*(2*M*M+2*M+1);
  for(let u=1;u<=M;u++)for(let v=1;v<=M;v++)for(let a=1;a<=M;a++)
    total+=Math.max(0,M-Math.floor(K*u*v/(a*(K-Math.max(u,v)))));
  return total;
}
function directCount(K,M) {
  let total=0;
  for(let i=0;i<=M;i++)for(let j=0;j<=M;j++)for(let b=0;b<=M;b++)for(let c=0;c<=M;c++){
    if(i===M||j===M||b===0||c===0){total++;continue;}
    const u=M-i,v=M-j,a=M-b+1,d=M-c+1;
    if((K-Math.max(u,v))*a*d>K*u*v) total++;
  }
  return total;
}
function phi(n) {
  let x=n, ans=n;
  for(let p=2;p*p<=x;p++)if(x%p===0){while(x%p===0)x/=p;ans-=ans/p;}
  if(x>1)ans-=ans/x;
  return ans;
}
function energy(M){
  let e=M*M;
  for(let h=2;h<=M;h++)e+=2*phi(h)*Math.floor(M/h)**2;
  return e;
}
function plateau(M){return (2*M+1)*(2*M*M+2*M+1)+(M**4-energy(M))/2;}
function main() {
  let pairs=0;
  for(let M=1;M<=7;M++)for(let K=M+1;K<9*M+5;K++){
    const a=fastCount(K,M),b=directCount(K,M);
    if(a!==b)throw Error("independent mismatch M="+M+" K="+K);
    pairs++;
  }
  const tested=[];
  for(let M=1;M<=10;M++){
    const first=M===1?2:M===2?5:M*(M-1)**2+1;
    const target=plateau(M);
    if(fastCount(first,M)!==target)throw Error("plateau missing "+M);
    if(M>1&&fastCount(first-1,M)>=target)throw Error("sharpness fails "+M);
    for(let K of [first,first+1,first+5])if(fastCount(K,M)!==target)throw Error("not plateau "+M);
    if(M>=3) {
      let equality=false;
      for(let u=1;u<=M;u++)for(let v=1;v<=M;v++)for(let a=1;a<=M;a++)for(let d=1;d<=M;d++){
        if(a*d<=u*v)continue;
        const lhs=Math.max(u,v)*a*d, rhs=M*(M-1)**2*(a*d-u*v);
        if(lhs>rhs)throw Error("bound false "+M);
        if(lhs===rhs)equality=true;
      }
      if(!equality)throw Error("bound non-sharp "+M);
    }
    tested.push({M,energy:energy(M),plateau:target,first_saturated_K:first,at_previous_K:M>1?fastCount(first-1,M):null});
  }
  const selected=[[2,1],[3,2],[4,3],[5,4],[5,2],[7,3],[12,3],[13,3],[36,4],[37,4],[80,5],[81,5],[320,160]].map(([K,M])=>({K,M,classes:fastCount(K,M),fixed_width_bits:Math.ceil(Math.log2(fastCount(K,M)))}));
  return {status:"PASS",arithmetic:"exact integer within safe JS integer bound on the tested inputs",pairs_independently_checked:pairs,saturation_checked:tested,selected_grids:selected,proof_scope:"Theorems A-C for all integer K>M>=1; finite checks are independent regression evidence",frozen_science:"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389"};
}
console.log(JSON.stringify(main(),null,2));
