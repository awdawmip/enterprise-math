#define main unused_solver_main
#include "front_orbit_min.cpp"
#undef main
#include <cassert>
#include <random>

int main(int argc,char**argv){
 init_actions(argv[2]);
 vector<M> classes;
 ifstream db(argv[1],ios::binary);struct BR{uint64_t lo,hi;unsigned c,s;};BR row;
 while(db.read((char*)&row,sizeof(row)))if((row.s&255)==11&&row.c==936)classes.push_back(M(row.lo)|(M(row.hi)<<64));
 assert(classes.size()==4500);
 ifstream cf(string(argv[2])+"/cores2.txt");uint64_t lo,hi;int c,d;set<M> frames;
 while(cf>>lo>>hi>>c>>d){M f=M(lo)|(M(hi)<<64);for(int h=0;h<4;h++){
  M g=f;bool okay=true;for(auto[bit,point]:{pair{1,c},pair{2,d}})if(h&bit){M z=M(1)<<point;if(!(g&z)){okay=false;break;}g^=z;}
  if(okay)frames.insert(g);
 }}
 mt19937_64 rng(9861);int checked=0,tied=0,nontrivial_frames=0,empty_pools=0;map<int,int> stabilizers;
 for(M free:frames){
  vector<const Action*> group;for(const auto&a:affine_actions)if(image(FULL^free,a)==(FULL^free))group.push_back(&a);
  ++stabilizers[group.size()];if(group.size()==1)continue;++nontrivial_frames;
  vector<M> pool;map<M,M> minima;
  for(M m:classes)if((m&free)==m){M best=m;for(const auto*a:group)best=min(best,image(m,*a));pool.push_back(m);minima[m]=best;}
  if(pool.empty()){++empty_pools;continue;}
  auto verify=[&](const vector<M>&selected){
   M wanted=FULL;for(M m:selected)wanted=min(wanted,minima.at(m));bool okay=false;
   for(const auto*a:group){
    vector<M> transformed;for(M m:selected)transformed.push_back(image(m,*a));sort(transformed.begin(),transformed.end());
    if(transformed.front()!=wanted)continue;
    bool valid=true;for(int i=0;i<transformed.size();i++){
     M m=transformed[i];assert(minima.count(m));
     if(minima.at(m)<wanted||(i&&m<=wanted))valid=false;
    }
    if(valid){okay=true;break;}
   }
   assert(okay);++checked;
  };
  for(int trial=0;trial<100;trial++){
   vector<M> selected;M used=0;bool complete=true;
   for(int i=0;i<1+trial%3;i++){
    bool found=false;for(int attempt=0;attempt<100000;attempt++){M m=pool[rng()%pool.size()];if(!(m&used)){selected.push_back(m);used|=m;found=true;break;}}
    if(!found){complete=false;break;}
   }
   if(complete)verify(selected);
  }
  bool found_tie=false;
  for(M m:pool){
   for(const auto*a:group){M q=image(m,*a);if(!(m&q)){assert(minima.at(m)==minima.at(q));verify({m,q});++tied;found_tie=true;break;}}
   if(found_tie)break;
  }
 }
 cout<<"{\"fixed_core_frames\":"<<frames.size()<<",\"nontrivial_stabilizer_frames\":"<<nontrivial_frames
     <<",\"empty_candidate_pools\":"<<empty_pools<<",\"selected_class_sets_checked\":"<<checked<<",\"same_orbit_pairs_checked\":"<<tied<<",\"stabilizer_orders\":{";
 bool comma=false;for(auto[k,n]:stabilizers){if(comma)cout<<",";cout<<"\""<<k<<"\":"<<n;comma=true;}cout<<"}}"<<endl;
}
