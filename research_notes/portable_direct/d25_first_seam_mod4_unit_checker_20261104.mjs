// D25 first-wall exact p-adic test. Node.js or plain modern JS; no packages.
"use strict";
function prime(n){if(n<2)return false;for(let k=2;k*k<=n;k++)if(n%k===0)return false;return true;}
function mod(x,m){x%=m;return x<0n?x+m:x;}
function inv(v,m){let a=mod(v,m),b=m,x=1n,y=0n;while(b){const q=a/b;[a,b]=[b,a-q*b];[x,y]=[y,x-q*y];}if(a!==1n)throw Error("nonunit");return mod(x,m);}
function power(v,e,m){let z=1n;v=mod(v,m);while(e>0){if(e%2)z=z*v%m;v=v*v%m;e=Math.floor(e/2);}return z;}
function binom(n,k){let v=1n;for(let i=1;i<=k;i++)v=v*BigInt(n-k+i)/BigInt(i);return v;}
function chooseMod(n,k,m){let v=1n;for(let i=1;i<=k;i++)v=mod(v*BigInt(n-k+i)*inv(BigInt(i),m),m);return v;}
function check(p){const P=BigInt(p),Q=P*P,m=Math.floor(p/4),L=m+1,M=(p+1)/2;
let a=1n,b=1n;
for(let i=0;i<m;i++){const j=BigInt(i),D=(j+1n)**3n;
a=mod(a*(2n*j+1n)*(3n*j+1n)*(3n*j+2n)*inv(36n*D,Q),Q);
b=mod(b*(4n*j+1n)*(4n*j+2n)*(4n*j+3n)*inv(576n*D,Q),Q);}
const lam=p%4===1?mod((P+1n)*(P+2n)*inv(9n*(P+3n)**3n,Q),Q):mod((P-2n)*(P-1n)*inv(9n*(P+1n)**3n,Q),Q);
const expansion=p%4===1?mod((2n+P)*inv(243n,Q),Q):mod(2n*inv(9n,Q)-P,Q);
if(lam!==expansion)throw Error("lambda p^2 "+p);
const R=mod(a*inv(b,P),P);
const formula=mod(power(32n*inv(3n,P),m,P)*chooseMod(3*m,m,P)*(p%4===1?1n:-8n),P);
if(R!==formula)throw Error("ratio "+p);
const e=mod(lam*(a-b),Q);
if(e%P!==mod(lam*b*(R-1n),P))throw Error("first digit "+p);
let T=0n,q=1n;
for(let i=L;i<M;i++){const j=BigInt(i);
T=mod(T+(6n*j+1n)*q,Q);
q=mod(q*(4n*j+1n)*(4n*j+2n)*(4n*j+3n)*inv(576n*(j+1n)**3n,Q),Q);}
const flux=mod(P*e*T,P**3n);
if([5,7,11,13,19,97,373].includes(p)){
const c=binom(2*m,m);
const aa=mod(c*c*binom(3*m,m)*inv(216n**BigInt(m),Q),Q);
const bb=mod(c*c*binom(4*m,2*m)*inv(2304n**BigInt(m),Q),Q);
if(aa!==a||bb!==b||mod((aa-bb)*lam,Q)!==e)throw Error("independent binom "+p);
}
return {p,m,lambda:lam.toString(),E0_over_p:e.toString(),T0_mod_p:(T%P).toString(),flux:flux.toString()};
}
const rows=[];for(let p=5;p<=2000;p++)if(prime(p))rows.push(check(p));
const selected=rows.filter(v=>[5,7,11,13,19,97,373].includes(v.p));
const result={checked_primes:rows.length,max_prime:2000,failed:0,zero_E0_first_digit:rows.filter(v=>BigInt(v.E0_over_p)%BigInt(v.p)===0n).map(v=>v.p),selected};
if(typeof console!=="undefined")console.log(JSON.stringify(result,null,2));
