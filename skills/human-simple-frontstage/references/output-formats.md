# Output Formats

Follow the format the user requests. Use these templates only when the user has not supplied a stricter format.

## Final-only

Use when the user says «فقط متن»، «فقط اسم‌ها»، «مقدمه نده»، or equivalent.

Output only the finished copy. Do not explain the reasoning or add alternatives.

## Exact replacement

Use for implementation-ready copy changes:

```text
متن فعلی:
«[current copy]»

جایگزین دقیق:
«[final copy]»
```

When several strings are involved, number them by visible section or stable key.

## Compact audit

```text
مشکل:
[what prevents understanding or action]

اثر روی مخاطب:
[what the user may misunderstand or fail to do]

جایگزین دقیق:
«[final copy]»
```

Keep the explanation short unless the user asks for a full analysis.

## Bulk UI copy deck

| بخش یا کلید | متن فعلی | متن نهایی | نکته اجرا |
|---|---|---|---|
| hero_title | ... | ... | Preserve existing line emphasis |
| primary_cta | ... | ... | Verify destination before publishing |

Use implementation notes only when they prevent a bug or inaccurate promise.

## Code-key mapping

Use when a developer needs stable strings:

```yaml
hero:
  eyebrow: "هوش مصنوعی، به زبان آدمیزاد."
  title: "قرار نیست همه‌ی هوش مصنوعی رو یاد بگیری."
  emphasis: "فقط چیزی که به درد تو می‌خوره."
  primary_cta: "رایگان شروع کن"
```

Do not rename keys unless asked. Change visible values only.

## Variants

Provide variants only when the user requests options or a real strategic decision remains.

```text
گزینه ۱ — مستقیم
«...»

گزینه ۲ — گرم‌تر
«...»

گزینه ۳ — رسمی‌تر
«...»
```

Each option must differ in strategy or tone, not just one adjective.

## Form flow

```text
مرحله ۱
عنوان: «...»
سؤال: «...»
گزینه‌ها:
- «...»
- «...»
دکمه: «...»

خطا:
«...»

موفقیت:
«...»
```

## Consent or privacy copy

Separate the human summary from the full legal destination:

```text
متن ساده:
«...»

انتخاب‌ها:
«موافقم»
«فقط ضروری»

لینک تکمیلی:
«حریم خصوصی»
```

State only what the implementation can prove.

## Educational explanation

```text
اصل موضوع:
[one simple sentence]

مثال:
[one familiar example]

کاری که الان انجام بده:
[one concrete action]
```

## Review verdict

When asked to approve copy:

```text
وضعیت: PASS / NEEDS CHANGES

ایرادهای ضروری:
1. ...
2. ...

نسخه نهایی:
«...»
```

Do not manufacture issues merely to look thorough.
