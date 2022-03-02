# Jaakko's Dungeon generator

Project is set up using poetry, but simply for running the program no exotic dependencies are needed, just run launch.py. All dependencies are testing or code formatting related. The program however expects you to run it from the root directory. This is because of the write to file functionality, the current verson has it set to true by default, I will change that for next version.

While using the program use commands Q to quit, C to create new map, S to open settings view and B to get back to main view, all are case insensitive.

if the output to console is messy and unreadable, first ensure that the console window is wide enough to fit full lines of the map, so that no unwanted linebreaks happen.

You should be able to alter the general look of the dungeon a great deal by playing with the settings, so I recommend doing some manual testing. Testing document with pre-generated dungeons to illustrate this is on the way. The settings should be constrained so that it is not possible to crash the program, but I have not yet done enough testing to ensure it. The path to the filewriter is not really monitored at the time of changing the settings, but there probably is no need to change it. If invalid path is given, the program won't crash, but will not create maps either (if "write map to file" is set true).

The program is called dungeon generator, but really the resulting patterns can be used for variety of different purposes. I have designed this mainly level maps in mind, but that should not discourage other possibilities.

Detailed explanation of the algorithms can be found in the Implementation report. Link to it is bit further bellow. It is still work in progress, but it should be complete enough to understand what is happening inside the program. 


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
Run performance tests
```bash
poetry run invoke performance
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
[manual](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Manual.md)

[Project specification](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/project_specification.md)

[Implementation report WIP](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/implementation_report.md)

[Testing report WIP](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/testing_report.md)


## Weekly reports

[week 1](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_1.md)

[week 2](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_2.md)

[week 3](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_3.md)

[week 4](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_4.md)

[week 5](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_5.md)

[week 6](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_6.md)
