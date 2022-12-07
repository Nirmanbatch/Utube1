import os


class Config:

    BOT_TOKEN ="5881003026:AAHFiFQK71adFiUYatOyeC-Pk8afim4CrhA")

    SESSION_NAME ="NT_Utube_uploads_bot")

    API_ID = int(os.environ.get("API_ID"))

    API_HASH ="11619862")

    CLIENT_ID ="http://491277194702-7519gk437d7vvt6cumupgikqs367fsi2.apps.googleusercontent.com")

    CLIENT_SECRET ="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")

    BOT_OWNER ="5028339608"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
