#!/bin/bash -e

usage="$0 container_name_pattern apply|revert"

if [[ $# -ne 2 ]]; then
  echo "ERROR: Invalid usage"
  echo $usage
  exit 1
fi

container_pattern=$1
containers=$(docker ps --format "{{ .Image }}" --filter "name=$container_pattern")
if [[ -z $containers ]]; then
  echo "ERROR: Failed to find container matching /$container_name_pattern/"
  echo $usage
  exit 1
fi
shift

patch_action=$1
if [[ $patch_action != 'apply' ]] && [[ $patch_action != 'revert' ]]; then
  echo "ERROR: Invalid patch action - $patch_action - specified - should be - apply|revert"
  echo $usage
  exit 1
fi

for container in $(echo -e "$containers" | sort -n); do
  if [[ $patch_action == 'apply' ]]; then
    set -x
    docker exec -it $container /bin/bash /patches/apply_patch.sh
    set +x
  elif [[ $patch_action == 'revert' ]]; then
    set -x
    docker exec -it $container /bin/bash /patches/revert_patch.sh
    set +x
  fi
done
