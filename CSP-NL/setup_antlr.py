import subprocess

def setup_antlr():
    # 生成基础的解析器和词法分析器
    antlr_basic_command = "/opt/homebrew/bin/antlr4 -Dlanguage=Python3 CSP.g4"
    subprocess.run(antlr_basic_command, shell=True, check=True)

    # 生成包含访问者的解析器
    antlr_visitor_command = "/opt/homebrew/bin/antlr4 -Dlanguage=Python3 -visitor CSP.g4"
    subprocess.run(antlr_visitor_command, shell=True, check=True)

def run_translation_example():
    # 使用 python3 运行翻译示例脚本
    translation_command = "python3 translate_ast.py example.csp"
    subprocess.run(translation_command, shell=True, check=True)

if __name__ == "__main__":
    setup_antlr()
    run_translation_example()
