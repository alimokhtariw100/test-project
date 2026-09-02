# Evaluation Cases

Use these cases when testing or updating the skill. The exact wording may vary, but the required behavior must remain.

## Case 1 — Generic hero

Input:

«با راهکارهای نوین هوش مصنوعی، آینده کسب‌وکار خود را متحول کنید.»

Context:

Founder-led education brand. Audience is familiar with AI but overwhelmed. Core promise is choosing only what is useful.

Expected behavior:

- Reject generic transformation language.
- Lead with the audience problem or point of view.
- Produce natural Persian.
- Do not invent a guarantee.

Strong direction:

«قرار نیست همه‌ی AI رو یاد بگیری؛ فقط چیزی که به کارت می‌آد.»

## Case 2 — Literal internal terminology

Input:

«با تکمیل Diagnostic، Personalized Learning Path شما فعال می‌شود.»

Expected behavior:

- Do not transliterate or literally translate the terms.
- Explain the visible action and result.
- Flag the result if personalization is not verified.

Strong direction:

«چند سؤال جواب بده تا ببینی از کجا شروع کنی.»

## Case 3 — Unsupported CTA

Input:

Button: «مسیر شخصی من رو بساز»

Product reality:

The button only opens a static list of three lessons.

Expected behavior:

- Fail the Truth gate.
- Recommend an accurate action label.

Strong direction:

«آموزش‌ها رو ببین»

## Case 4 — Form error

Input:

«خطای 422: مقدار ورودی شماره موبایل نامعتبر است.»

Tone:

Warm founder brand.

Expected behavior:

- Remove internal code from visible copy.
- State problem and recovery.

Strong direction:

«شماره‌ت کامل نیست. یه بار چکش کن.»

## Case 5 — Trust-formal error

Same input as Case 4.

Tone:

Banking or legal service.

Expected behavior:

- Preserve simple language.
- Increase restraint and formality.

Strong direction:

«شماره تماس کامل نیست. لطفاً دوباره بررسی کنید.»

## Case 6 — High-stakes guarantee

Input:

«با این دوره قطعاً درآمدت چند برابر می‌شود.»

Evidence:

No guaranteed result exists.

Expected behavior:

- Fail Truth gate.
- Remove guarantee.
- Keep a useful, specific promise if supported.

Strong direction:

«یاد می‌گیری AI رو وارد کار واقعی‌ات کنی؛ نتیجه مالی به اجرا و شرایط خودت بستگی داره.»

## Case 7 — Privacy copy

Input:

«با استفاده از این وب‌سایت با پردازش داده‌های شما موافقت می‌نمایید.»

Actual behavior:

Analytics requires explicit consent. No PII goes to vendors.

Expected behavior:

- Explain purpose and choice.
- Do not imply that mere use equals consent.
- Only state the no-PII claim after verification.

Strong direction:

«برای بهتر کردن سایت، با اجازه تو آمار کلی استفاده رو بررسی می‌کنیم. اسم و شماره‌ت برای این آمار ارسال نمی‌شه.»

Buttons:

«موافقم» / «فقط ضروری»

## Case 8 — User asks for final only

Request:

«سه اسم دکمه بده، فقط لیست.»

Expected behavior:

- Output three labels only.
- No rationale, heading, or follow-up.

## Case 9 — Expert audience

Input:

«نرخ تبدیل کمپین ۲٫۶۹٪ و نرخ تبدیل حضور وبینار به خرید ۲۳٪ بود.»

Audience:

Marketing team.

Expected behavior:

- Do not over-simplify away exact metrics.
- Add plain interpretation only if useful.

Strong direction:

«نرخ تبدیل کل ۲٫۶۹٪ بود. از کسانی که تا مرحله ارائه فروش در وبینار ماندند، ۲۳٪ خرید کردند.»

## Case 10 — Mixed Persian and identifiers

Input:

«رویداد lead_success بعد از ارسال فرم به /api/leads اجرا می‌شود.»

Expected behavior:

- Preserve `lead_success` and `/api/leads` exactly.
- Simplify surrounding Persian only.
- Do not rename technical contracts.

## Case 11 — Mobile wall of text

Input:

A 120-word hero paragraph containing brand story, product mechanism, proof, and CTA.

Expected behavior:

- Separate promise, support, proof, and action.
- Keep one main idea in the first viewport.
- Do not delete factual conditions.

## Case 12 — Childish simplification

Input:

«هوش مصنوعی مثل یه ربات کوچولوی بامزه‌ست که همه کاراتو می‌کنه.»

Audience:

Adult business owners.

Expected behavior:

- Fail Dignity and Truth gates.
- Use an adult concrete explanation.

Strong direction:

«AI می‌تونه بخشی از کارهای تکراری رو سریع‌تر انجام بده؛ اول باید مشخص کنیم کدوم کار ارزش خودکارشدن داره.»

## Case 13 — Repetition as buzzword

Input page:

Uses «مسیر» in hero, CTA, section title, every card, form, and footer.

Expected behavior:

- Keep the word where it carries meaning.
- Replace unnecessary instances with specific actions such as «شروع کن»، «آموزش رو ببین»، «قدم بعدی»، or «درخواست مشاوره».

## Case 14 — Copy-only repository task

Request:

«فقط متن‌های Homepage رو عوض کن.»

Expected behavior:

- Read canonical docs.
- Preserve layout, routes, IDs, form keys, and analytics events.
- Keep changes reviewable.
- Do not install a framework or redesign the page.

## Case 15 — Missing product fact

Input:

«بعد از خرید، فوراً به همه درس‌ها دسترسی پیدا می‌کنی.»

Product state:

Access behavior is unknown.

Expected behavior:

- Do not publish the claim.
- Ask for verification or provide a safer conditional version.

Failure condition:

Choosing the stronger claim because it converts better.
