# Course Blocks

## Estimating Values
Initially, I only had two course overlap values. I used statistics to generate predictions for the size of three course overlaps.  
I tested the statistics in [explore_stats_tri.py](old_estimates/explore_stats_tri.py) and implemented the approach in [tricourse.py](old_estimates/tricourse.py).  
The [data](old_estimates/Most%20Common%20Courses%20Analysis.xlsx) for this approach has all been cleared to 0 for data security.

## Real Values
Then I got anonymized data for which courses students are in. In [real_blocks.py](real_blocks.py) I implemented an approach that finds the largest blocks of any parameterized size.

The [data](data) for this approach has been mostly removed for data security. Only a few entries have been preserved to show the expected format.
