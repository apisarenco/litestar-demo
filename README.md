# Example Litestar API

Also demoing VS.Code powerful inlayHints feature.

To enable inlayHints in VS.Code, add (uncomment) the following to your `.vscode/settings.json`:

```json
    "python.analysis.inlayHints.functionReturnTypes": true,
    "python.analysis.inlayHints.pytestParameters": true,
    "python.analysis.inlayHints.variableTypes": true,
    "python.analysis.typeCheckingMode": "basic"
```

## Setup

Install using [Poetry](https://python-poetry.org/docs/).

```bash
poetry install
```

## Running litestar

```bash
poetry run litestar run
```

... then you can access the OpenAPI docs at http://127.0.0.1:8000/schema/elements
