<p align="center">
  <img src="https://img.shields.io/badge/🤖_Botwizer-OOP_Instagram_Automation-3B82F6?style=for-the-badge&logoColor=white" alt="Botwizer Badge" />
</p>

<h1 align="center">🤖 Botwizer - OOP Instagram Automation CLI</h1>

<p align="center">
  <strong>Automate. Target. Classify OOP.</strong>
</p>

<p align="center">
  A class-based CLI-driven Instagram automation simulation project designed as a study for Object-Oriented Programming (OOP) principles. It demonstrates the implementation of the four OOP pillars and strictly complies with defined coding standards.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/OOP-Principles-10B981?style=flat-square" alt="OOP Principles" />
  <img src="https://img.shields.io/badge/Unittest-Standard_Library-FF6B6B?style=flat-square&logo=python" alt="Unittest" />
  <img src="https://img.shields.io/badge/PEP--8-Compliant-FFD43B?style=flat-square&logo=python&logoColor=black" alt="PEP 8" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Original_Project-botwizer-000000?style=flat-square&logo=github&logoColor=white" alt="Original Project" />
  <img src="https://img.shields.io/badge/Source-GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" />
</p>

<p align="center">
  <a href="#-introduction">Introduction</a> •
  <a href="#-object-oriented-programming-oop-principles">OOP Principles</a> •
  <a href="#-coding-standards-compliance">Coding Standards</a> •
  <a href="#-project-structure">Project Structure</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-team">Team</a> •
  <a href="#-license">License</a>
</p>

---

## 📖 Introduction

**Botwizer - OOP Instagram Automation CLI** is a structured Python demonstration for the Final Project, based on the original **botwizer** automation bot. It simulates Instagram bot actions such as liking posts, posting comments, and following accounts, utilizing a terminal-driven flow instead of direct web scraping.

> 💡 **Designed for Educational Purposes**, this codebase showcases clean software engineering practices under Python including data encapsulation, class inheritance, abstract modeling, runtime polymorphism, exception handling, and input stream manipulation.

* **Original Project Link**: [https://github.com/DevGlitch/botwizer](https://github.com/DevGlitch/botwizer)

---

## 🏛️ Object-Oriented Programming (OOP) Principles

The project codebase under the `botwizer_automation` package implements the four core pillars of OOP:

| Principle | Description | Implementation Link |
| :--- | :--- | :--- |
| **Abstraction** | Hides execution complexity and defines strict interface structures using abstract classes. | [bot_data.py (TargetingAction)](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/bot_data.py#L4-L10) |
| **Inheritance** | Establishes a hierarchical relationship to share variables/methods and reuse code. | [bot_data.py (HashtagTargeter / AccountTargeter)](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/bot_data.py#L13-L49) |
| **Polymorphism** | Allows multiple subclasses to have different implementations of the same method, executed dynamically. | [bot_data.py (process_target)](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/bot_data.py#L16-L48) & [run_bot.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/run_bot.py#L80-L88) |
| **Encapsulation** | Restricts direct access to class attributes using private fields and exposes them safely via getters/setters. | [bot_data.py (BotSession)](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/bot_data.py#L51-L116) |

### Detailed Breakdown

#### 1. Abstraction
* **Class / Link**: [TargetingAction](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/bot_data.py#L4-L10)
* **Details**: Represents a high-level abstraction of any target processing behavior. It inherits from Python's abstract base class (`abc.ABC`) and declares the abstract method `process_target(self, target_name)`. It cannot be instantiated directly, hiding the internal implementation details and enforcing a common interface contract.

#### 2. Inheritance
* **Classes / Link**: [HashtagTargeter and AccountTargeter](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/bot_data.py#L13-L49)
* **Details**: The subclasses `HashtagTargeter` and `AccountTargeter` inherit from the `TargetingAction` base class. This relationship ensures they automatically reuse the common contract and type hierarchies defined by the base class while implementing specific behaviors for hashtag scanning and account profile scraping.

#### 3. Polymorphism
* **Method / Link**: [process_target(self, target_name)](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/bot_data.py#L16-L48) & [run_bot.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/run_bot.py#L80-L88)
* **Details**: Both `HashtagTargeter` and `AccountTargeter` override the `process_target` method to execute distinct simulation logic. In `run_bot.py`, the runner loops through targets dynamically and invokes `targeter.process_target(target_item)` at runtime. Depending on the runtime targeter object, the correct implementation executes seamlessly without the caller needing to know the exact subclass type.

#### 4. Encapsulation
* **Class / Link**: [BotSession](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/bot_data.py#L51-L116)
* **Details**: The `BotSession` class protects its critical state (e.g., `__username`, `__password`, `__targets`, and `__comments`) using private double leading underscores (`__`) to enforce private access control. These variables cannot be accessed or modified directly from outside the class. Access is strictly controlled through getter and setter methods (`get_username()`, `set_password()`, etc.) that contain try-except blocks to validate input data (e.g., ensuring passwords are at least 6 characters long and fields are not empty).

---

## 📋 Coding Standards Compliance

The codebase strictly adheres to the requested coding guidelines:

| Standard / Rule | Guideline | Codebase Implementation |
| :--- | :--- | :--- |
| **Class-Based Structure** | Every program must be class-based with a single `run()` method containing operational variables. | Main runner is `BotwizerAutomationRunner` in [run_bot.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/run_bot.py) which exposes only the `.run()` method. |
| **Variables Scope** | Operational variables must live inside `run()` method. | Variables (e.g. `self.username_input`, `self.password_input`, lists) reside strictly inside the `.run()` method scope. |
| **Input Stream Handling** | Input stream must be opened via `open(0)` and properly closed at the end of the method. | The stream is defined as `self.input_file = open(0)` and closed inside a `finally` block via `self.input_file.close()`. |
| **Exception Handling** | Implement `try-except` blocks around risky code and user input parsing. | Covered comprehensively inside setters of `BotSession` and user input prompts in `run_bot.py`. |
| **File Architecture** | Separate the data holder from the importer. | `bot_data.py` operates as the data holder containing models. `run_bot.py` operates as the importer/runner class. |
| **Input Loops** | Handle user lists collection gracefully until an empty line is received. | Implemented using interactive `while True` readline loops, breaking when target strings are empty. |
| **Naming Conventions** | Descriptive snake_case for methods/variables, PascalCase for classes. No single-letter names. | Clean descriptors used throughout (e.g., `error`, `target_item`, `runner`). Zero instances of single-letter variable names. |
| **Comments** | Short, direct, human-written, active-voice comments. No tutorials. | Simple comments (e.g., `# Read username from stdin`, `# Simulate searching hashtag`). |

---

## 📁 Project Structure & File Details

```
botwizer_oop_study/
├── 📂 oop_demo/                 # OOP study demonstration files
│   ├── 📂 botwizer_automation/  # Core package demonstrating OOP
│   │   ├── __init__.py          # Package initializer
│   │   ├── bot_data.py          # Data holder class (OOP Models)
│   │   └── run_bot.py           # Importer / runner class (CLI Main)
│   └── test_oop_implementation.py # OOP Unit test suite
├── 📂 final_project/            # Full-featured Instagram bot
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py                   # Main CLI execution script
│   ├── 📂 actions/              # Selenium automation modules
│   ├── 📂 user/                 # Excel/Parquet dashboard definitions
│   └── 📂 yolo/                 # YOLO Image processing modules
│   ├── conftest.py              # Pytest configuration
│   ├── pytest.ini               # Pytest configurations
│   ├── test_final_project.py    # Integration test suite for final project
│   ├── .coveragerc              # Coverage configuration
│   ├── .gitignore               # Git ignore rules
│   ├── .gitattributes           # Git attributes configuration
│   ├── LICENSE                  # MIT License details
│   ├── Pipfile                  # Pipenv Pipfile
│   ├── Pipfile.lock             # Pipenv lockfile
│   ├── .travis.yml              # Travis CI configuration
│   └── .pre-commit-config.yaml  # Pre-commit hooks configuration
└── README.md                    # Main repository README (You are here!)
```

---

## ⚡ Getting Started

### 📋 Prerequisites

Ensure you have Python installed on your system:
* **Python**: `≥ 3.8` (Standard distributions on Windows, macOS, or Linux)

### ⚡ Running the Program

1. Open your terminal or GitBash.
2. Navigate to the `oop_demo` directory:
   ```bash
   cd oop_demo
   ```
3. Run the main runner file:
   ```bash
   python -m botwizer_automation.run_bot
   ```
4. Follow the prompts on the standard input:
   * Enter your username (must not be empty).
   * Enter your password (must be at least 6 characters).
   * Choose target type (1 for Hashtag, 2 for Account).
   * Enter target items (one per line, press Enter on an empty line to stop).
   * Enter comment texts (one per line, press Enter on an empty line to stop).

### 🧪 Running the Verification Tests

Execute the unit tests verifying Abstraction, Inheritance, Polymorphism, and Encapsulation compliance:
1. Navigate to the `oop_demo` directory:
   ```bash
   cd oop_demo
   ```
2. Run the tests:
   ```bash
   python -m unittest test_oop_implementation.py
   ```

---

## 👥 Team

<table>
  <tr>
    <td align="center" width="100%">
      <strong>Elle</strong><br/>
      <sub>Student Developer</sub><br/>
      <sub>GitHub: <a href="https://github.com/TechyElle">TechyElle</a></sub>
    </td>
  </tr>
</table>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- Built as a final OOP study course project.
- Original Instagram automation blueprint from **[botwizer by DevGlitch](https://github.com/DevGlitch/botwizer)**.

---

<p align="center">
  <strong>Built with 💙 for OOP Excellence</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made_with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Powered_by-OOP-10B981?style=for-the-badge&logo=codeforces&logoColor=white" />
  <img src="https://img.shields.io/badge/Verified-Unittest-FF6B6B?style=for-the-badge&logo=githubactions&logoColor=white" />
</p>
