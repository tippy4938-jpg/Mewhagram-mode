## Mewhagram v1.2.0.0 — Standalone Clone Edition 🚀

### 🇷🇺 Что нового в обновлении:
- 📱 **Полная параллельная установка (Standalone Clone):** 
  - Пакет приложения переведён на независимый идентификатор `com.mewhagram.messenger`.
  - **Теперь Mewhagram можно устанавливать рядом с официальным Telegram и exteraGram на один телефон!** Больше никакой ошибки конфликта подписи (`INSTALL_FAILED_UPDATE_INCOMPATIBLE`) — приложения живут параллельно, имеют раздельные аккаунты, настройки и базы данных.
- 🔄 **Автономные Content Providers & Authorities:**
  - `FileProvider` переведён на `com.mewhagram.messenger.provider` (исправлена отправка и открытие файлов и APK).
  - Уведомления и звуки вызовов переведены на `com.mewhagram.messenger.notification_image_provider` и `call_sound_provider`.
  - Обновлены фоновые службы и внутренние права приложения.
- 🔑 **Официальная цифровая подпись Mewhagram:**
  - APK подписан выделенным сертификатом разработчика **Mewhagram Official** (`CN=Mewhagram Official, OU=Mewha Dev, O=Mewhagram Project, C=RU`), срок действия до **2054 года**.
  - Верифицирован по всем трём современным схемам Android: **v1, v2 и v3**.
- 🎨 **Кастомные иконки:**
  - Адаптированы алиасы динамических иконок приложения на рабочем столе (`Default`, `Amethyst`, `Monet`, `Gradient`, `Sus`, `Neo` и др.).
- 🚀 **Zipalign 4-byte оптимизация:**
  - Архитектурное выравнивание всех ресурсов и `classes.dex` для быстрого холодного запуска.
- 💎 **Фирменные фичи Mewhagram:**
  - Отображение точных секунд в таймстемпах (`HH:mm:ss`);
  - Бесплатный Developer & Booster Badge в профиле;
  - Локальный Premium (все стикеры, кастомные иконки и эмодзи-статусы);
  - Адаптивные темы Monet (Material 3 AMOLED);
  - Чистый интерфейс без рекламы.

📦 **Информация о сборке:**
- Имя пакета: `com.mewhagram.messenger`
- Версия: `9.6.6` (v1.2.0.0)
- Файл: `Mewhagram.apk` (41.71 МБ)
- Архитектура: `arm64-v8a`
- Совместимость: Android 6.0+

---

### 🇬🇧 What's New:
- 📱 **Standalone Clone Edition:** 
  - Package ID changed to `com.mewhagram.messenger`.
  - Install Mewhagram side-by-side with original Telegram and exteraGram on the same device without signature conflicts.
- 🔄 **Autonomous Providers & Permissions:** 
  - Fully mapped `FileProvider`, `NotificationImageProvider`, and sound authorities to Mewhagram namespace.
- 🔑 **Official Digital Signature:** 
  - Signed with dedicated Mewhagram Official keypair (valid through 2054) via v1, v2, and v3 Android signature schemes.
- 🚀 **Zipalign Optimization:** 4-byte alignment for fast app startup and minimal memory overhead.
- 💎 **All Core Mewhagram Features:** seconds in message timestamps, dev/booster badges, local premium assets, ad-free experience.
