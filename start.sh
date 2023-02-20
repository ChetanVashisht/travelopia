echo "Installing front end dependencies"
cd front-end
npm install
npm run build

echo "Installing back end dependencies"
cd ../backend
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt

mv ../front-end/dist .
mv dist static

set -m
echo "Starting Backend"
python setup.py&

sleep 3

echo "Testing Backend"
python testTravel.py

fg

deactivate
rm -rf static
