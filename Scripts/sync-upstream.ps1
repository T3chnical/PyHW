git config --global user.name 'T3chnical'
git config --global user.email 'thisnewacc46@gmail.com'

git pull --unshallow

git remote add upstream https://github.com/wusimon51/PyHW.git
git fetch upstream

git merge --no-edit upstream/main
git push origin main