#define main prefix180_original_main
#include "exact_180.cpp"
#undef main
#include <map>
int main(int argc,char**argv){
 if(argc!=2)return 2;setup();ifstream f(argv[1],ios::binary);if(!f)return 2;
 int rows=0,impossibleEvenWith35=0,notImpossibleEvenWith35=0;
 int maxempty=0;map<int,int> empties;map<int,int> minmissing_by_support;
 vector<unsigned char>b(27);
 while(f.read((char*)b.data(),27)){
  array<int,9>q;for(int j=0;j<9;j++)q[j]=b[j];prepare(q);
  int empty=0;
  for(size_t i=0;i<options.size();i++)if(options[i].empty()){
    empty++;minmissing_by_support[sup(T[i])]++;
    if(rows<3 && empty==1) cerr<<"EXAMPLE row="<<rows<<" unrecoverable_target="<<T[i][0]<<","<<T[i][1]<<","<<T[i][2]<<","<<T[i][3]<<"\n";
  }
  empties[empty]++;maxempty=max(maxempty,empty);rows++;
  if(empty)impossibleEvenWith35++;else notImpossibleEvenWith35++;
 }
 if(rows!=67525)return 3;
 cout<<"PREFIX180_EXACT_UNCOVERABILITY rows="<<rows<<" cannot_cover_even_using_all35="<<impossibleEvenWith35
 <<" all35_covers="<<notImpossibleEvenWith35<<" max_empty_target_clauses="<<maxempty<<"\n";
 cout<<"empty_clause_count_distribution=";for(auto [e,n]:empties)cout<<e<<":"<<n<<",";cout<<"\n";
 cout<<"uncoverable_target_support_distribution=";for(auto [e,n]:minmissing_by_support)cout<<e<<":"<<n<<",";cout<<"\n";
}
