// EC49EH independent JavaScript BigInt / modular finite verifier.
'use strict';
const OP={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const ATOMS=[['N',0],['N',1],['N',2],['A',0],['A',2],['B',0],['B',1],['AB',0],['BA',0]];
const BUCKETS=['N','A','B','AB','BA'];
const MOD=1000003;
function check(x,msg){if(!x)throw Error(msg);}
function nat(w){return [...w].flatMap(c=>OP[c]);}
function count(p){return Array.from({length:6},(_,i)=>p.filter(v=>v===i+1).length);}
function update(p,s='N',last=0){for(let v of p){let A=last===1&&v===2,B=last===2&&v===1;
if(s==='N')s=A?'A':B?'B':'N';else if(s==='A'&&B)s='AB';else if(s==='B'&&A)s='BA';last=v;}return s;}
function trans(w){return ATOMS.map(([s,last])=>BUCKETS.indexOf(update(nat(w),s,last)));}
function cols(t){return BUCKETS.map((_,j)=>t.reduce((a,v,i)=>a|(v===j?1<<i:0),0));}
function pow(a,n){let o=1;for(;n;n=Math.floor(n/2),a=a*a%MOD)if(n%2)o=o*a%MOD;return o;}
function rank(c){let b=new Map();for(let mask of c){let x=Array.from({length:9},(_,i)=>(mask>>i)&1);
for(let i=0;i<9;i++){if(!x[i])continue;if(b.has(i)){let q=b.get(i),k=x[i];for(let j=i;j<9;j++)x[j]=((x[j]-k*q[j])%MOD+MOD)%MOD;}else{let d=pow(x[i],MOD-2);b.set(i,x.map(z=>z*d%MOD));break;}}}return b.size;}
function pref(w){let p=nat(w),z=[];for(let i=1;i<=p.length;i++)z.push(p.slice(0,i).join(','));return z;}
function cost(words){return new Set(words.flatMap(pref)).size;}
function complete(h){let ans=new Map();function rec(w){if(w.length===h){let p=nat(w),d=Array.from({length:6},(_,i)=>p.filter(x=>x===i+1).length-p.filter(x=>x===-(i+1)).length);
if(d.join(',')!=='2,0,0,0,0,0')return;let k=count(p).join(',');if(!ans.has(k))ans.set(k,[]);ans.get(k).push(w);return;}
for(let a of 'acdefg')rec(w+a);}rec('');return ans;}
const base=['ce','de','ec','ed'];check(cost(base)===28,'base cost');
const g2=complete(2),g3=complete(3);check([...g2.values()].reduce((a,b)=>a+b.length,0)===8,'h2 total');
check([...g3.values()].reduce((a,b)=>a+b.length,0)===51,'h3 total');
let mins=[],num=0,matches=[];
for(let [fiber,ws] of g3){let best=Infinity;
for(let mask=1;mask<(1<<ws.length);mask++){num++;let s=ws.filter((w,i)=>mask>>i&1);
if(rank(s.flatMap(w=>cols(trans(w))))<9)continue;
let v=cost(base.concat(s));if(v<best)best=v;
if(v===36)matches.push({fiber,words:s});}
mins.push({fiber,cost:Number.isFinite(best)?best:null});}
let opt=Math.min(...mins.map(x=>x.cost??Infinity));check(opt===36,'h3 lower');check(matches.length===2,'h3 minimizer count');
for(let H=3;H<=32;H++){
let f='feg'+'f'.repeat(H-3),g='gef'+'f'.repeat(H-3);
check(count(nat(f)).join(',')===count(nat(g)).join(','),'equal positive count');
check(count(nat(f)).join(',')===`${H},1,1,0,0,0`,'p formula');
check(rank([f,g].flatMap(w=>cols(trans(w))))===9,'rank 9');
let all=base.slice();for(let h=3;h<=H;h++)all.push('feg'+'f'.repeat(h-3),'gef'+'f'.repeat(h-3));
check(cost(all)===4*H+30,'trie formula');
let words=base.map(w=>w+'f'.repeat(H-2));check(words.every(w=>count(nat(w)).join(',')===count(nat(words[0])).join(',')),'4-word fiber');
check(rank(words.flatMap(w=>cols(trans(w))))===9,'4-word rank');
let a=[];for(let h=2;h<=H;h++)a.push(...base.map(w=>w+'f'.repeat(h-2)));
check(cost(a)===8*H+12,'four tree bound');}
const out={status:'PASS',language:'Independent JavaScript',h2_return_count:8,h3_return_count:51,h3_masks:num,h3_min:opt,h3_fiber_minima:mins,h3_minimizers:matches,analytic_construction_checked_H:32};
console.log(JSON.stringify(out,null,2));
