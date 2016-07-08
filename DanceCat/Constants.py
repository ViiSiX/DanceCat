# Project section
PROJECT_NAME = 'Dance Cat - Data Report'

# DB section
MYSQL = 1
SQLSERVER = 2

CONNECTION_TYPES_LIST = [
    (MYSQL, 'MySQL'),
    (SQLSERVER, 'SQL Server')
]

CONNECTION_TYPES_DICT = {
    MYSQL: {
        'name': 'MySQL',
        'default_port': 3306,
        'mime': 'text/x-mysql'
    },
    SQLSERVER: {
        'name': 'SQL Server',
        'default_port': 1433,
        'mime': 'text/x-mssql'
    }
}

# Job Tracking section
JOB_QUEUED = 0
JOB_RUNNING = 1
JOB_RUN_SUCCESS = 2
JOB_RUN_FAILED = 3

JOB_TRACKING_STATUS_DICT = {
    JOB_QUEUED: {
        'name': 'Queued'
    },
    JOB_RUNNING: {
        'name': 'Running'
    },
    JOB_RUN_SUCCESS: {
        'name': 'Success'
    },
    JOB_RUN_FAILED: {
        'name': 'Failed'
    }
}

# Model versions section
MODEL_ALLOWED_EMAIL_VERSION = 1
MODEL_USER_VERSION = 1
MODEL_CONNECTION_VERSION = 1
MODEL_JOB_VERSION = 1
MODEL_SCHEDULE_VERSION = 1
MODEL_TRACK_JOB_RUN_VERSION = 1

# Schedule type section
SCHEDULE_ONCE = 0
SCHEDULE_HOURLY = 1
SCHEDULE_DAILY = 2
SCHEDULE_WEEKLY = 3
SCHEDULE_MONTHLY = 4

# Socket Section
WS_QUERY_SEND = 'r_query'
WS_QUERY_RECEIVE = 's_query'
WS_TRACKERS_SEND = 's_trackers'
WS_TRACKERS_RECEIVE = 'r_trackers'
