'use strict';
function verifyR318(){
const N=192;
function C(n,k){if(n<0||k<0||k>n)return 0n;let a=1n;for(let i=1;i<=k;i++)a=a*BigInt(n-i+1)/BigInt(i);return a;}
function add(a,b,sgn=1n){const x=Array(Math.max(a.length,b.length)).fill(0n);for(let i=0;i<a.length;i++)x[i]+=a[i];for(let i=0;i<b.length;i++)x[i]+=sgn*b[i];while(x.length>1&&x[x.length-1]===0n)x.pop();return x;}
function mul(a,b){const x=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)if(a[i]!==0n)for(let j=0;j<b.length;j++)if(b[j]!==0n)x[i+j]+=a[i]*b[j];while(x.length>1&&x[x.length-1]===0n)x.pop();return x;}
const powMinus=r=>Array.from({length:r+1},(_,j)=>(j%2?-1n:1n)*C(r,j));
const num=i=>[0n,-C(3,i-1),-C(6,i-1),C(8,i-2)];
const delta=i=>[0n,-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3)];
const M=[[1n]],counts={degree:0,prior_moments_0_5:0,moment6:0,moment6_difference:0,newton_q6:0,moment_recovery:0,positive_bound:0},samples={};
const m6poly=S=>243n*S**6n-1377n*S**5n-26055n*S**4n+348565n*S**3n-1709628n*S*S+3668252n*S-2031840n;
const diffpoly=S=>243n*S**5n-1755n*S**4n-14265n*S**3n+197435n*S*S-760138n*S+958480n;
const q6poly=S=>3125n*S**6n-24375n*S**5n+77375n*S**4n-215325n*S**3n-41188n*S*S+333444n*S+1048032n;
function moment(p,r){let sum=0n;for(let j=r;j<p.length;j++){let ff=1n;for(let v=0;v<r;v++)ff*=BigInt(j-v);sum+=p[j]*ff;}return sum;}
let prev6=null;
for(let n=0;n<=N;n++){
if(n>0){let x=mul(num(n),powMinus(n));for(let i=1;i<=Math.min(n,12);i++)x=add(x,mul(mul(delta(i),M[n-i]),powMinus(i-1)),-1n);M.push(x);}
const poly=M[n],S=BigInt(n),pow=2n**S;if(poly.length-1>2*n+1)throw Error('degree s='+n);counts.degree++;
const m=Array.from({length:7},(_,r)=>moment(poly,r));
const eq=(label,l,r)=>{if(l!==r)throw Error(label+' s='+n+' '+l+' != '+r);};
eq('m0',m[0],pow);counts.prior_moments_0_5++;
if(n>=1){eq('m1',4n*m[1],3n*(S+1n)*pow);counts.prior_moments_0_5++;}
if(n>=2){eq('m2',16n*m[2],(9n*S*S+11n*S-26n)*pow);counts.prior_moments_0_5++;}
if(n>=3){eq('m3',64n*m[3],3n*(9n*S**3n+6n*S*S-119n*S+220n)*pow);counts.prior_moments_0_5++;}
if(n>=4){eq('m4',256n*m[4],3n*(27n*S**4n-18n*S**3n-911n*S*S+4070n*S-6184n)*pow);counts.prior_moments_0_5++;}
if(n>=5){eq('m5',1024n*m[5],3n*(81n*S**5n-225n*S**4n-5295n*S**3n+43385n*S*S-134746n*S+162800n)*pow);counts.prior_moments_0_5++;}
if(n>=6){
eq('m6',4096n*m[6],3n*pow*m6poly(S));counts.moment6++;
if(n>=7){eq('m6 difference',2048n*(m[6]-2n*prev6),9n*pow*diffpoly(S));counts.moment6_difference++;}
let a=0n;for(let j=0;j<poly.length;j++)a+=poly[j]*C(2*n+1-j,6);
eq('q6',589824n*a,pow*q6poly(S));counts.newton_q6++;
const rec=8n*S*(S-1n)*(S-2n)*(2n*S-3n)*(2n*S-1n)*(2n*S+1n)*m[0]
-48n*S*(S-2n)*(S-1n)*(2n*S-3n)*(2n*S-1n)*m[1]
+60n*(S-2n)*(S-1n)*(2n*S-3n)*(2n*S-1n)*m[2]
-80n*(S-2n)*(S-1n)*(2n*S-3n)*m[3]
+30n*(S-2n)*(2n*S-3n)*m[4]-12n*(S-2n)*m[5]+m[6];
eq('recovery',720n*a,rec);counts.moment_recovery++;
if(!(32n*a>=629n*pow))throw Error('bound s='+n);counts.positive_bound++;
if([6,7,8,9,10,128,192].includes(n))samples[n]={moment6:String(m[6]),newton_q6:String(a)};
}prev6=m[6];}
return {schema:'ENTERPRISE_MATH_R318_EXACT_EVIDENCE_V1',status:'PASS',arithmetic:'JavaScript BigInt, exact integer',tested_s_range:[0,N],counts,samples,theorem:'For every integer s>=6, a_(s,s-6)=2^s*(3125s^6-24375s^5+77375s^4-215325s^3-41188s^2+333444s+1048032)/589824 >= (629/32)*2^s>0',caveats:'Finite computation to 192; unbounded theorem separately follows symbolic differentiation recurrence, polynomial finite difference and shifted-positive-coefficient proof. No native independent Driver review or P000 physical interpretation.'};
}
const evidence=verifyR318();
if(typeof process!=='undefined'&&process.stdout)process.stdout.write(JSON.stringify(evidence,null,2)+'\n');
