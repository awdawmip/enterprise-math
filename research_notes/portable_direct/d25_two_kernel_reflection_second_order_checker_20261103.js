"use strict";
function primes(n){let s=Array(n+1).fill(true);s[0]=s[1]=false;for(let i=2;i*i<=n;i++)if(s[i])for(let j=i*i;j<=n;j+=i)s[j]=false;return s.flatMap((v,i)=>v&&i>=5?[i]:[]);}
function powmod(a,e,m){a=(BigInt(a)%m+m)%m;e=BigInt(e);let z=1n;while(e){if(e&1n)z=z*a%m;a=a*a%m;e>>=1n;}return z;}
function egcd(a,b){if(!b)return [a,1n,0n];let [g,x,y]=egcd(b,a%b);return [g,y,x-a/b*y];}
function inv(a,m){let [g,x]=egcd((BigInt(a)%m+m)%m,m);if(g!==1n)throw Error("nonunit");return (x%m+m)%m;}
function fac(n){let v=1n;for(let i=2;i<=n;i++)v*=BigInt(i);return v;}
function comb(n,k){let v=1n;for(let i=1;i<=k;i++)v=v*BigInt(n-i+1)/BigInt(i);return v;}
function check(p,show){let P=BigInt(p),m=P*P,U=[1n],H=[0n],samples=[],rows=[];
 for(let n=1;n<=4*p;n++)U[n]=U[n-1]*(n%p?BigInt(n):1n)%m;
 for(let i=1;i<p;i++)H[i]=(H[i-1]+inv(BigInt(i),P))%P;
 let Q=((powmod(3n,P-1n,m)-1n)/P-5n*((powmod(2n,P-1n,m)-1n)/P)+5n*P)%P;
 let unit=n=>U[n]*fac(Math.floor(n/p))%m;
 for(let k=1;k<p;k++){
  let a=p-k,num=unit(4*k)*unit(k)*unit(4*a)*unit(a)%m,den=unit(2*k)*unit(3*k)*unit(2*a)*unit(3*a)%m;
  let observed=num*inv(den,m)%m*powmod(3n*inv(32n,m)%m,P,m)%m;
  let q2=Math.floor(2*k/p),q3=Math.floor(3*k/p),q4=Math.floor(4*k/p);
  let r2=2*k%p,r3=3*k%p,r4=4*k%p,d=q4-q2-q3;
  let tau=(((d%2?-1n:1n)*3n*comb(2,q3)*inv(comb(3,q4),m)*inv(16n,m))%m+m)%m;
  let E=((Q+4n*H[r4-1]+H[k-1]-2n*H[r2-1]-3n*H[r3-1])%P+P)%P;
  let expected=tau*(1n+P*E)%m;
  if(observed!==expected)throw Error(JSON.stringify({p,k,observed:String(observed),expected:String(expected)}));
  rows.push({tau,E});
  if(show&&[1,2,Math.floor(p/4)+1,Math.floor(p/2)].includes(k))samples.push({p,k,d,tau:String(tau),E:String(E),product:String(observed)});
 }
 for(let k=1;k<p;k++)if(rows[k-1].E!==rows[p-k-1].E||rows[k-1].tau!==rows[p-k-1].tau)throw Error("symmetry p="+p+" k="+k);
 return samples;
}
function main(){
 let ps=primes(400),samples=[];
 for(let p of ps)samples.push(...check(p,[13,19,373].includes(p)));
 let a=samples.find(x=>x.p===13&&x.k===1),b=samples.find(x=>x.p===13&&x.k===2);
 if(ps.length!==76||a.product!=="1"||b.product!=="157"||a.E===b.E)throw Error("coverage or witness");
 return {result:"PASS",primes:ps.length,index_checks:ps.reduce((v,p)=>v+p-1,0),samples};
}
if(typeof process!=="undefined")console.log(JSON.stringify(main(),null,2));
