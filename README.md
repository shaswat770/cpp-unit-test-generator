# C++ Unit Test Generator using LLM

## Overview
This project implements an automated unit test generator for C++ applications using a Large Language Model (LLM). The tool generates initial unit tests, refines them iteratively, and improves test coverage by integrating build feedback and coverage data.

## Features
- Automatic generation of Google Test unit tests for C++ source files.
- Iterative refinement of tests via LLM prompts.
- Build error handling with LLM assistance.
- Integration with GNU coverage tools (`gcov`, `lcov`).
- YAML-driven strict prompt instructions for LLM guidance.

## Project Structure
- `/tests` : Contains all generated and refined test files.
- `instructions.yaml` : YAML prompts used for initial and follow-up test generation.
- `CMakeLists.txt` or `Makefile` : Build configuration to compile tests.
- `README.md` : This documentation file.

## Build and Run
```bash
mkdir build
cd build
cmake ..
make
./runTests
