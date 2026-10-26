"use strict";
// EC48G exact test: all <=5-history, two-label ternary breakpoint
// templates with <=2 one-sided profiles; integer encoders/decoders.
const T=[-1,0,1], ROWS=[];for(const x of T)for(const y of T)ROWS.push([x,y]);
const P=[0,1,3,6,7], bit=w=>[w>>1,w&1], scale=w=>bit(w).map(x=>7*x);
const interp=(b,a,n)=>bit(b).map((x,i)=>(7-n)*x+n*bit(a)[i]);
const encode=a=>2*a[0]+a[1], uniq=xs=>[...new Set(xs)].sort((a,b)=>a-b);
const stat={schema:"EM_R4_EC48G_SIGN_TEMPLATE_AUDIT_V1",H_checked:[1,2,3,4,5],
 patterns_examined:0,qualifying_templates:0,shared_signature_templates:0,
 disjoint_signature_templates:0,disjoint_2_by_2_templates:0,
 policy_samples:0,individual_cell_checks:0,strict_profile_checks:0,
 monotone_segment_checks:0,status:"PASS"};
function ok(z,s){if(!z)throw Error(s)}
function run(rows){
 const lo=rows.map(r=>encode(r.map(x=>x>0?1:0))),hi=rows.map(r=>encode(r.map(x=>x>=0?1:0)));
 const B=uniq(lo),A=uniq(hi);
 if(B.length>2||A.length>2||!rows.some(r=>r.includes(0)))return;
 stat.qualifying_templates++;
 const common=A.filter(x=>B.includes(x)),stages=[];
 if(common.length){
   stat.shared_signature_templates++;
   const c=common[0],b=B.find(x=>x!==c)??c,a=A.find(x=>x!==c)??c;
   for(let stage=0;stage<3;stage++)stages.push(n=>{
      const bank=[scale(c),stage===0?scale(b):stage===1?interp(b,a,n):scale(a)];
      const pi=lo.map((v,h)=>{
        const z=hi[h];
        if(v===c&&z===c)return [7,0];
        if(z===c)return stage===0?[n,7-n]:[7,0];
        if(v===c)return stage===2?[7-n,n]:[7,0];
        return [0,7];
      });return {bank,pi};
   });
 }else{
   stat.disjoint_signature_templates++;
   if(B.length===1){
     stages.push(n=>({bank:A.map(a=>interp(B[0],a,n)),pi:hi.map(v=>A.map(x=>x===v?7:0))}));
   }else if(A.length===1){
     stages.push(n=>({bank:B.map(b=>interp(b,A[0],n)),pi:lo.map(v=>B.map(x=>x===v?7:0))}));
   }else{
     stat.disjoint_2_by_2_templates++;
     const horizontal=B.join(",")==="0,1"&&A.join(",")==="2,3";
     const vertical=B.join(",")==="0,2"&&A.join(",")==="1,3";
     ok(horizontal||vertical,"invalid disjoint 2x2");
     stages.push(n=>{
       const bank=horizontal?[[n,0],[n,7]]:[[0,n],[7,n]];
       const pi=lo.map((v,h)=>{
          const a=hi[h];
          if(v===0&&a===3)return [7-n,n];
          if(horizontal&&v===0&&a===2)return [7,0];
          if(horizontal&&v===1&&a===3)return [0,7];
          if(vertical&&v===0&&a===1)return [7,0];
          if(vertical&&v===2&&a===3)return [0,7];
          throw Error("unclassified history");
       });return {bank,pi};
     });
   }
 }
 let previous=null,initial=null;
 for(const fn of stages){
   let oldMass=-1;
   for(const n of P){
     const {bank,pi}=fn(n),out=[];
     ok(bank.length<=2,"too many states");
     for(let h=0;h<rows.length;h++){
       ok(pi[h].length===bank.length&&pi[h].every(v=>v>=0&&v<=7)&&pi[h].reduce((a,b)=>a+b,0)===7,"bad encoder");
       const row=[];
       for(let y=0;y<2;y++){
          const x=bank.reduce((acc,vec,i)=>acc+pi[h][i]*vec[y],0);
          ok(x>=bit(lo[h])[y]*49&&x<=bit(hi[h])[y]*49,"sign violation");
          row.push(x);stat.individual_cell_checks++;
          if(bit(lo[h])[y]===bit(hi[h])[y])stat.strict_profile_checks++;
       }out.push(row);
     }
     const mass=rows.reduce((s,rs,h)=>s+rs.reduce((t,x,y)=>t+(x===0?out[h][y]:0),0),0);
     ok(mass>=oldMass,"decreasing tie mass");
     oldMass=mass;stat.policy_samples++;
     if(n===0){if(previous!==null)ok(JSON.stringify(previous)===JSON.stringify(out),"stage discontinuity");else initial=out;}
     if(n===7)previous=out;
   }stat.monotone_segment_checks++;
 }
 const words49=x=>x.map(scale).map(row=>row.map(v=>7*v));
 ok(JSON.stringify(initial)===JSON.stringify(words49(lo)),"initial kernel mismatch");
 ok(JSON.stringify(previous)===JSON.stringify(words49(hi)),"final kernel mismatch");
}
for(let H=1;H<=5;H++){
 let total=9**H;
 for(let t=0;t<total;t++){
   let z=t,rs=[];for(let h=0;h<H;h++){rs.push(ROWS[z%9]);z=Math.floor(z/9);}
   stat.patterns_examined++;run(rs);
 }
}
console.log(JSON.stringify(stat,null,2));
