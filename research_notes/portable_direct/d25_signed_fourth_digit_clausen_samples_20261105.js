// D25 signed fourth-digit witnesses. Node.js 18+; exact BigInt, no dependencies.
"use strict";
const md=(a,m)=>((a%m)+m)%m;
function inv(a,m){let[x,y,b,c]=[0n,1n,m,md(a,m)];while(c){const q=b/c;[x,y]=[y,x-q*y];[b,c]=[c,b-q*c];}if(b!==1n)throw Error("nonunit");return md(x,m);}
function recurrenceW(p,m){let a=1n,w=0n;for(let k=0n;k<p;k++){w=md(w+(6n*k+1n)*a,m);if(k<p-1n)a=md(a*(2n*k+1n)*(3n*k+1n)*(3n*k+2n)*inv(36n*(k+1n)**3n,m),m);}return w;}
function factorialW(p,m){const f=[1n];for(let k=1n;k<=3n*(p-1n);k++)f.push(md(f.at(-1)*k,m));let w=0n,pow216=1n;for(let k=0n;k<p;k++){const j=Number(k);const ak=md(f[2*j]*f[3*j]*inv(pow216*f[j]**5n,m),m);w=md(w+(6n*k+1n)*ak,m);pow216=md(pow216*216n,m);}return{w,f};}
function recurrencePsi(p,m){const n=(p-1n)/6n,x=inv(2n,m);let a=1n,z=1n,g=0n,v=0n;for(let k=0n;k<=n;k++){g=md(g+a*z,m);if(k>0n)v=md(v+2n*k*a*z,m);if(k<n){a=md(a*2n*(k-n)*(k-2n*n)*inv((2n+2n*k-p)*(k+1n),m),m);z=md(z*x,m);}}return md(g*(g+6n*v),m);}
function fallingPsi(p,m,f){const n=(p-1n)/6n;let g=0n,v=0n;for(let k=0n;k<=n;k++){let a=1n,b=1n;for(let j=0n;j<k;j++){a=md(a*(j-n)*(j-2n*n),m);b=md(b*(2n+2n*j-p),m);}const t=md(a*inv(b*f[Number(k)],m),m);g=md(g+t,m);v=md(v+2n*k*t,m);}return md(g*(g+6n*v),m);}
const expected={
  7:["350","1246","215"],
  13:["19786","7761","925"],
  19:["82327","123158","4710"],
  373:["11832087049","14593651483","44491459"]
};
for(const P of [7,13,19,373]){const p=BigInt(P),m=p**4n,W=recurrenceW(p,m),f=factorialW(p,m),Psi=recurrencePsi(p,m),P2=fallingPsi(p,m,f.f);
 const diff=md(W-Psi,m);if(W!==f.w||Psi!==P2||diff%p!==0n)throw Error("route mismatch p="+P);
 const Q=diff/p,row=[String(W),String(Psi),String(Q)];if(row.some((a,i)=>a!==expected[P][i]))throw Error("certificate mismatch p="+P);
 console.log("PASS p="+P+" W="+W+" Psi="+Psi+" Q="+Q);
}
