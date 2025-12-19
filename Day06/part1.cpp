#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#define ll long long int



int main() {
	std::ifstream fin("input.txt");
	const size_t indexOfOperationLine = 4;

	std::string line;

	if (!fin.is_open()) {
		std::cout << "Error: Cannot open file!" << std::endl;
		return 1;
	}

	std::vector<std::vector<ll>> grid;

	for (int i = 0; i < indexOfOperationLine; ++i) {
		std::getline(fin, line);
		std::istringstream iss(line);
		ll num;

		grid.push_back(std::vector<ll>());
		while (iss >> num) {
			grid[i].push_back(num);
		}
	}

	std::getline(fin, line);
	std::istringstream iss(line);
	char op;

	std::vector<char> ops;
	while (iss >> op) {
		ops.push_back(op);
	}

	ll output = 0;
	for (int i = 0; i < grid[0].size(); i++) {
		if (ops[i] == '*') {
			ll res = 1;
			for (int j = 0; j < grid.size(); j++) {
				res *= grid[j][i];
			}
			output += res;
		} else {
			ll res = 0;
			for (int j = 0; j < grid.size(); j++) {
				res += grid[j][i];
			}
			output += res;
		}
	}



	fin.close();

	std::cout << "The answer is: " << output << std::endl;

	return 0;
}
