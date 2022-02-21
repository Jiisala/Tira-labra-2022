# Jaakko's Dungeon generator

Project is set up using poetry, but simply for running the program no exotic dependencies are needed, just run launch.py. All dependencies are testing or code formatting related. The program however expects you to run it from the root directory. This is because of the write to file functionality, the current verson has it set to true by default, I will change that for next version.

While using the program use commands Q to quit, C to create new map, S to open settings view and B to get back to main view, all are case insensitive.

if the output to console is messy and unreadable, first ensure that the console window is wide enough to fit full lines of the map, so that no unwanted linebreaks happen.

You should be able to alter the general look of the dungeon a great deal by playing with the settings, so I recommend doing some manual testing. Testing document with pre-generated dungeons to illustrate this is on the way. The settings should be constrained so that it is not possible to crash the program, but I have not yet done enough testing to ensure it. The path to the filewriter is not really monitored at the time of changing the settings, but there probably is no need to change it. If invalid path is given, the program won't crash, but will not create maps either (if "write map to file" is set true).

The program is called dungeon generator, but really the resulting patterns can be used for variety of different purposes. I have designed this mainly level maps in mind, but that should not discourage other possibilities.

Detailed explanation of the algorithms can be found in the Implementation report. Link to it is bit further bellow. It is still work in progress, but it should be complete enough to understand what is happening inside the program. 

**NOTE TO FOR THE PERSON DOING CODE REVIEW** 

The last weeks author of code review had some difficulties in running the program. I do not have information of the authors set-up, so figuring out the cause of the error was bit hit or miss. The program is developed with cubbli linux, if you are using that everything should work. I isolated two possible culprits for the failure of the last week. One was the write to file functionality, if that causes problems, just turn it of from the settings. Other was the not so random RNG, I tested the program on a windows 10 computer and for reason or another that failed to work. I think that has something to do with the usage of time_ns. I will fix that for the next versions, but If you are reading this, that has not happened yet. If you experience any problems and you want to see the program in action, please contact me and I will upload a fix at earliest possibility. For easy fix you can also replace the contents of the Random_number function with "return randrange(lower_bound, upper_bound)" and replace the import for time_ns with "from random import randrange".


## Poetry commands:

before first run, to se up dependencies
```bash
poetry install
```
Launch application
```bash
poetry run invoke start
```
Run tests
```bash
poetry run invoke tests
```
Coverage report
```bash
poetry run coverage-report
```
Pylint
```bash
poetry run invoke lint
```
Pylint automatic format
```bash
poetry run invoke format
```


## Documentation:

[Project specification](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/project_specification.md)

[Implementation report WIP](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/implementation_report.md)

[Testing report WIP](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/testing_report.md)


## Weekly reports

[week 1](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_1.md)

[week 2](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_2.md)

[week 3](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_3.md)

[week 4](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_4.md)

[week 5](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_5.md)

