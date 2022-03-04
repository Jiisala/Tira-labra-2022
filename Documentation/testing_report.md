# Testing report

For testing of the program three main approaches were taken. Automated Unittesting to make sure that everything works technically as intended, performance testing to get general grasp of the performance of the different parts of program and vigorous manual testing to assess the aesthetic outcome of different parameters. Because quite a bit of randomness is involved in the process, multiple passes of the same settings are needed, to get a picture of what kind of dungeons they generate. Since the main focus of the program is to generate usable dungeons, aesthetics were chosen over performance when the situation called to choose one or another.

## Testing methods

Unittests are written for all of the classes, except UI. The tests for logic class concentrate mainly on testing that calling of the other classes work as intended. The functionality of the algorithms has been already tested in the tests written for the respective classes. For other classes the tests aim to test that the classes perform as wanted with given parameters and that no unwanted side effects rise from them. Testing should cover most of the branches in the code. Final version of coverage report will get attached here at the end of the course. I of course aim to get the numbers to 100%. 

Performance tests are run on each algorithm separately and for the whole program. They are all written in performance.py. They consist of running the algorithms with different parameters, stripped of randomness as far as feasible, and measuring the running time. They are easily repeatable at will just by running performance.py. 

The manual testing is performed by running the program multiple times, changing the parameters after sufficient amount of runs and writing the results to a file. The file will then be inspected by a human inspector and observations of the results will be made. The file will get uploaded to the repository for others to inspect.

## More on performance testing

Performance tests are done by running each algorithm one thousand times and measuring the spent time. While not too great number of iterations for performance testing one thousand times, is enough to note how different parts of the program perform in relation to each other. The measured times given bellow, are gathered from test running on a "freshman laptop 2021 edition", running cubbli linux. It has the following specs:

- Lenovo ThinkPad T14 gen 2
- 4-core processor, 8-thread Intel Core i5-1135g7, 2.4-4.2 GHz
- 16 GB main memory
- internal flash disc (NVMe-SSD) 512 GB

The relevant preferences used when running the tests are:

- file_name = "performance.log"
- output_to_console = 0
- output_to_file = 0
- map_height = 100
- map_width = 100
- floor_propability = 0
- iterations =1
- stop_chance = 0
- turn_chance = 0
- stop_partitioning_height = 99
- stop_partitioning_width = 99

These are devised so that they would strip the program from randomness, as much as it is possible to do via preferences. Some randomness remained, but It should not affect the running times too much. BSP was tested twice, first with a shallow tree of two leaves, and then with a tree of four leaves.
One test that was not strictly a performance test, but was tested at the same time was a test to see that the RNG I wrote gave roughly similar distribution than the pythons build in randrange function. That was achieved by running both of them one million times and noting how often each number appeared. Then the subtraction of the number with least appearances and the number with most appearances was calculated from both. From that it can be concluded that the RNG is sufficiently random. The floodfill algorithm has a recursive function to traverse the BSP tree and look for leaves, but it is essentially the same as the BSP traversal function, so it is not tested separately. The corridors test involves initiating the matrix used for testing before each iteration. Time spent on that is fraction of the whole test time, so I did not feel like subtracting that from the time it took running the test necessary

The performance of the program was much worse than the individual algorithms combined. This is seems to be mainly overhead from stiching the small maps together. That part of the program could probably be optmized quite a lot, but for now I will let it be as it is.

The results of the tests run before writing this were as follows: 

- BSP shallow tree

   0.004816770553588867 seconds 
- BSP deeper tree
 
   0.010364055633544922 seconds 
- BSP traversal
 
   3.24249267578125e-05 seconds 
- Cellular automata
 
   5.1975250244140625e-05 seconds 
- Floodfill 

   0.42391252517700195 seconds 
- Corridors 

   0.3053302764892578 seconds 
- RNG peformance 

   0.0005633831024169922 seconds 
- RNG distribution mine (diference of most common and least common number) 

   1677 
- RNG distribution python (diference of most common and least common number) 

   1830 
- The whole program ran 1000 iterations 

   43.75894284248352 seconds 

By Investigating the result we can see that the BSP algorithm, cellular automata and RNG perform at much faster pace than Floodfill or corridors. For floodfill that is expected, because it potentially needs to visit each cell of the map multiple times. There are versions of the algorithm that are optimized better than the one used here. The different algorithms used are of course not directly comparable with each other, in terms of performance, but the test shows clearly which of them would need to be optimized most urgently if better performance was sought. 

# Manual testing

Through out the developement vigorous maual testing has taken place. As the aim of the program is to generate usable and above all aesthetically pleasing dungeons, testing the different settings and seeing that everything works as intended has been valuable tool. Most of the testing has not been recorded, but the testing done for will be written to a log file that can be inspected later. Bellow I will attach some images of generated dungeons and explanations on how different combinations of settings affect the results.

