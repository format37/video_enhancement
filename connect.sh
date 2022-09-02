###
# this shell script connects to container
###

# get id of running container with image name "video_enhancement_upscaler_1"
sudo container_id=$(docker ps | grep video_enhancement_upscaler_1 | awk '{print $1}')
echo "container id: $container_id"
# connect to container
sudo docker exec -it $container_id /bin/bash
