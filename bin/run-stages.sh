#!/bin/bash
set -e

. ./bin/utils.sh

USAGE=$(cat <<USAGE

USAGE:
$0

MANDATORY ENVIRONMENT VARIABLES:

STAGE      - Program stage to run - [0|1|2|3|4]
PROTO      - Protocol             - [http|https]

OPTIONAL ENVIRONMENT VARIABLES:

URL                 - URL to call                     - Default: Derived by STAGE and PROTO
COUNT               - Number of times to call         - Default: 5
PYVERSIONS          - Comma separated Python versions - Default: 27,37
LOG_LEVEL           - Logging level                   - Default: DEBUG
PROFILE             - Profile the code                - Default: 0
PROFILE_STATS_COUNT - num of profile stats to show    - Default: 20
TRACE               - Trace the code                  - Default: 0
SOCKET_CLASS        - Dump the socket class           - Default: 0

USAGE
)

VALID_STAGES="(0|1|2|3|4)"
VALID_PYVERSIONS="(27|37)"
VALID_PROTO="(http|https)"

if [[ -z $STAGE ]] || [[ -z $PROTO ]]; then
    log_error "Mandatory env vars not set"
    echo -e "$USAGE"
    exit 1
fi

if ! echo "$STAGE" | grep -E -q "$VALID_STAGES"; then
    log_error "Invalid STAGE - should be one of - $VALID_STAGES"
    echo -e "$USAGE"
    exit 1
fi

if [[ -n "$PYVERSIONS" ]]; then
    for PYVERSION in $(echo $PYVERSIONS | tr ',' '\n'); do
        if ! echo "$PYVERSION" | grep -E -q "$VALID_PYVERSIONS"; then
            log_error "Invalid PYVERSIONS - should be one or more of - $VALID_PYVERSIONS"
            echo -e "$USAGE"
            exit 1
        fi
    done
fi

if ! echo "$PROTO" | grep -E -q "$VALID_PROTO"; then
    log_error "Invalid PROTO - should be one of - $VALID_PROTO"
    echo -e "$USAGE"
    exit 1
fi

COUNT=${COUNT:-5}
PYVERSIONS=${PYVERSIONS:-27,37}
LOG_LEVEL=${LOG_LEVEL:-DEBUG}
PROFILE=${PROFILE:-0}
PROFILE_STATS_COUNT=${PROFILE_STATS_COUNT:-20}
TRACE=${TRACE:-0}

if [[ -z $URL ]]; then
    if [[ $STAGE == '0' ]]; then
        if [[ $PROTO == 'http' ]]; then
            URL="http://localhost:8081/delay/1"
        elif [[ $PROTO == 'https' ]]; then
            URL="https://localhost:8082/delay/1"
        fi
    else
        if [[ $PROTO == 'http' ]]; then
            URL="http://http_server:8080/delay/1"
        elif [[ $PROTO == 'https' ]]; then
            URL="https://https_server:8081/delay/1"
        fi
    fi
fi

EXTRA_OPTS="--log-level $LOG_LEVEL "
if [[ $PROFILE == '1' ]]; then
    EXTRA_OPTS="$EXTRA_OPTS --profile-code --profile-stats-count $PROFILE_STATS_COUNT"
fi
if [[ $TRACE == '1' ]]; then
    EXTRA_OPTS="$EXTRA_OPTS --trace"
fi
if [[ $SOCKET_CLASS == '1' ]]; then
    EXTRA_OPTS="$EXTRA_OPTS --socket-class"
fi

for PYVERSION in $(echo $PYVERSIONS | tr ',' '\n'); do
    if [[ $STAGE != '0' ]]; then
        program='/app/test_grequests_v1.py'
        if [[ $STAGE -gt 2 ]]; then
            program='/app/test_grequests_v2.py'
        fi

        ./docker-exec.sh "test_grequests_python${PYVERSION}_${STAGE}" \
        /usr/local/bin/python "${program}" \
        --url $URL --url-count $COUNT \
        $EXTRA_OPTS
    else
        interpreter='python2'
        if [[ $PYVERSION == '37' ]]; then
            interpreter='python3'
        fi
        program='./bin/test_grequests_v1.py'
        echo "============="
        $interpreter $program --url $URL --url-count $COUNT \
        $EXTRA_OPTS
        echo "============="
    fi
done
