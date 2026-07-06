# Adding a bundle to the registry

1. **Build and publish your bundle** (full guide:
   [okf-kit/docs/PUBLISHING.md](https://github.com/vinodborole/okf-kit/blob/main/docs/PUBLISHING.md)):

   ```bash
   okf build https://your-docs.example.com -o your-docs-okf
   okf validate your-docs-okf     # must be CONFORMANT
   okf zip your-docs-okf
   ```

   Put the bundle in its own repo (use the
   [okf-bundle-template](https://github.com/vinodborole/okf-bundle-template))
   and attach the zip to a GitHub Release.

2. **Open a PR** adding one entry to [`registry.yaml`](registry.yaml):

   ```yaml
   - name: your-docs                # unique, kebab-case
     source_url: https://your-docs.example.com
     description: One line about it.
     license: CC-BY-4.0             # REQUIRED — the content's license
     publisher: github.com/you
     repo: https://github.com/you/your-docs-okf
     download: https://github.com/you/your-docs-okf/releases/latest/download/your-docs-okf.zip
     okf_version: "0.1"
     tags: [docs, topic]
   ```

   CI validates the schema and the entry. A maintainer reviews licensing.

## Rules

- **Redistribution rights are required.** Owner-published, or a license that
  permits redistribution (CC-BY, CC-BY-SA, MIT/Apache-licensed project docs,
  public domain). Unverifiable licensing → the PR is declined. See
  [policies/LICENSING.md](policies/LICENSING.md).
- **One bundle per PR**, `name` unique, `license` and `source_url` present.
- Prefer bundles that **self-sync** (a weekly Action) so they stay fresh.
