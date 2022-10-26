# Copy reader code to destination
# sudo mkdir -p /var/lib/inclinometer-reader
# sudo cp -rf . /var/lib/inclinometer-reader

# Setup store location of the readings
# mkdir ~/.geobit/
# touch ~/.geobit/readings.txt

# Enable Cronjob to read every 5 minutes
# */5 * * * * bash /home/admin/workspace/geobit-inclinometer-reader/scripts/run.sh >/dev/null 2>&1

echo "### Installed by geobit-inclinometers ###" | tee -a ~/.bashrc > /dev/null
echo "alias readings=\"tail ~/.geobit/readings.txt\"" | tee -a ~/.bashrc > /dev/null
echo "alias make_measurement=\"bash ~/workspace/geobit-inclinometer-reader/scripts/read.sh\"" | tee -a ~/.bashrc > /dev/null
source ~/.bashrc