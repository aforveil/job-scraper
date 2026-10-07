import os
from dotenv import load_dotenv

load_dotenv()

# --- DO NOT MODIFY THE BELOW SECTION ---

# =================================================================
# 1. CORE SYSTEM CONFIGURATION (Do Not Modify)
# =================================================================
SUPABASE_URL: str = os.environ.get("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
SUPABASE_TABLE_NAME: str = "jobs"
SUPABASE_CUSTOMIZED_RESUMES_TABLE_NAME = "customized_resumes"
SUPABASE_STORAGE_BUCKET="personalized_resumes"
SUPABASE_RESUME_STORAGE_BUCKET="resumes"
SUPABASE_BASE_RESUME_TABLE_NAME = "base_resume"
BASE_RESUME_PATH = "resume.json"

# API keys — set only the key(s) needed for your chosen provider.
LLM_API_KEY = os.environ.get("LLM_API_KEY") or os.environ.get("GEMINI_API_KEY") or os.environ.get("GEMINI_FIRST_API_KEY")

# =================================================================
# 2. USER PREFERENCES (Editable)
# =================================================================

# --- LLM Settings ---
# Use any model supported by LiteLLM (gemini, openai/gpt-4o-mini, groq/llama-3.3-70b-versatile)
# Full list of supported models & naming: https://docs.litellm.ai/docs/providers
LLM_MODEL = "gemini"

# --- LinkedIn Search Configuration ---
LINKEDIN_SEARCH_QUERIES = [
    # 1. Les cibles directes Sales / B2B
    "alternance commercial",
    "alternance business developer",
    "alternance developpement commercial",
    "alternance commercial b2b",
    
    # 2. Les intitulés PME & Industrie très fréquents dans le 54 (Toul, Pompey, Lunéville)
    "alternance charge d affaires",
    "alternance technico commercial",
    "alternance assistant commercial",
    "alternance export",
    
    # 3. Le mot-clé pour chopper les offres rédigées par des RH à l'ancienne
    "apprentissage commercial"
]

LINKEDIN_LOCATION = "Nancy, Grand Est, France"
LINKEDIN_GEO_ID = ""           # Laissé vide exprès : LinkedIn prend Nancy et applique son rayon auto de 40 km
LINKEDIN_JOB_TYPE = ""         # Laisse vide : prend apprentissage, pro, stage, temps plein
LINKEDIN_JOB_POSTING_DATE = "r604800"  # Offres des 7 derniers jours (la fraîcheur absolue)
LINKEDIN_F_WT = ""             # Présentiel, hybride et remote acceptés


# --- Processing Limits ---
SCRAPING_SOURCES = ["linkedin"]

# On débride le scoring pour que l'IA note un gros paquet d'offres par passage
JOBS_TO_SCORE_PER_RUN = 25
JOBS_TO_CUSTOMIZE_PER_RUN = 1

# C'EST ICI LE DÉBRIDAGE : on passe de 2 à 10 offres traitées par mot-clé
MAX_JOBS_PER_SEARCH = {
    "linkedin": 10,
    "careers_future": 10,
}

# =================================================================
# 3. ADVANCED SYSTEM SETTINGS (Modify with Caution)
# =================================================================
LLM_MAX_RPM = 10
LLM_MAX_RETRIES = 3
LLM_RETRY_BASE_DELAY = 10
LLM_DAILY_REQUEST_BUDGET = 0
LLM_REQUEST_DELAY_SECONDS = 8

LINKEDIN_MAX_START = 1 
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 15

JOB_EXPIRY_DAYS = 30
JOB_CHECK_DAYS = 3
JOB_DELETION_DAYS = 60
JOB_CHECK_LIMIT = 50
ACTIVE_CHECK_TIMEOUT = 20
ACTIVE_CHECK_MAX_RETRIES = 2
ACTIVE_CHECK_RETRY_DELAY = 10
