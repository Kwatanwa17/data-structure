# python3

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = list(zip([0] * n_workers, range(n_workers)))
    heapq.heapify(next_free_time)

    for job in jobs:
        next_worker = heapq.heappop(next_free_time)
        result.append(AssignedJob(next_worker[1], next_worker[0]))
        heapq.heappush(next_free_time, (job + next_worker[0], next_worker[1]))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
