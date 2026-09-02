# Persian Frontstage Style Guide

Use this guide for natural, readable Persian interface and audience-facing copy. Project-specific brand rules override these defaults.

## 1. Natural Persian syntax

Prefer Persian sentence order and spoken rhythm. Avoid translated English structures.

Less natural:

«تجربه‌ای که برای شما شخصی‌سازی شده است.»

More natural:

«چیزی رو می‌بینی که به نیاز خودت می‌خوره.»

Less natural:

«برای آغاز سفر خود کلیک کنید.»

More natural:

«شروع کن.»

## 2. Formality level

Choose deliberately:

- **محاوره محترمانه:** default for founder-led education, creator brands, onboarding, and support
- **معیار ساده:** default for general public information, articles, and broad audiences
- **رسمی ساده:** use for legal, privacy, payment, medical, financial, and institutional contexts

Do not mix registers randomly inside one flow.

Example of an inconsistent flow:

- «اسمت رو بنویس»
- «لطفاً شماره تماس خویش را وارد نمایید»

Choose one coherent voice.

## 3. Colloquial endings

In conversational UI, forms like these are acceptable when they match the brand:

- می‌خوای
- می‌تونی
- می‌دونی
- به دردت می‌خوره
- باهات تماس می‌گیریم

Avoid exaggerated phonetic spelling:

- میخای
- میتونییی
- چیکاررر

Keep the writing clean even when the voice is spoken.

## 4. نیم‌فاصله

Use نیم‌فاصله consistently in common compounds and verb forms where it improves reading:

- می‌خوای
- می‌تونی
- به‌روزرسانی
- مرحله‌به‌مرحله
- دست‌به‌کار
- هوش مصنوعی‌ات

Do not over-engineer obscure compounds if it makes editing or implementation fragile.

## 5. Persian and English terms

Keep exact product names, tools, code identifiers, routes, and event names unchanged:

- ChatGPT
- Google Flow
- `/api/leads`
- `lead_success`

For unfamiliar terms, explain the meaning instead of forcing a literal Persian replacement.

Good:

«با Google Flow ویدیو می‌سازی.»

Good when clarification is needed:

«API یعنی راهی که دو سیستم از طریقش با هم حرف می‌زنن.»

Avoid mixed sentences where every second word is English merely to sound technical.

## 6. Direction and isolation

For implementation:

- Set document language correctly: `lang="fa"`
- Use `dir="rtl"` for Persian interfaces
- Isolate code, URLs, phone numbers, prices with Latin identifiers, and event names where bidirectional rendering can break
- Do not manually reverse strings
- Test the real rendered text on mobile

When writing Markdown or plain text, put long code identifiers and paths in backticks.

## 7. Digits

Follow the project's established convention. If no convention exists:

- Use Persian digits in audience-facing prose and simple counts: ۳ مرحله، ۱۰ دقیقه
- Keep Latin digits inside code, URLs, version numbers, analytics identifiers, and technical commands
- For phone input, accept and normalize both Persian and Latin digits when technically possible
- Keep price formatting consistent across one product flow

Do not mix `۳ میلیون` and `3,000,000` without a reason.

## 8. Punctuation

- Use Persian comma: `،`
- Use Persian question mark: `؟`
- Keep punctuation light
- Avoid repeated exclamation marks
- Avoid decorative dots and slashes unless the visual system requires them
- Do not use English semicolon patterns in everyday Persian UI

Prefer:

«درخواستت ثبت شد. بعد از بررسی باهات تماس می‌گیریم.»

Avoid:

«درخواست شما با موفقیت ثبت گردید!!!»

## 9. Parentheses and quotation marks

Use Persian quotation marks when quoting visible Persian copy:

«رایگان شروع کن»

Keep technical identifiers in backticks.

Avoid stacking parentheses. Rewrite the sentence instead.

## 10. Sentence length

Use one main idea per sentence. Break long formal sentences into smaller units.

Before:

«با تکمیل فرم زیر و ثبت اطلاعات تماس، کارشناسان مجموعه پس از انجام بررسی‌های لازم در اولین فرصت ممکن با شما ارتباط برقرار خواهند کرد.»

After:

«درخواستت رو بفرست. بعد از بررسی باهات تماس می‌گیریم.»

Only keep more detail when it changes expectations.

## 11. Headings

A heading should answer at least one of these:

- این بخش درباره چیه؟
- چه مشکلی رو حل می‌کنه؟
- چه نتیجه‌ای می‌گیرم؟
- الان باید چی‌کار کنم؟

Avoid headings that are only internal labels:

- «راهکارها»
- «خدمات تخصصی»
- «اکوسیستم»
- «مزیت‌ها»

Prefer specific headings:

- «می‌خوای با AI چی بسازی؟»
- «از اینجا رایگان شروع کن.»
- «مشکل، کمبود آموزش نیست.»

## 12. Buttons

Use the immediate action or result:

- «رایگان شروع کن»
- «آموزش رو ببین»
- «درخواست مشاوره»
- «دوباره تلاش کن»

Avoid unnecessary politeness inside short controls:

- «لطفاً برای مشاهده بیشتر کلیک نمایید»

Do not end button labels with punctuation.

## 13. Forms

Use short human questions:

- «اسمت چیه؟»
- «برای چی کمک می‌خوای؟»
- «الان چقدر با AI آشنایی؟»

For trust-sensitive contexts, soften the informality:

- «نام و نام خانوادگی»
- «شماره تماس»
- «موضوع درخواست»

Help text should explain only what is not obvious.

## 14. Errors

Do not blame the user. Name the issue and the fix.

- «شماره‌ت کامل نیست. یه بار چکش کن.»
- «اتصال قطع شد. دوباره تلاش کن.»
- «این صفحه پیدا نشد. از صفحه اصلی ادامه بده.»

Do not expose internal codes unless support needs them.

## 15. Premium tone

Premium Persian is not heavy Persian.

Premium copy is:

- precise
- calm
- specific
- restrained
- free of hype

Avoid using Arabic-heavy words or English jargon to manufacture authority.

## 16. Read-aloud test

Read every important string aloud at normal speed.

Revise if:

- breathing breaks in the wrong place
- the sentence sounds translated
- the speaker would naturally choose different words
- the emphasis appears too late
- the line feels written for a brochure rather than a person

## 17. Final consistency sweep

Across one page or flow, verify:

- one formality level
- one spelling convention
- consistent digits
- consistent product names
- consistent button verbs
- consistent use of «تو» or «شما»
- no accidental switch between Persian and English labels
- no duplicate slogans competing for attention
