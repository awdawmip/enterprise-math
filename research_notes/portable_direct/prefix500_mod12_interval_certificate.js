// PREFIX-500 exact integer elimination kernel; no external packages.
"use strict";
function ceil(a,b){return -Math.floor(-a/b);}
function feasible(rows,witness=false){
  // Each row is a*d+b*e+c >= 0; permitted nonzero |a| divide 12.
  for(let r=0;r<12;r++){
    const low=[],up=[],terms=[];
    for(const [a,b,c] of rows){
      if(a===0){terms.push([12*b,b*r+c]);continue;}
      if(12%Math.abs(a)!==0)throw Error("coefficient outside theorem");
      if(a>0)low.push([-12*b/a,ceil(-b*r-c,a)]);
      else up.push([12*b/(-a),Math.floor((b*r+c)/(-a))]);
    }
    for(const [p,q] of low)for(const [P,Q] of up)terms.push([P-p,Q-q]);
    let lo=0,hi=Infinity,ok=true;
    for(const [a,c] of terms){
      if(a>0)lo=Math.max(lo,ceil(-c,a));
      else if(a<0)hi=Math.min(hi,Math.floor(c/(-a)));
      else if(c<0){ok=false;break;}
    }
    if(!ok||lo>hi)continue;
    if(!witness)return true;
    const e=12*lo+r,d=low.length?Math.max(...low.map(([a,c])=>a*lo+c)):0;
    if(rows.some(([a,b,c])=>a*d+b*e+c<0))throw Error("bad witness");
    return [d,e];
  }
  return witness?null:false;
}
function check(){
  let cases=0;
  for(let a=-4;a<=4;a++){
    if(a!==0&&12%Math.abs(a)!==0)continue;
    for(let b=-3;b<=3;b++)for(let c=-7;c<=7;c++){
      const rows=[[1,0,0],[-1,0,8],[0,1,0],[0,-1,8],[a,b,c]];
      let brute=false;
      for(let d=0;d<=8;d++)for(let e=0;e<=8;e++){
        if(rows.every(([A,B,C])=>A*d+B*e+C>=0))brute=true;
      }
      const found=feasible(rows);
      if(found!==brute)throw Error(JSON.stringify({a,b,c,found,brute}));
      const w=feasible(rows,true);
      if(Boolean(w)!==brute)throw Error("witness mismatch");
      cases++;
    }
  }
  return {status:"ALL_CHECKS_PASS",certificate:"PREFIX500_MOD12_FEASIBILITY",
    grid_cases:cases,grid_domain:"0<=d,e<=8; |a| in {0,1,2,3,4} dividing 12; -3<=b<=3; -7<=c<=7",
    integer_semantics:"JavaScript safe integers for all declared bounded checks"};
}
return check();
