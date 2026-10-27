'use strict';
/*
 PREFIX-293: exact ordered-source-pair BRC checks for Q(i) complex rational mixing.
 Each port is a list of three labeled source-leg coefficients over Z[i],
 sharing denominator 4r. No ordinary propagation or floating-point arithmetic.
 */
const fs = require('fs');
const Z = (re = 0n, im = 0n) => [BigInt(re), BigInt(im)];
const add=(a,b)=>Z(a[0]+b[0],a[1]+b[1]);
const neg=a=>Z(-a[0],-a[1]);
const sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>Z(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]);
const conj=a=>Z(a[0],-a[1]);
const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1];
const mag2=a=>a[0]*a[0]+a[1]*a[1];
const sum=arr=>arr.reduce((x,y)=>add(x,y),Z());
const serialize=x=>[String(x[0]),String(x[1])];
const one=Z(1),zero=Z(),minus=Z(-1),ii=Z(0,1);
const phases=[one,ii,minus,neg(ii)];
const samples=[zero,one,minus,ii,neg(ii),add(one,ii)];
const solutions=[[1,0,1],[3,1,2],[5,0,3],[8,3,5],[12,1,7]];
let gram_checks=0, port_reads=0, pair_products=0, total_checks=0,
    cross_checks=0, leak_checks=0, event_checks=0, recovery_checks=0;
const assert=(b,m)=>{if(!b)throw Error(m)};
function ports(p,h,r,u){
  const R=BigInt(r),v=Z(p,h),Rz=Z(R),twoR=Z(2n*R),u2=mul(u,u);
  const times=(a,b)=>mul(a,b);
  return [
    [twoR,times(twoR,u),zero],
    [zero,neg(twoR),times(twoR,u)],
    [twoR,times(sub(v,Rz),u),times(add(v,Rz),u2)],
    [twoR,times(neg(add(Rz,v)),u),times(sub(Rz,v),u2)],
    [twoR,zero,neg(times(twoR,u2))],
    [zero,times(Z(2),u),times(Z(2),u2)]
  ];
}
function brc(port,a,b){
  let acc=Z();
  for(let j=0;j<3;j++) for(let k=0;k<3;k++){
    // Both source branches are labeled; keep the ordered (j,k) pair.
    const v=mul(mul(port[j],a[j]),conj(mul(port[k],b[k])));
    acc=add(acc,v);pair_products++;
  }
  return acc;
}
const inputs=[];
for(let a of samples)for(let b of samples)for(let c of samples)inputs.push([a,b,c]);
const seen=[];
for(let [p,h,r] of solutions){
  assert(p*p+h*h+2===3*r*r,'Diophantine premise');
  for(let u of phases){
    let P=ports(p,h,r,u),D=BigInt(4*r),D2=D*D;
    for(let j=0;j<3;j++)for(let k=0;k<3;k++){
      let actual=sum(P.map(x=>mul(x[j],conj(x[k]))));
      assert(eq(actual,j===k?Z(D2):zero),'Gram failure');gram_checks++;
    }
    for(let i=0;i<inputs.length;i++){
      let a=inputs[i],b=inputs[(i*37+17)%inputs.length];
      let zs=a.reduce((s,x)=>s+mag2(x),0n);
      let masses=P.map(port=>{
        let x=brc(port,a,a);
        assert(x[1]===0n&&x[0]>=0n,'nonpositive bin');
        port_reads++;
        return x[0];
      });
      assert(masses.reduce((x,y)=>x+y,0n)===D2*zs,'isometry');total_checks++;
      let cross=sum(P.map(port=>brc(port,a,b)));
      let expected=Z();for(let j=0;j<3;j++)expected=add(expected,mul(a[j],conj(b[j])));
      expected=mul(Z(D2),expected);
      assert(eq(cross,expected),'cross input isometry');cross_checks++;
      const wN=add(mul(u,a[1]),mul(mul(u,u),a[2]));
      assert(masses[5]*4n*BigInt(r*r)===D2*mag2(wN),'leak identity');leak_checks++;
      assert(masses[5]*2n*BigInt(r*r)<=D2*zs,'sharp universal leak cap');
      let priorEvent=mag2(add(a[0],mul(u,a[1])))+mag2(add(neg(a[1]),mul(u,a[2])));
      assert(masses[0]+masses[1]===BigInt(4*r*r)*priorEvent,'E unchanged');event_checks++;
      // Decode only pre-measurement coherent amplitudes, no physical reset implied.
      // Recover a0 from q_d0+q_d1+q_d2, all with shared denominator D.
      let v0=P.map(port=>sum(port.map((cj,j)=>mul(cj,a[j]))));
      const lhs=mul(Z(p,h),sub(sub(mul(Z(2n*D),a[0]),add(v0[2],v0[3])),mul(Z(2),v0[4])));
      const rhs=mul(Z(r),sub(v0[2],v0[3]));
      assert(eq(lhs,rhs),'coherent a0 decode');recovery_checks++;
    }
  }
  seen.push({p,h,r,least_five_port_worst_case_leak:'1/'+(2*r*r),common_denominator:4*r});
}
// Prove sharpness by an exact witness: a=(0,1,u^-1).
for (let [p,h,r] of solutions)for(let u of phases){
 let a=[zero,one,conj(u)],P=ports(p,h,r,u),D2=BigInt(16*r*r);
 let leak=brc(P[5],a,a)[0];
 assert(2n*BigInt(r*r)*leak===D2*2n,'witness sharpness');
}
const candidates=[];
for(let r=1;r<=30;r++){
 const target=3*r*r-2;
 const pairs=[];
 for(let p=0;p*p<=target;p++)for(let h=0;h*h<=target-p*p;h++)
   if(p*p+h*h===target)pairs.push([p,h]);
 if(pairs.length)candidates.push({r,pairs});
}
const result={schema:'PREFIX293_COMPLEX_GAUSSIAN_BRC_EXACT_V1',
 arithmetic:'Z[i] Gaussian BigInt / common denominator 4r; exhaustive ordered source-leg BRC pairs',
 tested_source_packets:inputs.length,phase_count:4,solution_count:solutions.length,
 total_input_phase_solution_combinations:inputs.length*4*solutions.length,
 direct_brc_port_reads:port_reads,ordered_pair_products:pair_products,
 exact_gram_entries_checked:gram_checks,total_mass_checks:total_checks,
 cross_input_checks:cross_checks,leak_checks,event_checks,recovery_checks,
 witness_sharpness_checks:4*solutions.length,
 solutions:seen,
 integer_denominator_scan_r_le_30:candidates,
 fixed_denominator_cap_example:{cap_r:2,complex_solution:[3,1,2],complex_worst_leak:'1/8',pell_family_cap_r_2_best:'1/2'},
 native_full_Hn_detector_executed:false,
 status:'AUTHOR_SIDE_EXACT_MODEL_CHECK_UNREVIEWED'};
fs.writeFileSync(__dirname+'/RESULTS_PREFIX293.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({combinations:result.total_input_phase_solution_combinations,reads:port_reads,ordered_pair_products:pair_products,gram:gram_checks,samples:candidates.slice(0,12)},null,2));
