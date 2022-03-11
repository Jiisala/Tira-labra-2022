# Jaakko's Dungeon generator

![dungeon](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/img/dungeon.png)

Project is set up using poetry, but simply for running the program no exotic dependencies are needed, just run launch.py. All dependencies are testing or code formatting related. The program expects you to run it from the root directory, if ran from somewhere else some parts of the program will fail.

While using the program use commands Q to quit, C to create new map, S to open settings view and B to get back to main view, all are case insensitive.

if the output to console is messy and unreadable, first ensure that the console window is wide enough to fit full lines of the map, so that no unwanted linebreaks happen.

You should be able to alter the general look of the dungeon a great deal by playing with the settings, so I recommend doing some manual testing. Testing document with pre-generated dungeons to illustrate this can be found [here](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/testing_report.md). The settings are constrained so that it should be impossible to crash the program. The path to the filewriter is not really monitored at the time of changing the settings, but there probably is no need to change it. If invalid path is given, the program won't crash, but will not create maps either (if "write map to file" is set true).

The program is called dungeon generator, but really the resulting patterns can be used for variety of different purposes. I have designed this mainly level maps in mind, but that should not discourage other possibilities.

Detailed explanation of the algorithms can be found in the [implementation report](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/implementation_report.md).



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

[Implementation report](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/implementation_report.md)

[Testing report](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/testing_report.md)


## Weekly reports

[week 1](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_1.md)

[week 2](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_2.md)

[week 3](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_3.md)

[week 4](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_4.md)

[week 5](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_5.md)

[week 6](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Weekly_report_6.md)
