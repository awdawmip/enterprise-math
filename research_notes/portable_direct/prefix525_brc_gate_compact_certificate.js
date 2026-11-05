// Exact signed-X6 four-STAR BRC/gate certificate; all arithmetic is integer.
const STARS=[[0,2,5],[0,3,4],[1,2,4],[1,3,5]];
function near(j,c){return STARS[j].filter(a=>a!==Math.abs(c)-1).map(a=>-Math.sign(c)*(a+1));}
function succ(s){let [j,p,c]=s,k=STARS.findIndex((v,i)=>i!==j&&v.includes(Math.abs(c)-1));return [...near(j,c).filter(v=>v!==p).map(v=>[j,c,v]),...near(k,c).map(v=>[k,c,v])];}
let S=[];for(let j=0;j<4;j++)for(let a of STARS[j])for(let sign of [-1,1])for(let p of near(j,sign*(a+1)))S.push([j,p,sign*(a+1)]);
const key=s=>s.join(',');let I=new Map(S.map((s,i)=>[key(s),i]));let NEXT=S.map(s=>succ(s).map(t=>I.get(key(t))));if(S.length!==48||NEXT.some(v=>v.length!==3))throw Error('states');
const T=I.get('0,1,-3');if(NEXT[T].includes(T))throw Error('target self loop');
const sigma=(c,a)=>Math.abs(c)===a?Math.sign(c):0;
const kval=(s,t,a)=>Number(Math.abs(S[s][2])===a)+Number(Math.abs(S[t][2])===a);
const step=(s,t,b)=>b===0?[-S[s][2],S[t][2]]:[S[t][2],-S[s][2]];
let checked=0;
for(let s=0;s<48;s++)for(let t of NEXT[s])for(let b of [0,1]){
 let w=step(s,t,b);
 for(let a=1;a<=6;a++){
  let n=w.filter(x=>Math.abs(x)===a).length,y=w.filter(x=>Math.abs(x)===a).reduce((v,x)=>v+Math.sign(x),0);
  if(n!==kval(s,t,a)||y!==sigma(S[t][2],a)-sigma(S[s][2],a))throw Error('local');checked++;
 }
}
const k=(a,b,c,d)=>`${a},${b},${c},${d}`;
const decode=x=>x.split(',').map(Number);
function add(o,k,n){o.set(k,(o.get(k)||0)+n);if(o.get(k)===0)o.delete(k);}
function W(f,axis,mult){let out=new Map();for(let [kk,n] of f){let [a,s,K,H]=decode(kk);for(let t of NEXT[s])add(out,k(a,t,K+kval(s,t,axis),H),mult*n);}return out;}
function compact(depth,axis){let f0=new Map(S.map((s,i)=>[k(i,i,0,0),1]));if(depth===0)return f0;let p0=f0,p1=W(f0,axis,2);for(let d=2;d<=depth;d++){let out=W(p1,axis,2);for(let [kk,n] of p0){let [a,r,K,H]=decode(kk);for(let s of NEXT[r])if(NEXT[s].includes(T)){let X=K+kval(r,s,axis)+kval(s,T,axis);add(out,k(a,T,X,H+1),n);add(out,k(a,T,X,H),-n);}}for(let n of out.values())if(n<0)throw Error('negative');p0=p1;p1=out;}return p1;}
function control(depth,axis){let f=new Map(S.map((s,i)=>[`${i},${i},2,0,0`,1]));for(let i=1;i<=depth;i++){let g=new Map();for(let [kk,n] of f){let [a,s,prev,K,H]=decode(kk);for(let t of NEXT[s])for(let b of [0,1]){let h=H+Number(i>=2&&prev===0&&b===0&&t===T);add(g,`${a},${t},${b},${K+kval(s,t,axis)},${h}`,n);}}f=g;}let out=new Map();for(let [kk,n] of f){let [a,t,b,K,H]=decode(kk);add(out,k(a,t,K,H),n);}return out;}
let coeff=0,hist=[];
for(let d=0;d<=5;d++)for(let a=1;a<=6;a++){
 let x=control(d,a),y=compact(d,a);if(x.size!==y.size)throw Error('size');for(let [k,n] of x)if(y.get(k)!==n)throw Error('transfer');coeff+=x.size;
 if(a===1){let counts=new Map(),pair=new Map();for(let [kk,n] of y){let [start,end,K,H]=decode(kk);let delta=sigma(S[end][2],1)-sigma(S[start][2],1);if(K<Math.abs(delta)||(K-Math.abs(delta))%2)throw Error('parity');let p=(K-Math.abs(delta))/2;add(counts,String(H),n);add(pair,`${H},${p}`,n);}hist.push({depth:d,hits:Object.fromEntries(counts),jointHp1:Object.fromEntries(pair)});}
}
let scans=0;const color=c=>c===1?'a':c===-1?'A':Math.abs(c)===3?'c':'_';
const hits=w=>{let s=w.map(color).join(''),v=0;for(let i=0;i+3<=s.length;i++)if(s.slice(i,i+3)==='aAc')v++;return v;};
function visit(s,word,prev,h,d,max){if(d===max){if(h!==hits(word))throw Error('primitive gate');scans++;return;}for(let t of NEXT[s])for(let b of [0,1]){let next=word.concat(step(s,t,b)),h2=h+Number(d>=1&&prev===0&&b===0&&t===T);visit(t,next,b,h2,d+1,max);}}
for(let d=0;d<=4;d++)for(let s=0;s<48;s++)visit(s,[],2,0,0,d);
const output={verdict:'ALL_CHECKS_PASS',model:'PREFIX-518/524 four-STAR signed-X6',phaseStates:48,axisChecks:checked,weightedTransferCoefficientChecks:coeff,macroDepthMax:5,primitiveHistoriesScanned:scans,gateHistograms:hist,formula:'f_d=2 W f_(d-1)+(z-1)e_T e_T^t W^2 f_(d-2)',brc:'p_a=(K_a-|sigma_a(c_d)-sigma_a(c_0)|)/2',scope:'exact integer finite verification of all-length algebraic proof; author run'};
console.log(JSON.stringify(output,null,2));
