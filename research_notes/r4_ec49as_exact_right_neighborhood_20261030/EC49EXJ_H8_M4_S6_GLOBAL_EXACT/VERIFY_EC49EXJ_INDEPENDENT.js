// Independent JavaScript exact integer count of H8/M4/S<=6 family assignments.
// Uses occurrence equations rather than Python iterator logic; no floating point.
const options = new Map();
for(let h=2;h<=8;h++) {
  const m = new Map();
  for(let a=0;a<=h;a++) for(let c=0;c<=h;c++) for(let d=0;d<=h;d++) {
    const e=a+1;
    if(a+c+d+e>h) continue;
    const rem=h-a-c-d-e;
    for(let f=0;f<=rem;f++) {
      const g=rem-f, r=c+d;
      const p=[2*e+r+f,r+g,e].join(',');
      const t=r>=1?4:((f>0&&g>0)?2:0);
      if(t){if(m.has(p)&&m.get(p)!==t)throw Error('ambiguous');m.set(p,t);}
    }
  }
  options.set(h,m);
}
const base='3,1,1', allKeys=[...new Set([...options.values()].flatMap(m=>[...m.keys()]))].sort();
if(allKeys.length!==84||options.get(2).size!==1||!options.get(2).has(base))throw Error('key universe mismatch');
const other=allKeys.filter(k=>k!==base);
let sets=0, total=0, early=0, residual=0, allT4H7=0;
const stage={};
for(let i=0;i<other.length;i++)for(let j=i+1;j<other.length;j++)for(let k=j+1;k<other.length;k++){
 const names=[base,other[i],other[j],other[k]];
 const rows=[];let viable=true;
 for(let h=3;h<=8;h++){
   const r=names.map((n,ix)=> options.get(h).has(n)?[ix,options.get(h).get(n)]:null).filter(x=>x);
   if(!r.length){viable=false;break;}rows.push(r);
 }
 if(!viable)continue;
 let n=0;
 // rows 0..5 correspond h3..h8, h5 index 2, h7 index 4.
 function walkExact(h,seen,priorS4,priorSeen){
   if(h===6){if(seen!==15)return;n++;total++;if(priorSeen===15){residual++;if(priorS4)allT4H7++;}else early++;return;}
   for(const [id,t] of rows[h])walkExact(h+1,seen|1<<id,h<5 ? priorS4&&(t===4):priorS4,h===4?seen|1<<id:priorSeen);
 }
 walkExact(0,1,true,0);if(n)sets++;
}
if(sets!==14092||total!==55493||early!==28560||residual!==26933||allT4H7!==923)
 throw Error(JSON.stringify({sets,total,early,residual,allT4H7}));
console.log(JSON.stringify({status:'PASS',sets,total,early,residual,allT4H7}));
