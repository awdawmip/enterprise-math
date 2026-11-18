'use strict';
// Independent iterative-array min-plus knapsack on an oriented six-axis trie.
const A='acdefg';
const P={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]];
const S=[0,0,4,1,16,32,8,2,0];
const BIT={1:1,2:2,4:4,8:8,16:16,32:32};
const roots=['fe','ge','feg','gef'];
function raw(w){return w.split('').flatMap(c=>P[c]);}
function edgeSet(){const set=new Set();for(const w of roots){const a=raw(w);for(let i=1;i<=a.length;i++)set.add(a.slice(0,i).join(','));}return set;}
const FREE=edgeSet();if(FREE.size!==16)throw Error('root');
function perms(counts,wanted,cb){if(counts.some(x=>x<0))return;const word=[];
 function dfs(st,n){if(!n){const s=S[st];if(wanted.has(s))cb(word.join(''),s);return;}
 for(let i=0;i<6;i++)if(counts[i]&&T[st][i]!==8){counts[i]--;word.push(A[i]);dfs(T[st][i],n-1);word.pop();counts[i]++;}}
 dfs(0,counts.reduce((a,b)=>a+b,0));}
function key(h,x,y,z,cd){return [z-1,cd==='c'?x+y-h-1:0,cd==='d'?x+y-h-1:0,z,h+1-y-2*z,h+1-x];}
function calc(x,z){const y=10-x;function mk(){return {children:new Map(),label:0};} const root=mk();let count=0;
 function add(w,s){let n=root;for(const step of raw(w)){if(!n.children.has(step))n.children.set(step,mk());n=n.children.get(step);}n.label|=BIT[s];count++;}
 for(const c of ['c','d'])perms(key(8,x,y,z,c),new Set([1,2,4,8]),add);
 perms(key(9,x,y,z,null),new Set([16,32]),add);
 let nodes=0, INF=100000000;
 function dp(n,prefix){nodes++;let val=new Int32Array(64).fill(INF);val[0]=0;
 for(let b=1;b<=32;b*=2)if(n.label&b)val[b]=0;
 for(const [step,child] of n.children){const pre=prefix.concat([step]);const cd=dp(child,pre);let nxt=val.slice();const edge=FREE.has(pre.join(','))?0:1;
 for(let j=0;j<64;j++)if(val[j]<INF)for(let k=1;k<64;k++)if(cd[k]<INF){let m=j|k,v=val[j]+cd[k]+edge;if(v<nxt[m])nxt[m]=v;}val=nxt;}
 return val;}
 return {x,y,z,cost:16+dp(root,[])[63],nodes,accepted:count};}
const vals=[];for(let z=1;z<=4;z++)for(let x=2*z+1;x<=9;x++){const v=calc(x,z);vals.push(v);console.log(x,10-x,z,v.cost,v.nodes,v.accepted);}console.log('total',vals.length);
