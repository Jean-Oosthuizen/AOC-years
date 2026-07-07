#include <string>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;


void part1(){
    ifstream file("input4.txt");
    int delim_position = -1, templine_delim_position = -1, answer = 0;
    vector<int> tasks_1 = {0, 0};
    vector<int> tasks_2 = {0, 0};
    string line, templine;
    while(getline(file, line)){
        delim_position = line.find(",");
        
        templine = line.substr(0, delim_position);
        templine_delim_position = templine.find('-');
        tasks_1[0] = stoi(templine.substr(0, templine_delim_position));
        tasks_1[1] = stoi(templine.substr(templine_delim_position + 1, templine.size()));
        
        templine = line.substr(delim_position + 1, line.size());
        templine_delim_position = templine.find('-');
        tasks_2[0] = stoi(templine.substr(0, templine_delim_position));
        tasks_2[1] = stoi(templine.substr(templine_delim_position + 1, templine.size()));
        // cout << tasks_1[0] << "-" << tasks_1[1] << "," << tasks_2[0] << "-" << tasks_2[1] << "\n";

        if(
            tasks_1[0] <= tasks_2[0] && tasks_2[1] <= tasks_1[1]
            || tasks_2[0] <= tasks_1[0] && tasks_1[1] <= tasks_2[1]
        ){
            answer += 1;
        }
    }
    cout << answer << "\n";
}

void part2(){
    ifstream file("input4.txt");
    int delim_position = -1, templine_delim_position = -1, answer = 0, count = 0;
    vector<int> tasks_1 = {0, 0};
    vector<int> tasks_2 = {0, 0};
    string line, templine;
    while(getline(file, line)){
        count ++;

        delim_position = line.find(",");
        
        templine = line.substr(0, delim_position);
        templine_delim_position = templine.find('-');
        tasks_1[0] = stoi(templine.substr(0, templine_delim_position));
        tasks_1[1] = stoi(templine.substr(templine_delim_position + 1, templine.size()));
        
        templine = line.substr(delim_position + 1, line.size());
        templine_delim_position = templine.find('-');
        tasks_2[0] = stoi(templine.substr(0, templine_delim_position));
        tasks_2[1] = stoi(templine.substr(templine_delim_position + 1, templine.size()));

        // cout << tasks_1[0] << "-" << tasks_1[1] << "," << tasks_2[0] << "-" << tasks_2[1] << "\n";

        if(tasks_1[1] < tasks_2[0] || tasks_2[1] < tasks_1[0]){
            answer += 1;
        }
    }
    cout << count - answer << "\n";
}

int main(){
    part1();
    part2();
    return 0;
}