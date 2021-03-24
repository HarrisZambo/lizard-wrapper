if [ $# -ne 1 ]
then
    echo Please provide exactly 1 argument
    exit 1
fi

mkdir results
touch results/function_stats.json

# docker build -t ces_image .

docker pull zamboharris/ces

docker run \
--mount type=bind,source="$(pwd)"/results,target=/ces/results \
--mount type=bind,source="$1",target=/ces/src \
zamboharris/ces