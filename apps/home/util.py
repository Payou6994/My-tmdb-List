def creditHelpers(listcrew):
    priorityJobs = [
        "Director",
        "Creator",
        "Screenplay",
        "Writer",
        "Composer",
        "Editor",
        "Producer",
        "Co-Producer",
        "Executive Producer",
        "Animation",
    ]

    return sorted(
        list(filter(lambda d: d["job"] in priorityJobs, listcrew)),
        key=lambda x: priorityJobs.index(x["job"]),
    )
