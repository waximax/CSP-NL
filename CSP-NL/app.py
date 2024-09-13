import sys
import io
from flask import Flask, render_template, request, jsonify
from antlr4 import *
from CSPParser import CSPParser
from CSPLexer import CSPLexer
from translate_ast import CSPToASTVisitor  # Import the CSPToASTVisitor from translate_ast.py

app = Flask(__name__)

# Route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the translation request
@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    csp_code = data.get('cspCode')

    if not csp_code:
        return jsonify({'result': 'No CSP code provided.'}), 400

    # Capture the printed output of the visitor
    old_stdout = sys.stdout  # Backup the current stdout
    sys.stdout = io.StringIO()  # Redirect stdout to a buffer

    try:
        # Translation logic: Parse and generate output
        input_stream = InputStream(csp_code)
        lexer = CSPLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CSPParser(stream)
        tree = parser.cspFile()

        # Visit the parsed tree using the CSPToASTVisitor
        visitor = CSPToASTVisitor()
        visitor.visit(tree)

        # Get the printed output
        translation_result = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout  # Restore the original stdout

    return jsonify({'result': translation_result})


if __name__ == '__main__':
    app.run(debug=True, port=5002)
