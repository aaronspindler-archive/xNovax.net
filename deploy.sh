echo "Deploying PersonalSite"
cd PersonalSite

echo "Renaming Files"
mv settings.py settings_dev.py
mv settings_prod.py settings.py

cd ..
git add .
echo -n "Enter commit message"
read commitmsg
git commit -m "$commitmsg"

git push

cd PersonalSite
echo "Changing filenames back"
mv settings.py settings_prod.py
mv settings_dev.py settings.py
