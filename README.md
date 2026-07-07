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
### AI & Agents

| Bundle | Source | License | Pages |
|---|---|---|---|
| [`dspy-book`](https://github.com/vinodborole/dspy-book-okf) | [dspy.ai](https://dspy.ai/) | MIT | 70 |
| [`mcp-book`](https://github.com/vinodborole/mcp-book-okf) | [modelcontextprotocol.io](https://modelcontextprotocol.io/docs) | CC-BY-4.0 | 16 |
| [`pydantic-ai-book`](https://github.com/vinodborole/pydantic-ai-book-okf) | [ai.pydantic.dev](https://ai.pydantic.dev/) | MIT | 90 |

### Web & Frameworks

| Bundle | Source | License | Pages |
|---|---|---|---|
| [`fastapi-book`](https://github.com/vinodborole/fastapi-book-okf) | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/tutorial/) | MIT | 51 |
| [`flask-book`](https://github.com/vinodborole/flask-book-okf) | [flask.palletsprojects.com](https://flask.palletsprojects.com/en/stable/) | BSD-3-Clause | 74 |

### Libraries & Tools

| Bundle | Source | License | Pages |
|---|---|---|---|
| [`httpx-book`](https://github.com/vinodborole/httpx-book-okf) | [python-httpx.org](https://www.python-httpx.org/) | BSD-3-Clause | 23 |

### Platforms & DevOps

| Bundle | Source | License | Pages |
|---|---|---|---|
| [`backstage-book`](https://github.com/vinodborole/backstage-book-okf) | [backstage.io](https://backstage.io/docs/) | Apache-2.0 | 139 |

### Languages & Learning

| Bundle | Source | License | Pages |
|---|---|---|---|
| [`rust-book`](https://github.com/vinodborole/rust-book-okf) | [doc.rust-lang.org](https://doc.rust-lang.org/book/) | MIT OR Apache-2.0 | 109 |
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
