# botwizer (Final Project Submission)

### 🌟 New OOP-Based Files (For the Final Project Assignment)

* 📂 **[botwizer_automation/](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation)**: Custom OOP automation package.
  * 📄 **[botwizer_automation/\_\_init\_\_.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/__init__.py)**: Initializer for the custom OOP automation package.
  * 📄 **[botwizer_automation/bot_data.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/bot_data.py)**: The Data Holder component containing class implementations of the four OOP pillars:
    * 🧩 **Abstraction**: [TargetingAction](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/bot_data.py#L4-L10) abstract class.
    * 🌿 **Inheritance**: [HashtagTargeter](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/bot_data.py#L13-L30) and [AccountTargeter](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/bot_data.py#L32-L49) subclasses.
    * 🎭 **Polymorphism**: [process_target()](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/bot_data.py#L8) implementation on the subclasses.
    * 🔒 **Encapsulation**: [BotSession](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/bot_data.py#L51-L116) class with private variables and getters/setters with validation.
  * 📄 **[botwizer_automation/run_bot.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/run_bot.py)**: The Importer component containing [BotwizerAutomationRunner](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/botwizer_automation/run_bot.py#L5-L105), which coordinates the interactive CLI flow (using stream input `open(0)` and exception handling blocks matching practice guidelines).
* 🧪 **[test_oop_implementation.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/oop_demo/test_oop_implementation.py)**: The unit test suite verifying the behavior of all OOP principles.
* 📄 **[README.md](file:///C:/Users/pciel/Desktop/botwizer_oop_study/README.md)**: Main repository README documenting the project architecture, presentation slides script, and guidelines (You are here!).

### 📦 Base Project Files (Committed in progressive milestones)

* ⚙️ **Configuration & CI**:
  * 📄 **[.gitignore](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/.gitignore)** / **[.gitattributes](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/.gitattributes)**: Git repository configurations.
  * 📄 **[LICENSE](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/LICENSE)**: MIT License details.
  * 📄 **[Pipfile](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/Pipfile)** / **[Pipfile.lock](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/Pipfile.lock)**: Pipenv package dependency manager specifications.
  * 📄 **[.travis.yml](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/.travis.yml)**: Travis CI configuration.
  * 📄 **[.coveragerc](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/.coveragerc)**: Code coverage configurations.
  * 📄 **[.pre-commit-config.yaml](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/.pre-commit-config.yaml)**: Pre-commit code formatting hooks.
  * 📄 **[conftest.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/conftest.py)** / **[pytest.ini](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/pytest.ini)**: Pytest configurations and shared fixtures.
* 🤖 **Final Project Bot Package**:
  * 📄 **[final_project/\_\_init\_\_.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/__init__.py)** & **[final_project/\_\_main\_\_.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/__main__.py)**: Entry points for the final project execution.
  * 📄 **[final_project/cli.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/cli.py)**: Main command line interface for the botwizer engine.
  * 📂 **[final_project/actions/](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/actions)**: Core action modules implementing specific selenium routines:
    * [pages.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/actions/pages.py), [driver.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/actions/driver.py), [login.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/actions/login.py), [follow.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/actions/follow.py), [comment.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/actions/comment.py), [like.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/actions/like.py), [post.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/actions/post.py), [search.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/actions/search.py), [targeting.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/actions/targeting.py), [user_data.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/actions/user_data.py), [data_folder.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/actions/data_folder.py), [decision.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/actions/decision.py)
  * 📊 **[final_project/user/dashboard.xlsx](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/user/dashboard.xlsx)**: Analytical Excel dashboard for statistics.
  * 👁️ **[final_project/yolo/](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/final_project/yolo)**: YOLO object recognition configs, class names, and image processing scripts.
* 🧪 **Integration Tests**:
  * 📄 **[test_final_project.py](file:///C:/Users/pciel/Desktop/botwizer_oop_study/final_project/test_final_project.py)**: Complete integration test suite for the final project selenium workflow.

## Demo video

[Link to my demo video] — *(replace this with your video link before sending it)*

## License

This is a derivative submission for educational purposes. All rights to the
original code belong to its original author. See the original repo's
[LICENSE](https://github.com/DevGlitch/botwizer/blob/master/LICENSE) (MIT).

