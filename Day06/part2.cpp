#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#define ll long long int



ll ctoll(char c) { return static_cast<ll>(c - '0'); }

int main() {
	std::ifstream fin("input.txt");
	const size_t indexOfOperationLine = 4;

	std::string line;

	if (!fin.is_open()) {
		std::cout << "Error: Cannot open file!" << std::endl;
		return 1;
	}

	std::vector<std::string> lines;
	while (std::getline(fin, line)) {
		lines.push_back(line);
	}

	ll output = 0;

	const size_t len = lines[0].length();
	
	bool isMult = false;
	std::vector<ll> numbers;
	for (int col = len - 1; col >= 0; col--) {
		bool newprob = true;
		for (int row = indexOfOperationLine; row >= 0; row--) {
			if (lines[row][col] != ' ') {
				newprob = false;
				break;
			}
		}

		if (newprob) {
			ll problem = isMult ? 1 : 0;
			for (const ll& num : numbers) {
				if (isMult) problem *= num;
				else problem += num;
			}
			output += problem;

			numbers.clear();
			isMult = false;
		} else {
			ll num = 0;
			for (int row = 0; row < indexOfOperationLine; row++) {
				if (lines[row][col] != ' ') {
					num *= 10;
					num += ctoll(lines[row][col]);
				}
			}
			numbers.push_back(num);

			if (lines[indexOfOperationLine][col] == '*') {
				isMult = true;
			}
		}
	}

	ll problem = isMult ? 1 : 0;
	for (const ll& num : numbers) {
		if (isMult) problem *= num;
		else problem += num;
	}
	output += problem;

	numbers.clear();
	isMult = false;



	fin.close();

	std::cout << "The answer is: " << output << std::endl;

	return 0;
}
