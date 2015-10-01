git checkout builds
git merge -s ours master
./build.sh
git add .
git add -u
git commit -m 'build'
git push origin builds
git checkout master