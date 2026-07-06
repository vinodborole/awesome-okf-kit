# awesome-okf-kit

**A community registry of ready-to-use [OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) knowledge bundles.**

Pre-built, agent-ready, self-updating knowledge for popular docs sites — pull
one and chat with it in two commands, with your own LLM or fully offline:

```bash
pip install okf-kit
okf get rust-book              # download + validate a published bundle
okf chat rust-book --provider ollama
```

Built with **[okf-kit](https://github.com/vinodborole/okf-kit)** (the library)
— part of the [calknowledge](https://github.com/vinodborole/calknowledge)
ecosystem.

## How it works

This repo is an **index**, not a bundle store. Each bundle lives in its own
repo and ships as a release zip; [`registry.yaml`](registry.yaml) points at
them, and `okf get` downloads the zip, validates it, and installs it to
`~/.okf/bundles/`.

## Catalog

<!-- CATALOG:START (generated from registry.yaml) -->
| Bundle | Source | License | Tags |
|---|---|---|---|
| [`rust-book`](https://github.com/vinodborole/rust-book-okf) | [doc.rust-lang.org/book](https://doc.rust-lang.org/book/) | MIT OR Apache-2.0 | rust, programming, book, docs |
| [`backstage-book`](https://github.com/vinodborole/backstage-book-okf) | [backstage.io/docs](https://backstage.io/docs/) | Apache-2.0 | backstage, developer-portal, cncf, docs |
<!-- CATALOG:END -->

## Publish your bundle

See **[CONTRIBUTING.md](CONTRIBUTING.md)** and okf-kit's
[docs/PUBLISHING.md](https://github.com/vinodborole/okf-kit/blob/main/docs/PUBLISHING.md).
In short: `okf build` → ship as a release zip with a weekly self-sync Action →
open a PR adding a `registry.yaml` entry. CI validates the schema and runs
`okf validate` on your bundle.

> **Licensing:** publish only content you may redistribute — your own site, or
> permissively-licensed content (CC-BY, CC-BY-SA, open-source project docs,
> public domain). `license` and `source_url` are required. See
> [policies/LICENSING.md](policies/LICENSING.md) and
> [policies/TAKEDOWN.md](policies/TAKEDOWN.md).

## License

The registry index and tooling are MIT. Each bundle carries its own content
license (the `license` field of its entry).
