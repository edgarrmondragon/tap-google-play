<div align="center">

# tap-google-play

<div>
  <a href="https://results.pre-commit.ci/latest/github/edgarrmondragon/tap-google-play/main">
    <img alt="pre-commit.ci status" src="https://results.pre-commit.ci/badge/github/edgarrmondragon/tap-google-play/main.svg"/>
  </a>
  <a href="https://github.com/edgarrmondragon/tap-google-play/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/edgarrmondragon/tap-google-play"/>
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json" alt="Ruff" style="max-width:100%;">
  </a>
</div>

Singer tap for Google Play Reviews. Built with the [Meltano Singer SDK](https://sdk.meltano.com).

Based on [hotglue/tap-google-play](https://gitlab.com/hotglue/tap-google-play).

</div

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`
* `batch`

## Settings

| Setting             | Required | Default | Description |
|:--------------------|:--------:|:-------:|:------------|
| app_id              | True     | None    | The app ID to extract reviews from |
| start_date          | False    | None    | The date to start extracting reviews from |
| stream_maps         | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |
| stream_map_config   | False    | None    | User-defined config values to be used within map expressions. |
| flattening_enabled  | False    | None    | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth| False    | None    | The max depth to flatten schemas. |
| batch_config        | False    | None    |             |

A full list of supported settings and capabilities is available by running: `tap-google-play --about`

## Supported Python Versions

* 3.8
* 3.9
* 3.10
* 3.11

## Usage

You can easily run `tap-google-play` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-google-play --version
tap-google-play --help
tap-google-play --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests` subfolder and then run:

```bash
poetry run pytest
```

You can also test the `tap-google-play` CLI interface directly using `poetry run`:

```bash
poetry run tap-google-play --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-google-play
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-google-play --version
# OR run a test `elt` pipeline:
meltano elt tap-google-play target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
