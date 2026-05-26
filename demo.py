#!/usr/bin/env python3
"""
在终端输出一个心形。

运行:
	python demo.py

支持彩色输出（如果终端支持 ANSI 颜色）。
"""

def print_heart(char='❤', color=True):
	RED = '\033[91m'
	RESET = '\033[0m'
	height = 15
	width = 30
	for y in range(height, -height - 1, -1):
		line = ''
		for x in range(-width, width + 1):
			xx = x * 0.04
			yy = y * 0.1
			if (xx * xx + yy * yy - 1) ** 3 - (xx * xx) * (yy ** 3) <= 0:
				if color:
					line += f"{RED}{char}{RESET}"
				else:
					line += char
			else:
				line += ' '
		print(line)


if __name__ == '__main__':
	# 尝试在大多数终端显示彩色；在不支持的终端上也能正常显示（会包含控制字符）
	print_heart()
