echo -n "Deploying PersonalSite"
cd PersonalSite
mv settings.py settings_dev.py
mv settings_prod.py settings.py

cd ..
git add .
git commit -m "Working on deploy script"

git push

cd PersonalSite
mv settings.py settings_prod.py
mv settings_dev.py settings.py
