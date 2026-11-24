'use strict';
// R5 exact finite regression checks. Run: node VERIFY_R5_RESET_ALGEBRA_RIGIDITY.js
function verify(){
 const assert=(x,m)=>{if(!x)throw Error(m)};
 const set=(u,i,b)=>b?(u|1<<i):(u&~(1<<i));
 let quotients=0, laws=0, fidelity=0, parityWitness=0;
 for(let k=3;k<=8;k++){
   const mask=(1<<k)-1;
   const cost=(f)=>{let n=0;for(let i=0;i<k;i++)if(f&((1<<i)|(1<<((i+1)%k))))n++;return n;};
   for(let f=0;f<=mask;f++){
     const retain=mask^f;
     const pi=u=>u&retain;
     const d=(state,i,b)=>pi(set(state,i,b));
     for(let u=0;u<=mask;u++){
       for(let i=0;i<k;i++)for(let b=0;b<2;b++){
         assert(pi(set(u,i,b))===d(pi(u),i,b),"homomorphism");
         for(let c=0;c<2;c++){
           assert(d(d(pi(u),i,c),i,b)===d(pi(u),i,b),"same-coordinate absorption");
           laws++;
         }
         for(let j=i+1;j<k;j++)for(let c=0;c<2;c++){
           assert(d(d(pi(u),i,b),j,c)===d(d(pi(u),j,c),i,b),"commutation");
           laws++;
         }
         fidelity++;
       }
     }
     const states=new Set(Array.from({length:mask+1},(_,u)=>pi(u)));
     assert(states.size===2**(k-(f.toString(2).replace(/0/g,'').length)),"state count");
     quotients++;
     // For every F and every outer-coordinate value, worst-case slack <= incident cycle-edge count.
     const q=u=>{let n=0;for(let i=0;i<k;i++)n+=((u>>i)&1)*((u>>((i+1)%k))&1);return n;};
     for(let outer=0;outer<=mask;outer++){
       if(outer&f)continue;
       const r=outer|f;
       for(let v=f;;v=(v-1)&f){assert(q(r)-q(outer|v)<=cost(f),"budget");if(v===0)break;}
     }
   }
   // A source-exact controller with one extra toggling label is valid but violates Set idempotence.
   const p=(u,label,i,b)=>({u:set(u,i,b),label:label^1});
   const first=p(0,0,0,1),second=p(first.u,first.label,0,1);
   assert(first.u===second.u && first.label!==second.label,"parity witness");
   parityWitness++;
 }
 return {status:"PASS_R5_RESET_ALGEBRA_RIGIDITY_CONSTRUCTION",cycle_k_range:"3..8",all_projection_quotients:quotients,reset_equations_tested:laws,raw_state_step_tests:fidelity,nonalgebraic_parity_label_witnesses:parityWitness,arithmetic:"exact integer and Boolean",frozen_science_pin:"435e77af0d180eac32bd1f9c4c464bc4010b7551",independent_review:"NOT_REVIEWED"};
}
console.log(JSON.stringify(verify(),null,2));
