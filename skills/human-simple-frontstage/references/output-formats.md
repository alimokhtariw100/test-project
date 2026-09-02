# Output Formats

Choose the smallest format that completes the task. Follow the user’s requested format over these defaults.

## 1. Final-only

Use when the user asks for:

- «فقط متن»
- «فقط لیست»
- «فقط اسم‌ها»
- «مقدمه نده»
- «فقط خروجی نهایی»

Output only the requested copy. Do not explain the reasoning, tests, or alternatives.

## 2. Exact replacement

Use for implementation-ready changes to an existing interface.

```text
بخش: HERO_HEADLINE

متن فعلی:
«هوش مصنوعی را فقط یاد نگیر؛ یاد بگیر که استفاده‌اش کنی.»

جایگزین دقیق:
«قرار نیست همه‌ی هوش مصنوعی رو یاد بگیری؛ فقط چیزی که به درد تو می‌خوره.»
```

Rules:

- quote the current string exactly when provided
- provide one final replacement
- preserve required names, numbers, and conditions
- add an implementation note only when behavior or destination must also change

## 3. Compact audit

Use when the user asks what is wrong and how to fix it.

```markdown
### [Surface]

**مشکل:** [specific issue]

**اثر روی مخاطب:** [what becomes confusing, slow, risky, or untrustworthy]

**جایگزین دقیق:**
«[final copy]»
```

Do not write generic comments such as «ساده‌تر شود» without supplying the final string.

## 4. Bulk UI copy deck

Use for many strings across one page or product.

| Key / surface | Current copy | Final copy | Note |
|---|---|---|---|
| `hero_title` | ... | ... | ... |
| `primary_cta` | ... | ... | destination must be verified |

Keep keys or selectors supplied by the project. Do not invent technical IDs unless asked.

## 5. Structured copy specification

Use when handing copy to a developer or coding agent.

```text
━━━━━━━━━━━━━━━━━━
01 — HERO HEADLINE
━━━━━━━━━━━━━━━━━━

متن فعلی:
«...»

جایگزین دقیق:
«...»

رفتار:
بدون تغییر

لینک/مقصد:
/verified-route/
```

Include `رفتار` and `لینک/مقصد` only when relevant.

## 6. Variant mode

Use only when the user requests options or when a genuine strategic decision remains.

```markdown
### گزینه ۱ — مستقیم
«...»

### گزینه ۲ — گرم‌تر
«...»

### گزینه ۳ — رسمی‌تر
«...»
```

Every option must differ in strategy or tone, not just one synonym.

If one option is clearly strongest, say which one and why in one sentence unless the user requested final-only output.

## 7. Before / after demonstration

Use when teaching the simplification pattern.

```markdown
**قبل:**
«فرایند تشخیص شخصی‌سازی‌شده برای فعال‌سازی مسیر یادگیری»

**بعد:**
«چند سؤال جواب بده تا بفهمی از کجا شروع کنی.»

**چه چیزی بهتر شد:**
اصطلاح داخلی حذف شد، نتیجه برای مخاطب روشن شد، و قدم بعدی مشخص شد.
```

## 8. Form copy package

```markdown
### عنوان فرم
«...»

### توضیح کوتاه
«...»

### فیلد ۱
- Label: «...»
- Placeholder: «...»
- Help text: «...»
- Required error: «...»
- Format error: «...»

### دکمه
«...»

### پیام موفقیت
«...»

### پیام خطا
«...»
```

Do not add placeholder text when a visible label is enough. Placeholders are not replacements for labels.

## 9. Consent or privacy package

```markdown
### خلاصه ساده
«...»

### انتخاب‌ها
- قبول: «...»
- رد یا فقط ضروری: «...»
- بازکردن تنظیمات: «...»

### ادعای فنی که باید تأیید شود
- [claim]

### وضعیت
`READY` / `NEEDS POLICY OR LEGAL CONFIRMATION`
```

Never mark the copy ready when the implementation does not make the statement true.

## 10. Repository change report

After editing code, keep the report compact:

```text
COPY STATUS: PASS / FAIL
FILES CHANGED:
- ...

BEHAVIOR CHANGED: YES / NO
ROUTES VERIFIED:
- ...

UNSUPPORTED CLAIMS FOUND:
- NONE / ...

QA:
- MOBILE: PASS / FAIL
- RTL: PASS / FAIL
- LINKS: PASS / FAIL
```

Do not claim verification that was not actually performed.
