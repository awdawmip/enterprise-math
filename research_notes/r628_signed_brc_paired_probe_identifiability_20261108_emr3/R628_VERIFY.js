
function run(){
 const ok=(v,m)=>{if(!v)throw Error(m)};
 const C=(n,k)=>{if(n<0||k<0||k>n)return 0n;let v=1n;k=Math.min(k,n-k);for(let i=1;i<=k;i++)v=v*BigInt(n-i+1)/BigInt(i);return v};
 const T=v=>{while(v.length>1&&v.at(-1)===0n)v.pop();return v};
 const add=(a,b)=>T(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+(b[i]||0n)));
 const sub=(a,b)=>T(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)-(b[i]||0n)));
 const mul=(a,b)=>{let v=Array(a.length+b.length-1).fill(0n);a.forEach((x,i)=>b.forEach((y,j)=>v[i+j]+=x*y));return T(v)};
 const sh=(a,r)=>Array(r).fill(0n).concat(a),tr=(a,d)=>T(a.slice(0,d+1).length?a.slice(0,d+1):[0n]);
 const nu=a=>{for(let i=0;i<a.length;i++)if(a[i]!==0n)return i;return Infinity};
 const eq=(a,b)=>{a=T(a.slice());b=T(b.slice());return a.length===b.length&&a.every((z,i)=>z===b[i])};
 const K=i=>{let ds=[-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3)],z=[0n];for(let k=1;k<=4;k++){let n=i+1-k;if(n>=0&&ds[k-1]!==0n)z=add(z,sh(Array.from({length:n+1},(_,j)=>-ds[k-1]*C(n,j)),i-1))}return z};
 const ks=Array.from({length:12},(_,i)=>K(i+1));ok(ks.every((z,i)=>nu(z)===i),"frozen valuations");
 const P=[0,2,4,6,8,10].map(i=>ks[i]),M=[1,3,5,7,9,11].map(i=>ks[i]),D=P.map((p,i)=>sub(p,M[i]));
 const c=D.map(z=>z[nu(z)]),orders=D.map(nu);
 ok(orders.join(",")==="0,2,4,6,8,10","delta valuations");
 ok(c.map(String).join(",")==="2,-8,6,106,83,9","delta coefficients");
 const perms=[];function perm(a,k){if(k===6){perms.push(a.slice());return}for(let i=k;i<6;i++){[a[k],a[i]]=[a[i],a[k]];perm(a,k+1);[a[k],a[i]]=[a[i],a[k]]}}
 perm([0,1,2,3,4,5],0);ok(perms.length===720,"perms");
 const checks={band:0,normalized:0,wide_full_series:0,sharp_depth:0,unpaired_nuisance:0};
 const Y=(pi,g,h)=>[pi.map((j,x)=>add(mul(g[x],P[j]),h[x])),pi.map((j,x)=>add(mul(g[x],M[j]),h[x]))];
 for(const [a,b] of [[0,0],[0,1],[2,3],[5,5]]){
   const d=b+8;
   for(let t=0;t<3;t++)for(const pi of perms){
     const g=Array.from({length:6},(_,x)=>sh([BigInt((x+t)%2?3:-1),BigInt(x+1)],a+(x+t)%(b-a+1)));
     const h=Array.from({length:6},(_,x)=>[BigInt(x*7+t),BigInt(x-2),1n]);const [u,v]=Y(pi,g,h);
     for(let x=0;x<6;x++){
       const z=tr(sub(u[x],v[x]),d),r=nu(z);
       let j=r===Infinity?5:-1;
       if(r!==Infinity)for(let i=0;i<5;i++)if(r>=a+2*i&&r<=b+2*i)j=i;
       ok(j===pi[x],"band orientation");
     }checks.band++;
   }
   let g=sh([1n],b),h=[3n,-2n],h2=add(h,sub(mul(g,P[4]),mul(g,P[5])));
   ok(eq(tr(add(mul(g,P[4]),h),d-1),tr(add(mul(g,P[5]),h2),d-1)),"depth plus");
   ok(eq(tr(add(mul(g,M[4]),h),d-1),tr(add(mul(g,M[5]),h2),d-1)),"depth minus");checks.sharp_depth++;
 }
 const abs=z=>z<0n?-z:z,tab=new Map(c.map((z,i)=>[String(abs(z)),i]));
 for(const R of [0,1,4])for(let t=0;t<2;t++)for(const pi of perms){
   const g=Array.from({length:6},(_,x)=>sh([BigInt((x+t)%2?1:-1),BigInt(x+1)],(x+t)%(R+1)));
   const h=Array.from({length:6},(_,x)=>[BigInt(x+2),0n,3n]);const[u,v]=Y(pi,g,h);const ids=[];
   for(let x=0;x<6;x++){let z=tr(sub(u[x],v[x]),R+8),r=nu(z);ids.push(r===Infinity?null:tab.get(String(abs(z[r]))))}
   ok(ids.filter(z=>z===null).length<=1,"normalization missing");if(ids.includes(null))ids[ids.indexOf(null)]=5;
   ok(ids.every((j,x)=>j===pi[x]),"normalized orientation");checks.normalized++;
 }
 let U5=D[4].slice(8),U6=D[5].slice(10);ok(U5[0]===83n&&U6[0]===9n,"U leading");
 for(let a of [0,2,7]){
   const A5=sh(U6,a+2),A6=sh(U5,a);
   ok(nu(A5)===a+2&&nu(A6)===a,"wide band gains");
   ok(eq(mul(A5,D[4]),mul(A6,D[5])),"entire delta coincidence");
   for(let [i,j,g,h] of [[4,5,A5,A6],[5,4,A6,A5]]){
     let H=[7n,-3n],H2=add(H,sub(mul(g,P[i]),mul(h,P[j])));
     ok(eq(add(mul(g,P[i]),H),add(mul(h,P[j]),H2)),"full plus");
     ok(eq(add(mul(g,M[i]),H),add(mul(h,M[j]),H2)),"full minus");checks.wide_full_series++;
   }
 }
 for(let pi of perms){for(let j of pi){ok(eq(add(P[j],P[j].map(x=>-x)),[0n]),"free plus");ok(eq(add(M[j],M[j].map(x=>-x)),[0n]),"free minus")}checks.unpaired_nuisance++}
 return {schema:"EM_R628_PAIRED_BRC_EXACT_V1",date:"2026-11-08",frozen_R462:"18783e01e3646c72b7aab3b16d3f565e83e6446f",source_K_blob:"7fa7a762f758b30c6090468ac43487daa34abad8",delta_orders:orders,delta_leading:c.map(String),D5:D[4].map(String),D6:D[5].map(String),checks,total:Object.values(checks).reduce((x,y)=>x+y,0),arithmetic:"BigInt exact integer polynomials",status:"AUTHOR_SIDE_UNREVIEWED",marker:"R628_PAIRED_BRC_IDENTIFIABILITY_EXACT_PASS"};
}
if(typeof require==="function"&&require.main===module)console.log(JSON.stringify(run(),null,2));
