#!/usr/bin/bash

#######################################################################
# Determine what day it is today.                                     #
# Create an output directory and link to it.                          #
# Kick-off the scrape for the retailers that drop new catalogs today. #
# Push results to Azure.                                              #
#######################################################################

# Must set the environment so cron can send HTTPS requests.
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-bundle.crt

# Index to the current day of the week.
DAYS_OF_WEEK=("Sunday" "Monday" "Tuesday" "Wednesday" "Thursday" "Friday" "Saturday")
DAY_OF_WEEK=`date +%w`

# User input may also provide the day of the week.
if [ "$#" = 1 ]
then
  DAY_OF_WEEK=$1
fi

if [ ${DAY_OF_WEEK} -gt 6 ]
then
  echo "Error: Found ("${DAY_OF_WEEK}") Expected range of 0-6 (Sunday to Saturday)"
  exit 1
fi

#
# Schedule for retailers.
# 0 - Sunday
# 1 - Monday
#
RETAILERS=(
    # Sun
    # - Family Dollar: 6
    "6 "
    # Monday (Requires VPN connection)
    # - Dollar General: 5
    # - Family Dollar: 6
    # - Rite Aid: 16
    # - Frescoymas: 30
    "5 6 16 30"
    # Tuesday
    # - Albertsons: 20 21 22 23 24 25
    # - Family Dollar: 6
    # - Food Lion: 7 8 
    # - Kroger: 10 11
    # - Safeway: 26
    "6 7 8 10 11 20 21 22 23 24 25 26"
    # Wed
    # - Aldi: 2 3 4
    # - Family Dollar: 6
    # - Walgreens: 14
    "2 3 4 6 14"
    # Thu (Requires VPN connection)
    # - Family Dollar: 6
    # - Acme Markets: 18 19
    # - CVS: 15
    # - Giant Food: 9
    # - Stop & Shop: 13
    "6 9 13 15 18 19"
    # Fri
    # - Family Dollar: 6
    # - Meijer: 12
    # - Shoprite: 27
    # - Publix: 34
    "6 12 27 34"
    # Sat
    # - Family Dollar: 6
    # - Walmart: 17
    "6 17"
)

# Build the output directory name.
YEAR=`date +%Y`
MONTH=`date +%b`
DAY=`date +%d`

OUTPUT_DIR="/home/hernandj/catalyticsscraping/code/dailyOutput/"${YEAR}"_"${MONTH}"_"${DAY}"/"

# Create output directory.
mkdir -p ${OUTPUT_DIR}

####################
# Kick-off scrape. #
####################
if [ -z "${RETAILERS[${DAY_OF_WEEK}]}" ]
then
  echo "Error: Nothing to do for "${DAYS_OF_WEEK[${DAY_OF_WEEK}]}"("${DAY_OF_WEEK}")."
  exit 1
fi

echo "Scrape for "${DAYS_OF_WEEK[${DAY_OF_WEEK}]}

GOOGLE_SHEET_ROWS=(${RETAILERS[${DAY_OF_WEEK}]})

# Lower range of random number.
LOWER=10
# Upper range of random number.
UPPER=30

# Kick-off multiple scrapes in parallel.
for CURRENT_ROW in ${GOOGLE_SHEET_ROWS[@]}
do
  # Create the command to run a scrape for a single retailer.
  CMD="python /home/hernandj/catalyticsscraping/code/driveCatalytics.py --output "${OUTPUT_DIR}" "${CURRENT_ROW}

  # Report the command and kick-off.
  echo ${CMD}
  ${CMD} &

  # Generate a random number between LOWER and UPPER
  RANDOM_TIME=$(( (RANDOM % (${UPPER}-${LOWER})) + ${LOWER} + 1 ))

  # Report the random time and sleep for a little while before
  # kick-off the next scrape as don't want them all to start
  # at the same time.
  echo "About to sleep for "${RANDOM_TIME}" seconds..."
  sleep ${RANDOM_TIME}
done

# Wait for parallel scrapes to complete.
wait

##########################
# Push results to Azure. #
##########################
#CMD="python /home/hernandj/catalyticsscraping/code/uploadBlobs.py "${OUTPUT_DIR}
#
#echo ${CMD}
#${CMD}
