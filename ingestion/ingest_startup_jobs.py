"""
Ingestion script: ingest_startup_jobs

Purpose:
- Insert raw (unprocessed) job postings into raw_job_posts
- This version inserts a single fake job to validate the pipeline

Notes:
- We explicitly set fetched_at because PostgREST sends NULL
  if the field is omitted, which bypasses the DB default.
"""

import os
from datetime import datetime, timezone

from supabase import create_client


# -------------------------------------------------------------------
# Supabase client setup
# -------------------------------------------------------------------

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_SERVICE_ROLE_KEY = os.environ["SUPABASE_SERVICE_ROLE_KEY"]

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SERVICE_ROLE_KEY
)


# -------------------------------------------------------------------
# Ingestion logic
# -------------------------------------------------------------------

def insert_fake_raw_job():
    """
    Insert a single fake raw job posting.

    This validates:
    - Supabase connectivity
    - raw_job_posts schema
    - Insert permissions
    """

    fake_payload = {
        "html": "<html><body><h1>Senior Python Developer</h1></body></html>"
    }

    response = supabase.table("raw_job_posts").insert({
        "source": "startup.jobs",
        "source_url": "https://startup.jobs/fake-job",
        "search_query": "python developer remote",
        "raw_payload": fake_payload,
        "fetched_at": datetime.now(timezone.utc).isoformat()
    }).execute()

    print("Insert response:")
    print(response)


# -------------------------------------------------------------------
# Entry point
# -------------------------------------------------------------------

if __name__ == "__main__":
    insert_fake_raw_job()
