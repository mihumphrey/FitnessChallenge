#!/bin/bash

SSH_ARGS="-i /home/michael/.ssh/recipes.pem -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"

echo "Remove the root stopper thingy from authorized_keys"

for TARGET_SERVER in "$@"
do
  echo "Hello thar ${TARGET_SERVER}"
  FILE_SIZE=$(ssh ${SSH_ARGS} ubuntu@${TARGET_SERVER} "sudo sh -c 'wc -c < /root/.ssh/authorized_keys'")
  echo "FILE SIZE IS: ${FILE_SIZE}"
  if [ "$FILE_SIZE" != "396" ]
  then
    echo "FILE SIZE IS NOT 396 for ${TARGET_SERVER}"
    ### IF FILE SIZE IS OFF, DO PREP
    scp ${SSH_ARGS} ./etc/_ssh/authorized_keys ubuntu@${TARGET_SERVER}:/home/ubuntu/root_authorized_keys
    ssh ${SSH_ARGS} ubuntu@${TARGET_SERVER} "sudo mv /home/ubuntu/root_authorized_keys /root/.ssh/authorized_keys"
    ssh ${SSH_ARGS} ubuntu@${TARGET_SERVER} "sudo chmod 600 /root/.ssh/authorized_keys"
    ssh ${SSH_ARGS} ubuntu@${TARGET_SERVER} "sudo chown root:root /root/.ssh/authorized_keys"
  fi
done