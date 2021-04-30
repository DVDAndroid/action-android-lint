#!/bin/sh

export REVIEWDOG_GITHUB_API_TOKEN="${INPUT_GITHUB_TOKEN}"

python3 /usr/local/bin/converter.py $GITHUB_WORKSPACE/${INPUT_LINT_XML_FILE} ${SEVERITIES_TO_IGNORE}
cat output_checkstyle.xml | reviewdog -f=checkstyle -name="Android Lint" -reporter="${INPUT_REPORTER}" -level="${INPUT_LEVEL}" ${INPUT_REVIEWDOG_FLAGS}
