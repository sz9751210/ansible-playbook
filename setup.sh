#!/bin/bash

set -e

export PROJECT_ID=""
export REGION=""

envsubst < group_vars/all/env.yml.example > group_vars/all/env.yml
