#!/bin/bash

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-files /home/sshuser/mapper.py,/home/sshuser/reducer.py \
-input $HDFS/map_reduce_input \
-output $HDFS/map_reduce_output \
-mapper mapper.py \
-reducer reducer.py
