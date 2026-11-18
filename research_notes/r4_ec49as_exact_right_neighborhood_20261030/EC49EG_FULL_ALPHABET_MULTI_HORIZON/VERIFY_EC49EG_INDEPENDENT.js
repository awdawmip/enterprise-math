// EC49EG independent BigInt finite recheck. Native X6 paths; h=2..64.
'use strict';
const OP={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const atoms=['N0','N1','N2','A0','A2','B0','B1','AB','BA'];
const bins=['N','A','B','AB','BA'];
function ck(ok,msg){if(!ok)throw Error(msg)}
function native(w){return [...w].flatMap(x=>OP[x]);}
function label(q,s='N',p=0){for(const x of q){const a=p===1&&x===2,b=p===2&&x===1;
if(s==='N')s=a?'A':b?'B':'N';else if(s==='A'&&b)s='AB';else if(s==='B'&&a)s='BA';p=x;}return s;}
function atom(h){const s=label(h),last=h[h.length-1];return s==='N'?(last===1?'N1':last===2?'N2':'N0'):s==='A'?(last===2?'A2':'A0'):s==='B'?(last===1?'B1':'B0'):s;}
function histories(){let f=new Map(),q=[],left=new Map([[-2,2],[-1,4],[1,2],[2,2]]);
function walk(){if(f.size===9)return;if(q.length===10){let k=atom(q);if(!f.has(k))f.set(k,q.slice());return}
for(const v of [-2,-1,1,2]){if(left.get(v)){left.set(v,left.get(v)-1);q.push(v);walk();q.pop();left.set(v,left.get(v)+1);if(f.size===9)return}}}
walk();ck(atoms.every(a=>f.has(a)),'history states not realized');return atoms.map(a=>f.get(a));}
const histories9=histories();
function transfer(w){let v=native(w);return histories9.map(h=>label(v,label(h),h[h.length-1]));}
function det9(m){let a=m.map(row=>row.map(BigInt));let sign=1n,last=1n;
for(let k=0;k<8;k++){if(a[k][k]===0n){let j=k+1;while(j<9&&a[j][k]===0n)j++;if(j===9)return 0n;[a[k],a[j]]=[a[j],a[k]];sign=-sign;}
let z=a[k][k];for(let i=k+1;i<9;i++){for(let j=k+1;j<9;j++){let num=a[i][j]*z-a[i][k]*a[k][j];ck(num%last===0n,'nonexact Bareiss');a[i][j]=num/last}a[i][k]=0n;}last=z;}return sign*a[8][8];}
function cost(ws){const prefixes=new Set();for(const w of ws){const p=native(w);for(let i=1;i<=p.length;i++)prefixes.add(p.slice(0,i).join(','));}return prefixes.size;}
function weight(path,x){let out=1n;for(let k=1;k<=6;k++){let n=path.filter(t=>t===k).length;out*=BigInt(x[k-1])**BigInt(n);}return out;}
const xs=[[2,3,5,7,11,13],[3,4,7,11,13,17]];
const out=[];
for(let H=2;H<=64;H++){
 let w=['fe'+'f'.repeat(H-2),'ge'+'f'.repeat(H-2)];let a=transfer(w[0]),b=transfer(w[1]);
 let m=Array.from({length:9},(_,i)=>[1,2,3,4].map(k=>Number(a[i]===bins[k])).concat([0,1,2,3,4].map(k=>Number(b[i]===bins[k]))));
 ck(det9(m)===-1n,'unimodular determinant');
 let paths=w.map(native);ck(paths.every(p=>p.length===2*H+2),'primitive length');
 ck(cost(w)===4*H+4,'native prefix cost');
 for(let p of paths)for(let h of histories9)for(let x of xs)ck(weight(h.concat(p),x)===weight(h,x)*weight(p,x),'BRC composition');
 let all=[];for(let i=2;i<=H;i++)all.push('fe'+'f'.repeat(i-2),'ge'+'f'.repeat(i-2));
 ck(cost(all)===4*H+4,'multi-window shared prefix cost');
 if(H<=8||H===64)out.push({H,cost:cost(w),minor:'-1'});
}
const result={status:'PASS',scope:'Independent JS native-X6, nine real histories, BigInt Bareiss 9x9, BRC factors, H2..64',samples:out};
console.log(JSON.stringify(result,null,2));
