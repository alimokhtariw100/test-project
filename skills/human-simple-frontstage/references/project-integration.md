# Project Integration

Use this guide when applying Human-Simple Frontstage inside a repository or alongside other skills.

## 1. Read the project before rewriting

Inspect, in this order when available:

1. `START_HERE` or equivalent project entrypoint
2. locked decisions and source-of-truth documents
3. brand voice and copy rules
4. current state, open decisions, known issues, and next steps
5. actual UI source and backend behavior
6. analytics event dictionary, route map, form contract, and legal text when relevant

Do not treat an old page, uncommitted file, stale design, or abandoned offer as current merely because it exists in the repository.

## 2. Preserve technical contracts

Unless the task explicitly includes behavior changes, preserve:

- element IDs and selectors
- route paths and canonical URLs
- form field names
- backend payload keys
- analytics event names and allowed properties
- ARIA labels and relationships
- translation keys
- structured-data keys
- test selectors
- legal identifiers and company names

Change visible copy without silently changing the contract behind it.

## 3. Match copy to real behavior

Before approving a CTA, verify:

- the destination exists
- the destination matches the label
- the route is not a known 404 or deprecated offer
- the feature is implemented
- the form is actually stored or delivered
- the success message describes what truly happened

If verification is unavailable, mark it clearly:

`NEEDS VERIFICATION`

Do not convert uncertainty into confident copy.

## 4. Keep scope clean

Separate:

- copy changes
- design changes
- behavior changes
- backend changes
- analytics changes
- documentation changes

Do not use a copy task as permission for a broad refactor.

Prefer reviewable commits such as:

```text
copy: simplify homepage frontstage language

ui: improve mobile hierarchy without changing content

fix(forms): align error messages with validation behavior
```

## 5. Mobile-first application

For mobile-heavy products:

- inspect copy at the target mobile width before desktop
- keep primary meaning in the first visible screen
- prevent headings from becoming six-line walls
- keep button labels short and specific
- avoid long explanatory paragraphs before the user’s first useful action
- preserve readable RTL ordering when English names, digits, and punctuation appear

Do not approve copy from source code alone when rendered output is available.

## 6. Collaboration with other skills

### With `ux-writing`

Use Human-Simple Frontstage for:

- audience knowledge level
- Persian naturalness
- jargon removal
- concept simplification
- brand-specific plain language

Use UX Writing for:

- microcopy patterns
- form sequencing
- error and success behavior
- accessibility of labels and instructions

When they conflict, preserve factual truth first, then project voice, then choose the clearer user-facing result.

### With `design-taste-frontend`

Do not let visual ambition reduce comprehension.

Copy hierarchy should define:

- primary statement
- supporting explanation
- primary action
- secondary action

The design skill may change layout, typography, or emphasis, but must not invent claims or fragment one sentence until its meaning is lost.

### With `redesign-existing-projects`

Audit current copy and current behavior before replacement.

Do not rewrite from scratch when the existing wording contains necessary facts, legal conditions, or useful search language.

### With `i18n-rtl-audit`

After writing:

- verify `lang="fa"` and RTL behavior where applicable
- inspect mixed-direction strings
- inspect punctuation around English tool names
- inspect mobile line breaks
- verify screen-reader labels remain meaningful

### With link, form, privacy, and diff review skills

Use:

- broken-link review for all action labels
- form-validation review for errors, required states, and success messages
- privacy review for consent and analytics claims
- diff-risk review before deployment

Human-Simple Frontstage does not replace those checks.

## 7. Brand source of truth

When a project has a brand rule such as:

> «به زبان آدمیزاد»

Translate it into observable behavior:

- no unexplained internal terms
- one clear idea at a time
- concrete outcome
- natural spoken Persian
- no fake authority
- no childish tone
- clear next action

Do not turn the slogan itself into a phrase repeated on every section.

## 8. Documentation

When the new wording changes a durable brand rule, term policy, or product promise:

- update the canonical brand/copy document
- record the reason
- distinguish `LOCKED`, `PROPOSED`, and `NEEDS VERIFICATION`
- keep old historical documents rather than silently rewriting history

When the change is page-specific, do not inflate it into a global law.

## 9. Safe implementation sequence

```text
Read source of truth
→ inspect rendered surface and behavior
→ lock facts and constraints
→ rewrite copy
→ run quality gates
→ verify mobile and RTL
→ verify links/forms
→ review diff
→ update only necessary documentation
```

## 10. Stop conditions

Stop and report the exact blocker when:

- the current source contradicts a locked decision
- the CTA destination is missing
- the form behavior is unknown and the success message depends on it
- legal or medical meaning cannot be preserved confidently
- multiple active source-of-truth documents conflict
- the user requests verbatim preservation but the source is unavailable

Do not improvise past these blockers.
