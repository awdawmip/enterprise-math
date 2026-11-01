"use strict";
// EC49DZ independently reconstructs native X6 order-sensitive seam transfers.
// All arithmetic for certificates is exact BigInt.
const OPS={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3]};
const B=["N","A","B","AB","BA"];
const ST=[["N",0],["N",1],["N",2],["A",0],["A",2],["B",0],["B",1],["AB",0],["BA",0]];
const PATHS=[
[2,-2,2,-1,1,-1,-1,1,-1,-2],
[-1,-1,2,-1,1,-1,2,-2,-2,1],
[-2,-1,1,-1,1,-1,2,-1,-2,2],
[-1,-1,1,-1,2,-1,1,2,-2,-2],
[1,-1,-1,-1,-2,2,-2,-1,1,2],
[1,-1,-1,-1,-2,-1,2,1,-2,2],
[-2,-2,2,1,-1,-1,-1,2,-1,1],
[-2,2,-1,-1,-1,-1,-2,1,2,1],
[-1,-1,-1,-1,-2,2,1,-2,1,2]];
function must(ok,msg){if(!ok)throw Error(msg);}
function steps(w){return [...w].flatMap(c=>OPS[c]);}
function disp(t){return Array.from({length:6},(_,j)=>t.reduce((s,v)=>s+(v===j+1)-(v===-j-1),0));}
function pc(t){return Array.from({length:6},(_,j)=>t.filter(v=>v===j+1).length);}
function z(s){const [b,l]=s;return [+(b==="N"),+(b==="A"),+(b==="B"),+(b==="AB"),+(b==="BA"),+(b==="A"&&l===2),+(b==="B"&&l===1),+(b==="N"&&l===1),+(b==="N"&&l===2)];}
function bucket(initial,t){let [b,last]=initial;
 for(const v of t){
  const e=last===1&&v===2?"A":last===2&&v===1?"B":null;
  if(e){if(b==="N")b=e;else if(b==="A"&&e==="B")b="AB";else if(b==="B"&&e==="A")b="BA";}
  last=v;
 }
 return b;
}
function atom(t){const b=bucket(["N",0],t),l=t[t.length-1];return [b,b==="N"?(l===1||l===2?l:0):b==="A"&&l===2?2:b==="B"&&l===1?1:0];}
function mat(w){
 const t=steps(w);
 const F=ST.map(s=>B.map(b=>+(bucket(s,t)===b)));
 const T=Array.from({length:9},()=>Array(5).fill(0));
 for(let j=0;j<5;j++){
  T[0][j]=F[0][j];T[7][j]=F[1][j]-F[0][j];T[8][j]=F[2][j]-F[0][j];
  T[1][j]=F[3][j];T[5][j]=F[4][j]-F[3][j];
  T[2][j]=F[5][j];T[6][j]=F[6][j]-F[5][j];
  T[3][j]=F[7][j];T[4][j]=F[8][j];
 }
 for(let i=0;i<9;i++)for(let j=0;j<5;j++)must(z(ST[i]).reduce((a,b,k)=>a+b*T[k][j],0)===F[i][j],"transfer reconstruction "+w);
 return T;
}
function det(a){const M=a.map(r=>r.map(BigInt));const n=M.length;must(M.every(r=>r.length===n),"square");let sign=1n,den=1n;
 for(let k=0;k<n-1;k++){
  if(M[k][k]===0n){let p=k+1;while(p<n&&M[p][k]===0n)p++;if(p===n)return 0n;[M[k],M[p]]=[M[p],M[k]];sign=-sign;}
  const q=M[k][k];
  for(let i=k+1;i<n;i++){for(let j=k+1;j<n;j++){const v=M[i][j]*q-M[i][k]*M[k][j];must(v%den===0n,"Bareiss divisibility");M[i][j]=v/den;}M[i][k]=0n;}
  den=q;
 }
 return sign*M[n-1][n-1];
}
const Z=ST.map(z);must(det(Z)===-1n,"nine independent features");
for(let i=0;i<9;i++){
 const t=PATHS[i];must(JSON.stringify(disp(t))===JSON.stringify([-2,0,0,0,0,0]),"historical displacement");
 must(JSON.stringify(pc(t))===JSON.stringify([2,2,0,0,0,0]),"historical p");
 must(JSON.stringify(atom(t))===JSON.stringify(ST[i]),"genuine historical state "+i);
}
const BASE=["ce","ec","de","ed"], BT=BASE.map(mat);
const LABELS=["ce:A","ce:AB","ce:BA","de:B","de:AB","ec:A","ec:AB","ed:B","ed:AB"];
function ninecols(W){return LABELS.map(label=>{let [w,b]=label.split(":");const i=BASE.indexOf(w),j=B.indexOf(b);return BT[i].map(row=>row[j]);});}
must(det(ninecols())===1n,"exact 9x9 transfer determinant");
const x=[2n,3n,5n,7n,11n,13n],y=[17n,19n,23n,29n,31n,37n];
function weighted(v,p){return p.reduce((a,k,j)=>a*v[j]**BigInt(k),1n);}
const padded=[];
for(let h=2;h<=8;h++){
 const c="c".repeat(h-1),d="d".repeat(h-1),W=[c+"e","e"+c,d+"e","e"+d];
 const ps=W.map(w=>pc(steps(w)));
 const expected=[h+1,h-1,1,0,0,0];
 for(let j=0;j<4;j++){
  must(JSON.stringify(disp(steps(W[j])))===JSON.stringify([2,0,0,0,0,0]),"return word");
  must(JSON.stringify(ps[j])===JSON.stringify(expected),"future p");
  must(JSON.stringify(mat(W[j]))===JSON.stringify(BT[j]),"all-h transfer");
  for(let i=0;i<9;i++){
   const t=PATHS[i],f=steps(W[j]);
   must(bucket(atom(t),f)===bucket(["N",0],t.concat(f)),"literal seam");
   must(weighted(x,pc(t.concat(f)))===weighted(x,pc(t))*weighted(x,pc(f)),"BRC x");
   must(weighted(y,pc(t.concat(f)))===weighted(y,pc(t))*weighted(y,pc(f)),"BRC y");
  }
 }
 padded.push({h,words:W,positive_counts:expected,transfer_det:"1",future_X:String(weighted(x,expected)),future_Y:String(weighted(y,expected))});
}
const all={};
for(let h of [2,3]){
 const records=[];
 function gen(s){if(s.length===h){const w=s.join(""),t=steps(w);if(JSON.stringify(disp(t))===JSON.stringify([2,0,0,0,0,0]))records.push({word:w,p:pc(t),transfer:mat(w)});return;}
 for(let v of "abcde")gen([...s,v]);}
 gen([]);
 all[h]=records;
 must(records.length===(h===2?4:15),"original alphabet returning count");
}
const result={schema:"EC49DZ_EXACT_NATIVE_TRANSFER_AUDIT_V1",status:"PASS",genuine_history_count:9,history_positive_count:[2,2,0,0,0,0],history_det:"-1",h2_witness_columns:LABELS,h2_witness_det:"1",padded_witnesses:padded,transfer_h2_h3:all,history_paths:PATHS,language_minimality:"{c,d,e}: three letters; e required; every 2-letter alphabet loses a history direction"};
return result;
