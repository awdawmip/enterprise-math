'use strict';
// R319. Exact integer validation directly from the original ordered six-edge BRC recurrence.
const N=192;
const choose=(n,k)=>{if(n<0||k<0||k>n)return 0n;let v=1n;for(let j=1;j<=k;j++)v=v*BigInt(n-j+1)/BigInt(j);return v;};
function trim(x){while(x.length>1&&x[x.length-1]===0n)x.pop();return x;}
function add(x,y,sgn=1n){let z=Array(Math.max(x.length,y.length)).fill(0n);for(let i=0;i<x.length;i++)z[i]+=x[i];for(let i=0;i<y.length;i++)z[i]+=sgn*y[i];return trim(z);}
function mul(x,y){let z=Array(x.length+y.length-1).fill(0n);for(let i=0;i<x.length;i++)for(let j=0;j<y.length;j++)z[i+j]+=x[i]*y[j];return trim(z);}
const minus=r=>Array.from({length:r+1},(_,j)=>(j%2?-1n:1n)*choose(r,j));
const num=i=>[0n,-choose(3,i-1),-choose(6,i-1),choose(8,i-2)];
const delta=i=>[0n,-choose(4,i)+choose(2,i-1),choose(5,i-1)-choose(5,i-2),choose(7,i-2),-choose(9,i-3)];
const moment=(p,r)=>{let v=0n;for(let j=r;j<p.length;j++){let f=1n;for(let k=0;k<r;k++)f*=BigInt(j-k);v+=p[j]*f;}return v;};
const p7=s=>243n*s**7n-2268n*s**6n-38052n*s**5n+780850n*s**4n-5472663n*s**3n+16271178n*s*s-1634008n*s-78016960n;
const d7=s=>243n*s**6n-2673n*s**5n-21105n*s**4n+492865n*s**3n-3063498n*s*s+7465528n*s-3456320n;
const q7=s=>15625n*s**7n-175000n*s**6n+910000n*s**5n-3151750n*s**4n+2148895n*s**3n+1397438n*s*s+28570632n*s+24865344n;
const shift=[15625n,590625n,9638125n,87651375n,472346770n,1453381608n,2184880704n,1036707840n];
let poly=[[1n]], prev7=null, checks={degree:0, moment7:0, recurrence7:0, newton7_direct:0, newton7_recovery:0, shifted_identity:0, strict_bound:0},samples={};
for(let t=0;t<=N;t++){
 if(t>0){let m=mul(num(t),minus(t));for(let i=1;i<=Math.min(t,12);i++)m=add(m,mul(mul(delta(i),poly[t-i]),minus(i-1)),-1n);poly.push(m);}
 const x=poly[t],s=BigInt(t),pow=2n**s;
 if(x.length-1>2*t+1)throw Error('degree bound fails s='+t);checks.degree++;
 if(t>=7){
   const ms=Array.from({length:8},(_,i)=>moment(x,i));
   if(16384n*ms[7]!==9n*pow*p7(s))throw Error('m7 formula s='+t);checks.moment7++;
   if(t>=8){if(16384n*(ms[7]-2n*prev7)!==63n*pow*d7(s))throw Error('m7 diff s='+t);checks.recurrence7++;}
   let a=0n;for(let j=0;j<x.length;j++)a+=x[j]*choose(2*t+1-j,7);
   if(16515072n*a!==pow*q7(s))throw Error('Newton q7 formula s='+t);checks.newton7_direct++;
   // Independent falling-factorial moment recovery, clear denominators 7!.
   let recovered=0n,fac=1n;
   for(let r=0;r<=7;r++){
      if(r)fac*=BigInt(r);
      let ff=1n;for(let j=0;j<7-r;j++)ff*=BigInt(2*t+1-r-j);
      recovered+=(r%2?-1n:1n)*choose(7,r)*ff*ms[r];
   }
   if(recovered!==5040n*a)throw Error('moment recovery s='+t);checks.newton7_recovery++;
   const u=s-7n;let vv=0n;for(const c of shift)vv=vv*u+c;
   if(vv!==q7(s))throw Error('shift identity s='+t);checks.shifted_identity++;
   if(128n*a<8035n*pow)throw Error('positive bound s='+t);checks.strict_bound++;
   if([7,8,9,10,32,128,192].includes(t))samples[t]={moment7:String(ms[7]),newton_q7:String(a)};
   prev7=ms[7];
 }
}
const output={schema:'ENTERPRISE_MATH_R319_EXACT_EVIDENCE_V1',status:'PASS',source:'R313/R318 ordered six-edge BRC polynomial recurrence',arithmetic:'Node.js BigInt exact integer',range_s:[0,N],checks,samples,bound:'for every integer s>=7, a_(s,s-7)>=8035/128 * 2^s >0; equality at s=7',scope:'Numerical checks only through s=192. Universal claim uses separate symbolic recurrence/induction and coefficient-positivity proof. Not native Source acceptance or Driver review.'};
if(typeof process!=='undefined')process.stdout.write(JSON.stringify(output,null,2)+'\n');
