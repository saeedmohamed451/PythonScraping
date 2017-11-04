#!/usr/bin/bash

ROWS="2 6 3"

ROWS_LIST=(${ROWS})

for CURRENT_ROW in ${ROWS_LIST[@]}
do
  CMD="sleep "${CURRENT_ROW}
  echo ${CMD}
  ${CMD} &
done

# Wait for the parallel child processes to finish.
wait

# All done!
echo "Done"
