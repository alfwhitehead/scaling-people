# Dev setup

This directory holds local development scaffolding that is NOT part of the published plugin.

## `marketplace/.claude-plugin/marketplace.json`

A one-plugin marketplace declaration used to install this repo into Claude Code locally, without publishing it through the `klick-ai-playbooks` marketplace or any other shared distribution channel.

The marketplace is called `scaling-people-local`. It declares one plugin (`klick-management`) whose `source` is `./klick-management` — a symlink inside this directory pointing at the plugin subdir (`../../klick-management`). Claude Code's marketplace loader only resolves plugin sources that are subdirectories of the marketplace root, so the symlink is what makes a same-repo standalone marketplace work.

## Install locally

1. Edit `~/.claude/settings.json`:

   Under `extraKnownMarketplaces`, add:

   ```json
   "scaling-people-local": {
     "source": {
       "source": "directory",
       "path": "/Users/awhitehead/Code/scaling-people-skills/dev/marketplace"
     }
   }
   ```

   Under `enabledPlugins`, add:

   ```json
   "klick-management@scaling-people-local": true
   ```

2. Restart Claude Code so the loader picks up the new marketplace and plugin.

## Uninstall

Remove the two settings entries above. Optionally delete this `dev/` directory.

## Why not merge into `klick-ai-playbooks` directly?

The plugin is `v0.1.0` and still being tested. Merging into the shared `klick-ai-playbooks` marketplace would expose it to coachees before it's been validated end-to-end. Use this standalone marketplace until the plugin is ready to graduate.
