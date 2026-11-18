/* EC49AV exact integer-cofactor / BigInt fractional certificate; run with node VERIFY_EC49AV.js. */
function verifyEC49AV(){
const S=[];for(let a=0;a<11;a++)for(let b=a+1;b<12;b++)for(let c=b+1;c<13;c++)for(let d=c+1;d<14;d++)for(let e=d+1;e<15;e++)S.push([a,b,c,d,e]);
const aCost=[1,1,2,2,0], top=Array.from({length:4},()=>Array(16).fill(0));
for(let i=0;i<15;i++){top[Math.floor(i/5)][i]=1;top[3][i]=aCost[i%5];}
[16,16,16,43].forEach((v,i)=>top[i][15]=v);
const permutations=[];
function perm(p){if(p.length===4){let inv=0;for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)if(p[i]>p[j])inv++;permutations.push([p.slice(),inv%2?-1:1]);return;}for(let i=0;i<4;i++)if(!p.includes(i))perm([...p,i]);}perm([]);
const cache=new Map();
function det4(ids){const key=ids.join(",");if(cache.has(key))return cache.get(key);let d=0;for(const [p,sgn] of permutations)d+=sgn*top[0][ids[p[0]]]*top[1][ids[p[1]]]*top[2][ids[p[2]]]*top[3][ids[p[3]]];cache.set(key,d);return d;}
const cof=[],numCof=[];
for(const support of S){const c=Array(5).fill(0),n=Array.from({length:5},()=>Array(5).fill(0));for(let k=0;k<5;k++)c[k]=(k%2?-1:1)*det4(support.filter((_,i)=>i!==k));for(let j=0;j<5;j++){const t=support.slice();t[j]=15;for(let k=0;k<5;k++)if(k!==j)n[j][k]=(k%2?-1:1)*det4(t.filter((_,i)=>i!==k));}cof.push(c);numCof.push(n);}
const abs=a=>a<0n?-a:a;
function gcd(a,b){a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t;}return a;}
function Q(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return [a/g,b/g];}
const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const sub=(a,b)=>Q(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
const div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
const cmp=(a,b)=>a[0]*b[1]-b[0]*a[1];
const fmt=a=>a[1]===1n?String(a[0]):String(a[0])+"/"+String(a[1]);
const tick=[[4,26],[15,15],[26,4]],z=Q(0),target=Q(14401,123840);
function score(x,mask){let H=z;for(let c=0;c<4;c++)for(let u=0;u<2;u++)if((mask>>(2*c+u))&1){const q=[0,1,2].map(w=>mul(x[5*w+c],Q(tick[w][u],90)));const T=add(add(q[0],q[1]),q[2]);for(let w=0;w<3;w++){const d=div(sub(mul(Q(43),q[w]),mul(Q(16),T)),Q(172));if(d[0]>0n)H=add(H,d);}}return H;}
let feasible=0,nonsing=0,ties=0,best=Q(-1),rankDeficient=0,witness=null;const ux=new Set();
for(let mask=1;mask<256;mask++){
const last=Array(15).fill(0);const c0=[4,15,26],c1=[26,15,4];
for(let w=0;w<3;w++)for(let c=0;c<4;c++)last[5*w+c]=c0[w]*((mask>>(2*c))&1)+c1[w]*((mask>>(2*c+1))&1);
let bases=0;
for(let si=0;si<S.length;si++){const row=S[si].map(id=>last[id]),C=cof[si],N=numCof[si];let D=0;for(let k=0;k<5;k++)D+=row[k]*C[k];if(!D)continue;nonsing++;bases++;const num=[];let ok=true;for(let j=0;j<5;j++){let v=1170*C[j];for(let k=0;k<5;k++)v+=row[k]*N[j][k];if(v*D<0){ok=false;break;}num.push(v);}if(!ok)continue;feasible++;
const x=Array(15).fill(z);for(let j=0;j<5;j++)x[S[si][j]]=Q(num[j],16*D);ux.add(x.map(fmt).join(","));
const val=score(x,mask);if(cmp(val,best)>0n){best=val;ties=0;witness={mask,support:S[si],x:x.map(fmt)};}if(cmp(val,best)===0n)ties++;if(cmp(val,target)>0n)throw Error("an exact better deterministic policy was found");}
if(!bases)rankDeficient++;
}
const W=[Q(0),Q(3,16),Q(1,4),Q(0),Q(9,16),Q(1),Q(0),Q(0),Q(0),Q(0),Q(0),Q(1),Q(0),Q(0),Q(0)];
if(cmp(best,target)!==0n||cmp(score(W,63),target)!==0n||nonsing!==445440||feasible!==6240||S.length!==3003||rankDeficient!==0||ux.size!==852||ties!==32)throw Error(JSON.stringify({best:fmt(best),actualW:fmt(score(W,63)),nonsing,feasible,supports:S.length,rankDeficient,unique:ux.size,ties}));
return {schema:"EC49AV_DETERMINISTIC_PURCHASE_CERT_V1",status:"AUTHOR_EXACT_BIGINT_CHECK_PASS_UNREVIEWED_NOT_ADMITTED",model:"auxiliary 18+18-leaf positive probability BRC",eta:"11/30",C1:"43/48",C2:"13/16",k:"177/172",binary_purchase_masks_valid:255,first_stage_five_support_sets:3003,nonsingular_bases:nonsing,feasible_basic_pairs:feasible,distinct_first_stage_rational_points:ux.size,exact_deterministic_purchase_max:fmt(best),maximizer_basic_pairs:ties,explicit_prior_witness_H:fmt(score(W,63)),example_maximizer:witness,scope:"All real first-stage allocations with deterministic observation-only purchase; global fractional-purchase optimum remains open."};
}
console.log(JSON.stringify(verifyEC49AV(), null, 2));
