
# use modified sphinx templates templates
cp --recursive --verbose mod/_templates/* ./_templates/

# run runestone build
# this overwrites the docs folder
runestone build

# copy back from mod folder to
# use modified js and css
cp --recursive --verbose mod/docs/* ./docs/
