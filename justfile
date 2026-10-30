# oblinger.github.io — personal website

website_repo := justfile_directory()
# The ASIO essays' source in the vault; override with WEB_VAULT_ASIO
vault_asio   := env("WEB_VAULT_ASIO", home_directory() / "ob/kmr/ASIO")

# Preview locally at http://localhost:4000/
preview:
    cd {{website_repo}} && bundle exec jekyll serve --livereload

# Copy the ASIO essays from the vault, which is their source of truth.
# The vault holds the .md; this repo holds a published copy, because GitHub
# Pages builds from what is committed here. Never edit ASIO/ in this repo —
# edit the vault's ASIO/ (vault_asio above) and re-run this. The copy is
# staged and run through tools/strip-vault, which removes vault machinery
# (breadcrumbs, the BRIEF, HookAnchor stubs and hook:// links) and turns
# [[wikilinks]] into site links; it refuses, leaving ASIO/ untouched, when a
# page still names a local path. --delete keeps a vault rename from leaving
# an orphan page live on the site. .anchor is vault machinery.
sync-asio:
    #!/usr/bin/env bash
    set -euo pipefail
    stage=$(mktemp -d)
    trap 'rm -rf "$stage"' EXIT
    rsync -a --exclude='.anchor' --exclude='.DS_Store' "{{vault_asio}}/" "$stage/"
    python3 "{{justfile_directory()}}/tools/strip-vault" "$stage" /ASIO/
    rsync -a --delete --checksum "$stage/" "{{website_repo}}/ASIO/"
    echo "ASIO synced from {{vault_asio}}"

# Commit the synced ASIO essays and push (triggers the GitHub Pages build).
# Stages ASIO/ only: anything else in the working tree is not swept into the public repo.
publish: sync-asio
    cd {{website_repo}} && git add -- ASIO && git commit -m "Update ASIO" -- ASIO && git push
    @echo "Deployed to https://oblinger.github.io/"

# Rebuild Deliberative Coherence Quarto papers and publish
publish-dcl:
    cd {{website_repo}}/gitproj/DeliberativeCoherence && quarto render DeliberativeCoherence_Paper.qmd
    cd {{website_repo}}/gitproj/DeliberativeCoherence && quarto render Experiments_Paper.qmd
    cd {{website_repo}} && git add -- gitproj/DeliberativeCoherence && git commit -m "Update Deliberative Coherence" -- gitproj/DeliberativeCoherence && git push
    @echo "Deployed to https://oblinger.github.io/gitproj/DeliberativeCoherence/"

# Rebuild /trip/, the password-locked trip index, from Drive Oblio/Trip; commit and push
trip:
    {{website_repo}}/tools/trip-index
