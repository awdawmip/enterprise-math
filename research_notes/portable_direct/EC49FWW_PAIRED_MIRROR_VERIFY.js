#!/usr/bin/env node
// EC49FWW exact integer verifier; Node.js; no network or external dependencies.
const result=(function verifyPaired(){
const mod=(x,m)=>(x%m+m)%m,gcd=(a,b)=>b?gcd(b,a%b):a,inv=(a,m)=>{for(let z=1;z<m;z++)if(mod(a*z,m)===1)return z;throw Error("inv")};
const p10=(H,N)=>{const h=mod(H,10),n=mod(N,10);if(h%5===0&&n%5===0)return false;const s=h%5===0?5:mod(n*inv(h,5),5);return [[[3],[0,3,4,5]],[[2,3,4,5],[2,3]]][h%2][n%2].includes(s)};
const bit=(u,j)=>(u>>mod(j,10))&1;
const masks=new Set();let dirs=0;
for(let a=0;a<10;a++)for(let y=0;y<10;y++){if(gcd(gcd(a,y),10)!==1)continue;dirs++;let root=null;for(let h=0;h<10&&root===null;h++)for(let n=0;n<10;n++)if(mod(y*h-a*n+1,10)===0){root=[h,n];break}if(!root)throw Error("root");let u=0;for(let t=0;t<10;t++)if(p10(root[0]+a*t,root[1]+y*t))u|=1<<t;masks.add(u)}
if(dirs!==72||masks.size!==50)throw Error("frozen 72/50 mismatch");
const crt=Array.from({length:10},()=>Array(11).fill(-1));for(let t=0;t<110;t++)crt[t%10][t%11]=t;
const worst=(a,b)=>{const A=a.reduce((p,q)=>p+q,0);return Math.min(2*A,2*(A+b)-Math.max(...a))};
const central=[];
for(let r=1;r<=20;r++){let best=null;for(let a0=0;a0<=2;a0++)for(let a1=0;a1<=2;a1++)for(let a2=0;a2<=2;a2++)for(let a3=0;a3<=2;a3++)for(let a4=0;a4<=2;a4++)for(let b=0;b<=2;b++){const a=[a0,a1,a2,a3,a4],m=b+a.reduce((p,q)=>p+q,0),d=worst(a,b);if(d<r)continue;const x={m,b,a,d};if(!best||m<best.m||(m===best.m&&b<best.b)||(m===best.m&&b===best.b&&d>best.d))best=x}const h=r<=10?r+1:r+2;if(best.m!==Math.ceil(h/2))throw Error("central minimum "+r);central.push(best)}
const layouts=[];
for(let r=1;r<=20;r++){const h=r<=10?r+1:r+2,acts=[];for(const i of [1,2]){for(let c=0;c<Math.min(h,11);c++)acts.push(crt[i][c]);for(let c=0;c<Math.max(0,h-11);c++)acts.push(crt[i+5][c])}const v=central[r-1];for(let c=1;c<=5;c++){if(v.a[c-1]>0)acts.push(crt[0][c]);if(v.a[c-1]>1)acts.push(crt[5][c])}if(v.b>0)acts.push(crt[0][0]);if(v.b>1)acts.push(crt[5][0]);if(new Set(acts).size!==acts.length||acts.length!==Math.ceil(5*h/2))throw Error("layout "+r);layouts.push(acts)}
const hist={};let states=0,tests=0;const minima=Array(20).fill(Infinity);
for(const u of masks){let d=0;for(let t=0;t<10;t++)d+=bit(u,t)!==bit(u,t-5)?1:0;hist[d]=(hist[d]||0)+1;for(let hole=-1;hole<11;hole++)for(let s=0;s<110;s++){const gap=new Uint8Array(110);for(let t=0;t<110;t++)gap[t]=(bit(u,t-s)!==bit(u,t-s-5)&&(hole<0||mod(t-s,11)!==hole))?1:0;states++;for(let r=1;r<=20;r++){let n=0;for(const t of layouts[r-1])n+=gap[t]+gap[mod(-t,110)];if(n<r)throw Error("actual gap "+[u,hole,s,r,n]);minima[r-1]=Math.min(minima[r-1],n);tests++}}}
if([2,4,6,8].some((x,i)=>hist[x]!==[10,26,10,4][i])||Object.keys(hist).length!==4)throw Error("gap histogram");
if(minima.some((v,i)=>v!==i+1))throw Error("not sharp");
const bruteC=Array(20).fill(Infinity);
for(let bits=0;bits<4096;bits++){const a=Array.from({length:5},(_,c)=>((bits>>(2*c))&1)+((bits>>(2*c+1))&1));const b=((bits>>10)&1)+((bits>>11)&1),m=a.reduce((p,q)=>p+q,0)+b,d=worst(a,b);for(let r=1;r<=Math.min(d,20);r++)bruteC[r-1]=Math.min(bruteC[r-1],m)}
const bruteS=Array(20).fill(Infinity);
for(let state=0;state<177147;state++){let z=state,m=0,mx=0;for(let c=0;c<11;c++){let q=z%3;z=(z-q)/3;m+=q;mx=Math.max(mx,q)}for(let r=1;r<=Math.min(m-mx,20);r++)bruteS[r-1]=Math.min(bruteS[r-1],m)}
for(let r=1;r<=20;r++){const h=r<=10?r+1:r+2;if(bruteC[r-1]!==Math.ceil(h/2)||bruteS[r-1]!==h)throw Error("finite exhaustive optimality "+r)}
return {status:"ALL PASS",frozen_pin:"BRC16943",model:"known reference, universal preinstalled paired left/right mirror probes, opposite shared phase drift, two separately counted channel reads per activation",directions:dirs,distinct_masks:masks.size,states_tested:states,layout_distance_checks:tests,central_orbit_subsets_exhausted:4096,swapped_block_column_occupancies_exhausted:177147,gap_histogram:hist,scope_r:[1,20],minimum_observed_distances:minima,optimal_activations:Array.from({length:20},(_,i)=>{const r=i+1,h=r<=10?r+1:r+2;return {r,unpaired_sites:5*h,paired_activations:layouts[i].length,each_swapped_block:h,central_block:central[i].m}}),independent_review:false};
})();
console.log(JSON.stringify(result,null,2));
