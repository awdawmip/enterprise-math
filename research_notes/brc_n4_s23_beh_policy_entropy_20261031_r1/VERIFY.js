// BRC N4 behavioral S23 policy-entropy proof: exact integer checker.
function runChecks() {
  const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
           [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
  const V=[[44,-40,0,0,0,0],[-36,40,0,0,0,0],[0,0,4,0,0,0],
           [0,0,0,9,-5,0],[0,0,0,-1,5,0],[0,0,0,0,0,4]];
  const gc=[0,0,1,2,2,3],gr=[0,0,1,2,2,3];
  for(let i=0;i<6;i++) {
    if(M[i].reduce((a,b)=>a+b,0)!==20)throw Error("nonprobability row "+i);
    for(let j=0;j<6;j++) {
      const a=M[i].reduce((s,v,z)=>s+v*V[z][j],0);
      const b=V[i].reduce((s,v,z)=>s+v*M[z][j],0);
      if(a!==(i===j?80:0)||b!==(i===j?80:0))throw Error("inverse mismatch "+i+","+j);
    }
  }
  if((10*11-10*9)!==20||(10*18-10*2)!==160)throw Error("determinant mismatch");
  function tuples(values,d,fn) {
    let visited=0,cur=[];
    function visit(depth) {
      if(depth===d){fn(cur);visited++;return;}
      for(const v of values){cur.push(v);visit(depth+1);cur.pop();}
    }
    visit(0);return visited;
  }
  let checkedGroupRows=0;
  const groupCount=tuples([0,2,3,4,6],4,t=>{
    for(let i=0;i<6;i++){
      let p=0;for(let z=0;z<6;z++)p+=M[i][z]*t[gc[z]];
      if(p!==20*t[gr[i]])throw Error("group coin mismatch");
      checkedGroupRows++;
    }
  });
  let checkedCellRows=0;
  const cellCount=tuples([0,1,2],6,t=>{
    for(let i=0;i<6;i++){
      let p=0;for(let z=0;z<6;z++)p+=M[i][z]*t[z];
      if(p<0||p>40)throw Error("invalid six-cell coin law");
      checkedCellRows++;
    }
  });
  let checkedGridPoints=0;
  const lines=[];
  for(let n=1;n<=4;n++){
    const vals=Array.from({length:2*n+1},(_,i)=>i);
    let worst=0;
    tuples(vals,4,t=>{
      let sup=0;
      for(let j=0;j<4;j++){
        let best=Infinity;
        for(let a=0;a<n;a++)best=Math.min(best,Math.abs(t[j]-(2*a+1)));
        sup=Math.max(sup,best);
      }
      if(sup>1)throw Error("quantization mesh failed "+n);
      worst=Math.max(worst,sup);
      checkedGridPoints++;
    });
    if(worst!==1||n**4>=(n+1)**4)throw Error("packing radius failed");
    lines.push("n="+n+" labels="+(n**4)+" packing_points="+((n+1)**4)+" exact_grid_radius=1/"+(2*n));
  }
  if(groupCount!==625||cellCount!==729||checkedGroupRows!==3750||checkedCellRows!==4374||checkedGridPoints!==9668)
    throw Error("incomplete test domain");
  lines.push("det_AU=1/20 det_BU=2/5 det_M=1/50 exact_inverse=PASS");
  lines.push("four_group_row_checks="+checkedGroupRows+" six_cell_row_checks="+checkedCellRows+" four_cube_grid_checks="+checkedGridPoints);
  lines.push("PASS_BRC_N4_S23_BEHAVIORAL_POLICY_ENTROPY_20261031");
  return lines.join("\n")+"\n";
}
if(typeof module!=="undefined"&&require.main===module)process.stdout.write(runChecks());
