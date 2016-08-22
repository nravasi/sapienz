#!/bin/bash

acpi -t

DIR="$HOME/apps/tamarin-run-sapienz"
APPS=$(ls "$DIR" | grep -e 'apk_output$' | wc -l)

if [ $APPS -eq 0 ]; then
  echo "sapienz is spinning up..."
  exit
fi

echo "$APPS apps started"

for app in $(ls "$DIR" | grep -e 'apk_output$'); do
  RUNS=$(ls "$DIR/$app/intermediate" | wc -l)
  CRASHES=$(ls "$DIR/$app/crashes" | wc -l)
  echo "${app%.apk_output}:
    run $RUNS times
    found $CRASHES crashes"
done
