/* EC49EXH independent signed six-axis/BRC/observer/native-prefix witness */
'use strict';
const assert=require('node:assert/strict');
const O={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const H=[['N',0],['N',1],['N',2],['A',0],['A',2],['B',0],['B',1],['AB',0],['BA',0]];
const B=['N','A','B','AB','BA'];
const W={2:['ce','de','ec','ed'],3:['feg','gef'],4:['fegd','gefd','gefc','fegc'],5:['fegfg','geffg'],6:['geffgd','geffgc','fegfgd','fegfgc'],7:['fegfgfg','geffgfg'],8:['fegfgfgg','geffgfgg']};
function signature(st){
 let out=0;
 for(const [i,[first,last]] of H.entries()){
  let ev=first,prev=last;
  for(const s of st){
   if(prev===1&&s===2){if(ev==='N')ev='A';else if(ev==='B')ev='BA';}
   else if(prev===2&&s===1){if(ev==='N')ev='B';else if(ev==='A')ev='AB';}
   prev=s;
  }
  out+=B.indexOf(ev)*5**i;
 }
 return out;
}
function rankMod(sigs){
 const P=1000003;
 let a=Array.from({length:9},(_,i)=>sigs.flatMap(s=>Array.from({length:5},(_,b)=>Number(Math.floor(s/5**i)%5===b))));
 function pow(v,e){let r=1;while(e){if(e%2)r=r*v%P;v=v*v%P;e=Math.floor(e/2);}return r;}
 let row=0;
 for(let c=0;c<a[0].length;c++){
  let p=a.findIndex((x,j)=>j>=row&&x[c]!==0);
  if(p<0)continue;
  [a[row],a[p]]=[a[p],a[row]];
  let inv=pow(a[row][c],P-2);
  for(let j=c;j<a[0].length;j++)a[row][j]=a[row][j]*inv%P;
  for(let i=row+1;i<9;i++){
   let t=a[i][c];
   if(t)for(let j=c;j<a[0].length;j++)a[i][j]=(a[i][j]-t*a[row][j]+P)%P;
  }
  if(++row===9)break;
 }
 return row;
}
const seen=new Set(),keys=new Set(),sigs=new Set(),rows=[];
for(let h=2;h<=8;h++){
 const K=new Set(),S=new Set(),old=seen.size;
 for(const w of W[h]){
  assert.equal(w.length,h);
  const st=[...w].flatMap(op=>O[op]);
  const pos=Array.from({length:6},(_,i)=>st.filter(v=>v===i+1).length);
  const net=Array.from({length:6},(_,i)=>pos[i]-st.filter(v=>v===-(i+1)).length);
  assert.deepEqual(net,[2,0,0,0,0,0]);
  K.add(pos.join(','));S.add(signature(st));
  for(let i=1;i<=st.length;i++)seen.add(st.slice(0,i).join(','));
 }
 assert.equal(K.size,1);assert.equal(rankMod([...S].sort((a,b)=>a-b)),9);
 for(const k of K)keys.add(k);for(const s of S)sigs.add(s);
 rows.push({h,new_edges:seen.size-old,E:seen.size,rank_F1000003:9,words:W[h]});
}
assert.equal(seen.size,90);assert.equal(keys.size,4);assert.equal(sigs.size,6);
// Each 9x9 zero-one minor obeys Hadamard |det|<=3^9=19683<1000003.
console.log(JSON.stringify({status:'PASS',unit:'EC49EXH',E:90,M:4,S:6,rows},null,2));
