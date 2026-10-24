// R4-EC8 independent C++17 exact checker, positive affine BRC auxiliary model.
#include <boost/multiprecision/cpp_int.hpp>
#include <map>
#include <vector>
#include <tuple>
#include <iostream>
#include <stdexcept>
using boost::multiprecision::cpp_int;
using Key=std::tuple<int,int,int,int>; // (q,r,epsilon,k)
using Tag=std::pair<int,int>;            // (r,epsilon)
using Hist=std::map<Key,cpp_int>;
using Poly=std::map<int,cpp_int>;        // t=epsilon*k
constexpr int Q[3][2]={{2,2},{0,0},{1,2}};
constexpr int ETA[3][2]={{-1,1},{-1,1},{1,1}};
constexpr int B[3][2]={{-1,-1},{-1,-1},{1,-1}};
constexpr int MON[3][2]={{1,0},{2,0},{2,2}};
const std::map<Tag,std::map<std::pair<int,int>,int>> NUM={
 {{0,1},{{{6,0},1},{{4,0},-1},{{2,0},-1},{{1,-1},1}}},
 {{1,1},{{{6,0},-1},{{5,1},1}}},
 {{0,-1},{{{3,1},-1},{{2,2},1}}},
 {{1,-1},{{{5,1},1},{{4,2},-1},{{3,1},1},{{2,2},-1},{{2,0},-1},{{1,1},1}}}
};
void add(Poly& p,int k,const cpp_int& a){ if(a!=0)p[k]+=a; }
void emit(Poly& out,const Poly& in,int shift,int coefficient){
  for(const auto& item:in)add(out,item.first+shift,item.second*coefficient);
}
int main(){
 try{
  Hist hist{{{0,0,1,0},1}};
  std::map<Tag,std::vector<Poly>> series;
  for(const auto& item:NUM)series[item.first]={};
  cpp_int expected=1;
  for(int n=0;n<=100;++n){
   for(const auto& item:NUM){
    const Tag tag=item.first;
    const auto& impulse=item.second;
    auto& rows=series[tag];Poly row;
    for(const auto& term:impulse)
      if(term.first.first==n)add(row,term.first.second,term.second);
    const int lag[]={1,1,2,3,3,4,6,8};
    const int delta[]={1,-1,0,1,-1,0,0,0};
    const int coef[]={1,1,-1,1,1,-2,-1,1};
    for(int i=0;i<8;++i)
      if(n>=lag[i])emit(row,rows[n-lag[i]],delta[i],coef[i]);
    for(auto it=row.begin();it!=row.end();){
      if(it->second==0)it=row.erase(it);
      else {if(it->second<0)throw std::runtime_error("negative count");++it;}
    }
    rows.push_back(std::move(row));
   }
   std::map<Tag,Poly> actual;
   for(const auto& item:NUM)actual[item.first]={};
   cpp_int mass=0;
   for(const auto& item:hist){
    auto [q,r,e,k]=item.first;
    mass+=item.second;
    if(q==2 && r<2)add(actual.at({r,e}),e*k,item.second);
   }
   if(mass!=expected)throw std::runtime_error("raw path mass mismatch");
   for(const auto& item:actual)
     if(item.second!=series.at(item.first).back())
       throw std::runtime_error("scalar recurrence mismatch");
   if(n==100)break;
   Hist next;
   for(const auto& item:hist){
    auto [q,r,e,k]=item.first;
    for(int a=0;a<2;++a){
      next[{Q[q][a],MON[r][a],e*ETA[q][a],ETA[q][a]*k+B[q][a]}]+=item.second;
    }
   }
   hist.swap(next);expected*=2;
  }
  std::cout<<"PASS: independent C++17 exact integer comparison, n=0..100\n";
  return 0;
 }catch(const std::exception& e){
   std::cerr<<"FAIL: "<<e.what()<<"\n";return 1;
 }
}
