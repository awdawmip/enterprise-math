// EC49FWZ frozen BRC16943, exact integer/Boolean crosscheck; run: node EC49FWZ_PHASE_TRANSVERSAL_VERIFY.js
function verify(){
  const mod=(a,n)=>(a%n+n)%n, gcd=(a,b)=>b?gcd(b,a%b):a;
  const masks=new Set();let primitive=0;
  const inv={1:1,2:3,3:2,4:4};
  const p10=(h,n)=>{
    h=mod(h,10);n=mod(n,10);
    if(h%5===0&&n%5===0)return false;
    const slope=h%5===0?5:mod(n*inv[h%5],5);
    return [[[3],[0,3,4,5]],[[2,3,4,5],[2,3]]][h%2][n%2].includes(slope);
  };
  for(let x=0;x<10;x++)for(let y=0;y<10;y++){
    if(gcd(gcd(x,y),10)!==1)continue;
    primitive++;
    let root=null;
    for(let h=0;h<10&&!root;h++)for(let n=0;n<10;n++)if(mod(y*h-x*n+1,10)===0){root=[h,n];break;}
    if(!root)throw Error("No root");
    let u=0;for(let t=0;t<10;t++)if(p10(root[0]+x*t,root[1]+y*t))u|=1<<t;
    masks.add(u);
  }
  if(primitive!==72||masks.size!==50)throw Error("Frozen support mismatch");
  const hist={};
  for(const u of masks){let d=0;for(let t=0;t<10;t++)d+=((u>>t)&1)!==((u>>mod(t-5,10))&1);hist[d]=(hist[d]||0)+1;}
  if(JSON.stringify([2,4,6,8].map(d=>hist[d]))!==JSON.stringify([10,26,10,4]))throw Error("Frozen gap mismatch");
  const crt=Array.from({length:5},(_,i)=>Array.from({length:11},(_,j)=>Array.from({length:55},(_,t)=>t).find(t=>t%5===i&&t%11===j)));
  const mfun=r=>r<=20?Math.ceil(r/2)+1:Math.ceil(r/2)+2;
  const layout=r=>{
    const m=mfun(r),a=[];
    for(let i=0;i<5;i++){for(let j=0;j<Math.min(m,11);j++)a.push(crt[i][j]);for(let j=0;j<Math.max(0,m-11);j++)a.push(crt[i][j]+55);}
    if(new Set(a).size!==5*m)throw Error("Layout distinctness");
    return a;
  };
  const dist=(S,d,i,j)=>S.reduce((s,t)=>s+(t%5===i&&t%11!==j?1:0)+(mod(d-t,5)===i&&mod(d-t,11)!==j?1:0),0);
  let coverageChecks=0,lowerChecks=0,booleanChecks=0;
  const rows=[];
  for(let r=1;r<=40;r++){
    const m=mfun(r), S=layout(r);let best=999;
    for(let d=0;d<55;d++)for(let i=0;i<5;i++)for(let j=0;j<11;j++){
      const z=dist(S,d,i,j),w=dist(S,d+55,i,j);
      if(z!==w||z<r)throw Error("Coverage fail r="+r+" d="+d+" i="+i+" j="+j);
      if(z<best)best=z;
      coverageChecks++;
    }
    const f=2*m-2*Math.ceil(m/11);
    if(best!==f)throw Error("Minimum mismatch r="+r);
    for(let small=0;small<m;small++)if(2*small-2*Math.ceil(small/11)>=r)throw Error("Lower bound mismatch");
    lowerChecks+=m;
    rows.push({r,m,activations:5*m,min_distance:best});
  }
  const u=299;
  if(!masks.has(u))throw Error("Missing single-pair witness");
  const gaps=[0,1,2,3,4].filter(i=>((u>>i)&1)!==((u>>(i+5))&1));
  if(gaps.length!==1)throw Error("Not a single-pair witness");
  const word=(t,j)=>((u>>mod(t,10))&1)&&mod(t,11)!==j?1:0;
  const S=layout(3);
  for(let sL=0;sL<110;sL++)for(let d=0;d<55;d++)for(let j=0;j<11;j++){
    const sR=mod(sL-d,110), origJ=mod(j-sL,11),i=mod(gaps[0]+sL,5);
    let actual=0;
    for(const t of S){
      actual+=(word(t-sL,origJ)!==word(t-sL-55,origJ)?1:0);
      actual+=(word(-t-sR,origJ)!==word(-t-sR-55,origJ)?1:0);
    }
    if(actual!==dist(S,d,i,j))throw Error("Direct word mismatch");
    booleanChecks++;
  }
  const all=Array.from({length:110},(_,i)=>i);
  for(let d=0;d<55;d++)for(let i=0;i<5;i++)for(let j=0;j<11;j++)if(dist(all,d,i,j)!==40)throw Error("Max distance mismatch");
  return {status:"ALL_PASS",scientific_pin:"BRC16943",primitive_directions:primitive,distinct_masks:masks.size,
   gap_histogram:hist,offset_projection_count:55, r_values:40,
   singleton_offset_missing_column_checks:coverageChecks, lower_bound_size_checks:lowerChecks,
   direct_boolean_CRT_checks:booleanChecks,maximum_distance:40,
   formula_r_1_to_20:"5*(ceil(r/2)+1)",formula_r_21_to_40:"5*(ceil(r/2)+2)",
   r_above_40:"IMPOSSIBLE", selected:rows.filter(x=>[1,2,3,4,19,20,21,22,39,40].includes(x.r)),
   status_scope:"finite auxiliary CRT / Farey Boolean observer; author validation, not independent review"};
}
console.log(JSON.stringify(verify(),null,2));
