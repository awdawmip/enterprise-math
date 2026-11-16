"use strict";
// Exact integer validation of the R617 ordered-source coding.
const L=[1n,0n,1n,1n],R=[1n,1n,0n,1n],I=[1n,0n,0n,1n];
function mult(A,B){return [A[0]*B[0]+A[1]*B[2],A[0]*B[1]+A[1]*B[3],A[2]*B[0]+A[3]*B[2],A[2]*B[1]+A[3]*B[3]];}
function bitCode(i){if(!Number.isInteger(i)||i<0||i>=12)throw Error("bad label");return i.toString(2).padStart(4,"0");}
function basis(){return Array.from({length:12},(_,i)=>{let A=I;for(const b of bitCode(i)) A=mult(A,b==="0"?L:R);return A;});}
const F=basis();
function matrixWord(w){let A=I;for(const i of w)A=mult(A,F[i]);return A;}
function decode(A){let p=A[0]+A[1],q=A[2]+A[3];const bits=[];let steps=0;
  while(p!==q){if(p>q){p-=q;bits.push("1");}else{q-=p;bits.push("0");}
    steps++;if(steps>100000)throw Error("bad decode");}
  if(p!==1n||bits.length%4)throw Error("bad terminator or code length");
  const stream=bits.join(""),w=[];
  for(let j=0;j<stream.length;j+=4){const n=parseInt(stream.slice(j,j+4),2);
    if(n>=12)throw Error("unused code");w.push(n);}
  return w;}
function eq(A,B){return A.every((x,i)=>x===B[i]);}
function check(){
  const seenMat=new Set(),seenRat=new Set();let count=0,maxBits=0;
  function visit(w,remaining){
    if(remaining===0){const A=matrixWord(w);const key=A.join(",");
      const rk=(A[0]+A[1])+"/"+(A[2]+A[3]);
      if(seenMat.has(key)||seenRat.has(rk))throw Error("collision: "+w);
      seenMat.add(key);seenRat.add(rk);
      if(decode(A).join(",")!==w.join(","))throw Error("decode mismatch: "+w);
      if(w.length){const B=mult(matrixWord(w.slice(0,-1)),F[w[w.length-1]]);
        if(!eq(A,B))throw Error("composition");}
      count++;
      for(const n of A)maxBits=Math.max(maxBits,(n<0n?-n:n).toString(2).length);
      return;}
    for(let i=0;i<12;i++)visit([...w,i],remaining-1);
  }
  for(let depth=0;depth<=4;depth++)visit([],depth);
  const sideA=F[0].map((a,j)=>2n*a+F[3][j]+F[4][j]);
  const sideB=F[2].map(a=>3n*a);
  if(!eq(sideA,sideB))throw Error("rank relation");
  if(count!==22621||seenMat.size!==count||seenRat.size!==count)throw Error("wrong count");
  return {test:"R617_FREE_MONOID_EXACT_PASS",depth_max:4,
    ordered_words_verified:count,distinct_matrices:seenMat.size,
    distinct_rationals:seenRat.size,max_matrix_entry_bits:maxBits,
    branch_codes:12,code_bits_per_branch:4,
    linear_relation:"2*F0 + F3 + F4 = 3*F2",
    relation_LHS:sideA.map(String),relation_RHS:sideB.map(String),
    word_rank_s_le_12:"N_s=2^s",
    minimum_matrix_dimension_s3:3,minimum_matrix_dimension_s4:4,
    scientific_scope:"auxiliary 12-branch history labels, not a native X6 update"};
}
if(typeof module!=="undefined"&&require.main===module)console.log(JSON.stringify(check(),null,2));
