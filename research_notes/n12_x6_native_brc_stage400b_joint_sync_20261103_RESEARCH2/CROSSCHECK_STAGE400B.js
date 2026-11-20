'use strict';
const words=[[1,1,-1,1],[1,-1,1,1]];
const K=(u,v)=>u.reduce((n,x,i)=>n+Number(x===v[i]),0);
const grid=words.map(w=>words.map(v=>K(w,v)));
if(JSON.stringify(grid)!=='[[4,2],[2,4]]')throw Error('K mismatch');
function brc(weighted){let x=new Map([['0,0,0,0,0,0',1n]]);
 for(let k=0;k<4;k++){let y=new Map();
 for(const [key,n] of x){const a=key.split(',').map(Number);
 for(let i=0;i<6;i++)for(const d of [-1,1]){const b=[...a];b[i]+=d;const q=b.join(',');
 const f=weighted&&i===0?(d===1?2n:3n):1n;y.set(q,(y.get(q)||0n)+n*f)}}
 x=y;}return x.get('2,0,0,0,0,0')||0n;}
if(brc(false)!==64n||brc(true)!==336n)throw Error('native BRC mismatch');
console.log(JSON.stringify({status:'STAGE400B_INDEPENDENT_JS_PASS',K:grid,N4:String(brc(false)),W4:String(brc(true))}));
