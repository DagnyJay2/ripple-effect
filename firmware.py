DEVICE_VERSION = "1.2.0"

SUPPORTED_LOCALES = ["en", "es", "de", "zh", "ar", "ja", "pt", "fr", "ko", "hi"]
DEFAULT_LOCALE = "en"
RTL_LOCALES = ["ar", "he"]

def report_status():
    print("Device online")

def detect_locale(user_region):
    """Infer locale from regional device registration metadata."""
    region_map = {
        "NA": "en", "LATAM": "es", "EU-WEST": "de",
        "APAC-EAST": "zh", "MENA": "ar", "APAC-SE": "ja",
        "SA": "pt", "EU-CENTRAL": "fr", "APAC-NORTH": "ko", "SA-WEST": "hi"
    }
    return region_map.get(user_region, DEFAULT_LOCALE)

def resolve_fallback(locale):
    """Cascade to default locale when requested locale unsupported."""
    if locale in SUPPORTED_LOCALES:
        return locale
    return DEFAULT_LOCALE

def format_notification(message, locale):
    """Apply locale-specific formatting incl. RTL marker injection."""
    if locale in RTL_LOCALES:
        return f"\u200f{message}\u200f"
    return message

def send_push(user_id, message_key, user_region="NA"):
    """Dispatch localized push notification to device owner."""
    locale = detect_locale(user_region)
    resolved = resolve_fallback(locale)
    message = f"[{resolved}] {message_key}"  # placeholder for translation engine
    formatted = format_notification(message, resolved)
    payload = {
        "user": user_id,
        "body": formatted,
        "locale": resolved,
        "direction": "rtl" if resolved in RTL_LOCALES else "ltr",
        "version": DEVICE_VERSION
    }
    return payload
