# ⚖️ The Cursed Code Court | محكمة الأكواد الملعونة

[English](#english) · [العربية](#العربية)

---

## English

Debugging, turned into courtroom theatre. Paste your buggy code and a ruthless **cyber-judge** roasts it, lists the charges, then locks the real fix behind a small coding **penance**. Complete the penance and the fix is revealed.

### How it works
1. Paste buggy code (Python, Java, JavaScript, C++ …) and pick the language.
2. The judge delivers a sarcastic verdict, lists the bugs, and assigns a penance (e.g. *"Write code that prints ‘I will not use global variables again’ 10 times"*).
3. You write the penance code. The judge checks it.
4. If it passes, the corrected code and an explanation are unlocked.

### Features
- Arabic and English UI with automatic RTL/LTR switching
- Works with any programming language
- Penance verified by AI, not just a button click
- Dark and light themes
- Single `index.html`, no build step

### Run / deploy
The page calls an LLM. In claude.ai it uses the built-in `sample` capability. To host it yourself (e.g. GitHub Pages) **never put an API key in the frontend**. Instead:

1. Create a tiny serverless proxy (Cloudflare Worker, Vercel, Netlify) that holds your key and forwards a prompt to your LLM provider.
2. Replace the `ask()` function in `index.html` with a `fetch("/api/judge", …)` call to that proxy.
3. Push to GitHub and enable **Pages** (Settings → Pages).

### Roadmap
- [ ] Judge severity levels (lenient / strict / merciless)
- [ ] Shareable “case files”
- [ ] Hall of Shame leaderboard
- [ ] More languages

### License
MIT

---

## العربية

عملية تصحيح الأخطاء الممِلّة تتحول إلى مسرحية في قاعة محكمة. الصق كودك المليء بالأخطاء، فيسخر منه **قاضٍ سيبراني** قاسٍ، ويعدّد التهم، ثم يقفل الحل الصحيح خلف **عقوبة برمجية** بسيطة. نفّذ العقوبة ليظهر الحل.

### كيف يعمل
1. الصق الكود واختر لغة البرمجة.
2. يصدر القاضي حكماً ساخراً، ويذكر الأخطاء، ويحدد عقوبة (مثل: *«اكتب كوداً يطبع جملة "لن أستخدم المتغيرات العامة مجدداً" 10 مرات»*).
3. تكتب كود العقوبة ويفحصه القاضي.
4. عند النجاح يظهر الكود المصحح مع الشرح.

### المميزات
- واجهة بالعربية والإنجليزية مع تبديل تلقائي للاتجاه (RTL/LTR)
- تدعم أي لغة برمجة
- العقوبة يتحقق منها الذكاء الاصطناعي فعلياً
- وضع داكن وفاتح
- ملف `index.html` واحد بدون أي خطوات بناء

### التشغيل والنشر
الصفحة تستدعي نموذج ذكاء اصطناعي. داخل claude.ai تستخدم ميزة `sample` المدمجة. عند استضافتها بنفسك (مثل GitHub Pages) **لا تضع مفتاح API في الواجهة أبداً**، بل:

1. أنشئ وسيطاً صغيراً (Cloudflare Worker أو Vercel أو Netlify) يحتفظ بالمفتاح ويمرّر الطلب لمزوّد النموذج.
2. استبدل الدالة `ask()` في `index.html` بطلب `fetch("/api/judge", …)` إلى هذا الوسيط.
3. ارفع المشروع إلى GitHub وفعّل **Pages** من الإعدادات.

### خارطة الطريق
- [ ] مستويات قسوة القاضي
- [ ] مشاركة ملفات القضايا
- [ ] لوحة «قاعة العار»
- [ ] دعم المزيد من اللغات

### الرخصة
MIT
