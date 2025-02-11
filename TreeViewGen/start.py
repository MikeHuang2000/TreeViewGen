import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path)
# 调用示例：从文件读取输入并生成目录树文件
import TreeViewGen  # 替换为实际模块名

def process_file(input_path, output_path):
    # 读取输入文件
    with open(input_path, 'r', encoding='utf-8') as f:
        input_lines = f.readlines()
    
    # 生成目录树文本
    tree_text = TreeViewGen.generate_treeview(input_lines)
    
    # 写入输出文件
    with open(output_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(tree_text)

# 使用示例
process_file('input.txt', 'output.txt')