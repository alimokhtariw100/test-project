# Test Cases

Use these cases to evaluate whether the skill preserves meaning while reducing cognitive load.

## Case 1 — Generic AI headline

**Input**

«هوش مصنوعی را فقط یاد نگیر؛ یاد بگیر که استفاده‌اش کنی.»

**Context**

A founder brand that helps people choose only the AI skills relevant to them.

**Expected direction**

«قرار نیست همه‌ی هوش مصنوعی رو یاد بگیری؛ فقط چیزی که به درد تو می‌خوره.»

**Why**

The rewrite expresses a specific brand point of view instead of a generic AI promise.

## Case 2 — Diagnostic

**Input**

«شروع فرایند تشخیص شخصی‌سازی‌شده»

**Context**

Three questions that recommend where to start.

**Expected direction**

«ببین از کجا شروع کنی»

**Failure**

«شروع تشخیص شخصی» still exposes the internal label instead of the benefit.

## Case 3 — Flagship

**Input**

«محصول پرچم‌دار ما»

**Expected direction**

«برنامه اصلی ما»

**Failure**

Using «پرچم‌دار» merely because it is a literal translation.

## Case 4 — Workflow

**Input**

«Workflow اختصاصی خود را ایجاد کنید.»

**Context**

The user is arranging three repeated work steps.

**Expected direction**

«مراحل کار خودت رو بچین.»

**Alternative for a technical audience**

«Workflow خودت رو بساز.»

## Case 5 — AI agent

**Input**

«یک AI Agent برای کسب‌وکار شما طراحی می‌کنیم.»

**Context**

The system answers common customer questions and routes requests to a human.

**Expected direction**

«یک دستیار هوش مصنوعی می‌سازیم که سؤال‌های تکراری مشتری‌ها رو جواب بده و درخواست‌های مهم رو به تیمت برسونه.»

**Why**

The task and limit are clearer than the category name.

## Case 6 — Form error

**Input**

«ورودی نامعتبر است.»

**Context**

Iranian mobile number is shorter than required.

**Expected direction**

«شماره‌ت کامل نیست. یه بار چکش کن.»

**Failure**

A vague error that forces the user to guess which field is wrong.

## Case 7 — Form success

**Input**

«عملیات با موفقیت انجام شد!»

**Context**

A consultation request was saved and the team will review it, but no exact contact time is guaranteed.

**Expected direction**

«درخواستت ثبت شد. بعد از بررسی باهات تماس می‌گیریم.»

**Failure**

«تا یک ساعت دیگه تماس می‌گیریم» when the operation cannot guarantee it.

## Case 8 — Vague CTA

**Input**

«بیشتر بدانید»

**Context**

The destination is a free video lesson.

**Expected direction**

«آموزش رو ببین»

## Case 9 — Free course CTA

**Input**

«شروع مسیر رایگان دبی»

**Context**

The button opens the free Dubai Future course.

**Expected direction**

«رایگان شروع کن»

**Implementation requirement**

Verify the destination before approval.

## Case 10 — Overloaded benefit copy

**Input**

«با بهره‌گیری از اکوسیستم یکپارچه هوش مصنوعی، بهره‌وری و خلاقیت خود را به سطح بعدی ارتقا دهید.»

**Context**

A tool turns a rough idea into a first social post draft.

**Expected direction**

«ایده‌ت رو بده؛ یک پیش‌نویس آماده برای پست تحویل بگیر.»

## Case 11 — Feature that does not exist

**Input**

«مسیر کاملاً شخصی تو در چند ثانیه آماده می‌شود.»

**Context**

The current page only has a static list of courses.

**Expected result**

Do not rewrite and publish. Mark:

`UNSUPPORTED CLAIM — FEATURE NOT IMPLEMENTED`

## Case 12 — Privacy

**Input**

«برای بهینه‌سازی تجربه کاربری از ابزارهای تحلیلی استفاده می‌کنیم.»

**Context**

The site uses GA4 and Clarity after explicit consent and does not send form text, name, or phone to them.

**Expected direction**

«با اجازه تو، آمار کلی استفاده از سایت رو بررسی می‌کنیم تا بهترش کنیم. اسم، شماره و متن فرم‌هات برای این آمار ارسال نمی‌شن.»

**Requirement**

Verify the implementation makes every sentence true.

## Case 13 — Legal condition

**Input**

«امکان بازگشت وجه تا ۷ روز، فقط در صورتی وجود دارد که کمتر از ۲۰٪ دوره مشاهده شده باشد.»

**Expected direction**

«تا ۷ روز می‌تونی درخواست بازگشت وجه بدی؛ به شرطی که کمتر از ۲۰٪ دوره رو دیده باشی.»

**Failure**

«تا ۷ روز امکان بازگشت وجه داری» because the condition was deleted.

## Case 14 — Medical uncertainty

**Input**

«این روش ممکن است در بعضی افراد به کاهش درد کمک کند، اما جای تشخیص پزشک را نمی‌گیرد.»

**Expected direction**

Keep the uncertainty and medical boundary. Do not turn «ممکن است» into certainty.

## Case 15 — Navigation label

**Input**

«منابع آموزشی تخصصی»

**Context**

A navigation link opens videos and articles.

**Expected direction**

«آموزش‌ها»

## Case 16 — Repeated brand word

**Input set**

- مسیر رایگان
- مسیر مناسب
- مسیر اصلی
- تست مسیر
- مسیر خدمات

**Expected direction**

Use different natural actions:

- «رایگان شروع کن»
- «ببین از کجا شروع کنی»
- «برنامه اصلی»
- «چند سؤال کوتاه»
- «کمک اختصاصی»

## Case 17 — Technical audience override

**Input**

«API key را در متغیر محیطی ذخیره کنید.»

**Context**

Developer documentation.

**Expected direction**

Keep `API key` and «متغیر محیطی» because the audience needs exact technical terminology. Simplicity must not erase precision.

## Case 18 — Mobile hero

**Input**

A 54-word paragraph before any CTA.

**Context**

Most visitors arrive from Instagram on 390px mobile screens.

**Expected direction**

Split into:

1. one clear headline
2. one short supporting sentence
3. one primary action

Do not preserve the paragraph merely because each sentence is grammatically simple.

## Case 19 — Social-native tone

**Input**

«خواهشمند است نوع آموزش مورد نظر خود را انتخاب نمایید.»

**Expected direction**

«بیشتر چی می‌خوای یاد بگیری؟»

**Context boundary**

Use this only when the project voice addresses the user as «تو».

## Case 20 — Exact identifiers

**Input**

«بعد از `payment_success` کاربر وارد `/onboarding/` می‌شود.»

**Expected direction**

Simplify the surrounding explanation if needed, but keep `payment_success` and `/onboarding/` exact.

## Evaluation rule

A successful output is not merely shorter. It must:

- remain true
- preserve decision-changing conditions
- sound natural in the selected register
- reveal the concrete user outcome
- make the next action clear
- fit the actual surface and audience
