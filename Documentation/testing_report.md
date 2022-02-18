# Testing report

For testing of the program three main approaches were taken. Automated Unittesting to make sure that everything works technically as intended, performance testing to get general grasp of the performance of the different parts of program and vigorous manual testing to assess the aesthetic outcome of different parameters. Because quite a bit of randomness is involved in the process, multiple passes of the same settings are needed, to get a picture of what kind of dungeons they generate. Since the main focus of the program is to generate usable dungeons, aesthetics were chosen over performance when the situation called to choose one or another.

## Testing methods

Unittests were written for all of the classes, except UI. The tests for logic class concentrate mainly on testing that calling of the other classes work as intended, because the functionality of the algorithms is already tested in the tests written for the respective classes. For other classes the tests aim to test that the classes perform as wanted with given parameters and that no unwanted side effects rise from them. Testing should cover most of the branches in the code. Final version of coverage report will get attached here at the end of the course. I of course aim to get the numbers to 100%. 

Performance tests are run on each algorithm separately and for the whole program. They can be launched with their own launcher (not yet materialized, but will get made soon) They consist of running the algorithms with different parameters, stripped of randomness, and measuring the running time. They will be easily repeatable at will.

The manual testing is performed by running the program multiple times, changing the parameters after sufficient amount of runs and writing the results to a file. The file will then be inspected by a human inspector and observations of the results will be made. The file will get uploaded to the repository for others to inspect.

## Note on the RNG used

The RNG used is really far from true randomness, it uses linear time and does not do any further operations to the seed number. Quick testing will show that for example generating 100 numbers between 1000 and 10000 in rapid succession, result in a noticeable pattern because the first digit does not change as fast enough. I believe that it is needless to say that it is not really sufficient way of generating randomness. However in this particular use, the numbers generated are mostly smaller than hundred and there is always a big enough interval between the calls. I chose to use this method because of ease of implementation and because I knew that it would satisfy my needs. If this project should continue after this course, the RNG will be replaced with something more random.

I omitted the test for random distribution of numbers, as it is clear that the method would not pass any serious testing for randomness. Performance tests and unit tests for the class of course are performed. 
