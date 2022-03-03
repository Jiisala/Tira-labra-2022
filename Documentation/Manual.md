
# Jaakko's Dungeon Generator manual

Welcome dear reader. This manual will go through the basics of running the program and the different settings you can fiddle with. The python version used in development is 3.8.10, but it should run just fine on any relatively modern version of it. To launch the generator, navigate to the root folder of the program and give the command `python3 src/launch.py`. The program is set up using poetry, so if running the program fails or you want to do some testing, you can let poetry handle figuring out the dependencies and such. Check that you have poetry installed on your system, and if not install it, instructions can be found [here](https://python-poetry.org/docs/). After that you can use the following commands:

**All commands expect you to be in the root directory of the program when executing them** 

before first run, to set up dependencies
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
## Now that the program is running

When you start the program you are presented with title screen and two three options [C]reate, [S]ettings or [Q]uit. Enter the corresponding command to venture forward. All of the commands are case insensitive. 

- Q for quit, should be pretty self explanatory, it exits the program. 
- C for create creates map with the current settings, and, if enabled in settings, outputs it to console (default: on) and to a file (default: off) 
- S for settings takes you to the settings view.

If you see the line ` \033c\033[3J", end='') ` printed on top of the map, don't get worried. That is a convenience command meant to clear the screen. It does not seem work on all systems, but I chose to let it be as it makes the program nicer to use on the systems it works in.

In the setting view you can see the current settings and alter them. Here we have the already familiar [C]reate and [Q]uit commands. What is new is the [B]ack command that takes you back to the title screen and the commands for different settings. Entering numbers from 1 to 17 let you assign new value to the corresponding setting. If the value is not within acceptable limits, it won't change and a error message is displayed.

## Settings explained:
The limits explained here are enforced by the program unless stated otherwise. Giving values larger than maximum integer value for map dimensions will crash the program. If you wish to create maps of that size, this program will probably not be the best choise for you anyway.

**GENERAL:** 

1. Map width = Width of the mag generated. 
2. Map height = = Height of the mag generated. 

One of these needs to be bigger than the corresponding partitioning limit (6. and 7.), as the program expects to make at least one cut to the area. 
Both naturally need to be positive integers.  

**BINARY SPACE PARTITIONING:**

3. Minimum subarea width = Minimum width of the subarea. The program will never go bellow this when partitioning
4. Minimum subarea_height = Minimum height of the subarea. The program will never go bellow this when partitioning
5. Stop chance = Chance for the partitioning to stop before reaching the minimum limits. Set to high if you want generally bigger areas with a small area every now and then and small if vice versa. Setting to zero with suitable values for other BSP settings will give you precise control of the map created. Max is 99 because the program always needs to make at least one cut to the area.
6. Width to cease partitioning = If the current subarea width is smaller than this the program won't make any further vertical cuts to it. 
7. Height to cease partitioning = If the current subarea height is smaller than this the program won't make any further horizontal cuts to it.

Here 3. and can not be more than half of the 6. and same goes for 4. and 7. otherwise there is a high chance of program crashing.

**CELLULAR AUTOMATA:**

8. Initial floor propability = The probability to create floortiles when initiating the algorithm.  
9. Min neighbouring walls to set wall to floor = When running the algorithm the minimum number of neighbouring walls to turn a walltile to a floortile.
10. Min neighbouring walls to set floor to wall = When running the algorithm the minimum number of neighbouring walls to turn a floortile to a walltile.
11. Iterations = How many sweeps of the area the algorithm makes. Generally speaking the lower the value the grittier the outcome. setting too high will run havoc on performance.

The effects of these settings are highly depended on each other so it is hard to give specific instructions on them. Examples of the effects can be found in the [testing report](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/testing_report.md) (not really yet)

**CORRIDORS:**

12. Chance to make a turn on each step = affects the shape of the corridor, but the effect is not very spectacular. The setting is here mainly to give better control during testing phase.
13. Draw corridors = If this is set to 0 the program will not connect the rooms with corridors, any other value will get interpreted as `True`.
            
**OUTPUT:**

 14. Output to console = If set to 0 the program wont print out the created map to console, any other value will get interpreted as `True`.
 15. Output to file = If set to 0 the program wont output the created map to a file, any other value will get interpreted as `True`. The current settings will get exported to the file with the map.
 16. Path to file = Path to the output file, needs to be given as a relative path to the /src folder. The program won't enforce correct path to be given, but invalid path will cause the map creation to fail.
 17. Filename: Name of the file created, defaults to current date and the extension .txt
 
## Miscellaneous notes

To if you want to run the performance tests the easiest way is to use the command `python3 src/performance.py`, `poetry run invoke performance` works also. The performance test will run its course and output the results to a file called performance.log in the /data folder as well as print them to the console.

The coverage report can be created with the poetry command `poetry run invoke coverage-report` The report will get printed to the console and output to the folder /htmlcov for further inspection

Pylint check can be run with `poetry run invoke lint` It will output the results to console. 

That should really be all the information you need to run the program successfully. More in depth look on the inner works of the program can be found in the [implementation report](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/implementation_report.md) and the [testing report](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/testing_report.md).

