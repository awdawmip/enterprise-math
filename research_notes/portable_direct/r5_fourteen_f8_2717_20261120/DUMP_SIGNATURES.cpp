#define main solver14_unused
#include "SOLVE_F8_14.cpp"
#undef main
int main(int argc,char**argv){
 if(argc<4)return 2;
 ifstream fd(argv[1],ios::binary);vector<uint8_t>adj((size_t)Q*N*N);
 fd.read((char*)adj.data(),adj.size());if(fd.gcount()!=(streamsize)adj.size())return 3;
 int u=stoi(argv[2]),v=stoi(argv[3]);auto s=signature(adj,u,v);
 cout<<"{\"u\":"<<u<<",\"v\":"<<v<<",\"actions\":[";
 for(size_t i=0;i<s.size();i++){if(i)cout<<",";
  cout<<"{\"cost\":"<<s[i].cost<<",\"masks\":[";
  for(size_t j=0;j<s[i].masks.size();j++){if(j)cout<<",";cout<<s[i].masks[j];}
  cout<<"]}";
 }
 cout<<"]}\n";
}
