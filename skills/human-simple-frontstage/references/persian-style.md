# Persian Style Guide

Use these rules for natural, clear Persian frontstage copy. Adapt to the project’s explicit voice rules when they exist.

## Natural syntax

Prefer Persian sentence order and familiar verbs.

Avoid translated-English constructions such as:

- «تجربه خود را ارتقا دهید»
- «قدرت هوش مصنوعی را آزاد کنید»
- «در راستای بهبود تجربه کاربران»

Prefer:

- «راحت‌تر کار کن»
- «از AI برای این کار استفاده کن»
- «می‌خوایم سایت رو بهتر کنیم»

## Formality levels

### Human-neutral

Use for most public UI:

- «شماره‌ت رو وارد کن.»
- «درخواستت ثبت شد.»

### Warm-personal

Use for founder-led education and community:

- «بگو دقیقاً چی می‌خوای بسازی.»
- «از همین‌جا شروع کن.»

### Trust-formal

Use for payment, privacy, medical, legal, and high-stakes contexts:

- «شماره تماس شما فقط برای پیگیری همین درخواست استفاده می‌شود.»
- «پیش از پرداخت، مبلغ و شرایط را بررسی کنید.»

Do not mix registers randomly inside one flow.

## نیم‌فاصله

Use نیم‌فاصله consistently in standard compounds and verb forms when it improves reading:

- می‌خوام
- می‌تونی
- ثبت‌نام
- به‌روزرسانی
- مرحله‌به‌مرحله
- هوش مصنوعیِ اختصاصی only when the ezafe matters

Do not obsess over نیم‌فاصله at the cost of natural social-native voice. Follow the project’s existing standard.

## Persian and English together

- Preserve official product and brand names: `ChatGPT`, `Google Flow`, `Claude`, `Codex`.
- Place English identifiers on their own when mixed-direction rendering becomes unclear.
- Keep code, URLs, file paths, event names, API fields, and command names exactly unchanged.
- Explain an unfamiliar English term in Persian rather than creating an awkward literal translation.

Example:

«Flow رو باز کن و روی New Project بزن؛ یعنی یک پروژه جدید بساز.»

## Digits

Choose one digit system per surface.

- Public Persian copy may use Persian digits when the design and input behavior support them.
- Preserve Latin digits in URLs, code, versions, event names, dimensions, and technical commands.
- Normalize user-entered Persian and English phone digits in product logic when the task includes validation; do not silently change the displayed value unless intended.

## Punctuation

- Use Persian comma `،` in Persian prose.
- Avoid repeated exclamation marks.
- Avoid decorative ellipses unless hesitation is meaningful.
- Use colon when it genuinely improves scanning.
- Keep button labels without terminal punctuation.
- Avoid em dashes in Persian UI unless the brand deliberately uses them.

## Line breaks and mobile

- Break by meaning, not merely by available width.
- Keep a headline’s emphasized phrase together.
- Avoid leaving one weak word on a final line.
- Keep paragraphs short: usually one to three sentences per mobile block.
- Do not place essential conditions in tiny helper text.
- Keep button labels short enough to avoid wrapping where possible.

## Voice and pronouns

- Use «تو» only when the brand consistently speaks directly and warmly.
- Use «شما» for formal, regulated, or mixed-audience contexts.
- Do not switch between «تو» and «شما» inside one journey without a deliberate reason.
- Prefer gender-neutral language unless the product intentionally targets a specific group.

## Slang

Use slang only when:

- the project explicitly wants a social-native voice
- the audience uses it
- trust and clarity remain intact

Do not use slang to fake closeness.

## Emoji

Use emoji only when the surface and brand call for it. Avoid emoji in:

- legal and privacy copy
- payment states
- serious errors
- technical identifiers
- premium-minimal pages unless explicitly requested

One intentional emoji is usually stronger than several decorative ones.

## CTA style

Prefer immediate, concrete verbs:

- «رایگان شروع کن»
- «آموزش رو ببین»
- «درخواست مشاوره»
- «شماره‌م رو ثبت کن» only when the action really does that

Avoid:

- «بیشتر بدانید»
- «کلیک کنید»
- «ادامه فرایند»
- «ثبت» when the object is unclear

## Error style

Keep errors calm and useful.

Pattern:

`مشکل مشخص + کار بعدی`

Examples:

- «شماره‌ت کامل نیست. یه بار چکش کن.»
- «این صفحه باز نشد. اینترنتت رو بررسی کن و دوباره بزن.»
- «درخواست ثبت نشد. چند لحظه دیگه دوباره امتحان کن.»

## Success style

Confirm reality, then explain what happens next.

Examples:

- «درخواستت ثبت شد. بعد از بررسی باهات تماس می‌گیریم.»
- «پرداخت انجام شد. حالا وارد حسابت شو و آموزش رو شروع کن.»

Never promise a time, access, certificate, refund, or human response unless the system and operations guarantee it.
