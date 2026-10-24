'use strict';
// Exact author-side three-axis box-corner certificate, runnable with Node.js 18+.
// No floating point is used to decide signs, and all 16-mask crosschecks are independent.
const verifyBoxCorner = function verifyBoxCorner(){
  'use strict';
  const Q=[[1n,665n,1n,333n],[333n,333n,1n,333n],[1n,1n,1n,997n]];
  const edges=[[0,1],[1,2],[1,3],[2,3]], deg=[1n,3n,2n,2n];
  const barriers=[
    [15,0,0,0,12],[2,5,60,1,2],[0,8,110,2,17],[3,3,184,1,2],
    [1,6,225,2,30],[2,4,322,2,60],[0,7,353,2,15],[3,2,402,2,139],
    [1,5,426,2,30],[2,3,485,2,66],[0,6,502,2,17],[3,1,533,2,176],
    [1,4,545,2,36],[2,2,579,2,86],[0,5,587,2,22],[3,0,607,2,353],
    [1,3,612,2,49],[2,1,631,2,129],[0,4,634,2,30],[1,2,648,2,73],
    [2,0,660,2,241],[0,3,660,2,44],[1,1,669,2,116],[0,2,675,2,68],
    [1,0,681,2,220],[0,1,683,2,112],[0,0,689,2,214]
  ];
  const pow=(b,n)=>b**BigInt(n), total=c=>c[0]+c[1]+c[2];
  const assert=(v,msg)=>{if(!v)throw Error(msg);};
  function N(c){
    if(total(c)===0)return 0n; // Empty support: the nonempty-word inclusion-exclusion formula has an empty-set correction.
    let t=0n;
    for(const [i,j] of edges){let u=1n;for(let a=0;a<3;a++)u*=pow(Q[a][i]+Q[a][j],c[a]);t+=u;}
    for(let i=0;i<4;i++){let u=deg[i];for(let a=0;a<3;a++)u*=pow(Q[a][i],c[a]);t-=u;}
    return t;
  }
  function xcoef(y,z){
    return [pow(2n,z)*(pow(666n,y)+pow(334n,y)),pow(998n,z)*pow(666n,y),
      pow(998n,z)*pow(334n,y),3n*pow(333n,y),2n*pow(333n,y)*pow(997n,z),pow(333n,y)+2n];
  }
  function ycoef(x,z){
    return [pow(2n,z)*pow(666n,x)+pow(998n,z)*pow(998n,x),
      pow(2n,z)*pow(666n,x)+pow(998n,z)*pow(334n,x),
      1n+3n*pow(665n,x)+2n*pow(997n,z)*pow(333n,x)];
  }
  function zcoef(x,y){
    return [pow(666n,x)*(pow(666n,y)+pow(334n,y)),
      pow(998n,x)*pow(666n,y)+pow(334n,x)*pow(334n,y),
      2n*pow(333n,x+y),pow(333n,y)*(1n+3n*pow(665n,x))+2n];
  }
  const xform=(x,y,z)=>{const [A,B,C,D,E,F]=xcoef(y,z);return A*pow(666n,x)+B*pow(998n,x)+C*pow(334n,x)-D*pow(665n,x)-E*pow(333n,x)-F;};
  const yform=(x,y,z)=>{const [A,B,C]=ycoef(x,z);return A*pow(666n,y)+B*pow(334n,y)-C*pow(333n,y)-2n;};
  const zform=(x,y,z)=>{const [A,B,C,D]=zcoef(x,y);return A*pow(2n,z)+B*pow(998n,z)-C*pow(997n,z)-D;};
  const GX=(x,y,z)=>{const [A,B,C,D,E,F]=xcoef(y,z);return -334n*A*pow(666n,x)-2n*B*pow(998n,x)-666n*C*pow(334n,x)+335n*D*pow(665n,x)+667n*E*pow(333n,x)+999n*F;};
  const GY=(x,y,z)=>{const [A,B,C]=ycoef(x,z);return -334n*A*pow(666n,y)-666n*B*pow(334n,y)+667n*C*pow(333n,y)+1998n;};
  const GZ=(x,y,z)=>{const [A,B,C,D]=zcoef(x,y);return -998n*A*pow(2n,z)-2n*B*pow(998n,z)+3n*C*pow(997n,z)+999n*D;};
  let identityPoints=0;
  for(let x=0;x<=6;x++)for(let y=0;y<=5;y++)for(const z of [0,1,2,3,7,17]){
    if(x+y+z===0)continue;
    const c=[x,y,z],n=N(c);
    assert(n===xform(x,y,z)&&n===yform(x,y,z)&&n===zform(x,y,z),"grouping at "+c);
    assert(N([x+1,y,z])-1000n*n===GX(x,y,z),"x difference");
    assert(N([x,y+1,z])-1000n*n===GY(x,y,z),"y difference");
    assert(N([x,y,z+1])-1000n*n===GZ(x,y,z),"z difference");
    let [A,B,C,D,E,F]=xcoef(y,z);
    assert(GX(x+1,y,z)-334n*GX(x,y,z)===
      -1328n*B*pow(998n,x)-110888n*A*pow(666n,x)+110885n*D*pow(665n,x)-667n*E*pow(333n,x)-332667n*F,"x 334 recurrence");
    assert(GX(x+1,y,z)-665n*GX(x,y,z)===
      -666n*B*pow(998n,x)-334n*A*pow(666n,x)+220446n*C*pow(334n,x)-221444n*E*pow(333n,x)-663336n*F,"x 665 recurrence");
    [A,B,C]=ycoef(x,z);
    assert(GY(x,y+1,z)-334n*GY(x,y,z)===
      -334n*332n*A*pow(666n,y)-667n*C*pow(333n,y)-1998n*333n,"y recurrence");
    [A,B,C,D]=zcoef(x,y);
    assert(GZ(x,y,z+1)-2n*GZ(x,y,z)===-1992n*B*pow(998n,z)+2985n*C*pow(997n,z)-999n*D,"z 2 recurrence");
    assert(GZ(x,y,z+1)-997n*GZ(x,y,z)===-2n*B*pow(998n,z)+998n*995n*A*pow(2n,z)-996n*999n*D,"z 997 recurrence");
    identityPoints++;
  }
  assert(identityPoints===251,"grid audit size");
  assert(pow(998n,6)>331n*pow(334n,6) && pow(499n,3)>496505n,"tail bounds");
  for(let x=1;x<=6;x++)assert(GX(x,0,0)>0n,"pure 0 positivity "+x);
  assert(GX(12,0,0)>0n && GX(13,0,0)<0n,"pure 0 threshold");
  for(let z=1;z<=3;z++)assert(GZ(0,0,z)>0n,"pure 3 positivity "+z);
  let oldChecks=0,newChecks=0,certificates=[];
  const points=new Map();
  for(const b of barriers){
    const terminal=b.slice(0,3),axis=b[3],level=b[4];
    const opts=terminal.map((v,i)=>i===axis?[level]:(v===0?[0]:[0,v]));
    const nc=total(terminal);let min=null,minPoint=null,corners=[];
    for(const x of opts[0])for(const y of opts[1])for(const z of opts[2]){
      const p=[x,y,z],np=total(p),margin=N(p)*pow(1000n,nc-np)-N(terminal);
      assert(margin>0n,"not a strict positive corner gap: "+terminal+" versus "+p);
      if(min===null||margin<min){min=margin;minPoint=p;}
      corners.push({count:p,gap_numerator:margin.toString()});
      points.set(p.join(","),p);
    }
    const full=opts.reduce((v,a,i)=>i===axis?v:v*(terminal[i]+1),1);
    oldChecks+=full;newChecks+=corners.length;
    certificates.push({terminal_count:terminal,transversal_axis_index:axis,level,
      original_full_rectangle_points:full,strict_corner_checks:corners.length,
      minimum_corner:minPoint,min_gap_numerator:min.toString(),
      gap_denominator:"1000^"+nc,corners});
  }
  assert(oldChecks===1094&&newChecks===80&&points.size===75,"corner domain counts");
  function independentMask(c){
    let m=Array(16).fill(0n);m[0]=1n;
    // Independent occupancy-state transition, deliberately ordered differently from the coefficient formula.
    for(const a of [2,1,0])for(let k=0;k<c[a];k++){
      const next=Array(16).fill(0n);
      for(let mask=0;mask<16;mask++)if(m[mask]!==0n)for(let label=0;label<4;label++)
        next[mask|(1<<label)]+=m[mask]*Q[a][label];
      m=next;
    }
    return edges.reduce((s,[i,j])=>s+m[(1<<i)|(1<<j)],0n);
  }
  const probes=[[12,0,0],[0,2,60],[0,2,184],[0,0,17],[2,5,60],[3,3,184],
    [0,0,689],[4,1,288],[0,1,683],[3,2,139],[1,4,545],[2,2,579]];
  for(const c of probes)assert(N(c)===independentMask(c),"16-mask independent crosscheck "+c);
  return {
    schema:"EM_BRC_THREE_AXIS_BOX_CORNER_EXACT_V1",
    status:"PASS_AUTHOR_UNREVIEWED_NOT_ADMITTED",
    scientific_scope:"Fixed four-label, three-action, positive-weight BRC support observer; no native X6 transfer.",
    weights:Q.map(q=>q.map(Number)),good_edges:edges,denominator:1000,
    analytic_result:"Every coordinate section of terminal good-pair occupancy is discretely unimodal; every axis-aligned integer box attains a minimum at a corner.",
    model_formula_domain:"nonempty word n>=1; empty support occupancy defined as 0, with special correction",
    recurrence_identity_grid_points:identityPoints,
    pure_0_increment_signs_1_to_6:Array.from({length:6},(_,i)=>[i+1,GX(i+1,0,0).toString()]),
    pure_0_boundary:{increment_at_count_12:"POSITIVE",increment_at_count_13:"NEGATIVE"},
    pure_3_increment_signs_1_to_3:[1,2,3].map(z=>[z,GZ(0,0,z).toString()]),
    finite_exceptions_inequalities:{x_tail:"998^6 > 331*334^6",z_tail:"499^3 > 496505"},
    old_transversal_points:oldChecks,new_transversal_corner_checks:newChecks,
    distinct_corner_points:points.size,independent_16_mask_crosschecks:probes.length,
    inherited_unreviewed_sources:{
      transversal:"0029daddde2e87ec299e1cfeb1a5f13edf4c3694",
      action_2:"0ae89109350005d3087d6856a16cf1a413db078d"},
    certificates
  };
};
console.log(JSON.stringify(verifyBoxCorner(), null, 2));
