
# CSP-NL Project

This project allows you to parse and translate Communicating Sequential Processes (CSP) specifications into natural language.

## Prerequisites

Before running the project, ensure that you have installed the following tools:

1. **Python** (>=3.x)
2. **ANTLR4** (to generate parsers from `.g4` grammar files)
3. **Virtual environment (optional but recommended)**

### 1. Install ANTLR4

#### macOS:
You can install ANTLR4 using Homebrew:

```bash
brew install antlr
```

#### Windows:
1. Download the ANTLR4 jar from [here](https://www.antlr.org/download.html).
2. Set up ANTLR in your environment:
   - Add the ANTLR jar to your `CLASSPATH`:
     ```cmd
     set CLASSPATH=.;C:\path\to\antlr-4.x-complete.jar;%CLASSPATH%
     ```

   - Add an alias for ANTLR in your `.bashrc`, `.bash_profile`, or PowerShell script:

     **For PowerShell**:
     ```powershell
     New-Alias antlr4 'java -jar C:\path\to\antlr-4.x-complete.jar'
     ```

### 2. Set up the project environment

1. Clone the repository:

```bash
git clone https://github.com/waximax/CSP-NL.git
cd CSP-NL
```

2. Set up a virtual environment (optional but recommended):

#### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows:
```cmd
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Generate the ANTLR4 Lexer and Parser

Use the following commands to generate the necessary ANTLR parser and lexer files from the `.g4` grammar file.

#### macOS/Linux:
```bash
antlr4 -Dlanguage=Python3 CSP.g4
antlr4 -Dlanguage=Python3 -visitor CSP.g4
```

#### Windows:
```cmd
java -jar C:\path\to\antlr-4.x-complete.jar -Dlanguage=Python3 CSP.g4
java -jar C:\path\to\antlr-4.x-complete.jar -Dlanguage=Python3 -visitor CSP.g4
```

### 4. Run the project

Once everything is set up, you can run the project using the following commands.

#### Running the tests:

```bash
python3 translate_ast.py example.csp
```

### 5. Start the web application

You can start the web application to interact with the CSP translator via a browser.

1. Activate the virtual environment (if not already activated).
2. Run the application:

#### macOS/Linux:
```bash
source venv/bin/activate
python app.py
```

#### Windows:
```cmd
venv\Scripts\activate
python app.py
```

3. Open the following URLs in your browser:

- For port 5002: [http://127.0.0.1:5002/](http://127.0.0.1:5002/)
- If it doesn't work, try opening the webpage in incognito mode.
---

### Additional Notes:

- Make sure to adjust any paths based on your system configuration (e.g., paths to ANTLR on Windows).
- If you're using Windows, ensure that you have Java installed to run the ANTLR `.jar` file.
