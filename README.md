# Job Scout (Vibecoding Project)

Goal:
Collect job postings from multiple sources, store raw data, transform it into
clean structured records, score jobs, and display them in a frontend.

Core principles:
- Database-first design
- Raw data is immutable
- Transformations are replayable
- Python-first backend
- AI-assisted parsing and scoring (MCPs)

Data flow:
Scrapers → raw_job_posts → processors → job_posts → scoring → frontend
