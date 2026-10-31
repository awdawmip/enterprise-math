"use strict";
// Exact integer auditor for BRC N4/S23 ten fixed uniform-pair decoders.
// No floating point or solver tolerance enters any loss comparison.
const M20=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
const BOXSTR=["34 24 34 24","34 23 34 34","34 34 34 23","24 24 12 12","12 12 24 34","12 13 23 24","23 34 12 13","24 34 12 14","13 12 13 13","12 12 14 12"];
const BOX=BOXSTR.map(r=>r.split(" ").map(s=>[Number(s[0])-1,Number(s[1])-1]));
const SOURCE_GROUP=[0,0,1,2,2,3],A_SLOT=[0,0,0,1,1,1],B_SLOT=[0,0,1,0,0,2];
function preparedFromF(f) {
  return M20.map(row=>[0,1,2,3].map(t=>row.reduce((sum,w,x)=>sum+w*f[x][t],0)));
}
function labelWorst(p,li,den) {
  // p rows sum to den; paired decoder assigns den/2 to each of two atoms.
  let worst=0;
  for(let i=0;i<6;i++) {
    const pair=BOX[li][SOURCE_GROUP[i]],half=den/2;
    let s=0;
    for(let t=0;t<4;t++){
      const q=(t===pair[0]||t===pair[1])?half:0;
      s+=Math.abs(p[i][t]-q);
    }
    worst=Math.max(worst,s);
  }
  return worst; // 2*den*TV
}
function ternaryResult(code) {
  const d=[];
  for(let j=0;j<11;j++){d.push(code%3);code=Math.floor(code/3);}
  // Parameter 0 denotes stop probability 0, 1 denotes 1/2, 2 denotes 1.
  // F8 is exact source-time law with common denominator 8.
  const f=[];
  for(let x=0;x<6;x++){
    const a=d[A_SLOT[x]],b=d[2+B_SLOT[x]],c=d[5+x];
    f.push([4*a,2*(2-a)*b,(2-a)*(2-b)*c,(2-a)*(2-b)*(2-c)]);
  }
  const p=preparedFromF(f); // denominator 20*8=160
  let best=Infinity;
  for(let l=0;l<10;l++) best=Math.min(best,labelWorst(p,l,160));
  return best; // TV=best/320
}
function edgePrepared(n,d) {
  // a_A=n/d, a_B=1; b_U=b_AV=0; c_AU0=c_AV=1; c_AU1=0.
  // All B sources stop at T=1. Rows have denominator 20*d.
  const f=[[n,0,d-n,0],[n,0,0,d-n],[n,0,d-n,0],[d,0,0,0],[d,0,0,0],[d,0,0,0]];
  return preparedFromF(f);
}
function main(){
  let count=0,max=0,eqHalf=0,underHalf=0;
  for(let code=0;code<3**11;code++){
    const best=ternaryResult(code);
    if(best>160) throw Error("TERNARY_FAILURE code="+code+" numerator="+best);
    max=Math.max(max,best);
    if(best===160)eqHalf++;else underHalf++;
    count++;
  }
  if(count!==177147||max!==160||eqHalf!==169441||underHalf!==7706)throw Error("UNEXPECTED_GRID_COUNTS");
  const d=120;let edgeChecked=0;
  for(let n=0;n<=d;n++){
    const p=edgePrepared(n,d);
    const actual=BOX.map((_,l)=>labelWorst(p,l,20*d));
    const expected=[
      ...Array(6).fill(40*d),
      2*(11*d+9*n),
      20*(d+n),
      Math.max(40*(d-n),20*d),
      Math.max(40*(d-n),20*d)
    ];
    if(actual.some((v,j)=>v!==expected[j]))throw Error("EDGE_LABEL_FORMULA_FAILURE n="+n+" actual="+actual+" expected="+expected);
    const profile=Math.min(20*(d+n),Math.max(40*(d-n),20*d));
    if(Math.min(...actual)!==profile)throw Error("EDGE_ENVELOPE_FAILURE n="+n);
    edgeChecked++;
  }
  const witness=edgePrepared(1,3);
  const witnessLossNumerators=BOX.map((_,l)=>labelWorst(witness,l,60));
  if(Math.min(...witnessLossNumerators)!==80)throw Error("WITNESS_FAILURE"); // 80/(2*60)=2/3
  return {status:"PASS_BRC_N4_S23_TENBANK_TERNARY_GRID_AND_EXACT_EDGE_20261101",grid_count:count,grid_values:[0,"1/2",1],grid_max_TV:"1/2",grid_equal_half:eqHalf,grid_below_half:underHalf,edge_rational_points_checked:edgeChecked,edge_formula:"min((1+t)/2,max(1-t,1/2))",unique_edge_peak_t:"1/3",edge_peak_TV:"2/3",witness_label_TV_numerators_over_120:witnessLossNumerators};
}
if(typeof module!=="undefined" && require.main===module) console.log(JSON.stringify(main(),null,2));

