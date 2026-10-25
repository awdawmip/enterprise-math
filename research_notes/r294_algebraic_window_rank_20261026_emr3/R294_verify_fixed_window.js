'use strict';
// Exact BRC auxiliary coefficient and quadratic-field rank verifier; Node >=18.
// No native X6 time evolution or classical phase calculation is performed.
const fs=require('fs');
const N=90, MAX_N=180;
const z=()=>Array(N+1).fill(0n);
const con=(a,b)=>{const c=z();for(let i=0;i<=N;i++)if(a[i])for(let j=0;i+j<=N;j++)if(b[j])c[i+j]+=a[i]*b[j];return c;};
const sh=(a,k)=>{const c=z();for(let i=0;i+k<=N;i++)c[i+k]=a[i];return c;};
const add=(...pairs)=>{const out=z();for(const [c,v]of pairs)for(let i=0;i<=N;i++)out[i]+=BigInt(c)*v[i];return out;};
const ONE=z();ONE[0]=1n;
const h=z();
for(let n=1;n<=N;n++){
  h[n]=(n===4?1n:0n);
  for(const [i,k] of [[1,1n],[2,2n],[3,1n],[4,1n]])if(n>=i)h[n]+=k*h[n-i];
  for(const [i,k] of [[1,1n],[2,2n],[3,1n]])if(n>=i){
    for(let j=0;j<=n-i;j++)h[n]+=k*h[j]*h[n-i-j];
  }
}
const yONE=sh(ONE,1);
const w=add([1n,ONE],[1n,yONE],[1n,h],[1n,sh(h,1)]);
const W=[ONE];for(let i=1;i<=16;i++)W.push(con(W[i-1],w));
// D(y)=(1-y)(1-y^3)(1-3y+y^2).
const D=[1n,-4n,4n,-2n,4n,-4n,1n];
const K=z(); K[0]=1n;
for(let n=1;n<=N;n++){
 let sum=0n;for(let j=1;j<=Math.min(n,6);j++)sum+=D[j]*BigInt(2*n-j)*K[n-j];
 const den=BigInt(2*n);if((-sum)%den!==0n)throw Error('noninteger inverse square root at n='+n);
 K[n]=-sum/den;
}
const J=z();J[0]=1n;for(let i=1;i<=N;i++)J[i]=K[i]-J[i-1];
const dMinus=add([1n,ONE],[-1n,sh(w,1)]);
const dPlus=add([1n,ONE],[-1n,yONE],[1n,sh(ONE,2)],[-1n,sh(w,1)]);
const C=(eps,m)=>{
 if(eps==='+'&&m===0)return con(J,add([1n,ONE],[1n,yONE],[1n,sh(ONE,2)],[-2n,sh(w,1)],[-1n,sh(w,2)]));
 if(eps==='-'&&m===0)return con(J,sh(add([1n,W[2]],[-1n,w]),3));
 if(eps==='-'&&m===1)return con(J,sh(add([1n,w],[-1n,ONE]),2));
 const s=Math.floor(m/2)+1, power=eps==='+'?m:m-2;
 return sh(con(J,con(W[power],eps==='+'?dPlus:dMinus)),s);
};
// Exact rank field R=(A+B*sqrt(5))/4 with BigInt coefficients.
const R=(eps,m)=>{
 if(eps==='+'&&m===0)return [-7n,5n];
 if(eps==='-'&&m===0)return [-37n,17n];
 if(eps==='-'&&m===1)return [-10n,4n];
 const mm=BigInt(m),s=BigInt(Math.floor(m/2)+1);
 if(eps==='+')return [-3n-8n*mm-15n*mm*mm-4n*s,5n+2n*mm+7n*mm*mm];
 const q=mm-2n;
 return [-9n-18n*q-15n*q*q-4n*s,5n+8n*q+7n*q*q];
};
const cmp=(a,b)=>{
 const A=a[0]-b[0],B=a[1]-b[1];
 if(B===0n)return A>0n?1:A<0n?-1:0;
 if(A===0n)return B>0n?1:-1;
 if((A>0n)===(B>0n))return A>0n?1:-1;
 const d=A*A-5n*B*B;
 if(d===0n)return 0;
 return (A>0n?1:-1)*(d>0n?1:-1);
};
const even=[['+',4],['-',4],['-',2],['+',6],['+',2],['-',6],['-',0],['+',8],['+',0],['-',8],['+',10],['-',10],['+',12],['-',12],['+',14]];
const odd=[['-',3],['+',5],['+',3],['-',5],['-',1],['+',7],['+',1],['-',7],['+',9],['-',9],['+',11],['-',11],['+',13]];
for(const xs of [even,odd])for(let i=1;i<xs.length;i++){
 if(cmp(R(...xs[i]),R(...xs[i-1]))!==1)throw Error('quadratic ordering not strict: '+JSON.stringify(xs[i-1])+','+JSON.stringify(xs[i]));
}
// Independent raw six-edge DP preserves each source word, sign, translation, and previous zero bit.
let dp=new Map([['0|1|0|0',1n]]), generated=0, compare=0, peak=0;
const edges={0:[[2,-1,-1],[2,1,-1]],1:[[0,-1,-1],[0,1,-1]],2:[[1,1,1],[2,1,-1]]};
for(let n=0;n<=MAX_N;n++){
 const terminal=new Map();for(const [key,v]of dp){const [qs,es,ks]=key.split('|');if(+qs!==0)continue;const e=+es,k=+ks,idx=e+'|'+k;terminal.set(idx,(terminal.get(idx)||0n)+v);}
 const xs=n%2?odd:even;
 for(const [eps,m]of xs){const e=eps==='+'?1:-1,got=terminal.get(e+'|'+(-m))||0n;const coeff=C(eps,m)[Math.floor(n/2)];if(got!==coeff)throw Error('Laurent/source mismatch n='+n+' effect='+eps+','+(-m)+' expected='+coeff+' got='+got);compare++;}
 if(n>=81){const ranked=[...terminal.entries()].sort((a,b)=>a[1]===b[1]?a[0].localeCompare(b[0]):(a[1]>b[1]?-1:1));const expected=xs.slice(0,3).map(([eps,m])=>(eps==='+'?1:-1)+'|'+(-m));const actual=ranked.slice(0,3).map(x=>x[0]);if(actual.join(',')!==expected.join(','))throw Error('top3 mismatch at '+n+': '+actual);if(ranked[2][1]<=ranked[3][1])throw Error('tie for third at '+n);peak++;}
 if(n===MAX_N)break;
 const next=new Map();for(const [key,v]of dp){const [qs,es,ks,zs]=key.split('|').map(Number);for(let bit=0;bit<=1;bit++){
  if(bit===0&&zs===1)continue;
  const [q1,eta,c]=edges[qs][bit];const key1=q1+'|'+(eta*es)+'|'+(eta*ks+c)+'|'+(bit===0?1:0);
  next.set(key1,(next.get(key1)||0n)+v);
 }}dp=next;generated++;
}
const gap=(a,b)=>{const x=R(...a),y=R(...b);return {A:(y[0]-x[0]).toString(),B:(y[1]-x[1]).toString(),denominator:4}};
const evidence={schema:'EM_R294_FIXED_WINDOW_V1',status:'PASS',model:'ordered 6-edge positive BRC, no consecutive 00, terminal q0, full affine effect',series_max_degree:N,dp_max_length:MAX_N,coefficient_equalities:compare,top_three_checked_lengths:peak,even_ranking:even,odd_ranking:odd,even_first_second_normalized_gap:gap(even[0],even[1]),odd_first_second_normalized_gap:gap(odd[0],odd[1]),method:'exact BigInt DP, algebraic formal-series recurrences, Q(sqrt(5)) strict comparison; no floating-point sign decisions',logical_scope:'finite coefficient cross-check plus exact rank constants; infinite eventual top-three follows analytically conditional on R283 precise generating functions and R293 28-effect reduction'};
fs.writeFileSync(process.argv[2]||'R294_EVIDENCE.json',JSON.stringify(evidence,null,2)+'\n');
console.log(JSON.stringify({status:'PASS',compare,peak,evenGap:evidence.even_first_second_normalized_gap,oddGap:evidence.odd_first_second_normalized_gap}));
