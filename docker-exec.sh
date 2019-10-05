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
  echo -n "$container: "
  docker exec -it $container sh -c 'echo installed_modules $(cat /tmp/requirements.txt | tr "\n" " ")'
  docker exec -it $container $* 
  echo "============="
done
