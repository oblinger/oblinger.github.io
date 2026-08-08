# oblinger.github.io — personal website

website_repo := "/Users/oblinger/ob/grove/oblinger.github.io"
vault_asio   := "/Users/oblinger/ob/kmr/ASIO"

# Preview locally at http://localhost:4000/
preview:
    cd {{website_repo}} && bundle exec jekyll serve --livereload

# Copy the ASIO essays from the vault, which is their source of truth.
# The vault holds the .md; this repo holds a published copy, because GitHub
# Pages builds from what is committed here. Never edit ASIO/ in this repo —
# edit ~/ob/kmr/ASIO/ and re-run this. --delete keeps a vault rename from
# leaving an orphan page live on the site. .anchor is vault machinery and
# must not be published.
sync-asio:
    rsync -a --delete --exclude='.anchor' --exclude='.DS_Store' \
        {{vault_asio}}/ {{website_repo}}/ASIO/
    @echo "ASIO synced from {{vault_asio}}"

# Push all changes to GitHub (triggers GitHub Pages auto-build)
publish: sync-asio
    cd {{website_repo}} && git add -A && git commit -m "Update site" && git push
    @echo "Deployed to https://oblinger.github.io/"

# Rebuild Deliberative Coherence Quarto papers and publish
publish-dcl:
    cd {{website_repo}}/gitproj/DeliberativeCoherence && quarto render DeliberativeCoherence_Paper.qmd
    cd {{website_repo}}/gitproj/DeliberativeCoherence && quarto render Experiments_Paper.qmd
    cd {{website_repo}} && git add -A && git commit -m "Update Deliberative Coherence" && git push
    @echo "Deployed to https://oblinger.github.io/gitproj/DeliberativeCoherence/"
