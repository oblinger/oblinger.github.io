# oblinger.github.io — personal website

website_repo := "/Users/oblinger/ob/proj/oblinger.github.io"

# Preview locally at http://localhost:4000/
preview:
    cd {{website_repo}} && bundle exec jekyll serve --livereload

# Push all changes to GitHub (triggers GitHub Pages auto-build)
publish:
    cd {{website_repo}} && git add -A && git commit -m "Update site" && git push
    @echo "Deployed to https://oblinger.github.io/"

# Rebuild Deliberative Coherence Quarto papers and publish
publish-dcl:
    cd {{website_repo}}/gitproj/DeliberativeCoherence && quarto render DeliberativeCoherence_Paper.qmd
    cd {{website_repo}}/gitproj/DeliberativeCoherence && quarto render Experiments_Paper.qmd
    cd {{website_repo}} && git add -A && git commit -m "Update Deliberative Coherence" && git push
    @echo "Deployed to https://oblinger.github.io/gitproj/DeliberativeCoherence/"
