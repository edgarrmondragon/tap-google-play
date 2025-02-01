py := '3.13'

update: lock-upgrade pre-commit-autoupdate gha build pre-commit test

lock-upgrade:
    uv lock --upgrade

pre-commit-autoupdate:
    uvx --python={{py}} --with pre-commit-uv pre-commit autoupdate

gha:
    uvx --python={{py}} gha-update

build:
    uv build

pre-commit:
    uvx --python={{py}} --with pre-commit-uv pre-commit run --all-files

test:
    uvx --python={{py}} --with=tox-uv tox run-parallel
