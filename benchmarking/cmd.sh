#! /bin/bash

# ----- run process -----
$@ &
PID=$!

# ----- save benchmark -----
# BENCH_FILE_NAME=$(echo "bench_$@.txt" | sed 's/ /_/g' | sed 's/\//@/g')
BENCH_FILE_NAME="bench_result.txt"
START_TIME=$(date +%s.%9N)
echo "PAST_TIME $(ps v | head -n 1)" > $BENCH_FILE_NAME
while true
do
  # ----- format of "ps v" -----
  # PID TTY STAT TIME MAJFL TRS DRS RSS %MEM COMMAND
  bench=$(ps v $PID | awk -v pid=$PID '{if ($1 == pid) { print $0}}')

  if [ "$bench" != "" ] && [ "$bench" != "\n" ]; then
    current_time=$(date +%s.%9N)
    bench=$(ps v $PID | awk -v pid=$PID '{if ($1 == pid) { print $0}}')

    # ----- format of "result_bench.txt" -----
    # PAST_TIME PID TTY STAT TIME MAJFL TRS DRS RSS %MEM COMMAND
    past_time=$(echo $current_time $START_TIME | awk '{print $1 - $2 }')
    echo $past_time $bench >> $BENCH_FILE_NAME
  else
    break
  fi
done

current_time=$(date +%s.%9N)
past_time=$(echo $current_time $START_TIME | awk '{print $1 - $2 }')
echo "Done: Time $past_time"

# ----- save spec -----
# CPU_NUM=$(cat /proc/cpuinfo | grep 'cpu cores' | sort -u | awk -F ":" '{print $2}')
# CPU_FREQ=$(cat /proc/cpuinfo | grep 'cpu MHz' | sort -u | awk -F ":" '{print $2}')
# MEM_SIZE=$(cat /proc/meminfo | grep 'MemTotal' | awk -F ":" '{print $2}' | awk '{print $1}')
# echo "----------" | tee -a $BENCH_FILE_NAME
# echo "CPU_NUM $CPU_NUM" | tee -a $BENCH_FILE_NAME
# echo "CPU_FREQ $CPU_FREQ (MHz)" | tee -a $BENCH_FILE_NAME
# echo "MEM_SIZE $MEM_SIZE (Byte)" | tee -a $BENCH_FILE_NAME
