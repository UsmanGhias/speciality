# Speciality (Odoo 18)

Reusable Odoo 18 module for managing a clean list of business specialities.

> Status: initial functional module scaffold. Odoo runtime tests are authored but may not have been executed in this environment. Do not treat this as fully production-proven until installed and tested in Odoo 18.

## Overview

`speciality` provides a standalone model (`speciality.speciality`) so teams can maintain a reusable catalogue of specialities with names, unique codes, sequencing, and archive support.

## Problem solved

Many business applications need a shared speciality list (for later optional linking to employees, partners, or products). This module starts as a **standalone, reusable catalogue** without forcing those integrations in v1.

## Supported Odoo version

- **Odoo 18** (`version` field: `18.0.1.0.0`)
- Dependency: `base` only

## Features

- Name (translatable)
- Unique code with validation
- Active / archived flag
- Sequence ordering (list handle)
- Description (translatable)
- List, form, and search views
- Active / archived filters and group-by
- Access rights for internal users (`base.group_user`)

## Module structure

```text
speciality/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── speciality.py
├── views/
│   └── speciality_views.xml
├── security/
│   └── ir.model.access.csv
├── tests/
│   ├── __init__.py
│   └── test_speciality.py
├── README.md
└── CHANGELOG.md
```

## Installation

1. Copy or clone this repository into your Odoo 18 addons path so the `speciality` directory is importable as an addon.
2. Update the Apps list.
3. Install **Speciality**.
4. Open the **Specialities** menu.

Example (development):

```bash
# Ensure this repository root is on the Odoo addons path, then:
odoo-bin -d <database> -i speciality --stop-after-init
```

## Configuration

No special system parameters are required. Create specialities from the menu and set sequence as needed.

## Usage

1. Open **Specialities → Specialities**.
2. Create a record with Name and Code.
3. Optionally set Description and Sequence.
4. Archive records by unchecking **Active** (or use the Archived filter).

Validation rules:

- Code is required and unique.
- Code cannot be blank or contain spaces.

## Access rights

Internal users (`base.group_user`) receive create / read / write / unlink on `speciality.speciality`.

## Testing

Odoo tests live in `speciality/tests/test_speciality.py`.

If Odoo is available:

```bash
odoo-bin -d <database> --test-enable --stop-after-init -i speciality
```

If Odoo is unavailable, still run honest static checks:

```bash
python -m compileall speciality
git diff --check
```

## Known limitations

- No employee / partner / product links in v1 (by design).
- No demo data.
- No declared open-source license yet.
- Odoo TransactionCase tests require an Odoo environment to execute.

## Contribution

See [`CONTRIBUTING.md`](../CONTRIBUTING.md).

## Security reporting

See [`SECURITY.md`](../SECURITY.md).

## License status

No open-source license has been declared yet. Until a license is added by the repository owner, reuse and redistribution rights are not granted.

## Maintainer

- GitHub: [UsmanGhias](https://github.com/UsmanGhias)
- Repository: https://github.com/UsmanGhias/speciality
