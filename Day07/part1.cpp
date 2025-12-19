#include <iostream>
#include <fstream>
#include <string>
#include <vector>



int main() {
	std::ifstream fin("input.txt");
	std::string line;

	if (!fin.is_open()) {
		std::cout << "Error: Cannot open file!" << std::endl;
		return 1;
	}

	std::vector<std::string> lines;
	while (std::getline(fin, line)) {
		lines.push_back(line);
	}

	const size_t rows = lines.size();
	const size_t cols = lines[0].length();

	std::vector<bool> tachyon(cols, false);
	int countSplit = 0;

	tachyon[lines[0].find('S')] = true;

	for (int i = 1; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			if (lines[i][j] == '^' && tachyon[j]) {
				if (j > 0) tachyon[j-1] = true;
				if (j < cols-1) tachyon[j+1] = true;
				tachyon[j] = false;
				countSplit++;
			}
		}
	}



	fin.close();

	std::cout << "The answer is: " << countSplit << std::endl;

	return 0;
}
