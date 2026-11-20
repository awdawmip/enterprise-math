'use strict';
const D=Array.from({length:12},(_,i)=>i);
function words(alpha,n){let a=[[]];for(let i=0;i<n;i++){let next=[];for(let w of a)for(let d of alpha)next.push([...w,d]);a=next;}return a;}

function obs(P,Q){const endpoint=w=>{const s=[0,0,0,0,0,0];for(let d of w)s[d>>1]+=d%2?-1:1;return s.join(',');};const hist=w=>{const h=new Map();for(let k=1;k<w.length;k++){const t=12*w[k-1]+w[k];h.set(t,(h.get(t)||0)+1);}return [...h].sort((x,y)=>x[0]-y[0]).map(([k,v])=>k+":"+v).join(',');};let k=0;for(let i=0;i<Math.min(P.length,Q.length);i++)if(P[i]===Q[i])k++;return [P.length,Q.length,endpoint(P),endpoint(Q),hist(P),hist(Q),k].join('|');}

function tuple(P,Q,p,r){const n=Q.length;return Q.slice(n-p-1).join(',')+'|'+P.slice(n-p,n+r).join(',');}

function ops(p,r){const z=[];function go(s,pc,ac){z.push(s);if(pc<p)go(s.concat([[-1]]),pc+1,ac);if(ac<r)for(let x of D)go(s.concat([[x]]),pc,ac+1);}go([],0,0);return z;}

function trace(P,Q,op){const q=Q.slice(),out=[];for(const [x] of op){if(x===-1){if(!q.length)return out.concat(['ILLEGAL']).join('::');q.pop();}else q.push(x);out.push(obs(P,q));}return out.join('::');}

function exactCheck(p,r,n,m,alpha){const fs=ops(p,r),groups=new Map();let same=0,different=0,groupsCollision=0,steps=0;
for(const P of words(alpha,m))for(const Q of words(alpha,n)){const o=obs(P,Q),arr=groups.get(o)||[];arr.push({P,Q,t:tuple(P,Q,p,r)});groups.set(o,arr);}
for(const arr of groups.values()){if(arr.length<2)continue;groupsCollision++;for(let i=0;i<arr.length;i++)for(let j=i+1;j<arr.length;j++){const a=arr[i],b=arr[j],eq=a.t===b.t;let diff=false;for(const op of fs){steps++;if(trace(a.P,a.Q,op)!==trace(b.P,b.Q,op)){diff=true;break;}}if(eq===diff)throw Error('quotient error '+JSON.stringify({p,r,n,m,a,b}));if(eq)same++;else different++;}}
return {p,r,n,m,alphabet:alpha,initial_histories:alpha.length**(n+m),observed_fibers:groups.size,nontrivial_fibers:groupsCollision,pairs_same_tuple:same,pairs_distinct_tuple:different,legal_operation_words:fs.length,paired_full_trace_checks:steps};}

function family(p,r){const L=p+r,n=p+3,m=5*L+9,M=3*L+3,R=L+1,q=Array(n).fill(2),all=[];for(let mask=0;mask<2**L;mask++){const w=Array.from({length:L},(_,i)=>(mask>>i)&1);const b=w.filter(x=>x===1).length,rr=w.filter((x,i)=>x===1&&(i===0||w[i-1]===0)).length,h=R-rr,z=M-b,t=2+b+rr;if(!(h>=1&&z>=h))throw Error('bad');const P=[0,0,0,...w,0,...Array(z-h+1).fill(1)];for(let i=1;i<h;i++)P.push(0,1);P.push(...Array(t).fill(0));if(P.length!==m)throw Error('length mismatch');all.push({P,w});}
const o=obs(all[0].P,q),sigs=new Set();for(const {P,w} of all){if(obs(P,q)!==o)throw Error('wrong observer');const hits=[];for(let j=0;j<=p;j++)for(let k=1;k<=r;k++){const at=n-j+k;const pop=q.slice(0,q.length-j);const pre=pop.concat(Array(k-1).fill(0)),post=pre.concat([0]);const b=Number(obs(P,pre).split('|').at(-1)),a=Number(obs(P,post).split('|').at(-1));if(a-b!==+(P[at-1]===0))throw Error('probe wrong');hits.push(`${at}:${a-b}`);}
const seen=new Map(hits.map(x=>x.split(':')));let recovered='';for(let at=4;at<=3+L;at++)recovered+=seen.get(String(at))==='1'?'0':'1';if(recovered!==w.join(''))throw Error('cannot decode');sigs.add(recovered);}
return {p,r,bit_length:L,history_count:all.length,distinct_traces:sigs.size,n,m};}

function sameTupleWitnesses(){const U0=[0,0,0,1,0],U1=[0,1,0,0,0],p=1,r=2;
const pairs=[
{kind:"P-hidden-Euler-switch",P0:[0,0,0,0,0,...U0],P1:[0,0,0,0,0,...U1],Q0:[2,2,2],Q1:[2,2,2]},
{kind:"Q-hidden-Euler-switch",P0:Array(9).fill(2),P1:Array(9).fill(2),Q0:[...U0,0,0],Q1:[...U1,0,0]}
];return pairs.map(v=>{if(obs(v.P0,v.Q0)!==obs(v.P1,v.Q1))throw Error("initial observer "+v.kind);if(tuple(v.P0,v.Q0,p,r)!==tuple(v.P1,v.Q1,p,r))throw Error("tuple "+v.kind);const f=ops(p,r);for(const w of f)if(trace(v.P0,v.Q0,w)!==trace(v.P1,v.Q1,w))throw Error("future "+v.kind);return {kind:v.kind,operation_words_compared:f.length,complete_traces_equal:true};});}

function verify(){const cases=[[0,2,2,4,[0,1,2]],[1,2,3,5,[0,1,2]],[2,2,3,5,[0,1]],[2,2,4,6,[0,1]]];return {status:"STAGE431B_GENERAL_POP_APPEND_QUOTIENT_EXACT_PASS",exact_fiber_checks:cases.map(x=>exactCheck(...x)),same_tuple_examples:sameTupleWitnesses(),lower_bound_families:[[0,2],[1,2],[2,2],[3,2],[2,3],[4,2]].map(x=>family(...x)),scope:"All twelve future native append labels; all legal operation words up to each stated budget; finite initial subalphabets. General theorem and lower bound proved symbolically."};}
if (typeof require!=='undefined' && require.main===module) console.log(JSON.stringify(verify(),null,2));
