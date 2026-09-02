# Examples

Use these examples to learn the transformation pattern. Do not copy them blindly into unrelated brands.

## 1. Generic hero to distinct promise

**Input**

«هوش مصنوعی را فقط یاد نگیر؛ یاد بگیر که استفاده‌اش کنی.»

**Problem**

Clear enough, but generic and usable by almost any AI educator.

**Output for a brand whose promise is selective learning**

«قرار نیست همه‌ی هوش مصنوعی رو یاد بگیری؛ فقط چیزی که به درد تو می‌خوره.»

**Why**

The sentence expresses a distinct point of view and reduces the audience’s real overload.

---

## 2. Internal product language

**Input**

«تشخیص مسیر شخصی‌سازی‌شده را آغاز کنید.»

**Output**

«ببین از کجا شروع کنی.»

**Why**

The user cares about the result, not the internal mechanism.

---

## 3. Vague CTA

**Input**

«بیشتر بدانید»

**Destination**

A free video lesson.

**Output**

«آموزش رو ببین»

---

## 4. Form label

**Input**

«نوع سرویس مورد تقاضا را انتخاب نمایید.»

**Output**

«برای چی کمک می‌خوای؟»

**Options**

- «مشاوره»
- «آموزش اختصاصی»

---

## 5. Error message

**Input**

«خطا در اعتبارسنجی شماره همراه.»

**Output**

«شماره‌ت کامل نیست. یه بار چکش کن.»

Use a more formal version when the surface requires it:

«شماره تماس کامل نیست. لطفاً دوباره بررسی کنید.»

---

## 6. Success message

**Input**

«عملیات با موفقیت انجام شد!»

**Known behavior**

The team reviews requests and calls later, with no guaranteed time.

**Output**

«درخواستت ثبت شد. بعد از بررسی باهات تماس می‌گیریم.»

---

## 7. Feature dump to outcome

**Input**

«پلتفرم مجهز به اتوماسیون، ورک‌فلوهای هوشمند و ایجنت‌های اختصاصی.»

**Output when the actual feature is proven**

«کارهای تکراری کسب‌وکارت رو به یک دستیار هوش مصنوعی بسپار.»

**Caution**

Do not use this output if the product does not really provide that assistant.

---

## 8. Privacy copy

**Input**

«برای بهبود تجربه کاربری از ابزارهای آنالیتیکس استفاده می‌کنیم.»

**Verified implementation**

The site collects page and click statistics only after consent, and does not send form names or phone numbers to analytics vendors.

**Output**

«برای بهتر کردن سایت، با اجازه تو آمار کلی استفاده از سایت رو بررسی می‌کنیم. اسم، شماره و متن فرم‌هات برای این آمار ارسال نمی‌شن.»

**Important**

If the implementation does not support this claim, change the implementation or the copy.

---

## 9. Educational explanation

**Input**

«Prompt engineering is the process of optimizing instructions to achieve higher-quality model responses.»

**Output**

«پرامپت‌نویسی یعنی درخواستت رو طوری به AI بگی که دقیق‌تر بفهمه چه خروجی‌ای می‌خوای.»

**Example**

«به‌جای “یه عکس خوب بساز”، بگو سوژه، نور، زاویه و حال‌وهوای تصویر چی باشه.»

---

## 10. Preserve an important condition

**Input**

«پس از بررسی درخواست و در صورت مناسب‌بودن شرایط، تیم با شما تماس می‌گیرد.»

**Bad simplification**

«با شما تماس می‌گیریم.»

**Why it fails**

It removes the review condition and turns a possibility into a promise.

**Better**

«درخواستت رو بررسی می‌کنیم؛ اگر این خدمت برات مناسب باشه، باهات تماس می‌گیریم.»

---

## 11. Avoid childish simplification

**Input**

«این ابزار امکان ساخت گردش‌کار خودکار را فراهم می‌کند.»

**Too childish**

«یه ربات کوچولو همه کاراتو می‌کنه.»

**Better**

«می‌تونی کارهای تکراری رو طوری بچینی که خودکار انجام بشن.»

---

## 12. Repetition becoming a buzzword

**Input page vocabulary**

- مسیر رایگان
- مسیر مناسب
- تست مسیر
- مسیر اصلی
- مسیر فارسی
- مسیر تخصصی

**Problem**

A meaningful brand word has become noise.

**Output strategy**

Keep «مسیر» only where it names the real product or decision. Replace the rest with:

- «رایگان شروع کن»
- «ببین از کجا شروع کنی»
- «آموزش رو ببین»
- «قدم بعدی»
- «کمک اختصاصی»

---

## 13. Exact replacement mode

**User request**

«کلی نگو؛ بگو این متن با چی عوض بشه.»

**Output**

```text
متن فعلی:
«هوش مصنوعی را فقط یاد نگیر؛ یاد بگیر که استفاده‌اش کنی.»

جایگزین دقیق:
«قرار نیست همه‌ی هوش مصنوعی رو یاد بگیری؛ فقط چیزی که به درد تو می‌خوره.»
```

Do not add a redesign lecture when the user asked for exact copy replacement.
