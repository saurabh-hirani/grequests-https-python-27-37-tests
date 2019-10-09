#!/bin/bash -e

container_pattern=$1
containers=$(docker ps --format "{{ .Image }}" --filter "name=$container_pattern")
if [[ -z $containers ]]; then
  echo "ERROR: Failed to find container matching /$container_name_pattern/"
  exit 1
fi

shift

for container in $(echo -e "$containers" | sort -n); do
  echo "============="
  for module in $(docker exec -it $container cat /tmp/requirements.txt); do
      echo -e "$container: installed_module: $module"
  done
  echo "============="
  # set -x
  docker exec -it $container $* 
  # set +x
  echo "============="
done
