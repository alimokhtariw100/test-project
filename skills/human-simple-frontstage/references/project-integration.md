# Project Integration

Use this reference when applying the skill inside a codebase, website, app, campaign system, or alongside other skills.

## Read order

Before editing visible copy, read the project’s canonical files in this order when available:

1. `START_HERE` or project entrypoint
2. locked decisions and source-of-truth documents
3. brand voice and copy rules
4. current-state and handoff documents
5. architecture, routes, integrations, and backend contracts
6. the actual visible implementation

Do not infer current product truth from old code alone when newer locked documents supersede it.

## Precedence

Apply:

`verified behavior and locked decisions`

before:

`brand preference`

before:

`this skill`

before:

`generic UX-writing advice`

If two source-of-truth documents conflict, flag the conflict instead of silently choosing the version that produces nicer copy.

## Copy-only changes

When the task is copy-only:

- preserve layout and behavior
- preserve IDs, classes, routes, field names, event names, ARIA links, and backend payload keys
- do not add sections or features
- do not change form logic
- do not rename technical identifiers
- keep the diff focused

## CTA verification

Before publishing a CTA:

1. verify that the destination exists
2. verify that the promised action matches the destination
3. verify that the route is not intentionally deferred or archived
4. avoid sending traffic to a 404, placeholder, or unfinished product

If verification is impossible, use a non-promissory label or keep the CTA unpublished.

## Feature truth

Do not write copy for a feature merely because:

- code for an old version exists
- a design mockup contains it
- another product uses it
- a strategy document mentions it as future work
- the copy would make the page stronger

Only present a feature as available when the current system supports it.

## Forms and backend contracts

- Keep required fields aligned with backend validation.
- Do not promise that a request is saved unless the endpoint and success state are real.
- Preserve error handling and retry behavior.
- Do not add sensitive information requests without a clear product need.
- Keep analytics copy separate from actual lead or payment operations.

## Working with other skills

### UX-writing skill

Use `human-simple-frontstage` as the audience-simplicity and Persian-clarity layer.

Use a general UX-writing skill for broader patterns such as accessible labels, error structures, empty states, and content consistency.

If recommendations conflict, prefer the project’s locked voice and this skill’s truth/meaning gates.

### Design skills

Design must support comprehension.

Check that:

- heading hierarchy matches copy hierarchy
- emphasis lands on the intended phrase
- mobile wrapping does not change meaning
- buttons remain readable and tappable
- helper text is not visually hidden

Do not compensate for weak copy with decorative design.

### RTL and internationalization skills

After finalizing Persian strings, audit:

- `lang="fa"`
- `dir="rtl"`
- mixed Persian/English rendering
- Persian/Latin digits
- punctuation direction
- button and input alignment
- line breaks at 360, 375, 390, and 430 pixels when mobile traffic matters

### QA skills

Before release, verify:

- no CTA destination is broken
- forms still validate and submit
- visible strings match the approved copy deck
- no old copy remains in duplicate mobile/desktop markup
- no placeholder or hidden version overrides the new text
- no analytics or event key was renamed accidentally

### Analytics skills

Visible analytics and consent copy must match actual behavior.

Do not claim:

- «اطلاعات شخصی ارسال نمی‌شود» without inspecting payloads
- «فقط آمار کلی» if detailed identifiers are collected
- «فقط با اجازه شما» if scripts fire before consent

## Commit discipline

Keep copy changes separate from broad refactors when practical.

A useful sequence:

1. copy update
2. functional wiring only if requested
3. QA fixes
4. documentation and handoff

Do not bury visible-message changes inside an unrelated architecture commit.

## Handoff requirements

When a project uses continuity documents, record:

- what visible copy changed
- what did not change
- any claims intentionally removed
- any unresolved copy decisions
- routes or features that remain deferred
- the exact files changed

A new agent should be able to understand why the copy says what it says without the original conversation.
