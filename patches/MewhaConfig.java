package org.telegram.messenger;

import android.content.Context;
import android.content.SharedPreferences;

/**
 * 🐾 MewhaConfig
 * Centralized configuration & toggles for Mewhagram client features.
 */
public class MewhaConfig {

    private static final String PREFS_NAME = "mewhaconfig";
    private static SharedPreferences preferences;

    // Feature toggles
    public static boolean showSeconds = true;
    public static boolean fakePremium = true;
    public static boolean customBranding = true;
    public static boolean expandedLimits = true;

    // Signature Mewha color palette
    public static final int COLOR_MEWHA_PINK = 0xFFD81B60;    // Deep vibrant pink
    public static final int COLOR_MEWHA_PURPLE = 0xFF8E24AA;  // Rich purple

    /**
     * Initializes config from SharedPreferences.
     */
    public static void loadConfig(Context context) {
        if (context == null) return;
        if (preferences == null) {
            preferences = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);
        }
        showSeconds = preferences.getBoolean("showSeconds", true);
        fakePremium = preferences.getBoolean("fakePremium", true);
        customBranding = preferences.getBoolean("customBranding", true);
        expandedLimits = preferences.getBoolean("expandedLimits", true);
    }

    public static void setShowSeconds(boolean value) {
        showSeconds = value;
        if (preferences != null) {
            preferences.edit().putBoolean("showSeconds", value).apply();
        }
    }

    public static void setFakePremium(boolean value) {
        fakePremium = value;
        if (preferences != null) {
            preferences.edit().putBoolean("fakePremium", value).apply();
        }
    }

    public static void setExpandedLimits(boolean value) {
        expandedLimits = value;
        if (preferences != null) {
            preferences.edit().putBoolean("expandedLimits", value).apply();
        }
    }

    public static boolean isFakePremiumEnabled() {
        return fakePremium;
    }

    public static boolean isShowSecondsEnabled() {
        return showSeconds;
    }

    public static boolean isExpandedLimitsEnabled() {
        return expandedLimits;
    }
}
