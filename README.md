# Jaakko's Dungeon generator

Project is set up using poetry, but simply for running the program no exotic dependencies are needed, just run launch.py. All dependencies are testing or code formatting related. 

While using the program use commands Q to quit, C to create new map, S to open settings view and B to get back to main view, all are case insensitive.

if the output to console is messy and unreadable, first ensure that the console window is wide enough to fit full lines of the map, so that no unwanted linebreaks happen.

When manually testing the program, please note that at this point it is possible to crash the program or to cause a endless loop if conflicting parameters are given. 

The program is called dungeon generator, but really the resulting patterns can be used for variety of different purposes. I have designed this mainly level maps in mind, but that should not discourage other possibilities.

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

