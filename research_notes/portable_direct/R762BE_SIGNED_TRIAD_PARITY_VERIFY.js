'use strict';
const fs = require('fs');
// Exact signed-parity triad candidate; parity is NOT a P000/native law.
function fac(n){let a=1n;for(let i=2;i<=n;i++)a*=BigInt(i);return a;}
function bin(n,k){return k<0||k>n?0n:fac(n)/(fac(k)*fac(n-k));}
function D(n,p,q,t){
 if(n<0||p<0||q<0||t<0||p>n||q>n||t>n)return 0n;
 const v=t-n+p+q;if(v%2!==0)return 0n;
 const x=v/2;if(x<Math.max(0,p+q-n)||x>Math.min(p,q))return 0n;
 return bin(p,x)*bin(n-p,q-x)*fac(q)*fac(n-q)*fac(t)*fac(n-t);
}
function perms(n){let a=Array.from({length:n},(_,i)=>i),ans=[];
 function go(k){if(k===n){ans.push(a.slice());return;}for(let i=k;i<n;i++){[a[k],a[i]]=[a[i],a[k]];go(k+1);[a[k],a[i]]=[a[i],a[k]];}}go(0);return ans;}
let byN=[],profiles=0,candidates=0,valid=0,checks=0;
for(let n=1;n<=5;n++){
 const ps=perms(n);if(BigInt(ps.length)!==fac(n))throw Error('incomplete permutation set');
 let perProfiles=0,perCandidates=0,perValid=0,perChecks=0;
 for(let p=0;p<=n;p++)for(let q=0;q<=n;q++)for(let t=0;t<=n;t++){
  const R=Array.from({length:n},(_,i)=>i<p?1:-1);
  const S=Array.from({length:n},(_,i)=>i<q?1:-1);
  const T=Array.from({length:n},(_,i)=>i<t?1:-1);
  let got=0n;const pair=Array.from({length:n},()=>Array(n).fill(0n));
  for(let s of ps)for(let w of ps){
   perCandidates++;let good=true;
   for(let i=0;i<n;i++)if(R[i]*S[s[i]]*T[w[i]]!==1){good=false;break;}
   if(good){got++;pair[s[0]][w[0]]++;}
  }
  if(got!==D(n,p,q,t))throw Error('bad total '+[n,p,q,t]);
  for(let j=0;j<n;j++)for(let k=0;k<n;k++){
   const expect=R[0]*S[j]*T[k]===1?
     D(n-1,p-(R[0]===1?1:0),q-(S[j]===1?1:0),t-(T[k]===1?1:0)):0n;
   if(pair[j][k]!==expect)throw Error('bad pair '+[n,p,q,t,j,k]);
   perChecks++;
  }
  perProfiles++;perValid+=Number(got);
 }
 byN.push({n,profiles:perProfiles,namedCandidatePartitions:perCandidates,validNamedPartitions:perValid,pairThirdChecks:perChecks});
 profiles+=perProfiles;candidates+=perCandidates;valid+=perValid;checks+=perChecks;
}
if(D(2,2,1,1)!==2n||D(1,1,0,0)!==1n)throw Error('two-triad witness');
const evidence={
 schema:'R762BE_EXACT_PARITY_TRIAD_CHECK_V1',status:'PASS',date:'2026-11-15',
 scope:'conditional signed-parity triadic relation; author-proved NOT_REVIEWED',
 arithmetic:'exact BigInt analytic count vs independently enumerated named bijections',
 maxN:5,totals:{profiles,namedCandidatePartitions:candidates,validNamedPartitions:valid,pairThirdChecks:checks},
 byN,witness:{n:2,r:[1,1],s:[1,-1],third:[{axis:3,sign:1},{axis:4,sign:-1}],fullPartitions:2,observedPair:'u+ on axis1, v+ on axis2',unsignedHiddenAxes:[3,4],signedHiddenAxes:[3],namedLiftForAxis3:1,namedLiftForAxis4:0},
 limits:['All-n formula follows symbolic matching proof; tests exhaust only n=1..5','sign parity is a declared candidate, not native P000 TRIADIC_CLOSURE_E','all full partitions uniquely anchor at the named first saturated axis']
};
const content=JSON.stringify(evidence,null,2)+'\n';
if(require.main===module){const out=process.argv[2]||'R762BE_SIGNED_TRIAD_PARITY_EVIDENCE.json';fs.writeFileSync(out,content);console.log(content);}
module.exports={D,evidence};
