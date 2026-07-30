# Contributing

Thank you for considering a contribution to `speciality`.

## Principles

- Prefer small, reviewable changes with a clear purpose.
- Do not create empty commits, fake issues, or contribution-graph spam.
- Do not rewrite Git history.
- Do not modify the default branch (`UsmanGhias`) directly.
- Do not add secrets, credentials, customer data, or private URLs.
- Do not invent features that are not needed for a reusable speciality catalogue.

## Development flow

1. Fork or branch from the latest default branch.
2. Create a feature branch (for example `improve/...` or `fix/...`).
3. Implement a focused change with tests when behavior changes.
4. Update documentation when user-facing behavior changes.
5. Open a pull request against `UsmanGhias`.
6. Wait for genuine review before merge.

## Coding guidelines

- Target Odoo 18 APIs and XML conventions (`list` views, not legacy `tree` where Odoo 18 expects `list`).
- Keep the module standalone unless there is an approved need to link other models.
- Use clear validation messages and translated user-facing strings.
- Keep dependencies minimal (`base` only unless justified).

## Tests

- Add or update Odoo tests under `speciality/tests/`.
- Run Odoo tests when an Odoo environment is available.
- Always run static checks (`compileall`, XML well-formedness, secret scan).

## Pull requests

Use the repository pull-request template. Explain:

- problem
- solution
- compatibility
- tests / manual verification
- security impact
- limitations

## License note

No open-source license has been declared yet. Until a license is added by the repository owner, reuse and redistribution rights are not granted.
