# Output Formats

Choose the smallest format that satisfies the request. Do not add commentary when the user asks for copy only.

## 1. Final-only

Use when the user says:

- «فقط متن»
- «لیست فقط»
- «هیچ توضیحی نده»
- «نسخه نهایی رو بده»

Output only the requested final copy.

Example:

```text
قرار نیست همه‌ی هوش مصنوعی رو یاد بگیری.
فقط چیزی که به درد تو می‌خوره.
```

## 2. Exact replacement deck

Use for implementation-ready copy changes.

```text
━━━━━━━━━━━━━━━━━━
01 — HERO HEADLINE
━━━━━━━━━━━━━━━━━━

متن فعلی:
«هوش مصنوعی را فقط یاد نگیر؛ یاد بگیر که استفاده‌اش کنی.»

جایگزین دقیق:
«قرار نیست همه‌ی هوش مصنوعی رو یاد بگیری؛ فقط چیزی که به درد تو می‌خوره.»

نکته اجرایی:
هیچ متن دیگری به Hero اضافه نشود.
```

Include the implementation note only when it prevents a real mistake.

## 3. Compact audit

Use when the user asks what is wrong and how to fix it.

```text
مشکل:
«پیدا کردن مسیر مناسب من» مبهم است و یک قابلیت کامل شخصی‌سازی را وعده می‌دهد.

اثر روی مخاطب:
نمی‌فهمد بعد از کلیک چه اتفاقی می‌افتد.

جایگزین دقیق:
«آموزش‌ها رو ببین»
```

## 4. UI string table

Use for many interface strings or localization work.

| Key / surface | Current | Final | Note |
|---|---|---|---|
| `hero_title` | هوش مصنوعی را فقط یاد نگیر | قرار نیست همه‌ی هوش مصنوعی رو یاد بگیری | Keep to two visual lines on mobile |
| `hero_primary_cta` | شروع مسیر رایگان دبی | رایگان شروع کن | Preserve current verified URL |

Do not include internal notes in user-visible copy.

## 5. Form flow

Use one block per step.

```text
مرحله ۱
عنوان: «برای چی کمک می‌خوای؟»
گزینه‌ها:
- مشاوره
- آموزش اختصاصی

مرحله ۲
عنوان: «الان چقدر با AI آشنایی؟»
گزینه‌ها:
- تازه شروع کردم
- یه چیزهایی بلدم
- حرفه‌ای‌ترم

مرحله ۳
عنوان: «چطور باهات تماس بگیریم؟»
فیلدها:
- نام و نام خانوادگی
- شماره موبایل

دکمه:
«ارسال درخواست»

پیام موفقیت:
«درخواستت ثبت شد. بعد از بررسی باهات تماس می‌گیریم.»
```

## 6. Error and recovery set

```text
حالت: شماره ناقص
پیام: «شماره‌ت کامل نیست. یه بار چکش کن.»
اقدام: فوکوس روی فیلد شماره

حالت: قطع ارتباط
پیام: «اتصال قطع شد. دوباره تلاش کن.»
دکمه: «دوباره تلاش کن»

حالت: ثبت موفق
پیام: «درخواستت ثبت شد. بعد از بررسی باهات تماس می‌گیریم.»
```

## 7. Variants with a decision

Only use when the user asks for options or a real strategic choice remains.

```text
گزینه ۱ — مستقیم
«رایگان شروع کن»
مناسب وقتی مقصد بلافاصله آموزش رایگان را باز می‌کند.

گزینه ۲ — نتیجه‌محور
«اولین آموزش رو ببین»
مناسب وقتی مقصد صفحه فهرست نیست و درس اول را باز می‌کند.

پیشنهاد نهایی:
«رایگان شروع کن»
چون هم کوتاه‌تر است، هم مقصد فعلی را دقیق توصیف می‌کند.
```

Do not produce cosmetic variants that differ by one synonym.

## 8. Backstage-to-frontstage translation

```text
اصطلاح داخلی:
`diagnostic_complete`

معنی برای تیم:
کاربر به آخرین سؤال رسیده و نتیجه آماده شده است.

متن برای مخاطب:
این اصطلاح نباید در رابط دیده شود.
عنوان مناسب صفحه نتیجه:
«این شروع برای تو مناسب‌تره.»
```

## 9. Content hierarchy

Use when the user gives a long paragraph that needs layering.

```text
عنوان:
«از بین این همه ابزار، کدوم به درد تو می‌خوره؟»

توضیح کوتاه:
«چند سؤال جواب بده تا شروع مناسب خودت رو پیدا کنی.»

جزئیات اختیاری:
«جوابت فقط برای پیشنهاد شروع بهتر استفاده می‌شه.»

دکمه:
«شروع سؤال‌ها»
```

## 10. Verification-required output

When the copy depends on an unverified product fact:

```text
نسخه پیشنهادی، مشروط به تأیید دسترسی فوری:
«بعد از پرداخت، همون لحظه وارد دوره می‌شی.»

نیاز به تأیید:
آیا دسترسی واقعاً خودکار و فوری است؟

نسخه امن تا قبل از تأیید:
«بعد از پرداخت، اطلاعات دسترسی برات نمایش داده می‌شه.»
```

Do not silently choose the more persuasive claim.

## 11. Social-native copy

Use short lines and spoken rhythm, but keep the meaning exact.

```text
مشکل این نیست که AI بلد نیستی.

مشکل اینه که نمی‌دونی
دقیقاً چی رو باید یاد بگیری.

و مهم‌تر:
چی رو اصلاً نباید یاد بگیری.
```

Do not apply social line breaks to legal, payment, or dense instructional copy.

## 12. Repository-ready report

```text
COPY SCOPE:
Homepage visible strings only

CHANGED:
- Hero headline
- Hero supporting text
- Primary and secondary CTA labels
- Founder introduction

PRESERVED:
- Routes
- IDs
- Form field names
- Analytics event names
- Backend payload keys

VERIFICATION NEEDED:
- Dubai Future CTA returns HTTP 200

OUT OF SCOPE:
- Layout redesign
- Analytics implementation
- Backend refactor
```

## Final formatting rule

Match the user's requested language, length, and structure. The format is a tool, not a ritual. If a one-line answer is enough, do not use a table.
