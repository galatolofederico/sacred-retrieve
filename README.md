# sacred-retrieve

Python script for easily retrieving and processing results from a [sacred](https://github.com/IDSIA/sacred) mongodb collection 

## Installation

## Usage

```
sacred-retrieve [parameters] experiment_name
```

For process your results you can use the following command line arguments

Argument | Description  | Example 
---|---|---
 --parameters | List of parameters which group the results by | --parameters learning_rate hidden_dim  
 --accumulate | List of info-dict fields to accumulate | --accumulate mean_reward 
 --reduce | List of Reducer to compute for each result bucket | --reduce mean 

The experiments results are accumulated by default  

## Example


```
$ sacred-retrieve experiment --parameters hidden_dim --reduce min max mean --accumulate mean_reward
+------------+---------------+---------------+-----------------------------+-------------------+-------------------+---------------------------+                                              
| hidden_dim | results (Min) | results (Max) |      results (Mean CI)      | mean_reward (Min) | mean_reward (Max) |   mean_reward (Mean CI)   |                                              
+------------+---------------+---------------+-----------------------------+-------------------+-------------------+---------------------------+                                              
|     5      |      260      |      4160     | 1131.800000 +/- 2105.571911 |      305.865      |      497.048      |  442.499200 +/- 97.818038 |                                              
|     2      |      175      |      1212     |  499.400000 +/- 545.345415  |      193.983      |      348.658      |  255.475000 +/- 75.190303 |                                              
|     3      |      111      |      1319     |  578.600000 +/- 575.896961  |      255.632      |       499.08      | 357.105000 +/- 120.861125 |                                              
+------------+---------------+---------------+-----------------------------+-------------------+-------------------+---------------------------+  
```