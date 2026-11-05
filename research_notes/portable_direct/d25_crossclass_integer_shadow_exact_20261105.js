// Exact supplementary certificate for D25 complementary primes and terminating shadows.
// Node.js: node d25_crossclass_integer_shadow_exact_20261105.js
'use strict';
function mod(a,m){let r=a%m;return r<0n?r+m:r;}
function inv(a,m){
 let b=m,u=1n,v=0n;a=mod(a,m);
 while(b){const q=a/b;[a,b]=[b,a-q*b];[u,v]=[v,u-q*v];}
 if(a!==1n)throw Error('Non-unit denominator');
 return mod(u,m);
}
function prime(p){if(p<2)return false;for(let d=2;d*d<=p;d++)if(p%d===0)return false;return true;}
function originals(p){
 const P=BigInt(p),M=P**3n;let a=1n,b=1n,w=0n,v=0n;
 for(let k=0;k<p;k++){
  const K=BigInt(k),j=K+1n;
  w=mod(w+(6n*K+1n)*a,M);v=mod(v+(8n*K+1n)*b,M);
  if(k+1<p){
   a=mod(a*(2n*K+1n)*(2n*K+2n)*(3n*K+1n)*(3n*K+2n)*(3n*K+3n)*inv(216n*j**5n,M),M);
   b=mod(b*(4n*K+1n)*(4n*K+2n)*(4n*K+3n)*(4n*K+4n)*inv(2304n*j**4n,M),M);
  }
 }
 return {w,v};
}
function shadow(n,precision=1){
 const N=BigInt(6*n+1),M=N**BigInt(precision),halfInverse=inv(2n,M);
 let b2=1n,b3=1n,b4=1n,power=1n,s=0n;
 for(let k=0;k<=2*n;k++){
  s=mod(s+BigInt(6*k+1)*mod(b2*b3*b4*power,M),M);
  if(k<2*n){
   const j=BigInt(k+1);
   b2=b2*BigInt(2*n-k)/j;
   b3=b3*BigInt(3*n-k)/j;
   b4=b4*BigInt(4*n-k)/j;
   power=mod(-power*halfInverse,M);
  }
 }
 return s;
}
function run(){
 let primes=0,one=0,five=0;
 for(let p=5;p<=1500;p++)if(prime(p)){
  const P=BigInt(p),target=p%3===1?P:P**3n-P,{w,v}=originals(p);
  if(w!==target||v!==target)throw Error('Prime mismatch '+p);
  primes++;if(p%6===1)one++;else five++;
 }
 for(let n=1;n<=500;n++)if(shadow(n)!==0n)throw Error('Shadow mismatch '+n);
 if(shadow(2,2)!==104n||shadow(3,2)!==76n)throw Error('Second-digit controls failed');
 return {status:'PASS',primes,one_mod6:one,five_mod6:five,shadow_range:'1..500',shadow_13_square:String(shadow(2,2)),shadow_19_square:String(shadow(3,2))};
}
if(typeof module!=='undefined'&&require.main===module)console.log(JSON.stringify(run()));
