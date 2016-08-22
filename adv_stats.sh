DIR="$HOME/apps/tamarin-run-sapienz"
ls "$DIR" | grep apk_output | while read app; do
  ls "$DIR/$app/intermediate" | while read execution; do
    wc -l < "$DIR/$app/intermediate/$execution"
  done > "data_${app%.apk_output}.txt"
  python3 -c '#
from statistics import mean, median, mode, StatisticsError
from sys import argv

for filename in argv[1:]:
  print(filename + ":")
  with open(filename, "r") as f:
    step_counts = [ int(line.strip()) - 4 for line in f.readlines() ]

  print("  Number of executions:", len(step_counts))
  print("  Average length:", mean(step_counts))
  print("  Median length:", median(step_counts))
  try:
    print("  Most common length:", mode(step_counts))
  except StatisticsError:
    print("  No single most common length.")
  print("  Max length:", max(step_counts))
  print("  Min length:", min(step_counts))' \
"data_${app%.apk_output}.txt"
done
