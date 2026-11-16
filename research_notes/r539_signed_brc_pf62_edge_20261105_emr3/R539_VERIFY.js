'use strict';
// R539 | m=62 | frozen signed BRC R462 | exact reproducible BigInt certificate
const result=(function exactR539(){
 const m=62, cache=new Map(), ab=x=>x<0n?-x:x;
 const gcd=(a,b)=>{a=ab(a);b=ab(b);while(b)[a,b]=[b,a%b];return a};
 const lcm=(a,b)=>a/gcd(a,b)*b;
 function bin(n,k){if(n<0||k<0||k>n)return 0n;k=Math.min(k,n-k);if(k===0)return 1n;const key=n+":"+k;if(cache.has(key))return cache.get(key);let z=1n;for(let i=1;i<=k;i++)z=z*BigInt(n+1-i)/BigInt(i);cache.set(key,z);return z}
 const cat=k=>bin(2*k,k)/BigInt(k+1);
 function H(k,t){const r=2*k+1;if(t<2||t>r)return 0n;let s=0n;for(let q=0;q<=r-t;q++)s+=bin(r-t,q)*(bin(2*t,r-2*q)-bin(2*t,r-2*q-1));return bin(r+t,2*t)*s}
 function B(k,t){const r=2*k+1;if(t<2||t>r)return 0n;let s=0n;for(let q=0;q<=Math.min(Math.floor((t-1)/2),k);q++)s+=bin(t-1,2*q)*4n**BigInt(q)*cat(k-q);return bin(r+t,2*t)*s}
 function D(k,n){const p=B(k,2),h=Array.from({length:n},(_,j)=>B(k,j+3)),d=[1n];for(let j=1;j<=n;j++){let s=0n,pow=1n;for(let a=1;a<=j;a++){s+=(a%2?1n:-1n)*h[a-1]*pow*d[j-a];pow*=p}d.push(s)}return d[n]}
 function G(k){const x=BigInt(k);return (x*(x+1n)*(2n*x+1n)*(2n*x+3n))**BigInt(m)*(x+2n)}
 function dif(v){let a=v.slice(),r=[];while(a.length){r.push(a[0]);a=a.slice(1).map((x,i)=>x-a[i])}return r}
 function N(d,k,b){let s=0n;for(let j=0;j<d.length;j++)s+=d[j]*bin(k-b,j);return s}
 function bareiss(A){const a=A.map(r=>r.slice()),n=a.length;let prev=1n,sign=1n;for(let i=0;i<n-1;i++){if(!a[i][i]){let j=i+1;while(j<n&&!a[j][i])j++;if(j===n)return 0n;[a[i],a[j]]=[a[j],a[i]];sign=-sign;}const p=a[i][i];for(let j=i+1;j<n;j++){for(let h=i+1;h<n;h++){const v=p*a[j][h]-a[j][i]*a[i][h];if(v%prev)throw Error("Bareiss non-exact division");a[j][h]=v/prev;}a[j][i]=0n;}prev=p;}return sign*a[n-1][n-1];}
 let L=1n,values=[];
 for(let k=1;k<=2*m;k++){const a=D(k,m),b=cat(k)**BigInt(m)*G(k),g=gcd(a,b);values.push([a/g,b/g]);L=lcm(L,b/g)}
 const delta=dif(values.map(([a,b])=>a*(L/b)));
 const deltaDegree=delta.findLastIndex(x=>x!==0n);
 if(deltaDegree!==2*m-1)throw Error("Unexpected interpolant degree: "+deltaDegree);
 for(let k=1;k<=6*m+1;k++)if(L*D(k,m)!==cat(k)**BigInt(m)*G(k)*N(delta,k,1))throw Error("Polynomial identity failed at "+k);
 let origin=null,tail=null,tailSign=null;
 for(let k=1;k<=3000;k++){let e=dif(Array.from({length:2*m},(_,j)=>N(delta,k+j,1)));if(e.every(x=>x>0n)||e.every(x=>x<0n)){origin=k;tail=e;tailSign=e[0]>0n?"+":"-";break}}
 if(origin===null)throw Error("Tail not certified");
 const pre=Array.from({length:origin-1},(_,i)=>N(delta,i+1,1));
 let blocks=[];for(let i=0;i<pre.length;i++){const s=pre[i]>0n?"+":pre[i]<0n?"-":"0";if(blocks.length&&blocks.at(-1).sign===s)blocks.at(-1).to=i+1;else blocks.push({from:i+1,to:i+1,sign:s})}
 blocks.push({from:origin,to:"infinity",sign:tailSign});
 let direct=0,cross=0;
 for(let k=1;k<=20;k++){const mat=Array.from({length:m},(_,i)=>Array.from({length:m},(_,j)=>H(k,3+i-j)));if(bareiss(mat)!==D(k,m))throw Error("Direct determinant mismatch at "+k);direct++;for(let t=2;t<=m+1;t++){if(H(k,t)!==B(k,t))throw Error("H=B mismatch at "+k+","+t);cross++}}
 let grid=0;for(let k=1;k<=6*m+1;k++)for(let t=2;t<=m+2;t++){if(H(k,t)!==B(k,t))throw Error("Full grid H=B mismatch at "+k+","+t);grid++}
 return {status:"R539_EXACT_JS_PASS",date:"2026-11-05",scientific_pin:"18783e01e3646c72b7aab3b16d3f565e83e6446f",order:m,degree_max:6*m,G:"[k(k+1)(2k+1)(2k+3)]^62*(k+2)",interpolant_degree_max:2*m-1,interpolant_actual_degree:deltaDegree,L:String(L),delta_at_k1:delta.map(String),identity_grid:"k=1.."+(6*m+1),identity_checks:6*m+1,tail_shift_origin_k:origin,tail_sign:tailSign,tail_newton:tail.map(String),finite_values_before_tail:pre.map(String),sign_blocks:blocks,direct_Bareiss_checks:direct,original_signed_to_ballot_checks:cross,full_coefficient_grid_checks:grid,exact_arithmetic:"BigInt integer only",proof_premise:"Frozen R462 H=B and the derived fixed-t p_t(k)=H_k(t)/Catalan_k in Q[k] with degree<=2t",status_scope:"AUTHOR_SIDE_EXACT_CONDITIONAL_CERTIFICATE / DRIVER_UNREVIEWED / NOT_ADMITTED"};
})();
console.log(JSON.stringify(result,null,2));
