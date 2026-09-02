# Ali Mokhtari AI Skills

Custom, portable Agent Skills for the Ali Mokhtari AI workflow.

## Available skill

### `human-simple-frontstage`

Turns complex backstage language into clear, natural Persian frontstage copy without losing meaning, truth, dignity, or brand authority.

Use it for:

- website and landing-page copy
- headings, CTAs, navigation, and forms
- onboarding, errors, and success messages
- privacy and consent copy
- educational explanations and social content
- converting product, marketing, AI, analytics, and UX jargon into language ordinary users understand on the first read

Core principle:

> Backstage can be complex. Frontstage must feel simple, human, and immediately understandable.

Instruction precedence:

1. Verified behavior, facts, legal and safety requirements
2. Locked project and brand documents
3. Explicit user constraints
4. The skill
5. Generic writing or UX advice

## Install for Codex

```bash
npx -y skills add https://github.com/alimokhtariw100/test-project \
  --skill "human-simple-frontstage" \
  --agent codex \
  --global
```

## Install for Claude Code

```bash
npx -y skills add https://github.com/alimokhtariw100/test-project \
  --skill "human-simple-frontstage" \
  --agent claude-code \
  --global
```

## Source

`skills/human-simple-frontstage/`

The skill contains:

- `SKILL.md` — core workflow and rules
- `agents/openai.yaml` — UI metadata
- `references/term-map-fa.md` — backstage-to-frontstage terminology map
- `references/persian-style.md` — Persian writing and mixed RTL/LTR rules
- `references/quality-gates.md` — truth, meaning, clarity, dignity, mobile, and brand tests
- `references/output-formats.md` — exact replacement, copy deck, form, audit, and final-only formats
- `references/examples.md` — concrete before/after examples
- `references/project-integration.md` — safe use inside repositories and alongside design/QA skills
