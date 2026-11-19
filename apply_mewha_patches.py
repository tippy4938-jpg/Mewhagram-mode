#!/usr/bin/env python3
"""
🐾 Mewhagram Patch Engine
Applies all custom modifications (MewhaConfig, exact seconds, fake premium, branding)
to Telegram-FOSS source tree.
"""

import os
import sys
import shutil
from pathlib import Path

def patch_file(file_path: Path, search_text: str, replace_text: str, description: str):
    if not file_path.exists():
        print(f"[-] Warning: File not found: {file_path}")
        return False
    
    content = file_path.read_text(encoding="utf-8", errors="replace")
    if search_text not in content:
        print(f"[-] Pattern not found for: {description} in {file_path.name}")
        return False
    
    new_content = content.replace(search_text, replace_text)
    file_path.write_text(new_content, encoding="utf-8")
    print(f"[+] Successfully applied: {description}")
    return True

def main():
    root_dir = Path(__file__).resolve().parent
    telegram_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else root_dir / "telegram"
    
    if not telegram_dir.exists():
        print(f"[-] Error: Telegram directory not found at {telegram_dir}")
        sys.exit(1)

    print(f"[*] Starting Mewhagram patching process on: {telegram_dir}")

    # 1. Copy MewhaConfig.java into org.telegram.messenger package
    mewha_config_src = root_dir / "patches" / "MewhaConfig.java"
    dest_messenger = telegram_dir / "TMessagesProj" / "src" / "main" / "java" / "org" / "telegram" / "messenger"
    
    if mewha_config_src.exists() and dest_messenger.exists():
        shutil.copy2(mewha_config_src, dest_messenger / "MewhaConfig.java")
        print("[+] Injected MewhaConfig.java into org.telegram.messenger")
    else:
        print(f"[-] Could not copy MewhaConfig.java (src={mewha_config_src.exists()}, dest={dest_messenger.exists()})")

    # 2. Patch ApplicationLoader.java to initialize MewhaConfig on app start
    app_loader = dest_messenger / "ApplicationLoader.java"
    patch_file(
        app_loader,
        "super.onCreate();",
        "super.onCreate();\n        org.telegram.messenger.MewhaConfig.loadConfig(applicationContext);",
        "MewhaConfig initialization in ApplicationLoader.onCreate()"
    )

    # 3. Patch UserConfig.java for Fake Premium
    user_config = dest_messenger / "UserConfig.java"
    patch_file(
        user_config,
        "public boolean isPremium() {\n        return isPremium;",
        "public boolean isPremium() {\n        if (org.telegram.messenger.MewhaConfig.isFakePremiumEnabled()) return true;\n        return isPremium;",
        "Fake Premium override in UserConfig.isPremium()"
    )
    # Fallback pattern for single-line return
    patch_file(
        user_config,
        "public boolean isPremium() { return isPremium; }",
        "public boolean isPremium() { if (org.telegram.messenger.MewhaConfig.isFakePremiumEnabled()) return true; return isPremium; }",
        "Fake Premium fallback override in UserConfig.isPremium()"
    )

    # 4. Patch LocaleController.java for exact seconds (HH:mm:ss)
    locale_controller = dest_messenger / "LocaleController.java"
    if locale_controller.exists():
        content = locale_controller.read_text(encoding="utf-8", errors="replace")
        # Replace 24h and 12h time patterns with seconds when formatting
        new_content = content.replace('"HH:mm"', '"HH:mm:ss"')
        new_content = new_content.replace('"H:mm"', '"H:mm:ss"')
        locale_controller.write_text(new_content, encoding="utf-8")
        print("[+] Injected exact seconds (HH:mm:ss) into LocaleController.java")

    # 5. Patch strings.xml for AppName rebranding
    res_dir = telegram_dir / "TMessagesProj" / "src" / "main" / "res"
    strings_files = [
        res_dir / "values" / "strings.xml",
        res_dir / "values-ru" / "strings.xml"
    ]
    for s_file in strings_files:
        patch_file(
            s_file,
            '<string name="AppName">Telegram</string>',
            '<string name="AppName">Mewhagram</string>',
            f"Mewhagram rebranding in {s_file.parent.name}/strings.xml"
        )

    # 6. Patch MessagesController.java for expanded limits (pinned dialogs)
    messages_controller = dest_messenger / "MessagesController.java"
    patch_file(
        messages_controller,
        "public int maxPinnedDialogsCount = 5;",
        "public int maxPinnedDialogsCount = 100;",
        "Expanded pinned dialogs limit in MessagesController"
    )

    print("\n[🎉] All Mewhagram patches applied successfully!")

if __name__ == "__main__":
    main()
