# Project Integration

Use this reference when applying Human Simple Frontstage inside a codebase or alongside other skills.

## 1. Read source-of-truth documents first

Before editing visible copy, inspect the project's current canonical documents when they exist:

- brand positioning
- audience definition
- product and offer decisions
- voice and tone
- UX/UI law
- route map
- current state and handoff
- known issues and open decisions

Do not infer the current product architecture from old pages merely because code exists.

## 2. Precedence with other skills

Use this order:

1. Verified product behavior and high-stakes requirements
2. Locked project documents
3. Explicit user request
4. Human Simple Frontstage
5. General UX-writing or design guidance
6. Aesthetic preference

Examples:

- A design skill may prefer a short label, but a required condition must remain visible.
- A UX-writing skill may recommend informality, but a locked formal brand voice overrides it.
- A copy improvement must not change a route, payload, or event name unless the task includes that change.

## 3. Composition with design skills

Human Simple Frontstage owns:

- meaning
- audience comprehension
- hierarchy of information
- visible wording
- action clarity
- promise accuracy

Design skills own:

- layout
- typography
- spacing
- responsive composition
- visual emphasis
- motion

Shared responsibility:

- mobile line breaks
- button fit
- form step order
- progressive disclosure
- visible hierarchy

Do not let design force vague wording merely to fit a component. Change the component if accurate copy needs more room.

## 4. Composition with UX-writing skills

Use a general UX-writing skill for broad interaction patterns. Use Human Simple Frontstage as the Persian simplicity and backstage-to-frontstage filter.

Resolve differences by asking:

- Which version preserves the exact product meaning?
- Which version sounds natural in Persian?
- Which version is easier for the actual audience?
- Which version matches the project's locked voice?

Do not merge two versions into a longer compromise sentence.

## 5. Composition with RTL and accessibility audits

After copy changes, check:

- `lang="fa"`
- correct `dir="rtl"`
- mixed Persian/Latin rendering
- readable focus and error messages
- button labels at mobile widths
- headings and labels exposed correctly to assistive technology
- placeholder text is not the only label
- error meaning is not conveyed by color alone

Copy approval does not replace rendered RTL QA.

## 6. Composition with analytics

Preserve canonical event names and analytics semantics.

Visible text may change:

- «شروع مسیر رایگان دبی» → «رایگان شروع کن»

Internal event should remain stable unless analytics governance approves a rename:

- `free_course_click`

Do not include personal data in analytics properties merely because it appears in the form.

## 7. Composition with backend forms

Preserve unless explicitly authorized:

- form `name` attributes
- field IDs
- API endpoints
- payload keys
- validation hooks
- CSRF/security fields
- analytics event names
- success/error control flow

A label can change while the backend contract stays the same.

Example:

```html
<label for="request_type">برای چی کمک می‌خوای؟</label>
<select id="request_type" name="request_type">
```

The audience-facing label changed; `request_type` did not.

## 8. Existing project workflow

For copy-only changes:

1. Read canonical docs.
2. Inventory visible strings in scope.
3. Verify routes and functionality behind CTAs.
4. Produce or implement exact replacements.
5. Inspect the diff for accidental behavior changes.
6. Run RTL, responsive, link, and form checks as relevant.
7. Update handoff/docs if the project requires it.

For copy plus product changes, separate the commits when possible.

## 9. Scope control

When the user asks for copy correction, do not silently:

- redesign the page
- add animation
- change the color system
- create new product features
- restore legacy offers
- rename routes
- rewrite backend architecture
- add analytics vendors

Flag a product mismatch, but keep the requested scope.

## 10. Legacy content

Treat old code and archived pages as historical evidence, not current truth.

Before reusing an old offer, price, service, course, claim, or CTA:

- confirm it is current
- confirm its route works
- confirm the promised fulfillment exists
- confirm it fits the current architecture

If not verified, remove it from active frontstage copy or mark it for a decision.

## 11. Copy in configuration and code

Prefer existing localization/content structures when present.

Do not introduce a new content system for a small edit.

When text is duplicated across files:

- identify the duplicates
- change all intended instances
- avoid unrelated refactors during an urgent patch
- document drift risk if a centralized source is absent

## 12. Reviewable diffs

Keep changes easy to audit:

- one purpose per commit
- no formatting churn
- no minified-file edits unless the project requires them
- no generated asset changes mixed with copy edits
- no hidden behavior changes

A reviewer should be able to answer:

- What visible words changed?
- Why did they change?
- What behavior stayed untouched?

## 13. Production verification

Before declaring copy done, verify where relevant:

- final text is visible in production
- Persian glyphs and نیم‌فاصله render correctly
- no overflow at target mobile widths
- CTA lands on the promised page
- form labels match actual fields
- errors and success states still appear
- no old contradictory copy remains on the same path

## 14. Documentation note

If the project has continuity rules, record:

- scope of copy changes
- final approved promise/headline
- removed legacy messages
- open verification items
- routes and behavior intentionally preserved

Do not turn every string edit into a new strategy document. Update the existing canonical source when possible.
