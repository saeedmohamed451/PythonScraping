#!/usr/bin/bash


# Lower range of random number.
LOWER=10
# Upper range of random number.
UPPER=30

# Generate a random number between LOWER and UPPER
RANDOM_TIME=$(( (RANDOM % (${UPPER}-${LOWER})) + ${LOWER} + 1 ))

# Report the random time.
echo ${RANDOM_TIME}
sleep ${RANDOM_TIME}
