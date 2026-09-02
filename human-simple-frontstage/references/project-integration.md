# ادغام با پروژه، Codebase و Skillهای دیگر

این فایل مشخص می‌کند Human-Simple Frontstage هنگام کار در پروژه واقعی چطور با Brand docs، Code، Design، UX Writing، RTL و QA هماهنگ شود.

---

## 1. ترتیب منابع حقیقت

قبل از تغییر Copy این ترتیب را رعایت کن:

1. رفتار واقعی Product و Code
2. قوانین حقوقی، امنیتی و ایمنی
3. اسناد Locked یا Source of Truth پروژه
4. Brand voice و Audience definition
5. درخواست صریح کاربر
6. Human-Simple Frontstage
7. Skillهای عمومی UX/Design

Skill عمومی حق ندارد تصمیم قفل‌شده پروژه را عوض کند.

---

## 2. شروع کار در Repository

قبل از نوشتن:

1. فایل شروع پروژه را پیدا کن: `START_HERE`, `README`, `CLAUDE.md`, `AGENTS.md`, handoff یا معادل آن.
2. اسناد Brand، Copy، Product، Route و Current State را بخوان.
3. فایل یا Component واقعی متن را پیدا کن.
4. Route، CTA، Form behavior و Backend contract را بررسی کن.
5. وضعیت Production و Git را قاطی نکن.
6. مشخص کن Task فقط Copy است یا اجازه تغییر Layout/Behavior هم دارد.

اگر فایل مرجع وجود دارد، از حافظه یا حدس جای آن تصمیم نگیر.

---

## 3. مرز Copy-only

وقتی Task فقط اصلاح متن است:

### مجاز

- Text node
- Label
- Placeholder
- Help text
- Error copy
- Success copy
- Heading
- Meta description، اگر در Scope است
- Alt text، اگر در Scope است و تصویر مشخص است

### غیرمجاز مگر با اجازه

- تغییر Route
- تغییر ID
- تغییر Form field name
- تغییر Analytics event
- حذف Element
- تغییر CSS/Layout
- تغییر Backend
- ساخت Feature
- تغییر Validation logic

اگر متن جدید بدون تغییر رفتار گمراه‌کننده می‌شود، آن را `BLOCK` کن یا Scope اضافه بخواه.

---

## 4. هماهنگی با `ux-writing`

ترتیب پیشنهادی:

```text
Human-Simple Frontstage
→ مفهوم را قابل‌فهم می‌کند
→ اصطلاح پشت‌صحنه را به سؤال واقعی مخاطب تبدیل می‌کند

UX Writing
→ Microcopy را برای Surface دقیق می‌کند
→ طول، Tone، Error pattern و Accessibility را پولیش می‌کند
```

اگر تعارض بود:

- معنی و صداقت از Human-Simple Frontstage حفظ شود.
- استاندارد Surface از UX Writing استفاده شود.
- Brand docs بالاتر از هر دو هستند.

مثال:

Backstage:
`Submit lead qualification form`

Human-Simple:
«درخواستت رو بفرست»

UX Writing polish بسته به مرحله:
«ارسال درخواست»

---

## 5. هماهنگی با Skillهای Design

Skill طراحی می‌تواند Hierarchy، Layout و Visual treatment پیشنهاد دهد، اما نباید خودش Copy جدید Generic بسازد وقتی متن قفل شده است.

ترتیب:

```text
Message hierarchy
→ Human-simple copy
→ Design placement
→ Mobile visual QA
```

نه:

```text
Template section
→ پرکردن با متن Generic
```

قواعد:

- برای جا شدن متن، فونت را بیش از حد کوچک نکن.
- اگر Heading در موبایل بد می‌شکند، ابتدا Copy و عرض را بررسی کن.
- Design نباید اصطلاح داخلی را فقط برای جذابیت بصری وارد Frontstage کند.
- Badge، Eyebrow و Section label فقط وقتی بمانند که معنی اضافه می‌کنند.
- Visual creativity نباید فهم را کم کند.

---

## 6. هماهنگی با `i18n-rtl-audit`

بعد از نهایی‌شدن Copy:

- `lang="fa"` و `dir="rtl"` را بررسی کن.
- متن‌های انگلیسی، Code، URL و عددهای فنی را از نظر BiDi چک کن.
- Line breakهای Hero را در عرض‌های 360، 375، 390 و 430 بررسی کن.
- Placeholder و Error message را روی Mobile واقعی یا شبیه‌ساز تست کن.
- از بریدن متن، Overflow، ترتیب غلط آیکون و Label و جابه‌جایی علامت‌ها جلوگیری کن.

Human-Simple Frontstage متن را می‌سازد؛ RTL Audit Render نهایی را بررسی می‌کند.

---

## 7. هماهنگی با QA

### `broken-link-scan`

قبل از نوشتن CTA مطمئن شو Destination وجود دارد.

بد:

«آموزش رو ببین» → 404

در چنین حالت:

- CTA را پنهان یا Deferred کن، اگر Scope اجازه دارد.
- یا متن غیرعملی نساز.
- Issue را واضح گزارش کن.

### `form-validation-scan`

بررسی کن:

- Copy خطا با Validation واقعی یکی است.
- Field اختیاری اشتباهی ضروری معرفی نشده.
- Success message قبل از تأیید Backend نشان داده نمی‌شود.
- Duplicate، Network error و invalid input متن واقعی دارند.

### `diff-risk-review`

قبل از Commit:

- Copy change نباید Handler، Route، ID یا Contract را شکسته باشد.
- Escape character، Quote و Template string را بررسی کن.
- تغییرات نامرتبط را جدا کن.

### `secret-scan`

Copy، Screenshot، Example و Doc نباید Secret واقعی را افشا کند.

### `cookie-privacy-scan`

Privacy copy باید با رفتار واقعی Trackerها و Consent هماهنگ باشد. متن ساده جای Verification فنی را نمی‌گیرد.

---

## 8. رفتار واقعی CTA

برای هر CTA این چهار مورد را ثبت یا بررسی کن:

1. Label
2. Destination یا Action
3. Preconditions
4. Success/failure behavior

مثال:

```text
Label: رایگان شروع کن
Destination: /free/dubai-ai-certificate/
Precondition: none
Expected: HTTP 200, normal navigation
```

اگر Destination نامعلوم است، Copy را Final اعلام نکن.

---

## 9. فرم و Backend contract

قبل از تغییر Label یا Question:

- Field key را پیدا کن.
- Required/optional بودن را بررسی کن.
- نوع داده را بررسی کن.
- Validation client و server را مقایسه کن.
- پیام Telegram/Email/CRM را بررسی کن، اگر وجود دارد.
- مطمئن شو تغییر Copy معنی پاسخ ذخیره‌شده را عوض نمی‌کند.

مثال:

اگر Field فنی `goal` فقط مقادیر مشخص می‌پذیرد، متن Optionها می‌تواند ساده شود اما `value` بدون هماهنگی Backend تغییر نکند.

```html
<option value="private_training">آموزش اختصاصی</option>
```

Text قابل تغییر است؛ `value` Contract است.

---

## 10. Featureهای نساخته

وجود Mockup، متن قدیمی، TODO یا Route مرده دلیل فعال‌بودن Feature نیست.

قبل از Copy:

- Code path را Verify کن.
- Production status را Verify کن، اگر Task درباره Live site است.
- Source-of-truth را بخوان.

ممنوع:

- «نتیجه شخصی تو آماده است» وقتی سیستم نتیجه نمی‌سازد
- «همین حالا خرید کن» وقتی Checkout فعال نیست
- «ویدیو رو ببین» وقتی Embed یا Route 404 است
- «تا ۲۴ ساعت تماس می‌گیریم» وقتی SLA تأیید نشده

---

## 11. Git و Commit

Copy change را Reviewable نگه دار.

ترجیح:

```text
copy(homepage): align frontstage language with locked positioning
```

یا:

```text
copy(forms): simplify consultation labels and error messages
```

از مخلوط‌کردن این‌ها در یک Commit دوری کن:

- Copy rewrite
- Analytics implementation
- Backend refactor
- Design overhaul
- Documentation migration

مگر اینکه واقعاً یک تغییر اتمیک و جدانشدنی باشند.

---

## 12. Handoff

در پایان کار Repository-ready ثبت کن:

- کدام متن‌ها عوض شدند
- کدام متن‌ها به دلیل Fact/Feature باز ماندند
- چه Route یا رفتارهایی Verify شدند
- چه چیزهایی عمداً تغییر نکردند
- آیا Mobile/RTL/Form QA انجام شد
- Commit hash

Handoff نباید فقط بگوید «Copy improved».

---

## 13. حالت چند Agent

وقتی Claude، Codex یا انسان‌ها نوبتی کار می‌کنند:

- تصمیم Copy را در Canonical doc ذخیره کن.
- فقط به حافظه چت تکیه نکن.
- Current State و Next Steps را Update کن.
- Agent بعدی باید بتواند بدون چت قبلی ادامه دهد.
- متن قفل‌شده را با برچسبی مثل `LOCKED COPY` مشخص کن، اگر سیستم پروژه چنین قراردادی دارد.

---

## 14. حالت Design + Copy

اگر Task هم‌زمان Design و Copy است:

1. Audience و Purpose را قفل کن.
2. Message hierarchy را بنویس.
3. Copy نهایی را با این Skill تولید کن.
4. Layout را با Skill طراحی بساز.
5. Mobile و RTL را تست کن.
6. CTA، Form و Route را Verify کن.
7. Diff risk را بررسی کن.

Copy را بعد از Design به‌عنوان Filler تولید نکن.

---

## 15. حالت Copy Audit بدون Write

اگر کاربر Audit خواسته:

- فایل را تغییر نده.
- Findingها را با Location دقیق بنویس.
- جایگزین دقیق بده.
- Severity را فقط در صورت نیاز اضافه کن.
- تفاوت Source code و Production را روشن نگه دار.

---

## 16. الگوی Preflight

قبل از Edit:

```text
SOURCE OF TRUTH READ: YES / NO
AUDIENCE KNOWN: YES / NO
SURFACE KNOWN: YES / NO
BEHAVIOR VERIFIED: YES / NO
COPY-ONLY SCOPE: YES / NO
OPEN FACTS: ...
```

این Preflight لازم نیست همیشه به کاربر نشان داده شود؛ اما باید در تصمیم‌گیری انجام شود.

---

## 17. الگوی Postflight

```text
MEANING PRESERVED: PASS / FAIL
UNSUPPORTED CLAIMS: NONE / ...
ROUTES VERIFIED: PASS / NOT IN SCOPE
FORM CONTRACT PRESERVED: PASS / NOT IN SCOPE
RTL/MOBILE REVIEW: PASS / NOT RUN
COPY LOCKED: YES / NO
```

---

## اصل پایانی

> Code می‌گوید چه چیزی واقعاً کار می‌کند.
>
> Brand می‌گوید چگونه باید فهمیده شود.
>
> Human-Simple Frontstage فاصله این دو را برای مخاطب قابل‌فهم می‌کند.
