mv deploy build
git stash
git checkout builds
git stash pop
git add .
git add -u
git commit -m 'build'
git push origin builds
git checkout master