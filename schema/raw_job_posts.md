Purpose:
Store raw, unprocessed job data exactly as fetched from external sources.

Characteristics:
- Append-only
- Never updated or deleted
- Used as the single source of truth for reprocessing

Fields:
- id: UUID primary key
- source: text (linkedin | google | startup.jobs)
- source_job_id: optional text
- source_url: text
- search_query: text
- raw_payload: json
- fetched_at: timestamp with timezone

Indexes:
- source
- fetched_at

Rules:
- This table is append-only
- No updates or deletes are allowed
- Data here must never be modified after insertion
- All transformations must write to derived tables