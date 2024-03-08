# Lever Compiler

**Compiler for a BASIC-like language that translates source code into equivalent C code.**

## Overview

 Compiler is designed to transform high-level code written in a BASIC-like language into equivalent C code, facilitating easy execution on a variety of platforms.

## Features

- **BASIC-Like Syntax:** Familiar and intuitive syntax inspired by the BASIC programming language family.
- **Python-Based Compiler:** Implemented using Python for flexibility, readability, and ease of maintenance.
- **C Code Generation:** Translates source code into equivalent C code for portability and execution on diverse platforms.
- **Lexer and Parser:** Incorporates a robust lexer and parser for accurate tokenization and syntax analysis.
- **Intermediate Representation:** Utilizes abstract syntax trees (ASTs) for efficient intermediate representation during the compilation process.

## Getting Started

### Prerequisites

- Python 3.9

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SheldonDacon/BASIC-to-C
    ```

2. Navigate to the project directory:

    ```bash
    cd lever-compiler
    ```

3. Run the compiler:

    ```bash
    python BasictoC.py main.py
    ```

## Usage
```
An example BASIC snippet code that can be compiled:

INPUT nums
PRINT ""

LET a = 0
LET b = 1
WHILE nums > 0 REPEAT
    PRINT a
    LET c = a + b
    LET a = b
    LET b = c
    LET nums = nums - 1
ENDWHILE
```
