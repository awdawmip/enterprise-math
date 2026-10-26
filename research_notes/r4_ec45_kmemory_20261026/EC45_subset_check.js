// Independent BigInt subset-cost audit for EC45. No dependencies.
const p=[20n,10n,1n], q=[1n,10n,20n];
const min3=(a,b,c)=>a<b?(a<c?a:c):(b<c?b:c);
const table=[];
for(let mask=1;mask<8;mask++){
 let pp=0n,qq=0n;
 for(let i=0;i<3;i++)if(mask&(1<<i)){pp+=p[i];qq+=q[i]}
 const cont=pp+qq+(9n*pp<qq?9n*pp:qq)+(pp<9n*qq?pp:9n*qq);
 const v=min3(10n*qq,10n*pp,cont);
 table.push({mask,p:String(pp),q:String(qq),value:String(v)});
}
const want={'1':'10','2':'40','4':'10','3':'82','6':'82','5':'84','7':'124'};
for(const t of table){if(t.value!==want[String(t.mask)])throw Error('Mismatch '+JSON.stringify(t))}
const b1=124n;
const b2=[BigInt(want['1'])+BigInt(want['6']),BigInt(want['2'])+BigInt(want['5']),BigInt(want['3'])+BigInt(want['4'])].reduce((a,b)=>a<b?a:b);
const b3=BigInt(want['1'])+BigInt(want['2'])+BigInt(want['4']);
if(b1!==124n ||b2!==92n ||b3!==60n)throw Error('partition fail');
console.log(JSON.stringify({passed:true,subset_table:table,minimum_cost_without_baseline:{K1:String(b1),K2:String(b2),K3:String(b3)},minimum_objective_over_310:{K1:String(b1+124n),K2:String(b2+124n),K3:String(b3+124n)}}));
