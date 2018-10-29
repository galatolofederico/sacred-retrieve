# sacred-retrieve

Python script for easily retrieving and processing results from a [sacred](https://github.com/IDSIA/sacred) mongodb collection 

## Installation

```
pip install --upgrade git+https://github.com/galatolofederico/sacred-retrieve --user
```

## Usage

```
sacred-retrieve [arguments] experiments names
```

#### Results processing arguments

Argument | Description  | Example 
---|---|---
 --parameters | List of parameters to which group the results by | --parameters learning_rate hidden_dim  
 --accumulate | List of info-dict fields to accumulate | --accumulate mean_reward 
 --reduce | List of Reducer to compute for each result bucket | --reduce mean 

The experiments results are accumulated by default  

#### Configuration arguments

Argument | Description  | Example 
---|---|---
--output | Output format (table or csv) | --output csv
--db | Name of the MongoDB Database | --db sacred
--mongodb-uri | Uri for the MongoDB Connection | --mongodb-uri mongodb://db.host.tld:2500/

#### Reducers specific arguments

Argument | Reducer | Description  | Example 
---|---|---|---
--mean-ci | mean | Confidence for the confidences intervals | --mean-ci 0.99
--delimiter | list | Delimiter for the list of values | --delimiter :

### List of Reducers

The specified reducers will be applied to all the accumulated values 

Reducer | Description
---|---
min | Compute the minimum value
max | Compute the maximum value
mean | Compute the Mean and Confidences Intervals of values
count | Compute the number of values
list | List all the values
## Example


```
$ sacred-retrieve experiment_a experiment_b --parameters hidden_dim --reduce min max mean --accumulate mean_reward
+------------+---------------+---------------+-----------------------------+-------------------+-------------------+---------------------------+                                              
| hidden_dim | results (Min) | results (Max) |      results (Mean CI)      | mean_reward (Min) | mean_reward (Max) |   mean_reward (Mean CI)   |                                              
+------------+---------------+---------------+-----------------------------+-------------------+-------------------+---------------------------+                                              
|     5      |      260      |      4160     | 1131.800000 +/- 2105.571911 |      305.865      |      497.048      |  442.499200 +/- 97.818038 |                                              
|     2      |      175      |      1212     |  499.400000 +/- 545.345415  |      193.983      |      348.658      |  255.475000 +/- 75.190303 |                                              
|     3      |      111      |      1319     |  578.600000 +/- 575.896961  |      255.632      |       499.08      | 357.105000 +/- 120.861125 |                                              
+------------+---------------+---------------+-----------------------------+-------------------+-------------------+---------------------------+  
```