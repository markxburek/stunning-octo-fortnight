find . -iname "UAV_data*" -o \
       -iname "layer1_comparison.json" -o \
       -iname "layer2a_mobility_library.json"

find . -maxdepth 2 -type d | sort

ls -lh requirements.txt
