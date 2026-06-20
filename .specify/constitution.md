# Spec-Kit Constitution

## Principles

1. **Spec-First Development** — Every feature MUST begin with a spec before implementation.
2. **Test Alignment** — Tests MUST reflect the specs exactly.
3. **Documentation Parity** — Every spec MUST produce corresponding documentation.
4. **Review Gate** — No merge without an approved spec.

## Structure

- `.specify/` — Spec-Kit configuration and templates
- `specs/` — Feature specifications organized by domain
- Templates define the spec format for different work types

## Workflow

1. Author a spec in `specs/` using the appropriate template
2. Submit spec for review
3. Implement feature per spec
4. Update tests to match spec
5. Document per spec
6. Review against spec before merge

## Enforcement

- CI pipeline MUST validate that specs exist for new features
- Specs MUST be versioned alongside code
- Breaking changes MUST update existing specs before code changes
