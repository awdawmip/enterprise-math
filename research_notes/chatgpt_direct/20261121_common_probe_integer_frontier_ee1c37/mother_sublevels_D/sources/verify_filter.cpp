
#define main inherited_main
#include "native_original.cpp"
#undef main
#include <cassert>
#include <map>
#include <set>
struct Record{W lo,hi;unsigned cost,size;};
int main(int argc,char**argv){
  ifstream ob(argv[1],ios::binary),pp(argv[2]),bank(argv[3],ios::binary);
  ofstream out(argv[4],ios::binary);assert(ob&&pp&&bank&&out);
  int caps[14];ifstream capfile(argv[5]);for(int&v:caps)capfile>>v;assert(capfile);
  ob.read((char*)obs,sizeof(obs));assert(ob.gcount()==sizeof(obs));array<unsigned char,3>tr;
  while(ob.read((char*)tr.data(),3))do{bad[tr[0]][tr[1]]|=M(1)<<tr[2];}while(next_permutation(tr.begin(),tr.end()));
  array<M,250> parents;for(auto&m:parents){W lo,hi;pp>>lo>>hi;m=M(hi)<<64|lo;assert(card(m)==13);for(M q=m;q;q&=q-1)containing[at(q)].push_back(m);}
  set<M> seen;map<pair<int,int>,array<long long,2>>counts;Record r;
  vector<Record> proper;
  while(bank.read((char*)&r,sizeof(r))){
    int s=r.size%256;M mask=M(r.hi)<<64|r.lo;assert(s>=8&&s<=10);assert(card(mask)==s);
    assert(r.cost<=unsigned(caps[s]));assert(seen.insert(mask).second);
    assert(price(mask)==int(r.cost));
    for(M a=mask;a;a&=a-1)for(M b=a&(a-1);b;b&=b-1)assert(!(bad[at(a)][at(b)]&mask));
    ++counts[{s,r.cost}][0];bool embedded=false;
    for(M mother:containing[at(mask)])if(!(mask&~mother)){embedded=true;break;}
    if(!embedded){++counts[{s,r.cost}][1];r.size=s;proper.push_back(r);}
  }
  sort(proper.begin(),proper.end(),[](Record a,Record b){if(a.size!=b.size)return a.size<b.size;if(a.cost!=b.cost)return a.cost<b.cost;if(a.hi!=b.hi)return a.hi<b.hi;return a.lo<b.lo;});
  for(auto r:proper)out.write((char*)&r,sizeof(r));
  for(auto [type,number]:counts)cout<<type.first<<" "<<type.second<<" "<<number[0]<<" "<<number[1]<<"\n";
}
