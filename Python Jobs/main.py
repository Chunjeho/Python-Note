from indeed_extract import get_jobs as indeed_get_jobs
from stackoverflow_extract import get_jobs as so_get_jobs
from save import save_to_file

indeed_jobs = indeed_get_jobs()
so_jobs = so_get_jobs()

jobs = indeed_jobs + so_jobs
save_to_file(jobs)
